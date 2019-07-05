# ProcessaAutomato
Programa em python para interpretar automatos com pilha

Explicação sobre a compilação do Código: 

Primeiramente é necessário que o arquivo que contém o automato estejam no mesmo diretório do código fonte e do executável do programa.
Para a utilização do arquivo do automato definimos um nome padrão - "exemplodeautomato.txt" porém caso o arquivo não exista no diretório, o usuario deve digitar o nome do arquivo, em extensão '.txt'
Para reconhecimento do arquivo, utilizamos uma biblioteca chamada "os.path,que, basicamente, verifica se o arquivo existe ou não.
o Codigo foi compilado com o python "3.6.1" pois é a versão que aceita a formatação de alguns prints e outras funções.

O programa foi feito de forma recursivo e percorre todas transições possiveis para um estado, caso a palavra seja aceita, o programa mostra a mensagem "LINHA DE PROCESSAMENTO ACEITA", porém continua testando as outras linhas de processamento possíveis, mesmo assim, ao final de todas as linhas de processamento ele printa se a palavra foi aceita ou não.
