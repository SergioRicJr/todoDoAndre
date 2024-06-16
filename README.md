# Todo Do André

Este é um projeto FullStack, com API e FrontEnd para gerenciamento de usuários e tarefas a fazer, conta com segurança e privacidade, pois suas tarefas não são visíveis para outros usuários e é necessário criação de conta e autenticação para o uso.

## Requisitos

- Python 3.x
- Mongo DB Compass 1.x
- Git

## Funcionalidades do projeto

- [x] Criar conta
- [x] Editar conta
- [x] Deletar conta
- [x] Login
- [x] Logout
- [x] Criar tarefas
- [x] Visualizar tarefas
- [x] Editar tarefas
- [x] Deletar tarefas

## Endpoints do projeto

- `/`: lista as tarefas
- `/insert`: cria novas tarefas
- `/tasks/delete/`: deleta uma tarefas
- `/update/<pk>`: atualiza uma tarefas
- `/user_insert`: cria uma conta de usuário
- `/user/delete/`: deleta sua conta
- `/user_update/<pk>`: atualiza informações de conta
- `login`: acessa a aplicação através de credenciais
- `logout`: apaga os token do navegador

## Instalação e configuração

- 1 - Abra o terminal de comando e clone o repositório com o seguinte código: 

```
    git clone https://github.com/SergioRicJr/todoDoAndre
```

- 2 - Abra o vscode nesse projeto:

```
    cd todoDoAndre
```

```
    code .
```

- 3 - Garanta que o MongoDBCompass está ativo e configure a string de conexão do projeto no arquivo core/settings.py:

```
    MONGO_CONNECTION_STRING = "url e porta do seu MONGO"
    MONGO_DATABASE_NAME = "Nome da sua collection"
```

- 4 - Crie um ambiente virtual:

```
    python -m venv ./venv
```

- 5 - Ative o ambiente virtual:

```
    ./venv/Scripts/activate
```

- 6 - Baixe as dependências:


```
    pip install -r requirements.txt
```

## Inicie a aplicação

Após seguir todos os passos de instalação e configuração, basta rodar o seguinte código:

```
    python manage.py runserver
```
## Teste a aplicação / casos de uso

Após iniciar a aplicação, existem formas de acessar e testar, que são as seguintes:

- Através do navegador com a url `http://localhost:8000/` seguido pelos endpoints da aplicação, o que dará acesso a todas as funcionalidades através da interface web.

- Através do Postman, onde acessando com a mesma url da forma anterior, te traz uma forma diferente de acesso aos dados e facilidade no teste. Para isso, siga estes passos:

- Abra a collection `todoDoAndre.postman_collection.json` no postman
- Faça a requisição chamada get_crfstoken
- Acesse a aba de cookies e pegue o crfstoken recebido
- Em todas as requisições adicione no header a chave "X-CSRFToken" com o valor do csfstoken recebido