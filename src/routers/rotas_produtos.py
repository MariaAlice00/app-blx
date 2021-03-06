from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.routers.auth_utils import obter_usuario_logado


router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    produto.usuario_id = usuario.id
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(session: Session = Depends(get_db)):
    produtos  = RepositorioProduto(session).listar()
    return produtos


@router.get('/produtos/{id}')
def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(session).buscarPorId(id)

    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com o id = {id}')

    return produto_localizado


@router.put('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@router.delete('/produtos/{id}')
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {"msg": "produto removido com sucesso"}

