from typing import List

class Stack:
  """
  Estrutura de dados linear: Stack ou pilha.
  A pilha é uma estrutura de dados do tipo LIFO (Last In First Out),
  ou seja, o último elemento adicionado é o primeiro a ser removido.
  """
  def __init__(self):
    self.items: List[str] = []
    self.lastIndex: int = -1

  def push(self, item: str) -> None:
    """Adiciona um elemento no topo da pilha."""
    self.items.append(item)
  
  def pop(self) -> str:
    """Remove o último elemento adicionado na pilha e o retorna."""
    if self.isEmpty():
      raise IndexError("pop from empty stack")
    
    return self.items.pop()
  
  def isEmpty(self) -> bool:
    """
    Verifica se a pilha está vazia.
    Retorna True se a pilha estiver vazia, False caso contrário.
    """
    return len(self.items) == 0
  
  def top(self) -> str|None:
    """
    Retorna o último elemento adicionado na pilha.
    Se a pilha estiver vazia, retorna None.
    """
    return self.items[self.lastIndex] if not self.isEmpty() else None