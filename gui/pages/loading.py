import flet


class Loading(flet.UserControl):
    """
    The Loading class is used to display the loading screen.
    """

    def __init__(self):
        super().__init__()

    def build(self):
        """
        Build the loading screen.
        :return: 
        """

        page = flet.Column(
            controls=[
                flet.Image(
                    src="luna-pixel.gif",
                    width=280,
                ),
                flet.ProgressBar(
                    width=280,
                    bgcolor=flet.colors.TRANSPARENT,
                ),
                flet.Text(
                    value="Loading...",
                )
            ],
            alignment=flet.MainAxisAlignment.CENTER,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            expand=True,
        )

        return page
