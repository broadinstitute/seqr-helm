
# Changelog

Notable infrastructure changes will be kept in this file.

---

## [2.19.2-annotations-final] 02/25/2025

### Added

### Changed
- Moves the initContainers processes on the `pipeline-runner` that sync variant reference data used in the pipeline (both hail tables and VEP tarballs)
into cronjobs.

### Fixed
- The initContainers change resolves an bug reported [here](https://github.com/broadinstitute/seqr-helm/issues/182) relating to the initial migrations
when creating a seqr installation for the first time.  By offloading the initContainers, the `pipeline-runner` pod can immediately listen to requests
from the seqr migrations.

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