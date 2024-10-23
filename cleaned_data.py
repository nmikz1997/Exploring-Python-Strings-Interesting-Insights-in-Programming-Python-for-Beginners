#In data science, strings are fundamental for cleaning and preparing data, such as stripping whitespace or replacing characters.

raw_data = " 42,   7.5, 19 "
cleaned_data = [float(item.strip()) for item in raw_data.split(",")]

print(cleaned_data)