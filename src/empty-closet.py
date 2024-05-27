from pathlib import Path
import shutil
import os

# get user input - directory to unsweep closet
print('CURRENT DIR:', os.getcwd())
# exit()

dst = input("Type or paste in the directory containing the closet to be emptied (defaults to current): ")

if dst == '':
  dst = Path.cwd();
else:
  dst = Path(dst)
src = dst / 'closet'

if not src.exists():
  print(f'Error: no closet exists in {dst}')
  exit(1)
else:
  print(f'Thank you.\nBegin emptying: \'{src}\'...')

# iterate over all files in closet to be emptied

folder_count = 0
file_count = 0
unknown_count = 0

for item in src.iterdir():
  if item.is_dir():
    for sub_item in item.iterdir():
      print('in dir', sub_item, sub_item.name)
      if sub_item.is_dir():
        folder_count += 1
      elif sub_item.is_file():
        file_count += 1
      else:
        unknown_count += 1
      shutil.move(sub_item, dst / sub_item.name)
  elif item.is_file():
    print('straight file', item, item.name)
    shutil.move(item, dst / item.name)
    file_count += 1
  else:
    unknown_count += 1

# delete closet
if os.getcwd() == src:
  os.chdir('..')
shutil.rmtree(src, ignore_errors=True) #TODO:  make this remove 'closet' base folder

# done, print msg lettin user know
print('Done!')
print(f'Emptied: {folder_count} folders & {file_count} files.')
if unknown_count > 0:
  print(f'(Additional: {unknown_count} items of unknown type).')