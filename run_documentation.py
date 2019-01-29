############################################################################################
# Create functions to use later on

def have_enough(input_1, given_1):
    """
    A function to determine if an input is greater than a given value
    and create a text output to guide users
    """
    # Check if the input is less than a given amount
    if input_1<given_1:
        # If True return a text string explaining that not enough things are given
        # formatting in the variables given in the function input
        return "You only have {input_1}. You should have at least {given_1}!".format(input_1=input_1, given_1=given_1)
    # When if statement above evaluates as False, do this
    else:
        # Return the following string explaining that enough things were given
        # formatting in the variables given as part of the function
        return "Good job! You needed {given_1} things and you have {input_1} things.".format(input_1=input_1, given_1=given_1)

def repeat_cycle(input_1, given_1):
    """
    A function to determine if an input is greater than a given value
    and create a boolean output of the condition
    """
    # Check if the input is less than a given amount
    if input_1<given_1:
        # If so return True
        return True
    # When if statement above evaluates as False, do this
    else:
        # Else return false
        return False

############################################################################################
# This is where your code acually starts. Everything above this point is actually functions
# that you have not yet run

# Initialize a value stating that you wish to repeat a cycle until some condition is met
repeat=True

# Begin a cycle that will repeat until the variable 'repeat' becomes false
# Think of a while statement like a for statement that only ends when the condition is met
# If it is not able to be met for some reason, it will spin on forever
while repeat:
    # Create a statement in the command line to induce a user response
    print ('How many things do you have? (Hint: It should be more than 5)')
    print ('Enter your answer below...')
    # Create a variable that records what numbers users type in the command line.
    collected_input_1=int(input())
    # Run the function above that evaluates if enough things are there and returns
    # output text
    have_enough_text=have_enough(input_1=collected_input_1, given_1=5)
    # Print the output text calculated as part of the have_enough function
    print(have_enough_text)
    # Recalculate the variable 'repeat' using the function defined above
    repeat=repeat_cycle(input_1=collected_input_1, given_1=5)
    # Now this iteration of the while statement is done
    # The while statement will evaluate the 'repeat' variable
    # If repeat is False, the while statement will close out
    # If repeat is True, the while statement will restart

# Print out a closing statement
print ('Thank you for playing How Many Things Do You Have!')
