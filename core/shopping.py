# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import goods as g
from core import atm as a
from conf import settings as ss
from core import users as u
import json

class ShoppingCar(object):
    '''用户购物'''

    def getBuyList(self,username):
        '''读取用户购物车清单'''
        try:
            with open(ss.ShoppingCarFile(username), "r", encoding="utf-8") as f:
                buyList = json.load(f)
                #print(buyList)
        except:
            print('have no goods inof!')
            buyList = []
        #print(buyList)
        return buyList

    def setBuyList(self,username,buyList):
        '''将用户购物清单写入文件中'''
        with open(ss.ShoppingCarFile(username), "w", encoding="utf-8") as f:
            json.dump(buyList, f, ensure_ascii=False, indent="\t")

    def printBuyList(self,username):
        '''打印购物车列表'''
        sum = 0
        buyList = self.getBuyList(username)
        print(''.center(20,'-'))
        print('购买商品列表如下：')
        print(''.center(20,'-'))
        print('名称\t价格')
        print(''.center(20,'-'))
        for name,price in buyList:
            print(name,"\t",price)
            sum = sum + int(price)
        print(''.center(20,'-'))
        print('总计：\t %s' % sum)
        return sum

    def buyList(self,username,choice):
        '''请选择购物'''
        buyList = self.getBuyList(username)
        goods = g.Goods().getGoods()
        if choice < len(goods) and choice >=0:
            print(goods[choice])
            buyList.append(goods[choice])
            #print(buyList)
            self.setBuyList(username,buyList)
            print('加入购物车成功')
        else:
            print('商品未上架！')
        return buyList

    def shopping(self,username,userID):
        '''购物'''
        goods = g.Goods().printGoods()
        print(goods)
        while True:
            print('请选择，停止购物按q')
            choice = input().strip()
            if choice != 'q':
                if choice.isdigit():
                    choice = int(choice)
                    self.buyList(username,choice)
                else:
                    print('请输入有效数字！')
            else:
                # 获取购物车总价
                sum = self.printBuyList(username)
                print('开始结算！')
                password = input('请输入银行卡密码：')
                if u.Users().checkPassword(userID,password):
                    # 调用银行卡接口结算
                    if a.ATM().withdrawals(userID,sum):
                        print('结算成功！')
                        return True
                    else:
                        print('结算失败！')
                else:
                    print('密码错误！')

                # 清空本次购物信息
                buyList = ['结算失败！']
                self.setBuyList(username, buyList)
                return False


def run():
    s = ShoppingCar()
    print('欢迎登录XXX网上购物商城！')
    # 登录验证，通过后返回userID值
    username,userID = u.Users().userLoggin()
    if userID:
        s.shopping(username,userID)

if __name__ == '__main__':
    run()