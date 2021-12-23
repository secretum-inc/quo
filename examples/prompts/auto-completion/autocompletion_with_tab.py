#!/usr/bin/env python
"""
Autocompletion example.

Press [Tab] to complete the current word.
- The first Tab press fills in the common part of all completions
    and shows all the completions. (In the menu)
- Any following tab press cycles through all the possible completions.
"""
import quo

animal_completer = quo.completion.WordCompleter(
    [
        "alligator",
        "ant",
        "ape",
        "bat",
        "bear",
        "beaver",
        "bee",
        "bison",
        "butterfly",
        "cat",
        "chicken",
        "crocodile",
        "dinosaur",
        "dog",
        "dolphin",
        "dove",
        "duck",
        "eagle",
        "elephant",
        "fish",
        "goat",
        "gorilla",
        "kangaroo",
        "leopard",
        "lion",
        "mouse",
        "rabbit",
        "rat",
        "snake",
        "spider",
        "turkey",
        "turtle",
    ],
    ignore_case=True,
)

session = quo.Prompt(completer=animal_completer, complete_while_typing=False)

@quo.command()
@quo.app("@complete", help="Press [Tab] for completions")
def main(complete):
    """
    Press [Tab] to complete the current word.             - The first Tab press fills in the common part of all completions and shows all the completions. (In the menu)    
    - Any following tab press cycles through all the possi ble completions
    """

    text = session.prompt("List famous  animals: ")
    quo.echo(f"You said: {text}")


if __name__ == "__main__":
    main()