import tkinter as tk
from gui import BackupGUI


def main():

    root = tk.Tk()

    app = BackupGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()
