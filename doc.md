# Documentation

# Functions

All program functions are located in formatters

```python
from formatinger.formatters import number, email
```

# number

This function accepts 2 arguments, first - **obj** ( obligatory ), second - **hidden** ( optional )

**obj**

    Accepts telephone number which will be formatted.
    
**hidden**

    Accepts boolean value.
    
    If hidden is True, then telephone number will be hidden.
    Else if hidden is False, then telephone number will be just formatted.
    
    Default: False
    
    
### Example

```python 
from formatinger.formatters import number

number = '+01112223344'

showed_number = number(obj=number)
hidden_number = number(obj=number, hidden=True)

print(showed_number, hidden_number) # +0 (111) 222 33-44, +0 (111) *** **-44
```



# email

This function accepts 1 obligatory argument - **obj**

**obj**

    Accepts email which will be formated.
    
### Example

```python 
from formatinger.formatters import email

email = 'email_adress@gmail.com'

formated_email = email(obj=email)

print(formated_email) # e**********s@gmail.com
```
