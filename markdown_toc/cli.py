"""Command-line interface for markdown-toc."""

import sys
import argparse
from .generator import generate_toc, insert_toc
from .writer import write_toc_file


def main():
    parser = argparse.ArgumentParser(
        description="Generate table of contents for markdown files"
    )
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("-d", "--depth", type=int, default=3,
                        help="Maximum heading depth (default: 3)")
    parser.add_argument("-n", "--numbered", action="store_true",
                        help="Use numbered list instead of bullets")
    parser.add_argument("--inplace", action="store_true",
                        help="Insert TOC into input file")
    
    args = parser.parse_args()
    
    with open(args.input, "r") as f:
        content = f.read()
    
    toc = generate_toc(content, max_depth=args.depth, numbered=args.numbered)
    
    if args.inplace:
        new_content = insert_toc(content, toc)
        with open(args.input, "w") as f:
            f.write(new_content)
        print(f"TOC inserted into {args.input}")
    elif args.output:
        write_toc_file(toc, args.output)
        print(f"TOC written to {args.output}")
    else:
        print(toc)


if __name__ == "__main__":
    main()
