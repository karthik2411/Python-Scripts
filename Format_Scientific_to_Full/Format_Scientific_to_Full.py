# Define a function to format a number in scientific notation to a full number
def format_scientific_to_full(value):
    parts = value.split('.')
    if len(parts) == 2:
        # If the value has a decimal point, remove trailing zeros
        integer_part, decimal_part = parts
        return integer_part.rstrip('0')
    else:
        # If there's no decimal point, return the original value
        return value



# Apply the function to the 'Consignment' column
df['Number'] = df['Number'].apply(format_scientific_to_full)