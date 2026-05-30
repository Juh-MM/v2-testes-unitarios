# Sistema de Gerenciamento de Notas

## Descrição

Este projeto foi desenvolvido em Python com o objetivo de aplicar conceitos de testes unitários utilizando o framework Pytest.

O sistema permite:

* Calcular a média de duas notas;
* Verificar a situação do aluno de acordo com a média obtida.

## Regras de Negócio

* Média maior ou igual a 7: **Aprovado**
* Média entre 5 e 6,9: **Recuperação**
* Média menor que 5: **Reprovado**

## Estrutura do Projeto

```text
projeto/
├── classe.py
└── test_classe.py
```

### classe.py

Contém a classe `GerenciamentoNotas`, responsável por:

* Calcular a média das notas;
* Verificar a situação do aluno.

### test_classe.py

Contém os testes unitários desenvolvidos com Pytest para validar as regras de negócio.

## Testes Implementados

### Teste de média correta

Verifica se o método de cálculo de média retorna o valor esperado.

Exemplo:

```python
assert aluno.calcular_media(8, 6) == 7
```

### Teste de aprovação

Verifica se médias maiores ou iguais a 7 retornam "Aprovado".

### Teste de recuperação

Verifica se médias entre 5 e 6,9 retornam "Recuperação".

### Teste de reprovação

Verifica se médias menores que 5 retornam "Reprovado".

## Execução dos Testes

Para executar os testes foi utilizado o comando:

```bash
pytest -v
```

## Resultado Obtido

```text
=========================== test session starts ===========================
collected 4 items

test_classe.py::test_media_correta PASSED
test_classe.py::test_aprovado PASSED
test_classe.py::test_recuperacao PASSED
test_classe.py::test_reprovado PASSED

============================ 4 passed ============================
```

## Ciclo de Desenvolvimento

O desenvolvimento foi realizado seguindo a proposta de testes unitários:

1. Implementação da classe com as regras de negócio.
2. Criação dos testes para validar cada regra.
3. Execução dos testes utilizando Pytest.
4. Correção e validação até que todos os testes fossem aprovados.

Dessa forma foi possível garantir que o sistema está funcionando conforme os requisitos definidos para o cenário de gerenciamento de notas.
