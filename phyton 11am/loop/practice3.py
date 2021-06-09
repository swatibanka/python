text = "AABBCCDDEE"
result = ''
for x in text:
    if x not in result:
        result = result + x
print(result)
