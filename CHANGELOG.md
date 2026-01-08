
# Changelog

Notable infrastructure changes will be kept in this file.

---

## [seqr-platform-2.16.0] 1/8/2026

### Added
- Moves variant-level reference data sources directly into ClickHouse Materialized Views.  Note that this will temporarily increase the memory used by
the ClickHouse server process by 50% while we work to remove those sources from the loading pipeline.

### Changed

### Fixed

---

## [seqr-platform-2.11.0] 11/18/2025

### Added

### Changed
- Deprecates the ClickHouse loading service, moving loading directly into the loading pipeline as a Luigi task.
- Updates the `hail-search` -> `ClickHouse` migration script to load directly into ClickHouse after generating parquets.

### Fixed

---