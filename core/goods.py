# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'

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
        print(''.center(20,'-'))
        print('所有商品列表如下：')
        print(''.center(20,'-'))
        print('名称\t价格')
        print(''.center(20,'-'))
        for name,price in goods:
            print(name,"\t",price)
            print(''.center(20,'-'))

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
            print('商品\033[32;1m%s\033[0m已上架完成！价格为：\033[32;1m%s\033[0m' % (name,int(price)))
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
                    print('商品\033[41;1m%s\033[0m已下架成功！' % name)
                    self.setGoods(goods)
                    return True

    def goodSearch(self,name):
        '''商品搜索查询'''
        if not self.checkName(name):
            print('商品不存在！')
            return False
        else:
            goods = self.getGoods()
            for goodName,goodsPrice in goods:
                if name == goodName:
                    # 获取商品在list中的index值
                    index = goods.index([goodName,goodsPrice])
                    #print(index)
                    print('商品价格为：')
                    print(name,'\t',goods[index][1])
                    return (goods,index,True)

    def goodModify(self,name):
        '''修改商品价格'''
        goods,index,Flag = self.goodSearch(name)
        #print(Flag,'\n',goods,"\n",index)
        price=input("请要修改商品的价格")
        if self.checkPrice(price):
            goods[index][1] = int(price)
            self.setGoods(goods)
            print('商品价格修改完成！')
            print(goods[index][0],"\t","\033[32;1m%s\033[0m"  % goods[index][1] )
            return True

    def turnBack(self):
        '''返回上级菜单'''
        print(''.center(15,'*'))
        print( "1、返回上级")
        print( "2、退出")
        print(''.center(15,'*'))
        while True:
            choise = input("请选择：")
            if choise == '1':
                self.goodManagement()
            elif choise == '2':
                print ("谢谢使用！")
                exit(-1)
            else:
                print ("输入有误，请重新输入！")

    def goodManagement(self):
        '''用户选择'''
        print("请选择操作：")
        print("1、打印商品列表")
        print("2、商品上架")
        print("3、商品下架")
        print("4、修改商品价格")
        print("5、商品查询")
        while True:
            choice = input().strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 == choice:
                    # 打印商品列表
                    self.printGoods()
                    self.turnBack()
                    break
                elif 2 == choice:
                    # 商品上架
                    self.goodsShelves()
                    self.turnBack()
                    break
                elif 3 == choice:
                    # 商品下架
                    self.goodDelete()
                    self.turnBack()
                    break
                elif 4 == choice:
                    # 修改商品价格
                    name = input("请要修改商品价格的名称：").strip()
                    self.goodModify(name)
                    self.turnBack()
                    break
                elif 5 == choice:
                    # 商品查询
                    name = input("请输入要查询商品价格的名称:").strip()
                    self.goodSearch(name)
                    self.turnBack()
                    break
                else:
                    print("输入有误，请重新输入")
            else:
                print("请输入有效数字！")

def run():
    goods = Goods()
    goods.goodManagement()

if __name__ == '__main__':
    run()
