#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
estado_anterior = ""
NomeAutomato = "exemplodeautomato.txt"  #Buscando arquivo de nome padrão
while(not os.path.isfile(NomeAutomato)): #Verificando se o Arquivo existe
    print("Arquivo não encontrado")
    NomeAutomato = input("Digite o nome do arquivo (exetensão '.txt'): ")#Solicitando nome do arquivo para busca
print("Arquivo Encontrado")

def processaletra(estado_atual,estado_anterior, palavra, o, pilha):  
    pilha_aux = [i for i in pilha]
    boole = False
    boole2 = False
    k = len(pilha)
    print(f"\n|Estado atual: {estado_atual} | Pilha: {pilha}|")
    if o == len(palavra):
        for r in range (contadorTransicoes):  
          if Transicoes[r][0] == estado_atual and Transicoes[r][3] == EstadoFin[0] and Transicoes[r][1] == '?' and Transicoes[r][2] == '?': #Teste da Pilha Vazia
              print(f"Verificando da pilha vazia no estado {estado_atual}")
              if len(pilha) == 0:
                  print("==================================")
                  print("|| LINHA DE PROCESSAMENTO ACEITA||")
                  print("==================================")
                  return True
              else:
                  return False
    else:
        #print(f"Letra em processamento: {palavra[o]}")
        for x in range(contadorTransicoes):
            pilha = [i for i in pilha_aux]
            if (Transicoes[x][0]== estado_atual and Transicoes[x][1] == '-' and Transicoes[x][2] == '-') or (Transicoes[x][0] == estado_atual and Transicoes[x][1] == palavra[o]): #Verificando se o estado atual possivel para a letra tem processamento 
                print(f"Letra em processamento: {palavra[o]}")
                estado_novo = Transicoes [x][3]
                if Transicoes[x][2] != '-': #Leitura da Pilha
                    if len(pilha) != 0:
                        if Transicoes[x][2] == pilha[k - 1]:
                            if pilha != []: #Removendo Simbolo da Pilha
                                print(f"Removendo da Pilha: {pilha[k-1]}")
                                pilha.pop()
                        else:
                            continue
                    else:
                        return False
                if Transicoes[x][4] != '-': #Escrevendo Simbolo na Pilha
                    for z in Transicoes[x][4]:
                        print(f"Escrevendo na Pilha: {z}")
                        pilha.append(z)
                if Transicoes[x][1] != '-': #Trocando o estado atual e transições vazias
                    print(f"\n|{estado_atual} -> {estado_novo}|\n")
                    estado_anterior = estado_atual
                    boole = processaletra(estado_novo,estado_anterior, palavra, o+1, pilha) #Retorna 'true' caso exista um processamento possivel para o estado atual
                else:
                    if (estado_anterior != estado_novo): #Trocando o estado anterior
                      estado_anterior = estado_atual
                      boole = processaletra(estado_novo,estado_anterior, palavra, o, pilha) #O boole guarda o valor de retorno do processamento da palavra toda
                    else: 
                      continue  
                if boole:
                    boole2 = True #O boole2 é alterado para True caso uma das linhas possiveis de processamento retorne a True
                    '''esse parametro foi criado por que caso uma das linhas possiveis de processamento retorne a True
                    e logo apos uma outra linha de processamento retorne a false, é possivel que mesmo uma palavra aceita seja recusada pelo automato
                    por isso utilizamos o boole2'''
            else:
                continue
        if boole2: #Verificando se a Palavra foi aceita ou não
            return True
        else:
            return False

#Ordem de entrada de dados (Globais)
Simbolos = []
Estados = []
EstadoIn = []
EstadoFin = []
Transicoes = []
SimbolosPilha = []
pilhaa = []

def leAutomato(NomeAutomato): #Formatação e leitura de dados do arquivo
  arq = open(NomeAutomato, "r")
  text = arq.readline()
  i = 0
  n = 0
  
  while i < len(text):
      if n < 1 and text[i] == "{":  # Simbolos para processamento
          i += 1
          while text[i] != "}":
              if text[i] != "," and text[i] != " ":
                  Simbolos.append(text[i])
              i += 1
          n += 1

      elif n < 2 and text[i] == "{":  # Estados para processamento
          i += 1
          while text[i] != "}" and text[i + 1] != "}":
              if text[i] != "," and text[i] != " " and text[i + 1] != "," and text[i + 1] != " ":
                  Estados.append(text[i] + text[i + 1])
              i += 1
          n += 1

      elif n < 3 and n > 1 and text[i] == ",":  # Transições
          i += 1
          while text[i] != ",":
              i += 1
          n += 1

      elif n < 4 and n > 2:  # Estado Inicial
          i += 1
          while text[i] != "{":
              if text[i] != "," and text[i] != " " and text[i + 1] != "," and text[i + 1] != " ":
                  EstadoIn.append(text[i] + text[i + 1])
              i += 1
          n += 1

      elif n < 5 and n > 3:  # Estados Finais
          while text[i] != "}":
              if text[i] != "," and text[i] != " " and text[i + 1] != "," and text[i + 1] != "}":
                  EstadoFin.append(text[i] + text[i + 1])
              i += 1
          n += 1
          i += 1

      elif n < 6 and n > 4 and text[i] == "{":  # SimbolosPilha
          i += 1
          while text[i] != "}":
              if text[i] != "," and text[i] != " ":
                  SimbolosPilha.append(text[i])
              i += 1
          n += 1
      i += 1

  for i in arq: #Formatação das regras de transição
      i = i.splitlines()
      i = str(i).split(', ')
      i[0] = str(i[0]).split("'")
      del(i[0][0])
      i[0] = str(i[0][0])
      i[4] = str(i[4]).split("'")
      del(i[4][1])
      i[4] = str(i[4][0])
      Transicoes.append(i)
  str(EstadoIn).split("'")
  str(EstadoIn).split("'")

  arq.close()

arq = open(NomeAutomato,"r") #Contador de Transições (Global)
contadorTransicoes=0
for x in arq:
    contadorTransicoes +=1
contadorTransicoes -=1
arq.close()

def mostraDados(): #Mostra os dados do automato
  print('Alfabeto do automato:')
  print(Simbolos)
  print('Estados do automato:')
  print(Estados)
  print('Símbolo de transições:')
  print(Transicoes)
  print('Estado iniciais:')
  print(EstadoIn)
  print('Estado finais:')
  print(EstadoFin)
  print('Simbolos da pilha:')
  print(SimbolosPilha)
  print('Número de Transicoes:')
  print(contadorTransicoes)
  
leAutomato(NomeAutomato)
#mostraDados()
palavra = input("Digite a palavra a ser processada: ")
print(f"\nPalavra = {palavra}\n")
x = 0

#Verifica o processamento da palavra
if processaletra(EstadoIn[0],estado_anterior, palavra, x, pilhaa):
    print("====================")
    print("|| PALAVRA ACEITA ||")
    print("====================")
else:
    print("========================")
    print("|| PALAVRA NAO ACEITA ||")
    print("========================")
