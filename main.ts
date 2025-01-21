input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("C D E F G A B C5 ", 250), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . . # # .
        . . . . #
        # . . . #
        . . . . #
        . . # # .
        `)
    basic.showLeds(`
        . . # # .
        . . . . #
        . # . . #
        . . . . #
        . . # # .
        `)
    basic.showLeds(`
        . . # # .
        . . . . #
        . . # . #
        . . . . #
        . . # # .
        `)
    basic.showLeds(`
        . . # # .
        . . . . #
        . . . # #
        . . . . #
        . . # # .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . . . # #
        . . # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . . . . #
        . . # # .
        . . . . .
        `)
    basic.showLeds(`
        . . # # .
        . . . . #
        . . . . #
        . . . . #
        . . # # .
        `)
})
input.onGesture(Gesture.ScreenDown, function () {
    control.waitMicros(60)
    music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.InBackground)
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Happy)
})
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . # . .
        . . . . .
        # # # . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        . . . . .
        # # . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        . . . . .
        # # . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        . . . . .
        # # . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . # . .
        . . . . .
        # # # . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . #
        . . . . .
        . . # # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . # .
        . . . . .
        . . . # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . .
        . . . # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . # .
        . . . . .
        . . . # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . #
        . . . . .
        . . # # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        `)
})
