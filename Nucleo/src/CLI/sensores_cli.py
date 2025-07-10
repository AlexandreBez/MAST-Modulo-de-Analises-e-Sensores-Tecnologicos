from InquirerPy import inquirer

def sensores_cli():
    print(r"""
    ███████╗███████╗███╗   ██╗███████╗ ██████╗ ██████╗ ███████╗███████╗
    ██╔════╝██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
    ███████╗█████╗  ██╔██╗ ██║███████╗██║   ██║██████╔╝█████╗  ███████╗
    ╚════██║██╔══╝  ██║╚██╗██║╚════██║██║   ██║██╔══██╗██╔══╝  ╚════██║
    ███████║███████╗██║ ╚████║███████║╚██████╔╝██║  ██║███████╗███████║
    ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝                                                        
    [ MAST - Módulo de Análises e Sensores Tecnológicos ]
    """)
    opcao = inquirer.select(
        message="🛰️ MAST – Selecione uma opção:",
        choices=[
            "🔬 Verificar Status do Sensor",
            "📁 Dados",
            "📊 Estatísticas",
            "💾 Salvar relatório",
            "🚪 Sair"
        ],
        default="🔬 Sensores"
    ).execute()
    
    return opcao;