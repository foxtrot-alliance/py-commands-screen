# py-commands-screen

For support, please contact us: support@foxtrotalliance.com

This program allows you to execute screen-based commands such as clicking with the mouse, sending keystrokes, and taking screenshots. You can run the program via the CMD or as part of an automation script in an RPA tool like Foxtrot. This solution is meant to supplement Foxtrots core functionality and enable you to perform certain actions based on specified coordinates on the screen rather than Foxtrots own targeting technology. The solution is written in Python using the modules "pyautogui" and "keyboard". You can see the [full source code here](https://github.com/foxtrot-alliance/py-commands-screen/blob/master/py-commands-screen.py).

## Installation

1. Download the [latest version](https://github.com/foxtrot-alliance/py-commands-screen/releases/download/v0.0.2/py-commands-screen_v0.0.2.zip).
2. Unzip the folder somewhere appropriate, we suggest directly on the C: drive for easier access. So, your path would be similar to "C:\py-commands-screen_v0.0.2".
3. After unzipping the files, you are now ready to use the program. The only file you will have to be concerned about is the actual .exe file in the folder, however, all the other files are required for the solution to run properly.
4. Open Foxtrot (or any other RPA tool) to set up your action. In Foxtrot, you can utilize the functionality of the program via the DOS Command action (alternatively, the Powershell action).

## Usage

When using the program via Foxtrot, the CMD, or any other RPA tool, you need to reference the path to the program exe file. If you placed the program directly on your C: drive as recommended, the path to your program will be similar to: 
```
C:\py-commands-screen_v0.0.2\py-commands-screen_v0.0.2.exe
```
TIP: Make sure NOT to surround the path with quotation marks in your commands.

## Commands

All the available commands are specified [here](#all-available-parameters). Note, all parameters surrounded by [-x "X"] means that they are optional. For a more detailed description of each command, read the [detailed command description section](#detailed-command-description).

The solution offers three main commands:
* Click on the screen based on coordinates
```
PROGRAM_EXE_PATH -command_click "X" -position "X" [-value "X"] [-hover "X"]
```
TIP: How do you know the exact position of where you want to click? Open the Diagnostics Tool in Foxtrot and enable power targeting under the tools option.

* Write text or send keys to the screen
```
PROGRAM_EXE_PATH -command_send "X" -value "X"
```
* Take a screenshot of the full screen or specified region
```
PROGRAM_EXE_PATH -screenshot_path "X" -screenshot_region "X"
```

The solution will give an output to the selected variable in the DOS Command action to indicate whether the command was executed successfully or not.

## Multiple commands

It is possible to combine two or all three of the commands in one execution. It will always execute in the order:
1. Click
2. Send
3. Screenshot

It would look like this:
```
PROGRAM_EXE_PATH -command_click "X" -position "X" [-value "X"] [-hover "X"] -command_send "X" -value "X" -screenshot_path "X" -screenshot_region "X"
```

## Example
This example will first right-clicki and then send the keys "Down" "Down" "Enter":
```
PROGRAM_EXE_PATH -command_click "rightclick" -position "100, 100" -hover "true" -command_send "keys" -value "down, down, enter"
```

## All available parameters
```
-command_click: "click"/"doubleclick"/"rightclick"/"clickdragdrop", default = none (will not click unless specified)
  This is the click command you wish the solution to execute.

-position: "X, Y", required if any click command is specified.
  This is pixel coordinates to click.

-hover: "true/false", default = "false"
  If a click command is selected, this determines whether the mouse should remain in the position after clicking.

-command_send: "text"/"keys", default = none (will not send anything unless specified)
  This is the click command you wish the solution to execute.

-value: "X", required if "clickdragdrop" or any send command is specified.
  This specifies the text string or the keys to send.

-screenshot_path: "X", default = none (will not take a screenshot unless specified)
  This specifies the path to save any screenshot to.

-screenshot_region: "X", required if screenshot path is specified.
  This specifies the region to take a screenshot of. Can either be "all" (the whole screen) or a specific region "(StartLeft, StartTop, Width, Height)".

-traces: "true"/"false", default = "false"
  This determines whether you wish the output to include traces, information about the execution.
```

## Detailed command description

### Click
Parameters:
```
PROGRAM_EXE_PATH -command_click "click" -position "X, Y" [-hover "true"/"false"]
```
Examples:
```
PROGRAM_EXE_PATH -command_click "click" -position "250, 100"
PROGRAM_EXE_PATH -command_click "click" -position "100, 200" -hover "true"
```

### Double-click
Parameters:
```
PROGRAM_EXE_PATH -command_click "doubleclick" -position "X, Y" [-hover "true"/"false"]
```
Examples:
```
PROGRAM_EXE_PATH -command_click "doubleclick" -position "250, 100"
PROGRAM_EXE_PATH -command_click "doubleclick" -position "100, 200" -hover "true"
```

### Right-click
Parameters:
```
PROGRAM_EXE_PATH -command_click "rightclick" -position "X, Y" [-hover "true"/"false"]
```
Examples:
```
PROGRAM_EXE_PATH -command_click "rightclick" -position "250, 100"
PROGRAM_EXE_PATH -command_click "rightclick" -position "100, 200" -hover "true"
```

### Drag-and-drop
Parameters:
```
PROGRAM_EXE_PATH -command_click "clickdragdrop" -position "X, Y" -value "X, Y" [-hover "true"/"false"]
```
Examples:
```
PROGRAM_EXE_PATH -command_click "clickdragdrop" -position "250, 100" -value "500, 200"
PROGRAM_EXE_PATH -command_click "clickdragdrop" -position "100, 200" -value "200, 400" -hover "true"
```

### Write text
Parameters:
```
PROGRAM_EXE_PATH -command_send "text" -value "X"
```
Examples:
```
PROGRAM_EXE_PATH -command_send "text" -value "Hello World"
PROGRAM_EXE_PATH -command_send "text" -value "How are things going?"
```

### Send keystrokes
Parameters:
```
PROGRAM_EXE_PATH -command_send "keys" -value "X"
```
Examples:
```
PROGRAM_EXE_PATH -command_send "text" -value "down, down, enter"
PROGRAM_EXE_PATH -command_send "text" -value "ctrl+alt+del"
PROGRAM_EXE_PATH -command_send "text" -value "alt+F4, enter"
PROGRAM_EXE_PATH -command_send "text" -value "shift+s"
```

### Take screenshot
Parameters:
```
PROGRAM_EXE_PATH -screenshot_path "X" -screenshot_region "all"/"(StartLeft, StartTop, Width, Height)"
```
Examples:
```
PROGRAM_EXE_PATH -screenshot_path "c:\screenshots\screenshot.png" -screenshot_region "all"
PROGRAM_EXE_PATH -screenshot_path "c:\screenshots\screenshot.png" -screenshot_region "(0, 0, 1000, 1000)"
PROGRAM_EXE_PATH -screenshot_path "c:\screenshots\screenshot.png" -screenshot_region "(1000, 1000, 1500, 1500)"
```
