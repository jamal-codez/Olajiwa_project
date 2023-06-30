from django import template

register= template.Library()

@register.filter

def f_price(price):
    # Convert the price to a string
    price_str = str(price)
    
    # Determine the position of the decimal point (if any)
    decimal_pos = price_str.find('.')
    
    # Split the string into the integer and decimal parts
    if decimal_pos != -1:
        integer_part = price_str[:decimal_pos]
        decimal_part = price_str[decimal_pos:]
    else:
        integer_part = price_str
        decimal_part = ''
    
    # Add commas to the integer part
    formatted_integer = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i != 0 and i % 3 == 0:
            formatted_integer += ','
        formatted_integer += digit
    
    # Reverse the formatted integer part to get the correct order
    formatted_integer = formatted_integer[::-1]
    
    # Combine the formatted parts and return the result
    formatted_price = formatted_integer + decimal_part
    return formatted_price
