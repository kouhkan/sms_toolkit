from setuptools import setup, find_packages

setup(
    name="sms_toolkit",
    version="0.1.0",
    author="amirkouhkan1",
    description="A Python package for sending SMS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kouhkan/sms_toolkit",
    packages=find_packages(where="sms_toolkit"),
    package_dir={"": "sms_toolkit"},
    install_requires=[
        "httpx>=0.28.1",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
