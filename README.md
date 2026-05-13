# 🐍 Curso Introdutório de Python para Ciência de Dados

> Projeto de Extensão — Disciplina de Ciência de Dados (T326)  
> Universidade de Fortaleza — UNIFOR / Centro de Ciências Tecnológicas (CCT)  
> Professora: Dra. Cynthia Moreira Maia

---

## 📌 Objetivo Geral

Este repositório reúne os materiais produzidos pelas equipes da disciplina T326 como parte do Componente Curricular de Extensão (CCEX) da UNIFOR. O objetivo é oferecer um curso introdutório de Python com foco em Ciência de Dados para a comunidade externa, democratizando o acesso ao conhecimento em tecnologia e análise de dados.

---

## 📂 Estrutura Geral do Repositório

```
/
├── README.md               ← Este arquivo
├── modulo_1/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
├── modulo_2/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
├── modulo_3/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
├── modulo_4/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
├── modulo_5/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
├── modulo_6/
│   ├── README.md
│   ├── slides/
│   ├── codigos/
│   └── videos/
└── modulo_7/
    ├── README.md
    ├── slides/
    ├── codigos/
    └── videos/
```

---

## 📁 Convenção de Nomenclatura

Todos os arquivos dentro de cada módulo seguem o padrão abaixo:

| Pasta      | Formato          | Exemplo          |
| ---------- | ---------------- | ---------------- |
| `videos/`  | `video_N.txt`    | `video_1.txt`    |
| `slides/`  | `aula_N.pdf`     | `aula_1.pdf`     |
| `codigos/` | `codigo_N.ipynb` | `codigo_1.ipynb` |

## 🗂️ Módulos e Temas

### Módulo 1 — Fundamentos de Ciência de Dados e Linguagem Python

Conceitos gerais sobre Ciência de Dados · Etapas de um projeto · Introdução ao Python · Tipos e variáveis · Expressões e operadores · Estruturas condicionais · Estruturas de repetição · Listas, Tuplas, Conjuntos e Dicionários · Funções

### Módulo 2 — Python para Ciência de Dados

Manipulação de dados tabulares com Pandas · Series e DataFrame · Tipos de dados no Pandas · Leitura de CSV e Excel · Renomeação de colunas · Seleção, filtros e consultas · Agregações · Tratamento inicial de dados

### Módulo 3 — Exploração de Dados e Estatística

Estatística descritiva · Média, mediana e moda · Variância e desvio padrão · Quartis e medidas de dispersão · Correlação · Interpretação estatística com datasets reais

### Módulo 4 — Visualização de Dados

Importância da visualização na EDA · Gráfico de barras · Gráfico de pizza · Gráfico de dispersão · Histogramas · Boxplot · Gráfico de violino · Boas práticas de visualização

### Módulo 5 — Limpeza, Tratamento e Transformação de Dados / Introdução ao Machine Learning

**Opção A:** Dados ausentes · Remoção de inconsistências · Padronização de formatos · Tratamento de outliers · Transformação de variáveis  
**Opção B:** Introdução ao ML · Método Holdout · Classificação · Regressão · Avaliação de modelos e métricas

---

## 🐍 Versão do Python

Todos os módulos utilizam **Python 3.10 ou superior**.

Verifique sua versão com:

```bash
python --version
```

---

## 📦 Bibliotecas Utilizadas

Instale todas as dependências de uma vez:

```bash
pip install pandas numpy scipy matplotlib seaborn scikit-learn openpyxl notebook
```

Ou por módulo:

| Módulo | Bibliotecas                       |
| ------ | --------------------------------- |
| 1      | Nenhuma (Python puro)             |
| 2      | `pandas`, `openpyxl`              |
| 3      | `pandas`, `numpy`, `scipy`        |
| 4      | `matplotlib`, `seaborn`           |
| 5      | `pandas`, `numpy`, `scikit-learn` |

---

## ▶️ Como Executar

### Script `.py`

```bash
python modulo_X/codigos/nome_do_arquivo.py
```

### Notebook `.ipynb`

```bash
pip install notebook
jupyter notebook modulo_X/codigos/nome_do_notebook.ipynb
```

_Projeto extensionista — UNIFOR, 2026. Repositório público conforme exigência da disciplina T326._
