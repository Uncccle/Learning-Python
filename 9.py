#---------集合--------
#两种： set（ ）/ A={}


s1={1, 2, 3, 4, 6, 7}
print(s1)
#集合没有顺序没有下标

s2={1, 2, 2, 4, 5}
print(s2)
#集合会去重


a = set("fsjfhsdfs")
print(a)
#---返回给你的是 一个一个的子集集合



#---------空集合--------

a1= set() #空集
print(a1)
print(type(a1))

a2={}
print(a2)#空集
print(type(a2))




#---------增加数据----------
#变量.add()
#-----增加的是单个数据------
B1={1, 2, 3, 4}
B1.add("Z")
print(B1)


#变量.update()
#-------增加的是数据序列-------
B2={2, 3, 4, 5, 6}
B2.update([100, 200, 300])
print(B2)



#---------删除数据------------
# remove()
C1={10, 20, 30, 40}
C1.remove(10)
print(C1)
# 删除指定数据，如果数据不存在就报错


# discard()
C1.discard(100)
print(C1)
# 删除指定数据，如果数据不存在也不会报错

# pop()
J={10, 20, 30, 40}
Z=J.pop()
print(Z)
print(J)
# 随机删除任意一个数据，并且返回这个数据


#-------查找数据---------
#---in----
#---not in---

D1= {10, 20, 30, 40}
print(10 in D1)
print(100 not in D1)
print(100 in D1)
















