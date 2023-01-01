from pydantic import validate_arguments
from types import NoneType
import requests
import json

BASE_URL = "https://encurta.net/api"

INTERSTITIALS_ADS = 1
NO_ADS = 0

class EncurtaNetError(Exception):
    @validate_arguments
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"EncurtaNetError({self.message})"

class EncurtaNetResponse:
    @validate_arguments
    def __init__(
        self,
        response: str,
        is_text_format: bool,
    ) -> None:
        self.response = response
        self.is_text_format = is_text_format

        self.json_response: dict = json.loads(self.response)

    def get_raw_data(self) -> str | dict:
        if self.is_text_format:
            return self.response

        return self.json_response

    def get_shortened_url(self) -> str | None:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        return self.json_response["shortenedUrl"]

    def get_status(self) -> str | None:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        return self.json_response["status"]

    def get_message(self) -> str | None:
        if self.is_text_format:
            raise EncurtaNetError("It is not possible to get this data because you passed 'is_text_format' as True")

        if "message" in self.json_response.keys():
            return self.json_response["message"]

class EncurtaNet:
    @validate_arguments
    def __init__(
        self,
        api_token: str,
    ) -> None:
        self.__api_token = api_token

    @validate_arguments
    def shorten(
        self,
        url: str,
        alias: str | NoneType = None,
        is_text_format: bool = False,
        ads_type: int | NoneType = None,
    ) -> EncurtaNetResponse:
        params = {
            "api": self.__api_token,
            "url": url,
        }

        if alias:
            params["alias"] = alias

        if is_text_format:
            params["format"] = "text"

        if ads_type != None:
            if ads_type == INTERSTITIALS_ADS:
                params["type"] = INTERSTITIALS_ADS

            elif ads_type == NO_ADS:
                params["type"] = NO_ADS

            else:
                raise EncurtaNetError(f"{ads_type} is not valid ads type")

        response = requests.get(BASE_URL, params)
        json_response = response.json()

        if response.status_code != 200:
            raise EncurtaNetError(f"[Request Error] Status code: {response.status_code}")

        if response.text == "" or json_response["status"] == "error":
            message = json_response["message"]

            if type(message) == list:
                message = "".join(message)

            raise EncurtaNetError(message)

        return EncurtaNetResponse(response.text, is_text_format)