from pathlib import Path
import shutil

# get user input - directory to clean up

while True:
  src = input("Type or paste in the directory you want to clean up (defaults to current): ")
  src = Path(src)

  if src.exists():
    break
  else:
    print(f'Path \'{src}\' does not exist')

dst = src / 'closet'

print(f'Thank you.\nBegin clean-sweeping: \'{dst}\'...')

# create closet folder
#   subfolders: txt, csv, folders

Path.mkdir(dst, exist_ok=True)
Path.mkdir(dst / 'txt', exist_ok=True)
Path.mkdir(dst / 'csv', exist_ok=True)
Path.mkdir(dst / 'folders', exist_ok=True)
print('building closet...')

# iterate over all files in dir, sort if one of 3 ^ -> rest into closet base 
#   if is closet, don't move
#   if folder contains .*temp.* in name, delete

folder_count = 0
file_count = 0

for item in src.iterdir():
  
  if item.is_dir():
    if item.name != 'closet':
      print(f'moving folder: {item.name}')
      if 'temp' in item.name:
        shutil.rmtree(src / item.name)
      else:
        shutil.move(src / item.name, dst / 'folders' / item.name)
      folder_count += 1

  elif item.is_file():
    print(f'moving file: {item.name}')
    if item.suffix == '.txt':
      shutil.move(src / item.name, dst / 'txt' / item.name)
    elif item.suffix == '.csv':
      shutil.move(src / item.name, dst / 'csv' / item.name)
    else:
      shutil.move(src / item.name, dst / item.name)
    file_count += 1

  else:
    print(f'unhandled item with unknown type: {item.name}')


# done, print msg lettin user know
print('Done!')
print(f'Cleaned: {folder_count} folders & {file_count} files.')