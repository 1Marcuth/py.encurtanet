from setuptools import setup

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name = "encurtanet",
    version = "0.1.0",
    license = "MIT License",
    author = "Marcuth",
    long_description = readme_content,
    long_description_content_type = "text/markdown",
    author_email = "marcuth2006@gmail.com",
    keywords = "encurtanet wrapper api",
    description = "",
    packages = ["encurtanet"],
    install_requires = ["requests", "pydantic"],
)