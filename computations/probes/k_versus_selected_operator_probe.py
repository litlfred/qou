#!/usr/bin/env python3
"""Does the selected operator have anything to do with `K`? No — and it cannot.

THE QUESTION
------------
`positive_sector_operator_selection_probe.py` found an operator `x*` by solving
`min t.x  s.t.  Gx >= u_demand,  x >= 0`, and
`positive_sector_q_stability_probe.py` showed the `T`/`3He` separation it
produces is structural in `q`. The remaining question is whether `x*` is related
to the binding operator `K` of the knot convolution
`T_w(atom) = K . (x)_i T_w(nucleon_i)`.

This is a **formal question about the Hecke data**, not a physical one, and it is
answered here symbolically wherever the algebra permits. No `B_AME`, no fit, no
physical input of any kind enters.

`K` IS EXACTLY COMPUTABLE
--------------------------
In the `H_3`-local model of `pyhecke.atom` every object is a 6-vector, so with

    P     = the product of the A nucleon NFs, no inter-nucleon crossings
    atom  = the same with the inter-nucleon crossings applied
    M_P   = the matrix of LEFT multiplication by P (column j is `P (x) b_j`)

the binding operator is `K = M_P^{-1} . atom`, defined whenever `M_P` is
invertible — which it is at every `A` tested. Electrons are excluded throughout:
they are the EM channel, not binding.

**At `A = 2` this reproduces the letter it must.** `build_atom_nf` applies
exactly one inter-nucleon letter after both nucleon blocks, so `K` must be that
letter, and the solve returns

    K(2H)  =  sigma_0 + D_PN . 1        (to 1e-12)

with `D_PN = pn_interface_offset(q)` the colour-weighted `p`-`n` offset. That is
the construction validating itself; everything below rests on it.

`K` IS NEVER IN THE POSITIVE SECTOR — AND THE INTERVAL IS EXACT
-----------------------------------------------------------------
`K(2H)` has exactly one negative NF coefficient, the `gamma` one, and it **is**
`D_PN`. So the question "is `K` in the positive sector?" is exactly "is
`D_PN > 0`?", and that is answerable in closed form. Symbolically,

    delta(q)  =  (q-1)^2 (q^4 - 1) / (3 q^4)
    D_PN(q)   =  (q^2 - 1) (-6 q^4 + (q-1)^2 (q^4 - 1)) / (12 q^5)

whose numerator factors as

    (q - 1)(q + 1)(q^6 - 2 q^5 - 5 q^4 - q^2 + 2 q - 1)

The sextic has exactly one real root above 1,

    q_c  =  3.458099300032797192042069...

so **`D_PN(q) < 0` precisely on `1 < q < q_c`**, and `D_PN > 0` beyond it. Hence

    K(2H) lies OUTSIDE the positive sector exactly on 1 < q < q_c

and `q_0 = 1.10998` sits at `q_0/q_c = 0.32098` — inside that interval by a
factor of about 3.12, not near either end. (An earlier draft of this claimed
`D_PN < 0` for *all* `q > 1`; that is false, and the root above is why. The
corrected statement is the interval.)

At `A >= 3` the same holds numerically at `q_0`, with more negative components:

    nucleus   # negative NF coefficients   most negative
    D                  1  (gamma)            -0.104458
    T                  3  (gamma, s0, L-)    -0.420972
    3He                3  (gamma, s0, L-)    -0.312087
    4He                3  (s0, L+, e-)       -0.305506
    6Li                4  (gamma, s1, L+, e-) -0.462318

SO THE ANSWER IS NO, STRUCTURALLY
-----------------------------------
The positive-sector LP has feasible set `{x >= 0}`. `K` is not in it. Not "does
not happen to be" — **cannot be**, on the whole interval `1 < q < q_c` that
contains `q_0` and the entire `q` range swept in the stability probe.

Nor is `x*` a rescaling of `K`. At `A = 2`, where `K` is exactly known:

    x*  =  [1.006994, 0.290774, 0, 0, 0, 0.192275]
    K   =  [-0.104458, 1, 0, 0, 0, 0]

Their shared support is `{gamma, sigma_0}`, and the ratios `x*/K` there are
`-9.640158` and `0.290774` — not equal, so not proportional even on the overlap.

THE STRUCTURAL READING
----------------------
`K` and `x*` are **complementary objects, not competing ones**, and the corpus's
own vocabulary says why. Negative NF coefficients enter only through
`T_i^{-1} = T_i - A` (`jet_history_retention_probe.py` §Q3), so they are the
inverse-crossing sector — what the owner's steer calls backwards in computational
time, the entanglement sector.

  - `K` is **defined** as the operator carrying the free constituents to the
    bound atom, and on `1 < q < q_c` it necessarily carries negative content.
  - `x*` is **defined** by excluding exactly that content.

So the LP was never going to return `K`, and the two answer different questions:
`x*` is the cheapest *forward-time* operator whose Frobenius profile covers the
free constituent product; `K` is the actual free-to-bound map, and it lives
partly in the reverse-time sector. The `T`/`3He` separation `x*` produces stands
as a structural fact about the Hecke data — it is simply not a fact about `K`.

⚠ INTERPRETATION, EXPLICITLY NOT DERIVED
------------------------------------------
One remark, flagged as interpretation and carrying no weight in anything above:
the entire negative content of `K(2H)` is `D_PN`, the `p`-`n` interface offset —
and the deuteron is the `p`-`n` bound system. Nothing here derives that
correspondence, no physical quantity enters the computation, and the match is
recorded only so a later reader finds it already labelled rather than
rediscovering it as a lead.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired; no tier change. The `D_PN` sign interval is
exact (sympy, closed form). The `A >= 3` coefficient counts and the `x*` vs `K`
comparison are f64 at `q_0`; both are sign and proportionality conclusions on
`O(1)` quantities. LP via scipy HiGHS, declared.

-- Ref: [manuscript] bean t7qv; positive_sector_operator_selection_probe.py;
   jet_history_retention_probe.py §Q3
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

from hecke_core import h  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from pyhecke.gram import G as G3  # noqa: E402
from pyhecke.gram import NF_NAMES, TR_M, hm  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

GM = np.asarray(G3, dtype=float)
TM = np.asarray(TR_M, dtype=float)
BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
ONE = [1.0, 0, 0, 0, 0, 0]
NUCLEI = (("D", 1, 1), ("T", 1, 2), ("He3", 2, 1), ("He4", 2, 2), ("Li6", 3, 3))


def _apply(nf, letters):
    for (c, d, g) in letters:
        nf = hm(nf, c, d, g)
    return nf


def nucleon_letters(kind: str) -> list:
    L = []
    for _ in range(3):
        L += [(1, 0, 0), (1, -h, 1)]
    L += ([(1, 0, 0), (1, -h / 2, 0), (1, -h / 2, 1)] if kind == "p"
          else [(1, -h / 2, 0), (1, -h / 2, 0), (1, -h, 1)])
    return L + [(1, 0, 0), (1, 0, 0)]


def inter_letter(a: str, b: str):
    if a == "p" and b == "p":
        return (1, 0, 0)
    if a == "n" and b == "n":
        return (1, -h, 0)
    return (1, D_PN, 0)


def ordering(Z: int, N: int) -> list:
    o, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            o.append("p")
            pc += 1
        else:
            o.append("n")
            nc += 1
    return o


def build(Z: int, N: int, with_inter: bool) -> np.ndarray:
    """Nuclear only — electrons excluded (EM channel, not binding)."""
    o = ordering(Z, N)
    nf = list(ONE)
    for k in range(len(o)):
        nf = _apply(nf, nucleon_letters(o[k]))
        if with_inter:
            for prev in range(k):
                nf = _apply(nf, [inter_letter(o[prev], o[k])])
    return np.asarray(nf, dtype=float)


def left_mul_matrix(P) -> np.ndarray:
    cols = []
    for w in BASIS:
        v = list(P)
        for g in w:
            v = hm(v, 1, 0, g)
        cols.append(v)
    return np.array(cols, dtype=float).T


def binding_operator(Z: int, N: int) -> np.ndarray:
    """`K = M_P^{-1} . atom` — the free-to-bound map in the H_3-local model."""
    P = build(Z, N, False)
    return np.linalg.solve(left_mul_matrix(P), build(Z, N, True))


def dpn_sign_interval():
    """Closed form for where `D_PN(q) < 0`."""
    q = sp.symbols("q", positive=True)
    dpn = sp.simplify(pn_interface_offset(q))
    numer = sp.factor(sp.numer(sp.together(dpn)))
    sextic = sp.Poly(sp.Integer(-6) * q ** 4 + (q - 1) ** 2 * (q ** 4 - 1), q)
    roots = [r for r in sp.real_roots(sextic) if r.evalf() > 1]
    return dpn, numer, sextic.as_expr(), (roots[0].evalf(25) if roots else None)


def main() -> int:
    assertions = []
    print("t7qv — does the selected operator have anything to do with K?")

    # ── A1. K reproduces the single pn letter at A = 2 ────────────────
    K_D = binding_operator(1, 1)
    expected = np.asarray(hm(list(ONE), 1, D_PN, 0), dtype=float)
    ok = bool(np.allclose(K_D, expected, atol=1e-9))
    print("\n  1. K = M_P^-1 . atom, validated where it is known independently")
    print(f"     K(2H)    = {np.round(K_D, 9)}")
    print(f"     sigma_0 + D_PN.1 = {np.round(expected, 9)}")
    print(f"\n  A1  K(2H) IS the single colour-weighted pn letter ........ "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("K_at_A2_is_the_single_pn_letter", ok,
                       f"max diff {float(np.max(np.abs(K_D - expected))):.2e}"))

    # ── A2. The exact interval where K leaves the positive sector ─────
    dpn, numer, sextic, q_c = dpn_sign_interval()
    print("\n  2. K(2H)'s only negative coefficient is gamma, and it IS D_PN")
    print(f"     D_PN(q) numerator factors: {numer}")
    print(f"     sextic {sextic}")
    print(f"     single real root above 1:  q_c = {q_c}")
    q0 = float(Q0)
    ok = (q_c is not None and float(q_c) > q0
          and abs(float(K_D[0]) - float(D_PN)) < 1e-12)
    print(f"     q_0 = {q0:.16f};  q_0/q_c = {q0 / float(q_c):.10f}")
    print(f"\n  A2  D_PN < 0 exactly on 1 < q < q_c, and q_0 is inside ... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => K(2H) lies OUTSIDE the positive sector precisely there.")
    print("      (An earlier draft said 'for all q > 1'. False — hence q_c.)")
    assertions.append(("K_leaves_positive_sector_exactly_on_1_to_qc", ok,
                       f"q_c = {q_c}; q_0/q_c = {q0 / float(q_c):.9f}"))

    # ── A3. K is not positive at any A ────────────────────────────────
    print("\n  3. K's negative content at q_0, all A:")
    print(f"     {'nucleus':8s} {'#neg':>5s} {'min coeff':>11s}  negative components")
    rows, all_neg = [], True
    for nm, Z, N in NUCLEI:
        K = binding_operator(Z, N)
        neg = [NF_NAMES[i] for i in range(6) if K[i] < -1e-9]
        all_neg = all_neg and bool(neg)
        rows.append({"nucleus": nm, "n_negative": len(neg),
                     "min_coeff": f"{float(K.min()):.9f}",
                     "negative_components": neg,
                     "K": [f"{v:.9f}" for v in K]})
        print(f"     {nm:8s} {len(neg):>5d} {K.min():>11.6f}  {neg}")
    print(f"\n  A3  K has negative coefficients at EVERY A ............... "
          f"{'PASS' if all_neg else 'FAIL'}")
    print("      The LP's feasible set is {x >= 0}. K is not in it — not")
    print("      'does not happen to be', CANNOT be.")
    assertions.append(("K_is_never_in_the_positive_sector", all_neg,
                       str([(r["nucleus"], r["n_negative"]) for r in rows])))

    # ── A4. x* is not even proportional to K ──────────────────────────
    P = build(1, 1, False)
    r = linprog(TM, A_ub=-GM, b_ub=-(GM @ P), bounds=[(0, None)] * 6,
                method="highs")
    x = r.x
    shared = [i for i in range(6) if abs(K_D[i]) > 1e-9 and x[i] > 1e-9]
    ratios = [float(x[i] / K_D[i]) for i in shared]
    ok = r.success and len(ratios) > 1 and len({round(v, 6) for v in ratios}) > 1
    print("\n  4. is x* a rescaling of K?  (A = 2, K exactly known)")
    print(f"     x* = {np.round(x, 6)}")
    print(f"     K  = {np.round(K_D, 6)}")
    print(f"     shared support {[NF_NAMES[i] for i in shared]}, "
          f"ratios x*/K = {[round(v, 6) for v in ratios]}")
    print(f"\n  A4  x* is NOT proportional to K ......................... "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("x_star_is_not_proportional_to_K", ok,
                       f"ratios {[round(v, 6) for v in ratios]}"))

    print("\n### VERDICT: NO, structurally. K is the free-to-bound map and on")
    print("    1 < q < q_c it necessarily carries negative (inverse-crossing /")
    print("    entanglement) content; x* is defined by excluding exactly that.")
    print("    They are COMPLEMENTARY, not competing: x* is the cheapest")
    print("    forward-time operator covering the free constituents, K is the")
    print("    actual map, and it lives partly in the reverse-time sector. The")
    print("    T/He3 separation x* produces stands as a structural fact about")
    print("    the Hecke data — it is simply not a fact about K.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("k-versus-selected-operator",
                                engine="sympy", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): asks, formally and with no physical "
                "input, whether the positive-sector LP's selected operator x* "
                "relates to the knot-convolution binding operator K. K is made "
                "exactly computable in the H_3-local model as K = M_P^-1 . atom "
                "(M_P = left multiplication by the nucleon product P, electrons "
                "excluded), and validates itself at A=2 by returning the single "
                "colour-weighted pn letter sigma_0 + D_PN.1. K(2H)'s ONLY "
                "negative NF coefficient is the gamma one and it IS D_PN, so "
                "positivity of K reduces to the sign of D_PN, which is settled "
                "in closed form: the numerator factors as "
                "(q-1)(q+1)(q^6-2q^5-5q^4-q^2+2q-1), the sextic has exactly one "
                "real root above 1 at q_c = 3.4580993000327971920, and D_PN < 0 "
                "precisely on 1 < q < q_c — which contains q_0 = 1.10998 by a "
                "factor of ~3.12. (An earlier draft claimed 'all q > 1'; false, "
                "corrected.) At A >= 3 K has 3-4 negative components at q_0. So "
                "the LP, whose feasible set is {x >= 0}, CANNOT return K; and "
                "x* is not even proportional to K on their shared support "
                "(ratios -9.640158 vs 0.290774 at A=2). STRUCTURAL READING: K "
                "and x* are complementary, not competing — K is the free-to-"
                "bound map and necessarily carries inverse-crossing "
                "(entanglement) content, x* is defined by excluding it. No fit; "
                "no B_AME; nothing wired.")
            wb.add_data("K_per_nucleus", rows)
            wb.add_data("dpn_numerator_factored", str(numer))
            wb.add_data("dpn_sextic", str(sextic))
            wb.add_data("q_c", str(q_c))
            wb.add_data("q0_over_qc", f"{q0 / float(q_c):.12f}")
            wb.add_data("A2_comparison", {
                "x_star": [f"{v:.9f}" for v in x],
                "K": [f"{v:.9f}" for v in K_D],
                "shared_support": [NF_NAMES[i] for i in shared],
                "ratios": [f"{v:.9f}" for v in ratios]})
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "CORRECTION carried in this witness: D_PN(q) is NOT negative "
                "for all q > 1. The sextic factor has a real root at "
                "q_c = 3.4580993000327971920 and D_PN > 0 beyond it. The exact "
                "statement is the interval 1 < q < q_c, which contains q_0 and "
                "the whole range swept in positive_sector_q_stability_probe.")
            wb.add_caveat(
                "INTERPRETATION, NOT DERIVED: the entire negative content of "
                "K(2H) is D_PN, the p-n interface offset, and the deuteron is "
                "the p-n bound system. Nothing here derives that "
                "correspondence and no physical quantity enters the "
                "computation. Recorded only so a later reader finds it labelled "
                "rather than rediscovering it as a lead.")
            wb.add_caveat(
                "K is computed in the H_3-LOCAL model of pyhecke.atom, where "
                "inter-nucleon crossings act on generator 0 of the same H_3. "
                "That is a different model from the (H_3)^(x)A tensor space the "
                "earlier probes' LP runs on; the A=2 comparison is made in the "
                "H_3-local model on both sides so it is like-for-like. "
                "Electrons are excluded throughout as the EM channel.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
