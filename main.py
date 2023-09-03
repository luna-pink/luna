#    __         __  __     __   __     ______
#   /\ \       /\ \/\ \   /\ "-.\ \   /\  __ \
#   \ \ \____  \ \ \_\ \  \ \ \-.  \  \ \  __ \
#    \ \_____\  \ \_____\  \ \_\\"\_\  \ \_\ \_\
#     \/_____/   \/_____/   \/_/ \/_/   \/_/\/_/

"""luna selfbot main file."""

import argparse

import gui


def main():
    """
    The main function of Luna.
    :return:
    """

    parser = argparse.ArgumentParser(
        description='Luna selfbot, one step ahead of Discord.'
    )

    parser.add_argument(
        '-c',
        '--cli',
        action='store_true',
        help='Run the CLI version of Luna.'
    )

    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='Print the version of Luna.'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging.'
    )

    gui.initialize_ui()


if __name__ == '__main__':
    main()
