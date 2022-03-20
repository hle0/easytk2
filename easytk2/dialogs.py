from tkinter import ttk

from . import helpers, widgets


@helpers.prefab
def okdialog(tk, text):
    tk.grid()

    helpers.grid(
        """
        +-+
        |t|
        |k|
        +-+
        """,
        t=widgets.CopyableLabel(tk, text=text),
        k=ttk.Button(tk, text="Ok", command=lambda: tk.resolve(None)),
    )
