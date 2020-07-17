from Fraction import *

PLUS = "+"
MINUS = "-"
EQUALS_SIGN = " = "
MIN_ADDITIONAL_FRACTIONS_IN_HARD_TASK = 1
MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK = 2
FIRST_NOMINATOR_ONLY = 1
SECOND_NOMINATOR_ONLY = 2
THIRD_NOMINATOR_ONLY = 3
FOURTH_NOMINATOR_ONLY = 4


# An Object that has the properties of an addition or subtraction task containing exactly two fractions that can be
# solved by a 5th grader. It contains functions that can compute "sub-tasks" that the students have to learn and
# it is used in the application in order to verify the students answers.
class Task:

    def __init__(self, operator):
        self.first_fraction = Fraction()
        self.second_fraction = Fraction()
        self.operator = operator
        self.result_fraction = Fraction()

    def is_subtraction_task(self):
        return self.operator is MINUS

    def randomize(self):
        self.first_fraction.randomize()
        self.second_fraction.randomize()
        if not self.is_computable_by_app_user():
            self.randomize()
        else:
            self.calculate_result()
            self.result_fraction.simplify()

    def is_computable_by_app_user(self):
        if self.is_subtraction_task():
            return self.first_fraction.calculate() >= self.second_fraction.calculate()
        else:
            return True

    def visualize_as_string(self):
        representation = EMPTY_STRING
        representation = representation + self.first_fraction.visualize_as_string() + self.operator + SPACE + \
                         self.second_fraction.visualize_as_string()
        return representation

    def visualize_with_result_as_string(self):
        representation = EMPTY_STRING
        representation = representation + self.visualize_result_equation_as_string() + EQUALS_SIGN \
                         + self.result_fraction.visualize_as_string()
        return representation

    def visualize_result_equation_as_string(self):
        representation = EMPTY_STRING
        calculated_denominator = int(self.calculate_result_denominator())
        representation = representation + \
                         str(int(self.calculate_nominator_in_sum_by_index(FIRST_NOMINATOR_ONLY,
                                                                          calculated_denominator))) \
                         + DIVISION_SIGN + str(calculated_denominator) + SPACE + self.operator + SPACE + \
                         str(int(self.calculate_nominator_in_sum_by_index(SECOND_NOMINATOR_ONLY,
                                                                          calculated_denominator))) \
                         + DIVISION_SIGN + str(calculated_denominator)
        return representation

    def contains_real_fraction(self):
        return not self.first_fraction.is_integer() or not self.second_fraction.is_integer()

    def simplify_fractions(self):
        self.first_fraction.simplify()
        self.second_fraction.simplify()

    def calculate_result_denominator(self):
        return calculate_least_common_multiple(self.first_fraction.denominator, self.second_fraction.denominator)

    def calculate_nominator_in_sum_by_index(self, nominator_index, denominator):
        if nominator_index == FIRST_NOMINATOR_ONLY:
            return int(self.first_fraction.calculate_nominator_for_given_denominator(denominator))
        if nominator_index == SECOND_NOMINATOR_ONLY:
            return int(self.second_fraction.calculate_nominator_for_given_denominator(denominator))

    def calculate_result(self):
        self.result_fraction.denominator = int(self.calculate_result_denominator())
        if self.is_subtraction_task():
            self.result_fraction.nominator = \
                int(self.calculate_nominator_in_sum_by_index(FIRST_NOMINATOR_ONLY, self.result_fraction.denominator)) -\
                int(self.calculate_nominator_in_sum_by_index(SECOND_NOMINATOR_ONLY, self.result_fraction.denominator))
        else:
            self.result_fraction.nominator = \
                int(self.calculate_nominator_in_sum_by_index(FIRST_NOMINATOR_ONLY, self.result_fraction.denominator)) +\
                int(self.calculate_nominator_in_sum_by_index(SECOND_NOMINATOR_ONLY, self.result_fraction.denominator))
        self.result_fraction.determine_propriety()

    def is_hard(self):
        return False


# An object that inherits the Task object and adds complexity by introducing one to two additional fractions
# in said task.
class HardTask(Task):

    def __init__(self, operator):
        super().__init__(operator)
        self.third_fraction = Fraction()
        self.fourth_fraction = Fraction()
        self.number_of_additional_fractions = MIN_ADDITIONAL_FRACTIONS_IN_HARD_TASK

    def contains_two_additional_fractions(self):
        return self.number_of_additional_fractions == MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK

    def randomize(self):
        self.number_of_additional_fractions = \
            randomize_number(MIN_ADDITIONAL_FRACTIONS_IN_HARD_TASK, MAX_ADDITIONAL_FRACTIONS_IN_HARD_TASK)
        self.third_fraction.randomize()
        if self.contains_two_additional_fractions():
            self.fourth_fraction.randomize()
        super().randomize()

    def is_computable_by_app_user(self):
        if self.is_subtraction_task():
            result_value = self.first_fraction.calculate()
            result_value -= self.second_fraction.calculate()
            result_value -= self.third_fraction.calculate()
            if self.contains_two_additional_fractions():
                result_value -= self.fourth_fraction.calculate()
            return result_value >= 0
        else:
            return True

    def visualize_as_string(self):
        representation = EMPTY_STRING
        representation = representation + super().visualize_as_string() + self.operator + SPACE + \
                         self.third_fraction.visualize_as_string()
        if self.contains_two_additional_fractions():
            representation = representation + self.operator + SPACE + self.fourth_fraction.visualize_as_string()
        return representation

    def visualize_result_equation_as_string(self):
        representation = EMPTY_STRING
        calculated_denominator = int(self.calculate_result_denominator())
        representation = representation + super().visualize_result_equation_as_string() + \
                         SPACE + self.operator + SPACE + \
                         str(int(self.calculate_nominator_in_sum_by_index(THIRD_NOMINATOR_ONLY,
                                                                          calculated_denominator))) \
                         + DIVISION_SIGN + str(calculated_denominator)
        if self.contains_two_additional_fractions():
            representation = representation + SPACE + self.operator + SPACE + \
                             str(int(self.calculate_nominator_in_sum_by_index(FOURTH_NOMINATOR_ONLY,
                                                                              calculated_denominator))) \
                             + DIVISION_SIGN + str(calculated_denominator)
        return representation

    def contains_real_fraction(self):
        if self.contains_two_additional_fractions():
            return super().contains_real_fraction() \
                   or not self.third_fraction.is_integer() \
                   or not self.fourth_fraction.is_integer()
        else:
            return super().contains_real_fraction() or not self.third_fraction.is_integer()

    def simplify_fractions(self):
        super().simplify_fractions()
        self.third_fraction.simplify()
        if self.contains_two_additional_fractions():
            self.fourth_fraction.simplify()

    def calculate_result_denominator(self):
        first_common_denominator = super().calculate_result_denominator()
        second_common_denominator = self.third_fraction.denominator
        if self.contains_two_additional_fractions():
            second_common_denominator = calculate_least_common_multiple(self.third_fraction.denominator,
                                                                        self.fourth_fraction.denominator)
        return calculate_least_common_multiple(first_common_denominator, second_common_denominator)

    def calculate_nominator_in_sum_by_index(self, nominator_index, denominator):
        if nominator_index == THIRD_NOMINATOR_ONLY:
            return int(self.third_fraction.calculate_nominator_for_given_denominator(denominator))
        if nominator_index == FOURTH_NOMINATOR_ONLY:
            return int(self.fourth_fraction.calculate_nominator_for_given_denominator(denominator))
        return super().calculate_nominator_in_sum_by_index(nominator_index, denominator)

    def calculate_result(self):
        super().calculate_result()
        if self.is_subtraction_task():
            self.result_fraction.nominator -= \
                int(self.calculate_nominator_in_sum_by_index(THIRD_NOMINATOR_ONLY, self.result_fraction.denominator))
            if self.contains_two_additional_fractions():
                self.result_fraction.nominator -= \
                    int(self.calculate_nominator_in_sum_by_index(FOURTH_NOMINATOR_ONLY, self.result_fraction.denominator))
        else:
            self.result_fraction.nominator += \
                int(self.calculate_nominator_in_sum_by_index(THIRD_NOMINATOR_ONLY, self.result_fraction.denominator))
            if self.contains_two_additional_fractions():
                self.result_fraction.nominator += \
                    int(self.calculate_nominator_in_sum_by_index(FOURTH_NOMINATOR_ONLY, self.result_fraction.denominator))

    def is_hard(self):
        return True
