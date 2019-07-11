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
    dirs = '../db/shoppinCar/%s' % username
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    shoppingInfoFile = '%s/shopping-info_%s%s.json' % (dirs,year,day)
    #print(shoppingInfoFile)
    return shoppingInfoFile

# 日志文件
logFile = '../log/atm.log'

# log功能,使用装饰器
def log(func):
    def wrapper(*args, **kwargs):
        f = open(logFile, "a", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t"+func.__doc__+"\n")
        f.close()
        return func(*args, **kwargs)
    return wrapper

















