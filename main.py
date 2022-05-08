#Pokud hlasování neprobíhá, server odešle klientovi 0, pokud je však zmáčknuto tlačítko A, hlasování začne a server odešle 1.
#Po přijetí čísla 1, klient povolí vybrání odpovědi. Ta může být změněna kolikrát je potřeba. Jakmile je zmáčknuté logo, momentálně vybraná odpověď se odešle na server.
#Až server přijme odpověď, klientovi odešle "Přijato" a klient dá krátkou melodií vědět, že jeho odpověď byla přijata.
#Pokud je na serveru zmáčknuto znovu tlačítko A, hlasování se zastaví a po zmáčknutí B se zobrazí výsledky.
#Pokud je stisknutý PIN0 kód se zresetuje a server klientovi pošle číslo 2. Jakmile to je přijato, klient se resetuje také.
radio.set_group(150)
stop = 1
odpoved = 0

def on_received_number(receivedNumber):
    global stop
    if receivedNumber == 0:
        basic.show_icon(IconNames.NO)
        stop = 0
    elif receivedNumber == 1:
        basic.show_icon(IconNames.YES)
        stop = 1
    elif receivedNumber == 2:
        control.reset()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global stop, odpoved
    if stop == 1:
        odpoved = 0
        basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global stop, odpoved
    if stop == 1:
        odpoved = 1
        basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_released_p0():
    global stop, odpoved
    if stop == 1:
        odpoved = 2
        basic.show_string("C")
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_pin_released_p1():
    global stop, odpoved
    if stop == 1:
        odpoved = 3
        basic.show_string("D")
input.on_pin_released(TouchPin.P1, on_pin_released_p1)

def on_logo_event_pressed():
    global stop
    stop = 2
    radio.send_value("answer", odpoved)
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_received_string(receivedString):
    music.start_melody(music.built_in_melody(Melodies.JUMP_UP))
radio.on_received_string(on_received_string)