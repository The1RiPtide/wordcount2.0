import time
import curses
import curses.ascii
import tkinter
from tkinter import filedialog

stdscr = curses.initscr()

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

def input_goal(input_string, stdscr):

    try:
      input_int = int(input_string)
      return input_int
    except:
        stdscr.clear()
        stdscr.addstr(1, 4, "That is not a number you Dimwit...")

        stdscr.refresh()

        stdscr.attron(curses.color_pair(1))

        stdscr.addstr(3, 8, "I'm sorry, I'll try again")

        stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        while 1:
            key = stdscr.getch()

            if key == curses.KEY_ENTER or key in [10, 13]:
                break

        return -1

    finally:
        stdscr.clear()
        stdscr.refresh()


def start_screen(stdscr):


    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(1, 4, "Please Enter your goal for today: ")

    curses.echo()
    curses.curs_set(1)

    goal_string_raw = str(stdscr.getstr(3,4))
    goal_string = goal_string_raw[2 : (len(goal_string_raw)-1)]

    curses.noecho()
    curses.curs_set(0)

    goal_int = input_goal(goal_string, stdscr)

    return goal_int

def file_select(stdscr, selected_line_idx):
    menu = ["Select file", "Change goal"]

    stdscr.clear

    for idx, line in enumerate(menu):
        y = 3
        x = 7 + ((idx + 1) ** 5)

        if idx == selected_line_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, line)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, line)

    stdscr.refresh()

def main(stdscr):

    curses.curs_set(0)

    stdscr.keypad(True)

    goal = -1

    while 1:
        goal = start_screen(stdscr)
        if goal < 0:
            continue

        stdscr.addstr(1, 4, "Please select file to track:")

        current_line_idx = 0

        file_select(stdscr, current_line_idx)

        while 1:
            key = stdscr.getch()

            stdscr.clear()

            if key == curses.KEY_LEFT and current_line_idx > 0:
                current_line_idx -= 1
            elif key == curses.KEY_RIGHT and current_line_idx < 1:
                current_line_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                break

            stdscr.addstr(1, 4, "Please select file to track:")

            file_select(stdscr, current_line_idx)

            stdscr.refresh()

        if current_line_idx == 0:
            break
        elif current_line_idx == 1:
            continue



    root = tkinter.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()



    stdscr.addstr(1, 4, "Your Goal was set to: %d and your filepath is %s" % (goal, filepath))
    stdscr.refresh()
    time.sleep(5)

curses.wrapper(main(stdscr))

