import os
import sublime
import sublime_plugin


def trim_leading_charater(fileName, character):
    if len( fileName ) > 0 and fileName[0] == character:
        fileName = fileName.replace( character, '', 1 )
    return fileName


class CopyWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())
        selections = view.sel()
        fileName = view.file_name()

        # Settings
        settings = sublime.load_settings("CopyWithLineNumbersReloaded.sublime-settings")
        relativeFilePath = settings.get("copy_relative_filepath", False)
        sameLineNumberLength = settings.get("same_length_line_number", True)
        filePathHeader = settings.get("print_filepath_header", True)
        multiSelectionSeparator = settings.get("multi_selection_separator", "---")


        if filePathHeader:
            # Set file name, and header text
            if fileName:
                folders = view.window().folders()
                if folders and relativeFilePath:
                    fileName = self.removeAbsolutePath(fileName, folders)
                outputFileName = fileName
            else:
                outputFileName = "<unsaved>"

            output = "File: " + outputFileName.replace('\\', '/') + "\n"
        else:
            output = "" # no header


        if sameLineNumberLength:
            # To print all the line numbers with the same length
            largestLineNumber = self.getLineNumber(selections[-1].end())
            largestLineNumberLength = len(str(largestLineNumber))
            outputLineFormatString = "%" + str(largestLineNumberLength) + "d: %s\n"
        else:
            outputLineFormatString = "%d: %s\n"


        # handle text
        isFollowupSelection = None
        for selection in selections:
            if isFollowupSelection:
                # split multi selections with ---
                output += multiSelectionSeparator + "\n"
            else:
                # but not the first one
                isFollowupSelection = True
            # for each selection
            selection = view.line(selection)  # Extend selection to full line
            firstLineNumberInSelection = self.getLineNumber(selection.begin())
            linesInSelection = view.substr(selection).split("\n")  # Considers all line breaks
            for i, line in enumerate(linesInSelection):
                output += outputLineFormatString % (firstLineNumberInSelection + i, line)


        # Send to clipboard
        sublime.set_clipboard(output)


    def getLineNumber(self, point):
        return self.view.rowcol(point)[0] + 1

    @staticmethod
    def removeAbsolutePath(fileName, folderList):
        for folder in folderList:
            # print("folder", folder)
            dirname = os.path.dirname(folder);
            if folder in fileName and dirname != "/" and dirname != "\\":
                fileName = fileName.replace(dirname, '')
                fileName = trim_leading_charater(fileName, '/')
                fileName = trim_leading_charater(fileName, '\\')
            break
        return fileName
