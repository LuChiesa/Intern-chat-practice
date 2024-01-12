import flet as ft

def main(page):
    text = ft.Text("Chat Gpzap")


    username = ft.TextField(label="Write your name")

    def send_message(event):
        text_message_field = f"{username.value}: {message_field.value}"
        page.pubsub.send_all(text_message_field)
        message_field.value = ""
        page.update()
        
    message_field = ft.TextField(label="Write your message right here", on_submit=send_message)

    send_button = ft.ElevatedButton("Send", on_click=send_message)

    def send_message_tunel(info):
        chat.controls.append(ft.Text(info))
        page.update()


    page.pubsub.subscribe(send_message_tunel)

    chat = ft.Column()

    def enter_chat(event):
        popup.open = False
        page.add(chat)
        chatbox = ft.Row([message_field, send_button])
        page.add(chatbox)
        page.remove(start_button)
        page.update()

    popup = ft.AlertDialog(open=False, modal=True, title=ft.Text("Never use your true name! Here we have dangerous people"), content=username, actions=[ft.ElevatedButton("Enter", on_click=enter_chat)])

    def start_chat(event):
        page.dialog = popup
        popup.open = True
        text = f"{username.value} just droped in"
        chat.controls.append(ft.Text(text))

        page.update()
   
    start_button = ft.ElevatedButton("Start chat", on_click=start_chat)


    page.add(text)
    page.add(start_button)


ft.app(main, view=ft.WEB_BROWSER)