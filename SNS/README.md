# Aula 05.3 - Lambda

1. No terminal do IDE criado no cloud9 execute o comando `cd ~/environment/aula-serverless-mob/05\ -\ SNS/03\ -\ Lambda/ ` para entrar na pasta que fara este exercicio.
2. Crie uma pasta chamada layer com o comando `mkdir layer` no terminal
3. Execute o comando `pip3 install -r requirements.txt -t layer/` para que todas as dependecias fiquem dentro desta pasta.
4. Crie um arquivo 'serverless.yml' com o seguinte conteudo
![img/lambda-01.png](img/lambda-01.png)
5. Crie um arquivo 'lambda.py' com o seguinte conteudo
![img/lambda-02.png](img/lambda-02.png)
6. Na URL do slack deixe o seguinte conteudo que esta no dontpad
7. No channel coloque o seguinte `#atividade-slack`
8. Execute o comando `sls deploy`
9. Agora cada vez que você publicar uma mensagem para o SNS irá receber uma mensagem no slack

