from setuptools import setup
from encurtanet.config import BASE_URL

with open("README.md", "r") as readme_bf:
    readme_content = readme_bf.read()

setup(
    name="encurtanet",
    version="0.0.0.0.1",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="encurtanet wrapper api",
    description=f"Wrappper for {BASE_URL}",
    packages=[
        "encurtanet",
    ],
    install_requires=["requests", "pydantic"],
)