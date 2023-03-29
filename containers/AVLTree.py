'''
This file implements the AVL Tree data structure.
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        if not node:
            return True
        else:
            right_satisfied = AVLTree._is_avl_satisfied(node.right)
            left_satisfied = AVLTree._is_avl_satisfied(node.left)
            return right_satisfied and left_satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        node_copy = node
        if node_copy.right:
            new_root = Node(node_copy.right.value)
            new_root.left = Node(node_copy.value)
            new_root.right = node_copy.right.right
            new_root.left.left = node_copy.left
            new_root.left.right = node_copy.right.left
            return new_root
        else:
            return node_copy

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        node_copy = node
        if node_copy.left:
            new_root = Node(node_copy.left.value)
            new_root.right = Node(node_copy.value)
            new_root.left = node_copy.left.left
            new_root.right.right = node_copy.right
            new_root.right.left = node_copy.left.right
            return new_root
        else:
            return node_copy

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
            print(self)
        else:
            self.root = Node(value)
            print(self)

    @staticmethod
    def _insert(node, value):
        if node is None:
            node = Node(value)
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = AVLTree._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = AVLTree._insert(node.right, value)
        node = AVLTree._rebalance(node)
        return node

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
        return node
