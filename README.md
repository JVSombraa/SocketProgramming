# Programação de sockets

O trabalho apresenta 3 arquivos principais, sendo eles `app.py` responsável por executar o sistema, `client.py` responsável pela parte do cliente e `server.py` sendo o servidor da aplicação.
O servidor trabalha em **LocalHost** e pode ser executado em Windows ou Linux.

## Instalação

Para iniciar a aplicação, é apenas necessário a instalação do **python**.
Todas as bibliotecas utilizadas já estão inclusas no python, então não é necessário instalar nenhuma dependência externa.

## Execução

Existem 2 formas para se iniciar a aplicação.

> Lembre-se que o servidor deve sempre ser executado antes do cliente

 **1.** A primeira forma de executar a aplicação é a mais simples, basta apenas inicializar o arquivo `app.py` da seguinte forma:
 
	python app.py
    
 - Após a execução será aberto 2 terminais, um com a visão do servidor e outra com a do cliente.

**2.** A segunda forma de iniciar a aplicação é executar os terminais manualmente. Para isso é necessário abrir 2 terminais separados, vamos chama-los de **Servidor** e **Cliente**.

 - No terminal **Servidor** deve ser inserido os seguintes comandos:

	    cd components
	    python server.py
 - Com isso o servidor sera iniciado, o próximo passo é iniciar a aplicação **Cliente**, para isso no segundo terminal execute os comandos:

	    cd components
	    python client.py 



### Encerrando a aplicação
Para finalizar a aplicação basta pressionar o comando **ctrl + c** no terminal **Cliente** que ele será encerrado.
Enquanto para terminar o **servidor** basta fechar o terminal que o executa.

> Observe que, caso o servidor seja finalizado antes do cliente, a tentativa de conexão do cliente com o servidor resultará em erro, uma vez que a conexão não será bem-sucedida.

# Explicando a aplicação
Aqui será fornecida uma descrição detalhada do funcionamento dos três arquivos principais essenciais para o correto funcionamento da aplicação.

## Arquivo `app.py`
A função desse arquivo é inicializar o servidor e o cliente de forma simultânea.
 - Inicialmente é identificado o sistema operacional que o usuário está usando através da biblioteca *plataform*
 
 - Após a identificação do sistema, é executado 2 comandos no terminal, intercalados com um *time.sleep* de 1 segundo, o `time.sleep` é utilizado para que o servidor seja completamente iniciado antes do cliente.
 
 - Os comandos do terminal realizam a execução dos arquivos `server.py` e `client.py`. É utilizado a biblioteca **subprocess** para que seja possível executar os terminais simultaneamente.

## Arquivo `server.py`

Este arquivo é responsável por iniciar o servidor, receber e enviar mensagens ao cliente.

 - Inicialmente são importadas todas as bibliotecas necessárias, sendo elas: `socket`, `random`, `string` e `time`.
 
 - Após isso é informado o endereço **"Localhost"** e a porta **5000** onde o servidor trabalhará e o mesmo é iniciado.
 
 - Inicia-se um laço de repetição infinito e o sistema aguarda uma mensagem do cliente.
 
 - Quando a mensagem é recebida (em formato de *string*), é verificado se a mensagem tem mais de 10 caracteres.
 
 - Em caso positivo, será criada e devolvida ao cliente uma nova *string* composta por letras aleatórias com o mesmo comprimento da *string* de entrada.
 
 - Caso contrário, uma verificação é realizada para determinar se o número é divisível por 2, permitindo assim a identificação e o retorno adequado da informação de que o número é **Par** ou **Ímpar** ao cliente.
 
 - O servidor permanece em loop infinito aguardando a conexão de novos clientes. Quando uma conexão é encerrada, o servidor espera por um segundo antes de tentar aceitar novas conexões.

## Arquivo `cliente.py`

Esse arquivo é responsável por implementar um cliente que se conecta a um servidor por meio de um socket.

 - Primeiramente, são importadas as bibliotecas necessárias: `socket`, `random`, `time`, `signal` e `sys`.

 - Em seguida, é definido um endereço IP e porta para conexão do cliente ao servidor, nesse caso, o `localhost` na porta `5000`.

 - A função `signal_end` é definida para tratar o sinal de interrupção `SIGINT` (chamada quando o usuário pressiona `Ctrl+C` no terminal), encerrando a conexão do cliente com o servidor e finalizando a execução do programa.

 - Dentro do loop `while True`, é criado um objeto do tipo `socket` usando as constantes `AF_INET` e `SOCK_STREAM` para indicar que se trata de um socket TCP.

 - Em seguida, é gerado dois números inteiros aleatórios, um entre 1 e 30 para definir quantas casas o número poderá ter e o outro para gerar o número com esse número de casas, por fim é convertido em uma *string*. Esse número é enviado ao servidor por meio do método `send()` do objeto `socket`.

 - O cliente aguarda a resposta do servidor por meio do método `recv()`, que recebe no máximo 1024 bytes de dados do servidor. A mensagem recebida é decodificada para uma string e armazenada na variável `resp`.

 - Em seguida, a conexão é fechada e o ciclo se repete novamente, gerando um novo número aleatório e enviando-o para o servidor.

 - Antes de iniciar um novo ciclo, é feita uma contagem de ciclos e uma espera de 10 segundos usando a função `time.sleep()`.