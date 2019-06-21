import explorerhat as eh
from time import sleep

def allOn():
    eh.output.one.on()
    eh.output.two.on()
    eh.output.three.on()
    eh.output.four.on()
    print("All outputs on")

def pattern1():
    timer= .25
    eh.output.four.off()
    eh.output.one.on()
    sleep(timer)
    eh.output.one.off()
    eh.output.two.on()
    sleep(timer)
    eh.output.two.off()
    eh.output.three.on()
    sleep(timer)
    eh.output.three.off()
    eh.output.four.on()
    sleep(timer)


while True:
    if eh.touch.one.is_pressed():
        allOn()

    if eh.touch.two.is_pressed():
        pattern1()


