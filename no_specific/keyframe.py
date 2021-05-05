import numpy as np
import argparse
import cv2
import os

# 从.mp4 数据类型的视频中提取图像
def splitFrames_mp4(video_path, save_path):

    basename=os.path.basename(video_path)
    name,ext=os.path.splitext(basename)
    times = 0
    # 提取视频的频率，每25帧提取一个
    # frameFrequency = 25
    # 输出图片到当前目录vedio文件夹下
    outPutDirName = save_path + "\\"
    # 如果文件目录不存在则创建目录
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)

    camera = cv2.VideoCapture(video_path)
    print("视频开始提取图片")
    while True:
        times+=1
        res, image = camera.read()
        if not res:
            # print('not res , not image')
            break

        # if times%frameFrequency==0:
        #     cv2.imwrite(outPutDirName + str(times)+'.jpg', image)
        #     print(outPutDirName + str(times)+'.jpg')

        cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
        # print(times)
    print('图片提取结束')
    print('共有'+str(times)+'张图片')
    camera.release()
    os.system("python D:\All_VScodefiles\VScode_Python_code\deleteSame.py --image "+outPutDirName)
    # print("python deleteSame.py --image "+outPutDirName)

if __name__ == '__main__':

    ap = argparse.ArgumentParser()#创建对象
    ap.add_argument("-m", "--mp4", required=True,help="path to input mp4")
    ap.add_argument("-s", "--save", required=True,help="path to output image")
    args = vars(ap.parse_args())
    video_path = args["mp4"]
    save_path = args["save"]
    splitFrames_mp4(video_path,save_path)

