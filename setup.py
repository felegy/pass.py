#!/usr/bin/env python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pass.py",
    version="0.0.1",
    author="felegy",
    author_email="felegy@gmail.com",
    description="Minimal Pass implementation in Python based on keys in ssh-agent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felegy/pass.py",
    project_urls={
        "Bug Tracker": "https://github.com/felegy/pass.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
