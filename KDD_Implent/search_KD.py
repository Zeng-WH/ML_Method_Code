'''用kd树进行最近邻搜索'''
import numpy as np
import construct_balance_KD_tree

def search_Node(Node, input_example, depth, k):
    '''初始化寻找叶子节点，作为当前最近点'''
    eva_fea = depth % k
    temp_value = input_example[eva_fea]
    if Node.left_downNode == None and Node.right_downNode == None:
        most_near_Node = Node
    else:
        if temp_value < Node.value[eva_fea]:
            if Node.left_downNode != None:
                most_near_Node = search_Node(Node.left_downNode, input_example, depth+1, k)
            else:
                most_near_Node = Node
        else:
            if Node.right_downNode != None:
                most_near_Node = search_Node(Node.right_downNode, input_example, depth+1, k)
            else:
                most_near_Node = Node
    return most_near_Node

def calculate_distance(a, b, p):
    '''按照自定义函数计算距离'''
    temp1 = pow(a-b, p)
    temp2 = np.abs(temp1)
    temp3 = np.sum(temp2)
    temp4 = pow(temp3, 1/p)
    return temp4



def search_tree(root_Node, input_example, k, p):
    '''从根节点开始，初始化叶子节点并进行寻找，p为定义的计算距离的参数'''
    most_near_Node = search_Node(root_Node, input_example, 1, k)
    temp_Node = most_near_Node.upNode
    temp_Node1 = most_near_Node
    if calculate_distance(temp_Node.value, input_example, p) < calculate_distance(most_near_Node.value, input_example, p):
        most_near_Node = temp_Node
    if temp_Node1.note == 0:
        if temp_Node.right_downNode != None:
            temp_Node2 = temp_Node.right_downNode
            if calculate_distance(temp_Node2.value, input_example, p) < calculate_distance(most_near_Node.value, input_example, p):
                most_near_Node = temp_Node2
    else:
        if temp_Node.left_downNode != None:
            temp_Node2 = temp_Node.left_downNode
            if calculate_distance(temp_Node2.value, input_example, p) < calculate_distance(most_near_Node.value, input_example, p):
                most_near_Node = temp_Node2
    most_near_Node = search_iter(most_near_Node, input_example, p, temp_Node, temp_Node1)
    return most_near_Node

def search_iter(near_Node, input_example, p, temp_Node, temp_Node1):
    '''迭代寻找'''
    if temp_Node.upNode != None:
        temp_Node = temp_Node.upNode
        temp_Node1 = temp_Node1.upNode
        if calculate_distance(temp_Node.value, input_example, p) < calculate_distance(near_Node.value, input_example, p):
            near_Node = temp_Node
        if temp_Node1.note == 0:
            if temp_Node.right_downNode != None:
                temp_Node2 = temp_Node.right_downNode
                if calculate_distance(temp_Node2.value, input_example, p) < calculate_distance(near_Node.value,
                                                                                               input_example, p):
                    near_Node = temp_Node2
        else:
            if temp_Node.left_downNode != None:
                temp_Node2 = temp_Node.left_downNode
                if calculate_distance(temp_Node2.value, input_example, p) < calculate_distance(near_Node.value,
                                                                                               input_example, p):
                    near_Node = temp_Node2
        near_Node = search_iter(near_Node, input_example, p, temp_Node, temp_Node1)
    return near_Node


def main( ):
    origin_data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
    node = construct_balance_KD_tree.construct_tree(origin_data, 2)
    a = search_tree(node, [5, 4.5], 2, 2)
    print('bupt')

if __name__ == '__main__':
    main( )
