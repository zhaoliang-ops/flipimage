from PIL import Image
import os.path
from controller.mq.publish import Publish
  # rootdir 是被遍历的文件夹
class FlipImage:
    def flipImage(currentPath):
      im = Image.open(currentPath)
      out = im.transpose(Image.FLIP_LEFT_RIGHT)#实现翻转
      newname=r"../Images/"+"fliped"+os.path.basename(currentPath)#重新命名
      out.save(newname)#保存结束
       # 翻转之后推入队列
      Publish.public(newname)
