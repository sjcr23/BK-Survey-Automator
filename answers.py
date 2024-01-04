from pynput.keyboard import Key

# Key sequences
NEXT = [Key.tab, Key.enter]
TAB = [Key.tab]
OPT = [Key.tab, Key.space]
DATE = [Key.tab, Key.right, Key.right]
DOWN = [Key.down]

NEXT_OPTION = [OPT, NEXT]
SELECT_ONE = [OPT, TAB, NEXT]
SAY_NO = [OPT, DOWN, TAB, NEXT]
SET_DATE = [NEXT, DATE, NEXT]

# Text answers
restaurant_number = "29626"
text_answer = "Gracias BK por tanto, perdón por tan poco. <3"

# Repeats
double_ones = 2*[1]
triple_ones = 3*[1]
quadruples_ones = 4*[1]

# Page actions
actions = {
    "page_01": [""],
    "page_02": (SET_DATE, [1, 3, 1]),
    "page_03": (NEXT_OPTION, double_ones),
    "page_04": [""],
    "page_05": (NEXT_OPTION, double_ones),
    "page_06": (SELECT_ONE, triple_ones),
    "page_07": (NEXT_OPTION, [12, 1]),
    "page_08": (SELECT_ONE, [2, 1, 1]),
    "page_09": (SAY_NO, quadruples_ones),
    "page_10": (SELECT_ONE, [1, 44, 1]),
    "page_11": (SELECT_ONE, [1, 12, 1]),
    "page_12": (SELECT_ONE, [1, 8, 1]),
    "page_13": (SELECT_ONE, [2, 1, 1]),
    "page_14": (NEXT_OPTION, double_ones),
    "page_15": (SELECT_ONE, [9, 1, 1]),
    "page_16": (SELECT_ONE, triple_ones),
    "page_17": [""],
    "page_18": (SELECT_ONE, triple_ones),
    "page_19": (SELECT_ONE, triple_ones),
    "page_20": (SELECT_ONE, triple_ones),
    "page_21": (SELECT_ONE, triple_ones),
    "page_22": (SELECT_ONE, triple_ones),
    "page_23": (SELECT_ONE, triple_ones),
    "page_24": (SELECT_ONE, triple_ones)
}