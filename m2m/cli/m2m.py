from pathlib import Path

import typer
from typing_extensions import Annotated
from auth0.authentication import GetToken

app = typer.Typer()

@app.command(help="log in with private key")
def access_token(
        client_id: Annotated[str, typer.Argument(help="Auth0 M2M Application Client ID")],
        path: Annotated[
            Path,
            typer.Argument(
                exists=True,
                file_okay=True,
                dir_okay=False,
                writable=False,
                readable=True,
                resolve_path=True,
                help="Path to Private PEM file"
            ),
        ],
        domain: Annotated[str, typer.Argument(help="Auth0 Domain")]="sandbox-redzone-co.us.auth0.com",
        url: Annotated[str, typer.Argument(help="Auth0 Tenant API URL")]="https://redzone-co/api/v1/resource/server",
        ) -> None:
    print("Getting access token...")
    token = GetToken(
        domain=domain,
        client_id=client_id,
        client_assertion_signing_key=open(path, "r").read(),
    ).client_credentials(audience=url)
    print(token["access_token"])
