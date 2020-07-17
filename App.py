# The application is targeted towards students in 5th grade and tries to help them learn how to solve addition and
# subtraction tasks containing at least one fraction. The task are divided in 4 "difficulties" and the user can choose
# the type of tasks they want to practice. The application divides each task in five "steps" or sub tasks and gives
# feedback to the user in which "step" they should try to hone their skills.
# The application has 13 different screen layouts(the functions that end with "_window"):
# 5 for each step
# 5 for each result for corresponding step
# 1 for difficulty selection
# 1 for feedback
# 1 for non tasks - tasks that after randomizing have no fractions
from Task import *
from tkinter import *
from tkinter import messagebox
from Constants import *


def create_horizontal_spacing(space):
    Label(root, padx=space).pack(side=LEFT)


def create_vertical_spacing(space):
    Label(root, pady=space).pack()


def create_advice_button(advice_number):
    Button(root, text=ADVICE_BUTTON_TEXT, padx=ADVICE_BUTTON_SIZE,
           command=lambda: give_advice(advice_number)).pack(side=LEFT)


def create_task_label(mode):
    if mode == STANDARD_TASK_VISUALIZATION:
        Label(root, text=task.visualize_as_string(), pady=STANDARD_LABEL_PADDING).pack()
    if mode == ADVANCED_TASK_VISUALIZATION:
        Label(root, text=task.visualize_result_equation_as_string(), pady=STANDARD_LABEL_PADDING).pack()
    if mode == ADVANCED_TASK_VISUALIZATION_WITH_RESULT:
        Label(root, text=task.visualize_with_result_as_string(), pady=STANDARD_LABEL_PADDING).pack()


def clear_window():
    widgets = root.pack_slaves()
    for widget in widgets:
        widget.destroy()


def give_advice(advice_number):
    if advice_number == IDENTIFICATION_ADVICE:
        messagebox.showinfo(ADVICE_TITLE, IDENTIFICATION_ADVICE_CONTENT)
    if advice_number == SIMPLIFY_ADVICE:
        messagebox.showinfo(ADVICE_TITLE, SIMPLIFY_ADVICE_CONTENT)
    if advice_number == DENOMINATOR_ADVICE:
        messagebox.showinfo(ADVICE_TITLE, DENOMINATOR_ADVICE_CONTENT)
    if advice_number == NOMINATOR_ADVICE:
        messagebox.showinfo(ADVICE_TITLE, NOMINATOR_ADVICE_CONTENT)


def is_there_error_in_fifth_step(nominator_and_denominator):
    error_counter = NO_ERRORS
    try:
        if int(nominator_and_denominator[FIRST_NOMINATOR]) != int(task.result_fraction.get_nominator()):
            error_counter += ADD_ERROR
        if int(nominator_and_denominator[FIRST_DENOMINATOR]) != int(task.result_fraction.get_denominator()) \
                and error_counter == NO_ERRORS:
            error_counter += ADD_ERROR
    except ValueError:
        error_counter += ADD_ERROR
    return error_counter


def fifth_step_result_window(errors, nominator_and_denominator):
    clear_window()
    create_task_label(ADVANCED_TASK_VISUALIZATION_WITH_RESULT)
    error_counter = is_there_error_in_fifth_step(nominator_and_denominator)
    display_right_or_wrong(error_counter, SIMPLE_MODE)
    errors[ADDITION_ERROR] = errors[ADDITION_ERROR] + error_counter
    create_vertical_spacing(VERTICAL_SPACE_IN_FIFTH_STEP_RESULT)
    create_horizontal_spacing(SPACE_BEFORE_NEXT_TASK_BUTTON)
    Button(root, text=NEXT_TASK_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
           command=lambda: first_step_window(errors)).pack(side=LEFT)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    Button(root, text=FINALIZE_TASK_BUTTON_TEXT, padx=FINALIZE_TASK_BUTTON_SIZE,
           command=lambda: errors_report_and_feedback_window(errors)).pack(side=LEFT)


def create_result_entry_boxes():
    final_nominator = Entry(root, width=BIG_ENTRY_BOX_WIDTH)
    final_nominator.pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_FIFTH_STEP_BETWEEN_ENTRY_BOXES)
    final_denominator = Entry(root, width=BIG_ENTRY_BOX_WIDTH)
    final_denominator.pack()
    return final_nominator, final_denominator


def fifth_step_window(errors):
    clear_window()
    create_task_label(ADVANCED_TASK_VISUALIZATION)
    Label(root, text=STEP_FIVE_SUB_TASK_TEXT, pady=STANDARD_LABEL_PADDING).pack()
    final_nominator, final_denominator = create_result_entry_boxes()
    create_vertical_spacing(VERTICAL_SPACE_IN_FIFTH_STEP)
    Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
           command=lambda: fifth_step_result_window(errors, [final_nominator.get(), final_denominator.get()])).pack()


def count_nominator_errors(nominators):
    error_counter = NO_ERRORS
    denominator = task.calculate_result_denominator()
    for index in range(len(nominators)):
        try:
            if index == int(FIRST_NOMINATOR/COUNT_NOMINATORS_ONLY):
                if int(nominators[index]) != int(task.calculate_nominator_in_sum_by_index(FIRST_NOMINATOR_ONLY,
                                                                                          denominator)):
                    error_counter += ADD_ERROR
            if index == int(SECOND_NOMINATOR/COUNT_NOMINATORS_ONLY):
                if int(nominators[index]) != int(task.calculate_nominator_in_sum_by_index(SECOND_NOMINATOR_ONLY,
                                                                                          denominator)):
                    error_counter += ADD_ERROR
            if index == int(THIRD_NOMINATOR/COUNT_NOMINATORS_ONLY):
                if int(nominators[index]) != int(task.calculate_nominator_in_sum_by_index(THIRD_NOMINATOR_ONLY,
                                                                                          denominator)):
                    error_counter += ADD_ERROR
            if index == int(FOURTH_NOMINATOR/COUNT_NOMINATORS_ONLY):
                if int(nominators[index]) != int(task.calculate_nominator_in_sum_by_index(FOURTH_NOMINATOR_ONLY,
                                                                                          denominator)):
                    error_counter += ADD_ERROR
        except ValueError:
            error_counter += ADD_ERROR
    return error_counter


def fourth_step_result_window(errors, nominators):
    clear_window()
    error_counter = count_nominator_errors(nominators)
    create_task_label(ADVANCED_TASK_VISUALIZATION)
    display_right_or_wrong(error_counter, SPECIAL_MODE)
    errors[NOMINATOR_ERROR] = errors[NOMINATOR_ERROR] + error_counter
    create_vertical_spacing(VERTICAL_SPACE_IN_FOURTH_STEP_RESULT)
    Button(root, text=ADVANCE_BUTTON_TEXT, command=lambda: fifth_step_window(errors)).pack()


def create_fourth_step_finalize_button(nominators, errors):
    if task.is_hard():
        if task.number_of_additional_fractions == MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK:
            Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
                   command=lambda: fourth_step_result_window(errors,
                                                    [nominators[FIRST_NOMINATOR].get(),
                                                     nominators[int(SECOND_NOMINATOR / COUNT_NOMINATORS_ONLY)].get(),
                                                     nominators[int(THIRD_NOMINATOR / COUNT_NOMINATORS_ONLY)].get(),
                                                     nominators[int(FOURTH_NOMINATOR / COUNT_NOMINATORS_ONLY)].get()]))\
                .pack(side=LEFT)
        else:
            Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
                   command=lambda: fourth_step_result_window(errors,
                                                    [nominators[FIRST_NOMINATOR].get(),
                                                     nominators[int(SECOND_NOMINATOR / COUNT_NOMINATORS_ONLY)].get(),
                                                     nominators[int(THIRD_NOMINATOR / COUNT_NOMINATORS_ONLY)].get()]))\
                .pack(side=LEFT)
    else:
        Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
               command=lambda: fourth_step_result_window(errors,
                                                    [nominators[FIRST_NOMINATOR].get(),
                                                     nominators[int(SECOND_NOMINATOR / COUNT_NOMINATORS_ONLY)].get()]))\
            .pack(side=LEFT)


def fourth_step_window(errors, denominator):
    clear_window()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    Label(root, text=STEP_FOUR_SUB_TASK_TEXT).pack()
    message = DENOMINATOR_ANNOUNCEMENT_TEXT + str(int(denominator))
    Label(root, text=message, pady=STANDARD_LABEL_PADDING).pack()
    first_nominator, second_nominator, third_nominator, fourth_nominator = create_nominator_denominator_entry_boxes()
    create_vertical_spacing(VERTICAL_SPACE_IN_FOURTH_STEP)
    create_horizontal_spacing(STANDARD_SPACE_BEFORE_BUTTONS)
    create_fourth_step_finalize_button([first_nominator, second_nominator, third_nominator, fourth_nominator], errors)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    create_advice_button(NOMINATOR_ADVICE)


def is_there_error_in_third_step(denominator):
    new_denominator = task.calculate_result_denominator()
    error_counter = NO_ERRORS
    try:
        if int(denominator) != int(new_denominator):
            error_counter += ADD_ERROR
    except ValueError:
        error_counter += ADD_ERROR
    return error_counter


def third_step_result_window(errors, denominator):
    clear_window()
    new_denominator = task.calculate_result_denominator()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    error_counter = is_there_error_in_third_step(denominator)
    display_right_or_wrong(error_counter, SIMPLE_MODE)
    errors[DENOMINATOR_ERROR] = errors[DENOMINATOR_ERROR] + error_counter
    message = RIGHT_ANSWER_ANNOUNCEMENT_TEXT + str((int(new_denominator)))
    Label(root, text=message).pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_THIRD_STEP_RESULT)
    Button(root, text=ADVANCE_BUTTON_TEXT, command=lambda: fourth_step_window(errors, new_denominator)).pack()


def third_step_window(errors):
    clear_window()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    Label(root, text=STEP_THREE_SUB_TASK_TEXT, pady=STANDARD_LABEL_PADDING).pack()
    denominator = Entry(root, width=BIG_ENTRY_BOX_WIDTH)
    denominator.pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_THIRD_STEP)
    create_horizontal_spacing(STANDARD_SPACE_BEFORE_BUTTONS)
    Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
           command=lambda: third_step_result_window(errors, denominator.get())).pack(side=LEFT)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    create_advice_button(DENOMINATOR_ADVICE)


def count_simplify_errors(nominators_and_denominators):
    error_counter = NO_ERRORS
    for index in range(len(nominators_and_denominators)):
        try:
            if index == FIRST_NOMINATOR:
                if int(nominators_and_denominators[FIRST_NOMINATOR]) != int(task.first_fraction.get_nominator()):
                    error_counter += ADD_ERROR
            if index == FIRST_DENOMINATOR:
                if int(nominators_and_denominators[FIRST_DENOMINATOR]) != int(task.first_fraction.get_denominator()):
                    error_counter += ADD_ERROR
            if index == SECOND_NOMINATOR:
                if int(nominators_and_denominators[SECOND_NOMINATOR]) != int(task.second_fraction.get_nominator()):
                    error_counter += ADD_ERROR
            if index == SECOND_DENOMINATOR:
                if int(nominators_and_denominators[SECOND_DENOMINATOR]) != int(task.second_fraction.get_denominator()):
                    error_counter += ADD_ERROR
            if index == THIRD_NOMINATOR:
                if int(nominators_and_denominators[THIRD_NOMINATOR]) != int(task.third_fraction.get_nominator()):
                    error_counter += ADD_ERROR
            if index == THIRD_DENOMINATOR:
                if int(nominators_and_denominators[THIRD_DENOMINATOR]) != int(task.third_fraction.get_denominator()):
                    error_counter += ADD_ERROR
            if index == FOURTH_NOMINATOR:
                if int(nominators_and_denominators[FOURTH_NOMINATOR]) != int(task.fourth_fraction.get_nominator()):
                    error_counter += ADD_ERROR
            if index == FOURTH_DENOMINATOR:
                if int(nominators_and_denominators[FOURTH_DENOMINATOR]) != int(task.fourth_fraction.get_denominator()):
                    error_counter += ADD_ERROR
        except ValueError:
            error_counter += ADD_ERROR
    return error_counter


def second_step_result_window(errors, nominators_and_denominators):
    clear_window()
    task.simplify_fractions()
    error_counter = count_simplify_errors(nominators_and_denominators)
    create_task_label(STANDARD_TASK_VISUALIZATION)
    display_right_or_wrong(error_counter, SPECIAL_MODE)
    errors[SIMPLIFY_ERROR] = errors[SIMPLIFY_ERROR] + error_counter
    create_vertical_spacing(VERTICAL_SPACE_IN_SECOND_STEP_RESULT)
    Button(root, text=ADVANCE_BUTTON_TEXT, command=lambda: third_step_window(errors)).pack()


def create_visualized_fraction_labels():
    frame = Frame(root)
    frame.pack()
    Label(frame, text=task.first_fraction.visualize_as_string()).pack(side=LEFT)
    Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOX_LABELS).pack(side=LEFT)
    Label(frame, text=task.second_fraction.visualize_as_string()).pack(side=LEFT)
    if task.is_hard():
        Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOX_LABELS).pack(side=LEFT)
        Label(frame, text=task.third_fraction.visualize_as_string()).pack(side=LEFT)
        if task.number_of_additional_fractions == MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK:
            Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOX_LABELS).pack(side=LEFT)
            Label(frame, text=task.fourth_fraction.visualize_as_string()).pack(side=LEFT)


def create_nominator_denominator_entry_boxes():
    frame = Frame(root)
    frame.pack()
    first = Entry(frame, width=STANDARD_ENTRY_BOX_WIDTH)
    first.pack(side=LEFT)
    Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOXES).pack(side=LEFT)
    second = Entry(frame, width=STANDARD_ENTRY_BOX_WIDTH)
    second.pack(side=LEFT)
    if task.is_hard():
        Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOXES).pack(side=LEFT)
        third = Entry(frame, width=STANDARD_ENTRY_BOX_WIDTH)
        third.pack(side=LEFT)
        if task.number_of_additional_fractions == MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK:
            Label(frame, padx=STANDARD_SPACE_BETWEEN_ENTRY_BOXES).pack(side=LEFT)
            fourth = Entry(frame, width=STANDARD_ENTRY_BOX_WIDTH)
            fourth.pack(side=LEFT)
        else:
            fourth = PLACEHOLDER
    else:
        third = PLACEHOLDER
        fourth = PLACEHOLDER
    return first, second, third, fourth


def create_second_step_finalize_button(nominators_and_denominators, errors):
    if task.is_hard():
        if task.number_of_additional_fractions == MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK:
            Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
                   command=lambda: second_step_result_window(errors,
                                                             [nominators_and_denominators[FIRST_NOMINATOR].get(),
                                                              nominators_and_denominators[FIRST_DENOMINATOR].get(),
                                                              nominators_and_denominators[SECOND_NOMINATOR].get(),
                                                              nominators_and_denominators[SECOND_DENOMINATOR].get(),
                                                              nominators_and_denominators[THIRD_NOMINATOR].get(),
                                                              nominators_and_denominators[THIRD_DENOMINATOR].get(),
                                                              nominators_and_denominators[FOURTH_NOMINATOR].get(),
                                                              nominators_and_denominators[FOURTH_DENOMINATOR].get()])) \
                .pack(side=LEFT)
        else:
            Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
                   command=lambda: second_step_result_window(errors,
                                                             [nominators_and_denominators[FIRST_NOMINATOR].get(),
                                                              nominators_and_denominators[FIRST_DENOMINATOR].get(),
                                                              nominators_and_denominators[SECOND_NOMINATOR].get(),
                                                              nominators_and_denominators[SECOND_DENOMINATOR].get(),
                                                              nominators_and_denominators[THIRD_NOMINATOR].get(),
                                                              nominators_and_denominators[THIRD_DENOMINATOR].get()])) \
                .pack(side=LEFT)
    else:
        Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
               command=lambda: second_step_result_window(errors,
                                                         [nominators_and_denominators[FIRST_NOMINATOR].get(),
                                                          nominators_and_denominators[FIRST_DENOMINATOR].get(),
                                                          nominators_and_denominators[SECOND_NOMINATOR].get(),
                                                          nominators_and_denominators[SECOND_DENOMINATOR].get()])) \
            .pack(side=LEFT)


def second_step_window(errors):
    clear_window()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    Label(root, text=STEP_TWO_SUB_TASK_TEXT).pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_SECOND_STEP)
    create_visualized_fraction_labels()
    create_vertical_spacing(VERTICAL_SPACE_IN_SECOND_STEP)
    first_nominator, second_nominator, third_nominator, fourth_nominator = create_nominator_denominator_entry_boxes()
    create_vertical_spacing(VERTICAL_SPACE_IN_SECOND_STEP)
    first_denominator, second_denominator, third_denominator, fourth_denominator = \
        create_nominator_denominator_entry_boxes()
    create_vertical_spacing(VERTICAL_SPACE_IN_SECOND_STEP)
    create_horizontal_spacing(STANDARD_SPACE_BEFORE_BUTTONS)
    create_second_step_finalize_button([first_nominator, first_denominator,
                                        second_nominator, second_denominator,
                                        third_nominator, third_denominator,
                                        fourth_nominator, fourth_denominator], errors)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    create_advice_button(SIMPLIFY_ADVICE)


def first_step_result_window(answer, errors):
    clear_window()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    error_counter = NO_ERRORS
    if answer != task.contains_real_fraction():
        error_counter += ADD_ERROR
    display_right_or_wrong(error_counter, SIMPLE_MODE)
    errors[IDENTIFICATION_ERROR] = errors[IDENTIFICATION_ERROR] + error_counter
    Label(root, text=FIRST_STEP_REVIEW_TEXT).pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_FIRST_STEP_RESULT)
    Button(root, text=ADVANCE_BUTTON_TEXT, command=lambda: second_step_window(errors)).pack()


def build_error_counter_message(number_of_errors):
    return ERROR_COUNTER_MESSAGE_BEGINNING + str(number_of_errors) + ERROR_COUNTER_MESSAGE_END


def half_rounded_down(number):
    return number // 2


def get_error_message(errors):
    number_of_errors = sum(errors)
    required_number_of_errors_to_get_feedback = half_rounded_down(number_of_errors)
    if errors[IDENTIFICATION_ERROR] > required_number_of_errors_to_get_feedback:
        return ERROR_FEEDBACK_IDENTIFICATION_ERRORS_MESSAGE
    elif errors[SIMPLIFY_ERROR] > required_number_of_errors_to_get_feedback:
        return ERROR_FEEDBACK_SIMPLIFY_ERRORS_MESSAGE
    elif errors[DENOMINATOR_ERROR] > required_number_of_errors_to_get_feedback:
        return ERROR_FEEDBACK_DENOMINATOR_ERRORS_MESSAGE
    elif errors[NOMINATOR_ERROR] > required_number_of_errors_to_get_feedback:
        return ERROR_FEEDBACK_NOMINATOR_ERRORS_MESSAGE
    elif errors[ADDITION_ERROR] > required_number_of_errors_to_get_feedback:
        return ERROR_FEEDBACK_ADDITION_ERRORS_MESSAGE
    else:
        return ERROR_FEEDBACK_DIFFERENT_TYPES_OF_ERRORS_MESSAGE


def create_error_feedback(errors):
    number_of_errors = sum(errors)
    if number_of_errors > BAD_RESULT:
        Label(root, text=ERROR_FEEDBACK_MAIN_MESSAGE).pack()
        Label(root, text=get_error_message(errors)).pack()
        create_vertical_spacing(VERTICAL_SPACE_IN_ERROR_FEEDBACK_WITH_ERRORS)
    else:
        create_vertical_spacing(VERTICAL_SPACE_IN_ERROR_FEEDBACK_WITHOUT_ERRORS)


def errors_report_and_feedback_window(errors):
    clear_window()
    number_of_errors = sum(errors)
    Label(root, text=build_error_counter_message(number_of_errors), pady=STANDARD_LABEL_PADDING).pack()
    create_error_feedback(errors)
    create_horizontal_spacing(SPACE_BEFORE_NEW_DIFFICULTY_SELECTION_BUTTON)
    Button(root, text=SELECT_NEW_DIFFICULTY_BUTTON_TEXT, padx=SELECT_NEW_DIFFICULTY_BUTTON_SIZE,
           command=lambda: difficulty_selection_window()).pack(side=LEFT)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    Button(root, text=END_APP_BUTTON_TEXT, padx=END_APP_BUTTON_SIZE, command=lambda: root.quit()).pack(side=LEFT)


def display_right_or_wrong(error_counter, mode):
    if error_counter == NO_ERRORS:
        Label(root, text=RIGHT_ANSWER_TEXT).pack()
    elif mode == SIMPLE_MODE:
        Label(root, text=WRONG_ANSWER_TEXT).pack()
    else:
        Label(root, text=build_error_counter_message(error_counter)).pack()


def non_task_window(answer, errors):
    clear_window()
    create_task_label(STANDARD_TASK_VISUALIZATION)
    error_counter = NO_ERRORS
    if answer != task.contains_real_fraction():
        error_counter += ADD_ERROR
    display_right_or_wrong(error_counter, SIMPLE_MODE)
    errors[IDENTIFICATION_ERROR] = errors[IDENTIFICATION_ERROR] + error_counter
    Label(root, text=NON_TASK_REVIEW_TEXT).pack()
    create_vertical_spacing(VERTICAL_SPACE_IN_NON_TASK)
    create_horizontal_spacing(SPACE_BEFORE_BUTTONS_IN_NON_TASK)
    Button(root, text=ADVANCE_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
           command=lambda: first_step_window(errors)).pack(side=LEFT)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    Button(root, text=FINISH_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
           command=lambda: errors_report_and_feedback_window(errors)).pack(side=LEFT)


def create_first_step_selection_section(radio_button_variable):
    radio_button_frame = Frame(root, bd=FRAME_BORDER_WIDTH, relief=FRAME_BORDER_TYPE)
    radio_button_frame.pack()
    Radiobutton(radio_button_frame, text=YES_OPTION_TEXT, variable=radio_button_variable, value=True).pack(anchor=W)
    Radiobutton(radio_button_frame, text=NO_OPTION_TEXT, variable=radio_button_variable, value=False).pack(anchor=W)


def create_first_step_finalize_button(variable, errors):
    if task.contains_real_fraction():
        Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
               command=lambda: first_step_result_window(variable.get(), errors)).pack(side=LEFT)
    else:
        Button(root, text=CHECK_ANSWER_BUTTON_TEXT, padx=FINALIZE_STEP_BUTTON_SIZE,
               command=lambda: non_task_window(variable.get(), errors)).pack(side=LEFT)


def first_step_window(errors):
    clear_window()
    task.randomize()
    is_fraction = BooleanVar()
    is_fraction.set(str(True))
    create_task_label(STANDARD_TASK_VISUALIZATION)
    Label(root, text=STEP_ONE_SUB_TASK_TEXT, pady=STEP_ONE_SUB_TASK_PADDING).pack()
    create_first_step_selection_section(is_fraction)
    create_vertical_spacing(VERTICAL_SPACE_IN_FIRST_STEP)
    create_horizontal_spacing(STANDARD_SPACE_BEFORE_BUTTONS)
    create_first_step_finalize_button(is_fraction, errors)
    create_horizontal_spacing(STANDARD_SPACE_BETWEEN_BUTTONS)
    create_advice_button(IDENTIFICATION_ADVICE)


def determine_operator_type(difficulty):
    if difficulty == EASY_ADDITION or difficulty == HARD_ADDITION:
        return PLUS
    else:
        return MINUS


def determine_difficulty_of_task(difficulty, task_operator):
    if difficulty == HARD_ADDITION or difficulty == HARD_SUBTRACTION:
        return HardTask(task_operator)
    else:
        return Task(task_operator)


def create_task_and_start_process(difficulty):
    clear_window()
    errors = [STARTING_NUMBER_OF_ERRORS,
              STARTING_NUMBER_OF_ERRORS,
              STARTING_NUMBER_OF_ERRORS,
              STARTING_NUMBER_OF_ERRORS,
              STARTING_NUMBER_OF_ERRORS]
    task_operator = determine_operator_type(difficulty)
    # noinspection PyGlobalUndefined
    global task
    task = determine_difficulty_of_task(difficulty, task_operator)
    first_step_window(errors)


def create_select_difficulty_section(radio_button_variable):
    radio_button_frame = Frame(root, bd=FRAME_BORDER_WIDTH, relief=FRAME_BORDER_TYPE)
    radio_button_frame.pack()
    Radiobutton(radio_button_frame, text=EASY_ADDITION_TEXT,
                variable=radio_button_variable, value=EASY_ADDITION).pack(anchor=W)
    Radiobutton(radio_button_frame, text=EASY_SUBTRACTION_TEXT,
                variable=radio_button_variable, value=EASY_SUBTRACTION).pack(anchor=W)
    Radiobutton(radio_button_frame, text=HARD_ADDITION_TEXT,
                variable=radio_button_variable, value=HARD_ADDITION).pack(anchor=W)
    Radiobutton(radio_button_frame, text=HARD_SUBTRACTION_TEXT,
                variable=radio_button_variable, value=HARD_SUBTRACTION).pack(anchor=W)


def difficulty_selection_window():
    clear_window()
    difficulty = IntVar()
    difficulty.set(str(EASY_ADDITION))
    Label(root, text=SELECT_DIFFICULTY_MESSAGE, pady=STANDARD_LABEL_PADDING).pack()
    create_select_difficulty_section(difficulty)
    create_vertical_spacing(VERTICAL_SPACE_IN_DIFFICULTY_SELECTION)
    Button(root, text=ADVANCE_BUTTON_TEXT, command=lambda: create_task_and_start_process(difficulty.get())).pack()


root = Tk()
root.geometry(WINDOW_SIZE)
root.resizable(False, False)
root.title(WINDOW_TITLE)
difficulty_selection_window()
root.mainloop()
