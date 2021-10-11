/** Stack abstract data type */
public class Stack<T> {
  /** List objects to hold our stack items.
      Use List operations to implement the methods below */
  private List<T> list;

  public Stack() {
    // instantiate list here
    list = new List<T>();

  }

  // Push a value to the list using the prepend method from the list
  public void push(T value) {
    list.prepend(value);
  }

  // Pop a value by deleting the latest value added into the list
  public T pop() {
    T topValue = list.getValueAt(0);
    list.deleteAt(0);
    return topValue;
  }

  // Gets the value of the top value
  public T peek() {
    T value = list.getValueAt(0);
    return value;
  }

  // checks to see if the stack is empty by using the lsit.size method
  public boolean isEmpty() {
    int size = list.size();
    if (size == 0){
      return true;
    }

    return false;
  }
}
