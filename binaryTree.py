class BinaryTree:  
    """
do: класс для реализации бинарного дерева поиска
    """
    def __init__(self):
        """
    do: создание пустого бинарного дерева
    returns: None
        """
        self.root = EmptyNode()   
        BinaryNode.numberOfNodes = 0

    def __repr__(self):   
        """
    do: строковое представление дерева (корня)
    returns: строка представления корня (корня)
        """
        return repr(self.root)   

    def insert(self, value):   
        """
    do: вставляет новое значение в корень (в дерево)
    arguments: value: значение для вставки
    returns: None
        """ 
        self.root = self.root.insert(value) 

    def __contains__(self, value):
        """
    do: проверяет наличие значения в корне (в дереве)
    arguments: value: значение для проверки
    returns: bool: True -- значение найдено, False -- не найдено
        """
        return value in self.root  

    def __len__(self):  
        """
    do: считает количество узлов в корне (в дереве)
    returns: количество элементов в корне (в дереве)
        """
        return len(self.root)

    def lcr(self):  
        """
    do: делает lcr обход корня
    returns: значения полученные при обходе
        """
        return self.root.lcr()  

    def min(self):
        """
    do: находит минимальное значение в дереве
    returns: возвращает минимальное значение
        """
        return self.root.min() 

    def max(self):
        """
    do: находит максимальное значение в дереве
    returns: возвращает максимальное значение
        """
        return self.root.max()
    
class EmptyNode:  
    """
do: класс для пустой вершины бинарного дерева
    """

    def __repr__(self):
        """
        do: возвращает строковое представление пустой вершины
        returns: строка '*'
        """
        return '*'  

    def insert(self, value):
        """
        do: вставляет значение вместо пустой вершины
        arguments: value -- значение для вставки
        returns: новый объект BinaryNode c вставленным значением
        """
        return BinaryNode(self, value, self) 

    def __contains__(self, value):
        """
        do: проверяет наличие значения в пустой вершине (всегда False)
        arguments: value -- значение для проверки
        returns: False
        """
        return False  

    def __len__(self):
        """
        do: возвращает количество узлов в пустой вершине (всегда 0)
        returns: 0
        """
        return 0  

    def lcr(self):
        """
        do: возвращает список значений при центрированном обходе пустой вершины
        returns: пустой список
        """
        return []  

    def min(self):
        """
        do: возвращает минимальное значение в пустой вершине
        returns: None
        """
        return None

    def max(self):
        """
        do: возвращает максимальное значение в пустой вершине
        returns: None
        """
        return None
    
class BinaryNode:   
    """
do: класс для непустого элемента бинарного дерева
attributes: numberOfNodes -- количество созданных непустых вершин (обнуляется при создании нового объекта)
    """
    numberOfNodes = 0       

    def __init__(self, left, value, right): 
        """
        do: конструктор узла с левым и правым поддеревом и значением
        arguments: left -- левое поддерево
                   value -- значение узла
                   right -- правое поддерево
        returns: None
        """
        self.left = left  
        self.value = value  
        self.right = right   
        BinaryNode.numberOfNodes += 1  

    def __repr__(self):  
        """
        do: строковое представление узла и поддеревьев
        returns: строка вида '(левое поддерево, значение, правое поддерево)'
        """
        return f'({self.left}, {self.value}, {self.right})'  

    def insert(self, value): 
        """
        do: вставляет значение в поддерево по правилу бинарного дерева
        arguments: value -- значение для вставки
        returns: обновлённый узел
        """
        if value < self.value: 
            self.left = self.left.insert(value)
        if value >= self.value: 
            self.right = self.right.insert(value)
        return self  

    def __contains__(self, value): 
        """
        do: рекурсивно проверяет наличие значения в поддереве.
        arguments: value -- значение для поиска
        returns: True если найдено, иначе False
        """
        if value < self.value:  
            return value in self.left 
        elif value > self.value: 
            return value in self.right
        else:
            return True

    def __len__(self):   
        """
        do: возвращает количество всех узлов в дереве (атрибут класса)
        returns: число узлов
        """
        return self.numberOfNodes 

    def lcr(self):   
        """
        do: рекурсивно делает lcr обход дерева
        returns: список значений в порядке лево-центр-право
        """
        result = self.left.lcr() + [self.value] + self.right.lcr()    
        return result 

    def min(self):
        """
        do: рекурсивно находит минимальное значение в дереве
        returns: минимальное значение
        """
        if isinstance(self.left, EmptyNode):  
            return self.value   
        else: 
            return self.left.min() 

    def max(self):
        """
        do: рекурсивно находит максимальное значение в дереве
        returns: максимальное значение
        """
        if isinstance(self.right, EmptyNode):   
            return self.value    
        else: 
            return self.right.max()