# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_management.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/08 01:37:26 by orhernan         #+#    #+#              #
#    Updated: 2026/03/08 21:06:18 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    """Base exception for all garden errors."""
    pass


class PlantError(GardenError):
    """Exception for problems with specific plants."""
    pass


class WaterError(GardenError):
    """Exception for problems with the watering system."""
    pass


class GardenManager:
    """Manages the garden operations and plant health."""

    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int
    ) -> None:
        """Adds a plant to the garden, validating the name."""
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": water_level, "sunlight": sunlight_hours}
            print(f"Added {name} to the garden.")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """Water all plants safely, ensuring cleanup always happens."""
        print("Opening watering system")
        try:
            if not self.plants:
                msg = "No plants to water! Watering system not started"
                raise WaterError(msg)
            for name in self.plants:
                if not name:
                    msg = f"Cannot water {name} - invalid plant!"
                    raise PlantError(msg)
                print(f"Watering {name}")
        except GardenError as e:
            print(f"Error: {e}")
            return
        finally:
            print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    def check_plant_health(self, name: str) -> str:
        """Checks plant health, routing to specific custom errors."""
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in the garden.")

        water = self.plants[name]["water"]
        sunlight = self.plants[name]["sunlight"]

        if water < 1:
            msg = f"Water level {water} is too low (min 1)"
            raise WaterError(msg)
        if water > 10:
            msg = f"Water level {water} is too high (max 10)"
            raise WaterError(msg)
        if sunlight < 2:
            msg = f"Sunlight hours {sunlight} is too low (min 2)"
            raise PlantError(msg)
        if sunlight > 12:
            msg = f"Sunlight hours {sunlight} is too high (max 12)"
            raise PlantError(msg)
        return f"healthy (water: {water}, sun: {sunlight})"


def test_garden_management() -> None:
    """Runs the full garden management lifecycle with custom errors."""
    print("=== Advanced Garden Management System ===")
    manager = GardenManager()

    print("\n--- Adding Plants ---")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 6)
    manager.add_plant("cactus", 3, 1)
    manager.add_plant("", 5, 5)

    print("\n--- Watering Cycle ---")
    manager.water_plants()

    print("\n--- Checking Health ---")
    for plant_name in manager.plants:
        try:
            msg = manager.check_plant_health(plant_name)
            print(f"{plant_name}: {msg}")
        except GardenError as e:
            print(f"Error checking {plant_name}: {e}")

    print("\nSystem successfully recovered from errors and continued running!")


if __name__ == "__main__":
    test_garden_management()
