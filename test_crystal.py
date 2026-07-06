import sys
sys.path.insert(0, 'qou-mass/src')
from qou_mass.type_b_crystal import BnVectorNode, get_highest_weight_nodes, build_connected_component

# Test B_2 vector representation tensor square: B(omega_1) (x) B(omega_1)
n = 2
hws = get_highest_weight_nodes(n, 2)
print(f"Number of highest weight nodes in B(omega_1)^2 for B_{n}:", len(hws))
for hw in hws:
    comp = build_connected_component(hw, n)
    print(f"HW node {hw} with weight {hw.wt()} generates component of size {len(comp)}")
