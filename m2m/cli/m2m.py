from pathlib import Path

import typer
from typing_extensions import Annotated
from auth0.authentication import GetToken

app = typer.Typer()

"""
# bash function that I use to generate private and public pem keys...

gen-key-pair(){
 TIER=$1
 SVC=$2
 openssl genrsa -out $TIER-$SVC-msvc.pem 4096
 openssl rsa -in $TIER-$SVC-msvc.pem -outform PEM -pubout -out $TIER-$SVC-msvc.pem.pub
 ls -lsa
 cat $TIER-$SVC-msvc.pem
 cat $TIER-$SVC-msvc.pem.pub
}
"""

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
