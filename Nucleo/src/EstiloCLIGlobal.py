
def estiloGlobalPergunta():
    return{
        # Marcador da pergunta
        "questionmark": "fg:#ffffff bg:#00ff00 bold", 
        # Pergunta principal
        "question": "fg:#ffffff bg:#00ff00 bold",
    }
    
def estiloGlobalResposta():
    return{
        # Pergunta já respondida
        "answered_question": "fg:#ffffff bg:#00ffaa",
        # Marcador da resposta
        "answermark": "#00ffaa",
        # Resposta selecionada                    
        "answer": "fg:#ffffff bg:#00ff00 bold",   
        # Texto digitado
        "input": "fg:#ffffff bg:#00ff00 bold",
        
        "skipped": "#5c6370",
    }
        
def estiloGlobalSpinner():
    return{
        # Loading spinner
        "spinner_pattern": "fg:#ffffff bg:#00ff00 bold",
        # Texto do spinner
        "spinner_text": "fg:#ffffff bg:#00ff00 bold",
    }
    
def estiloGlobalInstrucao():
    return{
        # Instruções pequenas
        "instruction": "#abb2bf",
        # Instruções maiores
        "long_instruction": "#abb2bf",
    }
    
def estiloGlobalFuzzy():
    return{
        # Busca fuzzy
        "fuzzy_prompt": "#c678dd",
        # Info do fuzzy
        "fuzzy_info": "#abb2bf",
        # Borda do fuzzy
        "fuzzy_border": "#4b5263",
        # Match em busca
        "fuzzy_match": "#c678dd",
    }
    
def estiloGlobalValidacao():
    return{
        # Erros de validação
        "validator": "",
    }
    
def estiloGlobalCheckbox():
    return{
        # Marcador de check
        "checkbox": "#98c379",
    }

def estiloGlobalMarcadores():
    return{
        # Setinha de seleção
        "pointer": "#61afef",
        # Linhas divisórias
        "separator": "",
        # Check/Cross
        "marker": "#e5c07b",
    }