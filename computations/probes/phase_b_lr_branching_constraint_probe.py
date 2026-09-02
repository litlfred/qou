#!/usr/bin/env python3
"""Phase B: the LR branching constraint, built at `A = 3`. The next blocker is the diagonal Gram.

WHAT THIS BUILDS
----------------
`operator_selection_active_set_probe.py` localised the blocker on `K`-via-knot-
convolution: the per-nucleus LP at `H_{3A}` runs, but `T` and `3He` come out with
**identical** active blocks because the constraint that would make the program
depend on `(Z, N)` is not implemented. The witnesses say so themselves:

> *"Full real SDP needs Phase B color-flavor constraints (LR branching
> `H_{3A} ⊃ (H_3)^Z × (H_3)^N`); this is the bar-fold symmetry-reduced bounded
> baseline."*

This builds that constraint, `A`-generically, and instantiates it at `A = 3`.
The constraint itself is correct and validated. **Wiring it into the LP as it
currently stands does no work**, and the reason is specific and fixable.

THE CONSTRUCTION
----------------
Restriction along `H_{3A} ⊃ (H_3)^{⊗A}` decomposes each block, so for an element
of the constituent subalgebra

    chi^lambda(x) = SUM_{mu_1..mu_A} c^lambda_{mu_1..mu_A} PROD_i chi^{mu_i}(x_i)

Each nucleon is an `H_3` object with a three-block character
`(chi^{(3)}, chi^{(2,1)}, chi^{(1^3)})`, and the composite is the **iterated LR
convolution** — one `get_lr_table(3(m-1), 3)` per rung:

    P^(1) = p_{k_1}
    P^(m)_lambda = SUM_{nu |- 3(m-1)} SUM_{mu |- 3} c^lambda_{nu,mu} P^(m-1)_nu p_{k_m}^mu

That profile is the LP's **demand** `u_demand = y_lambda * chi^lambda_free`,
against the existing cost `t_lambda = y_lambda * chi^lambda_atom`. Cost carries
the bound atom, demand the free constituent product, so the program would price
exactly the gap — the binding operator, block by block. That is the knot
convolution `T_w(atom) = K . (x)_i T_w(nucleon_i)` read blockwise.

Validated two independent ways, exact at `A = 2, 3, 4`, all 11 / 30 / 77 blocks:
the **induction** identity (`SUM_lambda c dim S^lambda` against the multinomial)
and the **restriction** identity (`dim S^lambda = SUM_mu c PROD dim S^{mu}`),
the latter validating the character formula and not merely the coefficients.

TWO DEFECTS FOUND ON THE WAY
-----------------------------
**(1) `pyhecke.atom.nf_channel_exact` raised `NameError` on every call.** It uses
`_TR_M_FRAC`, `pyhecke.gram` defines it and lists it in `__all__`, and only
`atom.py`'s import line was short. Fixed here.

**(2) With that fixed, the function was still wrong — REPAIRED 2026-08-31.**
Its `chi_std` matched the standard-block character under *no* normalisation.
Measured against direct seminormal traces at `H_3`, as it stood then:

    element        nf_channel_exact   direct trace   trace/dim
    identity            1.000000        2.000000      1.000000
    sigma_0             0.864044        0.209060      0.104530
    sigma_0 sigma_1     0.055685       -1.000000     -0.500000

Defect (1) is why (2) survived: the function was dead code, so nobody ever
compared it to anything. It has since been repaired (option B of
`nf_channel_exact_repair_options_probe.py`) by giving `chi_std` its own
character vector `_STD_CHI_FRAC = [2, h, h, -1, -1, 0]`, so all three channels
are now read directly and none is derived by inversion. A3 below re-measures
the repair rather than the defect.

**The nucleon profiles here are still built from direct seminormal traces at
`q_0`**, deliberately: the exact-Fraction path pins `q = 111/100`, not `q_0`,
which is a separate open design question. So the numbers below are unchanged by
the repair.

    proton    chi^(3) = +1.382494463   chi^(2,1) = -0.280593351   chi^(1^3) = -0.739223571
    neutron   chi^(3) = +1.122106822   chi^(2,1) = -0.371956325   chi^(1^3) = -0.910762215

Note `chi^(2,1)` is **negative** for both, where `nf_channel_exact` reports
`+0.78` / `+0.66`. Anything downstream of that function needs re-checking.

RESULT AT `A = 3` — AND A CORRECTION TO MY OWN FIRST READING
--------------------------------------------------------------
The demand is genuinely `(Z, N)`-dependent, which is what Phase B was for:

    u_demand   T   [0.0030468 0.0363869 0.0312835 0.0328458 0.0385089]
              3He  [0.0054034 0.0469340 0.0433424 0.0450538 0.0474450]
    n_target   T   2.2035878        3He 2.7805848

**But the LP's duals do not see it.** `nucleus_sdp_assembly` builds a *diagonal*
Gram, `G = diag(y_lambda * dim S^lambda)`, and the dual constraint of
`solve_frobenius_dual_lp` is `y_0 * 1 + G^T y = t`, which does not mention
`u_demand` at all. With `G` diagonal and `y_0* = 0` this forces

    y*_lambda  =  t_lambda / G_lambda,lambda  =  chi^lambda_atom / dim S^lambda

exactly — measured, and **invariant under scaling `u_demand` by `7.3x`**. So:

- the primal `x = G^{-1} u` is *determined* outright, not optimised;
- the duals are the normalised atom characters, and would differ between `T` and
  `3He` with or without Phase B;
- `n_target` is the only other thing the demand changes.

I first read the differing `y*` as Phase B separating the isotopes. That was
wrong and is withdrawn: those prices are a property of the cost vector, which was
already `(Z, N)`-dependent through `chi^lambda_atom`. **Phase B, dropped into
this LP, adds a determined primal and a derived `n_target`, and nothing else.**

WHERE THE REAL BLOCKER NOW SITS
--------------------------------
**The Gram is diagonal by construction**, keeping only `G_lambda,lambda =
tr_M(P_lambda)` and discarding every off-diagonal Frobenius pairing. Against a
diagonal Gram no demand vector can do work: the equality `Gx = u` has a unique
solution and leaves no feasible set to optimise over, and the dual is pinned by
`t` alone. So the branching constraint cannot bite until the `H_{3A}` Frobenius
Gram is built with its off-diagonal entries. That is the next object to build,
and it is a well-posed one — the `H_3` Gram already exists in full (`pyhecke.gram`,
6x6, with its documented radical); what is missing is the `H_{3A}` analogue.

GENERAL PRINCIPLE FOR `A > 3`
------------------------------
1. **One new table per rung.** Only `get_lr_table(3(A-1), 3)` is new; everything
   below is reused. Measured:

       A=2  n= 6   11 blocks     35 LR entries   0.00 s
       A=3  n= 9   30 blocks    203 entries      0.00 s
       A=4  n=12   77 blocks    806 entries      0.00 s
       A=5  n=15  176 blocks   2659 entries      0.15 s
       A=6  n=18  385 blocks   7646 entries      0.51 s

   Tractable well past where the corpus has cost data; the bottleneck will be
   `chi^lambda` for the atom, not the branching.

2. **The demand depends on `(Z, N)` alone, not on nucleon ordering.** Verified to
   `8.5e-14` over every permutation of `ppn`, `ppnn`, `pppn` — as it must be,
   since Schur multiplication is commutative. A real contrast with
   `build_atom_nf`, which fixes an interleaved ordering: the demand side is
   ordering-free even though the cost side is not, so any surviving
   ordering-dependence is a property of the atom word, not of the branching.

3. **`A` enters only as recursion depth.** Nothing is special to `A = 3`.

**Caveat that will bite at `A >= 4`:** convention D's two-row cap zeroes
`y_lambda` outside two-row `lambda`, so the positive-norm subspace is 5 blocks of
30 at `A = 3`. The demand is computed over all blocks and then projected onto
that subspace, discarding most of the branching information before the LP sees
it. Whether the cap is the right truncation is not settled here, but it is the
next place `(Z, N)` signal is lost after the diagonal Gram.

DISCIPLINE
----------
No fit; no production wiring; no tier change. LR coefficients from the canonical
`substrate/lr_coefficients.py`. LP backend **scipy**, pinned and declared: the
clarabel Rust binary is not built in this container, and `lp_dual_solver`'s own
notes say the scipy vertex method is the more reliable for active sets (clarabel's
IPM returned 28 false actives on the `H_9` LP, bean `qou-q7f1`). The recorded
clarabel active sets reproduce here under scipy.

-- Ref: [manuscript] bean t7qv; nucleus_real_sdp.py; prop:operator-selection-lp
"""
from __future__ import annotations

import itertools
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "hecke"))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from hecke_core import h  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from murnaghan_nakayama import dim_specht  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from nucleus_sdp_assembly import cost_gram_from_arrays  # noqa: E402
from pyhecke.lp_dual_solver import (  # noqa: E402
    solve_frobenius_dual_lp,
    solve_operator_selection_lp,
)

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

BACKEND = "scipy"          # pinned, not auto — see DISCIPLINE.
P3 = [(3,), (2, 1), (1, 1, 1)]
_SIG = {lam: [np.asarray(m, dtype=float)
              for m in build_seminormal_matrices(list(lam))[0]] for lam in P3}


def nucleon_letters(kind: str) -> list:
    """`build_atom_nf`'s per-nucleon block, as `(c, d, gen)` Hecke letters."""
    L = []
    for _ in range(3):
        L += [(1.0, 0.0, 0), (1.0, -h, 1)]
    L += ([(1.0, 0.0, 0), (1.0, -h / 2, 0), (1.0, -h / 2, 1)] if kind == "p"
          else [(1.0, -h / 2, 0), (1.0, -h / 2, 0), (1.0, -h, 1)])
    return L + [(1.0, 0.0, 0), (1.0, 0.0, 0)]


def nucleon_profiles() -> dict:
    """Genuine (unnormalised) `H_3` block characters, by direct seminormal trace.

    Deliberately NOT `pyhecke.atom.nf_channel_exact` — see the header: its
    `chi_std` is wrong under every normalisation and its 1-dim blocks sit at
    `q = 111/100`.
    """
    out = {}
    for k in ("p", "n"):
        letters = nucleon_letters(k)
        prof = {}
        for lam in P3:
            sig = _SIG[lam]
            d = sig[0].shape[0]
            M = np.eye(d)
            for (c, dd, g) in letters:
                M = M @ (c * sig[g] + dd * np.eye(d))
            prof[lam] = float(np.trace(M))
        out[k] = prof
    return out


def lr_convolve(profiles: list[dict]) -> dict:
    """A-generic iterated LR branching; `A` is only the recursion depth."""
    cur = dict(profiles[0])
    m = 1
    for p in profiles[1:]:
        m += 1
        nxt = {lam: 0.0 for lam in partitions_of(3 * m)}
        for (nu, mu, lam), c in get_lr_table(3 * (m - 1), 3).items():
            if nu in cur and mu in p:
                nxt[lam] += c * cur[nu] * p[mu]
        cur = nxt
    return cur


def demand_of(seq: str, prof: dict) -> dict:
    return lr_convolve([prof[k] for k in seq])


def check_induction_identity() -> int:
    import math
    import random
    bad = 0
    for A in (2, 3, 4):
        for trial in range(3):
            random.seed(A * 10 + trial)
            mus = [random.choice(P3) for _ in range(A)]
            conv = lr_convolve([{m: (1.0 if m == mu else 0.0) for m in P3}
                                for mu in mus])
            lhs = sum(c * dim_specht(list(lam)) for lam, c in conv.items())
            rhs = math.factorial(3 * A) // (6 ** A)
            for mu in mus:
                rhs *= dim_specht(list(mu))
            if abs(lhs - rhs) > 1e-6 * max(1, abs(rhs)):
                bad += 1
    return bad


def check_restriction_identity() -> int:
    unit = {mu: float(dim_specht(list(mu))) for mu in P3}
    bad = 0
    for A in (2, 3, 4):
        got = lr_convolve([unit] * A)
        for lam in partitions_of(3 * A):
            d = dim_specht(list(lam))
            if abs(got[lam] - d) > 1e-6 * max(1, d):
                bad += 1
    return bad


def nf_channel_exact_defect() -> list:
    """Measure `nf_channel_exact` against direct seminormal traces.

    Since the 2026-08-31 repair this measures AGREEMENT; it used to measure the
    defect. Kept as the regression guard for that repair.
    """
    from fractions import Fraction

    from pyhecke.atom import nf_channel_exact
    from pyhecke.gram import _Q_FRAC, hm_exact
    # Compare LIKE FOR LIKE: the exact-Fraction path pins q = _Q_FRAC = 111/100,
    # so the reference seminormal matrices must be built at that q too. Using
    # the q_0 matrices instead makes a 5th-decimal pin difference look like a
    # defect.
    sig_q = [np.asarray(m, dtype=float)
             for m in build_seminormal_matrices([2, 1], q=float(_Q_FRAC))[0]]
    rows = []
    for name, word in (("identity", []), ("sigma_0", [0]),
                       ("sigma_0 sigma_1", [0, 1])):
        nf = [Fraction(1), 0, 0, 0, 0, 0]
        for g in word:
            nf = hm_exact(nf, Fraction(1), Fraction(0), g)
        cs, cst, ca, _tr = nf_channel_exact(nf)
        M = np.eye(2)
        for g in word:
            M = M @ sig_q[g]
        direct = float(np.trace(M))
        rows.append({"element": name, "nf_channel_chi_std": f"{float(cst):.6f}",
                     "direct_trace": f"{direct:.6f}",
                     "trace_over_dim": f"{direct / 2:.6f}",
                     "matches_either": bool(
                         abs(float(cst) - direct) < 1e-6
                         or abs(float(cst) - direct / 2) < 1e-6)})
    return rows


def solve_pair(atom: str, seq: str, prof: dict) -> dict:
    parts, y, chi, dims, meta = load_cost(atom)
    keys = [str(tuple(p)) for p in parts]
    cg = cost_gram_from_arrays(keys, parts, dims, y, chi)
    t, frob = cg.t, cg.frob_diag
    pos = [i for i, g in enumerate(frob) if g > 0.0]
    pk = [keys[i] for i in pos]
    t_pos, G_pos = t[pos], np.diag(frob[pos])

    free = demand_of(seq, prof)
    u = np.array([y[i] * free.get(parts[i], 0.0) for i in pos])

    cur = solve_operator_selection_lp(t_pos, G_pos, float(t_pos.sum()),
                                      backend=BACKEND).to_dict()
    n_target = float(sum(u[j] / G_pos[j, j] for j in range(len(pos))))
    pb = solve_frobenius_dual_lp(t_pos, G_pos, n_target, u).to_dict()

    # Does the dual move if the demand is scaled? (It must not: G is diagonal.)
    pb2 = solve_frobenius_dual_lp(t_pos, G_pos, 7.3 * n_target,
                                  7.3 * u).to_dict()
    y1 = np.array(pb.get("y_star") or [], dtype=float)
    y2 = np.array(pb2.get("y_star") or [], dtype=float)
    predicted = np.array([t_pos[j] / G_pos[j, j] for j in range(len(pos))])
    chi_over_dim = np.array([chi[i] / dim_specht(parts[i]) for i in pos])

    return {"atom": atom, "seq": seq, "Z": meta["Z"], "N": meta["N"],
            "blocks": pk,
            "u_demand": [f"{v:.9f}" for v in u],
            "n_target_derived": f"{n_target:.9f}",
            "current_active": [pk[i] for i in cur.get("active_set", [])
                               if i < len(pk)],
            "phaseB_active": [pk[i] for i in pb.get("active_set", [])
                              if i < len(pk)],
            "phaseB_y_star": [f"{v:.9f}" for v in y1],
            "y_star_equals_t_over_G": bool(
                len(y1) and np.allclose(y1, predicted, atol=1e-7)),
            "y_star_equals_chi_over_dim": bool(
                len(y1) and np.allclose(y1, chi_over_dim, atol=1e-7)),
            "dual_invariant_under_demand_scaling": bool(
                len(y1) == len(y2) and len(y1) and np.allclose(y1, y2, atol=1e-9)),
            "_u": u, "_y": y1}


def main() -> int:
    assertions = []
    print("t7qv — Phase B: the LR branching constraint at A = 3")

    # ── A1. The convolution is right, two independent ways ────────────
    bad_i, bad_r = check_induction_identity(), check_restriction_identity()
    ok = (bad_i == 0 and bad_r == 0)
    print("\n  1. validating the A-generic LR convolution  [A = 2,3,4]")
    print(f"     induction identity   : {bad_i} mismatches")
    print(f"     restriction identity : {bad_r} mismatches  "
          f"(validates the CHARACTER formula, not just the coefficients)")
    print(f"\n  A1  both identities exact ................................ "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("lr_convolution_validated_two_ways", ok,
                       f"induction {bad_i}, restriction {bad_r}"))

    # ── A2. nf_channel_exact is defective, so it is not used ──────────
    defect = nf_channel_exact_defect()
    print("\n  2. pyhecke.atom.nf_channel_exact — measured against direct traces")
    print(f"     {'element':18s} {'chi_std':>10s} {'direct':>10s} "
          f"{'direct/dim':>11s}  matches?")
    for r in defect:
        print(f"     {r['element']:18s} {r['nf_channel_chi_std']:>10s} "
              f"{r['direct_trace']:>10s} {r['trace_over_dim']:>11s}  "
              f"{r['matches_either']}")
    ok = all(r["matches_either"] for r in defect)
    print(f"\n  A2  chi_std now AGREES with the direct trace (repaired) .. "
          f"{'PASS' if ok else 'FAIL'}")
    print("      Repaired 2026-08-31 via _STD_CHI_FRAC = [2,h,h,-1,-1,0]; this")
    print("      assertion used to record the defect and now guards the fix.")
    print("      Profiles below still use DIRECT traces, because the exact")
    print("      path pins q = 111/100 rather than q_0 — a separate question.")
    assertions.append(("nf_channel_exact_chi_std_agrees_after_repair", ok,
                       str(defect)))

    # ── A3. Nucleon profiles differ ───────────────────────────────────
    prof = nucleon_profiles()
    print("\n  3. nucleon H_3 characters (direct seminormal traces at q_0):")
    for k, nm in (("p", "proton"), ("n", "neutron")):
        print(f"     {nm:8s} " + "  ".join(
            f"chi^{m}={prof[k][m]:+.9f}" for m in P3))
    diff = max(abs(prof["p"][m] - prof["n"][m]) for m in P3)
    ok = diff > 1e-9
    print(f"\n  A3  proton and neutron differ (max {diff:.6f}) ......... "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("nucleon_profiles_are_distinct", ok,
                       f"max channel difference {diff:.9f}"))

    # ── A4/A5/A6. A = 3 ───────────────────────────────────────────────
    print("\n  4. A = 3 — current LP vs Phase B")
    res = {a: solve_pair(a, s, prof)
           for a, s in (("tritium", "pnn"), ("he3", "ppn"))}
    for r in res.values():
        print(f"     {r['atom']:8s} (Z,N)=({r['Z']},{r['N']})  blocks {r['blocks']}")
        print(f"        u_demand (LR) = [{' '.join(r['u_demand'])}]")
        print(f"        n_target      = {r['n_target_derived']}")
        print(f"        current active= {r['current_active']}")
        print(f"        PhaseB  y*    = [{' '.join(r['phaseB_y_star'])}]")

    T, H = res["tritium"], res["he3"]
    ok = T["current_active"] == H["current_active"]
    print(f"\n  A4  the CURRENT LP cannot separate T from He3 ............ "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("current_lp_cannot_separate_T_from_He3", ok,
                       f"both {T['current_active']}"))

    u_diff = float(np.max(np.abs(T["_u"] - H["_u"])))
    ok = u_diff > 1e-9
    print(f"\n  A5  the LR demand IS (Z,N)-dependent (max diff {u_diff:.6f}) "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("lr_demand_is_ZN_dependent", ok,
                       f"u_demand max difference {u_diff:.9f}"))

    ok = all(r["y_star_equals_t_over_G"] and r["y_star_equals_chi_over_dim"]
             and r["dual_invariant_under_demand_scaling"] for r in res.values())
    print(f"\n  A6  ...but the DUALS DO NOT SEE IT ....................... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      y* = t/G = chi^lam_atom / dim S^lam exactly, and is")
    print("      INVARIANT under scaling u_demand by 7.3x. The Gram is")
    print("      DIAGONAL, so the dual constraint y0.1 + G^T y = t pins y")
    print("      from the cost alone and never mentions the demand.")
    print("      => I first read the differing y* as Phase B separating the")
    print("         isotopes. Withdrawn: those prices are a property of the")
    print("         cost vector, already (Z,N)-dependent through chi_atom.")
    print("         Phase B here adds a determined primal x = G^-1 u and a")
    print("         derived n_target, and nothing else.")
    assertions.append(("duals_are_blind_to_the_demand_under_a_diagonal_gram",
                       ok, "y* = t/G = chi/dim; invariant under 7.3x scaling"))

    # ── A7. General principle for A > 3 ───────────────────────────────
    print("\n  5. general principle for A > 3")
    worst = 0.0
    for base in ("ppn", "ppnn", "pppn"):
        ref = demand_of(base, prof)
        for perm in set(itertools.permutations(base)):
            g = demand_of("".join(perm), prof)
            worst = max(worst, max(abs(g[l] - ref[l]) for l in ref))
    print(f"     (a) demand depends on (Z,N) ALONE — max deviation over all")
    print(f"         permutations of ppn/ppnn/pppn: {worst:.3e}")
    print("     (b) one new table per rung, get_lr_table(3(A-1), 3):")
    scaling = []
    for A in range(2, 7):
        t0 = time.time()
        tbl = get_lr_table(3 * (A - 1), 3)
        dt = time.time() - t0
        scaling.append({"A": A, "n": 3 * A,
                        "blocks": len(partitions_of(3 * A)),
                        "lr_entries": len(tbl), "build_s": f"{dt:.3f}"})
        print(f"         A={A}  n={3 * A:2d}  blocks={len(partitions_of(3 * A)):4d}"
              f"  entries={len(tbl):5d}  {dt:6.2f}s")
    ok = worst < 1e-9
    print(f"\n  A7  the LR demand is ordering-independent ................ "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("lr_demand_is_ordering_independent", ok,
                       f"max deviation {worst:.3e}"))

    print("\n     ⚠ caveat for A >= 4: convention D's two-row cap zeroes")
    print("       y_lambda outside two-row lambda (5 blocks of 30 at A=3), and")
    print("       the demand is projected onto that subspace, discarding most")
    print("       of the branching. Second place (Z,N) signal is lost, after")
    print("       the diagonal Gram.")

    print("\n### VERDICT: the branching constraint is built, A-generic and")
    print("    validated, and its demand is genuinely (Z,N)-dependent. But it")
    print("    cannot bite against a DIAGONAL Gram: Gx = u has a unique")
    print("    solution, leaving nothing to optimise, and the dual is pinned by")
    print("    the cost alone. The next object to build is the H_{3A} Frobenius")
    print("    Gram WITH its off-diagonal entries — the H_3 one already exists")
    print("    in full in pyhecke.gram. Not wired into production.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("phase-b-lr-branching-constraint",
                                engine="python", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): builds the Phase B color-flavor "
                "constraint (LR branching H_{3A} > (H_3)^Z x (H_3)^N) "
                "A-generically and instantiates it at A=3. Each nucleon's H_3 "
                "block character is LR-convolved (one get_lr_table(3(m-1),3) "
                "per rung) into an H_{3A} profile serving as the LP demand "
                "u_demand = y_lambda * chi^lambda_free against the cost "
                "t_lambda = y_lambda * chi^lambda_atom. Validated two "
                "independent ways (induction and restriction identities, exact "
                "at A=2,3,4, all blocks). RESULT: the demand IS (Z,N)-"
                "dependent, but the LP's duals are blind to it — with the "
                "DIAGONAL Gram that nucleus_sdp_assembly builds, y* = t/G = "
                "chi^lambda_atom/dim S^lambda exactly and is invariant under "
                "scaling u_demand by 7.3x, so Phase B adds only a determined "
                "primal and a derived n_target. Corrects my own first reading, "
                "which took the differing y* for Phase B separation; those "
                "prices come from the cost vector and predate it. Next blocker "
                "is therefore the diagonal Gram. Also finds TWO defects in "
                "pyhecke.atom.nf_channel_exact: a NameError on every call "
                "(fixed) and, beneath it, a chi_std matching no normalisation "
                "plus 1-dim blocks at q=111/100. Both are now REPAIRED (option "
                "B: chi_std gets its own character vector), and A2 guards the "
                "repair rather than recording the defect; the profiles here "
                "still use direct seminormal traces because the exact path "
                "pins q=111/100 rather than q_0. No fit; not wired into production.")
            wb.add_data("nucleon_profiles_direct_traces",
                        {k: {str(m): f"{v:.9f}" for m, v in p.items()}
                         for k, p in prof.items()})
            wb.add_data("nf_channel_exact_defect", defect)
            wb.add_data("A3_solves", [{k: v for k, v in r.items()
                                       if not k.startswith("_")}
                                      for r in res.values()])
            wb.add_data("A_scaling", scaling)
            wb.add_data("ordering_independence_max_deviation", f"{worst:.3e}")
            wb.add_data("lp_backend", BACKEND)
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "NOT WIRED. nucleus_real_sdp.py still calls "
                "solve_operator_selection_lp with no demand. Adopting Phase B "
                "would change every recorded n_target and make the primal "
                "determined rather than optimised — but on the present diagonal "
                "Gram it would not change a single dual, which is the finding.")
            wb.add_caveat(
                "pyhecke.atom.nf_channel_exact is NOT used for the profiles "
                "here even after its 2026-08-31 repair, because the exact-"
                "Fraction path pins q = 111/100 rather than q_0 — a separate "
                "open question. A2 now measures AGREEMENT with the direct "
                "seminormal traces and so guards the repair; it previously "
                "recorded the defect (sigma_0: 0.864044 reported vs 0.209060 "
                "direct). The numbers in this probe are unchanged by the "
                "repair.")
            wb.add_caveat(
                "LP backend is scipy, pinned and declared: the clarabel Rust "
                "binary is not built in this container, and lp_dual_solver's "
                "notes say the scipy vertex method is the more reliable for "
                "active sets (clarabel's IPM returned 28 false actives on the "
                "H_9 LP, bean qou-q7f1). Recorded clarabel active sets "
                "reproduce here under scipy.")
            wb.add_caveat(
                "Convention D's two-row cap zeroes y_lambda outside two-row "
                "lambda, so the demand — computed over all 30 blocks at A=3 — "
                "is projected onto a 5-block subspace before the LP sees it. "
                "Most of the branching information is discarded there.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
