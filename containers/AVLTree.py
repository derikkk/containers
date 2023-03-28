'''
This file implements the AVL Tree data structure.
The functions in this file are
considerably harder than the functions in the BinaryTree and BST files,
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
        super().__init__(xs)

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
        Returns True if the avl tree satisfi
        es that all nodes have a balance factor in [-1,0,1].
        '''
        if self.root is None:
            return True
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node:
            if AVLTree._balance_factor(node) not in [-1, 0, 1]:
                return False
            else:
                if node.left:
                    ret &= AVLTree._is_avl_satisfied(node.left)
                if node.right:
                    ret &= AVLTree._is_avl_satisfied(node.right)
            return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AV
        L tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.right is None:
            return old_root
        else:
            new_root = Node(old_root.right.value)
            new_root.left = Node(old_root.value)
            new_root.right = old_root.right.right
            new_root.left.right = old_root.right.left
            new_root.left.left = old_root.left
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AV
        L tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.left:
            new_root = Node(old_root.left.value)
            new_root.right = Node(old_root.value)
            new_root.left = old_root.left.left
            new_root.right.right = old_root.right
            new_root.right.left = old_root.left.right
            return new_root
        return old_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-leve
        l overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AV
        L tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to th
        e code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(value, self.root)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left:
                node.left = AVLTree._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                node.right = AVLTree._insert(value, node.right)
            else:
                node.right = Node(value)
        return AVLTree._rebalance(node)

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
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
        return node
