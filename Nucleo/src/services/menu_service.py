from InquirerPy import inquirer
from src.CLI.menu_cli import menu_cli

def menu():
    
    while True:
        opcao = menu_cli()

        if opcao == "🔬 Sensores":
            print("Abrindo módulo de sensores...")
            # Aqui você pode importar e chamar sensores_menu() ou similar futuramente
        elif opcao == "📁 Dados":
            print("📁 Módulo de dados (em construção)...")
        elif opcao == "📊 Estatísticas":
            print("📊 Cálculos estatísticos (em breve)...")
        elif opcao == "💾 Salvar relatório":
            print("💾 Exportação de relatório (em breve)...")
        elif opcao == "🚪 Sair":
            sair = questionary.press_any_key_to_continue("").ask()
            if sair == true:
                print("👋 Saindo do sistema MAST...")
                break
            else:
                return
        else:
            print("❌ Opção inválida. Tente novamente.")
