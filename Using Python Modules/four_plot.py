#from numpy import *
#from matplotlib.pyplot import *
#from numpy import linspace, pi, sin
#from matplotlib.pyplot import plot, legend, annotate
#from matplotlib.pyplot import xlim, ylim, title, show
x=linspace(-5*pi, 5*pi, 500)
plot(x, x, 'b')
plot(x, -x, 'b')
plot(x, sin(x), 'g', linewidth=2)
plot(x, x*sin(x), 'r', linewidth=3)
legend(['x', '-x', 'sin(x)', 'xsin(x)'])
annotate('origin', xy = (0, 0))
title('Four Plot')
xlim(-5*pi, 5*pi)
ylim(-5*pi, 5*pi)
show()
