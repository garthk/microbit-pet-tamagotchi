input.onButtonPressed(Button.A, function on_button_pressed_a() {
    uhOh()
})
function hungerFace() {
    if (Hunger > 1800) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
    
}

function uhOh() {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(196, music.beat(BeatFraction.Quarter))
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (Busy) {
        uhOh()
        return
    }
    
    Busy = true
    if (Hunger > 30) {
        Hunger = 0
        basic.showIcon(IconNames.Happy)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
    }
    
    Busy = false
    hungerFace()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    if (Busy) {
        return
    }
    
    Busy = true
    basic.showIcon(IconNames.Sad)
    soundExpression.sad.playUntilDone()
    Busy = false
    hungerFace()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (Busy) {
        uhOh()
        return
    }
    
    Busy = true
    basic.showIcon(IconNames.Happy)
    soundExpression.giggle.playUntilDone()
    Busy = false
    hungerFace()
})
let Busy = false
let Hunger = 0
Hunger = 0
Busy = false
basic.showIcon(IconNames.Asleep)
basic.forever(function on_forever() {
    
    basic.pause(1000)
    Hunger += 1
    hungerFace()
})
