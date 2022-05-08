// Pokud hlasování neprobíhá, server odešle klientovi 0, pokud je však zmáčknuto tlačítko A, hlasování začne a server odešle 1.
// Po přijetí čísla 1, klient povolí vybrání odpovědi. Ta může být změněna kolikrát je potřeba. Jakmile je zmáčknuté logo, momentálně vybraná odpověď se odešle na server.
// Až server přijme odpověď, klientovi odešle "Přijato" a klient dá krátkou melodií vědět, že jeho odpověď byla přijata.
// Pokud je na serveru zmáčknuto znovu tlačítko A, hlasování se zastaví a po zmáčknutí B se zobrazí výsledky.
// Pokud je stisknutý PIN0 kód se zresetuje a server klientovi pošle číslo 2. Jakmile to je přijato, klient se resetuje také.
radio.setGroup(150)
let stop = 1
let odpoved = 0
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 0) {
        basic.showIcon(IconNames.No)
        stop = 0
    } else if (receivedNumber == 1) {
        basic.showIcon(IconNames.Yes)
        stop = 1
    } else if (receivedNumber == 2) {
        control.reset()
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (stop == 1) {
        odpoved = 0
        basic.showString("A")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (stop == 1) {
        odpoved = 1
        basic.showString("B")
    }
    
})
input.onPinReleased(TouchPin.P0, function on_pin_released_p0() {
    
    if (stop == 1) {
        odpoved = 2
        basic.showString("C")
    }
    
})
input.onPinReleased(TouchPin.P1, function on_pin_released_p1() {
    
    if (stop == 1) {
        odpoved = 3
        basic.showString("D")
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    stop = 2
    radio.sendValue("answer", odpoved)
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    music.startMelody(music.builtInMelody(Melodies.JumpUp))
})
