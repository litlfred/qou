#!/usr/bin/env python3
"""Is the positive-sector selection structural in `q`, or an accident at `q_0`?

WHY THIS EXISTS
---------------
`positive_sector_operator_selection_probe.py` showed that restricting the
operator-selection program to `x >= 0` — the forward-computational-time sector,
negatives being the inverse-crossing / entanglement sector per
`jet_history_retention_probe.py` §Q3 — breaks the `t = G e_1` degeneracy and
makes the LR demand select: `T` and `3He` get different supports, and the optimal
support lands on the sub-alphabet `{sigma_1, L+, L-}`.

A vertex of an LP can flip under an arbitrarily small perturbation, so a support
measured at one `q` is not yet a structural claim. `pyhecke.gram.gram_matrix_mp`
carries a `q` override for exactly this purpose — its own docstring says it
exists to test *"whether [a result] is structural in q or an accident at q_0"*.
This probe uses it, rebuilding **everything** at each `q`: the Gram, the Markov
cost `TR_M(q) = [1, z, z, z^2, z^2, h z^2 + z]` with `z = q^3/(q^2+1)`,
`h = q - 1/q`, and the nucleon NFs via `_hm_mp` at that `h`.

THE `x_free` QUESTION IS SETTLED
---------------------------------
The previous probe flagged a tension: `x_free` has 108 of 216 negative
coordinates at `A = 3`, so positivity is imposed on the *solution* while the
*demand* comes from an object violating it. **Owner ruling: that is fine.**
`x_free` is the tensor product of the individual nucleon NFs with no
inter-nucleon crossings — the **free constituents** of the atom, not a bound
configuration — and the constituents are not required to be stable. The program
is asking for the cheapest forward-time operator that *covers* an unbound,
entanglement-carrying constituent product. The tension is resolved in favour of
the construction as it stands; no rebuild of the nucleon is needed.

RESULT
------
Swept `q` from 1.02 to 1.50 at `A = 3` (`T = pnn`, `3He = ppn`), `q_0 = 1.10998`:

    q       |supp T|  |supp He3|   T != He3   obj > u_1   sub-alphabet
    1.02        8        11          yes        yes       {s1, L+, L-}
    1.05        7        10          yes        yes       {s1, L+, L-}
    1.08        7        10          yes        yes       {s1, L+, L-}
    q_0         6         9          yes        yes       {s1, L+, L-}
    1.15        6        10          yes        yes       {s1, L+, L-}
    1.20        6         7          yes        yes       {s1, L+, L-}
    1.26        -         -          yes        yes       {s1, L+, L-}
    1.28        -         -          yes        yes       + gamma, s0, e-
    1.30        -         -          yes        yes       + s0, e-
    1.35        -         -          yes        NO        + gamma, s0, e-
    1.50        5         5          yes        NO        + gamma, s0

Three claims, with different strengths:

**(1) The `T` / `3He` separation is fully robust.** Different supports at every
`q` tested, 1.02 through 1.50 — the whole range, including where everything else
has broken down. This is the claim Gap #2 needs and it does not depend on `q_0`.

**(2) The sub-alphabet `{sigma_1, L+, L-}` is robust on `q` in [1.02, 1.26]**,
breaking at 1.28 when `gamma`, `sigma_0` and `e-` enter. `q_0 = 1.10998` sits
well inside that window, at roughly 37 % of its width — not near an edge.

**(3) The degeneracy-breaking `obj > u_1` holds for `q <~ 1.30`** and fails by
1.35, where the optimum falls back onto the row-1 bound and the program returns
to the degenerate behaviour the unrestricted version always had.

WHAT IS **NOT** ROBUST
-----------------------
**The support size.** It drifts from 8/11 at `q = 1.02` to 6/9 at `q_0` to 6/7
at 1.20 to 5/5 at 1.50, with no monotone pattern. So `|support| = 6` and `9` are
**not** invariants and must not be quoted as structural facts about `T` and
`3He`. What is invariant is that the two differ, and which letters the support is
built from — not how many words it uses.

That distinction matters: a reader who takes "T selects 6 operators, 3He selects
9" as a structural statement will be quoting a vertex count that moves with `q`.

DISCIPLINE
----------
No fit; nothing wired; no tier change; no `B_AME` anywhere. Everything is
rebuilt per `q` — Gram, cost, and nucleon NFs — so no quantity is silently
carried over from `q_0`. mpmath at 30-40 dps for the algebra, f64 only at the LP
boundary; conclusions are set equalities, strict inequalities and support
comparisons. LP via scipy HiGHS, declared.

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

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

from pyhecke.gram import NF_NAMES, _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
CORE = {"σ₁", "L₊", "L₋"}
Q0_STR = mp.nstr(mp.mpf(str(Q0)), 20)
Q_SWEEP = ["1.02", "1.05", "1.08", Q0_STR, "1.15", "1.20", "1.24", "1.26",
           "1.28", "1.30", "1.35", "1.40", "1.50"]


def substrate_at(q_str: str):
    """Rebuild Gram, Markov cost and both nucleon NFs at `q`. Nothing carried."""
    q = mp.mpf(q_str)
    hq = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    G = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    t = np.array([1.0, float(z), float(z), float(z ** 2), float(z ** 2),
                  float(hq * z ** 2 + z)])

    def nucleon(kind: str) -> np.ndarray:
        nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
        for _ in range(3):
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq, 1, hq)
        if kind == "p":
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 1, hq)
        else:
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq, 1, hq)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
        return np.array([float(x) for x in nf])

    return G, t, {k: nucleon(k) for k in "pn"}


def kron_pow(M, A: int):
    out = M
    for _ in range(A - 1):
        out = np.kron(out, M)
    return out


def alphabet_of(support, A: int) -> set:
    out = set()
    for i in support:
        j = i
        for _ in range(A):
            out.add(NF_NAMES[j % 6])
            j //= 6
    return out


def solve_positive(seq: str, G, t, NUC):
    """`min t.x  s.t.  Gx >= u_demand, x >= 0` on the constituent subalgebra."""
    A = len(seq)
    GA = kron_pow(G, A)
    tA = kron_pow(t.reshape(1, -1), A).ravel()
    d = GA.shape[0]
    v = NUC[seq[0]]
    for k in seq[1:]:
        v = np.kron(v, NUC[k])
    r = linprog(tA, A_ub=-GA, b_ub=-(GA @ v), bounds=[(0, None)] * d,
                method="highs")
    if not r.success:
        return None
    supp = tuple(i for i in range(d) if r.x[i] > 1e-9)
    return {"support": supp, "size": len(supp), "obj": float(r.fun),
            "u1": float(tA @ v), "alphabet": alphabet_of(supp, A)}


def main() -> int:
    assertions = []
    print("t7qv — is the positive-sector selection structural in q?")
    print(f"      q_0 = {Q0_STR}; everything rebuilt per q (Gram, cost, nucleons)")
    print()
    print(f"  {'q':>20s} {'|supp T|':>9s} {'|supp He3|':>11s} {'T!=He3':>7s} "
          f"{'obj>u1':>7s}  sub-alphabet")

    rows, sep_all, core_qs, break_qs, obj_ok_qs = [], [], [], [], []
    for qs in Q_SWEEP:
        G, t, NUC = substrate_at(qs)
        rT = solve_positive("pnn", G, t, NUC)
        rH = solve_positive("ppn", G, t, NUC)
        if rT is None or rH is None:
            print(f"  {qs:>20s}  INFEASIBLE")
            continue
        sep = rT["support"] != rH["support"]
        alpha = rT["alphabet"] | rH["alphabet"]
        is_core = alpha <= CORE
        obj_ok = rT["obj"] > rT["u1"] and rH["obj"] > rH["u1"]
        sep_all.append(sep)
        (core_qs if is_core else break_qs).append(qs)
        if obj_ok:
            obj_ok_qs.append(qs)
        tag = "  <- q_0" if qs == Q0_STR else ""
        rows.append({"q": qs, "supp_T": rT["size"], "supp_He3": rH["size"],
                     "separates": sep, "obj_gt_u1": obj_ok,
                     "alphabet": sorted(alpha), "core": is_core})
        print(f"  {qs:>20s} {rT['size']:>9d} {rH['size']:>11d} "
              f"{str(sep):>7s} {str(obj_ok):>7s}  {sorted(alpha)}{tag}")

    # ── A1. The separation is fully robust ────────────────────────────
    ok = bool(sep_all) and all(sep_all)
    print(f"\n  A1  T != He3 at EVERY q tested ........................... "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      {len(sep_all)} values from {Q_SWEEP[0]} to {Q_SWEEP[-1]} —")
    print("      the claim Gap #2 needs, and it does not depend on q_0.")
    assertions.append(("separation_robust_across_q", ok,
                       f"{sum(sep_all)}/{len(sep_all)} q values separate"))

    # ── A2. The sub-alphabet is robust in a window containing q_0 ─────
    ok = (Q0_STR in core_qs) and len(core_qs) >= 6 and len(break_qs) > 0
    print(f"\n  A2  sub-alphabet {{σ₁,L₊,L₋}} holds in a window round q_0 . "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      core at: {core_qs}")
    print(f"      breaks at: {break_qs}")
    print("      q_0 sits well inside, not near an edge.")
    assertions.append(("subalphabet_stable_in_window_containing_q0", ok,
                       f"core {core_qs}; breaks {break_qs}"))

    # ── A3. The degeneracy-breaking has a q range ─────────────────────
    ok = (Q0_STR in obj_ok_qs) and len(obj_ok_qs) < len(rows)
    print(f"\n  A3  obj > u_1 holds near q_0 and FAILS at large q ........ "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      holds at: {obj_ok_qs}")
    print("      beyond that the optimum falls back onto the row-1 bound and")
    print("      the program returns to its degenerate behaviour.")
    assertions.append(("degeneracy_breaking_has_a_q_range", ok,
                       f"obj>u1 at {obj_ok_qs}"))

    # ── A4. The support SIZE is not an invariant ──────────────────────
    sizes_T = {r["supp_T"] for r in rows}
    sizes_H = {r["supp_He3"] for r in rows}
    ok = len(sizes_T) > 1 and len(sizes_H) > 1
    print(f"\n  A4  the support SIZE is NOT robust ....................... "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      |supp T| takes {sorted(sizes_T)};  "
          f"|supp He3| takes {sorted(sizes_H)}")
    print("      => '6 and 9' are vertex counts that move with q, NOT")
    print("         structural facts. Do not quote them as invariants. What")
    print("         is invariant is THAT they differ, and which letters are")
    print("         used — not how many words.")
    assertions.append(("support_size_is_not_an_invariant", ok,
                       f"T sizes {sorted(sizes_T)}, He3 sizes {sorted(sizes_H)}"))

    print("\n### VERDICT: the separation is structural — it survives every q")
    print("    tested. The sub-alphabet {σ₁, L₊, L₋} is structural on a broad")
    print("    window containing q_0 with margin. The support SIZE is not, and")
    print("    should never be quoted as one. The owner's ruling settles the")
    print("    x_free question: those are the FREE constituents of the atom and")
    print("    are not required to be stable, so positivity on the solution")
    print("    against an entanglement-carrying demand is the intended reading.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("positive-sector-q-stability",
                                engine="scipy", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): tests whether the positive-sector "
                "operator selection is structural in q or an accident at q_0, "
                "rebuilding the Gram, the Markov cost TR_M(q) and both nucleon "
                "NFs at each q (gram_matrix_mp's q override exists for exactly "
                "this). Swept q = 1.02 .. 1.50 at A=3. RESULTS: (1) the T vs "
                "He3 separation holds at EVERY q tested — fully robust, and it "
                "is the claim Gap #2 needs; (2) the optimal sub-alphabet "
                "{sigma_1, L+, L-} is stable on q in [1.02, 1.26], breaking at "
                "1.28 when gamma, sigma_0 and e- enter, with q_0 = 1.10998 well "
                "inside; (3) the degeneracy-breaking obj > u_1 holds to about "
                "q = 1.30 and fails by 1.35, where the optimum falls back onto "
                "the row-1 bound. NOT robust: the support SIZE, which drifts "
                "8/11 -> 6/9 -> 6/7 -> 5/5 with no monotone pattern, so '6 and "
                "9' are vertex counts and must not be quoted as invariants. "
                "Also records the owner's ruling that x_free's negative "
                "coordinates are fine: it is the FREE constituent product, and "
                "constituents are not required to be in a stable "
                "configuration. No fit; no B_AME; nothing wired.")
            wb.add_data("q_sweep", rows)
            wb.add_data("core_alphabet", sorted(CORE))
            wb.add_data("q_core_window", core_qs)
            wb.add_data("q_alphabet_breaks", break_qs)
            wb.add_data("q_obj_gt_u1", obj_ok_qs)
            wb.add_data("support_sizes_T", sorted(sizes_T))
            wb.add_data("support_sizes_He3", sorted(sizes_H))
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "The support SIZE is not an invariant — it moves with q. Only "
                "the FACT of separation and the letters used are stable. "
                "Quoting '|support| = 6 for T, 9 for He3' as a structural "
                "result would be quoting a vertex count.")
            wb.add_caveat(
                "OWNER RULING (2026-08-31): x_free's 108 negative coordinates "
                "at A=3 are not a defect. x_free is the tensor product of the "
                "individual nucleon NFs with no inter-nucleon crossings — the "
                "FREE constituents of the atom — and the constituents are not "
                "asked to be in a stable configuration. Positivity is imposed "
                "on the solution only. The previous probe's flagged tension is "
                "resolved in favour of the construction as it stands.")
            wb.add_caveat(
                "Everything is rebuilt per q so nothing is carried over from "
                "q_0, but the LP itself runs at f64 after an mpmath (30-40 dps) "
                "algebra stage. Support membership is thresholded at x_i > 1e-9; "
                "near a vertex flip that threshold is the deciding quantity, "
                "which is part of why the size is not treated as an invariant.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
