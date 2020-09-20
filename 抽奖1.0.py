import random
print("""欢迎使用飞宇抽奖系统（beta）
按下回车抽奖""")
list= ["花","赛车","谢谢参与","洋娃娃","汉堡","小鸟玩偶","编程猫玩偶","积木套装","谢谢参与","城堡玩具","玩具相机","西瓜汁","遥控飞机","草莓汁","汉堡","橙汁","谢谢参与"]
L=len(list)
while True:
    input()
    a=random.randint(0,L)
    print("恭喜你抽中了“",list[a],"”","""
再次抽奖按下回车,若结束抽奖请输入退出""")
    c=input(" ")
    if "退出"in c:
        break
    elif " "in c:
        continue


