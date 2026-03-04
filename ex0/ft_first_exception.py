# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   ft_first_exception.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: orhernan <ohercelli@gmail.com>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2026/03/04 22:22:39 by orhernan          #+#    #+#              #
#   Updated: 2026/03/04 22:22:39 by orhernan         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def check_temperature(temp_str) -> int | None:
    """
    Validates temperature string for agricultural use.
    Returns the temperature as a integer if valid, otherwise prints an error.
    """
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}ºC is too cold for platns (min 0ºC)\n")
            return None
        if temp > 40:
            print(f"Error: {temp}ºC is too hot for plants (max 40ºC)\n")
            return None
        return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input():
    """Demo: validation pipeline with various inputs."""
    print("=== Garden Temperature Checker ===\n")

    test_cases = ["25", "abc", "100", "-50"]

    for test in test_cases:
        print(f"Testing temperature: {test}")
        result = check_temperature(test)
        if result is not None:
            print(f"Temperature {result}ºC is perfect for plants!\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
