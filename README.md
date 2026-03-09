## API (FastAPI) - Documentação Básica



### 1. Arquitetura e Organização

O projeto segue uma organização simples, mas inspirada em **Arquitetura Limpa**, separando cada responsabilidade em uma pasta:

- `app/api` → rotas (endpoints HTTP, controllers)
- `app/services` → regras de negócio (use cases)
- `app/repositories` → acesso ao banco com SQLAlchemy
- `app/models` → modelos/entidades do banco (`User`, `Course`, `Enrollment`)
- `app/schemas` → modelos Pydantic para entrada/saída (validação e respostas)
- `app/core` → utilitários (padrão de respostas JSON)
- `app/database.py` → configuração do banco (SQLite) e sessão do SQLAlchemy
- `app/main.py` → criação da aplicação FastAPI, registro das rotas e tratamento de erros

Essa separação deixa claro onde fica cada parte do sistema, melhora a organização do código e facilita a manutenção, atendendo ao que foi pedido sobre Arquitetura Limpa e Clean Code.

### 2. Modelagem do Banco

Banco de dados: **SQLite** (arquivo `studymanager.db`).

- **User**
  - Campos: `id`, `name`, `email` (único), `created_at`
  - Relacionamentos:
    - Um usuário tem várias matrículas (`enrollments`)
    - Um usuário está em vários cursos via tabela de matrículas (`courses`)

- **Course**
  - Campos: `id`, `title`, `description`, `workload`
  - Relacionamentos:
    - Um curso tem várias matrículas (`enrollments`)
    - Um curso possui vários usuários matriculados (`users`)

- **Enrollment**
  - Campos: `id`, `user_id`, `course_id`, `enrolled_at`
  - Relacionamentos:
    - Pertence a um usuário (`user`)
    - Pertence a um curso (`course`)
  - Regra: índice único (`user_id`, `course_id`) para impedir matrícula duplicada.

### 3. Endpoints Principais

Prefixo base da API: `http://localhost:8000`

- **Usuários**
  - `GET /users` → lista todos os usuários
  - `POST /users` → cria um usuário
  - `GET /users/{id}` → busca usuário por ID
  - `PUT /users/{id}` → atualiza usuário
  - `DELETE /users/{id}` → remove usuário

- **Cursos**
  - `GET /courses` → lista cursos
  - `POST /courses` → cria curso
  - `GET /courses/{id}` → busca curso por ID
  - `PUT /courses/{id}` → atualiza curso
  - `DELETE /courses/{id}` → remove curso

- **Matrículas**
  - `POST /enrollments` → cria matrícula (não permite duplicada e valida se usuário e curso existem)

- **Consulta Relacional**
  - `GET /users/{id}/courses` → retorna os dados do usuário e a lista de cursos em que ele está matriculado.

Todas as respostas seguem um padrão JSON:

```json
{
  "success": true,
  "message": "Mensagem da operação",
  "data": { }
}
```

### 4. Como Rodar o Projeto
  
1. No diretório `StudyManagerFastAPI`, instalar dependências:
   ```bash
   python -m pip install -r requirements.txt
   ```
   (Se a pasta estiver em app/ use:)
   ```bash
   cd ..
   ```
   Ou, se você usar `py` no Windows:
   ```bash
   py -m pip install -r requirements.txt
   ```
3. Rodar o servidor:
   ```bash
   python -m uvicorn app.main:app --reload
   ```
   Ou com `py`:
   ```bash
   py -m uvicorn app.main:app --reload
   ```
4. Acessar a documentação automática da API (Swagger):
   - `http://localhost:8000/docs`

