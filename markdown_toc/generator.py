from .parser import parse_headings

def generate_toc(content, max_depth=3, indent="  ", numbered=False):
    headings = parse_headings(content)
    lines = []
    
    for i, h in enumerate(headings):
        if h.level > max_depth:
            continue
        prefix = indent * (h.level - 1)
        if numbered:
            lines.append(f"{prefix}{i + 1}. [{h.text}](#{h.anchor})")
        else:
            lines.append(f"{prefix}- [{h.text}](#{h.anchor})")
    
    return "\n".join(lines)

def insert_toc(content, toc, marker="<!-- toc -->"):
    if marker in content:
        return content.replace(marker, toc)
    return f"{marker}\n{toc}\n\n{content}"
