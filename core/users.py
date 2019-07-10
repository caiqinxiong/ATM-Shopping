# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'

from conf import settings as ss
import json

class Users(object):
    '''用户类，管理用户接口'''

    def getUser(self):
        '''获取账户信息'''
        try:
            with open(ss.userInfoFile, "r", encoding="utf-8") as f:
                users = json.load(f)
                #print(users)
        except:
            print('have no users inof!')
            users = {}
        return users

    def setUser(self,users):
        '''重新写入账户信息'''
        with open(ss.userInfoFile, 'w') as f :
            json.dump(users , f , indent="\t")
        #print(users)

    def checkUser(self,username):
        '''检查用户是否存在'''
        users = self.getUser()
        for userID in users.keys():
            if username == users[userID]['username']:
                #print('账户名已存在！')
                return True
        return False

    def getUserID(self,username):
        '''通过账户名获取账户id值'''
        users = self.getUser()
        for userID in users.keys():
            if username == users[userID]['username']:
                return userID
        print('账户不存在!!!')
        return self.turnBack()

    def addUser(self,username,password,phone=None,limit=ss.creditLimit,isLock=False):
        '''添加账户'''
        users=self.getUser()
        # 字典key值自动加1
        max_id = "000000"
        if users != {}:
            max_id = max(users.keys())

        userID = str(int(max_id) + 1).zfill(6)  # id自动+1，补足6位
        users[userID] = {
            'username':username,
            'password':password,
            'phone':phone,
            'limit':limit,
            'isLock':isLock
        }
        self.setUser(users)
        print(''.center(50,'#'))
        print('账户\033[42;1m%s\033[0m添加成功' % users[userID]['username'])
        print('账户名： %s' % users[userID]['username'])
        print('手机号： %s' % users[userID]['phone'])
        print('信用卡额度： %s' % users[userID]['limit'])
        print(''.center(50,'#'))
        return True

    def delUser(self,userID):
        '''账户注销'''
        users=self.getUser()
        try:
            print('账户\033[41;1m%s\033[0m已删除！' % users[userID]['username'])
            users.pop(userID)
        except:
            print('账户不存在！')
            return False
        self.setUser(users)
        return True

    def frozenUser(self,userID):
        '''冻结账户'''
        users=self.getUser()
        users[userID]['isLock'] = True
        self.setUser(users)
        print('账户%s已冻结！' % users[userID]['username'] )

    def thawUser(self,userID):
        '''解冻账户'''
        users=self.getUser()
        users[userID]['isLock'] = False
        self.setUser(users)
        print('账户%s已解除冻结！' % users[userID]['username'] )

    def userLoggin(self):
        '''用户登录验证'''
        for i in range (1,4):
            username = input('请输入用户名：')
            if self.checkUser(username):
                userID = self.getUserID(username)
                users=self.getUser()
                if users[userID]['isLock']:
                    print('账户已被冻结，请联系管理员！')
                    exit(-1)
                password = input('请输入密码：')
                if self.checkPassword(userID,password):
                    return username,userID
                else:
                    print('密码错误！')
            else:
                print('账户不存在！')
        print('操作过于频繁！')
        return False,False

    def checkPassword(self,userID,password):
        '''校验密码是否正确'''
        users = self.getUser()
        if password == users[userID]['password']:
            return True
        else:
            return False

    def changePasswd(self,userID):
        '''修改密码'''
        for i in range(1,4):
            old_passwd = input('请输入旧密码：')
            # 校验旧密码是否正确
            check = self.checkPassword(userID,old_passwd)
            if check:
                for j in range(1,4):
                    if j == 3:
                        print('操作过于频繁')
                        return False
                    new_passwd1 = input('请输入新密码：')
                    if len(new_passwd1) < 8:
                        print('密码不能少于8位！')
                        continue
                    if new_passwd1 == old_passwd:
                        print('新密码不能和旧密码一样！')
                        continue
                    new_passwd2 = input('请再次确认新密码：')
                    if new_passwd1 != new_passwd2:
                        print('两次输入的密码不一致！')
                        continue
                    else:
                        users=self.getUser()
                        users[userID]['password'] = new_passwd1
                        self.setUser(users)
                        print('密码修改成功！')
                        return True
            else:
                print('旧密码输入错误！')
        print('操作过于频繁。')
        return False

    def changePhone(self,userID,phone):
        '''修改手机号'''
        users=self.getUser()
        users[userID]['phone'] = phone
        self.setUser(users)
        print('手机号修改完成！')
        print('账户名： %s' % users[userID]['username'])
        print('手机号： %s' % users[userID]['phone'])

    def changeLimit(self,userID,limit):
        '''修改账户信用额度'''
        users=self.getUser()
        users[userID]['limit'] = limit
        self.setUser(users)
        print('账户%s的信用额度已更新为%s' % (users[userID]['username'],users[userID]['limit']))

    def turnBack(self):
        '''返回上级菜单'''
        print(''.center(15,'*'))
        print( "1、返回上级")
        print( "2、退出")
        print(''.center(15,'*'))
        while True:
            choise = input("请选择：")
            if choise == '1':
                self.userManagement()
            elif choise == '2':
                print ("谢谢使用！")
                exit(-1)
            else:
                print ("输入有误，请重新输入！")

    def userManagement(self):
        '''账户管理，总入口函数'''
        print('''请选择账户管理操作：
        1、账户信息查询
        2、添加新账户
        3、删除账户
        4、修改密码
        5、修改手机号
        6、冻结账户
        7、解冻账户
        8、修改账户信用额度''')

        while True:
            choise=input().strip()
            if choise.isdigit():
                if '1' == choise:
                    # 账户信息查询
                    users = self.getUser()
                    print(''.center(50,'#'))
                    for i in users.keys():
                        print('账户名： %s' % users[i]['username'])
                        print('手机号： %s' % users[i]['phone'])
                        print('信用卡额度： %s' % users[i]['limit'])
                        print(''.center(50,'#'))
                    self.turnBack()
                    break
                elif '2' == choise:
                    # 添加新账户
                    username = input('请输入用户名：')
                     # 校验用户名是否已存在
                    if self.checkUser(username):
                        print('账户已存在！')
                        self.turnBack()
                        break
                    password = input('请输入密码：')
                    phone = input('请输入手机号：')
                    self.addUser(username,password,phone)
                    self.turnBack()
                    break
                elif '3' == choise:
                    # 删除账户
                    username = input('请输入要删除的账号名：')
                    userID = self.getUserID(username)
                    self.delUser(userID)
                    self.turnBack()
                    break
                elif '4' == choise:
                    # 修改密码
                    username = input('请输入要修改密码的账号名：')
                    userID = self.getUserID(username)
                    self.changePasswd(userID)
                    self.turnBack()
                    break
                elif '5' == choise:
                    # 修改手机号
                    username = input('请输入要修改手机号的账号名：')
                    userID = self.getUserID(username)
                    phone = input('请输入新手机号：')
                    self.changePhone(userID,phone)
                    self.turnBack()
                    break
                elif '6' == choise:
                    # 冻结账户
                    username = input('请输入要冻结的账号名：')
                    userID = self.getUserID(username)
                    self.frozenUser(userID)
                    self.turnBack()
                    break
                elif '7' == choise:
                    # 解冻账户
                    username = input('请输入要解除冻结的账号名：')
                    userID = self.getUserID(username)
                    self.thawUser(userID)
                    self.turnBack()
                    break
                elif '8' == choise:
                    # 修改账户信用额度
                    username = input('请输入要更改信用额度的账号名：')
                    userID = self.getUserID(username)
                    limit = input('请输入要更改的信用额度：')
                    if limit.isdigit():
                        self.changeLimit(userID,limit)
                    else:
                        print('输入无效,更新失败！')
                    self.turnBack()
                    break

                else:
                    print('请输入有效数字！')

            else:
                print('请输入有效数字！')

def run():
    users=Users()
    users.userManagement()

if __name__ == '__main__':
    run()
