"""
This module contains the style of the application.
"""

import flet

color_scheme_dark = flet.ColorScheme(
    primary="#D0BCFF",
    on_primary="#381E72",
    primary_container="#4F378B",
    on_primary_container="#EADDFF",
    secondary="#CCC2DC",
    on_secondary="#332D41",
    secondary_container="#4A4458",
    on_secondary_container="#E8DEF8",
    tertiary="#EFB8C8",
    on_tertiary="#492532",
    tertiary_container="#633B48",
    on_tertiary_container="#FFD8E4",
    error="#F2B8B5",
    on_error="#601410",
    error_container="#8C1D18",
    on_error_container="#F9DEDC",
    outline="#938F99",
    background="#1C1B1F",
    on_background="#E6E1E5",
    surface="#1C1B1F",
    on_surface="#E6E1E5",
    surface_variant="#49454F",
    on_surface_variant="#CAC4D0",
    inverse_surface="#E6E1E5",
    on_inverse_surface="#313033",
    inverse_primary="#6750A4",
    shadow="#000000",
    surface_tint="#D0BCFF",
    outline_variant="#49454F",
    scrim="#000000"
)

text_theme = flet.TextTheme(
    body_medium=flet.TextStyle(
        color=flet.colors.WHITE
    )
)

transition = flet.PageTransitionsTheme(
    android=None,
    ios=None,
    linux=None,
    macos=None,
    windows=None
)

# noinspection PyUnusedName
theme = flet.Theme(
    color_scheme=color_scheme_dark,
    text_theme=text_theme,
    page_transitions=transition
)
