# Golden Raspberry Awards API

Esta é uma API RESTful desenvolvida para leitura e análise da lista de indicados e vencedores da categoria **Pior Filme** do Golden Raspberry Awards.

---

## Requesitos

- Docker 24.0.7 
- Docker Compose 1.29.2

---

## Estrutura do Projeto

O projeto foi desenvolvido com **Python 3.11+**, utilizando **FastAPI** e organizado com base no padrão **MVC**, aliado à aplicação dos princípios **SOLID**.

```
├── .collections/              # Coleções para uso com o Postman
├── .docker/                   # Dockerfile e configurações de build
├── application/               # Core da api
│   ├── controllers/           # Camada de controllers
│   ├── database/              # Conexão com SQLite e seeder
│   │   ├── seeder/            # Seeder e arquivo CSV
│   ├── helpers/               # Funções universais
│   ├── models/                # Modelos de manipulação ORM
│   ├── routes/                # Configurações de rotas
│   ├── tests/                 # Testes automatizados
│   └── main.py                # Init da aplicação
├── .env                       # Variáveis de ambiente
├── requirements.txt           # Dependências do projeto
├── docker-compose.yml         # Orquestração dos serviços
├── Dockerfile                 # Imagem da aplicação
└── README.md                  # Documentação do projeto
```

---

## Instalação

1. Clone o repositório em uma pasta local (exemplo: `/home/fernando/Teste`)
2. Acesse o diretório raiz do projeto
3. Crie um arquivo `.env` na raiz do diretório `application` e cole o conteúdo `CSV_PATH=./application/database/seeder/movies.csv`
4. Execute o ambiente com os comandos:

```bash
make build
make up
```

---

## Swagger

Após iniciar o ambiente, acesse a documentação via Swagger:

```
http://localhost:8000/docs
```

---

## Teste unitário

Para executar o teste unitário basta rodar, com o ambiente online: `make test`

---


## Observações gerais

#### Requisitos aplicados
- Leitura de arquivo CSV contendo os dados dos filmes
- Carga automática de dados na base via seeder
- API para cálculo dos intervalos de prêmios por produtor
- Testes automatizados de integração com Pytest
- Ambiente isolado e configurado via Docker

#### Avisos
- O CSV encontra-se em `application/database/seeder/movies.csv`
- Produtores foram separados por `,` e `and`
- O banco SQLite é em memória, compartilhado via `StaticPool` para garantir consistência entre múltiplas threads

#### Endpoint Principal

`GET /producers/intervals`
`GET /producers/intervals/max`
`GET /producers/intervals/min`

### Tecnologias

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (em memória)
- Pytest
- python-dotenv
- Git Flow

---

## Autor

**Fernando Becker**  
Desenvolvedor Backend Python  
[linkedin.com/in/febeckers](https://www.linkedin.com/in/febeckers)
