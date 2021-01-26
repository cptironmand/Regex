# reg stands for the regex variable in a function
# ts is the string variable in a function
# _ev means the variable has been evaluated

counter = 0


def input_strings():
    the_input = input()
    index_no = the_input.index("|")
    reg = the_input[0:index_no]
    ts = the_input[index_no+1:]
    return reg, ts


def checkdowns(reg):
    slash_in = False
    start_in = False
    end_in = False
    question_in = False
    star_in = False
    plus_in = False
    if "\\" in reg:
        slash_in = True
    if "^" in reg:
        if "^" == reg[0]:
            start_in = True
    if "$" in reg:
        if "$" == reg[-1] and "\\" != reg[-2]:
            end_in = True
    if "?" in reg:
        q_index = reg.index("?")
        if reg[q_index-1] != "\\":
            question_in = True
    if "*" in reg:
        s_index = reg.index("*")
        if reg[s_index-1] != "\\":
            star_in = True
    if "+" in reg:
        p_index = reg.index("+")
        if reg[p_index-1] != "\\":
            plus_in = True
    return slash_in, start_in, end_in, question_in, star_in, plus_in


def quick_compare(reg, ts):
    global counter
    if counter == 0:
        if reg in ts:
            return True
        counter += 1
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


def remove_slash(reg):
    reg_ev = ""
    s = 0  # Count of all slashes
    t = 0  # running total slashes
    for letter in reg:
        if letter == "\\":
            s += 1

    for letter in reg:
        if letter != "\\":
            reg_ev += letter
        if letter == "\\":
            t += 1
            i = reg.index(letter)
            if reg[i+1] == "\\" and s > t:
                reg_ev += letter
    return reg_ev


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
    ind = reg.index("?")
    # Preceding char occurs 1 times
    if (len(reg) - (len(ts))) == 1:   # Check for only the '$'
        reg_ev = reg[0:ind] + reg[ind+1:]
        return reg_ev
    # Preceding char occurs 0 times
    elif len(reg) - (len(ts)) == 2:  # Check for the "$' plus 1 char
        reg_ev = reg[0:ind-1] + reg[ind+1:]
        return reg_ev
    else:
        reg_ev = reg[0:ind] + reg[ind+1:]
    return reg_ev


def check_star(reg, ts):  # Preceding char occurs 0 or more times
    ind = reg.index("*")
    # Preceding char occurs 0 times
    if len(reg) - len(ts) == 2:
        reg_ev = reg[0:ind - 1] + reg[ind + 1:]
    # Preceding character occurs 1 or more times
    else:
        reg_test = reg[0:ind] + reg[ind+1:]
        need = len(ts) - len(reg_test)
        reg_ev = reg[0:ind] + (reg[ind-1]*need) + reg[ind+1:]
    return reg_ev


def check_plus(reg, ts):  # Preceding char occurs 1 or more times
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

slash, start, end, question, star, plus = checkdowns(regex)

if slash:
    regex = remove_slash(regex)

if start and end:
    regex, the_string = check_start_end(regex, the_string)

if start and not end:
    regex, the_string = starting(regex, the_string)

if end and not start:
    regex, the_string = ending(regex, the_string)

if question:
    regex = check_questionmark(regex, the_string)

if star:
    regex = check_star(regex, the_string)

if plus:
    regex = check_plus(regex, the_string)

print(evaluate(regex, the_string))
