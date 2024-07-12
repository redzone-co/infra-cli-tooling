# CLI tool to assist with M2M Accounts

## Dependencies

* python >= 3.10
* poetry >= 1.8.2


## Quickstart

1. Create an Machine To Machine (M2M) application in the Auth0 Tenant
2. Generate a private and public key pair in PEM format (see below)**
3. Configure the M2M application to authenticate using Private Key JWT by uploading the public PEM
4. Verify all is configured using this tool as shown below:

```
poetry install
poetry run cli --help
poetry run cli m2m access-token [AUTH0 APP ID] /path/to/private/pem/file.pem 
# outputs the access token

abcdefg...blah..blah
```

5. To verify that the access token returned by Auth0 is valid, you can check it in jwt.io. It should look like this:

Header:

```
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "FChMh5aiSbbpUSQfa03b1"
}
```

Payload:

```
{
  "iss": "https://sandbox-redzone-co.us.auth0.com/",
  "sub": "OOZH6s5sgOORoVKBMNRu0xRd4I3dl5T7@clients",
  "aud": "https://redzone-co/api/v1/resource/server",
  "iat": 1720762274,
  "exp": 1723354274,
  "gty": "client-credentials",
  "azp": "OOZH6s5sgOORoVKBMNRu0xRd4I3dl5T7"
}

```

6. To verify that your M2M application has been configured in the `backend-auth-microservice` with the appropriate permissions, navigate to the `/docs` page of the service:

https://auth.sandbox.redzone.zone/docs#/Authorization/authorized_api_v1__org_key__authorized_post

1. Authorize the webpage with the access token that was printed out (above)
2. Hit the `/api/v1/{org_key}/authorized` endpoint to see if you have the permissions you need/expect. Because `string` is not a valid permission, the API Endpoint will return all the permissions that are granted to this account.
3. You can replace the default value with the permission that you are curious about:

So replace:

```
[
  "string"
]
```

with some permission that you are interested in, e.g.:

```
[
    "rz:foo:bar:baz"
]



## Documentation

This tool was built using typer, so it has fairly robust help documentation.

```
$ poetry run cli --help
                                                                                                                                                                                                                                                               
 Usage: cli [OPTIONS] COMMAND [ARGS]...                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                                                                                     │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                                                                                              │
│ --help                        Show this message and exit.                                                                                                                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ m2m   manage auth0 m2m service account credentials                                                                                                                                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


```
$ poetry run cli m2m --help 
                                                                                                                                                                                                                                                               
 Usage: cli m2m [OPTIONS] COMMAND [ARGS]...                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                               
 manage auth0 m2m service account credentials                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ access-token   log in with private key                                                                                                                                                                                                                      │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


```
$ poetry run cli m2m access-token --help 
                                                                                                                                                                                                                                                               
 Usage: cli m2m access-token [OPTIONS] CLIENT_ID PATH [DOMAIN] [URL]                                                                                                                                                                                           
                                                                                                                                                                                                                                                               
 log in with private key                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                               
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    client_id      TEXT      Auth0 M2M Application Client ID [default: None] [required]                                                                                                                                                                    │
│ *    path           FILE      Path to Private PEM file [default: None] [required]                                                                                                                                                                           │
│      domain         [DOMAIN]  Auth0 Domain [default: sandbox-redzone-co.us.auth0.com]                                                                                                                                                                       │
│      url            [URL]     Auth0 Tenant API URL [default: https://redzone-co/api/v1/resource/server]                                                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```


## How To Create PEM files

Here's a bash function that I use to generate private and public pem keys...

```
gen-key-pair(){
 TIER=$1
 SVC=$2
 openssl genrsa -out $TIER-$SVC-msvc.pem 4096
 openssl rsa -in $TIER-$SVC-msvc.pem -outform PEM -pubout -out $TIER-$SVC-msvc.pem.pub
 ls -lsa
 cat $TIER-$SVC-msvc.pem
 cat $TIER-$SVC-msvc.pem.pub
}
```
