# reg stands for the regex variable in a function
# ts is the string variable in a function
# _ev means the variable has been evaluated

import sys
sys.setrecursionlimit(10000)

counter = 0

def input_strings():
    the_input = input()
    index_no = the_input.index("|")
    reg = the_input[0:index_no]
    ts = the_input[index_no+1:]
    return reg, ts


def quick_compare(reg, ts):
    global counter
    if counter == 0:
        if reg in ts:
            return True
        counter +=1
    if reg == ts:
        return True
    elif not reg:
        return True
    elif not ts:
        return False
    elif (reg == "") and (ts == ""):
        return True
    else:
        return False


def starting(reg, ts):
    reg_ev = reg[1:]
    length = len(reg_ev)
    ts_ev = ts[0:length]
    return reg_ev, ts_ev


def ending(reg, ts):
    reg_ev = reg[0:-1]
    ts_ev = ts[-len(reg_ev):]  # Grab the last x characters in ts as ts_ev
    return reg_ev, ts_ev


def check_questionmark(reg, ts):  # Preceding char occurs 0 or 1 times
    if "?" in reg:
        ind = reg.index("?")
        # Preceding char occurs 1 times
        if (len(reg) - (len(ts))) == 1:   #  Check for only the '$'
            reg_ev = reg[0:ind] + reg[ind+1:]
            return reg_ev
        # Preceding char occurs 0 times
        elif (len(reg) - (len(ts)) == 2):  # Check for the "$' plus 1 char
            reg_ev = reg[0:ind-1] + reg[ind+1:]
            return reg_ev
        else:
            reg_ev = reg[0:ind] + reg[ind+1:]
        return reg_ev
    else:
        return reg


def check_star(reg, ts):  # Preceding char occurs 0 or more times
    if "*" in reg:
        ind = reg.index("*")
        # Preceding char occurs 0 times
        if (len(reg) - (len(ts)) == 2):
            reg_ev = reg[0:ind - 1] + reg[ind + 1:]
        # Preceding character occurs 1 or more times
        else:
            regtest = reg[0:ind] + reg[ind+1:]
            need = len(ts) - len(regtest)
            reg_ev = reg[0:ind] + (reg[ind-1]*need) + reg[ind+1:]
        return reg_ev
    else:
        return reg


def check_plus(reg, ts):  # Preceding char occurs 1 or more times
    if "+" in reg:
        ind = reg.index("+")
        char = reg[ind-1]
        count = 0
        beg = reg[0:ind]
        end = reg[ind+1:]

        # loop to find max number of reg chars
        for l in ts:
            if l == char:
                count +=1

        # Build a work in progress regex and test it while you build it for the length of 'count'
        for i in range(count):
            ev = evaluate((beg + char*i + end), ts)
            if ev:
                return (beg + char*i + end)

        return (beg + end)
    else:
        return reg

def check_start_end(reg, ts):
    # Check starting AND ending
    if "^" in reg and "$" in reg:
        ind = 0
        orig_reg = reg
        reg = reg[1:-1]
        # Make sure reg is as long as ts
        if len(reg) >= len(ts):
            return reg, ts
        if len(reg) < (len(ts)+1):
            if "+" in reg:
                ind = reg.index("+")
                var_char = reg[ind - 1]
                num = len(ts) - len(reg) + 1
                reg = reg[0:ind] + (var_char * num) + reg[ind:]
                return reg, ts
            elif "*" in reg:
                ind = reg.index("*")
                var_char = reg[ind-1]
                num = len(ts) - len(reg) + 1
                reg = reg[0:ind] + (var_char*num) + reg[ind:]
                return reg, ts
            else:
                reg = orig_reg
                return reg, ts
        #elif len(reg) >= len(ts):
         #   return reg, ts
        else:
            reg = orig_reg
            return reg, ts

    # Check starting OR ending
    if "^" in reg:
        reg, ts = starting(reg, ts)
    if '$' in reg:
        reg, ts = ending(reg, ts)

    return reg, ts


def evaluate(reg, ts):
    ev = quick_compare(reg, ts)
    if ev:
        return True

    # Run the regression
    if reg and ts:
        if (reg[0] == ".") or (reg[0] == ts[0]):
            reg_ev = reg[1:]
            mod_string = ts[1:]
            return evaluate(reg_ev, mod_string)
        elif reg[0] != ts[0]:
            return False
    else:
        return False

# Main Body
regex, the_string = input_strings()
#print(f'the regex after the input string function is {regex} and the string is {the_string}')
regex, the_string = check_start_end(regex, the_string)
#print(f'the regex after checking for starting / ending chars is {regex} and the string is {the_string}')
regex = check_questionmark(regex, the_string)
#print(f'the regex after we check question mark is {regex} and the string is {the_string}')
regex = check_star(regex, the_string)
#print(f'the regex after we check star is {regex} and the string is {the_string}')
regex = check_plus(regex, the_string)
#print(f'the regex after we check plus is {regex} and the string is {the_string}')
print(evaluate(regex, the_string))
