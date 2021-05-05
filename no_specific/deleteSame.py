import os
import argparse
import cv2
from skimage.metrics import structural_similarity
# import shutil
# def yidong(filename1,filename2):
#     shutil.move(filename1,filename2)
def delete(filename1):
    os.remove(filename1)
if __name__ == '__main__':
    ap = argparse.ArgumentParser()#创建对象
    ap.add_argument("-i", "--image", required=True, help="path to read image")
    args = vars(ap.parse_args())
    path = args["image"]
    img_path = path
    # print(img_path)
    imgs_n = []
    i=0
    num = []
    img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(path) for file in files if
                 (file.endswith('.jpg'))]
    print("开始删除相似图片")
    for currIndex, filename in enumerate(img_files):
        if not os.path.exists(img_files[currIndex]):
            print('not exist', img_files[currIndex])
            break
        img = cv2.imread(img_files[currIndex])
        img1 = cv2.imread(img_files[currIndex + 1])
        ssim = structural_similarity(img, img1, multichannel=True)
        if ssim > 0.2:
            imgs_n.append(img_files[currIndex + 1])
            # print(img_files[currIndex], img_files[currIndex + 1], ssim)
        else:
            i+=1
            # print('small_ssim',img_files[currIndex], img_files[currIndex + 1], ssim)
        currIndex += 1
        if currIndex >= len(img_files)-1:
            break
    for image in imgs_n:
        # yidong(image, save_path_img)
        delete(image)
    
    print("最终得到"+str(i+1)+"张图片")
