# EmptyFolderDeleter

A simple python script to delete folders that are empty.

## "Installation" & Usage

 * Download the script and put it somewhere.
 * Ensure python 3 is installed
 * Run the script by double clicking the file or running `python path/to/file.py` or `python3 path/to/file.py` when on linux.

## Example output
```
A:\test>python main.py
📁 Path to folder to check for empty folders: A:\folders
🔁 Recursively (check child folders)? [y/N]: y
📂 Found ./a/a
📂 Found ./a/b
🗑️ Delete 2 empty folders? [y/N]: n
❌ No folders were deleted

🔄 Restarting

📁 Path to folder to check for empty folders: A:\folders
🔁 Recursively (check child folders)? [y/N]: y
📂 Found ./a/a
📂 Found ./a/b
🗑️ Delete 2 empty folders? [y/N]: y
🚮 Deleting folders
🧬 Creating threads
🔨 Starting 2 threads
⌛ Waiting for threads to finish
🗑️ Deleted ./a/a
🗑️ Deleted ./a/b
✅ Deleted 2 folders
💫 Rerun to check if new empty folders where created? [y/N]: y

✅ No empty folders found
```
