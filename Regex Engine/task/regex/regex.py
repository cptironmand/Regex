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
        var_letter = reg[ind-1]
        count = 0
        loop = len(ts)
        # Preceding char occurs 1 times
        if (len(reg) - (len(ts))) == 1:  # Check for only the '$'
            reg_ev = reg[0:ind] + reg[ind + 1:]
            return reg_ev
        else:
            for i in range(loop):
                if ts[i] == ts[i - 1]:
                    count +=1
            reg_ev = reg[0:ind-1] + (var_letter*(count)) + reg[ind+1:]
            return reg_ev
    else:
        return reg


def evaluate(reg, ts):
    ev = quick_compare(reg, ts)
    if ev:
        return True

    # Check starting and ending
    if reg[0] == "^":
        reg, ts = starting(reg, ts)
    if reg[-1] == '$':
        reg, ts = ending(reg, ts)

    # Run the regression
    if reg and ts:
        if (reg[0] == ".") or (reg[0] == ts[0]):
            reg_ev = reg[1:]
            mod_string = ts[1:]
            print(f'regression test - reg is {reg_ev} and string is {mod_string}')
            return evaluate(reg_ev, mod_string)
        elif reg[0] != ts[0]:
            return False
    else:
        return False

# Main Body
regex, the_string = input_strings()
#print(f'the regex after the input string function is {regex}')
regex = check_questionmark(regex, the_string)
#print(f'the regex after we check question mark is {regex}')
regex = check_star(regex, the_string)
#print(f'the regex after we check star is {regex}')
regex = check_plus(regex, the_string)
#print(f'the regex after we check plus is {regex}')
print(evaluate(regex, the_string))
