
print("Break")
for i in range(1, 21):
    if i == 11:
        break # breaks the loop where value is matched from if condition
    print(i)

print("Continue")
for i in range(1, 21):
    if i == 11:
        continue #skips the match value mentioned in if condition
    print(i)


print("pass")
for i in range(1, 21):
    if i == 11:
        pass # does nothing
    print(i)
