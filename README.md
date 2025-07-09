rgb(0, 0, 0)

# 🛰️ MAST – Módulo de Análises e Sensores Tecnológicos
![Logo do MAST(Modulo de Analise de Sensores Técnologicos)](MAST.png)

> Inspirado no laboratório MAST do universo de Starfield, este projeto tem como objetivo centralizar a leitura, coleta e análise de dados experimentais em um sistema modular e adaptável a diversos tipos de sensores para arduino e raspberry pi.

---

## 📌 Objetivo

[^1]: Criar um sistema completo e modular capaz de:

[^1]: Coletar dados em tempo real de sensores analógicos ou digitais (como pH, corrente, voltagem, temperatura, gases voláteis);
[^2]: Registrar e salvar automaticamente os dados para posterior análise;
[^3]: Gerar gráficos e relatórios com base nas medições;
[^4]: Aplicar estatísticas descritivas e análises para detectar padrões ou anomalias;
[^5]: Simular ambientes extremos e registrar o comportamento químico das amostras.

---

## 🧰 Tecnologias utilizadas

- **Python 3.11+**
- [Pandas](https://pandas.pydata.org/) – manipulação de dados
- [Matplotlib](https://matplotlib.org/) – gráficos científicos
- [NumPy](https://numpy.org/) – cálculos numéricos
- [pyserial](https://pythonhosted.org/pyserial/) – leitura de sensores via serial
- [ADS1115 ou multiplexadores](https://www.adafruit.com/product/1085) – para leituras analógicas com precisão
- **Raspberry Pi + Arduino** – integração com sensores físicos

---

## 🧪 Estrutura do projeto

MAST/
├── .venv/ # Ambiente virtual Python
├── data/ # Dados coletados dos sensores (.csv, .json)
├── docs/ # Documentação, objetivos e anotações
├── src/ # Código-fonte principal do projeto
│ ├── main.py # Script principal de execução
│ ├── sensores.py # Leitura dos sensores
│ ├── analise.py # Cálculos estatísticos
│ ├── graficos.py # Geração de gráficos
│ └── utils.py # Funções auxiliares
├── requirements.txt # Pacotes Python necessários
├── README.md # Esta documentação
└── .gitignore # Ignora arquivos do ambiente virtual

---

## 🧠 Filosofia do projeto

Este projeto é guiado por uma abordagem científica experimental e filosófica, valorizando:

- O questionamento constante (estilo cartesiano);
- A busca por evidências em vez de suposições;
- A união entre ciência de dados e ciência experimental prática;
- A possibilidade de modular e adaptar sensores para qualquer ambiente — da Terra até simulações planetárias.

---

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/MAST.git
cd MAST

