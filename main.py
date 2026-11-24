#!/usr/bin/env python3
"""Print the funniest toaster error message (no trailing newline)."""

_PARTS = (
    "ERROR: Your bread has filed for divorce. ",
    "Reason cited: 'irreconcilable browning differences.'",
)


def build_message() -> str:
    return "".join(_PARTS)


def main() -> None:
    print(build_message(), end="")


if __name__ == "__main__":
    main()
