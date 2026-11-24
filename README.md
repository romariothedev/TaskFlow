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
## Mudança de escopo simulada

Durante o desenvolvimento do TaskFlow, foi simulada uma
solicitação de mudança no escopo do projeto.

Inicialmente, o sistema previa apenas o cadastro e a
visualização de tarefas.

Após uma avaliação das necessidades dos usuários, foi
solicitada a inclusão de duas funcionalidades:

- Alteração do status das tarefas.
- Exclusão de tarefas cadastradas.

A mudança foi aceita porque melhora a organização e o
controle das atividades.

As funcionalidades foram incorporadas ao sistema e
registradas no quadro Kanban do GitHub Projects.

## Impactos da mudança

A alteração exigiu ajustes na aplicação, no banco de dados,
nos testes automatizados e na documentação.

## Instalação detalhada

Para executar o TaskFlow em outro computador, siga os passos:

1. Clone o repositório:
   `git clone https://github.com/romariothedev/TaskFlow.git`

2. Entre na pasta:
   `cd TaskFlow`

3. Instale as dependências:
   `pip install -r requirements.txt`

4. Inicie a aplicação:
   `python app.py`

5. Abra o navegador e acesse:
   `http://127.0.0.1:5000`

Qualidade do projeto
O projeto utiliza testes automatizados com Pytest para verificar o funcionamento das funcionalidades principais. O GitHub Actions executa os testes automaticamente quando novas alterações são enviadas ao repositório.

## Testes automatizados implementados

O TaskFlow possui 8 testes automatizados utilizando Pytest:

1. Verificação da página inicial.
2. Cadastro de tarefas.
3. Validação de título obrigatório.
4. Atualização do status.
5. Exclusão de tarefas.
6. Verificação do status inicial.
7. Rejeição de status inválido.
8. Armazenamento da descrição da tarefa.

Todos os 8 testes foram executados com sucesso utilizando o comando `python -m pytest -v`.