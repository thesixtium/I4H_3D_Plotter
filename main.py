import random

import serial
import re
import matplotlib.pyplot as plt
import numpy

def clean_data(data):
    clean_t_xyz = [[]]

    for i in range(1, len(data)):
        if data[i] != data[-1]:
            clean_t_xyz.append(data[i])
            x = (data[i][0] + data[i + 1][0]) / 2
            y = (data[i][1] + data[i + 1][1]) / 2
            z = (data[i][2] + data[i + 1][2]) / 2
            clean_t_xyz.append([x, y, z])
        else:
            clean_t_xyz.append(data[i])
    return clean_t_xyz

if __name__ == '__main__':
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM3', 115200, timeout=1)

    # Get data
    t_xyz = []
    for i in range(5000):
        try:
            line = ser.readline()  # read a byte
            if line:
                string = line.decode()  # convert the byte string to a unicode string
                returnArray = re.findall("[0-9]{0,4}", string)
                if len(returnArray) == 14 and int(returnArray[2]) != 0 and int(returnArray[10]) != 0:
                    t_xyz.append([int(returnArray[2]), int(returnArray[6]), int(returnArray[10])])
                    print([returnArray[2], returnArray[6], returnArray[10]])
        except:
            print("Error")
    ser.close()

    # Clean data
    print(t_xyz)
    t_xyz = clean_data(t_xyz)
    print(t_xyz)
    t_xyz = clean_data(t_xyz)
    t_xyz.pop(0)
    print(t_xyz)

    # Plot graphs
    fig = plt.figure(figsize=plt.figaspect(0.5))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.title.set_text('Touchscreen')

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.title.set_text('IMU')

    t_x = []
    t_y = []
    t_z = []

    i_x = [random.randint(1, 100) for _ in range(0, len(t_xyz))]
    i_y = [random.randint(1, 100) for _ in range(0, len(t_xyz))]

    plt.ion()
    plt.show()

    for i in range(1, len(t_xyz)):
        t_x.append(t_xyz[i][0])
        t_y.append(t_xyz[i][1])
        t_z.append(t_xyz[i][2])

        ax1.plot(numpy.array(t_x),
                 numpy.array(t_y),
                 numpy.array(t_z))
        ax2.plot(numpy.array(i_x),
                 numpy.array(i_y))
        fig.canvas.flush_events()
        plt.draw()

    while True:
        fig.canvas.flush_events()
        plt.draw()
