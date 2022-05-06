import os
from PIL import Image


def PNG_to_JPG(from_path, to_path):
    pics = os.listdir(from_path)

    for i in range(len(pics)):
        try:
            temp = pics[i]
            img = Image.open(from_path + "/" + temp)
            img = img.convert("RGB")
            img.save(to_path + "/" + temp.split(".")[0] + ".jpg")
        except:
            print(i)


if __name__ == "__main__":
    from_path = "/Users/gavin/Downloads/archive/images" # path of png images
    to_path = "/Users/gavin/Downloads/SP22_ML_final_project/VOCdevkit/VOC2007/JPEGImages" # path to store the jpg images
    
    PNG_to_JPG(from_path, to_path)
