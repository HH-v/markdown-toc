def write_toc_file(toc, output_path):
    with open(output_path, "w") as f:
        f.write(toc)
        f.write("\n")

def append_to_file(content, output_path):
    with open(output_path, "a") as f:
        f.write(content)
