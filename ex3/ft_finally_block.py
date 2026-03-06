# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_finally_block.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/06 21:56:25 by orhernan         #+#    #+#              #
#    Updated: 2026/03/06 22:37:07 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def water_plants(plant_list: list[str]) -> None:
    """Water a list of plants, ensuring the system is always closed."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    """Demonstrates normal operations and error recovery using finally."""
    plants = ["tomato", "lettuce", "carrots"]
    print("\nTesting normal watering...")
    water_plants(plants)
    plants = ["tomato", None, "lettuce", "carrots"]
    print("\nTesting with error...")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
