from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Waiting times
INITIAL_WAIT, INSTANT, FAST, RESPONSE = 2, 0, 0.1, 1.4

# Key sequences
NEXT = [Key.tab, Key.enter]
TAB = [Key.tab]
OPT = [Key.tab, Key.space]
DATE = [Key.tab, Key.right, Key.right]
DOWN = [Key.down]

# Answers
BK_NUMBER = "29626"
TEXT_ASNWER = "Sí. ;)"
NEXT_OPTION = [OPT, NEXT]
SELECT_ONE = [OPT, TAB, NEXT]
SAY_NO = [OPT, DOWN, TAB, NEXT]
SET_DATE = [NEXT, DATE, NEXT]

# Page counter
CURRENT_PAGE = 1


def press_and_release(keys, times=1):
    for i in range(times):
        for key in keys:
            time.sleep(INSTANT)
            keyboard.press(key)
            keyboard.release(key)


def set_BK_number(text):
    press_and_release(TAB, 2)
    keyboard.type(text)
    press_and_release(NEXT, 1)


def answerText(text):
    press_and_release(TAB, 1)
    keyboard.type(text)
    press_and_release(TAB, 1)
    press_and_release(NEXT, 1)


def execute(commands, times):
    assert len(commands) == len(times)
    for i in range(len(commands)):
        press_and_release(commands[i], times[i])


def log_response():
    global CURRENT_PAGE
    print("Page #" + str(CURRENT_PAGE) + " completed.")
    CURRENT_PAGE += 1
    time.sleep(RESPONSE)


answers = [
    [BK_NUMBER],
    [SET_DATE, [1, 3, 1]],
    [NEXT_OPTION, [1, 1]],
    [TEXT_ASNWER],
    [NEXT_OPTION, [1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [NEXT_OPTION, [12, 1]],
    [SELECT_ONE, [2, 1, 1]],
    [SAY_NO, [1, 1, 1, 1]],
    [SELECT_ONE, [1, 43, 1]],
    [SELECT_ONE, [1, 12, 1]],
    [SELECT_ONE, [1, 8, 1]],
    [SELECT_ONE, [2, 1, 1]],
    [NEXT_OPTION, [1, 1]],
    [SELECT_ONE, [9, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [TEXT_ASNWER],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]],
    [SELECT_ONE, [1, 1, 1]]
]

time.sleep(INITIAL_WAIT)

for answer in answers:
    if len(answer) > 1:
        execute(answer[0], answer[1])
        log_response()

    else:
        if answer[0] == BK_NUMBER:
            set_BK_number(answer[0])
            log_response()
        else:
            answerText(answer[0])
            log_response()

print("done. :)")
