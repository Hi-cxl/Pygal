import pygal
from die import Die

#创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#将结果储存在一个列表中
results = []
for roll_num in range(50000):
    #计算每次的总点数
    result = die_1.roll() + die_2.roll(）
    results.append(result)

#分析结果
frequencies = []
#将可能出现的最大点数储存在max_result中
max_result = die_1.num_sides + die_2.num_sides
#2为可能出现的最小点数
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()
#标题
hist.title = "Results of rolling  D6 and D10 dice 50000 times."
#x轴
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
#x，y轴名称
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')