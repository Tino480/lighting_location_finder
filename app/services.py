import pandas as pd
import random
import matplotlib.pyplot as plt
import itertools
import sys
from operator import itemgetter
from matplotlib.backends.backend_pdf import PdfPages


def get_lighting_locations(file):
    global free_space
    global table
    global free_space_edit
    global light_positions
    global final_light_positions
    free_space, table = get_free_spaces_coords(file)
    free_space_edit = []
    light_positions = []
    final_light_positions = free_space.copy()
    permutations = list(itertools.permutations(free_space_edit))
    for i in permutations:
        free_space_edit = list(i)
        search(free_space_edit)
        if len(light_positions) < len(final_light_positions):
            final_light_positions = light_positions
        light_positions = []

    for rec in final_light_positions:
        table.at[rec[0], rec[1]] = "x"

    colors = assign_cell_colors()
    create_pdf(colors)

    return "lighting_diagram.pdf"


def assign_cell_colors():
    colors = []
    for i in range(table.shape[0]):
        x = []
        for j in range(table.shape[1]):
            value = table.at[i, j]
            if value == "x":
                x.append("#FFFF00")
            elif value == 0:
                x.append("#C0C0C0")
            else:
                x.append("#808080")
        colors.append(x)
        x = []
    return colors


def create_pdf(colors):
    fig, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")
    ax.table(
        cellText=table.values,
        loc="center",
        cellColours=colors,
        rowLabels=table.index,
        colLabels=table.columns,
    )
    pp = PdfPages("lighting_diagram.pdf")
    pp.savefig(fig, bbox_inches="tight")
    pp.close()


def get_free_spaces_coords(file):
    free_space = []
    matrix = [
        [int(num) for num in line if num != "\n"]
        for line in file.decode("utf-8").split("\n")
        if len(line) > 0
    ]
    table = pd.DataFrame(matrix)
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            value = table.at[i, j]
            if value == 0:
                free_space.append([i, j])
    return free_space, table


def search(table):
    while len(table) > 0:
        for rec in table:
            x = rec[0]
            y = rec[1]
            light_positions.append(rec)
            free_space_edit.remove(rec)
            search_x_axis_positive(x, y)
            search_x_axis_negative(x, y)
            search_y_axis_positive(x, y)
            search_y_axis_negative(x, y)
            search(free_space_edit)


def search_x_axis_positive(x, y):
    table = sorted(
        [rec for rec in free_space.copy() if rec[0] == x and rec[1] > y],
        key=itemgetter(1),
    )
    for rec in table:
        if rec[1] == y + 1:
            if rec in free_space_edit:
                free_space_edit.remove(rec)
            y += 1
        elif not (rec[0] == x and rec[1] == y):
            break


def search_x_axis_negative(x, y):
    table = sorted(
        [rec for rec in free_space.copy() if rec[0] == x and rec[1] < y],
        key=itemgetter(1),
        reverse=True,
    )
    for rec in table:
        if rec[1] == y - 1:
            if rec in free_space_edit:
                free_space_edit.remove(rec)
            y -= 1
        elif not (rec[0] == x and rec[1] == y):
            break


def search_y_axis_positive(x, y):
    table = sorted(
        [rec for rec in free_space.copy() if rec[1] == y and rec[0] > x],
        key=itemgetter(0),
    )
    for rec in table:
        if rec[0] == x + 1:
            if rec in free_space_edit:
                free_space_edit.remove(rec)
            x += 1
        elif not (rec[0] == x and rec[1] == y):
            break


def search_y_axis_negative(x, y):
    table = sorted(
        [rec for rec in free_space.copy() if rec[1] == y and rec[0] < x],
        key=itemgetter(0),
        reverse=True,
    )
    for rec in table:
        if rec[0] == x - 1:
            if rec in free_space_edit:
                free_space_edit.remove(rec)
            x -= 1
        elif not (rec[0] == x and rec[1] == y):
            break
