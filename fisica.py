import tkinter as tk

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def on_entry_click(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='black')

def on_focusout(entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg='grey')

def create_window():
    window = tk.Toplevel()
    window.title("Física")
    window.geometry("500x500")

    def show_results(results):
        # Criar uma nova janela para exibir os resultados
        result_window = tk.Toplevel(window)
        result_window.title("Resultados")
        result_window.geometry("300x300")

        tk.Label(result_window, text=results, font=("Arial", 12)).pack(pady=20)

    def get_input_values():
        # Validação para garantir que os valores não são os textos padrão
        valor_espaco = None
        valor_velocidade = None
        valor_tempo = None
        valor_aceleracao = None
        

    # Verificações e atribuições
        if entrada_espaco.get() != "Espaço" and is_float(entrada_espaco.get()):
           valor_espaco = float(entrada_espaco.get())
        if entrada_velocidade.get() != "Velocidade" and is_float(entrada_velocidade.get()):
           valor_velocidade = float(entrada_velocidade.get())
        if entrada_tempo.get() != "Tempo" and is_float(entrada_tempo.get()):
           valor_tempo = float(entrada_tempo.get())
        if entrada_aceleracao.get() != "Aceleracao" and is_float(entrada_aceleracao.get()):
           valor_aceleracao = float(entrada_aceleracao.get())

        # Após obter os valores, realizar as condicionais e cálculos
        
        results = ""
        if valor_espaco is None and valor_velocidade is not None and valor_aceleracao is not None and valor_tempo is not None:
            #valor do espaço no sovetao
            valor_espaco=valor_tempo*valor_velocidade + 0.5*valor_aceleracao*(valor_tempo**2)
            resultado = valor_espaco
            results += f"Resultado é espaço = {resultado}\n"
        elif valor_espaco is None and valor_velocidade is None and valor_aceleracao is not None and valor_tempo is not None:
            #valor da velocidade no vovoat e do espaço no sovetao
            valor_velocidade=valor_aceleracao*valor_tempo
            valor_espaco=valor_tempo*valor_velocidade + 0.5*valor_aceleracao*(valor_tempo**2)
            resultado = valor_espaco
            results += f"Resultado é espaço = {resultado}\n e a velocidade={valor_velocidade}"
        elif valor_espaco is not None and valor_velocidade is None and valor_aceleracao is not None and valor_tempo is not None:
            #valor da velocidade no vovoat e do espaço no sovetao
            valor_velocidade=valor_aceleracao*valor_tempo
            resultado = valor_espaco
            results += f"Resultado é velocidade={valor_velocidade}"
        elif valor_espaco is not None and valor_velocidade is not None and valor_aceleracao is None and valor_tempo is not None:
            #valor da aeleração na vovoat
            valor_aceleracao=((valor_espaco-(valor_velocidade*valor_tempo))*2)/valor_tempo**2
            resultado = valor_aceleracao
            results += f"Resultado é aceleração = {resultado}\n"
        elif valor_espaco is None and valor_velocidade is not None and valor_aceleracao is None and valor_tempo is not None:
            valor_aceleracao=valor_velocidade/valor_tempo
            valor_espaco=valor_tempo*valor_velocidade + 0.5*valor_aceleracao*(valor_tempo**2)
            resultado = valor_espaco
            results += f"Resultado é espaço = {resultado}\n e aceleração = {valor_aceleracao}"
        elif valor_espaco is not None and valor_velocidade is not None and valor_aceleracao is not None and valor_tempo is None:
            valor_tempo=valor_velocidade/valor_aceleracao
            resultado = valor_tempo
            results += f"Resultado é tempo = {resultado}\n"


        show_results(results)

    

    estilo_input = {"font": ("Arial", 12), "bg": "#2400FF", "fg": "grey", "width": 13, "justify": "center"}

    default_texts = ["Espaço", "Aceleração", "Velocidade", "Tempo"]

    # Configuração das entradas de texto
    entrada_espaco = tk.Entry(window, **estilo_input)
    entrada_espaco.insert(0, default_texts[0])
    entrada_espaco.bind('<FocusIn>', lambda event: on_entry_click(entrada_espaco, default_texts[0]))
    entrada_espaco.bind('<FocusOut>', lambda event: on_focusout(entrada_espaco, default_texts[0]))
    entrada_espaco.place(x=58, y=234, width=150, height=42)

    entrada_aceleracao = tk.Entry(window, **estilo_input)
    entrada_aceleracao.insert(0, default_texts[1])
    entrada_aceleracao.bind('<FocusIn>', lambda event: on_entry_click(entrada_aceleracao, default_texts[1]))
    entrada_aceleracao.bind('<FocusOut>', lambda event: on_focusout(entrada_aceleracao, default_texts[1]))
    entrada_aceleracao.place(x=279, y=319, width=150, height=47)

    entrada_velocidade = tk.Entry(window, **estilo_input)
    entrada_velocidade.insert(0, default_texts[2])
    entrada_velocidade.bind('<FocusIn>', lambda event: on_entry_click(entrada_velocidade, default_texts[2]))
    entrada_velocidade.bind('<FocusOut>', lambda event: on_focusout(entrada_velocidade, default_texts[2]))
    entrada_velocidade.place(x=58, y=319, width=150, height=47)

    entrada_tempo = tk.Entry(window, **estilo_input)
    entrada_tempo.insert(0, default_texts[3])
    entrada_tempo.bind('<FocusIn>', lambda event: on_entry_click(entrada_tempo, default_texts[3]))
    entrada_tempo.bind('<FocusOut>', lambda event: on_focusout(entrada_tempo, default_texts[3]))
    entrada_tempo.place(x=279, y=234, width=150, height=42)

    texto_orientacao = tk.Label(window, text="use sempre final-inicial, nao coloque separado", font=("Arial", 14))
    texto_orientacao.place(x=100, y=50)

    btn_confirmar = tk.Button(window, text="Confirmar", bg="#2400FF", fg="white", command=get_input_values)
    btn_confirmar.place(x=161, y=420, width=168, height=40)
