package com.shala.tree;

import java.beans.beancontext.BeanContext;

import javax.management.RuntimeErrorException;

public class Tree {

    public enum Traverse {
        PRE_ORDER, IN_ORDER, POST_ORDER, LEVEL_ORDER
    }

    private Node root;

    public Tree() {
    }

    public Tree(int value) {
        this.root = new Node(value);
    }

    public void insert(int value) {
        if (this.root == null) {
            this.root = new Node(value);
            return;
        }

        Node newNode = new Node(value);
        Node current = this.root;

        while (current != null) {
            if (value <= current.value) {
                if (current.left == null) {
                    current.left = newNode;
                    break;
                }
                current = current.left;
            }
            if (value > current.value) {
                if (current.right == null) {
                    current.right = newNode;
                    break;
                }
                current = current.right;
            }
        }
    }

    public boolean find(int value) {
        Node current = this.root;

        while (current != null) {
            if (value == current.value)
                return true;
            else if (value < current.value) {
                current = current.left;
            } else if (value > current.value) {
                current = current.right;
            }
        }

        return false;
    }

    public void traverse(Traverse traverse) {
        Node node = this.root;

        if (traverse == Traverse.PRE_ORDER) {
            traversePreOrder(node);
        }
        if (traverse == Traverse.IN_ORDER) {
            traverseInOrder(node);
        }
        if (traverse == Traverse.POST_ORDER) {
            traversePostOrder(node);
        }
        if (traverse == Traverse.LEVEL_ORDER) {
            traverseLevelOrder(node);
        }
    }

    private void traverseLevelOrder(Node node) {
        int height = height();
        for (int i = 0; i < height; i++) {
            getValuesAtNode(i);
        }
    }

    private void traversePreOrder(Node node) {
        if (node != null) {
            System.out.println(node.value);
            traversePreOrder(node.left);
            traversePreOrder(node.right);
        }
    }

    private void traverseInOrder(Node node) {
        if (node != null) {
            traverseInOrder(node.left);
            System.out.println(node.value);
            traverseInOrder(node.right);
        }
    }

    private void traversePostOrder(Node node) {
        if (node != null) {
            traversePostOrder(node.left);
            traversePostOrder(node.right);
            System.out.println(node.value);
        }
    }

    public int height() {
        return height(root);
    }

    private int height(Node root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 0;
        }
        return 1 + Math.max(height(root.left), height(root.right));
    }

    @Override
    public String toString() {
        return "{" + " root='" + this.root + "'" + "}";
    }

    private class Node {
        private int value;
        private Node left;
        private Node right;

        public Node(int value) {
            this.value = value;
        }

        public Node() {
        }

        public Node(int value, Node left, Node right) {
            this.value = value;
            this.left = left;
            this.right = right;
        }

        public int getValue() {
            return this.value;
        }

        public void setValue(int value) {
            this.value = value;
        }

        public Node getLeft() {
            return this.left;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public Node getRight() {
            return this.right;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public Node value(int value) {
            this.value = value;
            return this;
        }

        public Node left(Node left) {
            this.left = left;
            return this;
        }

        public Node right(Node right) {
            this.right = right;
            return this;
        }

        @Override
        public String toString() {
            return "{" + " value='" + getValue() + "'" + ", left='" + getLeft() + "'" + ", right='" + getRight() + "'"
                    + "}";
        }

    }
}