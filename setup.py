from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wizardsdata",
    version="0.1.0",
    author="Pere Martra",
    author_email="peremartral@uadla.com",
    description="A library for generating conversation datasets using language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peremartra/WizardSData",
    # Explicitly specify packages instead of using find_packages()
    packages=["wizardsdata"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 license",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai>=1.0.0",
        "jinja2>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "wizardsdata=wizardsdata:main",
        ],
    },
)