import data_struct
import numpy as np
import math

def construct_node(last_node, data, depth, k, note):
    '''迭代生成节点, last_node为上一节点， data为数据， depth记录当前深度，k为数据的维度， note记录当前为上一节点的
    左节点还是右节点'''
    eva_fea = depth % k
    temp_data = data[:, eva_fea]
    if len(temp_data) > 0:
        arg_temp = np.argsort(temp_data)
        temp_length = len(arg_temp)
        temp_poi = math.floor(temp_length/2)
        temp_Node = data_struct.KDD_Node(data[arg_temp[temp_poi], :])
        if note == 0:
            last_node.left_downNode = temp_Node
            temp_Node.note_node(note)
        else:
            last_node.right_downNode = temp_Node
            temp_Node.note_node(note)
        temp_Node.upNode = last_node
        if temp_poi != 0:
            arg_temp1 = arg_temp[0: temp_poi]
            arg_temp2 = arg_temp[temp_poi+1:]
            data1 = data[arg_temp1]
            data2 = data[arg_temp2]
            construct_node(temp_Node, data1, depth + 1, k, 0)
            construct_node(temp_Node, data2, depth + 1, k, 1)


def construct_tree(input_data, k):
    '''构造根节点，并且利用
    construct_node构造平衡kd树'''
    root_fea = 1 % k
    root_temp_data = input_data[:, root_fea]
    if len(root_temp_data) > 0:
        arg_temp = np.argsort(root_temp_data)
        temp_length = len(arg_temp)
        temp_poi = math.floor(temp_length / 2)
        root_Node = data_struct.KDD_Node(input_data[arg_temp[temp_poi], :])
        if temp_poi != 0:
            arg_temp1 = arg_temp[0: temp_poi]
            arg_temp2 = arg_temp[temp_poi + 1:]
            data1 = input_data[arg_temp1]
            data2 = input_data[arg_temp2]
            construct_node(root_Node, data1, 2, k, 0)
            construct_node(root_Node, data2, 2, k, 1)
    return root_Node

def main( ):
    origin_data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
    node = construct_tree(origin_data, 2)
    print('bupt')

if __name__ == '__main__':
    main( )
