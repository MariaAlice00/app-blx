<h1>APP BLX</h1>

<div>
    <p>Funcionalidades</p>
    <ul>
        <li>Qualquer pessoa poderá anunciar produtos</li>
        <li>Qualquer pessoa poderá fazer pedidos dos produtos anunciados</li>
        <li>Uma pessoa tem:
            <ul>
                <li>Nome</li>
                <li>Telefone whatsapp</li>
                <li>Senha(?)</li>
            </ul>
        </li>
        <li>Uma produto tem:
            <ul>
                <li>Nome</li>
                <li>Detalhamento</li>
                <li>Preço</li>
                <li>Disponível (sim / não)</li>
                <li>Fotos (?)</li>
            </ul>
        </li>
        <li>Um pedido tem:
            <ul>
                <li>Produto</li>
                <li>Pessoa que está pedindo</li>
                <li>Quantidade</li>
                <li>Local de entrega</li>
                <li>Entrega ou retirada</li>
                <li>Observações (sabor, horário de entrega, troco, etc)</li>
            </ul>
        </li>
        <li>Cada usuário terá uma lista de pedidos recebidos (minhas vendas) e pedidos feitos (minhas compras)</li>
        <li>O pedido deverá ser aceito pelo vendedor</li>
        <li>O comprador poderá acompanhar seus pedidos:
            <ul>
                <li>Status (feito, aceito)</li>
            </ul>
        </li>
    </ul>
</div>

<div>
    <p>Arquitetura e Ferramentas</p>
    <ul>
        <li>Python + FastAPI</li>
        <li>Será uma API REST</li>
        <li>Banco de Dados: Postgres e/ou MongoDB (firebase firestore)</li>
        <li>MVC</li>
        <li>Domain Driven Design (DDD) e Arquitetura Limpa (Clean Architecture)</li>
    </ul>
</div>

<div>
    <p>Informações extras:</p>
    <ul>
        <li>SQLAlchemy = ferramenta que auxilia na conexão com o banco de dados</li>
        <li>Rodar o código -> uvicorn src.server:app --reload --reload-dir=src</li>
    </ul>
</div>
