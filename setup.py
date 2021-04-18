import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bhavpr", # Replace with your own username
    version="1.0.0",
    author="Jeffry Copps Robert Jose",
    author_email="code.jeffry@gmail.com",
    description="A simple parser to consume PR files available with NSE.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcopps/BhavCopyPRParser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=required
)
