# Processa Automato
Programa em python para interpretar automatos com pilha

Explicação sobre a compilação do Código: 

Primeiramente é necessário que o arquivo que contém o automato estejam no mesmo diretório do código fonte e do executável do programa.
Para a utilização do arquivo do automato definimos um nome padrão - "exemplodeautomato.txt" porém caso o arquivo não exista no diretório, o usuario deve digitar o nome do arquivo, em extensão '.txt'
Para reconhecimento do arquivo, utilizamos uma biblioteca chamada "os.path,que, basicamente, verifica se o arquivo existe ou não.
o Codigo foi compilado com o python "3.6.1" pois é a versão que aceita a formatação de alguns prints e outras funções.

O programa foi feito de forma recursivo e percorre todas transições possiveis para um estado, caso a palavra seja aceita, o programa mostra a mensagem "LINHA DE PROCESSAMENTO ACEITA", porém continua testando as outras linhas de processamento possíveis, mesmo assim, ao final de todas as linhas de processamento ele printa se a palavra foi aceita ou não.

# Process Automated
Python program to interpret stack automata

Explanation on compiling the Code:

Firstly, the file containing the automaton must be in the same directory as the program's source code and executable.
For the use of the automaton file we defined a default name - "exampleautomato.
txt" but if the file does not exist in the directory, the user must type the file name, in extension '.txt'
For file recognition, we use a library called "os.path, which basically checks whether the file exists or not.
Code was compiled with python "3.6.
1" because it is the version that accepts the formatting of some prints and other functions.

The program was done recursively and runs through all possible transitions to a state, if the word is accepted, the program shows the message "PROCESSING LINE ACCEPTED", but continues testing the other possible processing lines, even so,
at the end of all processing lines it prints whether the word was accepted or not.
