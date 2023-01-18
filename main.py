from src.menu import Menu
from src.settings import Settings
import argparse

def setup_arg_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--banner_show',
                        choices= [0, 1],
                        help='Whether show (1) or not (0) starting banner')

    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = setup_arg_parser()

    _settings = Settings()
    _settings.apply_cli_arguments(args)
    Menu().showMenu()
    print("Exit. Bye-bye!")