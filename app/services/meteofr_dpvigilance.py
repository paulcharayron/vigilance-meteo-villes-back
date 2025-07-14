from datetime import datetime
import json
import httpx
import jwt

from fastapi import status

from ..core.config import settings
from ..exceptions.meteofr_dpvigilance import (
    MeteoFrDPVigilance404Exception,
    MeteoFrDPVigilance500Exception,
)


class MeteoFrDPVigilanceService:

    def __init__(self, httpx_client, oauth_token):
        self.httpx_client = httpx_client
        self.oauth_access_token = oauth_token

    def generate_oauth_token(self):
        headers = {
            "accept": "application/json",
            "authorization": f"Basic {settings.METEOFR_DPVIG_APP_ID}",
        }
        form_encoded_data = {
            "grant_type": "client_credentials",
        }

        try:
            # Request an OAuth access token
            res = self.httpx_client.post(
                settings.METEOFR_GEN_OAUTH_TOKEN_URL,
                headers=headers,
                data=form_encoded_data,
            ).raise_for_status()

            self.oauth_access_token = json.loads(res.text)["access_token"]
            print(f"obtained access_token: {self.oauth_access_token}")

        except httpx.RequestError as exc:
            raise MeteoFrDPVigilance500Exception(
                "A RequestError occurred when attempting to generate an OAuth \
access token from Meteo France API."
            )
        except httpx.HTTPStatusError as exc:
            raise MeteoFrDPVigilance500Exception(
                f"An HTTPStatusError with code {exc.response.status_code} \
occurred when attempting to generate an OAuth access token from Meteo France API."
            )

    def is_oauth_access_token_expired(self) -> bool:
        # Decode OAuth access token
        try:
            decoded_token = jwt.decode(
                self.oauth_access_token,
                options={"verify_signature": False},
            )
        except jwt.exceptions.DecodeError as exc:
            raise MeteoFrDPVigilance500Exception(
                "An exception occurred while decoding the current Meteo France \
OAuth access token."
            )

        return datetime.fromtimestamp(decoded_token["exp"]) < datetime.now()

    def get_dpvigilance_texts(self):
        if not self.oauth_access_token or self.is_oauth_access_token_expired():
            self.generate_oauth_token()

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.oauth_access_token}",
        }

        try:
            # Get textes DPVigilance
            res = self.httpx_client.get(
                f"{settings.METEOFR_DPVIG_API_BASE_URL}/textesvigilance/encours",
                headers=headers,
            ).raise_for_status()
            payload = json.loads(res.text)

            return payload

        except httpx.RequestError as exc:
            raise MeteoFrDPVigilance500Exception(
                "A RequestError occurred when attempting to get Meteo France \
DPVigilance texts."
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == status.HTTP_404_NOT_FOUND:
                raise MeteoFrDPVigilance404Exception(
                    f"An HTTPStatusError with code {exc.response.status_code} \
occurred when attempting to get Meteo France DPVigilance texts."
                )
            else:
                raise MeteoFrDPVigilance500Exception(
                    f"An HTTPStatusError with code {exc.response.status_code} \
occurred when attempting to get Meteo France DPVigilance texts."
                )


meteofr_dpvigilance_service = MeteoFrDPVigilanceService(
    httpx.Client(verify=False),
    "",
)
