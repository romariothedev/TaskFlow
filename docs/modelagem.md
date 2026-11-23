\# Modelagem UML — TaskFlow



\## 1. Diagrama de casos de uso



O diagrama representa as principais funcionalidades disponíveis para o usuário do sistema TaskFlow.



```mermaid

flowchart LR

&#x20;   U\[Usuário]

&#x20;   A((Cadastrar tarefa))

&#x20;   B((Visualizar tarefas))

&#x20;   C((Alterar status))

&#x20;   D((Excluir tarefa))



&#x20;   U --- A

&#x20;   U --- B

&#x20;   U --- C

&#x20;   U --- D

```



\## 2. Diagrama de classes



O diagrama representa a estrutura principal da aplicação e os dados utilizados para gerenciar as tarefas.



```mermaid

classDiagram

&#x20;   class Task {

&#x20;       +int id

&#x20;       +string title

&#x20;       +string description

&#x20;       +string status

&#x20;   }



&#x20;   class Application {

&#x20;       +create\_task()

&#x20;       +list\_tasks()

&#x20;       +update\_status()

&#x20;       +delete\_task()

&#x20;   }



&#x20;   class Database {

&#x20;       +init\_db()

&#x20;       +get\_connection()

&#x20;   }



&#x20;   Application --> Task : gerencia

&#x20;   Application --> Database : utiliza

&#x20;   Database --> Task : armazena

```



\## 3. Importância da modelagem



A modelagem UML facilita a compreensão da estrutura e do funcionamento do sistema antes e durante o desenvolvimento.



Os diagramas ajudam a identificar funcionalidades, organizar responsabilidades e documentar a solução, tornando a manutenção e futuras melhorias mais simples.

