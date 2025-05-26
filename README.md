# Testes Automatizados de Interface com Selenium

## Alunos
- Gabriel Henrique Evaristo  
- Igor Campos Pereira  
- Higor Batista de Oliveira  
- Pedro Henrique Cruz Vilas Boas  

**Turma:** Tecnologia em Análise e Desenvolvimento de Sistemas

---

## Descrição

Este projeto tem como objetivo demonstrar a aplicação de testes automatizados de interface utilizando a linguagem **Python** e a ferramenta **Selenium** para criação e registro de interações na interface gráfica do usuário.

Como estudo de caso, foi utilizado o site de demonstração **SauceDemo**, que simula uma plataforma de e-commerce com fluxos típicos de navegação:

- Autenticação de usuários
- Navegação por catálogo de produtos
- Gerenciamento de carrinho de compras
- Finalização de pedidos

Foram realizados dois cenários principais de teste:

1. **Simulação da autenticação de usuário e navegação pelo catálogo**
2. **Execução completa do fluxo de adição de produto ao carrinho com finalização do checkout**

A automação visa validar o comportamento da interface sob diferentes condições de uso, contribuindo para a **garantia de qualidade** do sistema.

---

## Casos de Teste

### 1. Autenticação de Usuário no Sistema

**Objetivo:**  
Verificar se o sistema permite autenticar corretamente um usuário com credenciais válidas, redirecionando para o catálogo de produtos.

**Pré-condição:**  
A página inicial de login do site SauceDemo deve estar acessível.

**Passos:**

1. Acessar a página inicial de login do SauceDemo.
2. Inserir o nome de usuário válido: `standard_user`.
3. Inserir a senha correspondente: `secret_sauce`.
4. Submeter o formulário de login.

**Tabela de Decisão:**

| Cenário                              | Usuário         | Senha           | Esperado                               |
|--------------------------------------|-----------------|-----------------|----------------------------------------|
| Login válido                        | standard_user   | secret_sauce    | Redirecionar para catálogo de produtos |
| Login inválido - usuário incorreto  | invalid_user    | secret_sauce    | Exibir mensagem de erro                |
| Login inválido - senha incorreta    | standard_user   | invalid_password| Exibir mensagem de erro                |
| Login inválido - campos vazios      | -               | -               | Exibir mensagem de erro                |

**Resultado esperado:**  
O sistema deve redirecionar o usuário autenticado para a página de catálogo de produtos, indicando que o login foi realizado com sucesso.

---

### 2. Adição de Produto ao Carrinho e Finalização de Compra

**Objetivo:**  
Verificar se o sistema permite ao usuário adicionar um produto ao carrinho de compras e finalizar a compra.

**Pré-condição:**  
O usuário deve estar autenticado e ter acesso ao catálogo de produtos.

**Passos:**

1. Acessar o catálogo de produtos.
2. Selecionar um produto qualquer.
3. Clicar no botão **"Add to cart"**.
4. Acessar o carrinho de compras pelo ícone no topo da página.
5. Iniciar o processo de checkout.
6. Preencher as informações obrigatórias.
7. Prosseguir para o resumo do pedido.
8. Finalizar a compra clicando em **"Finish"**.

**Tabela de Decisão:**

| Cenário                               | Produto selecionado | Informações de checkout preenchidas | Compra finalizada com sucesso |
|---------------------------------------|---------------------|-------------------------------------|-------------------------------|
| Produto selecionado, dados OK        | Sim                 | Sim                                 | Sim                           |
| Produto não selecionado              | Não                 | Sim                                 | Não                           |
| Dados de checkout incompletos        | Sim                 | Não                                 | Não                           |
| Nenhum produto e dados faltando      | Não                 | Não                                 | Não                           |

**Resultado esperado:**  
O sistema deve exibir uma mensagem de confirmação indicando que o pedido foi finalizado com sucesso.

---

### 3. Remoção de Produto do Carrinho de Compras

**Objetivo:**  
Verificar se o sistema permite ao usuário remover um produto previamente adicionado ao carrinho de compras.

**Pré-condição:**  
O usuário deve estar autenticado, ter acessado o catálogo de produtos e adicionado pelo menos um item ao carrinho.

**Passos:**

1. Acessar o catálogo de produtos.
2. Adicionar um produto ao carrinho clicando em **"Add to cart"**.
3. Acessar o carrinho de compras pelo ícone no topo da página.
4. Clicar no botão **"Remove"** ao lado do produto selecionado.

**Tabela de Decisão:**

| Cenário                             | Produto no carrinho | Produto removido | Carrinho vazio |
|--------------------------------------|---------------------|------------------|----------------|
| Produto presente                    | Sim                 | Sim              | Sim            |
| Produto não presente                | Não                 | Não              | Sim            |
| Produto presente, não removido      | Sim                 | Não              | Não            |

**Resultado esperado:**  
O produto deve ser removido do carrinho e o sistema deve atualizar a visualização, exibindo a quantidade correta de itens.

---

### 4. Logout do Sistema

**Objetivo:**  
Verificar se o sistema permite que o usuário efetue logout de forma adequada, redirecionando para a página inicial de login.

**Pré-condição:**  
O usuário deve estar autenticado no sistema e visualizar o catálogo de produtos.

**Passos:**

1. Acessar o menu lateral clicando no ícone de **"hambúrguer"** no canto superior esquerdo.
2. Clicar na opção **"Logout"**.

**Tabela de Decisão:**

| Cenário                             | Usuário autenticado | Logout acionado | Redirecionado para login |
|--------------------------------------|---------------------|-----------------|--------------------------|
| Usuário autenticado, logout realizado | Sim                 | Sim             | Sim                      |
| Usuário autenticado, logout não realizado | Sim             | Não             | Não                      |
| Usuário não autenticado              | Não                 | Não             | Não                      |

**Resultado esperado:**  
O sistema deve redirecionar o usuário para a página inicial de login após o logout ser acionado.

---

## Tecnologias Utilizadas

- **Python**  
- **Selenium**  
- **Site de testes:** [SauceDemo](https://www.saucedemo.com/)

---

## Licença

Este projeto é de caráter acadêmico, desenvolvido para a disciplina de **Testes Automatizados de Software**.

