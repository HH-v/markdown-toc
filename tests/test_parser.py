import pytest
from markdown_toc.parser import parse_headings

SAMPLE = '''# Title
Some text
## Section 1
More text
### Subsection 1.1
#### Deep 1.1.1
## Section 2
'''

def test_parse_headings_count():
    headings = parse_headings(SAMPLE)
    assert len(headings) == 5

def test_parse_headings_levels():
    headings = parse_headings(SAMPLE)
    assert [h.level for h in headings] == [1, 2, 3, 4, 2]

def test_parse_headings_text():
    headings = parse_headings(SAMPLE)
    assert headings[0].text == "Title"
    assert headings[1].text == "Section 1"
