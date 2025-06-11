def extract_title(markdown):
    lines=markdown.splitlines()
    heading="default"
    for line in lines:
        new_line=line.strip()
        if new_line.startswith("# "):
            heading=line.lstrip("# ")
    if heading == "default":
        raise Exception("no L1 header present")
    return heading