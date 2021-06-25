import pytest
import random
import string
import session7
import os
import inspect
import re
import math
from decimal import Decimal

FUNCTIONS_TO_CHECK_FOR = [
    'docstring_checker'
    ,'docstring_checker_inner'
    ,'next_fibonacci_number'
    ,'next_fibonacci_number_inner'
    ,'add'
    ,'mul'
    ,'div'
    ,'func_call_counter'
    ,'func_call_counter_inner'
    ,'func_call_counter_user'
    ,'func_call_counter_user_inner'
    ,'func_call_counter_user_innermost'
]

WORDS_TO_CHECK_FOR = [
    'global',
    'local',
    'nonlocal',
    'free variable',
    'closure'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in WORDS_TO_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_function_are_listed():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    AllFUNCTIONSDEFINED = True
    for c in FUNCTIONS_TO_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_doc_strings():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        print(function)
        assert function[1].__doc__

def test_docstring_checker_invalid():
    test1 = 'test'
    func1 = session7.docstring_checker()
    with pytest.raises(ValueError):
        func1(test1)

def test_docstring_checker_true():
    func1 = session7.docstring_checker()

    assert True == func1(session7.func_call_counter), "The docstring_checker function does not work properly"

def test_docstring_checker_false():
    func1 = session7.docstring_checker()

    assert False == func1(session7.add), "The docstring_checker function does not work properly"

def test_docstring_checker_blank():
    def test():
        pass
    func1 = session7.docstring_checker()

    assert False == func1(test), "The docstring_checker function does not work properly"

def test_next_fibonacci_number_true():
    func1 = session7.next_fibonacci_number()
    func1()
    func1()
    func1()
    func1()
    func1()

    assert 8 == func1(), "The next_fibonacci_number function does not work properly"

def test_next_fibonacci_number_invalid_args():
    with pytest.raises(TypeError):
        func1 = session7.next_fibonacci_number(1)

def test_add():
    assert 6 == (session7.add(4,2)), "The add function does not work properly"

def test_mul():
    assert 8 == (session7.mul(4,2)), "The mul function does not work properly"

def test_div():
    assert 2 == (session7.div(4,2)), "The div function does not work properly"

def dummy_func():
    pass

def test_func_call_counter_invalid_input():
    with pytest.raises(ValueError):
        func1 = session7.func_call_counter(dummy_func)

def test_func_call_counter_add_valid():
    func1 = session7.func_call_counter(session7.add)
    func1(2,3)
    func1(2,3)
    func1(2,3)
    assert {'add': 4, 'div': 0, 'mul': 0} == func1(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_add_invalid():
    func1 = session7.func_call_counter(session7.add)
    func1(2,3)
    func1(2,3)
    func1(2,3)
    assert {'add': 0, 'div': 0, 'mul': 0} != func1(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_div_valid():
    div1 = session7.func_call_counter(session7.div)
    div1(2,3)
    div1(2,3)
    div1(2,3)
    assert {'add': 4, 'div': 4, 'mul': 0} == div1(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_div_invalid():
    div2 = session7.func_call_counter(session7.div)
    div2(2,3)
    div2(2,3)
    div2(2,3)
    assert {'add': 0, 'div': 0, 'mul': 0} != div2(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_mul_valid():
    mul1 = session7.func_call_counter(session7.mul)
    mul1(2,3)
    mul1(2,3)
    mul1(2,3)
    assert {'add': 4, 'div': 4, 'mul': 4} == mul1(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_mul_invalid():
    mul2 = session7.func_call_counter(session7.mul)
    mul2(2,3)
    mul2(2,3)
    mul2(2,3)
    assert {'add': 0, 'div': 0, 'mul': 0} != mul2(2,3), "The func_call_counter function does not work properly"

def test_func_call_counter_user_invalid_dict():
    with pytest.raises(TypeError):
        non_dict1 = (1,2,3)
        func1 = session7.func_call_counter_user(non_dict1)

def test_func_call_counter_user_invalid_dictname():
    with pytest.raises(NameError):
        func1 = session7.func_call_counter_user(non_dict1)

def test_func_call_counter_user_blank_dict():
    dict1 = {}
    func1 = session7.func_call_counter_user(dict1)
    func2 = func1(session7.mul)
    func2(2,3)
    assert {'mul': 2} == func2(2,3), "The func_call_counter_user function does not work properly"

def test_func_call_counter_user_add_valid():
    dict1 = {'sub': 0}
    func1 = session7.func_call_counter_user(dict1)
    func2 = func1(session7.add)
    func2(2,3)
    assert {'sub': 0, 'add': 2} == func2(2,3), "The func_call_counter_user function does not work properly"

def test_func_call_counter_user_add_invalid():
    dict1 = {'sub': 0}
    func1 = session7.func_call_counter_user(dict1)
    func2 = func1(session7.add)
    func2(2,3)
    print(func2(2,3))
    assert {'sub': 0, 'add': 0} != func2(2,3), "The func_call_counter_user function does not work properly"