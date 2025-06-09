from markdownblock import BlockType

def block_type_to_tag(blocktypelist):
    dict={
        BlockType.HEADING:{
            1:"h1",
            2:"h2",
            3:"h3",
            4:"h4",
            5:"h5",
            6:"h6"
        },
        BlockType.QUOTE:"blockquote",
        BlockType.UNORDERED_LIST:"ul",
        BlockType.ORDERED_LIST:"ol",
        BlockType.CODE:"pre",
        BlockType.PARAGRAPH:"p"

    }
    if blocktypelist[0]==BlockType.HEADING:
        return dict[blocktypelist[0]][blocktypelist[1]]
    else:
        return dict[blocktypelist[0]]