import re
import socket
from colorama import init, Fore, Style
from datetime import datetime

init()


def match_pattern(colorized, machine_format, pattern, file):
    """
    This function get parameters from the main runner func,
    and searching a match from a given file & regex
    :param colorized: color flag(bool)
    :param machine_format: machine readable output flag(bool)
    :param pattern: regex pattern (str)
    :param file: file path(str)
    :return: return list of all pattern matches
    """

    results = []
    readable = gen_machine_format() if machine_format else ''
    with open(file) as fp:
        for cnt, line in enumerate(fp):
            match = re.search(pattern, line)
            if match:
                file_only = file.split("/")
                #
                # check for backslash if slash wasn't found
                if len(file_only) < 2:
                    file_only = file.split("\\")
                file_only = file_only[len(file_only)-1]
                timestamp = datetime.now()
                output = f'{readable}{file_only}:{cnt}:{timestamp}'
                results.append(f'{output}:' + match.group())
                if colorized:
                    print(f'{output}:' + Fore.GREEN + line)
                    print(Style.RESET_ALL)
                else:
                    print(f'{readable}{file_only}:{cnt}:{timestamp}:{line}')
    return results


def gen_machine_format():
    """
    :return: machine readable output format:
    timestamp,target,type (str)
    """
    logtype = 'Pattern_Matches'
    timestamp = datetime.now()
    #
    # Getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    #
    # Getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)

    return f'{timestamp},{hostname}-{ip_address},{logtype}, '
