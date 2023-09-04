"""
The viewport is the main container for the GUI.
It is the first container to be rendered.
"""

import flet

import config

components = config.Components([]).components

view_base = flet.Container(
    # image_src="background.png",
    blur=3,
    image_fit=flet.ImageFit.COVER,
    border_radius=8,
    expand=True,
)
components.extend(
    [
        [view_base, str, "image_src", "view_base", "image_url"],
        [view_base, str, "gradient", "view_base", "color"],
        [view_base, [int, None], "blur", "viewport", "blur"]
    ]
)

view_container = flet.Container(
    content=view_base,
    blur=None,
    image_fit=flet.ImageFit.COVER,
    border_radius=8,
    expand=True,
    padding=8,
)
components.extend(
    [
        [view_container, [int, None], "blur", "viewport", "blur"],
    ]
)

base = flet.Container(
    flet.Row(
        [
            flet.Row(
                [
                    view_container
                ],
                expand=True,
                alignment=flet.MainAxisAlignment.CENTER,
                vertical_alignment=flet.CrossAxisAlignment.CENTER,
                spacing=0
            ),
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        vertical_alignment=flet.CrossAxisAlignment.START,
        spacing=0
    ),
    alignment=flet.alignment.center,
    # image_src="background.png",
    image_src="https://wallpaperaccess.com/full/8351171.gif",
    image_fit=flet.ImageFit.COVER,
    expand=True,
    margin=0,
)
components.extend(
    [
        [base, str, "image_src", "base", "image_url"],
        [base, str, "gradient", "base", "color"]
    ]
)
