from pydantic import BaseModel
from typing import Optional, List
from models.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Geladeira"
    preco: float = 130.00
    descricao: str = "Uma Geladeira economica baseado em consumo de energia"
    marca: str = "Brastemp"
    categoria: str = "Eletrodomesticos"


class ProdutoViewSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Geladeira"
    preco: float = 130.00
    descricao: str = "Uma Geladeira economica baseado em consumo de energia"
    marca: str = "Brastemp"
    categoria: str = "Eletrodomesticos"
    comentarios: List[str] = ["Só comprar se o preço  estiver com desconto!"]


class ProdutoBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    termo: str = "Geladeira"


class ProdutoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoViewSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ListagemProdutosSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "marca": produto.marca,
            "categoria": produto.categoria,
            "comentarios": [c.texto for c in produto.comentarios]
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Geladeira"
    preco: float = 130.00
    descricao: str = "Uma Geladeira economica baseado em consumo de energia"
    marca: str = "Brastemp"
    categoria: str = "Eletrodomesticos"
    total_cometarios: int = 1
    comentarios:List[str] = ["Só comprar se o preço estiver com desconto!"]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "descricao": produto.descricao,
        "marca": produto.marca,
        "categoria": produto.categoria,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [c.texto for c in produto.comentarios]
    }


