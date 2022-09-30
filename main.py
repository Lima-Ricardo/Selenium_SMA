from selenium import webdriver #Biblioteca de automação
from selenium.webdriver.common.by import By #Função utilizada pra achar os componentes html
from webdriver_manager.firefox import GeckoDriverManager #Biblioteca específica para quem vai utilizar o navegador firefox
from selenium.webdriver.firefox.service import Service #Identifica a versão do seu navegador e para o selenium funcionar corretamente
from selenium.webdriver.common.keys import Keys #Função do selenium que automatiza a entrada de caracteres
from bs4 import BeautifulSoup # Biblioteca que faz a coleta dos dados
from time import sleep # Usado para deixar o programa o mais humano possível evitando o banimento de ip
import csv # usado para gravar os resultados do scrape

#======================================================

#entrar com o navegador firefox

att = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=att)

print('- Passo 01 concluído.')

url = "https://admin.byinti.com/ticket/report/exported-reports"

driver.get(url)
sleep(3)
print('- Passo 1.1 concluído.')

#======================================================

# 1.2 Buscando o arquivo no sistema que contém a senha e o email do linkedin fake

# acessando um arquivo em txt que contém o email e a senha do linkedin fake
login = open("Credenciais.txt", encoding="utf-8")

# Alocando a leitura do txt em uma váriavel e utilizando o método .readlines()
line = login.readlines()

# Lendo a posicção[0] do meu txt que contém o email
email = line[0]

# Lendo a posição[1] do meu txt que contém o a senha
senha = line[1]

print('- Passo 1.2 concluído.')

#======================================================

# 1.3 Buscando pelo campo de email e fazendo a inserção

# Mandando o selenium buscar pelo campo de inserção de email com o método find_element()
field_email = driver.find_element(By.NAME,'LoginForm[email]')
sleep(4)

# Mandando o selenium inserir o email com método send_keys()
field_email.send_keys(email)
sleep(4)

print('- Passo 1.3 concluído.')

#======================================================

#1.4 Buscando pelo campo de senha e fazendo a inserção

# Mandando o selenium bucar pelo campo de inserção da senha senha com o método find_element()
field_password = driver.find_element(By.XPATH, '//*[@id="loginform-password"]')
sleep(2)

# Mandando o selenium inserir a senha no campo de senha  com o método .send_keys()
field_password.send_keys(senha)
sleep(3)

print('- Passo 1.4 concluído.')

#======================================================

# 1.5 Buscando pelo botão de login

# Mandando o selenium procurar pelo botão ENTRAR com o find_element(By.XPATH)
button_enter = driver.find_element(By.XPATH,'//*[@id="entrar"]')
sleep(3)

# Mandando o selenium clicar no botão entrar
button_enter.click()
sleep(3)


# Confirmando o logon após a inserção e a confirmação de email e senha.
button_confirm_log_on = driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li/a")
button_confirm_log_on.click()
sleep(3)
print('- Passo 1.5 concluído.')
#======================================================

#1.6 selecionando o campo dos dados
sleep(2)
# Acessando o botão home da homepage
home_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]/a")
home_button.click()

sleep(3)
# Acessando o botão pra download dos dados
report_download_button = driver.find_element(By.XPATH,'//*[@id="export"]')
report_download_button.click()

sleep(3)
# Acessando os dados para download
download_confirmed = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[1]/section[1]/div[2]/div/section/div/div/div[2]/div/div/div[2]/div/div/div/a[2]')
download_confirmed.click()

sleep(3)
# Fazendo o download
client_report = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[4]/td[5]/a[1]")
client_report.click()


print("Automação finalizada com sucesso!")