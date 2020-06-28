import re
from colorama import init, Fore, Style

init()


class ParametersParser:
    """
        module for parsing the command line
        arguments:
            -c(--color): Highlight matching text
            -m(--machine): Generate machine readable output
                format: file_name:no_line:start_pos:matched_text
            -f(--files-list): single or multiple input text files
            -r(--regex): This is the regex flag
    """

    def __init__(self, cli_arguments):
        """
        Initializing parameters OBJ
        :param cli_arguments: input parameters from user
        """
        regex = False
        self.colorized = False
        self.machine_format = False
        self.files_list = False
        self.line_regex = False

        for item in cli_arguments:
            if item == '-c' or item == '--color':
                self.colorized = True
                # Turning on highlight matching text
            elif item == '-m' or item == '--machine':
                self.machine_format = True
                # Turning on machine readable format
            elif item == '-f' or item == '--files-list':
                self.files_list = self.get_list_of_files(cli_arguments)
            elif item == '-r' or item == '--regex':
                regex = True
                continue
            elif regex:
                self.line_regex = re.compile(rf'{item}')
                regex = False

        if not self.files_list or not self.line_regex:
            err_msg = "No file\s name or regex entered as expected, please add file\s name and regex " \
                      "pattern.\nExample: run_app.py -f filename.txt -r .*ExampleOfRegexPattern.\d "
            print(Fore.RED + err_msg)
            print(Style.RESET_ALL)
            raise AssertionError(err_msg)

    @staticmethod
    def get_list_of_files(cli_arguments):
        """
        This method use to parse only files directories
        :param cli_arguments: list of given parameters (list of strings)
        :return: files list
        """
        files_trigger = False
        files_list = []
        for item in cli_arguments:
            if item == '-f' or item == '--files-list':
                files_trigger = True
            elif files_trigger:
                if not item[0] == '-':
                    files_list.append(item)
                else:
                    files_trigger = False
        return files_list
