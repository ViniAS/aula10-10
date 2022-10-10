inventario = {}

def listar_inventario() ->dict[str,int]:
    """ retorna o inventario

    Returns:
        dict[str,int]: inventário
    """    
    global inventario
    return inventario

def cadastrar_item(item: str, quantidade: int)-> dict[str, int]:
    """Cadastra um item no inventário

    Args:
        item (str): item a ser adcionado
        quantidade (int): quantidade do item

    Returns:
        dict[str, int]: inventário
    """    
    global inventario
    if item in inventario.keys():
        inventario[item] += quantidade
    else:
        inventario[item] = quantidade
    return inventario

def excluir_item(item: str) -> dict[str, int]:
    """Exclui um item do inventário

    Args:
        item (str): item a ser excluido

    Returns:
        dict[str, int]: iventário atualizado
    """    
    global inventario
    if item in inventario:
        inventario = inventario.pop(item)
    return inventario

def buscar_item(item: str) -> int|bool:
    """buscar um item no inventario

    Args:
        item (str): item a ser buscado

    Returns:
        int|bool: quantidade do item. Se o item não existir retorna False
    """    
    global inventario
    if item in inventario:
        return inventario[item]
    return False