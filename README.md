# SpaceX-API

Consumo da API SpaceX para desafio do zapay

A intenção do projeto é apresentar de maneira amigavel os lançamentos de foguetes disponibilizados
na [API Space X](https://documenter.getpostman.com/view/2025350/RWaEzAiG#intro).

O projeto terá como funcionalidades:

1. Mostrar o próximo lançamento que será realizado.
2. Mostrar o último lançamento realizado.
3. Mostrar a lista de lançamentos que serão realizados.
4. Mostrar a lista de lançamentos já realizados.

### Instalação

```
pip install -r requirements
```

### Executar

```
python3 main.py
```

### Testes

```
pytest
```

### Coverage

```
pytest --cov=. tests/
```

### Implementação

A implementação foi realizada com a intenção de o executavel ser totalmente limpo, encapsulando
toda sua lógica de negocio dentro de suas classes especificas, cada uma com sua função, como prega
o **Single-Responsibility-Principle** do SOLID.

Todos os métodos com dois underlines na frentes são privados e foi utilizado o decorator @property
para torna-lo somente de leitura, ou seja, não há como modificar os dados que foi retornado da API.

Foi aplicado também o principio **Don't Repeat Yourself** em códigos que estavam se repetindo,
tornando eles métodos para serem reutilizados.

O menu do projeto foi adaptado para que todas as ações dependam do usuário, ou seja, para cada ação
será perguntado o que o usuário deseja de forma limpa.

Os testes estão bem simples e com 50% de cobertura de código e foi utilizado try-catch nas áreas
críticas do projeto com mensagens amigaveis de erro.