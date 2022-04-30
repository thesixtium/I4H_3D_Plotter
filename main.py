'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib, time

class plot3dClass( object ):

    def __init__( self, systemSideLength, lowerCutoffLength ):
        self.systemSideLength = systemSideLength
        self.lowerCutoffLength = lowerCutoffLength
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot( 111, projection='3d' )
        self.ax.set_zlim3d( -10e-9, 10e9 )

        rng = np.arange( 0, self.systemSideLength, self.lowerCutoffLength )
        self.X, self.Y = np.meshgrid(rng,rng)

        self.ax.w_zaxis.set_major_locator( LinearLocator( 10 ) )
        self.ax.w_zaxis.set_major_formatter( FormatStrFormatter( '%.03f' ) )

        heightR = np.zeros( self.X.shape )
        self.surf = self.ax.plot_surface(
            self.X, self.Y, heightR, rstride=1, cstride=1,
            cmap=cm.jet, linewidth=0, antialiased=False )
        # plt.draw() maybe you want to see this frame?

    def drawNow( self, heightR ):
        self.surf.remove()
        self.surf = self.ax.plot_surface(
            self.X, self.Y, heightR, rstride=1, cstride=1,
            cmap=cm.jet, linewidth=0, antialiased=False )
        plt.draw()                      # redraw the canvas
        self.fig.canvas.flush_events()
        time.sleep(1)
if __name__ == '__main__':
    matplotlib.interactive(True)
    p = plot3dClass(5,1)
    for i in range(100):
        p.drawNow(np.random.random(p.X.shape))'''

'''import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt


def update_line(hl, new_data):
    xdata, ydata, zdata = hl._verts3d
    hl.set_xdata(list(np.append(xdata, new_data[0])))
    hl.set_ydata(list(np.append(ydata, new_data[1])))
    hl.set_3d_properties(list(np.append(zdata, new_data[2])))
    plt.draw()


map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)

# # # Setting the axes properties
map_ax.set_xlim3d([0.0, 10.0])
map_ax.set_ylim3d([0.0, 10.0])
map_ax.set_zlim3d([0.0, 10.0])

hl, = map_ax.plot3D([0], [0], [0])

update_line(hl, (2, 2, 1))
plt.show(block=False)
plt.pause(1)

update_line(hl, (5, 5, 5))
plt.show(block=False)
plt.pause(2)

update_line(hl, (8, 1, 4))
plt.show(block=True)'''


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import numpy


count=0
fig = plt.figure()
ax = fig.gca(projection='3d')
z = [0]
x = [0]
y = [0]

plt.ion()    ###

plt.show()
while True:
    count +=1
    x.append(count)
    y.append(count**2) #
    z.append(count**3) # just for eye-candy

    ax.plot(numpy.array(x),    ###
            numpy.array(y),    ###
            numpy.array(z))    ###
    fig.canvas.flush_events()
    time.sleep(1)
    plt.draw()
