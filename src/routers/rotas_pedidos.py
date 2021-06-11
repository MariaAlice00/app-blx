from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.schemas.schemas import Pedido, PedidoSimples, Usuario
from src.routers.auth_utils import obter_usuario_logado


router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravarpedido(pedido)
    return pedido_criado


@router.get('/pedidos/{id}', response_model=List[Pedido])
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pedido_localizado = RepositorioPedido(session).buscar_por_id(id)

    if not pedido_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com o id = {id}')

    return pedido_localizado


@router.get('/pedidos', response_model=List[PedidoSimples])
def listar_meus_pedidos(usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario.id)

    return pedidos


@router.get('/pedidos/{usuario_id}/vendas', response_model=List[PedidoSimples])
def listar_minhas_vendas(usuario_id: int, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)

    return pedidos
