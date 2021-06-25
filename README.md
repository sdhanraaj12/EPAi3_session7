# Session 7 Assignment 
### Assignment states

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200  
2. Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100  
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250  
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250  


### Concepts required
Various scopes and closures concepts in Python. Concepts like global scope, local scope, nonlocal scope, closure and free variable etc.  

### Implementation
## 1. Closure that takes a function and then check whether the function passed has a docstring with more than 50 characters

```python 
def docstring_checker():
    '''
    This function creates a closure with a free variable check_length = 50.
    The function doesn’t need any input.
    The function returns the inner function which evaluates whether the passed function
    has a valid docstring length.
    '''
    check_length = 50
    def docstring_checker_inner(func:'function name') -> bool:
        '''
        This function checks for validity of docstring by checking it's length.
        Currently the docstring length > 50 is assumed to be valid.
        The function takes a function name as input.
        The function returns True or False depending on whether the passed function
        has a valid docstring length.
        '''
        if not hasattr(func,'__call__'):
            raise ValueError('Please pass a valid function')

        length_checker =  True if bool(func.__doc__) and len(func.__doc__) >= check_length else False
        return length_checker
    return docstring_checker_inner
```

## 2. Closure that gives the next Fibonacci number 

```python 
def next_fibonacci_number():
    '''
    This function creates a closure for identifying next Fibonacci number.
    The function doesn’t need any input.
    The function returns you the inner function which gives the next Fibonacci number
    every time the function is run.
    '''
    ini_num = 0

    def next_fibonacci_number_inner():
        nonlocal ini_num
        if(ini_num == 0):
            ini_num = 0,1
        else:
            temp_num = ini_num[1]
            ini_num = temp_num,ini_num[1] +ini_num[0]
        return ini_num[-1]
    return next_fibonacci_number_inner
```

## 3. Closure that counts how many times a function was called. Another closure that can keep a track of how many times add/mul/div functions were called

```python 

def add(a:int,b:int)->int:
    '''
    A custom function to add two numbers.
    '''
    return a+b

def mul(a:int,b:int)->int:
    '''
    A custom function to multiply two given numbers.
    '''
    return a*b

def div(a:int,b:int)->int:
    '''
    A custom function to add two given numbers. It also checks that the denominator is not zero.
    '''
    try:
        return a/b
    except:
        return 'ZeroByDivisionError: please provide non-zero Denominator.'

dict_of_func_call_counter = {'add':0,'mul':0,'div':0}

def func_call_counter(func:'callable'):
    '''
    This function creates a closure that can keep count of how many times a function was called.
    The function takes function name as input.
    The function returns you the inner function which returns a dictionary with fuction names and
    their total runs so far as a key value pair.
    '''
    global dict_of_func_call_counter
    if func.__name__ not in dict_of_func_call_counter:
        raise ValueError("Only these functions are allowed: add/mul/div")

    cnt = 0
    def func_call_counter_inner(*args,**kwargs):
        '''
        This function returns a dictionary with fuction names and
        their total runs so far as a key value pair.
        The function any number of arguments as inputs.
        The function returns a dictionary with fuction names and their total runs so far as a key value pair.
        '''
        global dict_of_func_call_counter
        nonlocal cnt
        cnt += 1
        dict_of_func_call_counter[func.__name__] = cnt
        return dict_of_func_call_counter
    return func_call_counter_inner


```

## 4. Closure that can keep count of how many times a function was called. The function takes a dictionary as input which can be passed in different dictionary variables to update different dictionaries

```python 
def func_call_counter_user(dict_by_user:'dict'):
    '''
    This function creates a closure that can keep count of how many times a function was called.
    The function takes a dictionary as input.
    The function returns you the inner function which returns the updated dictionary with fuction
    names and their total runs so far as a key value pair.
    '''
    if not isinstance(dict_by_user,dict):
        raise TypeError("need to pass a dictionary per user")

    def func_call_counter_user_inner(func):
        '''
        This function returns an inner function.
        The function takes function name as input.
        The function returns an inner function which in turn returns a dictionary with fuction names
        and their total runs so far as a key value pair.
        '''
        cnt = 0
        def func_call_counter_user_innermost(*args,**kwargs):
            '''
            This function returns a dictionary with fuction names and
            their total runs so far as a key value pair.
            The function any number of arguments as inputs.
            The function returns a dictionary with fuction names and their total runs so far as a key value pair.
            '''
            nonlocal dict_by_user
            nonlocal cnt
            cnt +=1
            dict_by_user[func.__name__] = cnt
            return dict_by_user
        return func_call_counter_user_innermost
    return func_call_counter_user_inner
```
### Test Cases:

There are total 29 test cases to check the working of each task function. There are some general test cases of checking documentation of the project and the python files,There are testcases to check to whether they are acutally closures or not. All are listed below.

	1. test_readme_exists
	2. test_readme_contents
	3. test_readme_proper_description
	4. test_function_are_listed
	5. test_readme_file_for_formatting
	6. test_indentations
	7. test_function_name_had_cap_lette:
	8. test_function_doc_strings:
	9. test docstring_checker
	10. test_docstring_checker_true
	11. test_docstring_checker_false
	12. test_docstring_checker_blank
	13. test_next_fibonacci_number_true
	14. test_next_fibonacci_number_invalid_args
	15. test_add
	16. test_mul
	17. test_div
	18. test_func_call_counter_invalid_input
	19. test_func_call_counter_add_valid
	20. test_func_call_counter_add_invalid
	21. test_func_call_counter_div_valid
	22. test_func_call_counter_div_invalid
	23. test_func_call_counter_mul_valid
	24. test_func_call_counter_mul_invalid
	25. test_func_call_counter_user_invalid_dict
	26. test_func_call_counter_user_invalid_dictname
	27. test_func_call_counter_user_blank_dict
	28. test_func_call_counter_user_add_valid
	29. test_func_call_counter_user_add_invalid

<image src='assets/pass.png' height='790'>
