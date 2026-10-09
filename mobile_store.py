'''
Question 2: Online Mobile Store 
An online store maintains a list of mobile prices. Write a function 
to display all mobiles costing more than ₹20,000, calculate the 
total inventory value, and find the most expensive mobile price. 
'''
mobiles=[15000,20000,30000,25000,35000,10000]
def mobile_stats(mobiles:list):
    return [i for i in mobiles if i>20000], sum(mobiles), max(mobiles)
print('mobiles costing more than 20000={}, total inventory value={}, most expensive mobile={}'.format(*mobile_stats(mobiles)))