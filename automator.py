from webbrowser import open
from pynput.keyboard import Controller

import time
import answers


class Automator:
    '''
    The Automator class is designed to automate the process of completing a survey. It utilizes the Controller class
    from the pynput library to simulate keyboard input, enabling navigation and data entry. The class provides methods
    for pressing and releasing keys, setting Burger King (BK) numbers, entering text answers, executing sequences of
    commands, logging responses, and completing the entire survey.

    Attributes:
        wait_time (float): The time interval between key presses and releases.
        page_counter (int): Counter for keeping track of completed pages.
        keyboard (Controller): Instance of the Controller class for simulating keyboard input.

    Methods:
        press_and_release(keys, times=1): Simulates pressing and releasing a sequence of keys a specified number of times.
        set_BK_number(): Enters the Burger King number and advances to the next input field.
        answer_text(): Enters a text answer and advances to the next input field.
        execute(commands, times): Executes a series of key sequences a specified number of times.
        log_response(): Logs the completion of a survey page, updating the page counter.
        complete_survey(): Initiates the survey completion process, navigating through pages and entering data.

    Usage Example:
        automator = Automator()
        automator.complete_survey()
    '''
    def __init__(self, time=0.23):
        self.wait_time = time
        self.page_counter = 1
        self.keyboard = Controller()


    def press_and_release(self, keys, times=1):
        '''
        Simulates pressing and releasing a sequence of keys a specified number of times.

        Parameters:
            keys (list): List of keys to be pressed and released.
            times (int): Number of times the key sequence should be executed. Default is 1.
        '''
        for _ in range(times):
            for key in keys:
                time.sleep(self.wait_time)
                self.keyboard.press(key)
                self.keyboard.release(key)


    def set_BK_number(self):
        '''
        Enters the Burger King number and advances to the next input field.
        '''
        self.press_and_release(answers.TAB, 2)
        self.keyboard.type(answers.restaurant_number)
        self.press_and_release(answers.NEXT)


    def answer_text(self):
        '''
        Enters a text answer and advances to the next input field.
        '''
        self.press_and_release(answers.TAB)
        self.keyboard.type(answers.text_answer)
        self.press_and_release(answers.TAB)
        self.press_and_release(answers.NEXT)


    def execute(self, commands, times):
        '''
        Executes a series of key sequences a specified number of times.

        Parameters:
            commands (list): List of key sequences to be executed.
            times (list): List specifying the number of times each corresponding command should be executed.
        '''
        if len(commands) != len(times):
            return "Error"

        for i in range(len(commands)):
            self.press_and_release(commands[i], times[i])


    def log_response(self):
        '''
        Logs the completion of a survey page, updating the page counter.
        '''
        print("Page #" + str(self.page_counter) + " completed.")
        self.page_counter += 1
        time.sleep(RESPONSE_TIME)


    def complete_survey(self):
        '''
        Initiates the survey completion process, navigating through pages and entering data.
        '''
        open(SURVEY_URL)
        time.sleep(INITIAL_WAIT)
        pages = answers.actions

        for page in pages:
            is_text = len(pages[page]) == 1

            if not is_text:
                keys = pages[page][0]
                repeats = pages[page][1]
                self.execute(keys, repeats)
                self.log_response()

            else:
                match page:
                    case "page_01":
                        self.set_BK_number()
                        self.log_response()

                    case _:
                        self.answer_text()
                        self.log_response()

        print("Survey completed.")


# Waiting times
FAST = 0.05
INSTANTLY = 0
INITIAL_WAIT = 7
RESPONSE_TIME = 1.6

# Survey
SURVEY_URL = "https://www.evaluabk.com/"

# Automator
bot = Automator(time= FAST)
bot.complete_survey()