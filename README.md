# SpaceX-API

Consumo da API SpaceX para desafio do zapay

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

A implementação foi realizada com a intenção de o executavel ser totalmente limpo, e encapsulando
toda sua lógica de negocio dentro de suas classes especificas, cada uma com sua função, como prega
o **Single-Responsibility-Principle** do SOLID.

Todos os métodos com dois underlines na frentes são privados e foi utilizado o decorator @property
para torna-lo somente de leitura, ou seja, não há como modificar os dados que foi retornado da API.

Foi aplicado também o principio **Don't repeat yourseal** em códigos que estavam se repetindo
no código, tornando eles métodos para serem reutilizados.

O menu do projeto foi adaptado para que todas as ações dependam do usuário, ou seja, para cada ação
será perguntado o que o usuário deseja.

Os testes estão bem simples e fiz só até 50% de cobertura de código e foi utilizado try-catch nas áreas
críticas do projeto.