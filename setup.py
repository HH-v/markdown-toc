from setuptools import setup, find_packages

setup(
    name="markdown-toc",
    version="0.2.0",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "markdown-toc=markdown_toc.cli:main",
        ],
    },
)
