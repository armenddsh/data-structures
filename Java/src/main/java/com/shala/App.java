package com.shala;

import com.shala.tree.Tree;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        Tree tree = new Tree(10);
        tree.insert(30);
        tree.insert(5);
        tree.insert(25);

        boolean found = tree.find(4);
        System.out.println(found);
        System.out.println(tree);
    }
}
