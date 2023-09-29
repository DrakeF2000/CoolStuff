import matplotlib.pyplot as plt
import numpy

# A SIMPLE LINE GRAPH
'''
x, y = [1,3,5,7],[2,4,6,1]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("A simple line graph")
plt.show()
'''

# A SIMPLE BAR GRAPH
'''
heights = [10,20,30,15,40]
bar_labels = ['One','Two','Three','Four','Five']
plt.bar(bar_labels, heights, width=0.6, color=['red','black'])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("A simple bar graph")
plt.show()
'''

# A SIMPLE PI GRAPH
'''
data = [25, 20, 50, 5]
labels = ['white birds', 'blue birds', 'black birds', 'purple birds']
plt.pie(data)
plt.title("A simple pi graph")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(labels)
plt.show()
'''

# Plotting a function
'''
def func(x):
    return numpy.sin(x)
x = numpy.linspace(-numpy.pi, numpy.pi, 100)
y = func(x)
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Func(x)")
plt.title("Plotting a function: sin(x)")

custom_yticks = numpy.arange(-5, 10, 10)
custom_ylabels = [str(tick) for tick in custom_yticks]
plt.yticks(custom_yticks, custom_ylabels)

plt.show()
'''