# To Run the Script
    1. Make sure you are in the in_debt directory
    2. Run 'python3 -m in_debt'
        ---> Looking at lines 135-136 I hard coded the user_ids for demonstration purposes
    
# To Run the Tests
    1. Go to the main/home directory
    2. Run 'python3 -m unittest discover -v'

# How I spent my time
    - I mainly focused on gathering requirements and coming up with a algorithm. Then spent
    the rest on implementing the code and test cases.

# Thought Process and Approach
    On a notepad I broke down the steps I would take. I started with the /debts endpoint 
    and checked if users owed any money. The reason I started with /debts is because someone
    can have debt owed and not be in a payment plan. if they did then I would go to /payment_plans 
    and /payments and calculate how much amount they owed after all of the payments they did.
    Finally, I return a json object with the user info plus an update on amount owed as well as
    payment plan activity. What I had was a condition map so if this condition 
    passed then go here and if this condition failed go there. After that I broke down
    each logic/condition into functions. I gathered up all of those functions 
    and made the main function 'is_in_payment_plan'. Also the 'users_in_payment_plans' can 
    return multiple user debt info given a list of user ids. You can use the 'is_in_payment_plan'
    for one user.

    If I had more time, I would spend writing negative/invalid test cases and making sure the code
    handles invalid inputs. Also the testing class uses the json data from the endpoints. I wanted to use
    mock json data for those test cases.

