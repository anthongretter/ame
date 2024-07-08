# AMEC (AME Compiler)

#### A - Anthon Porath Gretter
#### M - Matheus Antonio de Souza
#### E - Eduardo de Moraes

---

### Objetivos

O objetivo deste projeto é realizar a implementação de um compilador para a linguagem 
AME, uma linguagem de programação de alto nível. O desenvolvimento consiste na construção de:

- Analisador Léxico (AL);
- Analisador Sintático (AS);
- Analisador Semântico (ASem);
- Gerador de Código Intermediário (GCI).

Este trabalho faz parte do plano de ensino da disciplina de Construção de Compiladores 
(INE5426), ministrado pelo prof. Alvaro Junio Pereira Franco.

### Estrutura do Projeto

A organização do código é bem simples:
- A execução dos analisadores é centralizada em `main.py`;
- `src/lexer` fica o código pertinente ao AL; 
- `src/syntax` está o código pertinente ao AS; 
- `src/semantic` é onde está o código pertinente ao ASem;
- `src/test` contém os arquivos `.ame` a serem testados; 
- `src/resources`, por sua vez, estão localizados arquivos de textos que descrevem as
SDDs e SDTs do projeto, e a gramática da linguagem.

### Dependências

- make;
- Python >= 3.10;
  - pip;
  - venv;
  - ply.
- Versão da biblioteca mencionada contra-se listada no arquivo de dependências `requirements.txt`.

### Instalação

Para instalar as dependências do projeto, basta executar o comando abaixo:

```fish
make install
```

> Caso dê algum problema com o uso do venv, é recomendado deletar a pasta `venv`
na raiz do projeto e executar o comando novamente.

### Execução

Para executar o projeto após instalação, basta executar o comando abaixo:

```fish
make run FILE=path/to/file.ame
```

Onde `path/to/file.ame` é o caminho para o arquivo `.ame` a ser analisado.

### Execução de testes

O projeto possui testes prontos, para executá-los basta executar o comando abaixo:

```fish
make desired_test
```

Onde `desired_test` é o teste desejado. Os testes disponíveis são:
- `test1`: testa o arquivo `merge.ame`;
- `test2`: testa o arquivo `primo.ame`;
- `test3`: testa o arquivo `adivinha.ame`;

> Ou, alternativamente, basta executar o seguinte comando para executar todos eles sequencialmente
> ```fish
> make tests
> ```
