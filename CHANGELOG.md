# Changelog

All notable changes to PaintCalx will be documented in this file.

## [2.0.0] - 2026-01-12

### Added
- **Unified API Contract**: Single `/calculate` endpoint replacing multiple endpoints
- **Enhanced Validation**: Surface deductions cannot exceed total surface
- **Coefficient Range Validation**: Coefficients limited to 0.8-1.5 range
- **Improved Proportion Tolerance**: Accepts 0.99-1.01 range for component proportions
- **Automatic Unit Conversion**: Built-in L ↔ mL, kg ↔ g conversions
- **Comprehensive Error Handling**: Clear error messages and validation responses
- **Professional API Documentation**: Interactive Swagger UI at `/docs`

### Changed
- **API Structure**: Moved from 3 separate endpoints to unified contract
- **Response Format**: Standardized JSON response with success/error fields
- **Input Validation**: Enhanced business logic validation
- **Documentation**: Complete API and usage documentation

### Fixed
- **Floating Point Precision**: Improved rounding and decimal handling
- **Edge Case Handling**: Better validation for boundary conditions

### Technical
- **Dependencies**: Added FastAPI and Uvicorn for REST API functionality
- **Testing**: Expanded test suite to 10 comprehensive test cases
- **Code Structure**: Improved separation of concerns and error handling

## [1.0.0] - 2026-01-11

### Added
- **Core Calculation Engine**: Surface to volume calculation
- **Component Proportions**: Multi-component paint mixture calculations
- **Unit Conversions**: Basic L/mL and kg/g conversions
- **Custom Coefficients**: User-configurable surface coefficients
- **Basic Validation**: Input validation and error handling
- **Test Suite**: Initial test coverage for core functionality

### Features
- Surface area to paint volume calculation
- Component proportion calculations
- Unit conversions (L, mL, kg, g)
- Customizable surface coefficients
- Python library interface
