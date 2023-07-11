import matplotlib.pyplot as plt


def read_datas():
    """read datas"""
    def float_input(user_info, user_prompt, min_value):
        print("---[ data loading ]---------")
        print(user_info)
        user_input = input(user_prompt)
        if user_input.count(".") > 1:
            return None

        if not user_input.replace(".", "").isdecimal():
            return None

        user_value = float(user_input)
        if user_value < min_value:
            print(f"Value {user_value} is lower that min value {min_value}!")
            return None
        return user_value

    h_start = None
    v_start = None

    while h_start is None:
        h_start = float_input(
            "Wrong height data value, it should be float type ( 3.14 )",
            "Write start height value [ m ]: ",
            10,
        )

    while v_start is None:
        v_start = float_input(
            "Wrong speed data value, it should be float type ( 3.14 )",
            "Write start speed value [ m/s ]: ",
            2,
        )

    return (h_start, v_start)


initial_values = None
while initial_values is None:
    print("Please, write all data to generate chart.")
    initial_values = read_datas()

print("Data OK")

# destroying tuple
H_START, V_START = initial_values

# calculating most important values
g = 9.81  # m/s^2
total_time = ((2 * H_START) / g) ** (1 / 2)
max_range = V_START * total_time

# generate chart, adding start point and finish point
title = f"""Horizontal projection chart, V_START = {V_START} [m/s], ( g={g} m/s^2 ), 
        flight time = {round(total_time, 4)} [s]"""

plt.scatter(0, H_START, label=f"H_START={H_START} [m]")
plt.scatter(max_range, 0, label=f"max_range={round(max_range, 3)} [m]")
plt.grid()
plt.title(title)
plt.legend()
plt.show()
