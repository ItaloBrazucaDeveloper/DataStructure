from stack import Stack

def main():
  stack = Stack()
  stack.push("A")
  stack.push("B")
  stack.push("C")
  
  print("Pilha:", stack.items)
  
  print("Elemento removido:", stack.pop())
  print("Pilha após remoção:", stack.items)
  
  print("Elemento do topo:", stack.top())
  
  print("A pilha está vazia?", stack.isEmpty())
  
  print("Elemento removido:", stack.pop())
  print("Elemento removido:", stack.pop())
  
  print("A pilha está vazia?", stack.isEmpty())

if __name__ == "__main__":
  main()