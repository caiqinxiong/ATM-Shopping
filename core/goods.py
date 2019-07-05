# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'

import sys
from conf import settings as ss
import json

class Goods(object):
    '''商品类'''

    def getGoods(self):
        '''获取账户信息'''
        try:
            with open(ss.goodsInfoFile, "r", encoding="utf-8") as f:
                goods = json.load(f)
                #print(goods)
        except:
            print('have no goods inof!')
            goods = []
        #print(goods)
        return goods

    def setGoods(self,goods):
        '''写入商品信息'''
        with open(ss.goodsInfoFile, "w", encoding="utf-8") as f:
            json.dump(goods, f, ensure_ascii=False, indent="\t")

    def printGoods(self):
        '''打印商品列表'''
        goods = self.getGoods()
        for name,price in goods:
            print(name,"\t",price)

    def checkPrice(self,price):
        '''校验输入的价格是否为有效数字'''
        if price.isdigit():
            return int(price.strip())
        else:
            print('请输入有效数字！')
            return False

    def checkName(self,name):
        '''校验商品名称是否存在'''
        goods = self.getGoods()
        for goodName,price in goods:
            if name == goodName:
                return True
        return False

    def goodsShelves(self):
        '''商品上架'''
        name = input("请输入要上架的商品名称").strip()
        if self.checkName(name):
            print('商品已存在！')
            return False
        price=input("请输入该商品的价格")
        if self.checkPrice(price):
            goods = self.getGoods()
            goods.append([name,int(price)])
            self.setGoods(goods)
            return True

    def goodDelete(self):
        '''商品下架'''
        name = input("请输入要下架的商品名称").strip()
        if not self.checkName(name):
            print('商品不存在！')
            return False
        else:
            goods = self.getGoods()
            for goodName,goodsPrice in goods:
                if goodName == name:
                    goods.remove([goodName,goodsPrice])
                    #print(goods)
                    self.setGoods(goods)
                    return True
    def goodModify(self):
        '''修改商品价格'''
        name = input("请输入要修改商品价格的名称").strip()
        if not self.checkName(name):
            print('商品不存在！')
            return False
        else:
            goods = self.getGoods()
            for goodName,goodsPrice in goods:
                # 获取商品在list中的index值
                index = goods.index([goodName,goodsPrice])
                #print(index)
                print('商品原价格为：')
                print(name,'\t',goods[index][1])
                price=input("请要修改商品的价格")
                if self.checkPrice(price):
                    if goodName == name:
                        goods[index][1] = int(price)
                        self.setGoods(goods)
                        print('商品价格修改完成！')
                        print(goods[index][0],"\t",goods[index][1])
                        return True

"""
def readGoogs():
    '''读取商品文件'''
    try:
        with open('goodsList.txt','r') as f:
            goods=f.readlines()
    except:
        print("文件未存在！")
        sys.exit(-1)
    return goods

def getGoods():
    '''获取商品信息'''
    good_list = []
    for good in readGoogs():
        good_list.append(good.split())

    return dict(good_list)

def printGoods():
    '''打印商品'''
    print("商品列表如下：")
    for index,item in enumerate(readGoogs()):
        print "%s\t%s" % (index+1,item)


def goodsShelves():
    '''商品上架'''
    name=raw_input("请输入要上架的商品名称")
    if getGoods().has_key(name):
        print('上架商品已存在！')
        sys.exit(-1)
    price=raw_input("请输入该商品的价格")
    f = open('goodsList.txt','a')
    f.write(name + "\t" + price + "\n")
    print('已经将商品\033[31;1m%s\033[0m上架完成') % name
    f.flush()
    f.close()
    printGoods()

def goodDelete():
    '''商品下架'''
    name=raw_input("请输入要下架的商品名称")
    if getGoods().has_key(name):
        # 要先对文件读，再覆盖写入
        goods = readGoogs()
        with open('goodsList.txt','w') as f_w:
            for line in goods:
                # 写入时跳过要下架的商品即可
                if name in line:
                    continue
                f_w.write(line)
        print('已经将商品\033[31;1m%s\033[0m下架完成') % name
        printGoods()

    else:
        print('下架的商品不存在！')
        sys.exit(-1)

def goodModify():
    '''修改商品价格'''
    printGoods()
    name=raw_input("请输入要修改商品价格的名称")
    if getGoods().has_key(name):
        price=raw_input("请输入要修改商品的价格")
        goods = readGoogs()
        with open('goodsList.txt','w') as f_w:
            for line in goods:
                # 写入时跳过要下架的商品即可
                if name in line:
                    f_w.write(name+'\t'+price+'\n')
                    continue
                f_w.write(line)
        printGoods()
    else:
        print('修改的商品不存在！')
        sys.exit(-1)

def goodSearch():
    '''商品搜索'''
    name=raw_input("请输入搜索商品名称")
    if getGoods().has_key(name):
        for line in readGoogs():
            if name in line:
                print("搜索的商品价格为：%s" % line)
                break
    else:
        print('搜索的商品不存在！')
        sys.exit(-1)

def userChoice():
    '''用户选择'''
    print("欢迎登录XXX系统后台，请选择操作")
    print("1、商品上架")
    print("2、商品下架")
    print("3、修改商品价格")
    print("4、商品查询")
    print("5、退出")
    choice = input('请选择：')
    if choice.isdigit():
        choice = int(choice)
        if 1 == choice:
            goodsShelves()
        elif 2 == choice:
            goodDelete()
        elif 3 == choice:
            goodModify()
        elif 4 == choice:
            goodSearch()
        elif 5 == choice:
            print("谢谢使用！")
            sys.exit(-1)
        else:
            print("输入有误，请重新输入")
            userChoice()
    else:
        print("请输入有效数字！")
        userChoice()
"""
if __name__ == '__main__':
    goods = Goods()
    #goods.goodsShelves()
    goods.printGoods()
    #goods.goodDelete()
    goods.goodModify()
