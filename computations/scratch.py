quaternion_quantum = 2.277455  # Phase density quantum
target = 2.224566
kashiwara = 1.0/32.0

print(f"Target Deuteron Binding: {target}")
print(f"quaternion_quantum: {quaternion_quantum}")
print("quaternion_quantum - target:", quaternion_quantum - target)
print("difference * 32:", (quaternion_quantum - target) * 32)
print("quaternion_quantum * (1 - 1/32):", quaternion_quantum * (1 - kashiwara))
