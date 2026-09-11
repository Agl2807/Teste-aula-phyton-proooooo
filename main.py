meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "FARMAR AURA": "Farmar aura significa realizar ações ou atitudes para acumular pontos de estilo, carisma, confiança e respeito perante as outras pessoas",
    "67": "A gíria 67 não tem um significado fixo ou lógico.",
    "SIX-SEVEN": "A gíria six-seven não tem um significado fixo ou lógico.",
    "TUFF": "é uma gíria da internet derivada da palavra em inglês tough (que significa forte ou durão), usada para elogiar algo ou alguém que é muito estiloso, legal ou impressionante"
}

print("--- Dicionário de Gírias Modernas ---")
print("(Para encerrar o programa, digite SAIR)")

while True:
    word = input("Digite uma palavra moderna (EM MAIÚSCULAS): ")
    
    if word == "SAIR":
        print("Programa encerrado. Até mais!")
        break
        
    if word in meme_dict:
        print("Significado de",word,":") 
        print(meme_dict[word])
    else:
        print("Palavra não encontrada. Tente novamente!")
