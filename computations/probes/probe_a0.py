import json

with open('computations/habiro/habiro-coefficients-atomic.witness.json') as f:
    data = json.load(f)

p_a0 = data['results']['p (proton, A=1)']['habiro_coefficients'][0]['a_m']
n_a0 = data['results']['n (neutron, A=1)']['habiro_coefficients'][0]['a_m']

print("p a0:", p_a0)
print("n a0:", n_a0)
