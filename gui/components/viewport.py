"""
The viewport is the main container for the GUI.
It is the first container to be rendered.
"""

import flet

import config

components = config.Components([]).components

base = flet.Container(
    flet.Row(
        [
            flet.Row(
                [
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
    image_src="background.png",
    image_fit=flet.ImageFit.COVER,
    expand=True,
    margin=0,
)
components.extend(
    [
        [base, "image_src", "background", "image_url"],
        [base, "gradient", "background", "color"]
    ]
)
