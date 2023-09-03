"""
The config module is used to store the configuration of the application.
"""

from dataclasses import dataclass


# noinspection PyUnusedName
@dataclass
class InterfaceSettings:
    """
    The InterfaceSettings class is used to store the settings of the interface.
    """
    title: str = "luna"

    window_width: int = 1000
    window_height: int = 700
    window_min_width: int = 1000
    window_min_height: int = 700
    window_max_width: int = 1000
    window_max_height: int = 700
    window_resizable: bool = True
    window_title_bar_hidden: bool = True
    window_title_bar_buttons_hidden: bool = True
    window_frameless: bool = False
    window_always_on_top: bool = False

    padding: int = 0


# noinspection PyUnusedClass
@dataclass
class Components:
    """
    The Components class is used to store the components of the interface.
    """
    components: list
