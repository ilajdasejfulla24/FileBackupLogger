import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from backup import BackupManager
from logger import Logger
from config import ConfigManager


class BackupGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("File Backup Logger")
        self.root.geometry("600x300")

        self.config = ConfigManager.load()

        self.source_var = tk.StringVar(
            value=self.config["source_folder"]
        )

        self.destination_var = tk.StringVar(
            value=self.config["destination_folder"]
        )

        self.zip_var = tk.BooleanVar(
            value=self.config["zip_enabled"]
        )

        self.create_widgets()

    def create_widgets(self):

        tk.Label(
            self.root,
            text="Source Folder"
        ).pack()

        tk.Entry(
            self.root,
            textvariable=self.source_var,
            width=70
        ).pack()

        tk.Button(
            self.root,
            text="Browse",
            command=self.select_source
        ).pack()

        tk.Label(
            self.root,
            text="Destination Folder"
        ).pack()

        tk.Entry(
            self.root,
            textvariable=self.destination_var,
            width=70
        ).pack()

        tk.Button(
            self.root,
            text="Browse",
            command=self.select_destination
        ).pack()

        tk.Checkbutton(
            self.root,
            text="ZIP Compression",
            variable=self.zip_var
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Start Backup",
            command=self.start_backup,
            bg="green",
            fg="white"
        ).pack(pady=15)

    def select_source(self):
        folder = filedialog.askdirectory()
        self.source_var.set(folder)

    def select_destination(self):
        folder = filedialog.askdirectory()
        self.destination_var.set(folder)

    def start_backup(self):

        try:

            source = self.source_var.get()
            destination = self.destination_var.get()

            manager = BackupManager(
                source,
                destination
            )

            if self.zip_var.get():
                result = manager.zip_backup()
            else:
                result = manager.copy_backup()

            Logger.write(
                f"SUCCESS | Files: {result['files']} | "
                f"Duration: {result['duration']}s | "
                f"{result['path']}"
            )

            ConfigManager.save({
                "source_folder": source,
                "destination_folder": destination,
                "zip_enabled": self.zip_var.get()
            })

            messagebox.showinfo(
                "Success",
                "Backup completed successfully!"
            )

        except Exception as e:

            Logger.write(f"ERROR | {e}")

            messagebox.showerror(
                "Error",
                str(e)
            )
