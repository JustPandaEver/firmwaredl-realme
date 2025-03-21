# OTA Firmware Downloader

This script is a simple yet powerful tool for downloading OTA firmware files for Realme and Oplus devices. It utilizes Python and the `tqdm` library to provide a progress bar during the download process, making it user-friendly and efficient.

## Requirements

- Python 3.x
- `tqdm` library (automatically installed if not present)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/JustPandaEver/firmwaredl-realme.git
   cd firmwaredl-realme
   ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the downloader, run the script from the command line with the URL of the firmware file you wish to download:

```bash
python dl.py <url>
```

### Example

For example, to download a firmware file from a specific URL, you would run:

```bash
python dl.py http://gauss-componentotacostmanual-in.allawnofs.com/remove-e56cf731999231d8936d0551e249e30d/component-ota/25/01/02/6d8564d101c74c709f14f2bb4bc54e7b.zip
```

## Features

- **Progress Bar**: Visual feedback on download progress.
- **Resume Capability**: If the download is interrupted, it can resume from where it left off.
- **Cross-Platform**: Works on both Windows and Unix-based systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements!

## Acknowledgments

- Thanks to the creators of the `tqdm` library for providing a great tool for progress visualization.
