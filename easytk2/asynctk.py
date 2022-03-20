import asyncio
from tkinter import Tk


class AsyncTkMixin:
    # https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui
    def __init__(self, *args, loop=None, interval=1 / 120, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = loop or asyncio.get_event_loop()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.fut = self.loop.create_future()
        self.fut.add_done_callback(lambda _: self.close())
        self.create_task(self.async_updater(interval))

    def create_task(self, coro):
        task = self.loop.create_task(coro)
        self.fut.add_done_callback(lambda _: task.cancel())
        return task

    def run_in_executor(self, *args, **kwargs):
        task = self.loop.run_in_executor(*args, **kwargs)
        self.fut.add_done_callback(lambda _: task.cancel())
        return task

    async def async_updater(self, interval):
        while True:
            self.update()
            await asyncio.sleep(interval)

    def close(self):
        self.destroy()

    def resolve(self, obj):
        self.fut.set_result(obj)

    async def wait(self):
        return await self.fut


class AsyncTk(AsyncTkMixin, Tk):
    pass
