import doctest

def funcao1 (invent):
    """Printa o inventario no cmd.

    :param invent: Rece um dicionario com as chaves sendo o nome e o valor a quantidade
    :type invent: dict
    
    
    >>> inv = {"item1": 1, "item2": 3, "item3": 6}
    >>> funcao1(inv)
    {'item1': 1, 'item2': 3, 'item3': 6}
    
    >>> mercado = {"arroz": 4, "feijão": 10, "farofa": 25}
    >>> funcao1(mercado)
    {'arroz': 4, 'feijão': 10, 'farofa': 25}
    
    >>> mercado = ["arroz", "feijão", "farofa"]
    >>> funcao1(mercado)
    O objeto do inventário fornecido deve ser um dicionário!
    """
    if not isinstance(invent, dict):
        print("O objeto do inventário fornecido deve ser um dicionário!")
        return
    
    print(invent)


def funcao2 (item, quant, invent):
    """adiciona no invenetario

    :param item: nome do item
    :type item: str
    :param quant: quantidade do item
    :type quant: int
    :param invent: dicionario do inventario
    :type invent: dict
    :return: Dicionario atualizado
    :rtype: dict
    
    >>> inv = {"item1": 1, "item2": 3, "item3": 6}
    >>> funcao2("item1", 2, inv)
    {'item1': 3, 'item2': 3, 'item3': 6}
    
    >>> mercado = {"arroz": 4, "feijão": 10, "farofa": 25}
    >>> funcao2("cenoura", 3, mercado)
    {'arroz': 4, 'feijão': 10, 'farofa': 25, 'cenoura': 3}
    
    >>> mercado = {"arroz": 4, "feijão": 10, "farofa": 25}
    >>> funcao2("cenoura", 3.4, mercado)
    A quantidade fornecida deve ser um número inteiro!
    {'arroz': 4, 'feijão': 10, 'farofa': 25}
    """
    if not isinstance(invent, dict):
        print("O objeto do inventário fornecido deve ser um dicionário!")
        return
        
    if not isinstance(quant, int) or quant < 0:
        print("A quantidade fornecida deve ser um número inteiro!")
        return invent
    
    if not isinstance(item, str):
        print("O item fornecido deve ser uma string!")
        return invent
    
    lista_inv = list(invent.keys())
    
    if item in lista_inv:
        invent[item] += quant
        
    # Caso o item não exista no inventário
    else:
        invent[item] = quant
        
    return invent
    

def funcao3 (item, quant, invent):
    """Remove item

    :param item: nome do item
    :type item: str
    :param quant: quantidade do item
    :type quant: int
    :param invent: dicionario do inventario
    :type invent: dict
    :return: Dicionario atualizado
    :rtype: dict
    
    >>> inv = {"item1": 1, "item2": 3, "item3": 6}
    >>> funcao3("item2", 1, inv)
    {'item1': 1, 'item2': 2, 'item3': 6}
    
    >>> mercado = {"arroz": 4, "feijão": 10, "farofa": 25}
    >>> funcao3("arroz", 5, mercado)
    {'feijão': 10, 'farofa': 25}
    
    >>> mercado = {"arroz": 4, "feijão": 10, "farofa": 25}
    >>> funcao3("cenoura", 3.4, mercado)
    A quantidade fornecida deve ser um número inteiro!
    {'arroz': 4, 'feijão': 10, 'farofa': 25}
    """
    if not isinstance(invent, dict):
        print("O objeto do inventário fornecido deve ser um dicionário!")
        return
        
    if not isinstance(quant, int) or quant < 0:
        print("A quantidade fornecida deve ser um número inteiro!")
        return invent
    
    if not isinstance(item, str):
        print("O item fornecido deve ser uma string!")
        return invent
    
    lista_inv = list(invent.keys())
    
    if item in lista_inv:
        invent[item] -= quant
        
        # Caso a quantidade de item fique menor ou igual a zero, remove do inventário
        if invent[item] <= 0: 
            invent.pop(item)
    else:
        print(f"Não existem itens do tipo '{item}' no inventário fornecido.")
    
    return invent
    pass
    
def funcao4 (item, invent):
    """Retorna um item e sua quantidade

    :param item: nome do item
    :type item: srt
    :param invent: dicionario do inventario
    :type invent: dict
    :return: Lista com o item e a quantidade
    :rtype: list
    """
    pass

doctest.testmod()