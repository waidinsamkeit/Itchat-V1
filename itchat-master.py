#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import check_module
import itchat
# 登录后给微信文件助手发消息测试!
itchat.auto_login()
itchat.send('Hello, filehelper', toUserName='filehelper')
# 获取微信好友数据列表
itchat.auto_login(hotReload = True)
friends = itchat.get_friends(update = True)
