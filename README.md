# 🛰️ MAST – Módulo de Análises e Sensores Tecnológicos
![Logo do MAST(Modulo de Analise de Sensores Técnologicos)](MAST.png)

> Inspirado no laboratório MAST do universo de Starfield, este projeto tem como objetivo centralizar a leitura, coleta e análise de dados experimentais em um sistema modular e adaptável a diversos tipos de sensores para arduino e raspberry pi.

---

## 📌 Objetivo

Criar um sistema completo e modular capaz de:

* Coletar dados em tempo real de sensores analógicos ou digitais (como pH, corrente, voltagem, temperatura, gases voláteis, presão atmosférica, etc);
* Registrar e salvar automaticamente os dados para posterior análise em .odt/.pdf/.excel/.csv/etc;
* Realizar análises gerando gráficos em arquivos .pdf/.odt
* Continuar implementações futuras para novos sensores e soluções

---

## 🧪 Software utilizados

- **Python 3.11+**
- [Pandas](https://pandas.pydata.org/) – manipulação de dados
- [Matplotlib](https://matplotlib.org/) – gráficos científicos
- [NumPy](https://numpy.org/) – cálculos numéricos
- [pyserial](https://pythonhosted.org/pyserial/) – leitura de sensores via serial

---

## 🧰 Estrutura

> O projeto é divido em varios modulos independentes que mantem comunicação entre sí:

1. **Núcleo**
> Responsável pela comunicação entre os submódulos. Ele centraliza os dados recebidos, coordena a leitura dos sensores, e oferece um terminal CMD para operações principais como coleta, visualização e exportação de dados.

    **Hardware usado no Núcleo:**
    - **Raspberry Pi 3/4** (ou superior) com Raspberry Pi OS Lite
    - Cartão microSD classe 10 (mínimo 16 GB)
    - Fonte de alimentação 5V 2.5A
    - Módulo Conversor Analógico Digital Ads1115 16bits 4 Canais

    *Nota:* O módulo ADS1115 permite a leitura de sinais analógicos com alta precisão (16 bits), 
    algo necessário para sensores como pH, temperatura por termistor, entre outros — especialmente 
    porque o Raspberry Pi não possui entradas analógicas nativas.

    **Arquivos principais:**
    - `mast/__main__.py` – ponto de entrada do sistema via terminal
    - `mast/menu.py` – interface do usuário via CLI
    - `mast/sensores.py` – comunicação com sensores
    - `mast/analise.py` – cálculos estatísticos
    - `mast/utils.py` – exportações e manipulações


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
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🧾 Licença

Este projeto está licenciado sob os termos da Licença MIT.  
Consulte o arquivo `LICENSE` para mais detalhes.