# markdown-toc

Generate a table of contents for markdown documents.

## Features

- Parses headings h1–h6
- Configurable depth limit
- Numbered or bullet lists
- In-place insertion or standalone output
- Zero dependencies (Python stdlib only)

## Quickstart

```bash
# Print TOC to stdout
python -m markdown_toc README.md

# Insert TOC into file
python -m markdown_toc README.md --inplace

# Write to separate file
python -m markdown_toc README.md -o TOC.md
```

## Install

```bash
pip install markdown-toc
```

## Options

| Flag | Description |
|------|-------------|
| `-o, --output` | Write TOC to file |
| `-d, --depth` | Max heading depth (default: 3) |
| `-n, --numbered` | Use numbered list |
| `--inplace` | Insert TOC into source file |
