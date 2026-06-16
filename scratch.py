import sys
sys.path.insert(0, "./computations")
sys.path.insert(0, "./computations/substrate")
sys.path.insert(0, "./tools/qou-substrate/python")

from binding_canonical import binding_canonical

for Z, N, name, B_AME in [(3, 2, "5Li", 25.947), (3, 3, "6Li", 31.994)]:
    r = binding_canonical(Z, N, verbose=False)
    B_pred = r["B_MeV"]
    delta = B_AME / B_pred
    import math
    from q_parameter import Q as q0
    lnq = math.log(float(q0))
    x = math.log(delta) / lnq
    print(f"{name}: B_pred={B_pred}, Delta={delta}, log_q0(Delta)={x}")
