// https://visualgo.net/en/list

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
    this.length++;
  }

  prepend(value) {
    const node = new Node(value);
    node.next = this.head.next;
    this.head = node;
    this.length++;
  }

  insert(index, value) {
    if (index === 0) {
      return;
    }

    let current = this.head;

    for (let k = 0; k < index - 1; k++) {
      current = current.next;
    }
    const next = current.next;
    const node = new Node(value);
    node.next = next;
    current.next = node;
    this.length++;
    return;
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
linkedlist.insert(0, 110);
linkedlist.print();
