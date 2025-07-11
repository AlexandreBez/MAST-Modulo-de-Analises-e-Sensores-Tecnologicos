from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

def perguntaTerminalParaTexto(
    msg: str,
    estilo: dict = None,
    instrucao: str = "",
    instrucao_avancada: str = "",
    dicionario: dict = None,
    multi_linha: bool = False,
    validador: any = None,
    msg_invalida: str = "Entrada inválida.",
    transformador: any = None,
    filtro: any = None,
    teclaDeAtalho: dict = None,
    permitir_Ctrl_C: bool = True,
    obrigatorio: bool = False,
    msg_mandatorio: str = "Este campo é obrigatório."
) -> str:
    mensagem = inquirer.text(
        message=msg,
        style=estilo,
        instruction=instrucao,
        long_instruction=instrucao_avancada,
        completer=dicionario,
        multicolumn_complete=True,
        multiline=multi_linha,
        validate=validador,
        invalid_message=msg_invalida,
        transformer=transformador,
        filter=filtro,
        keybindings=teclaDeAtalho,
        wrap_lines=True,
        raise_keyboard_interrupt=permitir_Ctrl_C,
        mandatory=obrigatorio,
        mandatory_message=msg_mandatorio
    ).execute()
    return mensagem

def perguntaTerminalParaNumero(
    msg: str,
    estilo: dict = None,
    instrucao: str = "",
    instrucao_avancada: str = "",
    validador: any = NumberValidator(float_allowed=True,message="Escreve apenas números inteiros ou decimais..."),
    msg_invalida: str = "Entrada inválida.",
    transformador: any = lambda x: f"{x} 🔢",
    filtro: any = None,
    teclaDeAtalho: dict = None,
    permitir_Ctrl_C: bool = True,
    obrigatorio: bool = False,
    msg_mandatorio: str = "Este campo é obrigatório."
) -> float:
    valor = inquirer.text(
        message=msg,
        style=estilo,
        instruction=instrucao,
        long_instruction=instrucao_avancada,
        validate=validador,
        invalid_message=msg_invalida,
        transformer=transformador,
        filter=filtro,
        keybindings=teclaDeAtalho,
        wrap_lines=True,
        raise_keyboard_interrupt=permitir_Ctrl_C,
        mandatory=obrigatorio,
        mandatory_message=msg_mandatorio
    ).execute()
    return valor
