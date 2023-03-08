import os

files_path = os.path.join(os.curdir, 'words_directory')

files_full_path = [f for f in os.listdir(files_path)]
print(files_full_path)
