from pathlib import Path


def load_prompt(
    prompt_name: str
):

    path = (
        Path("prompts/v1")
        / prompt_name
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()