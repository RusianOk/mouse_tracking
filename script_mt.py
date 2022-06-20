import time, mouse, json, keyboard

event_list = []

def event_listener(event):

    x, y = mouse.get_position()

    if mouse.is_pressed("left") == True:
        event_list.append({
            'timestamp' : time.time(),
            'action' : 'lmb',
            'x' : x,
            'y' : y,
        })

    if mouse.is_pressed("right") == True:
        event_list.append({
            'timestamp' : time.time(),
            'action' : 'rmb',
            'x' : x,
            'y' : y,
        })

mouse.hook(event_listener)

keyboard.wait('ESC')

event_list_json = json.dumps(event_list, indent=4)
with open("event_list.json", "w") as my_file:
    my_file.write(event_list_json)