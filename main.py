import random
import math
import serial
import re
import matplotlib.pyplot as plt
import numpy
import time


def clean_data(data):
    clean_t_xyz = [[]]

    for i in range(1, len(data)):
        if i != (len(data) - 1):
            clean_t_xyz.append(data[i])
            x = (data[i][0] + data[i + 1][0]) / 2
            y = (data[i][1] + data[i + 1][1]) / 2
            z = (data[i][2] + data[i + 1][2]) / 2
            clean_t_xyz.append([x, y, z])
        else:
            clean_t_xyz.append(data[i])
    return clean_t_xyz


def magnitude(data):
    magnitude_data = []

    for point in data:
        x2 = point[0] * point[0]
        y2 = point[1] * point[1]
        z2 = point[2] * point[2]
        m2 = x2 + y2 + z2
        magnitude_data.append(math.sqrt(m2))

    return magnitude_data


if __name__ == '__main__':
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM3', 115200, timeout=1)

    # Get data
    t_xyz = []
    i_xyz = []
    for i in range(2000):
        try:
            line = ser.readline()  # read a byte
            if line:
                string = line.decode()  # convert the byte string to a unicode string
                returnArray = string.split(" ")
                if len(returnArray) == 14 and int(returnArray[1]) != 0 and int(returnArray[5]) != 0:
                    t_xyz.append([int(returnArray[1]), int(returnArray[3]), int(returnArray[5])])
                    i_xyz.append([int(returnArray[7]) + 1,
                                  int(returnArray[9]) + 1,
                                  int(returnArray[11]) + 1])
                    print(
                        str([returnArray[1], returnArray[3], returnArray[5]])
                        + " " +
                        str([returnArray[7], returnArray[9], returnArray[11]])
                    )
        except:
            print("Error")
        finally:
            if i % 500 == 0:
                print("On run " + str(i))
    ser.close()

    # Clean data
    print("Data clean started")
    # t_xyz = clean_data(t_xyz)
    # i_xyz = clean_data(i_xyz)
    # t_xyz = clean_data(t_xyz)
    # i_xyz = clean_data(i_xyz)
    t_xyz.pop(0)
    i_xyz.pop(0)
    print("Data clean done")

    # Get magnitudes
    print("Started getting magnitudes")
    t_mag = magnitude(t_xyz)
    i_mag = magnitude(i_xyz)
    print("Finished getting magnitudes")

    # Plot graphs
    print("Starting plot config")
    fig = plt.figure(figsize=plt.figaspect(1.0))

    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.title.set_text('Touchscreen XYZ')
    # ax1.set_xlim(xyz_xlim)
    # ax1.set_ylim(xyz_ylim)
    # ax1.set_zlim(xyz_zlim)

    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.title.set_text('IMU XYZ')
    # ax2.set_xlim(xyz_xlim)
    # ax2.set_ylim(xyz_ylim)
    # ax2.set_zlim(xyz_zlim)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.title.set_text('|Touchscreen XYZ|')
    # ax3.set_xlim(mag_xlim)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.title.set_text('Touchscreen XY')
    # ax4.set_xlim(mag_xlim)

    '''
    Plot 1: Touchscreen XYZ
    Plot 2: IMU Acceleration XYZ
    Plot 3: Touchscreen Magnitude
    Plot 4:  IMU Acceleration Magnitude
    '''

    t_x = []
    t_y = []
    t_z = []

    i_x = []
    i_y = []
    i_z = []

    t_m = []
    i_m = []

    t_cb = []

    time = []

    plt.ion()
    print("Finished plot config")
    plt.show()

    for i in range(1, len(t_xyz)):
        t_x.append(t_xyz[i][0])
        t_y.append(t_xyz[i][1])
        t_z.append(t_xyz[i][2])

        i_x.append(i_xyz[i][0])
        i_y.append(i_xyz[i][1])
        i_z.append(i_xyz[i][2])

        t_m.append(t_mag[i])
        i_m.append(i_mag[i])

        time.append(i)

        ax1.plot(numpy.array(t_x),
                 numpy.array(t_y),
                 numpy.array(t_z))
        ax2.plot(numpy.array(i_x),
                 numpy.array(i_y),
                 numpy.array(i_z))
        ax3.plot(numpy.array(time),
                 numpy.array(t_m))
        ax4.plot(numpy.array(t_x),
                 numpy.array(t_y))
        fig.canvas.flush_events()
        plt.draw()

    while True:
        fig.canvas.flush_events()
        plt.draw()
