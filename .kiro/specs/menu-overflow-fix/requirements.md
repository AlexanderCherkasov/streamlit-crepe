# Requirements Document

## Introduction

The Streamlit Crepe component has an issue where dropdown menus (toolbar dropdowns, slash menu, table editing menus, etc.) cannot fit within the constrained frame height, especially when using minimum height settings. This causes menus to be cut off or hidden, making the editor unusable in many scenarios.

## Requirements

### Requirement 1

**User Story:** As a user of the Streamlit Crepe editor, I want dropdown menus to be fully visible and accessible, so that I can use all editor features regardless of the frame height constraints.

#### Acceptance Criteria

1. WHEN a dropdown menu is opened THEN the menu SHALL be fully visible even if it extends beyond the editor frame
2. WHEN the editor has a minimum height constraint THEN dropdown menus SHALL still be accessible and not clipped
3. WHEN multiple menus are open simultaneously THEN all menus SHALL remain visible and functional
4. WHEN the editor is in a small container THEN menus SHALL automatically position themselves to remain visible

### Requirement 2

**User Story:** As a developer integrating the Streamlit Crepe component, I want the menu overflow to be handled automatically, so that I don't need to manually adjust container styles or frame heights.

#### Acceptance Criteria

1. WHEN the component is embedded in Streamlit THEN menu overflow SHALL be handled automatically without additional configuration
2. WHEN the editor frame height is constrained THEN the component SHALL communicate with Streamlit to allow menu overflow
3. WHEN menus are opened THEN the Streamlit frame SHALL temporarily expand if needed to accommodate the menu
4. WHEN menus are closed THEN the frame SHALL return to its original size

### Requirement 3

**User Story:** As a user working with different screen sizes and layouts, I want menus to position intelligently, so that they remain usable across different viewport configurations.

#### Acceptance Criteria

1. WHEN a menu would extend below the viewport THEN the menu SHALL position itself above the trigger element
2. WHEN a menu would extend beyond the right edge THEN the menu SHALL align to the right edge of the trigger
3. WHEN there is insufficient space in any direction THEN the menu SHALL use scrolling within the menu container
4. WHEN the editor is near viewport edges THEN menus SHALL adjust their positioning automatically