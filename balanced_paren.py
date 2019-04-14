from stack import Stack
def par_checker(string):
    s = Stack()
    for ch in string:
        if ch == "(":
            s.push(ch)
        if ch == ")":
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()

if __name__ == '__main__':
    srting = input()
    if par_checker(srting):
        print('() is balanced.')
    else:
        print("() is not balanced.")