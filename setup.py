from setuptools import setup, find_packages


# Function to read the requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


setup(
    name="TezzCrawler",
    version="0.2.0",
    author="Japkeerat Singh (TezzLabs)",
    author_email="japkeerat@tezzlabs.com",
    description="A web crawler that converts web pages to markdown and prepares them for LLM consumption",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TezzLabs/TezzCrawler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "requests==2.32.3",
        "typer==0.13.0",
        "beautifulsoup4==4.12.3",
        "markdownify==0.13.1",
        "lxml==5.3.0",
    ],
    entry_points={
        "console_scripts": [
            "tezzcrawler=tezzcrawler.main:app",
        ],
    },
    include_package_data=True,
)
