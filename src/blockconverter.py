from markdownblock import BlockType

def block_to_block_type(block):
    heading_id=["# ","## ","### ","#### ","##### ","###### "]
    lines=block.splitlines()
       
    if any(block.startswith(h) for h in heading_id):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{idx+1}. ") for idx,line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH