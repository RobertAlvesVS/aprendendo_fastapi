# 📦 Guia de Configuração de Ambiente Python com Pipx, Poetry, FastAPI e Ferramentas de Desenvolvimento

---

## 🔹 1. Instalação do Pipx

O **Pipx** permite instalar e executar utilitários Python de forma **global e isolada**, utilizando ambientes virtuais.

### ✅ Instalação:

```bash
pip install --user pipx
```

### ✅ Adicionando ao PATH:

```bash
pipx ensurepath
```

---

## 🔹 2. Instalando o Poetry com o Pipx

O **Poetry** é um gerenciador completo de projetos Python.

### ✅ Instalação:

```bash
pipx install poetry
```

### ✅ Habilitando suporte ao `poetry shell`:

```bash
pipx inject poetry poetry-plugin-shell
```

---

## 🔹 3. Criando um Projeto com Poetry

Crie um novo projeto com estrutura plana:

```bash
poetry new --flat nome_do_projeto
cd nome_do_projeto
```

### ✅ Definindo a versão do Python no `pyproject.toml`:

```toml
[project]
requires-python = ">=3.13,<4.0"
```

---

## 🔹 4. Instalando o FastAPI

### ✅ Instalação:

```bash
poetry install
poetry add 'fastapi[standard]'
```

### ✅ Ativando o ambiente virtual:

```bash
poetry shell
```

---

## 🔹 5. Instalando Ferramentas de Desenvolvimento

Instale as ferramentas de desenvolvimento no grupo `dev`.

### ✅ Ferramentas:

- `taskipy`: automação de comandos
- `pytest`: testes
- `ruff`: linter e formatador de código

```bash
poetry add --group dev pytest pytest-cov taskipy ruff
```

---

## 🔹 6. Configuração do Ruff

### ✅ `pyproject.toml`:

```toml
[tool.ruff]
line-length = 79
extend-exclude = ['migrations']

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

[tool.ruff.format]
preview = true
quote-style = 'single'
```

---

## 🔹 7. Configuração do Pytest

### ✅ `pyproject.toml`:

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = "-p no:warnings"
```

---

## 🔹 8. Automação de Tarefas com Taskipy

### ✅ `pyproject.toml`:

```toml
[tool.taskipy.tasks]
lint = "ruff check"
pre_format = "ruff check --fix"
format = "ruff format"
run = "fastapi dev fast_zero/app.py"
pre_test = "task lint"
test = "pytest -s -x --cov=fast_zero -vv"
post_test = "coverage html"
```

### ✅ Descrição dos comandos:

| Comando         | Ação                                                                |
|-----------------|---------------------------------------------------------------------|
| `task lint`     | Verifica boas práticas no código                                    |
| `task pre_format` | Aplica correções automáticas de linting                         |
| `task format`   | Formata o código segundo a PEP-8                                    |
| `task run`      | Executa o servidor FastAPI                                          |
| `task pre_test` | Executa o lint antes dos testes                                     |
| `task test`     | Executa testes com cobertura e saída detalhada                      |
| `task post_test`| Gera relatório HTML de cobertura                                    |

### ✅ Executando tarefas:

```bash
task <comando>
# Exemplo:
task run
```