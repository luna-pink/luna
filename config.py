from dataclasses import dataclass


# noinspection PyUnusedName
@dataclass
class InterfaceSettings:
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
