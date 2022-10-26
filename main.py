import json
import rel
import websocket
from pynput.keyboard import Key, Controller


punchout = False
sensitivity = 50



keyboard = Controller()

def on_message(ws, message):
    y = json.loads(message)
    hands = y["hands"]
    if len(hands) != 0 and len(hands) == 2:
        if hands[0]["type"] == "left":
            handl = hands[0]
            handr = hands[1]
        if hands[0]["type"] == "right":
            handl = hands[1]
            handr = hands[0]

        palmPositionLeft = handl["palmPosition"]
        palmPositionLeftX = palmPositionLeft[0] + 200  # ujemna to lewo, dodatnia prawo
        palmPositionLeftY = palmPositionLeft[2]  # ujemna to przod ,dodatnia tyl
        palmPositionRight = handr["palmPosition"]
        palmPositionRightX = palmPositionRight[0] - 200
        palmPositionRightY = palmPositionRight[2]
        grabStrengthLeft = handl["grabStrength"]
        grabStrengthRight = handr["grabStrength"]

        text = f'lewa x  {palmPositionLeftX}\n' \
               f'lewa y  {palmPositionLeftY}\n' \
               f'lewa chwyt  {grabStrengthLeft}\n' \
               f'prawa x  {palmPositionRightX}\n' \
               f'prawa y  {palmPositionRightY}\n' \
               f'prawa chwyt  {grabStrengthRight}\n'

        if grabStrengthLeft == 1:  # use
            keyboard.press(Key.space)
        else:
            keyboard.release(Key.space)

        if punchout:  # fire
            if grabStrengthRight == 1 and palmPositionRightY < -sensitivity:
                keyboard.press('i')
            else:
                keyboard.release('i')
        else:
            if grabStrengthRight == 1:
                keyboard.press('i')
            else:
                keyboard.release('i')

        if palmPositionRightX < -sensitivity:  # aim left and right
            keyboard.press('j')
            keyboard.release('l')
        elif palmPositionRightX > sensitivity:
            keyboard.press('l')
            keyboard.release('j')
        else:
            keyboard.release('j')
            keyboard.release('l')

        if palmPositionLeftX < -sensitivity:  # walk left and right
            keyboard.press('a')
            keyboard.release('d')
        elif palmPositionLeftX > sensitivity:
            keyboard.press('d')
            keyboard.release('a')
        else:
            keyboard.release('a')
            keyboard.release('d')

        if palmPositionLeftY < -sensitivity:  # walk forward and backward
            keyboard.press('w')
            keyboard.release('s')
        elif palmPositionLeftY > sensitivity:
            keyboard.press('s')
            keyboard.release('w')
        else:
            keyboard.release('w')
            keyboard.release('s')


    else:
        text = f'no hands'

    print(text)

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")



if __name__ == "__main__":
    text = f'init'
    print(text)
    ws = websocket.WebSocketApp("ws://localhost:6437/v7.json",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
