# https://github.com/pywinauto/pywinauto

from pywinauto import Application, mouse

mouse_position = mouse.get_position()

app = Application().connect(handle=mouse.get_foreground_window())

window_title = app.top_window().window_text()

mouse.click(button='left', coords=mouse_position)

print("current active window:", window_title)
