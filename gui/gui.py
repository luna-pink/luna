"""
This module contains the user interface for the application.
"""

import flet

import config
from gui import components
from .style import theme


async def user_interface(page: flet.Page):
    """
    The user_interface function is the entry point of the program.
    :param page:
    :return:
    """
    for setting, value in config.InterfaceSettings().__dict__.items():
        setattr(page, setting, value)

    page.theme = theme
    page.theme_mode = flet.ThemeMode.DARK

    await page.window_center_async()

    await page.add_async(
        components.base
    )

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
