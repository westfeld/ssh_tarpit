# Changelog

## Version 0.0.3
### Changed
 * Dependency on secrets module was removed. Random byte generation is now based
   on the random module.
 * HTTP statistics server was extended to return an empty HTTP message with the
   status code 204 NO CONTENT
 * Updated docs

## Version 0.0.2
### Added
 * A small HTTP server for serving statistics about trapped clients in SSHTarpit
   was added.

## Version 0.0.1

Initial version of SSHTarpit
