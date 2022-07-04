def on_button_pressed_a():
    uhOh()
input.on_button_pressed(Button.A, on_button_pressed_a)

def hungerFace():
    if Hunger > 1800:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.ASLEEP)
def uhOh():
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.QUARTER))

def on_button_pressed_b():
    global Busy, Hunger
    if Busy:
        uhOh()
        return
    Busy = True
    if Hunger > 30:
        Hunger = 0
        basic.show_icon(IconNames.HAPPY)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.UNTIL_DONE)
    Busy = False
    hungerFace()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global Busy
    if Busy:
        return
    Busy = True
    basic.show_icon(IconNames.SAD)
    soundExpression.sad.play_until_done()
    Busy = False
    hungerFace()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global Busy
    if Busy:
        uhOh()
        return
    Busy = True
    basic.show_icon(IconNames.HAPPY)
    soundExpression.giggle.play_until_done()
    Busy = False
    hungerFace()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Busy = False
Hunger = 0
Hunger = 0
Busy = False
basic.show_icon(IconNames.ASLEEP)

def on_forever():
    global Hunger
    basic.pause(1000)
    Hunger += 1
    hungerFace()
basic.forever(on_forever)
