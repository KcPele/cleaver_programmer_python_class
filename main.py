import re 

text = 'random string Myname123@website.com some more random text YourName13435@company.com'

pattern = re.compile('[a-yA-Y1-9]+@[a-yA-Y1-9]+\.[a-yA-Y]+')

result = pattern.findall(text)
print(result)

    