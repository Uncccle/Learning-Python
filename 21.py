#   面向对象    #


#   面向对象的过程中，有两个重要的组成部分：
#   类   和   对象


#   必须先有类   再有对象

#  类和对象的关系：
#                   用类去创建一个对象



#   例如： 洗衣机
#   洗衣机有：放水，洗衣，抽水，甩干等功能
#这些功能就是： 函数


# 类：其实就是设计洗衣机的图纸，抽象的

#  对象：实物,例如洗衣机等




#类
#语法：
#   class 类名():
#       代码
#       ......





#   需求：洗衣机
#   功能：能洗衣服

# 1.定义洗衣机的类
"""
class 类名():
    代码

"""

class washer():
    def wash(self):
        print("能洗衣服！")



# 2.创建对象
# 对象名 = 类名()
Haier = washer()



# 3.验证成果
# 打印Haier对象
print(Haier)

#使用wash功能 -- 实例方法/对象方法 -- 对象名.wash()
Haier.wash()





#

























