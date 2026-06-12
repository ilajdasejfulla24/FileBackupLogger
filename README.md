# File Backup Logger

## Overview

File Backup Logger is an Object-Oriented Python application designed to create secure backups of files and directories. The application allows users to select source and destination folders through a graphical user interface, create timestamped backups, compress backups into ZIP archives, and maintain detailed logs of all backup operations.

The project was developed using Python and follows Object-Oriented Programming (OOP) principles.

---

## Features

### Backup Management

* Create backups of files and directories
* Preserve original folder structure
* Support for large files and folders
* Automatic backup naming with timestamps

### Versioning

Each backup is automatically assigned a unique name containing:

* Date
* Time
* Application version

Example:

```text
backup_2026-06-12_15-30-45_v1.0.0
```

### ZIP Compression

Users can choose between:

* Standard folder copy
* ZIP-compressed backup

### Logging System

Every backup operation is recorded in a log file containing:

* Backup date and time
* Success or failure status
* Number of files processed
* Backup duration
* Destination path

### Graphical User Interface

Built with Tkinter:

* Select source folder
* Select destination folder
* Enable or disable ZIP compression
* Start backup with a single click

### Configuration File

User preferences are automatically stored in a JSON configuration file:

* Last selected source folder
* Last selected destination folder
* ZIP compression preference

### Error Handling

The application handles common issues such as:

* Missing folders
* Invalid paths
* Permission errors
* Unexpected file system exceptions

---

## Technologies Used

* Python 3.x
* Tkinter
* shutil
* zipfile
* json
* os
* datetime

---

## Object-Oriented Design

### BackupManager

Responsible for:

* Creating backups
* Copying directories
* Generating ZIP archives
* Calculating backup statistics

### Logger

Responsible for:

* Writing backup records
* Tracking successes and failures

### ConfigManager

Responsible for:

* Loading configuration settings
* Saving user preferences

### BackupGUI

Responsible for:

* User interface
* Folder selection
* User interaction

---

## Project Structure

```text
File-Backup-Logger/
│
├── main.py
├── backup.py
├── config.py
├── logger.py
├── gui.py
│
├── config.json
├── backup.log
│
├── backups/
│
├── screenshots/
│   └── gui.png
│
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/File-Backup-Logger.git
```

### Navigate to the Project Directory

```bash
cd File-Backup-Logger
```

### Run the Application

```bash
python main.py
```

---

## How to Use

1. Launch the application.
2. Select the source folder.
3. Select the destination folder.
4. Choose whether to enable ZIP compression.
5. Click **Start Backup**.
6. Wait for the confirmation message.

The backup will be created automatically and logged in the log file.

