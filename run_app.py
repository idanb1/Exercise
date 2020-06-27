import argparse
import FileRunner


def runner(**kwargs):
    """
    runner function use to search regex in text files,
    using parameters from user(cli) or directly from another test
    module (TestClass)
    :param kwargs: dictionary of parameters
    (support TestSuite class for testing)
    :return: dictionary of key = filename,
    value = list of all pattern matches in file
    """
    if not kwargs:
        parser = argparse.ArgumentParser(description='RegexInFiles', prog='''
        This application is designed to search for regex matches in text files''', epilog='''
        Example of use: python run_app.py -c -f
        "./pytest/example1.txt" -r grows''')
        parser.add_argument('-f', '--files', type=str, required=True,
                            help='This is the files flag - **required flag',
                            action=UniqueStore)
        parser.add_argument('-r', '--regex', type=str, required=True,
                            help='This is the regex flag - **required flag',
                            action=UniqueStore)
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-c', '--color', action='store_true',
                           help='This is the color flag')
        group.add_argument('-m', '--machine', action='store_true',
                           help='This is the machine readable output flag')

        kwargs = vars(parser.parse_args())

    files = kwargs.get('files').split(',')
    dict_result = {}
    for file in files:
        dict_result[file] = FileRunner.match_pattern(
            kwargs.get('color'), kwargs.get('machine'),
            kwargs.get('regex'), file)
        if len(dict_result[file]) == 0:
            print(f'No matches found in file {file}')

    return dict_result


class UniqueStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if getattr(namespace, self.dest, self.default) is not self.default:
            parser.error(option_string + " appears several times.")
        setattr(namespace, self.dest, values)


if __name__ == '__main__':
    runner()
