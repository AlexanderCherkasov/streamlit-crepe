# Design Document

## Overview

The menu overflow issue in Streamlit Crepe occurs because the component runs inside an iframe, and dropdown menus cannot escape iframe boundaries due to browser security restrictions. When the editor has a minimum height or is in a small container, menus get clipped by the iframe edges. This design addresses the issue by working within iframe constraints through dynamic frame height adjustment and intelligent menu positioning that keeps menus within the iframe bounds.

## Architecture

Since the component runs in an iframe, menus cannot escape the iframe boundaries. The solution involves two main approaches:

1. **Dynamic Frame Height Management**: Temporarily expand the iframe height when menus open to provide space for dropdowns
2. **Intelligent Menu Positioning**: Position menus within the iframe bounds, using upward positioning and scrollable containers when needed

Key constraint: All solutions must work within the iframe sandbox - no DOM manipulation outside the iframe is possible.

## Components and Interfaces

### 1. Iframe Height Management

**Component**: `IframeHeightManager` utility
**Purpose**: Communicate with Streamlit to expand iframe height when menus need space

Key features:
- Detect when menus are about to open
- Calculate required additional height for menu display
- Use `Streamlit.setFrameHeight()` to temporarily expand iframe
- Restore original height when menus close

### 2. Menu Boundary Detection

**Component**: `MenuBoundaryDetector` utility  
**Purpose**: Detect when menus would overflow iframe boundaries and calculate positioning

Interface:
```typescript
interface MenuBoundaryDetector {
  getAvailableSpace(triggerElement: Element): BoundaryInfo;
  calculateOptimalPosition(menuSize: Size, triggerElement: Element): Position;
  willMenuOverflow(menuSize: Size, position: Position): boolean;
}

interface BoundaryInfo {
  spaceBelow: number;
  spaceAbove: number;
  spaceLeft: number;
  spaceRight: number;
  iframeHeight: number;
  iframeWidth: number;
}
```

### 3. Menu State Tracker

**Component**: `MenuStateTracker` hook
**Purpose**: Track when menus are open/closed to trigger frame adjustments

Interface:
```typescript
interface MenuState {
  isMenuOpen: boolean;
  menuType: 'toolbar' | 'slash' | 'table' | 'link';
  menuPosition: { x: number; y: number };
  menuHeight: number;
}
```

### 4. Menu Positioning Strategy

**Component**: Menu positioning utilities within Milkdown Crepe configuration
**Purpose**: Configure Crepe menus to position intelligently within iframe bounds

Key strategies:
- **Upward positioning**: When space below is insufficient, position menus above trigger
- **Scrollable containers**: For large menus, use max-height with internal scrolling
- **Edge alignment**: Align menus to iframe edges when near boundaries
- **Compact layouts**: Use more compact menu designs when space is limited

## Data Models

### MenuConfiguration
```typescript
interface MenuConfiguration {
  allowOverflow: boolean;
  maxHeight: number;
  positioning: 'auto' | 'above' | 'below';
  alignment: 'left' | 'right' | 'center';
}
```

### FrameState
```typescript
interface FrameState {
  originalHeight: number;
  currentHeight: number;
  isExpanded: boolean;
  expandedFor: string; // menu identifier
}
```

## Error Handling

### Menu Positioning Failures
- **Fallback**: Use default positioning if intelligent positioning fails
- **Recovery**: Provide scrollable menu container if no position works
- **Logging**: Log positioning issues for debugging

### Frame Height Communication Errors
- **Fallback**: Rely on CSS overflow if Streamlit communication fails
- **Recovery**: Implement timeout to restore height if communication is lost
- **User Feedback**: Show warning if menus may be clipped

### CSS Override Conflicts
- **Detection**: Check for conflicting styles from parent containers
- **Resolution**: Use `!important` selectively for critical overflow styles
- **Compatibility**: Test with different Streamlit themes and custom CSS

## Testing Strategy

### Unit Tests
- Test menu positioning calculations
- Test frame height manager state transitions
- Test CSS class application logic

### Integration Tests
- Test menu visibility in constrained containers
- Test frame height communication with Streamlit
- Test multiple simultaneous menus

### Visual Regression Tests
- Screenshot tests for menu positioning
- Test across different screen sizes
- Test with different editor heights and content

### Manual Testing Scenarios
1. Small editor with toolbar dropdown
2. Minimum height editor with slash menu
3. Table editing in constrained space
4. Multiple editors on same page
5. Mobile viewport testing

## Implementation Approach

### Phase 1: Iframe Height Management Foundation
1. Create iframe height detection utilities
2. Implement menu open/close event detection
3. Integrate with Streamlit.setFrameHeight() API
4. Test basic height expansion/restoration

### Phase 2: Menu Boundary Detection
1. Implement iframe boundary calculation
2. Create menu size estimation utilities  
3. Add trigger element position detection
4. Test boundary detection accuracy

### Phase 3: Crepe Menu Configuration
1. Research Milkdown Crepe menu positioning options
2. Configure toolbar dropdowns for intelligent positioning
3. Configure slash menu positioning
4. Configure table editing menu positioning

### Phase 4: Integration and Fallbacks
1. Integrate height management with menu positioning
2. Add fallback strategies for edge cases
3. Implement error handling for iframe communication failures
4. Performance optimization and testing

## Iframe-Specific Considerations

### Limitations
- Menus cannot render outside iframe boundaries
- No access to parent window DOM
- Limited communication with Streamlit host
- Security restrictions on cross-frame operations

### Solutions Within Constraints
- Use Streamlit.setFrameHeight() for temporary expansion
- Position menus within iframe using available space calculation
- Implement scrollable menu containers for large menus
- Use compact menu designs when space is very limited