def menu():
    # Dados fictícios de exemplo
    dados = []

    while True:
        print(r"""
        ███╗   ███╗    █████╗    ███████╗████████╗
        ████╗ ████║   ██╔══██╗   ██╔════╝╚══██╔══╝
        ██╔████╔██║   ███████║   ███████╗   ██║   
        ██║╚██╔╝██║   ██╔══██║   ╚════██║   ██║   
        ██║ ╚═╝ ██║██╗██║  ██║██╗███████║██╗██║   
        ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝   
        [ MAST - Módulo de Análises e Sensores Tecnológicos ]
        """)
        print("BEM-VINDO AO NUCLEO")
        print("\n1 - Sensores")
        print("2 - Dados")
        print("3 - Calcular estatísticas")
        print("4 - Salvar relatório")
        print("5 - Sair")

        opcao = input("\n>> Escolha uma opção: ")

        if opcao == "1":
            print("🔧 Modo sensores ativado...")
            # chamada futura: sensores.iniciar()
        elif opcao == "2":
            print("📋 Exibindo dados...")
            for i, d in enumerate(dados):
                print(f"T{i}: {d:.4f} unidades")
        elif opcao == "3":
            print("📈 Calculando estatísticas...")
            # analise.calcular_estatisticas(dados)
        elif opcao == "4":
            print("💾 Salvando relatório...")
            # utils.salvar_relatorio(dados)
        elif opcao == "5":
            print("👋 Encerrando o sistema MAST...")
            break
        else:
            print("❌ Opção inválida.")
