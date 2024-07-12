import typer

from cli import m2m

app = typer.Typer()

app.add_typer(
    m2m.app, name="m2m", help="manage auth0 m2m service account credentials"
)

if __name__ == "__main__":
    app()
