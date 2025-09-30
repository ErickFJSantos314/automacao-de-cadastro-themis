# importações

import pandas as pd
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

# ler planilha

dadoscadastro = pd.read_excel(r"C:\Users\erick\OneDrive\Área de Trabalho\automacaodecadastro\cadastrocompleto.xlsx")
print(dadoscadastro)

# abrir e logar

driver = webdriver.Edge()
wait = WebDriverWait(driver, 2)
driver.get ("https://******************************") #Domínio privado oculto
login = driver.find_element(By.ID, "login")
senha = driver.find_element(By.ID, "senha") #login oculto informações sensíveis
acessar = driver.find_element(By.ID, "btnLogin")
acessar.click()

# ir até processos

time.sleep(5)
acprocessos = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Processos")))
acprocessos.click()

#adicionar processo

adcprocessos = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conteudo"]/div[4]/container/div[1]/div[1]/div/a')))
adcprocessos.click()

#Banco master

dropdownbancomaster = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="conteudo"]/div[4]/container/div[1]/div[1]/div/ul/li[5]/a')))
dropdownbancomaster.click()

# dados para cadastro

for index, row in dadoscadastro.iterrows():
    advgint = row["ADVGINTERESSADO"] 
    observacao = row["OBSERVAÇÃO"]
    liticonsorcio = row["LITICONSORCIO"]
    partecontraria = row["PARTECONTRARIA"] 
    acao = row["ACAO"]
    objeto = row["OBJETO"]
    rito = row["RITO"]
    numerovara = row["NUMEROVARA"]
    vara = row["VARA"]
    foro = row["FORO"]
    processo = row["NUMEROINICIAL"]
    data = row["DATADEDISTRIBUICAO"]
    valor = row["VALORDACAUSA"]
    advcontra = row["ADVGCONTRA"]

    #cliente

    cliente = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="s2id_processoCliente"]/a')))
    cliente.click()
    cliente.send_keys('Banco')
    selecttoresult = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-result-label')))
    selecttoresult.click()

    #ADVG INTERESSADO

    advi = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2id_processoAdvogado"]/a')))
    advi.click()
    advi.send_keys(advgint)
    selecttoresult = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-result-label')))
    selecttoresult.click()
    
    #Observação

    obs = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoObservacao"]')))
    obs.click()
    obs.clear()
    obs.send_keys(observacao)

    #pedido liminar

    pliminar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoAlteravel1"]')))
    pliminar.clear()
    pliminar.send_keys("-")

    #liti

    liti = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoAlteravel2"]')))
    driver.execute_script("arguments[0].scrollIntoView();", liti)
    liti.clear()
    liti.send_keys(liticonsorcio)
    

    #reu

    reu = wait.until(EC.presence_of_element_located((By.ID, "processoPosicaoParteInteressada")))
    reu.send_keys("Reu")

    #parte contrária

    partecont = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div[4]/div[2]/section[2]/div/section/div[1]/form[1]/div[6]/div[3]/div/div[1]/div[1]/div/a')))
    partecont.click()
    partecont.send_keys(partecontraria)
    selecttoresult = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-result-label')))
    selecttoresult.click()
    time.sleep(1)

    #ação

    acc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoAcao"]')))
    acc.send_keys(acao)

    # objeto

    obj = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoObjeto"]')))
    driver.execute_script("arguments[0].scrollIntoView();", obj)
    obj.clear()
    obj.send_keys(objeto)

    #rito

    rit = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoRito"]')))
    rit.send_keys(rito)
    
    #instancia

    instancia = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoInstancia"]')))
    driver.execute_script("arguments[0].scrollIntoView();", instancia)
    instancia.send_keys('1ª Inst.')

    # fase

    fase = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoFase"]')))
    driver.execute_script("arguments[0].scrollIntoView();", fase)
    fase.send_keys('Inicial')

    # Número da vara

    varanumero = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoVara"]')))
    varanumero.send_keys(numerovara)
    varanumero.send_keys(Keys.BACKSPACE)

    #junta

    junta = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoSubdivisaoForo"]')))
    junta.send_keys(vara)

    #foro
    
    foroo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2id_processoForo"]/a')))
    driver.execute_script("arguments[0].scrollIntoView();", foroo)
    foroo.click()
    textoforo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2id_autogen11_search"]')))
    textoforo.send_keys(foro)
    time.sleep(4) # Pausa para as sugestões de foro carregarem
    
    #numero inicial

    numeroprocesso = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoNumero"]')))
    numeroprocesso.clear()
    for caractere in str(processo):
        numeroprocesso.send_keys(caractere)
        time.sleep(0.1)

    #data

    distribuicao = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dp2"]')))
    distribuicao.click()
    distribuicao.clear()
    for caractere in str(data):
        distribuicao.send_keys(caractere)
        time.sleep(0.1)
    numeroprocesso.click()



    valordacausa = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="processoValorCausaFormatado"]')))
    valordacausa.clear()
    for caractere in str(valor):
        valordacausa.send_keys(caractere)
        time.sleep(0.1)

    time.sleep(2)
    #advg.contra

    time.sleep(0.5)


    #advg.contra

    advgcontra_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2id_processoAdvogadoContra"]/a')))
    advgcontra_dropdown.click()
    time.sleep(0.5) 

    advgcontratexto = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2id_autogen12_search"]')))
    advgcontratexto.send_keys(str(advcontra))

    time.sleep(1.5)

    try:
        select2_result_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-result-label')))
        select2_result_label.click()
        print(f"Advogado '{advcontra}' selecionado via sugestão.")
        
    except TimeoutException:
        try:

            no_results_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-no-results" and contains(text(), "Nenhum resultado encontrado")]')))
            

            print(f"Nenhum resultado encontrado para o advogado '{advcontra}'. Adicionando novo...")
            

            advgcontratexto.send_keys(Keys.ESCAPE)
            time.sleep(0.5)


            try:
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#select2-drop')))
                wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'select2-drop-mask')))
                print("Dropdown do Select2 fechado antes de clicar em 'Adicionar Novo Advogado'.")
            except TimeoutException:
                print("Máscara/dropdown do Select2 não desapareceu a tempo. Tentando clique no 'Adicionar Novo Advogado' via JavaScript como fallback.")


            adcadv = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="adicionarNAdvogadoContra"]')))
            

            try:
                adcadv.click()
                print("Clicado em 'Adicionar Novo Advogado' normalmente.")
            except ElementClickInterceptedException:
                print("Clique em 'Adicionar Novo Advogado' interceptado. Tentando via JavaScript.")
                driver.execute_script("arguments[0].click();", adcadv)
                print("Clicado em 'Adicionar Novo Advogado' via JavaScript.")


            nomeadvcontra = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nomePessoa"]')))
            nomeadvcontra.send_keys(str(advcontra))
            time.sleep(0.1)
            
            salvarpessoa = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnSubmitProcessoPessoaSalva"]')))
            salvarpessoa.click()
            time.sleep(2.5) 
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'select2-drop-mask'))) 
            print(f"Novo advogado '{advcontra}' adicionado e selecionado.")
            
        except TimeoutException:
            print(f"Timeout: Nenhuma sugestão ou 'Nenhum resultado encontrado' para '{advcontra}' em tempo hábil. Prosseguindo ou tentando ENTER como fallback.")

            advgcontratexto.send_keys(Keys.ENTER)
            time.sleep(1) 
            try:
                 wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#select2-drop')))
                 print(f"Advogado '{advcontra}' possivelmente selecionado após ENTER (fallback).")
            except TimeoutException:
                 print("Dropdown ainda visível após ENTER. Advogado pode não ter sido selecionado ou erro não tratado.")


    salvar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnSubmitProcesso"]')))
    driver.execute_script("arguments[0].scrollIntoView();", salvar)
    salvar.click()

    time.sleep(3)


    try:
        verificador = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cabecalho"]/h3/span')))
        print(f"Processo cadastrado com sucesso. Título da página: {verificador.text}")
    except TimeoutException:
        print("Erro: Não foi possível verificar o cadastro do processo. Página pode não ter carregado como esperado.")
    driver.back()
    time.sleep(2)
