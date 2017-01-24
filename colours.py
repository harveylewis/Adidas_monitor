'''
Colour utilities for adidas stock checker
'''


class colour:

	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	PINK = '\033[35m'
	LIGHT_BLUE = '\033[36m'
	WHITE = '\033[37;1m'

	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def pi_(*args):
	input_string = ' '.join(map(str, args))
	return '{0}///{1:^50}///{2}'.format(
	    colour.WHITE,
	    input_string,
	    colour.ENDC,
	)




def red_(*args):
    """
    Colorize text with red
    """
    input_string = ' '.join(map(str, args))
    return colour.RED + str(input_string) + colour.ENDC


def green_(*args):
    """
    Colorize text with green
    """
    input_string = ' '.join(map(str, args))
    return colour.GREEN + str(input_string) + colour.ENDC


def yellow_(*args):
    """
    Colorize text with yellow
    """
    input_string = ' '.join(map(str, args))
    return colour.YELLOW + str(input_string) + colour.ENDC


def blue_(*args):
    """
    Colorize text with blue
    """
    input_string = ' '.join(map(str, args))
    return colour.BLUE + str(input_string) + colour.ENDC


def pink_(*args):
    """
    Colorize text with pink
    """
    input_string = ' '.join(map(str, args))
    return colour.PINK + str(input_string) + colour.ENDC



def light_blue_(*args):
    """
    Colorize text with light blue
    """
    input_string = ' '.join(map(str, args))
    return colour.LIGHT_BLUE + str(input_string) + colour.ENDC


