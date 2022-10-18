# A musical scale can be described in the serial system with the numbers 1 through 12
# 12 can also be equivalent to 0 in this system
# In fixed Do, 1 would be equivalent to the note "C Natural"
# In movable Do, all rules are off

# The Major Scale would have the serial numbers:

major_scale = [1, 3, 5, 6, 8, 10, 12, 1]


def translate_scale(new_note):
    new_scale = []
    for i in major_scale:
        if i + (new_note - 1) < 13:
            new_scale.append(i + (new_note - 1))
        elif i + (new_note - 1) >= 13:
            new_scale.append((i + new_note - 1) - 12)

    print(new_scale)

translate_scale(int(input("Number between 1 and 12?")))