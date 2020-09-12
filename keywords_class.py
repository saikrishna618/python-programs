# # import keyword
# # print(len(keyword.kwlist))
# # # # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# # # # 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# # # #  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
# # # #  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# # # #  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# a = 0
# while a<3:
#     pin=input("Enter pin value")
#     if pin=="1234":
#         account=input("Enter Account type")
#         if account=="savings":
#             amount=int(input("Enter the Amount"))
#             if amount <=5000:
#                 print("Transaction is Successfull") 
#             else:
#                 print("Transaction Unsuccesfull")
#         elif account=="current":
#             print("current account is activated")
#             break
#         elif account=="personal":
#             print("check balance")   
#             break
#         else:
#             print("Account type invalid")
#             a=a+1
#             # break
#     else:
#         a=a+1   
#         #if a != 3:
#         print("ur pin is invalid, please try again") 
# print("Your account is blocked for 24 hours")