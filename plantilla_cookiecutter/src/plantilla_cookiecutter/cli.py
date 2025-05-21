"""Console script for plantilla_cookiecutter."""
import plantilla_cookiecutter

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for plantilla_cookiecutter."""
    console.print("Replace this message by putting your code into "
               "plantilla_cookiecutter.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
