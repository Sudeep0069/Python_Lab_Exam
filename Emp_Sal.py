'''
Question 4: Employee Salary Analysis 
A company stores employee salaries in a list. Write a function to 
calculate the average salary, display salaries above the average, 
and increase every salary by 10%. 
'''
sal=[10000,20000,15000,25000,30000,20000]
def emp_sal_analysis(sal:list):
    avg= sum(sal)/len(sal)
    abv_avg_sal=[sal for sal in sal if sal>avg]
    sal2=[sal*1.1 for sal in sal]
    return avg,abv_avg_sal,sal2
print('Average salary={}\nAbove average salaries={}\nSalaries after "10%" increment={}'.format(*emp_sal_analysis(sal)))