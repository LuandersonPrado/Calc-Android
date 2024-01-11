import flet as ft


def main(page: ft.Page):
    page.title = "Calc Android"
    page.window_height = 400 
    page.window_width = 350
    page.bgcolor = "#1F1F1F"
 
    def keyboard(ac):
        data = ac.control.data
        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*",",","/","(",")"]:
            txt.value =  str(txt.value) + str(data)
            page.update()
        if data == "=":
            txt.value = str(eval(txt.value))
            page.update()
        if data == "c":
            st = list(txt.value)
            st.pop()
            txt.value = "".join(map(str,st))
            page.update()
        if data == "ac":
            txt.value = ""
            page.update()


    txt = ft.TextField(
        #read_only=True,
        border_color="#38393D",
        text_style=ft.TextStyle(size=30,color="#E2E4E5"),
        bgcolor="#38393D"
        ) 

    page.add(txt)
    btn_ac = ft.ElevatedButton(
        text="AC", bgcolor="#0F5324", color="#BFE8FF",data="ac",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_po = ft.ElevatedButton(
        text="()", bgcolor="#004A77", color="#BFE8FF",data="()",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_pc = ft.ElevatedButton(
        text="%", bgcolor="#004A77", color="#BFE8FF",data="%",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_divisao = ft.ElevatedButton(
        text="÷", bgcolor="#004A77", color="#BFE8FF",data="/",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r1 = ft.Row(
        controls=[btn_ac,btn_po,btn_pc,btn_divisao],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
 
    btn_7 = ft.ElevatedButton(
        text="7", bgcolor="#28282A", color="#C4E7FB",data="7",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_8 = ft.ElevatedButton(
        text="8", bgcolor="#28282A", color="#C4E7FB",data="8",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_9 = ft.ElevatedButton(
        text="9", bgcolor="#28282A", color="#C4E7FB",data="9",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_multi = ft.ElevatedButton(
        text="x", bgcolor="#004A77", color="#BFE8FF",data="*",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r2 = ft.Row(
        controls=[btn_7,btn_8,btn_9,btn_multi],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    btn_4 = ft.ElevatedButton(
        text="4", bgcolor="#28282A", color="#C4E7FB",data="4",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_5 = ft.ElevatedButton(
        text="5", bgcolor="#28282A", color="#C4E7FB",data="5",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_6 = ft.ElevatedButton(
        text="6", bgcolor="#28282A", color="#C4E7FB",data="6",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_minus = ft.ElevatedButton(
        text="-", bgcolor="#004A77", color="#BFE8FF",data="-",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r3 = ft.Row(
        controls=[btn_4,btn_5,btn_6,btn_minus],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    btn_1 = ft.ElevatedButton(
        text="1", bgcolor="#28282A", color="#C4E7FB",data="1",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_2 = ft.ElevatedButton(
        text="2", bgcolor="#28282A", color="#C4E7FB",data="2",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_3 = ft.ElevatedButton(
        text="3", bgcolor="#28282A", color="#C4E7FB",data="3",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_mais = ft.ElevatedButton(
        text="+", bgcolor="#004A77", color="#BFE8FF",data="+",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r4 = ft.Row(
        controls=[btn_1,btn_2,btn_3,btn_mais],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    btn_0 = ft.ElevatedButton(
        text="0", bgcolor="#28282A", color="#C4E7FB",data="0",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_vir = ft.ElevatedButton(
        text=",", bgcolor="#28282A", color="#C4E7FB",data=",",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_cln = ft.ElevatedButton(
        text="c", bgcolor="#28282A", color="#C4E7FB",data="c",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_igual = ft.ElevatedButton(
        text="=", bgcolor="#004A77", color="#BFE8FF",data="=",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    r5 = ft.Row(
        controls=[btn_0,btn_vir,btn_cln,btn_igual],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r1,r2,r3,r4,r5)

    

ft.app(target=main)
