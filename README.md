# JSFNC - JellyFin Series File Name Changer

**JSFNC (JellyFin Series File Name Changer)** is a command-line tool written in Python, designed to manage TV show episode files. It allows you to rename files to a consistent format and/or organize them into a structured directory layout, ideal for media servers like Jellyfin.

## 📦 Features

- **File Renaming**  
  Automatically renames episode files to a standard format: `Series Name - SXXEXX.extension`.

- **Directory Structuring**  
  Copies and organizes episodes into a structure: `Series Name/Season XX/Series Name - SXXEXX.extension`.

- **Interactive Confirmations**  
  Prompts for confirmation before renaming or moving files, with options to process all or quit.

- **Flexible Pattern Matching**  
  Recognizes multiple common season and episode naming formats (e.g., `S01E02`, `1x02`, `Season 01 Episode 02`).

- **Two Modes of Operation**  
  - `rename` (default): Renames files in place.  
  - `structure`: Creates a new organized directory structure by copying files.

## ⚙️ Requirements

- Python 3.x (Python 3.6 or newer recommended)

## 🧩 Installation

Clone the repository (if hosted on GitHub, GitLab, etc):

```bash
git clone https://github.com/NVTMRE/jsfnc.git
cd JSFNC
```

Or simply download the `.py` files and place them in one directory.

**Dependencies:**  
No external libraries are required — only Python's standard library is used.

## 🔨 Build

You can build a standalone executable or install JSFNC as a package:

1. **Using PyInstaller (standalone executable)**  
   A `build.py` script is provided to create a single-file executable. Run:
   ```bash
   python build.py
   ```
   This will generate a `JSFNC` executable in the `dist/` folder, including the `README.md` as data.

2. **Packaging and Installation with `setup.py`**  
   To install JSFNC as a console script, run:
   ```bash
   pip install .
   ```
   This will install the `jsfnc` command so you can run:
   ```bash
   jsfnc -n "Series Name" [options]
   ```

## 🚀 Usage

Run the program from the command line using the `main.py` script:

```bash
python main.py -n "Series Name" [options]
```

Or, if installed via `setup.py`:

```bash
jsfnc -n "Series Name" [options]
```

### Arguments

- `-n`, `--name <SERIES_NAME>`: **(required)** The target name for the TV show (e.g., `"My Favorite Show"`).
- `-p`, `--path <SOURCE_PATH>`: *(optional)* Directory containing episode files. Defaults to current directory.
- `-m`, `--mode <MODE>`: *(optional)* Operation mode:
  - `rename`: Rename files in place.
  - `structure`: Create an organized structure by copying files.
- `-t`, `--target <TARGET_PATH>`: *(required if mode=structure)* Path where the new folder will be created.

## 📚 Examples

### Rename files in place:

```bash
python main.py -n "My Awesome Show" -p "/path/to/your/episodes"
```

Or in the current directory:

```bash
python main.py -n "My Awesome Show"
```

If installed via `setup.py`:

```bash
jsfnc -n "My Awesome Show" -p "/path/to/your/episodes"
```

### Create an organized directory structure:

```bash
python main.py -n "Another Great Series" -p "/path/to/your/episodes" -m structure -t "/mnt/tv_shows"
```

Or with installed command:

```bash
jsfnc -n "Another Great Series" -p "/path/to/your/episodes" -m structure -t "/mnt/tv_shows"
```

### Directory Structure (structure mode):

```
<TARGET_PATH>/
└── <Series Name>/
    ├── Season 01/
    │   ├── <Series Name> - S01E01.extension
    │   └── <Series Name> - S01E02.extension
    ├── Season 02/
    │   ├── <Series Name> - S02E01.extension
    │   └── ...
    └── ...
```

## 🔍 How It Works

The script scans filenames for common season/episode formats (e.g., `S01E02`, `1x02`, `Season 1 Episode 2`, `.102`). Before renaming or copying, it prompts the user for confirmation, allowing you to skip, process all, or quit.

## 🤝 Contributing

I welcome help, suggestions, and contributions! If you have ideas or find bugs, feel free to:

- Open an issue in the project's repository.
- Submit a pull request.
- Contact me directly via email: **nvtmre@gmail.com**

Any form of help is appreciated!

## 📄 License

This project is licensed under the MIT License.