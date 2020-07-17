import random

MIN_VALUE_NOMINATOR_DENOMINATOR = 1
MAX_VALUE_NOMINATOR_DENOMINATOR = 20
MIN_COMMON_DIVISOR = 1
ZERO_REMAINDER = 0
EMPTY_STRING = ""
SPACE = " "
DIVISION_SIGN = "/"
OPEN_PARENTHESIS = " ("
CLOSE_PARENTHESIS = ") "


# helping function
def randomize_number(minimal_value, maximal_value):
    return random.randint(minimal_value, maximal_value)


# helping function
def is_divisible(integer, factor):
    return integer % factor == ZERO_REMAINDER


# helping function
def calculate_greatest_common_divisor(first_number, second_number):
    lower_number = min(first_number, second_number)
    greatest_common_divisor = MIN_COMMON_DIVISOR
    for potential_common_divisor in range(MIN_COMMON_DIVISOR, lower_number + MIN_COMMON_DIVISOR):
        if is_divisible(first_number, potential_common_divisor) \
                and is_divisible(second_number, potential_common_divisor)\
                and greatest_common_divisor < potential_common_divisor:
            greatest_common_divisor = potential_common_divisor
    return greatest_common_divisor


# helping function
def calculate_least_common_multiple(first_number, second_number):
    return int(first_number * second_number)\
           / int(calculate_greatest_common_divisor(int(first_number), int(second_number)))


# An object that has the properties and functions of simple fractions that students in 5th grade know and which the
# application is going to use in order to compare the answers the students give in each step of an addition or a
# subtraction task containing said fractions to the real ones.
class Fraction:

    def __init__(self):
        self.nominator = MIN_VALUE_NOMINATOR_DENOMINATOR
        self.denominator = MIN_VALUE_NOMINATOR_DENOMINATOR
        self.is_proper = False
        self.is_simplified = False

    def randomize(self):
        self.nominator = randomize_number(MIN_VALUE_NOMINATOR_DENOMINATOR, MAX_VALUE_NOMINATOR_DENOMINATOR)
        self.denominator = randomize_number(MIN_VALUE_NOMINATOR_DENOMINATOR, MAX_VALUE_NOMINATOR_DENOMINATOR)
        self.determine_propriety()
        self.is_simplified = False

    def visualize_as_string(self):
        representation = EMPTY_STRING
        if not self.is_proper and not self.is_simplified:
            if self.is_integer():
                representation = representation + str(self.nominator/self.denominator) + SPACE
            else:
                representation = representation + str(self.nominator // self.denominator) + OPEN_PARENTHESIS + \
                                 str(self.nominator % self.denominator) + DIVISION_SIGN + \
                                 str(self.denominator) + CLOSE_PARENTHESIS
        else:
            representation = str(self.nominator) + DIVISION_SIGN + str(self.denominator) + SPACE
        return representation

    def determine_propriety(self):
        if self.nominator < self.denominator:
            self.is_proper = True

    def is_integer(self):
        return is_divisible(self.nominator, self.denominator)

    def simplify(self):
        divisor = calculate_greatest_common_divisor(self.nominator, self.denominator)
        self.nominator = int(self.nominator / divisor)
        self.denominator = int(self.denominator / divisor)
        self.is_simplified = True

    def calculate(self):
        return self.nominator/self.denominator

    def calculate_nominator_for_given_denominator(self, potential_denominator):
        return int((potential_denominator / self.denominator) * self.nominator)

    def get_nominator(self):
        return int(self.nominator)

    def get_denominator(self):
        return int(self.denominator)
