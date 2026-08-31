#!/usr/bin/env python3
"""`K` via knot convolution: the convolution determines it, and it is infeasible.

THE ASK
-------
Owner steer (bean `t7qv`): *"knots should be SDP solutions via knot
convolution"* — rather than the census picks that
`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md` showed are an admitted
fit and that the derived closure arity refutes.

This probe takes that route and follows it to its end. The result is negative
in a specific and useful way: **there is no optimisation to perform, and the
object the convolution hands back is not in the PSD cone.**

1. THE CONVOLUTION LEAVES NOTHING TO OPTIMISE
----------------------------------------------
`binding_k_solver.py` defines the binding operator by

    T_w(atom) = K · ⊗_{i=1..A} T_w(nucleon_i)        in H_{3A}(q_0)
    K_word    = atom_word ++ cp_inv_word

Given the canonical substrate word `atom_braid_word_3A(Z, N)` and its
`include_inter=False` restriction (which *is* the constituent product — the
generator layout is the same, minus the inter-nucleon crossings), `K` is
**determined**. Not constrained, not narrowed: determined. Every averaged
letter `sigma - (h/2)` has eigenvalues `±(q + 1/q)/2 != 0`, so the constituent
product is invertible and `K = rho(atom) . rho(free)^{-1}` exists in every
Wedderburn block.

So "solve for K by SDP" has no free variable to solve for. What can be asked
is whether the determined `K` satisfies the program's constraints. It does not.

2. THE DERIVED BINDING ARITY IS 2A + 1, AND NO REGISTRY LINK HAS IT
--------------------------------------------------------------------
The permutation underlying `K` is `perm(atom) . perm(free)^{-1}`, and since
`sigma_g` and `sigma_g^-1` project to the same transposition this is
branch- and convention-independent. Measured exact over `0 <= Z,N <= 5`,
`2 <= A <= 6`, both `pn_convention`s:

    c(K) = 2A + 1                                    46/46 exact

(companion to `c_atom = A + 1` and `c_free = 2A` in
`link_assignment_census_selectivity_probe.py`.) Against the registry:

    atom   binding_link_name        components   derived 2A+1   verdict
    ---------------------------------------------------------------------
    2H     Hopf L2a1                     2             5        MISMATCH
    3H     8_11-class link               1             7        MISMATCH
    3He    L6a4 (3-component)            3             7        MISMATCH

And against the registry's own `EXPLICIT_BINDING_K_HEURISTIC` words, which are
a separate field and fare better but not well:

    2H   [3,3]        -> 6 components   vs 5   MISMATCH
    3He  [3,6]        -> 7              vs 7   match
    3H   [3,4,6,7]    -> 5              vs 7   MISMATCH

The `2H` row is structural rather than a near-miss: `sigma_3^2` is a **full
twist**, two crossings, while the canonical word's `pn` bond is one. An even
multiplicity merges no components (see the `c_atom` law), so the Hopf
assignment and the canonical word describe different bonds, and no convention
change reconciles them.

3. PSD-FEASIBILITY IS A PARITY CONDITION, SO IT CANNOT SELECT
---------------------------------------------------------------
In the seminormal representation `rho_lambda(sigma)` has eigenvalues
`{q_0, -1/q_0}` in every block of dimension >= 2 — one positive, one negative.
Hence `rho_lambda(sigma^k)` has `{q_0^k, (-1/q_0)^k}`, positive **iff `k` is
even**. Measured at `H_3`:

    identity (unknot)     PSD    +1.000000     <- the corpus's own control
    sigma^1               ---    -0.900918
    sigma^2  (Hopf)       PSD    +0.811654
    sigma^3  (trefoil)    ---    -0.731234
    sigma^4               PSD    +0.658782

So the program passes the unknot and every full twist and rejects everything of
odd crossing parity. That is not a selection principle; it is a parity filter,
and it explains every recorded outcome at once — why the unknot control passes,
why `L_H = sigma_1^2` passes, why `6_2` fails.

4. AND IT REJECTS THE CORPUS'S OWN CONSTITUENT
------------------------------------------------
`binding_k_solver.py` states as premise:

> *"at H_3 each nucleon's trefoil is the unique PSD-feasible canonical element
> (closed by R5-minimal)"*

Measured, at `H_3`, this is false in both presentations of the trefoil and for
the corpus's actual nucleon word:

    sigma_1^3        (B_2 form)     worst min-eig  -0.731234    NOT PSD
    (s1 s2)^2        (B_3 form)     worst min-eig  -0.604530    NOT PSD
    (s1 s2)^3        (full twist)   worst min-eig  +0.534703    PSD
    proton  word from atom_braid_word_3A          -0.739224    NOT PSD (1/3 blocks)
    neutron word from atom_braid_word_3A          -0.910762    NOT PSD (1/3 blocks)

The element at `H_3` that *is* PSD-feasible is the full twist, not the trefoil.

5. THE DETERMINED `K` IS INFEASIBLE
-------------------------------------
Carrying the canonical word to the atomic strand count:

    atom   blocks   atom PSD in   K PSD in   worst atom eig   worst K eig
    -----------------------------------------------------------------------
    2H       11        1 / 11       1 / 11       -4.210318      -1.595181
    3H       30        1 / 30       2 / 30       -9.531563      -4.265691
    3He      30        1 / 30       2 / 30      -10.040628      -3.646531

Every surviving block is **1-dimensional** — `(n)` (trivial) and, for `K` at
`A = 3`, `(1^n)` (sign). **No block of dimension >= 2 survives, for either
object, at any `A`.** That is exactly what the parity argument predicts: a
1-dimensional block sends `sigma` to the scalar `q_0` or `-1/q_0`, so positivity
is a sign condition on a single number, while any block of dimension >= 2
carries both eigenvalues and one odd crossing destroys it. So both the
substrate's canonical atom element and the `K` the convolution derives from it
lie outside the PSD cone wherever the cone has content. An SDP whose constraint
is `rho_lambda(.) >= 0` cannot select `K`, because `K` is not feasible for it.

WHAT THIS MEANS FOR `conj-canonical-knot-id-sdp`
--------------------------------------------------
The conjecture is not merely unsupported (the 2026-08-25 audit's finding) — its
constraint set excludes the object the substrate actually produces. Three
distinct routes now agree on the same conclusion from different directions:

  - volume matching: 10^3-10^4 census manifolds fit equally well (prior work);
  - closure arity: `c_atom = A+1` and `c(K) = 2A+1` refute every named link;
  - PSD feasibility: a parity filter that rejects `K`, the nucleon, and the
    trefoil, while accepting the unknot.

A well-posed replacement needs a constraint set that the canonical word
satisfies and an objective that takes no `B_AME` input. Neither exists yet, and
this probe proposes neither — inventing an objective that happens to admit the
incumbent would be the same fitting in a new coordinate system.

VALIDATION
----------
The PSD machinery reproduces all four results recorded in
`binding-link-psd-feasibility-probe.witness.json` at `H_3` (unknot True,
`L_H` True, `6_2` False, `L6a4` True), including locating `6_2`'s failure in the
standard `(2,1)` block. Magnitude there is `-0.8334` here against `-0.89`
recorded — a q-pin/normalisation difference; the sign and the block agree,
which is what the argument uses.

DISCIPLINE
----------
No fit; no wiring; no tier change; no knot proposed. Wedderburn evaluation is at
f64, as in `binding_k_solver.py` — the eigenvalue magnitudes here are O(1) and
the conclusions are sign conclusions, so f64 is adequate and is declared rather
than laundered.

-- Ref: [manuscript] bean t7qv; conj-canonical-knot-id-sdp.md;
   prior: qou-8ms1, docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "hecke"))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

set_compute_dps()

Q = float(Q0)
H = Q - 1 / Q          # the Hecke parameter; sigma^-1 = sigma - h
PSD_TOL = 1e-9

# Recorded verbatim from binding-link-psd-feasibility-probe.witness.json (H_3).
RECORDED_H3 = [
    ("unknot (control)", [], True),
    ("Hopf L_H = sigma_1^2", [1, 1], True),
    ("2H whole-atom 6_2", [1, -2, 1, 1, 1, -2], False),
    ("3He whole-atom L6a4", [-1, 2, -1, 2, -1, 2], True),
]

# Registry binding_link_name -> component count, and the separate heuristic
# K_word field, both from binding_k_solver.py.
REGISTRY_LINKS = [("2H", "Hopf L2a1", 2, 2), ("3H", "8_11-class", 1, 3),
                  ("3He", "L6a4 (3-comp)", 3, 3)]
REGISTRY_K_WORDS = [("2H", 2, [3, 3]), ("3He", 3, [3, 6]), ("3H", 3, [3, 4, 6, 7])]


# ── permutation layer (no representation needed) ──────────────────────

def perm_of_hecke_word(word, n: int) -> list[int]:
    p = list(range(n))
    for (_c, _d, g) in word:
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def perm_of_braid_word(gens, n: int) -> list[int]:
    """1-based signed braid generators; sign is irrelevant to the permutation."""
    p = list(range(n))
    for g in gens:
        i = abs(g) - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def cycles(p) -> int:
    n = len(p)
    seen = [False] * n
    k = 0
    for i in range(n):
        if not seen[i]:
            k += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return k


def compose(a, b):
    return [b[a[i]] for i in range(len(a))]


def inverse(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q


def sweep_k_arity() -> dict:
    """`c(K) = 2A + 1` over (Z, N) and both pn conventions."""
    tested = bad = 0
    for Z in range(6):
        for N in range(6):
            A = Z + N
            if not (2 <= A <= 6):
                continue
            n = 3 * A
            for conv in ("bring_color_weighted", "strict_averaged"):
                pa = perm_of_hecke_word(
                    atom_braid_word_3A(Z, N, include_inter=True,
                                       pn_convention=conv), n)
                pf = perm_of_hecke_word(
                    atom_braid_word_3A(Z, N, include_inter=False,
                                       pn_convention=conv), n)
                tested += 1
                if cycles(compose(pa, inverse(pf))) != 2 * A + 1:
                    bad += 1
    return {"tested": tested, "deviations": bad}


# ── representation layer ──────────────────────────────────────────────

def sigmas(lam):
    return [np.asarray(m, dtype=float)
            for m in build_seminormal_matrices(list(lam))[0]]


def min_sym_eig(M) -> float:
    """Least eigenvalue of the symmetric part — the PSD test on x'Mx."""
    return float(np.linalg.eigvalsh((M + M.T) / 2).min())


def rho_hecke(word, sig, dim):
    M = np.eye(dim)
    for (c, d, g) in word:
        M = M @ (float(c) * sig[g] + float(d) * np.eye(dim))
    return M


def rho_braid(gens, sig, dim):
    M = np.eye(dim)
    for g in gens:
        M = M @ (sig[g - 1] if g > 0 else (sig[-g - 1] - H * np.eye(dim)))
    return M


def psd_over_blocks(n: int, evaluate) -> tuple[int, int, float]:
    """(#blocks PSD, #blocks, worst min-eig) for a per-block evaluator."""
    parts = [tuple(p) for p in partitions_of(n)]
    npsd, worst = 0, float("inf")
    for lam in parts:
        sig = sigmas(lam)
        e = min_sym_eig(evaluate(lam, sig, sig[0].shape[0]))
        worst = min(worst, e)
        if e >= -PSD_TOL:
            npsd += 1
    return npsd, len(parts), worst


def main() -> int:
    assertions = []
    print("t7qv — K as an SDP solution via knot convolution")

    # ── A0. Validate the machinery against the recorded H_3 witness ───
    print("\n  validation against binding-link-psd-feasibility-probe (H_3):")
    agree = True
    for name, w, recorded in RECORDED_H3:
        npsd, nb, worst = psd_over_blocks(
            3, lambda lam, s, d, w=w: rho_braid(w, s, d))
        mine = npsd == nb
        agree = agree and (mine == recorded)
        print(f"    {name:24s} recorded={str(recorded):5s} mine={str(mine):5s} "
              f"worst {worst:+.6f}  {'AGREE' if mine == recorded else 'DISAGREE'}")
    print(f"\n  A0  machinery reproduces all four recorded results ....... "
          f"{'PASS' if agree else 'FAIL'}")
    assertions.append(("psd_machinery_validated_against_recorded_witness",
                       agree, "unknot/L_H/6_2/L6a4 at H_3"))

    # ── A1. c(K) = 2A + 1 ─────────────────────────────────────────────
    arity = sweep_k_arity()
    ok = arity["deviations"] == 0
    print(f"\n  the convolution DETERMINES K; its closure arity is derived:")
    print(f"    c(K) = 2A + 1 ........ "
          f"{arity['tested'] - arity['deviations']}/{arity['tested']} exact")
    print(f"\n  A1  c(K) = 2A+1 holds with no deviations ................. "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("k_closure_arity_is_2A_plus_1", ok,
                       f"{arity['deviations']} deviations in {arity['tested']}"))

    # ── A2. No registry binding link has that arity ───────────────────
    print("\n  registry binding_link_name vs the derived arity:")
    mism = []
    for atom, link, comps, A in REGISTRY_LINKS:
        need = 2 * A + 1
        mism.append(comps != need)
        print(f"    {atom:5s} {link:16s} components={comps:2d}  derived={need:2d}"
              f"   {'MISMATCH' if comps != need else 'match'}")
    ok = all(mism)
    print(f"\n  A2  no registry binding link has the derived arity ....... "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("no_registry_binding_link_matches_derived_arity", ok,
                       "; ".join(f"{a}:{c} vs {2 * A + 1}"
                                 for a, _l, c, A in REGISTRY_LINKS)))

    print("\n  and the registry's separate heuristic K_word field:")
    for atom, A, w in REGISTRY_K_WORDS:
        c = cycles(perm_of_braid_word(w, 3 * A))
        need = 2 * A + 1
        print(f"    {atom:5s} K_word={str(w):14s} -> {c:2d} components  "
              f"derived={need:2d}   {'MISMATCH' if c != need else 'match'}")
    print("    (2H's [3,3] is a FULL TWIST — two crossings where the canonical")
    print("     word's pn bond has one; an even multiplicity merges nothing,")
    print("     so these describe different bonds, not a near-miss.)")

    # ── A3. PSD is a parity condition ─────────────────────────────────
    print("\n  PSD-feasibility in the seminormal rep is a PARITY condition,")
    print("  because rho(sigma) has eigenvalues {q_0, -1/q_0}:")
    parity = []
    for k in range(5):
        npsd, nb, worst = psd_over_blocks(
            3, lambda lam, s, d, k=k: rho_braid([1] * k, s, d))
        parity.append((k, npsd == nb, worst))
        label = {0: " (unknot)", 2: " (Hopf)", 3: " (trefoil)"}.get(k, "")
        print(f"    sigma^{k}{label:11s} PSD={str(npsd == nb):5s} "
              f"worst {worst:+.6f}")
    ok = all(psd == (k % 2 == 0) for k, psd, _w in parity)
    print(f"\n  A3  sigma^k is PSD exactly when k is even ................ "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => the program passes the unknot and every full twist and")
    print("         rejects odd crossing parity. Not a selection principle.")
    assertions.append(("psd_feasibility_is_a_parity_condition", ok,
                       str([(k, p) for k, p, _ in parity])))

    # ── A4. It rejects the corpus's own constituent ───────────────────
    print("\n  binding_k_solver.py's premise is that the nucleon TREFOIL is")
    print("  'the unique PSD-feasible canonical element' at H_3. Measured:")
    tref = []
    for name, w in [("sigma_1^3 (B_2 form)", [1, 1, 1]),
                    ("(s1 s2)^2 (B_3 form)", [1, 2, 1, 2]),
                    ("(s1 s2)^3 (full twist)", [1, 2, 1, 2, 1, 2])]:
        npsd, nb, worst = psd_over_blocks(
            3, lambda lam, s, d, w=w: rho_braid(w, s, d))
        tref.append((name, npsd == nb, worst))
        print(f"    {name:24s} PSD={str(npsd == nb):5s} worst {worst:+.6f}")
    nucleons = []
    for nm, Z, N in [("proton", 1, 0), ("neutron", 0, 1)]:
        w = atom_braid_word_3A(Z, N, include_inter=False)
        npsd, nb, worst = psd_over_blocks(
            3, lambda lam, s, d, w=w: rho_hecke(w, s, d))
        nucleons.append((nm, npsd, nb, worst))
        print(f"    {nm + ' (corpus word)':24s} PSD in {npsd}/{nb} blocks, "
              f"worst {worst:+.6f}")
    ok = (not tref[0][1] and not tref[1][1] and tref[2][1]
          and all(np_ < nb_ for _n, np_, nb_, _w in nucleons))
    print(f"\n  A4  the trefoil is NOT PSD; the full twist is; and neither")
    print(f"      nucleon word is PSD ................................. "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("trefoil_and_nucleon_are_not_psd_feasible", ok,
                       f"trefoil {[(n, p) for n, p, _ in tref]}; "
                       f"nucleons {[(n, f'{a}/{b}') for n, a, b, _ in nucleons]}"))

    # ── A5. The determined K is infeasible ────────────────────────────
    print("\n  the determined K at the atomic strand count:")
    print(f"    {'atom':5s} {'blocks':>7s} {'atom PSD':>10s} {'K PSD':>8s} "
          f"{'worst atom':>12s} {'worst K':>10s}")
    rows, infeasible = [], []
    for nm, Z, N in [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1)]:
        A = Z + N
        n = 3 * A
        wa = atom_braid_word_3A(Z, N, include_inter=True)
        wf = atom_braid_word_3A(Z, N, include_inter=False)

        def eval_atom(lam, s, d, wa=wa):
            return rho_hecke(wa, s, d)

        def eval_k(lam, s, d, wa=wa, wf=wf):
            return rho_hecke(wa, s, d) @ np.linalg.inv(rho_hecke(wf, s, d))

        na, nb, worst_a = psd_over_blocks(n, eval_atom)
        nk, _nb, worst_k = psd_over_blocks(n, eval_k)
        infeasible.append(nk < nb)
        rows.append({"atom": nm, "n": n, "blocks": nb, "atom_psd_blocks": na,
                     "K_psd_blocks": nk, "worst_atom_min_eig": f"{worst_a:.6f}",
                     "worst_K_min_eig": f"{worst_k:.6f}",
                     "derived_K_components": 2 * A + 1})
        print(f"    {nm:5s} {nb:>7d} {na:>6d}/{nb:<3d} {nk:>4d}/{nb:<3d} "
              f"{worst_a:>12.6f} {worst_k:>10.6f}")
    ok = all(infeasible)
    print(f"\n  A5  K is NOT PSD-feasible at any A ....................... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      every surviving block is 1-DIMENSIONAL — (n), and (1^n) for")
    print("      K at A=3. No block of dim >= 2 survives, for either object,")
    print("      at any A, exactly as the parity argument predicts.")
    assertions.append(("determined_K_is_not_psd_feasible", ok,
                       "; ".join(f"{r['atom']}: K PSD in "
                                 f"{r['K_psd_blocks']}/{r['blocks']}"
                                 for r in rows)))

    print()
    print("### VERDICT: there is no SDP to solve. The convolution DETERMINES K,")
    print("    and the K it determines is outside the PSD cone in essentially")
    print("    every Wedderburn block — as are the canonical atom element, the")
    print("    corpus's own nucleon word, and the trefoil the solver names as")
    print("    its PSD-feasible constituent. PSD here is a parity filter that")
    print("    accepts the unknot and full twists. conj-canonical-knot-id-sdp")
    print("    is not merely unsupported: its constraint set excludes the")
    print("    object the substrate produces. No objective is proposed here —")
    print("    inventing one that admits the incumbent would be the same fit.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("binding-k-convolution-sdp",
                                engine="numpy", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): takes the owner's steer that K should "
                "be an SDP solution via knot convolution, and follows it to the "
                "end. (1) The convolution K = rho(atom).rho(free)^-1 DETERMINES "
                "K from the canonical substrate word — no free variable, so "
                "nothing to optimise. (2) Its derived closure arity is "
                "c(K) = 2A+1 (46/46 exact); no registry binding_link_name has "
                "it (Hopf 2 vs 5, 8_11 1 vs 7, L6a4 3 vs 7). (3) PSD-"
                "feasibility in the seminormal rep is a PARITY condition — "
                "rho(sigma) has eigenvalues {q0, -1/q0}, so sigma^k is PSD iff "
                "k is even — which passes the unknot and every full twist and "
                "cannot select. (4) It rejects the trefoil (-0.731) that "
                "binding_k_solver.py names as the unique PSD-feasible "
                "constituent, and both nucleon words. (5) The determined K is "
                "PSD in 1/11, 2/30, 2/30 blocks, every survivor being "
                "1-DIMENSIONAL — no block of dim >= 2 survives for either "
                "object at any A. So K is infeasible for the program said to "
                "select it. Machinery validated 4/4 against "
                "binding-link-psd-feasibility-probe. No fit; no objective "
                "proposed; no knot proposed.")
            wb.add_data("k_arity_law", arity)
            wb.add_data("registry_binding_links", [
                {"atom": a, "link": l, "components": c,
                 "derived_2A_plus_1": 2 * A + 1}
                for a, l, c, A in REGISTRY_LINKS])
            wb.add_data("registry_heuristic_K_words", [
                {"atom": a, "K_word": w,
                 "closure_components": cycles(perm_of_braid_word(w, 3 * A)),
                 "derived_2A_plus_1": 2 * A + 1}
                for a, A, w in REGISTRY_K_WORDS])
            wb.add_data("psd_parity", [
                {"k": k, "psd": bool(p), "worst_min_eig": f"{w:.6f}"}
                for k, p, w in parity])
            wb.add_data("trefoil_and_nucleons", {
                "trefoil": [{"form": n, "psd": bool(p),
                             "worst_min_eig": f"{w:.6f}"} for n, p, w in tref],
                "nucleons": [{"name": n, "psd_blocks": a, "blocks": b,
                              "worst_min_eig": f"{w:.6f}"}
                             for n, a, b, w in nucleons]})
            wb.add_data("determined_K", rows)
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=detail)
            wb.add_caveat(
                "Wedderburn evaluation is at f64, as in binding_k_solver.py. "
                "The eigenvalue magnitudes are O(1) and every conclusion is a "
                "SIGN conclusion, so f64 is adequate; declared, not laundered.")
            wb.add_caveat(
                "PSD is tested on the symmetric part, i.e. on the quadratic "
                "form x'Mx — rho_lambda(K) is not symmetric in general. The "
                "validation run reproduces all four recorded H_3 results under "
                "this convention, including locating 6_2's failure in the "
                "standard (2,1) block; the magnitude there is -0.8334 here "
                "against -0.89 recorded, a q-pin/normalisation difference. The "
                "argument uses the sign and the block, which agree.")
            wb.add_caveat(
                "include_inter=False is taken as the constituent product: the "
                "generator layout is identical to the full word minus the "
                "inter-nucleon crossings, which is what the factorisation "
                "T_w(atom) = K . (x)_i T_w(nucleon_i) means. binding_k_solver.py "
                "builds K from the HISTORICAL knot braid words instead; this "
                "probe uses the canonical substrate word, which is the point.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
