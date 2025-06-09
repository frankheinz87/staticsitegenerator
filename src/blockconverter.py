from markdownblock import BlockType

def block_to_block_type(block):
    heading_id=["# ","## ","### ","#### ","##### ","###### "]
    lines=block.splitlines()
    num_lines=len(lines)
    quote_flag=None
    unordered_list_flag=None
    ordered_list_flag=None

    for line in lines:
        if line[0]==">" and (quote_flag==None or quote_flag==True):
            quote_flag=True
        else:
            quote_flag=False
    
    for line in lines:
        if line[0:2]=="- " and (unordered_list_flag==None or unordered_list_flag==True):
            unordered_list_flag=True
        else:
            unordered_list_flag=False

    for i in range(0,num_lines):
        if lines[i][0:3]==f"{i+1}. " and (ordered_list_flag==None or ordered_list_flag==True):
            ordered_list_flag=True
        else:
            ordered_list_flag=False
       
    if (block[0:2] in heading_id) or (block[0:3] in heading_id) or (block[0:4] in heading_id) or (block[0:5] in heading_id) or (block[0:6] in heading_id) or (block[0:7] in heading_id):
        return BlockType.HEADING
    elif block[0:3]=="```" and block[-3:]=="```":
        return BlockType.CODE
    elif quote_flag==True:
        return BlockType.QUOTE
    elif unordered_list_flag==True:
        return BlockType.UNORDERED_LIST
    elif ordered_list_flag==True:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH