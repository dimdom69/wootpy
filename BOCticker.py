#!/usr/bin/env python3

import curses,wootpy,sys,time

stdscr = curses.initscr()
height,width = stdscr.getmaxyx()

w = wootpy.woot()

def setup():
	#curses.start_color()
	#curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	stdscr.keypad(1)

def end():
	#reverse curses settings
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()

	#end the curses session
	curses.endwin()
    
def update():
    #Add updating text at bottom right
    stdscr.move(height-2, 0)
    stdscr.clrtoeol()
    stdscr.addstr(height-2, 0, "Updating...")
    stdscr.refresh()
    
    ret = w.getWoot(site='www.woot.com',eventType='WootOff')
    boc = w.checkBOC(ret)
    woot_string = "Woot.com: " + str(ret[0]['Offers'][0]['Title'])

    stdscr.move(1, 0)
    stdscr.clrtoeol()
    stdscr.addstr(1, 0, woot_string)
    stdscr.move(height-2, 0)
    stdscr.clrtoeol()
    if boc:
        stdscr.addstr(height-2, 0, "Bag of Crap found!!!! "+boc['Url'])
    else:
        stdscr.addstr(height-2, 0, "No Bag of Crap found")
    stdscr.refresh()
    
def Main():
    setup()
    while True:
        update()
        time.sleep(30)
if __name__ == '__main__':
    try:
        Main()
    except:
        end()
        e0 = sys.exc_info()[0]
        e1 = sys.exc_info()[1]
        print(e0)
        print(e1)