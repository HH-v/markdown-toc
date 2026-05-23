import pytest
from markdown_toc.generator import generate_toc

SAMPLE = '''# Intro
## Setup
### Dependencies
## Usage
'''

def test_generate_toc_default():
    toc = generate_toc(SAMPLE)
    assert "- [Intro]" in toc
    assert "  - [Setup]" in toc
    assert "    - [Dependencies]" in toc

def test_generate_toc_max_depth():
    toc = generate_toc(SAMPLE, max_depth=2)
    assert "- [Intro]" in toc
    assert "  - [Setup]" in toc
    assert "Dependencies" not in toc

def test_generate_toc_numbered():
    toc = generate_toc(SAMPLE, numbered=True)
    assert "1. [Intro]" in toc
