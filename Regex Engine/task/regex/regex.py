# reg stands for the regression variable
# ts is the string variable
# _ev means the variable has been evaluated

def input_strings():
    the_input = input()
    index_no = the_input.index("|")
    reg = the_input[0:index_no]
    ts = the_input[index_no+1:]
    return reg, ts


def quick_compare(reg, ts):
    if reg in ts:
        return True
    elif reg == ts:
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
            return evaluate(reg_ev, mod_string)
        elif reg[0] != ts[0]:
            return False
    else:
        return False


# Main Body
regex, the_string = input_strings()
print(evaluate(regex, the_string))
