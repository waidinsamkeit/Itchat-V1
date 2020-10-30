#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 检测import是否进行导入
import os,time
print("""提示：该程序接口仅限微信Web版本使用
Module check starting.......
* itchat：微信网页版接口封装Python版本，在本文中用以获取微信好友信息。 
* jieba：结巴分词的 Python 版本，在本文中用以对文本信息进行分词处理。 
* matplotlib： Python 中图表绘制模块，在本文中用以绘制柱形图和饼图 
* snownlp：一个 Python 中的中文分词模块，在本文中用以对文本信息进行情感判断。 
* pillow： Python 中的图像处理模块，在本文中用以对图片进行处理。 
* numpy： Python中 的数值计算模块，在本文中配合 wordcloud 模块使用。 
* wordcloud： Python 中的词云模块，在本文中用以绘制词云图片。 
* TencentYoutuyun：腾讯优图提供的 Python 版本 SDK ，在本文中用以识别人脸及提取图片标签信
  息。
项目地址: https://github.com/waidinsamkeit/Itchat-V1
""")
time.sleep(5)
try:
    import itchat
    import jieba
    import matplotlib
    import snownlp
    import PIL
    import wordcloud
    import TencentYoutuyun
except ImportError:
    print("Module does not exist, installing for you")
    installs = os.system("pip install itchat jieba matplotlib")
    installs2 = os.system("pip install pillow numpy wordcloud")
    print("Install Successfuly")
else :
    print("依赖环境监测完成")
