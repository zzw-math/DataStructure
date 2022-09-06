#%%
from stack_folder.array_stack import ArrayStack


#%% 翻转数据
def reverse_data(S):
    L = ArrayStack()
    for i in range(len(S)):
        L.push(S.pop())
    return L


s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
print(s)
l = reverse_data(s)
print(l)


#%% 括号匹配
def is_matched(expr):
    """ Return True if all delimiters are properly match; False otherwise.
    """
    left = '({[' # opening delims
    right = ')}]' # closing delims
    S = ArrayStack()
    for c in expr:
        if c in left:
            S.push(c) # push left delim on stack
        elif c in right:
            if S.is_empty():
                return False # nothing to match with
            if right.index(c) != left.index(S.pop()): # 做了两件事
                return False # mismatched
    return S.is_empty()


expr = '[(5 + x) - (y + z)]'
if is_matched(expr):
    print(f" In {expr}: delimiters are matched")
else:
    print(f" In {expr}: delimiters are NOT matched")


#%% html匹配
def is_matched_html(raw):
    """ Return True if all HTML tags are properly match; False otherwise.
    """
    S = ArrayStack()           # find first '<'
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1) # find next '>'
        if k == -1:
            return False # invalid tag
        tag = raw[j+1:k] # strip away < >
        if not tag.startswith('/'): # this is opening tag
            S.push(tag)
        else: # this is closing tag
            if S.is_empty():
                return False # nothing to match with
            if tag[1:] != S.pop():
                return False # mismatched # find next '<'
        j = raw.find('<', k+1)
    return S.is_empty()

