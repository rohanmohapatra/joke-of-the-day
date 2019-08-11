import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="joke-for-the-day",
    version="0.0.1",
    author="Rohan Mohapatra",
    author_email="rohannmohapatra@gmail.com",
    description="Joke of the Day Package",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)