from pydantic import validate_call
from typing import Optional
import requests
import json

from .ads_types import AdsTypes

class EncurtaNetError(Exception):
    @validate_call
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"EncurtaNetError({self.message})"

class EncurtaNetResponse:
    @validate_call
    def __init__(
        self,
        response: str,
        is_text_format: bool,
    ) -> None:
        self.response = response
        self.is_text_format = is_text_format

        self.json_response: dict = json.loads(self.response)

    @property
    def raw_data(self) -> str | dict:
        if self.is_text_format:
            return self.response

        return self.json_response

    @property
    def shortened_url(self) -> str:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        return self.json_response["shortenedUrl"]

    @property
    def status(self) -> str:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        return self.json_response["status"]

    @property
    def message(self) -> str:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        if "message" in self.json_response.keys():
            return self.json_response["message"]

class EncurtaNet:
    @validate_call
    def __init__(
        self,
        api_token: str,
    ) -> None:
        self._base_url = "https://encurta.net/api"
        self._api_token = api_token

    @validate_call
    def shorten(
        self,
        url: str,
        alias: Optional[str] = None,
        is_text_format: bool = False,
        ads_type: Optional[int] = None,
    ) -> EncurtaNetResponse:
        params = {
            "api": self._api_token,
            "url": url,
        }

        if alias:
            params["alias"] = alias

        if is_text_format:
            params["format"] = "text"

        if ads_type != None:
            if ads_type == AdsTypes.InterstitialAds:
                params["type"] = AdsTypes.InterstitialAds

            elif ads_type == AdsTypes.NoAds:
                params["type"] = AdsTypes.NoAds

            else:
                raise EncurtaNetError(f"{ads_type} is not valid ads type")

        response = requests.get(self._base_url, params)
        json_response = response.json()

        if response.status_code != 200:
            raise EncurtaNetError(f"[Request Error] Status code: {response.status_code}")

        if response.text == "" or json_response["status"] == "error":
            message = json_response["message"]

            if type(message) == list:
                message = "".join(message)

            raise EncurtaNetError(message)

        return EncurtaNetResponse(response.text, is_text_format)