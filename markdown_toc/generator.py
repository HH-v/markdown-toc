from .parser import parse_headings

def generate_toc(content, max_depth=3, indent="  ", numbered=False, include_top=False):
    headings = parse_headings(content)
    lines = []
    
    if include_top:
        lines.append("# Table of Contents\n")
    
    for i, h in enumerate(headings):
        if h.level > max_depth:
            continue
        prefix = indent * (h.level - 1)
        bullet = f"{i + 1}." if numbered else "-"
        lines.append(f"{prefix}{bullet} [{h.text}](#{h.anchor})")
    
    return "\n".join(lines)

def insert_toc(content, toc, marker="<!-- toc -->"):
    if marker in content:
        return content.replace(marker, toc)
    out = f"{marker}\n{toc}\n\n"
    # Insert after first heading if it exists
    first_heading = content.find("\n# ")
    if first_heading != -1:
        end_of_line = content.find("\n", first_heading + 1)
        return content[:end_of_line + 1] + "\n" + out + "\n" + content[end_of_line + 1:]
    return out + content
