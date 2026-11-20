"""qou-g0jn, pre-registration 3: do the lepton strands carry chirality?

Pre-registered in bean qou-g0jn (2026-11-15 19:55Z) before computing.
Leptons are taken as a second copy of the doublet V (ν = the K = q vector,
e = the other); this is an assumption about how leptons carry T³.

Q3a  dim End_{U_q}(V⊗V*) and its action on the W⁻ line (weight -1 of V⊗V*).
     The dual rep is ρ*(x) = ρ(S(x))^T, with Δ(E) = E⊗K + 1⊗E,
     Δ(F) = F⊗1 + K⁻¹⊗F, S(E) = -E K⁻¹, S(F) = -K F, S(K) = K⁻¹.
Q3b  chain amplitude n -> p e⁻ ν̄ = b_q · c · b_ℓ for the four left/right
     choices, with b = ±1/[2] (PR #7977, flavour_vertex_chirality_probe).
Exact sympy, no floats.
"""
from __future__ import annotations

import itertools
import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q, is_zero  # noqa: E402

E = sp.Matrix([[0, 1], [0, 0]])
F = E.T
K = sp.diag(q, 1 / q)
Ki = K.inv()
I2 = sp.eye(2)


def dual(M):
    return M.T


def q3a():
    Ed, Fd, Kd = dual(-E * Ki), dual(-K * F), dual(Ki)
    kr = sp.kronecker_product
    gens = [kr(K, Kd), kr(E, Kd) + kr(I2, Ed), kr(F, I2) + kr(Ki, Fd)]
    xs = sp.symbols("x0:16")
    X = sp.Matrix(4, 4, xs)
    eqs = []
    for G in gens:
        eqs += list(X * G - G * X)
    (sol,) = sp.linsolve(eqs, xs)
    Xs = X.subs(dict(zip(xs, sol)))
    free = sorted(set().union(*[sp.sympify(e).free_symbols for e in sol]) & set(xs), key=str)
    # W⁻ line: e2 ⊗ e^1  -> index 2*1 + 0 = 2 ; check its weight under Δ(K)
    wK = sp.simplify(gens[0][2, 2])
    basis = []
    for f in free:
        B = sp.simplify(Xs.subs({g: (1 if g == f else 0) for g in free}))
        v = sp.zeros(4, 1)
        v[2] = 1
        out = sp.simplify(B * v)
        scalar = all(out[i] == 0 for i in range(4) if i != 2)
        basis.append({"generator": str(f), "acts_on_W_minus_as_scalar": scalar,
                      "scalar": str(out[2]), "matrix": [[str(x) for x in r] for r in B.tolist()]})
    ok = len(free) == 2 and all(b["acts_on_W_minus_as_scalar"] for b in basis)
    return ok, {"commutant_dim": len(free), "W_minus_K_eigenvalue": str(wK), "basis": basis}


def q3b():
    b = {"L": q / (q**2 + 1), "R": -q / (q**2 + 1)}
    c = sp.Symbol("c")  # the single transfer scalar on the W⁻ line (Q3a)
    rows = []
    for (cq, cl) in itertools.product("LR", repeat=2):
        amp = sp.factor(b[cq] * c * b[cl])
        rows.append({"quark_vertex": cq, "lepton_vertex": cl, "amplitude": str(amp),
                     "abs_sq": str(sp.factor(amp**2))})
    mags = {sp.simplify(sp.sympify(r["abs_sq"], locals={"c": c})) for r in rows}
    return len(mags) == 1, rows


def main():
    ok_a, ra = q3a()
    ok_b, rb = q3b()
    res = {"producer": "computations/probes/lepton_strand_chirality_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); no floats", "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "probe never reads q0: every quantity is exact over Q(q) (sympy), with q a free symbol; its import cone (w_braid_reconcile_probe) evaluates nothing at a substrate pin",
           "assumption": "leptons = second copy of doublet V (nu = K=q vector)",
           "Q3a_transfer": ra, "Q3b_chain_amplitudes": rb,
           "checks": {"Q3a_dim2_scalar_on_W_minus": ok_a, "Q3b_same_magnitude_all_four": ok_b}}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("lepton-strand-chirality.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    assert ok_a


if __name__ == "__main__":
    main()
