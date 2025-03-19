from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wizardsdata",
    version="0.1.0",
    author="Pere Martra",
    author_email="peremartra@uadla.com",
    description="library for generating conversation datasets using language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peremartra/WizardSData",
    project_urls={
        "Documentation": "https://peremartra.github.io/WizardSData/",
        "Bug Tracker": "https://github.com/peremartra/WizardSData/issues",
    },
    # Explicitly specify packages instead of using find_packages()
    packages=["wizardsdata"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
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