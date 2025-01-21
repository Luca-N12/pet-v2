def on_button_pressed_a():
    music.play(music.string_playable("C D E F G A B C5 ", 250),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . . # # .
        . . . . #
        # . . . #
        . . . . #
        . . # # .
        """)
    basic.show_leds("""
        . . # # .
        . . . . #
        . # . . #
        . . . . #
        . . # # .
        """)
    basic.show_leds("""
        . . # # .
        . . . . #
        . . # . #
        . . . . #
        . . # # .
        """)
    basic.show_leds("""
        . . # # .
        . . . . #
        . . . # #
        . . . . #
        . . # # .
        """)
    basic.show_leds("""
        . . . . .
        . . # # .
        . . . # #
        . . # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # # .
        . . . . #
        . . # # .
        . . . . .
        """)
    basic.show_leds("""
        . . # # .
        . . . . #
        . . . . #
        . . . . #
        . . # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    control.wait_micros(60)
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_shake():
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . # . .
        . . . . .
        # # # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . . .
        . . . . .
        # # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . . . .
        . . . . .
        # # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . . .
        . . . . .
        # # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . # . .
        . . . . .
        # # # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . #
        . . . . .
        . . # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # .
        . . . . .
        . . . # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . .
        . . . # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # .
        . . . . .
        . . . # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . #
        . . . . .
        . . # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
basic.forever(on_forever)
