# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/06 23:24:49 by orhernan         #+#    #+#              #
#    Updated: 2026/03/07 01:08:58 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        msg = f"Water level {water_level} is too low (min 1)"
        raise ValueError(msg)
    if water_level > 10:
        msg = f"Water level {water_level} is too high (max 10)"
        raise ValueError(msg)
    if sunlight_hours < 2:
        msg = f"Sunlight hours {sunlight_hours} is too low (min 2)"
        raise ValueError(msg)
    if sunlight_hours > 12:
        msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        raise ValueError(msg)
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("\nTesting good values...")
    try:
        msg = check_plant_health("tomato", 5, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        msg = check_plant_health("", 5, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        msg = check_plant_health("tomato", 15, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        msg = check_plant_health("tomato", 5, 0)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
