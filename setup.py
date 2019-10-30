from setuptools import (
    find_packages,
    setup
)

setup(
    name="python-coinone",
    version="0.1.0",
    description="Coinone REST-API Client",
    url="https://github.com/jaehong-park-net/python-coinone",

    author="Jaehong Park",
    author_email="jaehong.park.net@gmail.com",

    packages=find_packages(),

    install_requires=[
        "green",
        "requests"
    ]
)
