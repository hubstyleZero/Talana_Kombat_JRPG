def validacion_input(input_data, allowed, limit):
    if len(input_data) > limit:
        return True
    elif any(x not in allowed for x in input_data):
        return True
    else:
        return False