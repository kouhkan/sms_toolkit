from typing import List, Optional
import httpx


class KavenegarSMS:
    """
    A class to send SMS using the Kavenegar API's verification service.

    Attributes:
        api_key (str): The API key for authenticating with the Kavenegar service.

    Methods:
        pattern_sms(receptor: str, tokens: List[str], template: str, type: Optional[str] = "sms"):
            Sends a pattern-based SMS using the Kavenegar API.

    Example:
        >>> sms = KavenegarSMS(api_key="your_api_key")
        >>> response = await sms.pattern_sms(
        ...     receptor="09123456789",
        ...     tokens=["12345", "John Doe"],
        ...     template="welcome_template"
        ... )
        >>> print(response)
    """

    def __init__(self, api_key: str):
        """
        Initialize the KavenegarSMS object with an API key.

        Args:
            api_key (str): The API key for authenticating with the Kavenegar service.
        """
        self.api_key = api_key

    async def pattern_sms(
        self,
        receptor: str,
        tokens: List[str],
        template: str,
        type: Optional[str] = "sms",
    ):
        """
        Send a pattern-based SMS using the Kavenegar API.

        Args:
            receptor (str): The recipient's phone number.
            tokens (List[str]): A list of token values to replace placeholders in the SMS template.
            template (str): The template ID or name configured in Kavenegar.
            type (Optional[str], optional): The type of message (e.g., "sms"). Defaults to "sms".

        Returns:
            dict: The response from the Kavenegar API.

        Example:
            >>> sms = KavenegarSMS(api_key="your_api_key")
            >>> response = await sms.pattern_sms(
            ...     receptor="09123456789",
            ...     tokens=["12345", "John Doe"],
            ...     template="welcome_template"
            ... )
            >>> print(response)
        """
        url = f"https://api.kavenegar.com/v1/{self.api_key}/verify/lookup.json"
        payload = {
            "receptor": receptor,
            "template": template,
            "type": type,
        }
        tokens = {f'token{"" if k == 0 else k + 1}': v for k, v in enumerate(tokens)}

        payload.update(tokens)

        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, json=payload, timeout=30)

        return response.json()
