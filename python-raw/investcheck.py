import random

risk_profiles = {
    'low': {'DC': 4, 'effect_percentage': 0.75},
    'significant': {'DC': 6, 'effect_percentage': 1.5},
    'high': {'DC': 8, 'effect_percentage': 2},
    'extreme': {'DC': 10, 'effect_percentage': 3},
    'ridiculous': {'DC': 12, 'effect_percentage': 5}
}

def get_risk_profile(profile_name):
    """
    Get the DC and effect percentage for a given risk profile name.
    
    Args:
    profile_name (str): The name of the risk profile.

    Returns:
    tuple: A tuple containing the DC and effect percentage.
    """
    profile = risk_profiles.get(profile_name.lower())
    if profile is not None:
        return profile['DC'], profile['effect_percentage']
    else:
        raise ValueError("Invalid risk profile name. Choose from 'low', 'significant', 'high', 'extreme', 'ridiculous'.")

def main():
    try:
        profile_name = input("Enter risk profile (low, significant, high, extreme, ridiculous): ")
        invest_value = float(input("What is the value of the investment: "))
        dm_bonus = int(input("What is the total DM of the stat and skill used to manage the fund: "))

        DC, effect_percentage = get_risk_profile(profile_name)
        print(f"For the {profile_name} risk profile: DC = {DC}, Effect Percentage = {effect_percentage}%")

        event_die = random.randint(1, 36)
        print(f"The event die result is {event_die}")

        if event_die == 36:
            print("There is an event!")
        else:
            print("No Event this time")

        manager_roll = random.randint(1, 6) + random.randint(1, 6)
        print(f"Management roll is {manager_roll}")
        print(f"Roll with bonus is {manager_roll + dm_bonus}")

        effect = manager_roll + dm_bonus - DC
        print(f"Effect is {effect}")

        # Calculate the impact on the investment value
        investment_effect = invest_value * (effect_percentage / 100) * effect
        final_investment_value = invest_value + investment_effect

        # Round the final investment value to the nearest whole number
        final_investment_value_rounded = round(final_investment_value)
        print(f"Final investment value after applying effect: {final_investment_value_rounded}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()