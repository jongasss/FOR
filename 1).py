while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Nota inválida. Digite uma nota entre zero e dez.")
