# AMEC (AME Compiler)

#### A - Anthon Porath Gretter
#### M - Matheus Antonio de Souza
#### E - Eduardo de Moraes

---

### Objectives

The goal of this project is to implement a compiler for the AME language, a high-level programming language. The development consists of building:

- Lexical Analyzer (LA);
- Syntax Analyzer (SA);
- Semantic Analyzer (SAn);
- Intermediate Code Generator (ICG).

This work is part of the syllabus for the Compiler Construction course (INE5426), taught by Prof. Alvaro Junio Pereira Franco.

### Project Structure

The code organization is very simple:
- The execution of the analyzers is centralized in `main.py`;
- `src/lexer` contains the code related to the LA;
- `src/syntax` contains the code related to the SA;
- `src/semantic` contains the code related to the SAn;
- `src/test` contains the `.ame` files to be tested;
- `src/resources` contains text files that describe the SDDs and SDTs of the project, and the language grammar.

### Dependencies

- make;
- Python >= 3.10;
  - pip;
  - venv;
  - ply.
- The version of the mentioned library is listed in the `requirements.txt` file.

### Installation

To install the project dependencies, run the command below:

```fish
make install
```

> If you encounter issues with venv, it is recommended to delete the `venv` folder in the root of the project and run the command again.

### Execution

To run the project after installation, execute the command below:

```fish
make run FILE=path/to/file.ame
```

Where `path/to/file.ame` is the path to the `.ame` file to be analyzed.

### Test Execution

The project includes ready-to-use tests. To execute them, run the command below:

```fish
make desired_test
```

Where `desired_test` is the desired test. The available tests are:
- `test1`: tests the `merge.ame` file;
- `test2`: tests the `primo.ame` file;
- `test3`: tests the `adivinha.ame` file;

> Alternatively, you can run the following command to execute all of them sequentially:
> ```fish
> make tests
> ```
