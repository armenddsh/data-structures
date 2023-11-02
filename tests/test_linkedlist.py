from src.linkedlist import LinkedList

def test_linkedlist():

    linkedList = LinkedList()
    linkedList.append_beginning(10)
    linkedList.append_beginning(11)
    linkedList.append_beginning(12)
    linkedList.append_beginning(13)
    linkedList.append_end(9)
    linkedList.append_end(8)
    linkedList.append_end(7)

    linkedList.traverse_forward()

    assert linkedList.head.data == 13
    assert linkedList.head.next.data == 12
    assert linkedList.head.next.next.data == 11
    assert linkedList.head.next.next.next.data == 10
    assert linkedList.head.next.next.next.next.data == 9
    assert linkedList.head.next.next.next.next.next.data == 8
    assert linkedList.head.next.next.next.next.next.next.data == 7
    assert linkedList.head.next.next.next.next.next.next.next == None

def test_doublelinkedlist():

    linkedList = LinkedList()