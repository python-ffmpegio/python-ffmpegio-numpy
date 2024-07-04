# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.10.0] - 2024-07-03

- Matching the `ffmpegio-core` version bump 

## [0.9.1] - 2024-02-19

- Matching the `ffmpegio-core` version bump 

## [0.9.0] - 2023-12-08

- Matching the `ffmpegio-core` version bump 

## [0.8.6] - 2023-11-29

- Matching the `ffmpegio-core` version bump 

## [0.8.5] - 2023-11-13

- Matching the `ffmpegio-core` version bump 

## [0.8.4] - 2023-11-07

- Matching the `ffmpegio-core` version bump 

## [0.8.3] - 2023-03-19

- Matching the `ffmpegio-core` version bump 

## [0.8.2] - 2023-03-19

- Matching the `ffmpegio-core` version bump 

## [0.8.1] - 2023-03-18

- plugins to return `None` if not compatible

### Changed

- Skipping 0.8.0 to match `ffmpegio-core` version

## [0.7.0] - 2022-08-24

### Changed

- Matching the `ffmpegio-core` version bump 
- `video_bytes()` and `audio_bytes()` make sure data frames are C-contiguous

## [0.6.0] - 2022-08-13

### Changed

- Matching the `ffmpegio-core` version bump 
- `video_info()` allows 2-D grayscale array
- `audio_info()` allows 1-D mono array

## [0.5.1] - 2022-04-21

### Changed

- Matching the `ffmpegio-core` version bump 

## [0.5.0] - 2022-04-03

### Changed

- Matching the `ffmpegio-core` version bump 

## [0.4.1] - 2022-02-22

### Changed

- Matching the `ffmpegio-core` version bump 

## [0.4.0] - 2022-02-22

### Changed

- Matching the `ffmpegio-core` version bump 

## [0.3.3] - 2022-02-18

### Changed

- Matching the `ffmpegio-core` version bump 

## [0.3.1] - 2022-02-13

### Added

- Added `squeeze` argument to `bytes_to_video` and `bytes_to_audio` hooks
  
## [0.3.0] - 2022-02-13

### Added

- First release.
- A plugin to convert raw media I/O data of `ffmpegio` to use `numpy.ndarray` objects.

[Unreleased]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.10.0...HEAD
[v0.10.0]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.9.1...v0.10.0
[v0.9.1]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.9.0...v0.9.1
[v0.9.0]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.6...v0.9.0
[v0.8.6]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.5...v0.8.6
[v0.8.5]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.4...v0.8.5
[v0.8.4]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.3...v0.8.4
[v0.8.3]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.2...v0.8.3
[v0.8.2]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.8.1...v0.8.2
[v0.8.1]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.7.0...v0.8.1
[v0.7.0]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.6.0...v0.7.0
[v0.6.0]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.5.1...v0.6.0
[v0.5.1]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.5.0...v0.5.1
[v0.5.0]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.4.1...v0.5.0
[v0.3.3]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.3.1...v0.4.1
[v0.3.1]: https://github.com/python-ffmpegio/python-ffmpegio/compare/v0.3.0...v0.3.1
