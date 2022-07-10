import os
from tqdm import tqdm

path = 'test-folder'

files = os.listdir(path)

for file in tqdm(files):
    filename, filetype = file.split('.')
    if filetype == 'jpg':
        continue

    txtfile = os.path.join(path, file)
    jpgfile = os.path.join(path, filename + '.jpg')
    if not os.path.exists(jpgfile):
        print('{} deleted.'.format(txtfile))
        os.remove(txtfile)