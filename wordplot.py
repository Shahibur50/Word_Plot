'''
Word Plot
Version 1.0.0

Copyright (C) 2021 Shahibur Rahaman
Licensed under GNU GPLv3
'''

import pandas as pd
import matplotlib.pyplot as plt

starting_point = 0

def plot(letter):
    if letter == "a":
        plotter(plot_a())
    if letter == "b":
        plotter(plot_b())
    if letter == "c":
        plotter(plot_c())
    if letter == "d":
        plotter(plot_d())
    if letter == "e":
        plotter(plot_e())
    if letter == "f":
        plotter(plot_f())
    if letter == "g":
        plotter(plot_g())
    if letter == "h":
        plotter(plot_h())
    if letter == "i":
        plotter(plot_i())
    if letter == "j":
        plotter(plot_j())
    if letter == "k":
        plotter(plot_k())
    if letter == "l":
        plotter(plot_l())
    if letter == "m":
        plotter(plot_m())
    if letter == "n":
        plotter(plot_n())
    if letter == "o":
        plotter(plot_o())
    if letter == "p":
        plotter(plot_p())
    if letter == "q":
        plotter(plot_q())
    if letter == "r":
        plotter(plot_r())
    if letter == "s":
        plotter(plot_s())
    if letter == "t":
        plotter(plot_t())
    if letter == "u":
        plotter(plot_u())
    if letter == "v":
        plotter(plot_v())
    if letter == "w":
        plotter(plot_w())
    if letter == "x":
        plotter(plot_x())
    if letter == "y":
        plotter(plot_y())
    if letter == "z":
        plotter(plot_z())
    if letter == " ":
        plot_space()


def plot_a():
    coordinates = [[1, 3],
                   [1, 5],
                   [2, 4],
                   [3, 3],
                   [3, 5],
                   [5, 1]]
  
    return coordinates


def plot_b():
    coordinates = [[1, 4],
                   [5, 5],
                   [1, 5],
                   [3, 3],
                   [1, 4],
                   [1, 1],
                   [1, 1],
                   [5, 1],
                   [5, 5],
                   [4, 2],
                   [4, 5],
                   [5, 4],
                   [4, 5],
                   [1, 2]]
    
    return coordinates


def plot_c():
    coordinates = [[1, 1],
                   [2, 4],
                   [1, 2],
                   [4, 5],
                   [1, 2],
                   [2, 1],
                   [2, 5],
                   [5, 5],
                   [2, 5],
                   [1, 1]]
    
    return coordinates


def plot_d():
    coordinates = [[1, 4],
                   [5, 5],
                   [1, 4],
                   [1, 1],
                   [1, 1],
                   [5, 1],
                   [5, 5],
                   [4, 2],
                   [4, 5],
                   [5, 4],
                   [4, 5],
                   [1, 2]]
  
    return coordinates


def plot_e():
    coordinates = [[1, 5],
                   [5, 5],
                   [1, 1],
                   [5, 1],
                   [1, 4],
                   [3, 3],
                   [1, 5],
                   [1, 1]]
    
    return coordinates


def plot_f():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 4],
                   [3, 3],
                   [1, 5],
                   [5, 5]]
    
    return coordinates


def plot_g():
    coordinates = [[1, 1],
                   [2, 4],
                   [1, 2],
                   [4, 5],
                   [1, 2],
                   [2, 1],
                   [2, 5],
                   [5, 5],
                   [2, 5],
                   [1, 1],
                   [5, 5],
                   [1, 3],
                   [3, 5],
                   [3, 3]]
    
    return coordinates


def plot_h():
    coordinates = [[1, 1],
                   [5, 1],
                   [5, 5],
                   [5, 1],
                   [1, 5],
                   [3, 3]]
    
    return coordinates


def plot_i():
    coordinates = [[1, 5],
                   [5, 5],
                   [3, 3],
                   [5, 1],
                   [1, 5],
                   [1, 1]]
    
    return coordinates


def plot_j():
    coordinates = [[3, 3],
                   [5, 1],
                   [3, 1],
                   [1, 1],
                   [1, 1],
                   [1, 2],
                   [1, 5],
                   [5, 5]]
    
    return coordinates


def plot_k():
    coordinates = [[1, 1],
                   [1, 5],
                   [1, 4],
                   [3, 5],
                   [1, 5],
                   [3, 1]]
    
    return coordinates


def plot_l():
    coordinates = [[1, 1],
                   [1, 5],
                   [1, 5],
                   [1, 1]]
    
    return coordinates


def plot_m():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 3],
                   [5, 1],
                   [3, 5],
                   [1, 5],
                   [5, 5],
                   [5, 1]]
    
    return coordinates


def plot_n():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 5],
                   [5, 1],
                   [5, 5],
                   [5, 1]]
    
    return coordinates


def plot_o():
    coordinates = [[1, 1],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [1, 1],
                   [1, 2],
                   [4, 5],
                   [4, 5],
                   [5, 4],
                   [1, 2],
                   [2, 1],
                   [5, 4],
                   [2, 1]]
    
    return coordinates


def plot_p():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 5],
                   [5, 5],
                   [5, 5],
                   [5, 3],
                   [5, 1],
                   [3, 3]]
    
    return coordinates


def plot_q():
    coordinates = [[1, 1],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [5, 5],
                   [2, 4],
                   [1, 1],
                   [1, 2],
                   [4, 5],
                   [4, 5],
                   [5, 4],
                   [1, 2],
                   [2, 1],
                   [5, 4],
                   [2, 1],
                   [4, 5],
                   [2, 1]]
    
    return coordinates


def plot_r():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 5],
                   [5, 5],
                   [5, 5],
                   [5, 3],
                   [5, 1],
                   [3, 3],
                   [1, 5],
                   [3, 1]]
    
    return coordinates


def plot_s():
    coordinates = [[1, 5],
                   [5, 5],
                   [1, 5],
                   [3, 3],
                   [1, 5],
                   [1, 1],
                   [1, 1],
                   [5, 3],
                   [5, 5],
                   [3, 1]]
    
    return coordinates


def plot_t():
    coordinates = [[3, 3],
                   [5, 1],
                   [1, 5],
                   [5, 5]]
    
    return coordinates


def plot_u():
    coordinates = [[1, 1],
                   [5, 1],
                   [1, 5],
                   [1, 1],
                   [5, 5],
                   [1, 5]]
    
    return coordinates


def plot_v():
    coordinates = [[1, 3],
                   [5, 1],
                   [3, 5],
                   [1, 5]]
    
    return coordinates


def plot_w():
    coordinates = [[1, 2],
                   [5, 1],
                   [2, 3],
                   [1, 5],
                   [3, 4],
                   [5, 1],
                   [4, 5],
                   [1, 5]]
    
    return coordinates


def plot_x():
    coordinates = [[1, 5],
                   [5, 1],
                   [5, 1],
                   [5, 1]]
    
    return coordinates


def plot_y():
    coordinates = [[1, 3],
                   [5, 3],
                   [5, 1],
                   [5, 1]]
    
    return coordinates


def plot_z():
    coordinates = [[1, 5],
                   [5, 5],
                   [5, 1],
                   [5, 1],
                   [1, 5],
                   [1, 1]]
    
    return coordinates


def plot_space():
    global starting_point

    starting_point += 5


def clear_plots():
    global starting_point
    
    starting_point = 0


def plotter(coordinates):
    global starting_point

    for i in range(0, len(coordinates) - 1, 2):
        x_axis = [coordinate + starting_point for coordinate in coordinates[i]]
        y_axis = [coordinate for coordinate in coordinates[i + 1]]
        
        biggest_x_axis = max(x_axis)
        
        df = pd.DataFrame({"x_axis": x_axis, "y_axis": y_axis})
        
        plt.plot(df.x_axis, df.y_axis,
                 marker=',',
                 markersize=10,
                 linewidth=2,
                 linestyle='dashed')
        
    if biggest_x_axis > starting_point:
        starting_point = biggest_x_axis
