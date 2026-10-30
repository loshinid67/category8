facts = {
    "traffic_light_green",
    "road_clear",
    "pedestrian_absent"
}
rules = [
    ({"traffic_light_green", "road_clear"}, "move"),
    ({"traffic_light_red"}, "stop"),
    ({"pedestrian_present"}, "stop"),
    ({"obstacle_present"}, "stop"),
    ({"road_clear", "pedestrian_absent"}, "safe_to_move")
]
def forward_chaining(facts):
    new_facts = set(facts)
    changed = True
    while changed:
        changed = False
        for conditions, result in rules:
            if conditions.issubset(new_facts):
                if result not in new_facts:
                    new_facts.add(result)
                    changed = True
    return new_facts
def backward_chaining(goal, facts):
    if goal in facts:
        return True
    for conditions, result in rules:
        if result == goal:
            if all(backward_chaining(c, facts) for c in conditions):
                return True
    return False
result = forward_chaining(facts)
print("Initial Facts:")
print(facts)
print("\nForward Chaining:")
print("Derived Facts:", result)
print("\nBackward Chaining:")
if backward_chaining("move", facts):
    print("Action: Vehicle can MOVE")
elif backward_chaining("stop", facts):
    print("Action: Vehicle must STOP")
else:
    print("Action: No decision")
