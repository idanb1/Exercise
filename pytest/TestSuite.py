import pytest
import os
from run_app import runner

SCRIPT_DIR = os.path.dirname(__file__)


@pytest.fixture()
def data_init():
    """
    Initialize dependencies for test suite
    :return:
    """
    # SETUP
    data_init = dict()
    data_init['example_file1'] = os.path.join(SCRIPT_DIR, 'example1.txt')
    data_init['example_file2'] = os.path.join(SCRIPT_DIR, 'example2.txt')
    data_init['no_permissions'] = os.path.join(SCRIPT_DIR, 'NoPermissions.txt')
    print('doing things to setup')
    yield data_init
    # TEARDOWN
    print('doing things to teardown')


@pytest.mark.negative
def test_without_input_files():
    """
    Running test without input files
    :return:
    """
    print('Running test without input files')
    try:
        runner(files='', regex=r'\d\d\d\d\d')
        assert False
    except FileNotFoundError:
        assert True


#@pytest.mark.negative
#def test_without_permission_files(data_init):
#    """
#    Running test without permission files
#    :return:
#    """
#    print('Running test without permission files')
#    try:
#        runner(files=data_init['no_permissions'], regex='\d\d\d\d\d')
#        assert False
#    except PermissionError:
#        assert True



@pytest.mark.negative
def test_no_matches(data_init):
    """
    Running test without successful matches
    :param data_init: test suite dependencies (list of example input files)
    :return:
    """
    print('Running test without successful matches')
    results = runner(files=data_init['example_file1'], regex=r'\d')
    assert True if len(results[data_init['example_file1']]) == 0 else False


@pytest.mark.functional
def test_basic_functionality(data_init):
    """
    Running basic test functionality (1 input file & pattern)
    :param data_init: test suite dependencies (list of example input files)
    :return:
    """
    print('Running basic test functionality')
    results = runner(files=data_init['example_file1'],  regex='grows')
    assert True if len(results[data_init['example_file1']]) == 2 else False


@pytest.mark.functional
def test_multiple_files(data_init):
    """

    :param data_init:
    :return:
    """
    print('Running test with multiple files')
    example_files = \
        data_init['example_file1'] + ',' + data_init['example_file2']
    results = runner(files=example_files,  regex='grows')
    count = 0
    for val in results.values():
        count += len(val)
    assert True if count == 4 else False
