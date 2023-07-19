# This module is intended to be used by external scripts, such as the following shell script:
# python3 generate.py | wl-copy
# which will take the output of the script and copy it to the Wayland clipboard.

# This module can also be used as a simple interface to all 3 generators.

from random import randint

def gen(model, state):
    if model == 0:
        import models.main as model
    elif model == 1:
        import models.worse as model
    elif model == 2:
        import models.clusterfuck as model
    
    return model.generate(state)

choice = randint(0,2)
state = randint(1,4)

text = gen(choice, state)

print(text)