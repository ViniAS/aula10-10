import doctest

def listar_inventario() ->dict[str,int]:
    """ retorna o inventario

    Returns:
        dict[str,int]: inventário
    """    


def cadastrar_item(item: str, quantidade: int)-> dict[str, int]:
    """Cadastra um item no inventário

    Args:
        item (str): item a ser adcionado
        quantidade (int): quantidade do item

    Returns:
        dict[str, int]: inventário
    """    


def excluir_item(item: str) -> dict[str, int]:
    """Exclui um item do inventário

    Args:
        item (str): item a ser excluido

    Returns:
        dict[str, int]: iventário atualizado
    """    


def buscar_item(item: str) -> int|bool:
    """buscar um item no inventario

    Args:
        item (str): item a ser buscado

    Returns:
        int|bool: quantidade do item. Se o item não existir retorna False
    """    
