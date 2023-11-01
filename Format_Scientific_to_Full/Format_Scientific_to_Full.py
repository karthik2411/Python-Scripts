def format_scientific_to_full(value):
    # Convert the value to a string
    value_str = str(value)
    parts = value_str.split('.')
    if len(parts) == 2:
        # If the value has a decimal point, remove trailing zeros
        integer_part, decimal_part = parts
        return integer_part.rstrip('0')
    else:
        # If there's no decimal point, return the original value
        return value_str


# Apply the function to the 'Consignment' column
df['Number'] = df['Number'].apply(format_scientific_to_full)
