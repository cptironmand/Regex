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


# NEED TO REVISIT THIS - DON'T THINK I WANT TO DO IT THIS WAY
def starting(reg, ts):
    # function to determine if there is a karat leading the reg
    # and if so, to return the reg without the karat and ts strings accordingly
    # so that they are the same length
    if reg[0] == "^":
        reg_ev = reg[1:]
        length = len(reg_ev)
        ts_ev = ts[0:length]
        return reg_ev, ts_ev
    return reg, ts


# NEED TO REVISIT THIS - DON'T THINK I WANT TO DO IT THIS WAY
def ending(reg, ts):
    #funciton to determine if there is a dollar sign ending the reg
    # adn if so, to return the reg without the $ and ts strings accordingly
    # so that they are the same length
    if reg[-1] == '$':
        reg_ev = reg[0:-1]
        if len(ts) >= len(reg_ev):
            ts_ev = ts[-len(reg_ev):] # Grab the last x characters in ts as ts_ev
            return reg_ev, ts_ev
    return reg, ts


def evaluate(reg, ts):
    ev = quick_compare(reg, ts)
    #print(f"ev = {ev}")
    if ev:
        return True
    if reg and ts:
        if (reg[0] == ".") or (reg[0] == ts[0]):
            reg_ev = reg[1:]
            #print(reg_ev)
            ts_ev = ts[1:]
            #print(ts_ev)
            return evaluate(reg_ev, ts_ev)
        elif (reg[0] != ts[0]):
            return False
    else:
        return False


# Main Body
regex, the_string = input_strings()
print(evaluate(regex, the_string))
