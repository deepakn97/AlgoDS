from queue import LifoQueue

def isBalancedParanthesis(str):
    stack = LifoQueue(maxsize = 1000000);
    for s in str:
        if(s == '('):
            stack.push(s);
        else:
            if(stack.empty()):
                return False;
            stack.pop();
    return stack.empty();

def main():
    str = input();
    print(isBalancedParanthesis(str));

if __name__ == '__main__':
    main()
