from google_auth_oauthlib.flow import Flow
from flask import session
from decouple import config
import os
import pathlib

client_secrets_file = os.path.join(pathlib.Path(__file__).parent.parent.parent, "client_secret.json")


flow = Flow.from_client_secrets_file(
   client_secrets_file=client_secrets_file,
   scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
   redirect_uri="{}/auth/oauth".format(config("BACKEND_URL"))
)


class AuthService:
    @classmethod
    def login(cls):
        authorization_url, state = flow.authorization_url()
        session["state"] = state
        return authorization_url

    @classmethod
    def signup(cls, user):
        print(user)

    @classmethod
    def oauth(cls, code):
        print("code")
        print(code)
