import re

HEADING_PATTERN = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)

class Heading:
    def __init__(self, level, text, line, anchor=None):
        self.level = level
        self.text = text.strip()
        self.line = line
        self.anchor = anchor or self._make_anchor()

    def _make_anchor(self):
        text = self.text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'\s+', '-', text)
        return text

def parse_headings(content):
    headings = []
    for match in HEADING_PATTERN.finditer(content):
        level = len(match.group(1))
        text = match.group(2)
        line = match.start()
        headings.append(Heading(level, text, line))
    return headings
