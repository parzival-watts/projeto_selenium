# Sistema simples criado para entrar no site da Binary e pegar alguns dados
#criado por PHILLIP DYLAN

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# seu email e sua senha da binary para poder acessar o site
email = input("Digite seu email da Binary: \n\t")
senha = input("Digite sua senha da binary: \n\t")

# se teste igual a True vai fazer login e pegar os dados da conta de demonstração
# se teste igual a False vai fazer login e pegar os dados da conta real
teste = True


virgula = ','
ponto = '.'
banca = 0
atualizar = True
atua = 0
var0 = 0
var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
var7 = 0
var8 = 0
var9 = 0
cont = 0

pvar0 = 0
pvar1 = 0
pvar2 = 0
pvar3 = 0
pvar4 = 0
pvar5 = 0
pvar6 = 0
pvar7 = 0
pvar8 = 0
pvar9 = 0
pcont = 0

# parte responsavel por entrar no site da binary
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.binary.com/pt/home.html")
    sleep(2)

    driver.find_element(By.ID, "btn_login").click()
    print('\033[32m Pagina Acessada Com Sucesso\033[m ')
    sleep(2)

    driver.find_element(By.ID, "txtEmail").send_keys(email)
    driver.find_element(By.ID, "txtPass").send_keys(senha + Keys.RETURN)
    sleep(5)
# Parte responsavel por mudar o tipo de conta para real ou demosntração
    if teste:
        driver.find_element(By.CLASS_NAME, "main-account").click()
        sleep(2)
        ir = driver.find_element(By.CLASS_NAME, "login-id-list").click()
        sleep(2)

# responsavel por pegar o saldo da conta e transformar em uma forma qua nao da erro na hora que for mostrar ao usuario
    def saldo():
        global virgula, banca
        global ponto
        a = driver.find_element(By.CLASS_NAME, "topMenuBalance")
        b = str(a.text)
        c = b.split(' ')
        d = str(c[0])
        if ponto in d:
            e = d.split('.')
            if e[1]:
                f = str(e[0] + e[1])
            elif e[2]:
                f = str(e[0] + e[1] + e[2])
            elif e[0]:
                f = str(e[0])

        else:
            f = str(d)
        if virgula in f:
            r = f.split(',')
            banca = float(r[0] + '.' + r[1])
        print(banca)


    saldo()


    driver.find_element(By.ID, "underlying_component").click()
    sleep(2)
    element = driver.find_element(By.ID, '1HZ10V').click()
    sleep(3)

# parte responsavel por pegar os dados do preço atual e converter para mostar o ultimo numero
    def preço_atual():

        preço = driver.find_element(By.ID, 'spot')
        preço1 = str(preço.text)
        preço2 = preço1.split(',')
        preço3 = str(preço2[0] + preço2[1])
        preço3_1 = preço3.split('.')
        preço3_2 = int(preço3_1[1])
        # preço4 = float(preço3)
        # preço5 = str(preço4)
        # preço6 = preço5.split('.')
        # preço7 = int(preço6[1])
        preço3_3_1 = str(preço3_2)
        preço3_3 = len(preço3_3_1)
        if preço3_3 == 2:
            preço3_4 = int(preço3_3_1[1])
        elif preço3_3 == 1:
            preço3_4 = int(preço3_3_1[0])
        elif preço3_3 == 3:
            preço3_4 = int(preço3_3_1[2])
        return preço3_4

# responsavel por mostrar ao usuario os dados dos ultimos digitos
    def mostar():
        global var0,var1,var2,var3,var4,var5,var6,var7,var8,var9
        os.system("cls")
        print(f'''
        0 - {var0} - {pvar0:.2f}%
        1 - {var1} - {pvar1:.2f}%
        2 - {var2} - {pvar2:.2f}%
        3 - {var3} - {pvar3:.2f}%
        4 - {var4} - {pvar4:.2f}%
        5 - {var5} - {pvar5:.2f}%
        6 - {var6} - {pvar6:.2f}%
        7 - {var7} - {pvar7:.2f}%
        8 - {var8} - {pvar8:.2f}%
        9 - {var9} - {pvar9:.2f}%
        ''')

# atualiza os documentos para escrever o ultimo digito no documento dados
    while atualizar:
        # saldo()
        ultimo_digito = preço_atual()
        def escrever():
            global ultimo_digito
            dados_binary = open('dados.txt','w')
            dados_binary.write(f'{ultimo_digito}\n')
            dados_binary.close()
        escrever()
        def ler():
            with open('dados.txt','r') as dados_binary:
                for ultimo_digito in dados_binary:
                    print(ultimo_digito)
        ler()


        print("Ultimo digito: ",ultimo_digito)
        valores = preço_atual()
        if valores == 0:
            var0 = var0 + 1
            cont = cont + 1
        elif valores == 1:
            var1 = var1 + 1
            cont = cont + 1
        elif valores == 2:
            var2 = var2 + 1
            cont = cont + 1
        elif valores == 3:
            var3 = var3 + 1
            cont = cont + 1
        elif valores == 4:
            var4 = var4 + 1
            cont = cont + 1
        elif valores == 5:
            var5 = var5 + 1
            cont = cont + 1
        elif valores == 6:
            var6 = var6 + 1
            cont = cont + 1
        elif valores == 7:
            var7 = var7 + 1
            cont = cont + 1
        elif valores == 8:
            var8 = var8 + 1
            cont = cont + 1
        elif valores == 9:
            var9 = var9 + 1
            cont = cont + 1
        pvar0 = (var0 / cont) * 100
        pvar1 = (var1 / cont) * 100
        pvar2 = (var2 / cont) * 100
        pvar3 = (var3 / cont) * 100
        pvar4 = (var4 / cont) * 100
        pvar5 = (var5 / cont) * 100
        pvar6 = (var6 / cont) * 100
        pvar7 = (var7 / cont) * 100
        pvar8 = (var8 / cont) * 100
        pvar9 = (var9 / cont) * 100
        atua = atua + 1
        if (var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9) >= 200:
            cont = 0
            var0 = 0
            var1 = 0
            var2 = 0
            var3 = 0
            var4 = 0
            var5 = 0
            var6 = 0
            var7 = 0
            var8 = 0
            var9 = 0

        mostar()
        sleep(1)