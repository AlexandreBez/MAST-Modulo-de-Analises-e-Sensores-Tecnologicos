from InquirerPy import inquirer

def menu_cli():
    
    print(r"""
    ███╗   ███╗    █████╗    ███████╗████████╗
    ████╗ ████║   ██╔══██╗   ██╔════╝╚══██╔══╝
    ██╔████╔██║   ███████║   ███████╗   ██║   
    ██║╚██╔╝██║   ██╔══██║   ╚════██║   ██║   
    ██║ ╚═╝ ██║██╗██║  ██║██╗███████║██╗██║   
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝   
    [ MAST - Módulo de Análises e Sensores Tecnológicos ]
    """)
    opcao = inquirer.select(
        message="🛰️ MAST – Selecione uma opção:",
        choices=[
            "🔬 Sensores",
            "📁 Dados",
            "📊 Estatísticas",
            "💾 Salvar relatório",
            "🚪 Sair"
        ],
        default="🔬 Sensores"
    ).execute()
    
    return opcao;

def confirmar_()