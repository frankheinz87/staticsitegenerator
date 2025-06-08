def markdown_to_blocks(markdown):
    blocks=markdown.split("\n")
    result=[]
    int_result=[]
    for block in blocks:
        new_block=block.strip(" ")
        
        if new_block=="" and int_result!=[]:
            result.append("\n".join(int_result))
            int_result=[]
            continue 
        elif new_block!="":
            int_result.append(new_block)
               
    if int_result!=[]:
        result.append("\n".join(int_result))
        
    return result
            