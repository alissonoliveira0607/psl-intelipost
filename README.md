# Documentação da Aplicação

Esta aplicação Flask tem como objetivo disponibilizar um endpoint APTO que recebe uma solicitação de pré-lista de postagem (PSL - PLP by IP) no endpoint `/psl` e retorna uma resposta JSON.

## Configuração

Para configurar e executar esta aplicação, siga as instruções abaixo:

### Pré-requisitos

- Python 3.9 ou superior instalado.
- Ambiente virtual (opcional, mas recomendado).

### Instalação de Dependências

1. Clone este repositório:

    ```bash
    git clone https://github.com/alissonoliveira0607/psl-intelipost.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu_repositorio
    ```

3. Instale as dependências usando o arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Execução da Aplicação

Execute a aplicação Flask usando o seguinte comando:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

## Endpoint

### POST `/psl`

Este endpoint recebe uma solicitação de Pré-Lista de Postagem (PSL - PLP by IP) no formato JSON conforme especificado na documentação da [Intelipost](https://docs.intelipost.com.br/docs/tms-embarcador/7dc60ec3bf5dc-pre-lista-de-postagem) e retorna uma resposta JSON com os detalhes do processamento.


Consulte a [documentação da Intelipost](https://docs.intelipost.com.br/docs/tms-embarcador/7dc60ec3bf5dc-pre-lista-de-postagem) para obter mais detalhes sobre a estrutura da solicitação e da resposta.

## Docker

Você também pode executar esta aplicação usando Docker. Um Dockerfile está disponível no repositório para facilitar a criação de um contêiner Docker.

### Construção da Imagem Docker

Para construir a imagem Docker, execute o seguinte comando no diretório do projeto:

```bash
docker build -t nome_imagem:tag .
```

### Execução do Contêiner Docker

Para executar a aplicação em um contêiner Docker, use o seguinte comando:

```bash
docker run -d -p 5000:5000 nome_imagem:tag
```

Substitua `nome_imagem:tag` pelo nome e tag da imagem Docker que você deseja utilizar.

A aplicação estará disponível em `http://localhost:5000/psl`.

---

Desenvolvimento baseado na [documentação da Intelipost](https://docs.intelipost.com.br/docs/tms-embarcador/7dc60ec3bf5dc-pre-lista-de-postagem).
