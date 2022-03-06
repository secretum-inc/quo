#!/usr/bin/env python
"""
A simple example of a few buttons and click handlers.
"""
from quo.console import Console, get_app
from quo.widget import Button, TextArea, Box, Frame, Label
from quo.layout import Layout, VSplit, HSplit


# Event handlers for all the buttons.
def button1():
    get_app()
    text_area.text = "Button 1 clicked"


def button2():
    text_area.text = "Button 2 clicked"

import os 
def button3():
    text_area.text = "Button 3 clicked"


def exit():
    get_app().exit()


# All the widgets for the UI.


b1 = Button("Button 1", handler=button1)
b2 = Button("Button 2", handler=button2)
b3 = Button("Button 3", handler=button3)
b4 = Button("Exit", handler=exit)
text_area = TextArea(focusable=True)


# Combine all the widgets in a UI.
# The `Box` object ensures that padding will be inserted around the containing
# widget. It adapts automatically, unless an explicit `padding` amount is given.
root_container = Box(
        (
        [
            Label(text="Press `Tab` to move the focus."),
            VSplit([
                Box(body=HSplit([b1, b2, b3, b4], padding=1),
                        padding=1,
                        style="class:left-pane"),
                Box(body=Frame(text_area), padding=1, style="class:right-pane")
                ]
            ),
        ]
    ),
)

layout = Layout(container=root_container, focused_element=b1)


# Key bindings.
kb = KeyBinder()

kb.add("tab")(quo.keys.focus.next)
kb.add("s-tab")(quo.keys.focus.previous)


# Styling.

styling = Style

style = styling(
    [
        ("left-pane", "bg:#888800 #000000"),
        ("right-pane", "bg:#00aa00 #000000"),
        ("button", "#000000"),
        ("button-arrow", "#000000"),
        ("button focused", "bg:#ff0000"),
        ("text-area focused", "bg:#ff0000"),
    ]
)


# Build a main application object.
application = Console(layout=layout, bind=kb, style=style, full_screen=True)


def main():
    application.run()


if __name__ == "__main__":
    main()
