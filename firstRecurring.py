class FirstRecurringCharacter:

    def first_recurring(self, given_string):
        count_char = {}
        for chr in given_string:
            if chr in count_char:
                return chr
            count_char[chr] = 1
        return None

first_recurring_character = FirstRecurringCharacter()
result = first_recurring_character.first_recurring("ABCD")
print(result)