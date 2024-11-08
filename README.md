# Flask App e PyUnit

Repositório base para o desenvolvimento de um pipeline que execute testes unitários no Gitlab.

# O Arquivo .gitlab-ci.yml

- Arquivo YAML (YAML Ain't Markup Language) que especifica as instruções para a execução da pipeline através do Gitlab Runner;
- O arquivo deve ser salvo na raiz do projeto sempre com o nome .gitlab-ci.yml;
- Possui uma série de palavras-chave para diversas situações de uso, como acionamento em branches especificas;
- A sintaxe completa do arquivo pode ser consultada na [documentação de referência](https://docs.gitlab.com/ee/ci/yaml/index.html) e seu preenchimento pode ser validado no [Editor de  Pipelines do Gitlab](https://docs.gitlab.com/ee/ci/pipeline_editor/index.html) ou através de uma extensão do [VSCode](https://marketplace.visualstudio.com/items?itemName=gitlab.gitlab-workflow).

Exemplo de arquivo .gitlab-ci.yml que executa um stage chamado “test-job” exibindo o valor informado a partir do comando “echo” dentro da interface gráfica do Gitlab (menu CI/CD > Pipelines > Jobs):

```
test-job:
    stage: test
    script:
        - echo "This job tests something"
```

## Exercício Proposto

Alterar o arquivo .gitlab-ci.yml, contemplando a execução dos testes unitários com PyUnit e validar o pipeline.

## Executando a aplicação

```
$ python app/app.py run
```

A aplicação responderá em duas rotas na web:

http://localhost:5000/health-check

http://localhost:5000/hello?name=guijac
