import { useEffect, useRef, ReactElement } from 'react';
import { Streamlit, withStreamlitConnection, ComponentProps } from 'streamlit-component-lib';
import debounce from 'lodash.debounce';
import imageCompression from 'browser-image-compression';

// Import Crepe properly according to docs
import { Crepe } from '@milkdown/crepe';
import '@milkdown/crepe/theme/common/style.css';
import '@milkdown/crepe/theme/frame.css';
import './style.css';

// Fast image compression using browser-image-compression
async function compressImageFast(file: File): Promise<File> {
    try {
        const options = {
            maxSizeMB: 0.5,          // Max 500KB
            maxWidthOrHeight: 800,   // Max 800px
            useWebWorker: true,      // Use Web Worker to avoid blocking UI
            quality: 0.8,            // 80% quality
            initialQuality: 0.8,     // Initial quality
        };

        const compressedFile = await imageCompression(file, options);

        return compressedFile;
    } catch (error) {
        console.error('Compression failed, using original:', error);
        return file; // Fallback to original on error
    }
}

function CrepeEditor({ args }: ComponentProps): ReactElement {
    const editorRef = useRef<HTMLDivElement>(null);
    const crepeRef = useRef<any>(null);
    const currentValue = useRef<string>(args.default_value || '');
    const isInitialized = useRef<boolean>(false);

    const debouncedSetComponentValue = useRef(
        debounce((markdown: string) => {
            Streamlit.setComponentValue(markdown);
        }, args.throttle_delay || 500)
    );

    // Update debounced function when throttle_delay changes
    useEffect(() => {
        debouncedSetComponentValue.current.cancel();
        debouncedSetComponentValue.current = debounce((markdown: string) => {
            Streamlit.setComponentValue(markdown);
        }, args.throttle_delay || 500);
    }, [args.throttle_delay]);

    useEffect(() => {
        if (editorRef.current && !isInitialized.current) {
            isInitialized.current = true;


            let observer: MutationObserver | null = null;
            let proseMirrorElement: Element | null = null;
            let handleContentChange: (() => void) | null = null;
            let pasteHandler: (() => void) | null = null;

            const initializeEditor = async () => {
                try {
                    // Create Crepe instance with features configuration
                    const features = args.features || {};



                    const crepe = new Crepe({
                        root: editorRef.current!,
                        defaultValue: args.default_value || '# Hello, Crepe!\n\nStart writing your markdown...',
                        features: {
                            // ONLY enable features that are explicitly turned on
                            [Crepe.Feature.CodeMirror]: features.codeblock === true,
                            [Crepe.Feature.Latex]: features.math === true,
                            [Crepe.Feature.Table]: features.table === true,
                            [Crepe.Feature.ImageBlock]: features.image === true,
                            [Crepe.Feature.LinkTooltip]: features.link === true,
                            [Crepe.Feature.ListItem]: true, // Always enabled for basic functionality
                            [Crepe.Feature.Cursor]: true, // Always enabled for basic functionality
                            [Crepe.Feature.BlockEdit]: true, // Always enabled for basic functionality
                            [Crepe.Feature.Placeholder]: true, // Always enabled for basic functionality
                            [Crepe.Feature.Toolbar]: true, // Always show toolbar
                        },
                        featureConfigs: {
                            // Configure ImageBlock with fast compression and async processing
                            [Crepe.Feature.ImageBlock]: features.image === true ? {
                                onUpload: async (file: File) => {


                                    try {
                                        // Always compress for better performance (max 800px, 500KB)
                                        const compressedFile = await compressImageFast(file);

                                        // Convert to base64 asynchronously
                                        const base64Data = await new Promise<string>((resolve, reject) => {
                                            const reader = new FileReader();
                                            reader.onload = (e) => resolve(e.target?.result as string);
                                            reader.onerror = reject;
                                            reader.readAsDataURL(compressedFile);
                                        });


                                        return base64Data;

                                    } catch (error) {
                                        console.error('Image processing failed:', error);

                                        // Return placeholder with error
                                        return `data:image/svg+xml;base64,${btoa(`
                                            <svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
                                                <rect width="300" height="200" fill="#ffe6e6" stroke="#ff4444" stroke-width="2"/>
                                                <text x="150" y="100" text-anchor="middle" fill="#ff4444" font-size="16">Upload Failed</text>
                                                <text x="150" y="120" text-anchor="middle" fill="#ff4444" font-size="12">${file.name}</text>
                                            </svg>
                                        `)}`;
                                    }
                                }
                            } : undefined,
                        }
                    });

                    // Initialize the editor
                    await crepe.create();

                    crepeRef.current = crepe;

                    // Note: We handle line break conversion in handleContentChange instead
                    // of trying to configure Crepe's internal markdown serialization



                    // Set up content change listener
                    handleContentChange = () => {
                        try {
                            let markdown = crepe.getMarkdown();

                            // Clean up various forms of HTML line breaks that might appear
                            markdown = markdown
                                .replace(/<br\s*\/?>/gi, '\n')  // Replace <br/> and <br> with \n
                                .replace(/&nbsp;/gi, ' ')       // Replace non-breaking spaces
                                .replace(/\r\n/g, '\n')         // Normalize Windows line endings
                                .replace(/\r/g, '\n');          // Normalize Mac line endings

                            if (markdown !== currentValue.current) {
                                currentValue.current = markdown;
                                debouncedSetComponentValue.current(markdown);
                            }
                        } catch (error) {
                            console.error('Error getting markdown:', error);
                        }
                    };



                    // Create paste handler
                    pasteHandler = () => {
                        setTimeout(handleContentChange, 100); // Delay for paste processing
                    };

                    // Wait for ProseMirror to be ready
                    const waitForProseMirror = () => {
                        return new Promise<void>((resolve) => {
                            const checkForProseMirror = () => {
                                proseMirrorElement = editorRef.current?.querySelector('.ProseMirror');
                                if (proseMirrorElement) {
                                    resolve();
                                } else {
                                    setTimeout(checkForProseMirror, 100);
                                }
                            };
                            checkForProseMirror();
                        });
                    };

                    await waitForProseMirror();

                    // Listen for content changes using MutationObserver
                    observer = new MutationObserver(handleContentChange);
                    if (editorRef.current) {
                        observer.observe(editorRef.current, {
                            childList: true,
                            subtree: true,
                            characterData: true,
                            attributes: false
                        });
                    }

                    // Also listen for input events on ProseMirror
                    if (proseMirrorElement && handleContentChange && pasteHandler) {
                        proseMirrorElement.addEventListener('input', handleContentChange);
                        proseMirrorElement.addEventListener('keyup', handleContentChange);
                        proseMirrorElement.addEventListener('paste', pasteHandler);
                    }

                    // Set readonly mode if needed
                    if (args.readonly) {
                        crepe.setReadonly(true);
                    }

                    // Send initial value
                    debouncedSetComponentValue.current(args.default_value || '');

                    // Set component ready
                    Streamlit.setComponentReady();

                } catch (error) {
                    console.error('Error creating Crepe editor:', error);
                    // Display error message instead of fallback
                    if (editorRef.current) {
                        editorRef.current.innerHTML = `
                            <div style="padding: 20px; color: #d32f2f; background: #ffebee; border-radius: 4px; margin: 10px;">
                                <strong>Error:</strong> Failed to initialize Crepe editor. Please check console for details.
                            </div>
                        `;
                    }
                    Streamlit.setComponentReady();
                }
            };

            initializeEditor();

            // Cleanup function
            return () => {
                if (observer) {
                    observer.disconnect();
                }
                if (proseMirrorElement && handleContentChange && pasteHandler) {
                    proseMirrorElement.removeEventListener('input', handleContentChange);
                    proseMirrorElement.removeEventListener('keyup', handleContentChange);
                    proseMirrorElement.removeEventListener('paste', pasteHandler);
                }
                if (crepeRef.current) {
                    try {
                        crepeRef.current.destroy();
                    } catch (error) {
                        console.error('Error destroying Crepe editor:', error);
                    }
                    crepeRef.current = null;
                }
                debouncedSetComponentValue.current.cancel();
            };
        }
    }, [JSON.stringify(args.features)]); // Add features as dependency to force recreation

    // Handle image upload response from Python
    useEffect(() => {
        if (args.type === "image_upload_response" && args.image_id && args.image_url && crepeRef.current) {
            try {

                // Get current markdown and replace placeholder with actual URL
                const currentMarkdown = crepeRef.current.getMarkdown();
                const placeholderUrl = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==";

                // Find and replace the placeholder image with the real URL
                const updatedMarkdown = currentMarkdown.replace(
                    new RegExp(`!\\[([^\\]]*)\\]\\(${placeholderUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\)`, 'g'),
                    `![$1](${args.image_url})`
                );

                if (updatedMarkdown !== currentMarkdown) {
                    crepeRef.current.setMarkdown(updatedMarkdown);
                    currentValue.current = updatedMarkdown;
                }
            } catch (error) {
                console.error('Error handling image upload response:', error);
            }
        }
    }, [args.type, args.image_id, args.image_url]);

    // Update content when args change - simplified approach
    useEffect(() => {
        if (crepeRef.current && args.default_value !== currentValue.current) {
            try {
                // Use setMarkdown method if available
                if (crepeRef.current.setMarkdown) {
                    crepeRef.current.setMarkdown(args.default_value || '');
                    currentValue.current = args.default_value || '';
                }
            } catch (error) {
                console.error('Error updating markdown:', error);
            }
        }
    }, [args.default_value]);

    // Handle height management - simplified like st_quill
    useEffect(() => {
        if (args.height) {
            // Fixed height mode
            Streamlit.setFrameHeight(args.height);
        } else {
            // Auto height mode - let Streamlit calculate automatically
            Streamlit.setFrameHeight();

            // Set up ResizeObserver to watch for content changes
            const ro = new ResizeObserver(() => {
                Streamlit.setFrameHeight();
            });

            if (editorRef.current) {
                ro.observe(editorRef.current);
            }

            return () => ro.disconnect();
        }
    }, [args.height]);



    const isAutoHeight = !args.height;

    return (
        <div
            className="crepe-container"
            data-auto-height={isAutoHeight ? "true" : "false"}
            style={{
                height: isAutoHeight ? 'auto' : args.height,
                border: '1px solid #e1e5e9',
                borderRadius: '8px',
                overflow: 'visible', // Always allow dropdowns to overflow
                backgroundColor: '#ffffff',
                fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
                position: 'relative',
            }}
        >
            <div
                ref={editorRef}
                className="crepe-editor"
                style={{
                    height: isAutoHeight ? 'auto' : '100%',
                    width: '100%',
                    overflow: isAutoHeight ? 'visible' : 'auto', // Allow scrolling only for content in fixed height mode
                }}
            />
        </div>
    );
}

export default withStreamlitConnection(CrepeEditor);