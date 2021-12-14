from matplotlib import pyplot as plt
# import matplotlib.font_manager as fm
# zhfont1 = fm.FontProperties(fname='C:\Windows\Fonts\FrederickatheGreat-Regular.ttf')
x = range(15, 25)
y1 = [50, 55, 58, 65, 70, 68, 70, 72, 75, 70]
y2 = [60, 53, 60, 63, 65, 68, 75, 80, 85, 72]
plt.figure(figsize=(10, 6), dpi=80)
plt.title('体重年龄折线图')
plt.xlabel('年龄（岁）')
plt.ylabel('体重（kg）')
plt.plot(x, y1, color='red', label='张三')
plt.plot(x, y2, color='blue', label='李四')
# 添加网格，alpha 为透明度
plt.grid(alpha=0.5)
# 添加图例
plt.legend(loc='upper right')
plt.show()
