# Automação de Cadastro de Processos no Themis (Aurum)

Este projeto contém um script de automação desenvolvido em Python utilizando a biblioteca Selenium para realizar o cadastro **completo de processos** no sistema **Themis**, que faz parte da plataforma **Aurum**.

Esta automação foi **projetada para meu uso pessoal** com meus próprios modelos de dados, visando agilizar o processo de inserção de múltiplos registros de processos. Ela extrai os dados de uma planilha Excel e preenche os diversos campos do formulário web do Themis.

---

## 🚀 Funcionalidades Principais

* **Login Automatizado**: Realiza o login no sistema Themis utilizando credenciais configuradas externamente.
* **Navegação no Sistema**: Acessa a seção de "Processos" e o formulário de "Adicionar Processo" (especificamente o "Banco Master").
* **Preenchimento Abrangente**: Preenche uma vasta gama de campos do processo, incluindo:
    * Cliente (seleção "Banco")
    * Advogado Interessado
    * Observação
    * Pedido Liminar
    * Litisconsórcio
    * Posição da Parte Interessada (Réu)
    * Parte Contrária
    * Ação
    * Objeto
    * Rito
    * Instância
    * Fase
    * Número da Vara
    * Junta
    * Foro
    * Número Inicial do Processo
    * Data de Distribuição
    * Valor da Causa
    * Advogado Contrário
* **Interação com Dropdowns/Buscas (Select2)**: Lida com campos dinâmicos que exigem clique, digitação em campo de busca interno e seleção de resultados, como "Cliente", "Advogado Interessado", "Parte Contrária", "Foro" e "Advogado Contrário".
* **Tratamento de Campos com Máscara**: Implementa estratégias robustas para preencher campos com máscaras (ex: "Valor da Causa"), injetando o valor via JavaScript e disparando eventos para garantir a formatação correta, mesmo em casos de "zeros finais" problemáticos.
* **Tratamento Condicional de Advogado Contrário**:
    * Verifica se o Advogado Contrário já existe na base do Themis.
    * Se existir, seleciona-o.
    * **Se não existir ("Nenhum resultado encontrado")**, a automação clica no botão "Adicionar Novo Advogado Contrário", preenche o formulário de cadastro de pessoa (nome) e salva o novo registro, antes de retornar ao formulário do processo.
    * Inclui um fallback (`Keys.ENTER`) caso a lógica de identificação de resultados ou "nenhum resultado" falhe.
* **Verificação Pós-Cadastro**: Após tentar salvar o processo, o script tenta verificar se a página foi redirecionada para a tela de detalhes do processo (indicando sucesso), e então retorna à tela de adicionar processo para o próximo item da planilha.

---

## 🎯 Campo 'Foro': Detalhes da Implementação

Durante o desenvolvimento, foi notada uma particularidade no preenchimento do campo de **Foro**. No meu cenário, os valores para o foro (e potencialmente para outros campos do tipo Select2 que dependem de uma seleção a partir de sugestões de busca) **não seguem um padrão que permita uma seleção totalmente automatizada a partir de uma lista de sugestões com clique**.

Por este motivo, o código para o campo de Foro preenche o campo de busca interno (`textoforo.send_keys(foro)`), mas não inclui uma lógica explícita para *selecionar* um resultado específico (clicar em `select2-result-label` ou enviar `Keys.ENTER` para o campo de busca). Ele apenas aguarda um tempo (`time.sleep(4)`) após a digitação, pois a seleção automática não era viável para o meu caso de uso.

---

## ⚙️ Pré-requisitos


* **Python 3.x**
* **Microsoft Edge**
* **msedgedriver** (ou o WebDriver correspondente ao seu navegador, compatível com a versão do seu navegador, adicionado ao PATH do sistema)

### Bibliotecas Python

Instale as bibliotecas Python necessárias usando pip:

```bash
pip install pandas selenium openpyxl
``` 

### 📊 Estrutura da Planilha (cadastrocompleto.xlsx)

A planilha de entrada deve conter as seguintes colunas (os nomes dos títulos das colunas devem ser EXATOS):

* ADVGINTERESSADO
* OBSERVAÇÃO
* LITICONSORCIO
* PARTECONTRARIA
* ACAO
* OBJETO
* RITO
* NUMEROVARA
* VARA
* FORO
* NUMEROINICIAL
* DATADEDISTRIBUICAO
* VALORDACAUSA
* ADVGCONTRA

### ⚠️ Observações e Tratamento de Erros

* Tempos de Espera (time.sleep e WebDriverWait): Os tempos de espera foram ajustados para as condições de rede e carregamento do sistema Themis. Pode ser necessário ajustar os valores de time.sleep() ou aumentar o tempo limite de WebDriverWait se você enfrentar TimeoutExceptions ou interações falhas.

* XPATHs e IDs: Os seletores de elementos (By.XPATH, By.ID, By.CLASS_NAME) são específicos para a estrutura HTML do Themis no momento do desenvolvimento. Atualizações futuras do sistema Themis podem alterar esses seletores, exigindo que você os inspecione e atualize no script.

* Valor da Causa: A lógica de preenchimento do "Valor da Causa" utiliza injeção de JavaScript e disparo de eventos para contornar máscaras de entrada problemáticas e garantir a formatação correta (ex: XXX,YY).

* Tratamento de Erros de Advogado Contrário: O script tenta selecionar um advogado existente; se não encontrar, tenta adicionar um novo. Em caso de falha completa ou timeout, ele tenta pressionar ENTER como fallback.

* Verificação Pós-Cadastro: O script tenta verificar se o processo foi cadastrado com sucesso e retorna à página anterior para o próximo item da planilha. Se a página não carregar como esperado, um erro será impresso.
