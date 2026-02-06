# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    if not text:
        return "Please input characters."

    statement = []
    for i in range(repetitions, 0, -1):
        statement.append(text[-i:])
    statement.append(".")

    return "\n".join(statement)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
