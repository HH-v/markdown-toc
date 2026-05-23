from .parser import parse_headings

def generate_toc(content, max_depth=3, indent="  "):
    headings = parse_headings(content)
    lines = []
    
    for h in headings:
        if h.level > max_depth:
            continue
        prefix = indent * (h.level - 1)
        lines.append(f"{prefix}- [{h.text}](#{h.anchor})")
    
    return "\n".join(lines)
