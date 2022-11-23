# Formatinger
Formats your telephone numbers and email.

# Instalation

	pip install formatinger
	

# How it works

Formatinger accepts telephone number or E-Mail for formating to normal, hidden view.
If selected type of formating - "showed" to telephone number, then number symbols will be splited to sections. If hidden, then also symbols in zones - CCC and DD will be replaced to sign - "\*". In E-Mail all symbols except first and last will be replaced to sign - "\*"


# What is useful for

This script could use in softwares which collect users telephone numbers amd E-Mails for more beautiful displays.


# Examples

### Telephone number formating

	Show: ABBBCCCDDEE -> A (BBB) CCC DD-EE
	Hidden: ABBBCCCDDEE -> A (BBB) *** **-EE
	
### E-Mail formating

	mailadress@gmail.com -> m********s@gmail.com
