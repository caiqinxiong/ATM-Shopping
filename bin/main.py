# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/7/10 16:57

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import goods as g
from core import atm as a
from conf import settings as ss
from core import users as u
from core import shopping as s

def checkAdmin():
    '''校验管理员账号密码'''
    i = 2
    while i >= 0:
        username = input('请输入管理员账号：')
        if username == ss.adminName:
            j = 2
            while j >= 0:
                password = input('请输入管理员密码：')
                if password == ss.adminPassword:
                    return True
                else:
                    print('管理员密码输入有误！')
                    if j == 0:
                        print('账号已锁定，请10分钟后重新尝试！')
                        return False
                    else:
                        print('你还有%s次尝试机会！' % j)
                j -=1

        else:
            print('管理员账号输入有误！')
            if i != 0:
                print('你还有%s次尝试机会！' % i)
            else:
                print('账号已锁定，请10分钟后重新尝试！')
        i -=1
    return False

def averageUser():
    '''普通用户操作'''
    print('''请选择操作：
    1、购买商品
    2、ATM操作''')
    while True:
        choice = input().strip()
        if '1' == choice:
            s.run()
            break
        elif '2' == choice:
            a.run()
            break
        else:
            print('输入有误！')

def adminManagement():
    '''管理员操作'''
    print('''请选择操作：
    1、商品管理
    2、用户管理''')
    while True:
        choice = input().strip()
        if '1' == choice:
            g.run()
            break
        elif '2' == choice:
            u.run()
            break
        else:
            print('输入有误！')


def run():
    '''程序入口函数'''
    print('''欢迎进入ATM+购物程序!
    请选择操作：
    1、普通用户
    2、管理员''')
    while True:
        choice = input().strip()
        if '1' == choice:
            averageUser()
            break
        elif '2' == choice:
            if checkAdmin():
                adminManagement()
            break
        else:
            print('输入有误！')


if __name__ == '__main__':
    run()
