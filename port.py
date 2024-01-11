import flet as ft

def main(page):
    
    def login(e):
        if not entrada_email.value:
            entrada_email.error_text = "Por favor, insira seu E-mail!"
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Por favor, insira sua senha!"
            page.update()
        else:
            email = entrada_email.value
            senha = entrada_senha.value
            print(f"E-mail: {email}\nSenha: {senha}")
            page.clean() #Função para limpar a página
            page.add(ft.Text(f"Olá, Usuário! Seja muito bem-vindo ao meu aplicativo!"))
            pass



    entrada_email = ft.TextField(label="Digite seu E-mail")
    entrada_senha = ft.TextField(label="Digite a sua senha")
    
    page.add(
        entrada_email,
        entrada_senha,
        ft.ElevatedButton("Entrar", on_click=login)

    )
    pass


ft.app(target=main)
