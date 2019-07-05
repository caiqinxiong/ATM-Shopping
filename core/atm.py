# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'

from core import users as u

class ATM(object):
    '''ATM类'''

    def deposit(self,userID,money):
        '''存款'''
        # 调用用户类的获取用户信息方法
        users = u.Users().getUser()
        try:
            users[userID]['money'] = int(users[userID]['money']) +  money
        except:
            # 第一次存钱
            users[userID]['money'] = money
        # 调用用户类，重新写入用户信息
        u.Users().setUser(users)
        #print('账户%s已存入%s元！' % (users[userID]['username'],money) )
        #print('总余额为： %s 元' % users[userID]['money'])
        return True

    def withdrawals(self,userID,money):
        '''取款'''
        users = u.Users().getUser()
        int(users[userID]['money'])
        try:
            if money > users[userID]['money']:
                print('余额不足！！')
                return False
            else:
                users[userID]['money'] -= money
        except:
            print('余额不足！')
            return False
        u.Users().setUser(users)
        #print('账户%s已取出%s元！' % (users[userID]['username'],money) )
        #print('总余额为： %s 元' % users[userID]['money'])
        return True

    def transfer(self,userID1,userID2,money):
        '''转账'''
        # 直接调用取款、存款函数，取款成功了再存款。
        if self.withdrawals(userID1,money):
            self.deposit(userID2,money)
            return True
        return False

    def queryBalance(self,userID):
        '''查询余额'''
        users = u.Users().getUser()
        print('账户%s的余额为：\n%s元' % (users[userID]['username'],users[userID]['money']))

    def turnBack(self):
        '''返回上级菜单'''
        print(''.center(15,'*'))
        print( "1、返回上级")
        print( "2、退出")
        print(''.center(15,'*'))
        while True:
            choise = input("请选择：")
            if choise == '1':
                self.atmOperation(userID)
            elif choise == '2':
                print ("谢谢使用！")
                exit(-1)
            else:
                print ("输入有误，请重新输入！")

    def inputMoney(self):
        '''输入金额'''
        money = input()
        if money.isdigit():
            return int(money)
        else:
            print('输入不是有效数字！')
        return  self.turnBack()

    def atmOperation(self,userID):
        '''ATM操作，总入口函数'''

        print('''请选择：
        1、存款
        2、取款
        3、转账
        4、查询余额
        5、修改密码''')
        while True:
            choise=input().strip()
            if '1' == choise:
                # 存款
                print('请输入存款金额：')
                money = self.inputMoney()
                self.deposit(userID,money)
                print('存入%s元成功！' % (money))
                self.turnBack()
                break
            elif '2' == choise:
                # 取款
                print('请输入取款金额！')
                money = self.inputMoney()
                self.withdrawals(userID,money)
                print('已取出%s元！请收好！' % (money) )
                self.turnBack()
                break
            elif '3' == choise:
                # 转账
                username = input('请输入要转账的账户名：')
                checkUser =  u.Users().checkUser(username)
                if checkUser:
                    print('请输入要转账金额:')
                    money = self.inputMoney()
                    userID2 = u.Users().getUserID(username)
                    self.transfer(userID,userID2,money)
                    print('已成功向%s转账%s元！' % (username, money))
                else:
                    print('账户不存在！')
                self.turnBack()
                break
            elif '4' == choise:
                # 查询余额
                self.queryBalance(userID)
                self.turnBack()
                break

            elif '5' == choise:
                # 修改密码
                u.Users().changePasswd(userID)
                self.turnBack()
                break
            else:
                print('输入有误！')

if __name__ == '__main__':
    atm = ATM()
    userID = u.Users().userLoggin()
    if userID:
        atm.atmOperation(userID)