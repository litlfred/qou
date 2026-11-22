"""qou-g0jn, pre-registration 2: does the flavour-changing vertex carry chirality?

Pre-registered in bean qou-g0jn (2026-11-15 19:43Z) before computing.

Every U_q-equivariant one-quark vertex V -> V ⊗ (V ⊗ V*) is
(a·1 + b·Ř) ⊗ id applied after coev, because
Hom(V, V⊗V⊗V*) ≅ End_{U_q}(V⊗V) = span{1, Ř} (checked below as C1:
the commutant of Δ(K), Δ(E), Δ(F) on V⊗V has dimension 2).
The W⁻ component u ⊗ (d ūbar) needs the Ř term (decay_coproduct_two_arm_probe
arm A gives coefficient 1 for b = 1), so its amplitude is b.

C2 computes b exactly, by expanding in {1, Ř}, for
  P₊ = (Ř + q⁻¹)/[2]   left line, eigenvalue q (|q| > 1, owner ruling)
  P₋ = (q − Ř)/[2]     right line, eigenvalue −q⁻¹
  W  = σ P_R + σ⁻¹ P_L, the corpus weak vertex (W − σ = −h P_L)
Prediction: |b| = 1/[2] on both lines, opposite sign.
Exact sympy, no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import R, h, q, is_zero  # noqa: E402

Q2 = q + 1 / q  # [2]


def c1_commutant_dim():
    E = sp.Matrix([[0, 1], [0, 0]])
    F = E.T
    K = sp.diag(q, 1 / q)
    I = sp.eye(2)
    gens = [sp.kronecker_product(K, K), sp.kronecker_product(E, K) + sp.kronecker_product(I, E),
            sp.kronecker_product(F, I) + sp.kronecker_product(sp.diag(1 / q, q), F)]
    xs = sp.symbols("x0:16")
    X = sp.Matrix(4, 4, xs)
    eqs = []
    for G in gens:
        eqs += list(X * G - G * X)
    sol = sp.linsolve(eqs, xs)
    (s,) = sol
    free = set().union(*[sp.sympify(e).free_symbols for e in s]) & set(xs)
    S = R("std")
    # Ř must commute too, as a sanity check of the coproduct convention
    ok_R = all(is_zero(S * G - G * S) for G in gens)
    return len(free) == 2 and ok_R, {"commutant_dim": len(free), "R_in_commutant": ok_R}


def coeffs(M, S):
    """Write M = a·1 + b·Ř and return (a, b)."""
    a, b = sp.symbols("a b")
    sol = sp.solve(list(M - a * sp.eye(4) - b * S), [a, b], dict=True)[0]
    return sp.simplify(sol[a]), sp.simplify(sol[b])


def c2_vertex_amplitudes():
    S = R("std")
    I = sp.eye(4)
    Pp = (S + I / q) / Q2
    Pm = (q * I - S) / Q2
    Sinv = S - h * I
    assert is_zero(Pp * Pp - Pp) and is_zero(Pm * Pm - Pm) and is_zero(Pp + Pm - I)
    assert is_zero(S * Pp - q * Pp) and is_zero(S * Pm + Pm / q)
    W = S * Pm + Sinv * Pp
    assert is_zero(W - S + h * Pp), "W - σ = -h P_L"
    rows = {}
    for name, M in (("P_plus_left", Pp), ("P_minus_right", Pm), ("W_weak_vertex", W)):
        a, b = coeffs(M, S)
        rows[name] = {"a_identity": str(a), "b_W_minus_amplitude": str(sp.factor(b)),
                      "abs_b_sq": str(sp.factor(b**2))}
    bp = sp.sympify(rows["P_plus_left"]["b_W_minus_amplitude"])
    bm = sp.sympify(rows["P_minus_right"]["b_W_minus_amplitude"])
    same_mag = sp.simplify(bp**2 - bm**2) == 0
    opp_sign = sp.simplify(bp + bm) == 0
    return {"rows": rows, "left_right_same_magnitude": same_mag, "left_right_opposite_sign": opp_sign}


def main():
    ok1, r1 = c1_commutant_dim()
    r2 = c2_vertex_amplitudes()
    res = {"producer": "computations/probes/flavour_vertex_chirality_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); no floats", "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "exact sympy arithmetic over Q(q) with q a free symbol; no substrate q0 is read or substituted",
           "C1_equivariant_vertex_space": r1, "C2_vertex_amplitudes": r2,
           "checks": {"C1": ok1, "prediction_same_magnitude_opposite_sign":
                      bool(r2["left_right_same_magnitude"] and r2["left_right_opposite_sign"])}}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("flavour-vertex-chirality.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    assert ok1


if __name__ == "__main__":
    main()
