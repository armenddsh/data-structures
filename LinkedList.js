class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    const node = new Node(value);
    this.head = this.tail = node;
    this.length = 1;
  }
  
  append(value) {
    const node = new Node(value);
    this.tail.next = node;
    this.tail = node;
  }
  
  prepend(value) {
    const node = new Node(value);
    node.next = this.head.next;
    this.head = node;
  }
  
  print() {
    let current = this.head;
    let items = [];
    while (current != null) {
      items.push(current.value);
      current = current.next;
    }
    console.log(items);
  }
}


const linkedlist = new LinkedList(10);
linkedlist.append(1);
linkedlist.append(2);
linkedlist.append(3);
linkedlist.append(4);
linkedlist.append(5);
linkedlist.prepend(0);
linkedlist.print();
