"""
This module contains the user interface for the application.
"""

import flet

import config


async def user_interface(page: flet.Page):
    """
    The user_interface function is the entry point of the program.
    :param page:
    :return:
    """
    settings = config.InterfaceSettings()
    for setting, value in settings.__dict__.items():
        setattr(page, setting, value)

    await page.update_async()


def initialize_ui():
    """
    The initialize_ui function is used to initialize the user interface.
    :return:
    """
    flet.app(
        target=user_interface,
        view=flet.FLET_APP,
        port=5050,
        assets_dir="assets"
    )
