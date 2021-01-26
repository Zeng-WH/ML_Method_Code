class KDD_Node:
    '''KD树的节点'''

    def __init__(self, value):
        self.value = value # 存储当前节点的值
        self.upNode = None
        self.left_downNode = None
        self.right_downNode = None
        self.note = None # 用来记录该节点是上一节点的左节点还是有节点

    def note_node(self, note):
        self.note = note