import sys
import os
import pyautogui
import datetime
import keyboard
import traceback

def retrieve_project_parameters():
    
    parameters = sys.argv

    parameters_number = parameters.index("-traces") if "-traces" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        traces = parameters[parameters_number]
    else:
        traces = ""

    parameters_number = parameters.index("-command_click") if "-command_click" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        command_click = parameters[parameters_number]
    else:
        command_click = ""

    parameters_number = parameters.index("-position") if "-position" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        position = parameters[parameters_number]
    else:
        position = ""

    parameters_number = parameters.index("-hover") if "-hover" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        hover = parameters[parameters_number]
    else:
        hover = ""

    parameters_number = parameters.index("-command_send") if "-command_send" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        command_send = parameters[parameters_number]
    else:
        command_send = ""

    parameters_number = parameters.index("-value") if "-value" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        value = parameters[parameters_number]
    else:
        value = ""

    parameters_number = parameters.index("-screenshot_path") if "-screenshot_path" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        screenshot_path = parameters[parameters_number]
    else:
        screenshot_path = ""

    parameters_number = parameters.index("-screenshot_region") if "-screenshot_region" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        screenshot_region = parameters[parameters_number]
    else:
        screenshot_region = "(0 , 0, " + str(pyautogui.size().width) + ", " + str(pyautogui.size().height) + ")"
        
    return {
        "traces": traces,
        "command_click": command_click,
        "position": position,
        "hover": hover,
        "command_send": command_send,
        "value": value,
        "screenshot_path": screenshot_path,
        "screenshot_region": screenshot_region,
    }

def validate_project_parameters(parameters):
    
    traces = parameters["traces"]
    command_click = parameters["command_click"]
    position = parameters["position"]
    hover = parameters["hover"]
    command_send = parameters["command_send"]
    value = parameters["value"]
    screenshot_path = parameters["screenshot_path"]
    screenshot_region = parameters["screenshot_region"]
    
    if traces == "" or traces.upper() == "FALSE":
        traces = False
    elif traces.upper() == "TRUE":
        traces = True
    else:
        return "ERROR: Invalid traces parameter! Parameter = " + str(traces)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved start * ===")

    if command_click.upper() == "CLICK":
        command_click = "CLICK"
    elif command_click.upper() == "DOUBLECLICK":
        command_click = "DOUBLECLICK"
    elif command_click.upper() == "RIGHTCLICK":
        command_click = "RIGHTCLICK"
    elif command_click.upper() == "CLICKDRAGDROP":
        command_click = "CLICKDRAGDROP"
    elif not command_click == "":
        return "ERROR: Invalid click command parameter! Parameter = " + str(command_click)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tClick command = " + str(command_click))

    if not command_click.upper() == "":
        if not position == "":
            position = position.split(",")
        else:
            return "ERROR: Empty position parameter!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tPosition = " + str(position))

    if hover == "" or hover.upper() == "FALSE":
        hover = False
    elif hover.upper() == "TRUE":
        hover = True
    else:
        return "ERROR: Invalid hover parameter! Parameter = " + str(hover)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tHover = " + str(hover))

    if command_send.upper() == "TEXT":
        command_send = "TEXT"
    elif command_send.upper() == "KEYS":
        command_send = "KEYS"
    elif not command_send == "":
        return "ERROR: Invalid send command parameter! Parameter = " + str(command_send)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tSend command = " + str(command_send))

    if not command_send.upper() == "":
        if value == "":
            return "ERROR: Empty value parameter!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tValue = " + str(value))

    if not screenshot_path == "":
        screenshot_path_exists = os.path.isdir(os.path.dirname(os.path.abspath(screenshot_path)))
        if screenshot_path_exists:
            if not screenshot_path.upper().endswith(".PNG"):
                return "ERROR: The image file is not PNG!"
        else:
            return "ERROR: The folder directory was not found!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tScreenshot path = " + str(screenshot_path))

        if not screenshot_region.upper() == "ALL":
            screenshot_region = eval(screenshot_region)
        elif screenshot_region == "":
            return "ERROR: Empty screenshot region parameter!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tScreenshot region = " + str(screenshot_region))

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved end * ===")
        
    return {
        "traces": traces,
        "command_click": command_click,
        "position": position,
        "hover": hover,
        "command_send": command_send,
        "value": value,
        "screenshot_path": screenshot_path,
        "screenshot_region": screenshot_region,
    }
        
def execute_command(parameters):
    
    traces = parameters["traces"]
    command_click = parameters["command_click"]
    position = parameters["position"]
    hover = parameters["hover"]
    command_send = parameters["command_send"]
    value = parameters["value"]
    screenshot_path = parameters["screenshot_path"]
    screenshot_region = parameters["screenshot_region"]
    
    try:
        if "CLICK" in command_click.upper():

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform click command start * ===")

            mouse_location_x, mouse_location_y = pyautogui.position()

            if command_click.upper() == "CLICK":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to click...")

                pyautogui.click(position)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tClick complete!")

            elif command_click.upper() == "DOUBLECLICK":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to double-click...")

                pyautogui.doubleClick(position)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tDouble-click complete!")

            elif command_click.upper() == "RIGHTCLICK":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to right-click...")

                pyautogui.rightClick(position)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tRight-click complete!")

            elif command_click.upper() == "CLICKDRAGDROP":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to drag-and-drop...")

                pyautogui.moveTo(position)
                pyautogui.drag(value.split(","))

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tDrag-and-drop complete!")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform click command end * ===")
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Move mouse back to original position start * ===")

            if hover is False:

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to move mouse back to position...")

                pyautogui.moveTo(mouse_location_x, mouse_location_y)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tMoving mouse back to position complete!")

            else:

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tHovering mouse activated, therefore, do NOT move mouse back in position")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Move mouse back to original position end * ===")

        if not command_send == "":

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform send command start * ===")

            if command_send.upper() == "TEXT":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to write values: " + value)

                keyboard.write(value)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tWriting values complete!")

            elif command_send.upper() == "KEYS":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to send keys: " + value)

                keyboard.send(value)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tSend keys complete!")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform send command end * ===")

        if not screenshot_path == "":

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform screenshot start * ===")

            if str(screenshot_region).upper() == "ALL":

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Attempting to take a screenshot of the full screen")

                pyautogui.screenshot(screenshot_path)

            else:

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Attempting to take a screenshot of the full screen")

                pyautogui.screenshot(screenshot_path, screenshot_region)

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Screenshot complete!")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform screenshot end * ===")
    
    except:
        print(traceback.format_exc())
        return "ERROR: Unexpected issue!"
    
    return True
    
def main():
    
    parameters = retrieve_project_parameters()
    
    parameters = validate_project_parameters(parameters)
    if not isinstance(parameters, dict):
        print(str(parameters))
        return
    
    valid = execute_command(parameters)
    if not valid is True:
        print(str(valid))
        return
    
    print("SUCCESS")
    
    
if __name__ == "__main__":
    main()
