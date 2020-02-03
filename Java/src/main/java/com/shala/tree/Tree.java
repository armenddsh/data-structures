package com.shala.tree;

import java.beans.beancontext.BeanContext;

public class Tree {

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