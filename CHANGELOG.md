
# Changelog

Notable infrastructure changes will be kept in this file.

---

## [seqr-platform-2.11.0] 11/18/2025

### Added

### Changed
- Deprecates the ClickHouse loading service, moving loading directly into the loading pipeline as a Luigi task.
- Updates the migration script to load directly into ClickHouse after generating parquets.

### Fixed

---