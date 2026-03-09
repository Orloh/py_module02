# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/06 21:16:35 by orhernan         #+#    #+#              #
#    Updated: 2026/03/06 21:43:32 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    """Basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


def trigger_plant_problem() -> None:
    """Triggers a PlantError."""
    raise PlantError("The tomato plant is wilting!")


def trigger_water_problem() -> None:
    """Triggers a WaterError."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Tests the creation o GardenErrors."""
    print("\nTesting PlantError...")
    try:
        trigger_plant_problem()
        print("No problems with plants")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        trigger_water_problem()
        print("No problems with watering")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    error_triggers = [trigger_plant_problem, trigger_water_problem]

    for trigger_function in error_triggers:
        try:
            trigger_function()
            print("No problems in the garden")
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
