# File containing all the constants that are only used in "App.py"
# App size and title
WINDOW_SIZE = "500x300"
WINDOW_TITLE = "Събиране и изваждане на обикновени дроби"
ADVICE_TITLE = "Съвет"
# Advice massages contents
IDENTIFICATION_ADVICE_CONTENT = "Задача съдържа дроб, когато\n" \
                                "поне една от частите ѝ e\n" \
                                "несъкратима и има знаменател\n" \
                                "различен от единица.\n\n" \
                                "Пример: 1/2"
SIMPLIFY_ADVICE_CONTENT = "Намерете НОД и разделете\n" \
                          "и двете части на дробта\n" \
                          "на него.\n" \
                          "Пример: 2/4; НОД = 2;\n" \
                          "Резултат: 1/2"
DENOMINATOR_ADVICE_CONTENT = "Намерете НОК на \n" \
                             "знаменателите."
NOMINATOR_ADVICE_CONTENT = "Умножете всеки от \n" \
                           "числителите с разликата\n" \
                           "на знаменателя му и \n" \
                           "общия знаменател."
# types of tasks
EASY_ADDITION = 1
EASY_ADDITION_TEXT = "лесно събиране"
EASY_SUBTRACTION = 2
EASY_SUBTRACTION_TEXT = "лесно изваждане"
HARD_ADDITION = 3
HARD_ADDITION_TEXT = "трудно събиране"
HARD_SUBTRACTION = 4
HARD_SUBTRACTION_TEXT = "трудно изваждане"
# A placeholder for values that are not going to be used
PLACEHOLDER = 0
# Errors that the user makes in the computation of sub tasks
STARTING_NUMBER_OF_ERRORS = 0
NO_ERRORS = 0
ADD_ERROR = 1
BAD_RESULT = 5
# Values used so error and advice types can be identified
IDENTIFICATION_ADVICE = 0
IDENTIFICATION_ERROR = 0
SIMPLIFY_ADVICE = 1
SIMPLIFY_ERROR = 1
DENOMINATOR_ADVICE = 2
DENOMINATOR_ERROR = 2
NOMINATOR_ADVICE = 3
NOMINATOR_ERROR = 3
ADDITION_ERROR = 4
# Sizes of different buttons
ADVICE_BUTTON_SIZE = 15
END_APP_BUTTON_SIZE = 12
SELECT_NEW_DIFFICULTY_BUTTON_SIZE = 2
FINALIZE_STEP_BUTTON_SIZE = 5
FINALIZE_TASK_BUTTON_SIZE = 1
# Free space horizontally used to align buttons nicely
STANDARD_SPACE_BETWEEN_BUTTONS = 5
STANDARD_SPACE_BETWEEN_ENTRY_BOX_LABELS = 11
STANDARD_SPACE_BETWEEN_ENTRY_BOXES = 10
STANDARD_SPACE_BEFORE_BUTTONS = 85
SPACE_BEFORE_NEXT_TASK_BUTTON = 62
SPACE_BEFORE_NEW_DIFFICULTY_SELECTION_BUTTON = 77
SPACE_BEFORE_BUTTONS_IN_NON_TASK = 80
# Free space vertically used to align buttons nicely
VERTICAL_SPACE_IN_DIFFICULTY_SELECTION = 39
VERTICAL_SPACE_IN_NON_TASK = 61
VERTICAL_SPACE_IN_FIRST_STEP = 26
VERTICAL_SPACE_IN_FIRST_STEP_RESULT = 69
VERTICAL_SPACE_IN_SECOND_STEP = 3
VERTICAL_SPACE_IN_SECOND_STEP_RESULT = 80
VERTICAL_SPACE_IN_THIRD_STEP = 43
VERTICAL_SPACE_IN_THIRD_STEP_RESULT = 69
VERTICAL_SPACE_IN_FOURTH_STEP = 33
VERTICAL_SPACE_IN_FOURTH_STEP_RESULT = 80
VERTICAL_SPACE_IN_FIFTH_STEP = 27
VERTICAL_SPACE_IN_FIFTH_STEP_BETWEEN_ENTRY_BOXES = 5
VERTICAL_SPACE_IN_FIFTH_STEP_RESULT = 72
VERTICAL_SPACE_IN_ERROR_FEEDBACK_WITH_ERRORS = 61
VERTICAL_SPACE_IN_ERROR_FEEDBACK_WITHOUT_ERRORS = 82
# Values used so the right type of visualization can be used
STANDARD_TASK_VISUALIZATION = 1
ADVANCED_TASK_VISUALIZATION = 2
ADVANCED_TASK_VISUALIZATION_WITH_RESULT = 3
# Sub Tasks in each step
STEP_ONE_SUB_TASK_TEXT = "Съдържа ли задачата поне една дроб?"
STEP_TWO_SUB_TASK_TEXT = "Преобразуване и опростяване:"
STEP_THREE_SUB_TASK_TEXT = "Изчисляване на знаменател:"
STEP_FOUR_SUB_TASK_TEXT = "Пресмятане на числителите:"
STEP_FIVE_SUB_TASK_TEXT = "Съкратен краен резултат:"
# Padding for labels
STANDARD_LABEL_PADDING = 20
STEP_ONE_SUB_TASK_PADDING = 21
# Review of the result in the first step of a task
FIRST_STEP_REVIEW_TEXT = "Задачата съдържа дроб."
NON_TASK_REVIEW_TEXT = "Задачата НЕ съдържа дроб."
# Text before announcing the right answer of a step
RIGHT_ANSWER_ANNOUNCEMENT_TEXT = "Правилният отговор: "
DENOMINATOR_ANNOUNCEMENT_TEXT = "Знаменателят е "
# Feedback on validity of an answer given by user
RIGHT_ANSWER_TEXT = "Правилно"
WRONG_ANSWER_TEXT = "Грешно"
# Text displayed on buttons
FINISH_BUTTON_TEXT = "Приключи"
CHECK_ANSWER_BUTTON_TEXT = "Провери"
FINALIZE_TASK_BUTTON_TEXT = "Финализиране опит"
SELECT_NEW_DIFFICULTY_BUTTON_TEXT = "Избери трудност"
ADVICE_BUTTON_TEXT = "Съвет"
ADVANCE_BUTTON_TEXT = "Продължи"
END_APP_BUTTON_TEXT = "Край"
NEXT_TASK_BUTTON_TEXT = "Следваща задача"
# Message asking for the selection of a difficulty
SELECT_DIFFICULTY_MESSAGE = "Моля изберете трудност:"
# Radiobutton text options in first step
YES_OPTION_TEXT = "Да"
NO_OPTION_TEXT = "Не"
# Messages used when announcing the number of errors
ERROR_COUNTER_MESSAGE_BEGINNING = "Допуснати са общо "
ERROR_COUNTER_MESSAGE_END = " грешки."
# Frame properties
FRAME_BORDER_WIDTH = 1
FRAME_BORDER_TYPE = "solid"
# Feedback after finalizing the tasks.
ERROR_FEEDBACK_MAIN_MESSAGE = "Допуснати са много грешки при"
ERROR_FEEDBACK_IDENTIFICATION_ERRORS_MESSAGE = "определянето дали в задача има дроби."
ERROR_FEEDBACK_SIMPLIFY_ERRORS_MESSAGE = "съкращаването на дроби."
ERROR_FEEDBACK_DENOMINATOR_ERRORS_MESSAGE = "търсенето на общ знаменател."
ERROR_FEEDBACK_NOMINATOR_ERRORS_MESSAGE = "пресмятането на числителите."
ERROR_FEEDBACK_ADDITION_ERRORS_MESSAGE = "събирането."
ERROR_FEEDBACK_DIFFERENT_TYPES_OF_ERRORS_MESSAGE = "различните стъпки."
# Entry boxes width
STANDARD_ENTRY_BOX_WIDTH = 6
BIG_ENTRY_BOX_WIDTH = 10
# Nominators and denominators indexes
FIRST_NOMINATOR = 0
FIRST_DENOMINATOR = 1
SECOND_NOMINATOR = 2
SECOND_DENOMINATOR = 3
THIRD_NOMINATOR = 4
THIRD_DENOMINATOR = 5
FOURTH_NOMINATOR = 6
FOURTH_DENOMINATOR = 7
COUNT_NOMINATORS_ONLY = 2
# Modes for right/wrong message labels
SIMPLE_MODE = 1
SPECIAL_MODE = 2
