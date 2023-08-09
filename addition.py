'''import datetime
thisday = datetime.date.today()
thisyear = thisday.strftime("%Y")

print(thisyear)
# users = CustomUser.objects.filter(int(date_of_birth.strftime("%Y")))__lte=20)'''




# balanced_dict = {
#     '(':')',
#     '{':'}',
#     '[':']',
# }
# unbalanced_dict = {
#     '(':')',
#     '{':'}',
#     '[':']',
# }


# def check_order(string):
#     count = 0

#     if len(string) >= 2:
#         if string.count('(') == string.count(')') and string.count('{') == string.count('}') and string.count('[') == string.count(']'):
#             for i in string:

#                 if ('(') in string:
#                     string.remove('(')

#                     string.remove(')')
#                 print(string)

#                 if ('{') in string:
#                     string.remove('{')
#                     string.remove('}')
#                     print(string)
#                 if ('[') in string:
#                     string.remove('[')
#                     string.remove(']')
#                 print(string)
#                 return 'balanced'
#         else:
#             return 'Not balanced'    
        
#     else:
#         return "Not balanced"
# inputstring = "){([]}(())"
# liststring = list(inputstring)

# print(check_order(liststring))


# inputstring = "[{(}]"
# def check_inputstring(your_list):
#     open_list = ["[", "{", "("]
#     close_list = ["]", "}", ")"]
#     pushed_open = []
#     for i in your_list:
#         if i in open_list:
#             pushed_open.append(i)
#         elif i in close_list:
#             if len(pushed_open)==0:
#                 return 'unbalanced'
#             open_position = open_list.index(pushed_open.pop())
#             close_position = close_list.index(i)
#             if open_position!= close_position:
#                 return 'unbalanced'
#     if len(pushed_open)==0:
#         return 'balanced'
#     else:
#         return 'unbalanced'

# inputstring = ']'

# print(check_inputstring(inputstring))
'''def check_inputstring(your_list):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    for i in your_list:
        if i in open_list:
            open_yourlist_position = your_list.index(i)
            open_position = open_list.index(i)
            close_position_element = close_list[open_position]
            close_yourlist_position = your_list.index(close_position_element)
            if open_yourlist_position < close_yourlist_position:
                return 'balanced'
            else:
                return 'unbalanced'
        else:
            pass           

        '''
        


