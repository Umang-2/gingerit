import setuptools

setuptools.setup(
    name="gingerit",
    version="1.0",
    author="prithiviraj damodaran",
    author_email="",
    description="gingerit",
    long_description="A framework for detecting, highlighting and correcting grammatical errors on natural language text",
    url="https://github.com/PrithivirajDamodaran/Gramformer.git",
    packages=setuptools.find_packages(),
    install_requires=['cloudscraper'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)
