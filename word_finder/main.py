import os
os.chdir('C:/Users/prami/OneDrive/Desktop/py-projekts/word_finder')

files_path = os.path.join(os.curdir, 'words_directory')

files_full_path = [os.path.join(files_path, f) for f in os.listdir(files_path)]

print(files_full_path)
