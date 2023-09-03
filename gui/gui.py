import flet

import config


async def user_interface(page: flet.Page):
    settings = config.InterfaceSettings()
    for setting, value in settings.__dict__.items():
        setattr(page, setting, value)

    await page.update_async()


def initialize_ui():
    flet.app(target=user_interface, view=flet.FLET_APP, port=5050, assets_dir="assets")
