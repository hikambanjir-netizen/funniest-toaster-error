#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Prints exactly one line: the toaster's error message, with no
trailing newline, and exits 0.
"""

MESSAGE = "ERROR: Your bread has filed for divorce. Reason cited: 'irreconcilable browning differences.'"


def main() -> None:
    print(MESSAGE, end="")


if __name__ == "__main__":
    main()
