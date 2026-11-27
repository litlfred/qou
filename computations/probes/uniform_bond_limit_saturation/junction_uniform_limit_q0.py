"""Junction-only vs all-vertex uniform bond limit at q0 by power averaging. Usage: python3 junction_uniform_limit_q0.py A"""
import sys, itertools
from pathlib import Path
A = int(sys.argv[1])
P = Path(__file__).resolve().parents[1] / "bond_rules_length_bound"
sys.path[:0] = [str(P), str(P.parent / "binding_ceiling_q0"), str(P.parents[1] / "substrate"), str(P.parents[1])]
sys.argv = ["x", str(A)]
import bond_rules_length_bound_probe as br
mp, bc = br.mp, br.bc
N, STATES = br.N, br.STATES
print("junctions", br.JUNCTIONS, "NV", br.NV)
x_word = [(s + 3 * a, i) for a in range(A) for (s, i) in bc.V(0) * 3]
X = br.op_blocks(x_word); trx = br.trace_blocks(X)
Vb = {s: br.op_blocks(bc.V(s)) for s in range(br.NV)}
E0 = mp.mpf("4.2274833556290305503")
def limit(verts, label, LP=1024):
    S = {k: sum((Vb[s][k] for s in verts), mp.zeros(len(STATES[k]), len(STATES[k]))) for k in STATES}
    rho = mp.mpf(len(verts))
    M = {k: S[k] / rho for k in STATES}
    L = 1; out = []
    while L <= LP:
        r = br.trace_blocks({k: M[k] * X[k] for k in STATES}) / trx
        out.append((L, r))
        M = {k: M[k] * M[k] for k in STATES}; L *= 2
    for L, r in out[-4:]:
        print(label, "L", L, "r", mp.nstr(r, 15), "B", mp.nstr(-E0 * mp.log(r), 10) if r > 0 else None)
junc = sorted(set(s for J in br.JUNCTIONS for s in J))
limit(list(range(br.NV)), "all")
limit(junc, "junc")
