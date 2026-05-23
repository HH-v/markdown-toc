from .generator import generate_toc, insert_toc
from .parser import parse_headings
from .writer import write_toc_file
from .cli import main

__version__ = "0.2.0"
__all__ = ["generate_toc", "insert_toc", "parse_headings", "write_toc_file", "main"]
