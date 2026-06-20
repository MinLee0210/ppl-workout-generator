import os
from setuptools import setup, find_packages

# Read the contents of README.md file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ppl-workout-generator",
    version="0.1.0",
    author="Workout Generator Contributors",
    author_email="contributors@example.com",
    description="Intelligent, sports-science based Push-Pull-Legs (PPL) workout generator library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinLee0210/ppl-workout-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    extras_require={
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ppl-workout=ppl_workout_generator.__main__:main",
        ],
    },
)
