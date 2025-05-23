# 🎬 Flix API

Uma API RESTful para gerenciamento de filmes, atores, gêneros e avaliações, desenvolvida com Django Rest Framework.

## 🚀 Funcionalidades

- CRUD completo para filmes, atores, gêneros e avaliações
- Autenticação de usuários
- Filtros e ordenações personalizadas
- Documentação interativa com Swagger
- Banco de dados SQLite para desenvolvimento

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Django 4+
- Django Rest Framework
- SQLite (para ambiente de desenvolvimento)
- Swagger/OpenAPI para documentação

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/augustojbe/flix-api.git
   cd flix-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

6. Acesse a documentação interativa:

   Abra o navegador e vá para `http://127.0.0.1:8000/swagger/`

## 📁 Estrutura do Projeto

```bash
flix-api/
├── actors/           # Gerenciamento de atores
├── app/              # Configurações principais do projeto
├── authentication/   # Autenticação de usuários
├── genres/           # Gerenciamento de gêneros
├── movies/           # Gerenciamento de filmes
├── reviews/          # Gerenciamento de avaliações
├── db.sqlite3        # Banco de dados SQLite
├── manage.py         # Utilitário de gerenciamento do Django
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação do projeto
```

## 🧪 Testes

Para rodar os testes automatizados:

```bash
python manage.py test
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
