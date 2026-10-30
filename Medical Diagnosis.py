facts = {"fever", "cough", "headache"}
rules = [
    (["fever", "cough"], "flu"),
    (["fever", "headache"], "viral_fever"),
    (["flu", "headache"], "severe_flu")
]
def forward_chaining(facts):
    facts = set(facts)
    changed = True
    while changed:
        changed = False
        for conditions, result in rules:
            if all(condition in facts for condition in conditions):
                if result not in facts:
                    facts.add(result)
                    changed = True
    return facts
def backward_chaining(goal, facts):
    if goal in facts:
        return True
    for conditions, result in rules:
        if result == goal:
            if all(backward_chaining(c, facts) for c in conditions):
                return True
    return False
result = forward_chaining(facts)
print("Facts after Forward Chaining:")
for fact in result:
    print(fact)
print("\nBackward Chaining:")
if backward_chaining("severe_flu", facts):
    print("Severe Flu can be diagnosed")
else:
    print("Severe Flu cannot be diagnosed")
