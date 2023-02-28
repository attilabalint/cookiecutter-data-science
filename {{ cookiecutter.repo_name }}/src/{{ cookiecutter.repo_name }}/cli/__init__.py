import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.callback()
def cli():
    """
    Main entrypoint for this dummy program
    """


def main():
    app()
