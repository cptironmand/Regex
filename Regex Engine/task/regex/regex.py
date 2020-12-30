# write your code here



def input_string():
    the_input = input()
    index_no = the_input.index("|")
    reg = the_input[0:index_no]
    ts = the_input[index_no+1:]
    return reg, ts

def quick_compare(reg, ts):
    if reg in ts:
        return True
    elif not reg:
        return True
    elif not ts:
        return False
    elif (reg == "") and (ts == ""):
        return True


def evaluate(reg, ts):
    eval = quick_compare(reg, ts)
    if eval:
        return True
    else:
        str_len = len(ts)
        reg_len = len(reg)

        if reg_len > str_len:
            return False

        if "." in reg:
            if reg_len <= str_len:
                dot_index = reg.index(".")
                reg_minus_dot = reg[dot_index+1:]
                if reg_minus_dot in ts:
                    return True
    return False



# Main Body
regex, the_string = input_string()
print(evaluate(regex, the_string))
