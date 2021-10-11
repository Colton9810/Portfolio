/** Linked List implementation of our List abstract data type */
public class List<T> {
  // put all fields from ListAsLinkedList class here

  /**Pointers to the first and second node in the list */
  private Node head;
  private Node tail;

  /** constructor setting head and tail to null */
  public void List() {
    head = tail = null;
  }

  // put all methods from ListAsLinkedList class here

  // Adds to the end of the linked list by adding next to the tail (using tail.setNext) then setting that new node to the tail
  public void append(T data) {
    Node<T> temp = new Node<T>(data);

    // If no nodes currently in the list, make this the FIRST
    if (tail == null) {
      tail = temp;
      head = temp;
    }
    else {
      tail.next = temp;
      tail = temp;
    }
  }

  // Adds a new value to the beginning of the linked list by putting it next to the head and then setting it to head
  public void prepend(T data) {
    Node<T> temp = new Node<T>(data);

    // If empty list, make this the first node
    if (head == null) {
      tail = temp;
      head = temp;

    }

    else{
      temp.next = head;
      head = temp;
    }
  }

  // Delete specific value by setting the pointer to skip over the node that you want to delete
  public void deleteAt(int position) {
    // If position is 0 just skip over the current head
    if (position == 0) {
        Node<T> cur = head;
        head = cur.next;
    }
    // else find pos before the value and set the next node to the one after the deleted node
    else {

        for(int i = 0 ; i < (position - 1); i++) {
            head = head.next;
        }
        Node<T> cur = head;

        cur.next = cur.next.next;
    }
  }

  // Gets the size by searching the the whole list and increasing a counter each time it moves until it hits null
  public int size() {
    int n = 0;
    Node<T> cur = head;

    while (cur != null) {
      cur = cur.next;
      n++;
    }

    return n;
  }

  // gets a value at specific index by searching until you hit that position and returning the value
  public T getValueAt(int position) {
    Node<T> cur = head;
    for (int i = 0; i < position -1; i++) {
        cur = cur.next;
    }
    return cur.data;
  }

  // Gets the position of a specific value by searching the list until you find that value and then returning the index at that point
  public int positionOf(T value) {
    int pos = 0;
    Node<T> cur = head;

    /** Keep looking until we find a node containing target data */
    while (cur.data != value) {
      cur = cur.next;

      pos++;
      }

    return pos;
  }
}

/** A linked list node for our linked list */
class Node<T> {
  // put all fields from Node class here
  public T data;

  /** Link */
  public Node<T> next;

  /** Constructor taking data to be stored in the node @param data */
  public Node(T data) {
    this.data = data;
    this.next = null;
  }
}
