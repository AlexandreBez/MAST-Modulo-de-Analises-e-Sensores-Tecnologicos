from InquirerPy import inquirer

def senhaTerminal(
    msg: str,
    estilo: dict = None,
    instrucao: str = "",
    instrucao_avancada: str = "",
    validador: any = None,
    msg_invalida: str = "Entrada inválida.",
    transformador= lambda _: "[segredo]",
    filtro: any = None,
    teclaDeAtalho: dict = None,
    permitir_Ctrl_C: bool = True,
    obrigatorio: bool = False,
    msg_mandatorio: str = "Este campo é obrigatório."
) -> str:
    mensagem = inquirer.secret(
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
    return mensagem