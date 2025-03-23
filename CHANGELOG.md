# Changelog

Notable changes to this project will be documented in this file.

## [1.0.0] - 2024-03-23

### Added
- Update for Python 3 compatibility
- Fixed package structure re: `__init__.py` files
- Exposed BlueButton class as CCDA for backward compatibility

### Changed
- Replaced Python 2 string handling (`basestring`) with Python 3 (`str`)
- Updated imports to use relative imports for better Python 3 compatibility
- Updated dictionary methods from Python 2 `.iteritems()` to Python 3 `.items()`
- Removed unnecessary `__future__` imports

### Removed
- Removed Python 2 support
- Removed outdated warning about instability

## [0.0.1] - 2018-07-02

### Added
- Initial release of pyCCDA
- Basic CCDA document parsing functionality
- Support for all major sections of CCDA documents
