# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
import time
import os
from core import users as u

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
        users = u.Users().getUser()
        f = open(logFile, "a", encoding="utf-8")
        if func.__doc__ != '查询余额' and func.__doc__ != '修改密码':
            f.write('%s\t%s%s%s元\n' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),users[args[1]]['username'],func.__doc__,args[-1]))
        else:
            f.write('%s\t%s%s\n' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),users[args[1]]['username'],func.__doc__))
        f.close()
        return func(*args, **kwargs)
    return wrapper

# 可以传入参数的装饰器例子
def decrator(*dargs, **dkargs):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print ("装饰器参数:", dargs, dkargs)
            print ("函数参数:", args, kargs)
            return func(*args, **kargs)
        return _wrapper
    return wrapper

# 装饰器学习链接
# https://www.cnblogs.com/wupeiqi/articles/4980620.html
# https://blog.csdn.net/weixin_42359464/article/details/80671769













