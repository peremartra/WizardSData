from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wizardsdata",
    version="0.1.0",
    author="Pere Martra",
<<<<<<< HEAD
    author_email="peremartra@uadla.com",
    description="library for generating conversation datasets using language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peremartra/WizardSData",
    project_urls={
        "Documentation": "https://peremartra.github.io/WizardSData/",
        "Bug Tracker": "https://github.com/peremartra/WizardSData/issues",
    },
=======
    author_email="peremartral@uadla.com",
    description="A library for generating conversation datasets using language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peremartra/WizardSData",
>>>>>>> ee0323e21e5d05ca5c2787a28d907693de1640e6
    # Explicitly specify packages instead of using find_packages()
    packages=["wizardsdata"],
    classifiers=[
        "Programming Language :: Python :: 3",
<<<<<<< HEAD
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
=======
        "License :: OSI Approved :: Apache-2.0 license",
        "Operating System :: OS Independent",
>>>>>>> ee0323e21e5d05ca5c2787a28d907693de1640e6
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