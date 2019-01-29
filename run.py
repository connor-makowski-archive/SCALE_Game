def have_enough(input_1, given_1):
    if input_1<given_1:
        return "You only have {input_1}. You should have at least {given_1}!".format(input_1=input_1, given_1=given_1)
    else:
        return "Good job! You needed {given_1} things and you have {input_1} things.".format(input_1=input_1, given_1=given_1)

def repeat_cycle(input_1, given_1):
    if input_1<given_1:
        return True
    else:
        return False

repeat=True

while repeat:
    print ('How many things do you have? (Hint: It should be more than 5)')
    print ('Enter your answer below...')
    collected_input_1=int(input())
    have_enough_text=have_enough(input_1=collected_input_1, given_1=5)
    print(have_enough_text)
    repeat=repeat_cycle(input_1=collected_input_1, given_1=5)

print ('Thank you for playing How Many Things Do You Have!')
