import os
import shutil
import zipfile
from datetime import datetime
import time


class BackupManager:

    VERSION = "1.0.0"

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def create_backup_name(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"backup_{timestamp}_v{self.VERSION}"

    def copy_backup(self):
        start_time = time.time()

        backup_name = self.create_backup_name()
        backup_path = os.path.join(self.destination, backup_name)

        shutil.copytree(self.source, backup_path)

        duration = round(time.time() - start_time, 2)

        file_count = sum(len(files) for _, _, files in os.walk(self.source))

        return {
            "path": backup_path,
            "files": file_count,
            "duration": duration
        }

    def zip_backup(self):
        start_time = time.time()

        backup_name = self.create_backup_name()
        zip_path = os.path.join(self.destination, backup_name + ".zip")

        file_count = 0

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

            for root, dirs, files in os.walk(self.source):

                for file in files:
                    file_count += 1

                    file_path = os.path.join(root, file)

                    arcname = os.path.relpath(
                        file_path,
                        self.source
                    )

                    zipf.write(file_path, arcname)

        duration = round(time.time() - start_time, 2)

        return {
            "path": zip_path,
            "files": file_count,
            "duration": duration
        }
