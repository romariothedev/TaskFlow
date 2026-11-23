# TaskFlow — Gerenciamento Ágil de Tarefas

## Objetivo
Sistema web acadêmico para cadastrar, acompanhar, atualizar e excluir tarefas de uma equipe, visualizando o fluxo em três etapas: A Fazer, Em Progresso e Concluído.

## Escopo inicial
- Criar tarefas com título e descrição.
- Listar tarefas organizadas por status.
- Atualizar o status de uma tarefa.
- Excluir tarefas.
- Executar testes automatizados com Pytest.

## Metodologia
Será utilizado Kanban, com as colunas A Fazer, Em Progresso e Concluído. O quadro será mantido no GitHub Projects.

## Tecnologias
Python, Flask, SQLite, Pytest, GitHub Actions e Git.

## Como executar
1. Instale Python 3.10 ou superior.
2. Crie e ative um ambiente virtual (opcional, recomendado).
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute: `python app.py`
5. Acesse `http://127.0.0.1:5000`.

## Como executar os testes
`pytest -v`

## Estrutura
- `app.py`: rotas e regras da aplicação.
- `database.py`: criação e conexão com o banco SQLite.
- `templates/`: páginas HTML.
- `static/`: estilos CSS.
- `tests/`: testes automatizados.
- `.github/workflows/`: pipeline de integração contínua.

## Mudança de escopo
Após a versão inicial, foi incluída a possibilidade de alterar o status da tarefa diretamente no painel Kanban. A mudança melhora o acompanhamento do fluxo de trabalho sem alterar o objetivo principal do sistema.

## Situação
Projeto acadêmico em desenvolvimento. O quadro GitHub Projects, os commits e a execução do workflow devem ser registrados no repositório durante o desenvolvimento.
