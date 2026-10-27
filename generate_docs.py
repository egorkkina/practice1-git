from pathlib import Path
import html
import inspect

import utils


def generate_documentation():
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    functions = [
        (name, function)
        for name, function in inspect.getmembers(utils, inspect.isfunction)
        if function.__module__ == utils.__name__
    ]

    sections = []

    for name, function in functions:
        signature = html.escape(str(inspect.signature(function)))
        description = html.escape(
            inspect.getdoc(function) or "Описание отсутствует"
        )

        sections.append(
            f"<h2>{html.escape(name)}{signature}</h2>"
            f"<p>{description}</p>"
        )

    content = f"""<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Документация проекта</title>
            </head>
            <body>
                <h1>Документация проекта practice1-git</h1>
                <p>Версия: 1.0.0</p>
                {''.join(sections)}
            </body>
            </html>
        """

    (docs_dir / "index.html").write_text(
        content, encoding="utf-8"
    )

    print("Документация успешно создана: docs/index.html")


if __name__ == "__main__":
    generate_documentation()