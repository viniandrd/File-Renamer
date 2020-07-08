import os

def rename_folder(path):
    count = 0
    for image in os.listdir(path):
        count += 1
        path_to_image = path

        if (image.endswith('.jpg') or image.endswith('.JPG')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Image' + str(count) + '.jpg')
            except FileExistsError:
                print('File already exists, skipping this one..')

        if (image.endswith('.png') or image.endswith('.PNG')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Image' + str(count) + '.png')
            except FileExistsError:
                print('File already exists, skipping this one..')

        if (image.endswith('.heic') or image.endswith('.HEIC')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Image' + str(count) + '.heic')
            except FileExistsError:
                print('File already exists, skipping this one..')

        if (image.endswith('.mov') or image.endswith('.MOV')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Video' + str(count) + '.mov')
            except FileExistsError:
                print('File already exists, skipping this one..')

        if (image.endswith('.mp4') or image.endswith('.MP4')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Video' + str(count) + '.mp4')
            except FileExistsError:
                print('File already exists, skipping this one..')

        if (image.endswith('.jpeg') or image.endswith('.JPEG')):
            try:
                os.rename(path_to_image + image, path_to_image + 'Image' + str(count) + '.jpeg')
            except FileExistsError:
                print('File already exists, skipping this one..')


def find_files(path):
    if(os.path.isfile(path)):
        print('File found')
    else:
        for thing in os.listdir(path):
            if(os.path.isdir(path + thing)):
                folders_w_images = path + thing + '/'
                find_files(folders_w_images)
                print(folders_w_images)
                rename_folder(folders_w_images)

            elif (os.path.isfile(path + thing)):
                find_files(path + thing)

#if '__name__' == '__main__':
path = ''
find_files(path)