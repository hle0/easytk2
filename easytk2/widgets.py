from tkinter import DISABLED, ttk
import tkinter


class CopyableLabel(tkinter.Text):

    def __init__(self, *args, text="", **kwargs):
        super().__init__(*args, **kwargs)
        self.insert("1.0", text)
        self["state"] = DISABLED
        self.update()


class AsyncButtonMixin:

    def __init__(self, *args, command=None, **kwargs) -> None:
        if command is not None:
            kwargs["command"] = lambda: self.master.create_task(command())
        super().__init__(*args, **kwargs)


class AButton(AsyncButtonMixin, ttk.Button):
    pass
