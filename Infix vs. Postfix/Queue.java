/** Queue abstract data type */
public class Queue<T> {
  /** List objects to hold our queue items.
      Use List operations to implement the methods below */
  private List<T> list;

  public Queue() {
    // instantiate list here
    list = new List<T>();

  }

  // Adds a value to the end of the queue
  public void enqueue(T value) {
    list.append(value);
  }

  // Deletes the first value that was added to the list
  public T dequeue() {
    T value = list.getValueAt(0);
    list.deleteAt(0);
    return value;
  }

  // Shows the value that was first added to the list
  public T front() {
    T value = list.getValueAt(0);
    return value;
  }

  // Checks if the queue is empty with the list.size method
  public boolean isEmpty() {

    if (list.size() == 0) {
      return true;
    }

    return false;
  }
}
