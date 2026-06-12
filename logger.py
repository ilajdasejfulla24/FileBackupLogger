from datetime import datetime


class Logger:

    LOG_FILE = "backup.log"

    @staticmethod
    def write(message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(Logger.LOG_FILE, "a") as log:
            log.write(
                f"[{timestamp}] {message}\n"
            )
