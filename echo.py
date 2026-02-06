# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    if not text:
        print("Please input characters.")
    else:
        for i in range(3, 0, -1):
            print(text[-i:])
        print(".")


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    echo(text)
