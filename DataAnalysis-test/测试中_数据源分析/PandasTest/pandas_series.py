import pandas as pd
# pandas.Series( data, index, dtype, name, copy)
# 参数说明：
#     data：一组数据(ndarray 类型)。
#     index：数据索引标签，如果不指定，默认从 0 开始。index = ["x", "y", "z"] 指定元素的index
#     dtype：数据类型，默认会自己判断。
#     name：设置名称。
#     copy：拷贝数据，默认为 False。

#array[] 数据类型
studen = ["id","name","email"]
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

#字典 类型
a = pd.Series(studen,name="李华",index = ["x", "y", "z"])
print("数据结构： "+a["z"])

myvar = pd.Series(sites, index = [1, 2])
print(myvar)