# easytk2
WARNING: This library is in alpha stage. Expect breaking changes when it is most inconvenient for you.

easytk2 is a library that is designed to make doing common tasks with Tkinter easier.

Specifically, it aims to make bridging async or threaded code to Tkinter less painful. 
It does this by replacing Tkinter's mainloop with asyncio's event loop, adding async callbacks to some widgets, and replacing callback-based sync code with future-based async code.

For more information, look at `samples/`, and the code for easytk2 itself.

Contributions are welcome.