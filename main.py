def read_datas():
    """read all datas"""
    h_start = float(input("Beginning height [ m ]: "))
    v_start = float(input("Beginning speed [ m/s ]: "))

    if h_start < 10:
        print("Height is to low ( min 10[m] )!")
        return None

    if v_start < 2:
        print("Speed is to low ( min 2[m/s] )!")
        return None

    return (h_start, v_start)


initial_values = None
while initial_values is None:
    print("Please, write all data to generate chart.")
    initial_values = read_datas()

print("Data OK")
