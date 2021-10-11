import java.util.Scanner;

/** Main class gets user input for the operands/operators */
public class Main {
  private static String expression;

  private static Queue<Character> postfixQueueEval;

  public static void main(String[] args) {
    // empty string expression and eval queue to be used later
    expression = "";
    postfixQueueEval = new Queue<Character>();

    // scanner for user input
    Scanner s = new Scanner(System.in);
    System.out.print("Enter infix expression: ");
    expression = s.nextLine();

    // this is setting up the ouput
    System.out.println("Summary");
    System.out.println("_______");
    System.out.println("  Infix: " + expression);
    System.out.println("Postfix: " + infixToPostfix(expression));
    System.out.println(" Result: " + evalPostfix(infixToPostfix(expression)));

  }

  /** Returns the priority of the infix string chars */
  static int getInfixPriority(char c) {
    int priority;

    // all if the cases return their specific priority
    if (c == '(') {
      priority = 4;

    }
    else if (c == '^') {
      priority = 3;

    }
    else if (c == '*' || c == '/') {
      priority = 2;

    }
    else if (c == '+' || c == '-') {
      priority = 1;

    }
    else {
      priority = 0;
    }
    return priority;
  }
  /** Returns the priority of the chars from the stack */
  static int getStackPriority(char c) {
    int priority;

    // all of the cases return their specific priority
    if (c == '^' || c == '*' || c == '/') {
      priority = 2;
    }
    else if (c == '+' || c == '-') {
      priority = 1;
    }
    else {
      priority = 0;
    }

    return priority;

  }
  static boolean isOperand(char c) {
    if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
      return true;
    }
    return false;
  }
  /** I added this recursive method to get the power of a varible with another */
  static int power(int b, int e) {
    //setting the base case
    if (e == 0) {
      return 1;
    }
    // the recursive call
    return (b * power(b, e - 1));
  }
  /** Evaluates based on the given operater */
  static int eval(char operator, int x, int y) {
    int answer;

    // adds if char is '+'
    if (operator == '+') {
      answer = (x + y);
    }
    // subtracts if char is '-'
    else if (operator == '-') {
      answer =  (x - y);
    }
    // multiplies if char is '*'
    else if (operator == '*') {
      answer =  (x * y);
    }
    // divides if char is '/'
    else if (operator == '/') {
      answer = (x / y);
    }
    // calls the power method if char is '^'
    else if (operator == '^') {
      answer = power(x, y);
    }
    // otherwise it returns my error value
    else {
      answer = -1;
    }
    // returns the as=nswer given from above
    return answer;

  }
  /** Returns a string that contains the converted infix string */
  static String infixToPostfix(String infixString) {
    // instantiating all needed variables and stacks/queues
    char operator;
    String postfix = "";
    char token;

    Queue<Character> infixQueue = new Queue<Character>();
    Queue<Character> postfixQueue = new Queue<Character>();
    Stack<Character> operatorStack = new Stack<Character>();

    // moves chars from the given string into a queue
    for (int i = 0; i < expression.length(); i ++) {
      infixQueue.enqueue(expression.charAt(i));
    }
    // creating the token
    while (!infixQueue.isEmpty()) {
      token = infixQueue.dequeue();

      // checking if is a 0-9 char
      if (isOperand(token)) {
        postfixQueue.enqueue(token);
      }
      // this takes care of the opening and closing parenthesis
      else if (token == ')') {
        operator = operatorStack.pop();

        while (operator != '(') {
          postfixQueue.enqueue(operator);
          operator = operatorStack.pop();
        }
      }
      // this finds the operators and their priorities
      else {
        if (!operatorStack.isEmpty()) {
          operator = operatorStack.peek();

          while (getStackPriority(operator) >= getInfixPriority(token)) {
            operator = operatorStack.pop();
            postfixQueue.enqueue(operator);

            if (!operatorStack.isEmpty()) {
              operator = operatorStack.peek();

            }
            else {
              break;
            }
          }
        }
        operatorStack.push(token);
      }
    }
    while (!operatorStack.isEmpty()) {
      operator = operatorStack.pop();
      postfixQueue.enqueue(operator);
    }
    // putting together the postfix string, which is the completed coverted string
    while (!postfixQueue.isEmpty()) {
      postfix += postfixQueue.dequeue();
    }
    return postfix;
  }
  /** Takes in the converted postfix string and returns the value of the expression */
  static int evalPostfix(String postfixString) {
    // istantiate the needed stack and variables
    Stack<Integer> evalStack = new Stack<Integer>();

    char token;
    int a;
    int b;
    int answer;

    // filling up the queue from the postfix string
    for (int i = 0; i < postfixString.length(); i++) {
      postfixQueueEval.enqueue(postfixString.charAt(i));
    }
    // creating the token
    while (postfixQueueEval.isEmpty() == false) {
      token = postfixQueueEval.dequeue();

      // if it is a digit, pushes the numeric value of token
      if (isOperand(token)) {
        evalStack.push(Character.getNumericValue(token));
      }

      // otherwise evaluate two given variables with the operaters in char form
      // takes the resulting integer and put it into a stack
      else {
        a = evalStack.pop();
        b = evalStack.pop();
        answer = eval(token, b, a);
        evalStack.push(answer);
      }
    }
    // returns the final answer from the stack
    if (!evalStack.isEmpty()) {
      return evalStack.pop();
    }
    // returns my error value
    return -1;
  }
}
