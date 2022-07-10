import os
from tqdm import tqdm

path = 'test-folder'

files = os.listdir(path)

for file in tqdm(files):
    filename, filetype = file.split('.')
    if filetype == 'txt':
        continue

    imgfile = os.path.join(path, file)
    txtfile = os.path.join(path, filename + '.txt')
    if not os.path.exists(txtfile):
        print('{} deleted.'.format(imgfile))
        os.remove(imgfile)