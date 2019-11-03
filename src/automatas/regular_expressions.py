import re

date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')
print(re.match(date_regex, '2019-09-03'))
