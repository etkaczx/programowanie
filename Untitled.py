# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Dekoratory w pythonie

# %%
def my_decorator(func):
    def wrapper():
        my_character = '\u2740'
        print(my_character * 6)
        func()
        print(my_character * 6)

    return wrapper


# %%
@my_decorator 
def hello():
    print('kwiatki')
    


# %%
hello()


# %% [markdown]
# # Funkcje z argumentami

# %%
def my_decorator(func):
    def wrapper(*args, **kwargs):
        my_character = '\u2740'
        print(my_character * 6)d
        result = func(*args, **kwargs)
        print(my_character * 6)
        return result

    return wrapper
        
        
        

# %%
@my_decorator
def add(a,b):
    """dodaje dwie liczby :o"""
    return a+b


# %%
add.__doc__

# %%
add(2,3)


# %%
@my_decorator
def power_tower(a,b,c):
    return a**b**c

# %% [raw] jupyter={"outputs_hidden": true}
# power_tower(2,3,4)
