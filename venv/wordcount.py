import time
import curses
import curses.ascii

stdscr = curses.initscr()

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

def navKey(key):

    if key == curses.KEY_UP:
        return "UP"
    elif key == curses.KEY_DOWN:
        return "DOWN"
    elif key == curses.KEY_LEFT:
        return "LEFT"
    elif key == curses.KEY_RIGHT:
        return "RIGHT"
    elif key == curses.KEY_ENTER or key in [10, 13]:
        return "ENTER"
    elif key == curses.ascii.ESC:
        return "ESC"


def inputGoal(inputString, stdscr):

    try:
      inputInt = int(inputString)
      return inputInt
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

            if navKey(key) == "ENTER":
                break

        return -1

    finally:
        stdscr.clear()
        stdscr.refresh()


def startScreen(stdscr):


    stdscr.clear()

    stdscr.refresh()

    stdscr.addstr(1, 4, "Please Enter your goal for today: ")

    curses.echo()
    curses.curs_set(1)

    goalStringRaw = str(stdscr.getstr(3,4))

    goalString = goalStringRaw[2 : (len(goalStringRaw)-1)]

    # stdscr.clear()
    # stdscr.addstr(1, 4, "Your Goal was set to: %s" % goalString)
    # stdscr.refresh()
    # time.sleep(5)

    curses.noecho()
    curses.curs_set(0)

    goalInt = inputGoal(goalString, stdscr)

    stdscr.addstr(1, 4, "Your Goal was set to: %d" % goalInt)
    stdscr.refresh()
    time.sleep(5)

def main(stdscr):

    curses.curs_set(0)

    stdscr.keypad(True)

    startScreen(stdscr)

curses.wrapper(main(stdscr))

