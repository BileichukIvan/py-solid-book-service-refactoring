from app.book import Book
from app.printers import ConsolePrinter, ReverseConsolePrinter
from app.interfaces import ConsoleDisplay, ReverseConsoleDisplay
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "serialize": {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        },
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseConsoleDisplay(),
        },
        "print": {
            "console": ConsolePrinter(),
            "reverse": ReverseConsolePrinter(),
        }
    }

    for cmd, method_type in commands:
        if cmd == "display":
            actions[cmd][method_type].display(book)
        elif cmd == "print":
            actions[cmd][method_type].print(book)
        elif cmd == "serialize":
            return actions[cmd][method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
