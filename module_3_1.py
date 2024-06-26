calls = 0


def cont_calls():
    global calls
    calls += 1


def string_info(string):
    cont_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    cont_calls()
    lower_list = [i.lower() for i in list_to_search]
    if string.lower() in lower_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
