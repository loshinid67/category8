facts = {
    "machine_on",
    "raw_material_available",
    "temperature_normal",
    "quality_good"
}
rules = [
    ({"machine_on", "raw_material_available"}, "production_start"),
    ({"temperature_high"}, "machine_stop"),
    ({"machine_fault"}, "machine_stop"),
    ({"production_start", "temperature_normal"}, "production_continue"),
    ({"quality_good"}, "product_approved")
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
print("Derived Facts:")
print(result)
print("\nBackward Chaining:")
if backward_chaining("production_continue", facts):
    print("Decision: Production can CONTINUE")
elif backward_chaining("machine_stop", facts):
    print("Decision: Machine must STOP")
else:
    print("Decision: No decision")
