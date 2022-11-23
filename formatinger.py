# Exceptions

class FormatingError(Exception):
    pass

class NumberlError(Exception):
    pass

class EmailError(Exception):
    pass

# /. Exceptions

def number(obj: str, hidden=False) -> str:
    '''Formating object to number form.

    Transmissed object will be formated to A (BBB) CCC DD-EE
    If "hidden" is True, then object will be formated to A (BBB) *** **-EE'''

    if isinstance(obj, str):
        symbols = list(reversed(list(str(obj)))) # number symbols

        if len(symbols) <= 15:
            if hidden == True:
                number = '{0} ({1}) *** **-{2}'.format( 

                    ''.join(list(reversed(symbols[10:]))),
                    ''.join(list(reversed(symbols[7:10]))),
                    ''.join(list(reversed(symbols[0:2]))),

                )

            elif hidden == False:
                number = '{0} ({1}) {2} {3}-{4}'.format( 

                    ''.join(list(reversed(symbols[10:]))),
                    ''.join(list(reversed(symbols[7:10]))),
                    ''.join(list(reversed(symbols[4:7]))),
                    ''.join(list(reversed(symbols[2:4]))),
                    ''.join(list(reversed(symbols[0:2]))),

                )

            return number

        else:
            raise NumberError('The phone number can consist of a maximum of 15 characters. The signs - "+" and country codes are taken into account.')

    else:
        raise FormatingError('The passed object for formatting must be of type str')


def email(obj: str) -> str:
    '''Formating email to hidden type.

    After foramtting email it will become hidden.
    Before - itsmail@gmail.com, After - i*****l@gmail.com'''

    if isinstance(obj, str):
        if '@' in list(obj):
            email_elements = obj.split('@') # email spliting in elements - [email_adress, email_service.domain]

            email = '{0}*****{1}@{2}'.format(

                list(email_elements[0])[0], # first latter in name user email adress
                list(email_elements[0])[-1], # final latter in name user email adress
                email_elements[1]

            )

            return email

        else:
            raise EmailError('Email must have sign - "@".')

    else:
        raise FormatingError('The passed object for formatting must be of type str')
