import os


def get_images(path):
    '''
    find image files in test data path
    :return: list of files found
    '''
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
	        for ext in exts:
                if filename.endswith(ext):
                    if filename[:-4] in files:
                        # print filename
                        os.remove(os.path.join(path,filename))
                    else:
                        files.append(filename[:-4])
                        break
    print('Find {} images'.format(len(files)))
    return files

def get_txts(path):
    '''
    find image files in test data path
    :return: list of files found
    '''
    files = []
    exts = ['txt']
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
	        for ext in exts:
                if filename.endswith(ext):
                   if filename[:-4] in files:
                        # print filename
                        os.remove(os.path.join(path,filename))
                    else:
                        files.append(filename[:-4])
                        break
    print('Find {} txts'.format(len(files)))
    return files

def match():
    image_name = get_images(path)
    txt_name = get_txts(path)
    for file in image_name:
        if file not in txt_name:
            print file+'.jpg'
            os.remove(os.path.join(path,file + '.jpg'))
    for file in txt_name:
        if file not in image_name:
            print file+'.txt'
            os.remove(os.path.join(path,file + '.txt'))
    

if __name__ == '__main__':
    path = '/home/zhangjian/vehicleplate_east_detect/val/image/'
    # tf.app.run()
    match()




