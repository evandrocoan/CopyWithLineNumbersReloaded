# Copy With Line Numbers Reloaded

Use codes from:

* https://github.com/freeella/copy_with_line_numbers.sublime-package
* https://github.com/curiousstranger/copy_with_line_numbers.sublime-package


## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
   wait few seconds until the installation finishes up
1. Go to the menu **`Tools -> Command Palette...
   (Ctrl+Shift+P)`**
1. Type **`Preferences:
   Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   add the following setting to your **`Package Control.sublime-settings`** file, if it is not already there
   ```js
   [
       ...
       "channels":
       [
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
           "https://packagecontrol.io/channel_v3.json",
       ],
       ...
   ]
   ```
   * Note,
     the **`https://raw...`** line must to be added before the **`https://packagecontrol...`**,
     otherwise you will not install this forked version of the package,
     but the original available on the Package Control default channel **`https://packagecontrol...`**
1. Now,
   go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
search for **`CopyWithLineNumbersReloaded`** and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## Example

Single selection:
```
File: /home/dev/projects/CopyWithLineNumbersReloaded/README.md
1: Use codes from:
2:  - https://github.com/freeella/copy_with_line_numbers.sublime-package
```

Multi selection:
```
File: /home/dev/projects/CopyWithLineNumbersReloaded/Main.sublime-menu
04:         "children":
05:         [
06:             { "caption": "Copy With Line Numbers", "command": "copy_with_line_numbers" }
07:         ]
---
22:                             {
23:                                 "command": "open_file",
24:                                 "args": {"file": "${packages}/CopyWithLineNumbersReloaded/CopyWithLineNumbersReloaded.sublime-settings"},
25:                                 "caption": "Settings – Default"
26:                             },
```


## Screen rec. (thx Enteleform)

![Multiple selection](https://crash5.github.io/CopyWithLineNumbersReloaded/multi_selection.gif)


## License

See LICENSE for license info
