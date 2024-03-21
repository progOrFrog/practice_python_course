import re

#Task 1. Write regexes that:

# remove all special (non-alphanumeric) characters from a string.
def sub_non_alphanumeric(string:str) -> str:
	return re.sub(r"[^a-zA-Z0-9]", "", string)

assert sub_non_alphanumeric("aaa@@2vsdiuowcdeABC~DE_12345_abcd") == \
	"aaa2vsdiuowcdeABCDE12345abcd"

assert sub_non_alphanumeric("qwerty125_fjso39%!$^#*#fmoe2tj") == \
	"qwerty125fjso39fmoe2tj"
#match a word that contains a given character (e.g. ”y”)
def match_word(words:str) -> list:
    return re.findall(r"[a-zA-Z]*y[a-zA-Z]*", words)

sentence = "Professor Abdolmalek, please report your absences promptly asgfsgfs."
sentence2 = "Python Regular Expressions"

assert match_word(sentence) == ['your', 'promptly']

assert match_word(sentence2) == ['Python']
#match a word that is n characters long
def match_word_n_char_long(words, n) -> list:
    return re.findall(r"\b\w{%d}\b" % n, words)

n = 4
text = "It has survived not only five centuries but also the leap into \
electronic typesetting, remaining essentially unchanged"

assert match_word_n_char_long(text, n) == ['only', 'five', 'also', 'leap', 'into']
#match a word facthat begins with ”a” OR ”b” and ends with ”s”.
def match_word_from_a_b_to_s(words:str) -> list:
    return re.findall(r"\b[a|b]\w+s\b", words)

text1 = "Lorem Ipsum is simply dummy text of the printing and typesetting \
industry. Lorem Ipsum has been the industry's standard dummy text ever since \
the 1500s, when an unknown printer took a galley of type and scrambled it to \
make a type specimen book. It has survived not only five centuries, but also \
the leap into electronic typesetting, remaining essentially unchanged. \
It was popularised in the 1960s with the release of Letraset sheets containing \
Lorem Ipsum passages, and more recently with desktop publishing software like \
Aldus PageMaker including versions of Lorem Ipsum."

text2 = "adress bonus desktop paper clear analysis ashes"

assert match_word_from_a_b_to_s(text1) == []

assert match_word_from_a_b_to_s(text2) == ["adress", "bonus", "analysis", "ashes"]


#Task 2. Write a program that will
#collect all monetary amounts from a given text
#Example: ” first amount is $123.45, second amount is $400” −> [123.45, 400].
def all_monetary_amounts_from_given_text(text:str):
    res = re.findall(r"\d+.?\d+", text)
    res_l = []
    for e in res:
        if "." in e:
            res_l.append(float(e))
        else:
            res_l.append(int(e))
    return res_l

text2_1 = "first amount is $123.45, second amount is $400"
numbers = all_monetary_amounts_from_given_text(text2_1)

assert all_monetary_amounts_from_given_text(text2_1) == [123.45, 400]
#convert these to float numbers
def convert_to_float(numbers:list):
    return list(map(float, numbers))

assert convert_to_float(numbers) == [123.45, 400.00]
#sum them
def sum_these(numbers):
    return sum(numbers)

assert sum_these(numbers) == 523.45

#Task 3. Write a program that will cleanup Python source code by:
#removing source code comments from Python code.
#removing blank lines (hint: use \r, \n special characters)

code = r'''# Ця програма обчислює факторіал числа, яке вводить користувач

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Запитуємо у користувача число
number = int(input("Введіть число для обчислення факторіалу: "))

# Обчислюємо факторіал та виводимо результат
result = factorial(number)

# Пустий рядок для розділення логічних блоків програми
# Виводимо повідомлення про завершення програми
print(finish)'''

def remove_comments(text:str):
    return re.sub(r".*#.*\n", "", text)

def remove_blank_lines(text:str):
    return re.sub(r'\n\s*\n', '\n', text)

print(remove_comments(code))

rem_code = remove_comments(code)

print(remove_blank_lines(rem_code))

#Task 4. Write a program that will convert dates in ”yyyy-mm-dd” format
#to ”dd-mm-yyyy” format. Example: 2024−02−11 −> 11−02−2024.

def convert_date(date): 
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date) 
    if match: 
        year = match.group(1) 
        month = match.group(2) 
        day = match.group(3) 
        return f"{day}-{month}-{year}" 
    else: 
        return "Invalid date format"

print(convert_date("2024-02-11"))