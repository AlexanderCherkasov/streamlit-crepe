# Implementation Plan

- [ ] 1. Create iframe height management utilities
  - Implement utilities to detect current iframe height and manage dynamic height changes
  - Create functions to communicate with Streamlit.setFrameHeight() API
  - Add state management for tracking original vs expanded height
  - _Requirements: 2.2, 2.3_

- [ ] 2. Implement menu state detection system
  - [ ] 2.1 Create menu event listeners for Milkdown Crepe
    - Add event listeners to detect when toolbar dropdowns open/close
    - Implement detection for slash menu (/) activation and dismissal
    - Add listeners for table editing menu state changes
    - Create event listeners for link tooltip/editing menu
    - _Requirements: 1.1, 1.2_

  - [ ] 2.2 Build menu boundary calculation utilities
    - Implement function to calculate available space around menu trigger elements
    - Create utilities to measure iframe dimensions and current scroll position
    - Add functions to estimate menu size requirements for different menu types
    - Implement boundary detection to determine if menu will overflow
    - _Requirements: 1.4, 3.1, 3.2_

- [ ] 3. Implement dynamic iframe height expansion
  - [ ] 3.1 Create height expansion logic
    - Write function to calculate required additional height for menu display
    - Implement Streamlit.setFrameHeight() calls with calculated expanded height
    - Add debouncing to prevent excessive height changes during rapid menu interactions
    - Create fallback handling if Streamlit communication fails
    - _Requirements: 2.2, 2.3_

  - [ ] 3.2 Implement height restoration system
    - Create function to restore original iframe height when menus close
    - Add timeout-based restoration as fallback if menu close events are missed
    - Implement cleanup on component unmount to prevent stuck expanded height
    - Add state tracking to prevent multiple simultaneous expansions
    - _Requirements: 2.4_

- [ ] 4. Configure Milkdown Crepe menu positioning
  - [ ] 4.1 Research and implement toolbar dropdown positioning
    - Investigate Milkdown Crepe toolbar configuration options for menu positioning
    - Configure toolbar dropdowns to prefer upward positioning when space below is limited
    - Implement custom positioning logic if Crepe doesn't provide sufficient control
    - Add max-height and scrolling for large toolbar menus
    - _Requirements: 1.1, 3.1, 3.3_

  - [ ] 4.2 Configure slash menu positioning and constraints
    - Research Crepe slash menu (/) positioning configuration options
    - Implement intelligent positioning to keep slash menu within iframe bounds
    - Add scrollable container for slash menu when content exceeds available space
    - Configure menu to position above cursor when insufficient space below
    - _Requirements: 1.1, 3.1, 3.3_

  - [ ] 4.3 Implement table editing menu positioning
    - Configure table editing menus to respect iframe boundaries
    - Implement positioning logic for table cell editing dropdowns
    - Add scrollable containers for table formatting menus
    - Ensure table menus don't interfere with other editor functionality
    - _Requirements: 1.1, 3.1, 3.3_

- [ ] 5. Integrate height management with menu positioning
  - [ ] 5.1 Connect menu detection with height expansion
    - Integrate menu state detection with iframe height expansion system
    - Implement coordinated timing between menu opening and height changes
    - Add logic to expand height before menu renders to prevent clipping
    - Create system to handle multiple simultaneous menus
    - _Requirements: 1.3, 2.2, 2.3_

  - [ ] 5.2 Implement positioning fallbacks and error handling
    - Add fallback positioning strategies when optimal positioning fails
    - Implement error handling for iframe communication failures
    - Create graceful degradation when height expansion is not possible
    - Add logging and debugging utilities for troubleshooting menu issues
    - _Requirements: 1.4, 3.4_

- [ ] 6. Add comprehensive testing and validation
  - [ ] 6.1 Create unit tests for menu positioning logic
    - Write tests for boundary calculation functions
    - Test height expansion and restoration logic
    - Create tests for menu state detection accuracy
    - Add tests for edge cases and error conditions
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [ ] 6.2 Implement integration tests for iframe behavior
    - Test menu visibility in various iframe height configurations
    - Validate height expansion/restoration in different scenarios
    - Test multiple simultaneous menus and their interactions
    - Create tests for different screen sizes and viewport configurations
    - _Requirements: 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4_

- [ ] 7. Update component styling and CSS
  - Add CSS to ensure proper z-index layering for menus within iframe
  - Implement responsive menu styling for different iframe sizes
  - Add CSS for scrollable menu containers and compact menu layouts
  - Update component container styles to support dynamic height changes
  - _Requirements: 1.1, 1.3, 3.3_

- [ ] 8. Update documentation and examples
  - Update component documentation to explain menu overflow handling
  - Add examples demonstrating menu behavior in constrained spaces
  - Create troubleshooting guide for menu visibility issues
  - Update API documentation to reflect any new configuration options
  - _Requirements: 2.1_