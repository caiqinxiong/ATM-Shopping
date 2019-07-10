# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
import time
import os

# 管理员账号密码
adminName = 'admin'
adminPassword = 'admin'

# 当前时间
timeYear = time.strftime('%Y%m%d', time.localtime(time.time()))
timeDay = time.strftime('%H%M%S', time.localtime(time.time()))

# 信用卡额度
creditLimit = 15000

# 用户信息文件
userInfoFile = "../db/user-info.json"

# 商品信息文件
goodsInfoFile = '../db/goods-info.json'

# 用户购物车文件
def ShoppingCarFile(username,year=timeYear,day=timeDay):
    dirs = '../db/shoppinCar'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    shoppingInfoFile = '%s/%s_shopping-info_%s%s.json' % (dirs,username,year,day)
    #print(shoppingInfoFile)
    return shoppingInfoFile
