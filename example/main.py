import asyncio

from sms_toolkit import KavenegarSMS


async def main():
    api_key = "your_api_key"
    sms = KavenegarSMS(api_key=api_key)

    response = await sms.pattern_sms(
        receptor="09123456789",
        tokens=["12345", "John Doe"],
        template="welcome_template",
    )
    print(response)


asyncio.run(main())
