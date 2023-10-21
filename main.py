import os
from threading import Thread

def get_user_confirmation(message):
    return input("{} [y/N]: ".format(message)).strip().lower() == "y"

def minimize_path(s):
    global path
    return str(s).replace(path, ".", 1).replace("\\", "/")

def find_empty_folders(path, recursively):
    empty_folders = []

    if not os.path.isdir(path):
        print("❌ Invalid directory [{}]".format(minimize_path(path)))
        return empty_folders

    def run_loop(folder):
        if not os.path.isdir(folder):
            return

        try:
            if not os.listdir(folder):
                print("📂 Found {}".format(minimize_path(folder)))
                empty_folders.append(folder)
            elif recursively:
                try:
                    threads = []

                    for item in os.listdir(folder):
                        item_path = os.path.join(folder, item)
                        if os.path.isdir(item_path):
                            try:
                                threads.append(Thread(target=run_loop, args=(item_path,)))
                            except Exception as ex:
                                print("❌ Error-1: {}".format(ex))

                    for thread in threads:
                        thread.start()

                    for thread in threads:
                        thread.join()

                except Exception as ex:
                    print("❌ Error-2: {}".format(ex))
        except Exception as ex:
            print("❌ Error-3: {}".format(ex))

    run_loop(path)
    return empty_folders

def delete_folders(folders, deleted_folders):
    for folder in folders:
        try:
            if os.path.isdir(folder):
                os.rmdir(folder)
                deleted_folders[0] += 1
                print("🗑️ Deleted {}".format(minimize_path(folder)))
        except Exception as ex:
            print("❌ Error-4: {}".format(ex))

def main():
    global path
    path = os.path.normpath(input("📁 Path to folder to check for empty folders: ")).replace("\\", "/")
    if not os.path.isdir(path):
        print("❌ Path must be an existing folder")
        return

    recursively = get_user_confirmation("🔁 Recursively (check child folders)?")

    while True:
        empty_folders = find_empty_folders(path, recursively)
        folders_to_delete = len(empty_folders)

        if folders_to_delete > 0:
            if get_user_confirmation("🗑️ Delete {} empty folders?".format(folders_to_delete)):
                print("🚮 Deleting folders")

                threads = []
                thread_count = min(len(empty_folders), 10)
                deleted_folders = [0]

                print("🧬 Creating threads")
                for i in range(thread_count):
                    start = i * len(empty_folders) // thread_count
                    end = (i + 1) * len(empty_folders) // thread_count
                    threads.append(Thread(target=delete_folders, args=(empty_folders[start:end],deleted_folders,)))

                print("🔨 Starting {} threads".format(len(threads)))
                for thread in threads:
                    thread.start()

                print("⌛ Waiting for threads to finish")
                for thread in threads:
                    thread.join()

                print("✅ Deleted {} folders".format(deleted_folders[0]))
                if recursively and get_user_confirmation("💫 Rerun to check if new empty folders where created?"):
                    continue
            else:
                print("❌ No folders were deleted")
        else:
            print("✅ No empty folders found")
        break

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n🛑 Exiting")
            exit()
        except Exception as ex:
            print("❌ Fatal error: {}".format(ex))

        print("\n🔄 Restarting\n")
