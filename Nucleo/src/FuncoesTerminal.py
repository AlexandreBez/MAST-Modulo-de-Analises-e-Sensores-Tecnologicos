from InquirerPy import inquirer

def mensagemTerminalParaTexto(mensagem="", completar={"Default": None}, mandatorio=True):
    valor = inquirer.text(
        message=mensagem,
        completer=completar,
        multicolumn_complete=True,
        mandatory=mandatorio,
        keybindings={
            "answer": [{"key": "enter"}]
        }
    ).execute()
    return valor


def mensagemTerminalParaNumero(mensagem, completar):
    valor = inquirer.text(
        message=mensagem,
        completer={completar},
        multicolumn_complete=True
    ).execute()
    return valor