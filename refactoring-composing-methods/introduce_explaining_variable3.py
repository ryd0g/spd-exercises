# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cooked_temp = time * temperature * temperature * pressure * COOKED_CONSTANT
    if desired_state == 'well-done' and cooked_temp >= WELL_DONE:
        return True
    if desired_state == 'medium' and cooked_temp >= MEDIUM:
        return True
    return False

print(is_cookeding_criteria_satisfied(5, 350, 200, 'medium'))