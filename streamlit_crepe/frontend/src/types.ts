import { ComponentProps } from 'streamlit-component-lib';

/**
 * Props for the CrepeEditor component
 */
export interface CrepeEditorProps extends ComponentProps {
  args: {
    value: string;
    height: number | string;
    placeholder: string;
    readonly: boolean;
    theme: string;
    features: Record<string, boolean>;
    toolbar: Record<string, boolean>;
  };
}

/**
 * Upload result interface for image handling
 */
export interface UploadResult {
  src: string;
  alt: string;
}

/**
 * Event types for Streamlit communication
 */
export type EventType = 'content_change' | 'focus' | 'blur' | 'image_upload';

/**
 * Event payload for Streamlit communication
 */
export interface EventPayload {
  markdown: string;
  type: EventType;
  image_data?: string;
  image_name?: string;
}
