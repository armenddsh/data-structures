package com.shala;

import com.shala.tree.Tree;
import com.shala.tree.Tree.Traverse;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        Tree tree = new Tree(20);
        tree.insert(10);
        tree.insert(30);
        tree.insert(6);
        tree.insert(14);
        tree.insert(24);
        tree.insert(3);
        tree.insert(8);
        tree.insert(26);

        // int height = tree.height();
        // System.out.println(height);
        // tree.traverse(Traverse.PRE_ORDER);
        // tree.traverse(Traverse.IN_ORDER);
        // tree.traverse(Traverse.POST_ORDER);
        tree.traverse(Traverse.LEVEL_ORDER);
    }
}
