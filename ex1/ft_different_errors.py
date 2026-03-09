# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_different_errors.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 18:51:54 by orhernan         #+#    #+#              #
#    Updated: 2026/03/06 00:12:47 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def garden_operations(action: str) -> None:
    """
    Demonstrates common errors that can happen in a garden program.
    """
    match action:
        case "value":
            int("abc")
        case "zero":
            1 / 0
        case "file":
            f = open("missing.txt", "r")
            f.close()
        case "key":
            num_of_seeds = {"tomato": 10, "lettuce": 5}
            print(f"We have {num_of_seeds['missing_plant']}")
        case _:
            print("Unknown operation.")


def test_error_types() -> None:
    """Test and safely catch different types of errors."""
    test_cases = {
        "value": "ValueError",
        "zero": "ZeroDivisionError",
        "file": "FileNotFoundError",
        "key": "KeyError",
    }

    for action, error_name in test_cases.items():
        print(f"\nTesting {error_name}...")
        try:
            garden_operations(action)
        except ValueError as e:
            msg = e.args[0].split(" with ")[0]
            print(f"Caught {error_name}: {msg}")
        except ZeroDivisionError as e:
            print(f"Caught {error_name}: {e}")
        except FileNotFoundError as e:
            print(f"Caught {error_name}: {e.strerror} '{e.filename}'")
        except KeyError as e:
            print(f"Caught {error_name}: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
