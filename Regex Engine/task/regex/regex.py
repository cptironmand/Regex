
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
