#!/usr/bin/env python
"""
Demonstration of a custom completer class and the possibility of styling
completions independently.
"""
import quo

colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "yellow",
    "cyan",
    "magenta",
    "pink",
]

session = quo.Prompt()

class ColorCompleter(quo.completion.Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        for color in colors:
            if color.startswith(word):
                yield quo.completion.Completion(
                    color,
                    start_position=-len(word),
                    style="fg:" + color,
                    selected_style="fg:white bg:" + color,
                )


def main():
    # Simple completion menu.
    print("(The completion menu displays colors.)")
    session.prompt("Type a color: ", completer=ColorCompleter())

    # Multi-column menu.
    session.prompt(
        "Type a color: ",
        completer=ColorCompleter(),
        complete_style=quo.completion.CompleteStyle.multi_column,
    )

    # Readline-like
    session.prompt(
        "Type a color: ",
        completer=ColorCompleter(),
        complete_style=quo.completion.CompleteStyle.neat,
    )

    # Prompt with true color output.
    message = [
        ("#cc2244", "T"),
        ("#bb4444", "r"),
        ("#996644", "u"),
        ("#cc8844", "e "),
        ("#ccaa44", "C"),
        ("#bbaa44", "o"),
        ("#99aa44", "l"),
        ("#778844", "o"),
        ("#55aa44", "r "),
        ("#33aa44", "p"),
        ("#11aa44", "r"),
        ("#11aa66", "o"),
        ("#11aa88", "m"),
        ("#11aaaa", "p"),
        ("#11aacc", "t"),
        ("#11aaee", ": "),
    ]
    session.prompt(message, completer=ColorCompleter(), color_depth=quo.color.ColorDepth.twenty_four_bit)


if __name__ == "__main__":
    main()
