#!/usr/bin/env python3


def duplicate(plaintext: str) -> str:
    """
    Duplicate chars in 'plaintext':
    duplicate('hello') -> 'hheelloo'
    """
    # TODO
    pass


def intersection(a: str, b: str) -> str:
    """
    Return intersectioned string
    intersection('zirafa', 'karafa') -> 'rafa'
    """
    # TODO
    pass


def caesar(plaintext: str, move: int) -> str:
    """
    Move 'plaintext' by 'move' characters. 'move' could be negative
    caesar('hello', 1) -> 'ifmmp'
    """
    for i in plaintext:
            print(ord(char(i)+1))


def main() -> None:
    print("1.duplicate\n2.intersection\n3.caesar")
    match int(input()):
        case 1:
            duplicate(input("str:"))
        case 2:
            intersection(input("a.str:"),input("b.str:"))
        case 3:
                caesar(input("str:"),input("move:"))


if __name__ == '__main__':
    main()
