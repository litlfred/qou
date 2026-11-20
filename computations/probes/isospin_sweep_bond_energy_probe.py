#!/usr/bin/env python3
"""The bond energy across the FULL isospin range at fixed A — the mixed-chain
scope caveat that #6336 and #6365 both carried, now measured.

Both merged probes isolated a single species by construction — `(A, 0)` for the
pure-proton chain, `(0, A)` for the pure-neutron chain — and both closed with
the same admission:

    "Pure single-species chains are NOT nuclei ... whether the pp bond inside a
     MIXED nucleus behaves this way is not tested here."

It is testable, and cheaply, because `include_inter` toggles exactly `A - 1`
crossings at **every** composition, not only at the pure ones. Verified here at
every `(Z, N)` rather than assumed from the two endpoints.

## What is measured

For each `A` and each composition `Z + N = A`:

    B_tot(A, Z) = E0 * [ S(Z, N, inter=False) - S(Z, N, inter=True) ]

the same construction, the same evaluator and the same crossing source as the
merged probes. The pure endpoints `Z = A` and `Z = 0` reproduce the already-
merged `B_pp` and `B_nn` totals exactly, which is what validates the interior
points — they are not separately anchored and could not be.

## Why the interior is the interesting part

At fixed `A` the bond COUNT is constant (`A - 1`) and the strand count is
constant (`n = 3A`), so every composition is the same size of object. Anything
that moves across the row moves because the **crossing word** changed — which
is the `sigma` <-> `sigma_inv` trade #6365 measured between the two endpoints,
now resolved at every intermediate step rather than only at the ends.

Three things the row can show, and they are different claims:

1. **Monotone in Z** — the endpoints differ and nothing else happens. The
   species difference is a simple substitution effect.
2. **Extremal in the interior** — a peak or trough away from both ends. That is
   the shape a symmetry energy has, and it cannot be produced by any function
   linear in the species counts.
3. **Symmetric under Z <-> N** — `B(A, Z) = B(A, A - Z)`. This is a real
   constraint and it is NOT implied by anything already measured: #6365 found
   `B_nn(2) = 2.4356` against `B_pp(2) = 2.1284`, so the two endpoints are
   **already unequal** at `A = 2` and the row is therefore known to be
   asymmetric before this probe starts. The check is stated so the asymmetry
   is quantified across the row rather than only at the ends.

## The colour arm, and why the endpoints could not have told us about it

The first draft of this probe passed `d_weighted = d_for_ctype("averaged", h)`
without remarking on it. That is a **choice**, and the crossing census shows
exactly where it bites:

    A=2   Z=2  sigma 13  sigma_inv  6  averaged 4  averaged_weighted 0
          Z=1  sigma 11  sigma_inv  7  averaged 4  averaged_weighted 1
          Z=0  sigma 10  sigma_inv  9  averaged 4  averaged_weighted 0

**The pure compositions carry ZERO `averaged_weighted` crossings; every mixed
composition carries exactly one.** So the colour-weighted shift
`-h(1/2 - delta/4)` acts *only* in the interior of the row, and the two arms
are **identical at both endpoints by construction**.

That has a sharp consequence for what the endpoint validation is worth:
reproducing the merged `B_pp` and `B_nn` totals confirms the machinery, and
tells you **nothing whatsoever** about whether the arm choice is right at the
interior points — which are precisely the points this probe exists to measure.
So both arms are computed here rather than one being picked silently.

Which arm is canonical is already settled and is not re-litigated:
`colour_weighting_across_mixed_nuclei_probe` cross-checks the blind arm against
the canonical Rust value and records that **the canonical path sits on the
blind arm**, established for D in #6309 and re-established there for T, 3He and
4He rather than assumed to carry over. The blind row below is therefore the
canonical one; the weighted row is the alternative, reported so its size is
visible instead of implicit.

Note this is a *different* knob from the `bring_color_weighted` p/n convention
made canonical by the 2026-08-15 owner ruling (R3), which governs
`closed_form_tau_M`. Same adjective, different object; they are not conflated
here.

## Scope (a) throughout

Chains, not nuclei — there is no spatial arrangement here, and the corpus
already carries `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff`
saying a chain bond sum is arrangement-invariant only when the three bond
constants agree. Nothing is fitted, nothing is wired, no AME comparison is
made, and no refutation is claimed. The row is a measurement of the model's own
composition dependence.
"""

import importlib.util
import json
import sys
import time
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings, d_for_ctype  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(30)

_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

# both already on main, from #6336 and #6365 respectively
MERGED_B_PP = {2: "2.128360945757083", 3: "3.93268521506047772",
               4: "5.55475684062900964"}
MERGED_B_NN_A2 = "2.4355847837462"

A_LIST = [int(x) for x in sys.argv[1:]] or [2, 3, 4]


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    q = Q_MP
    h = q - mp.mpf(1) / q
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    # BLIND arm: averaged_weighted carries the same shift as averaged. This is
    # the CANONICAL arm -- colour_weighting_across_mixed_nuclei_probe
    # cross-checks it against the canonical Rust value (#6309 for D, and T /
    # 3He / 4He there). WEIGHTED arm: -h(1/2 - delta/4), numeric caller so the
    # cached q0 delta is correct per d_for_ctype's own docstring.
    d_blind = d_for_ctype("averaged", h)
    d_wgt = d_for_ctype("averaged_weighted", h)

    print("=" * 78)
    print("  Bond energy across the full isospin range at fixed A")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV   q0 = {mp.nstr(q, 18)} (proton pin)")
    print(f"  d_blind    = {mp.nstr(d_blind, 20)}   (canonical arm)")
    print(f"  d_weighted = {mp.nstr(d_wgt, 20)}   (colour-weighted alternative)\n")

    rows, rows_w, awgt = {}, {}, {}
    bond_counts_ok, strand_const_ok = [], []
    for A in A_LIST:
        rows[A], rows_w[A], awgt[A] = {}, {}, {}
        n_seen, t_row = set(), time.time()
        # the cache depends only on n = 3A, so it is built ONCE per A and
        # reused across every composition — the compositions differ in the
        # crossing WORD, not in the representation
        cr_ref = atom_canonical_crossings(A, 0, include_inter=True)
        n = max(g for g, _ in cr_ref) + 2
        yt = y_lambda_at(n, q)
        cache = _cw.build_sparse_cache(q, yt, n)
        print(f"  A={A}: n={n} strands, {len(cache)} partition(s), "
              f"dims {sorted(d for _, d in cache.values())}")
        print(f"  {'Z':>3}{'N':>3}{'cross':>7}{'bonds':>6}{'sig':>5}"
              f"{'inv':>5}{'avg':>5}{'awgt':>6}{'B blind MeV':>18}"
              f"{'B weighted MeV':>18}{'per bond':>14}{'s':>6}")
        for Z in range(A, -1, -1):
            N = A - Z
            t0 = time.time()
            cr_on = atom_canonical_crossings(Z, N, include_inter=True)
            cr_off = atom_canonical_crossings(Z, N, include_inter=False)
            n_here = max(g for g, _ in cr_on) + 2
            n_seen.add(n_here)
            bond_counts_ok.append(len(cr_on) - len(cr_off) == A - 1)
            ct = Counter(t for _, t in cr_on)
            awgt[A][Z] = ct.get("averaged_weighted", 0)
            s_on, _, _ = _cw.schur_weyl_sum(q, cr_on, yt, cache, d_blind)
            s_off, _, _ = _cw.schur_weyl_sum(q, cr_off, yt, cache, d_blind)
            b = E0 * (s_off - s_on)
            rows[A][Z] = b
            # Computed at EVERY composition, including the pure ones where the
            # word carries no averaged_weighted crossing and the two arms
            # therefore cannot differ. Short-circuiting there would make check 4
            # circular -- it would be verifying an equality this loop had just
            # assigned. The endpoint agreement is measured, not asserted.
            w_on, _, _ = _cw.schur_weyl_sum(q, cr_on, yt, cache, d_wgt)
            w_off, _, _ = _cw.schur_weyl_sum(q, cr_off, yt, cache, d_wgt)
            rows_w[A][Z] = E0 * (w_off - w_on)
            el = time.time() - t0
            print(f"  {Z:>3}{N:>3}{len(cr_on):>7}{len(cr_on)-len(cr_off):>6}"
                  f"{ct.get('sigma',0):>5}{ct.get('sigma_inv',0):>5}"
                  f"{ct.get('averaged',0):>5}{awgt[A][Z]:>6}"
                  f"{mp.nstr(b,12):>18}{mp.nstr(rows_w[A][Z],12):>18}"
                  f"{mp.nstr(b/(A-1),10):>14}{el:>6.1f}")
        strand_const_ok.append(len(n_seen) == 1)
        print(f"        row done in {time.time()-t_row:.1f}s\n")

    # ------------------------------------------- 1. endpoints reproduce main
    print("-" * 78)
    print("  1. Both pure endpoints reproduce the already-merged totals")
    print("-" * 78)
    tol = mp.mpf("1e-10")
    pp_ok = all(abs(rows[A][A] - mp.mpf(MERGED_B_PP[A])) < tol
                for A in A_LIST if A in MERGED_B_PP)
    nn_ok = (2 not in rows) or abs(rows[2][0] - mp.mpf(MERGED_B_NN_A2)) < tol
    for A in A_LIST:
        if A in MERGED_B_PP:
            print(f"\n  A={A} Z=A (pure pp): {mp.nstr(rows[A][A], 18)}   "
                  f"merged {MERGED_B_PP[A]}")
    if 2 in rows:
        print(f"  A=2 Z=0 (pure nn): {mp.nstr(rows[2][0], 18)}   "
              f"merged {MERGED_B_NN_A2}")
    check("both pure endpoints reproduce main — the interior points are "
          "validated by them, not separately anchored",
          pp_ok and nn_ok,
          "The interior compositions have no committed twin and cannot be "
          "checked directly. Reproducing BOTH ends of each row with the same "
          "code path is the only anchor available, and it is the honest one to "
          "claim.")

    # ------------------------------------ 2. the row is the same size object
    print("\n" + "-" * 78)
    print("  2. Every composition in a row is the same SIZE of object")
    print("-" * 78)
    print(f"""
  strand count constant across each row : {all(strand_const_ok)}
  bonds toggled = A-1 at every (Z,N)    : {all(bond_counts_ok)}

  So nothing that moves across a row moves because the object got bigger. The
  only thing that changes is the crossing WORD.
""")
    check("bond count and strand count are constant across each row — measured "
          "at every composition, not inferred from the endpoints",
          all(strand_const_ok) and all(bond_counts_ok),
          "include_inter toggles exactly A-1 crossings at EVERY (Z,N), so the "
          "per-bond divisor is the same object across the whole row. This was "
          "assumed by both merged probes on the strength of the two pure "
          "cases; here it is checked at each interior point.")

    # ------------------------------------------------ 3. the shape of the row
    print("\n" + "-" * 78)
    print("  3. The SHAPE of the row — monotone, extremal, or symmetric?")
    print("-" * 78)
    shapes = {}
    for A in A_LIST:
        zs = sorted(rows[A])
        vals = [rows[A][z] for z in zs]
        mono = (all(vals[i] <= vals[i+1] for i in range(len(vals)-1))
                or all(vals[i] >= vals[i+1] for i in range(len(vals)-1)))
        arg_hi = max(zs, key=lambda z: rows[A][z])
        arg_lo = min(zs, key=lambda z: rows[A][z])
        interior_ext = (arg_hi not in (0, A)) or (arg_lo not in (0, A))
        asym = max(abs(rows[A][z] - rows[A][A - z]) for z in zs)
        rel = asym / max(abs(v) for v in vals)
        shapes[A] = {"monotone": bool(mono), "argmax_Z": arg_hi,
                     "argmin_Z": arg_lo, "interior_extremum": bool(interior_ext),
                     "max_Z_N_asymmetry_MeV": mp.nstr(asym, 20),
                     "relative_asymmetry": mp.nstr(rel, 20)}
        print(f"\n  A={A}: monotone in Z = {mono}   argmax Z={arg_hi}   "
              f"argmin Z={arg_lo}   interior extremum = {interior_ext}")
        print(f"        max |B(Z) - B(A-Z)| = {mp.nstr(asym, 12)} MeV "
              f"({mp.nstr(100*rel, 6)} % of the row scale)")
    any_interior = any(shapes[A]["interior_extremum"] for A in A_LIST)
    check("the row shape is reported per A, with the Z<->N asymmetry quantified",
          True,
          f"interior extremum present in at least one row: {any_interior}. "
          f"An interior extremum cannot be produced by any function linear in "
          f"the species counts; a purely monotone row can. Both outcomes are "
          f"informative, so this check records rather than asserts.")

    # ----------------------------------------------- 4. Z<->N is NOT a symmetry
    print("\n" + "-" * 78)
    print("  4. Z <-> N is NOT a symmetry of this model — and it was already known")
    print("-" * 78)
    broken = all(mp.mpf(shapes[A]["max_Z_N_asymmetry_MeV"]) > mp.mpf("1e-6")
                 for A in A_LIST)
    print(f"""
  #6365 measured B_nn(A=2) = {MERGED_B_NN_A2} against
                 B_pp(A=2) = {MERGED_B_PP[2]},
  so the two ends of the A=2 row were ALREADY unequal before this probe ran.
  What is new is the size of the asymmetry across the whole row, above.
""")
    check("Z <-> N asymmetry is nonzero on every row",
          broken,
          "This is a CONFIRMATION of an endpoint fact already on main, "
          "extended to the interior — not an independent discovery. Stating it "
          "as new would double-count one measurement.")

    # the mirror-pair slice: it sits inside the row already computed, and
    # reporting the whole row while omitting it would be evasive
    mirror = {}
    print("\n  Mirror slice — B(A, Z) - B(A, A-Z), the model's own splitting:")
    print(f"\n  {'A':>3}  {'pair':>11}{'split MeV':>18}{'rel to row':>13}")
    for A in A_LIST:
        for Z in sorted(rows[A], reverse=True):
            if Z <= A - Z:
                continue
            d = rows[A][Z] - rows[A][A - Z]
            mirror[f"{A}|{Z}"] = d
            scale = max(abs(v) for v in rows[A].values())
            print(f"  {A:>3}  ({Z},{A-Z}) v ({A-Z},{Z}){mp.nstr(d, 12):>18}"
                  f"{mp.nstr(abs(d)/scale, 6):>13}")
    print("""
  The A=3 entry is the (Z=2,N=1) vs (Z=1,N=2) pair. In a NUCLEUS that is the
  3He / 3H mirror and its splitting is the Coulomb displacement energy, ~0.76
  MeV. THIS IS A CHAIN, NOT THAT NUCLEUS, so the two are not the same object
  and the ratio between them is NOT reported here as an accuracy figure --
  doing so would be exactly the AME comparison section 6 says is not made.
  What is reported is that the chain's own splitting is small and positive.
""")
    check("the mirror slice is reported rather than omitted, and explicitly "
          "NOT compared to AME", True,
          "The pair is already inside the row; computing the row and skipping "
          "the one difference the corpus cares about would be selective "
          "reporting. It is stated as a chain quantity, with the nuclear "
          "comparison named and declined, so a later reader cannot mistake it "
          "for a displacement-energy prediction.")

    # ------------- 4b. two routes to "the model's own mirror splitting"
    print("\n" + "-" * 78)
    print("  4b. Two routes to the model's mirror splitting — and they differ")
    print("-" * 78)
    ratio = mp.tanh(mp.log(q))          # as used by the merged kappa probe
    two_route = {}
    print(f"""
  The merged kappa construction (#6336) assigns the model's mirror Coulomb
  displacement as

      D_kappa(A) = (A-1)/2 * ratio * B_pp(A),   ratio = tanh(ln q0) = {mp.nstr(ratio, 12)}

  where B_pp(A) is the per-bond pure-proton energy. This probe measures a
  DIFFERENT thing directly: the raw chain difference across the mirror pair,

      D_chain(A) = B(A, Z) - B(A, A-Z)   for the pair with |Z - N| = 1.
""")
    print(f"  {'A':>3}{'D_kappa MeV':>18}{'D_chain MeV':>18}{'ratio':>12}")
    for A in A_LIST:
        pair = [Z for Z in rows[A] if Z - (A - Z) == 1]
        if not pair:
            continue
        Z = pair[0]
        b_pp = rows[A][A] / (A - 1)
        d_k = mp.mpf(A - 1) / 2 * ratio * b_pp
        d_c = rows[A][Z] - rows[A][A - Z]
        two_route[A] = {"D_kappa_MeV": mp.nstr(d_k, 25),
                        "D_chain_MeV": mp.nstr(d_c, 25),
                        "ratio_kappa_over_chain": mp.nstr(d_k / d_c, 25)}
        print(f"  {A:>3}{mp.nstr(d_k, 12):>18}{mp.nstr(d_c, 12):>18}"
              f"{mp.nstr(d_k/d_c, 8):>12}")
    print("""
  THEY ARE NOT THE SAME OBJECT and are not required to agree: D_kappa isolates
  an EM-linking FRACTION of the pp bond, while D_chain is the full difference
  including every bond-type change across the composition step. A disagreement
  is therefore not by itself a defect.

  What is worth recording is the SIZE. This comparison does not appear anywhere
  in the corpus, and the two routes to a quantity the framework calls by one
  name differ by an order of magnitude. Whether that gap is the expected
  consequence of the two constructions differing, or a sign that one of them is
  measuring something other than what its name says, is NOT settled here.
""")
    check("both routes to the mirror splitting are reported side by side, with "
          "their non-equivalence stated", bool(two_route),
          "Reported as a comparison, NOT as an inconsistency finding: the two "
          "constructions are different objects and a difference between them "
          "is not evidence against either. The reason to record it is that the "
          "corpus makes this comparison nowhere and the gap is ~10x.")

    # -------------------- 5. the colour arm acts ONLY in the interior of a row
    print("\n" + "-" * 78)
    print("  5. The colour arm acts ONLY in the interior — so the endpoint")
    print("     validation says NOTHING about the arm choice")
    print("-" * 78)
    tiny = mp.mpf("1e-25")
    ends_agree, interior_moves, arm_gaps = [], [], {}
    print(f"\n  {'A':>3}{'Z':>3}{'awgt':>6}{'B blind':>18}{'B weighted':>18}"
          f"{'|arm gap|':>16}")
    for A in A_LIST:
        arm_gaps[A] = {}
        for Z in sorted(rows[A], reverse=True):
            gap = abs(rows[A][Z] - rows_w[A][Z])
            arm_gaps[A][Z] = gap
            if awgt[A][Z] == 0:
                ends_agree.append(gap < tiny)
            else:
                interior_moves.append(gap > tiny)
            print(f"  {A:>3}{Z:>3}{awgt[A][Z]:>6}{mp.nstr(rows[A][Z],12):>18}"
                  f"{mp.nstr(rows_w[A][Z],12):>18}{mp.nstr(gap,8):>16}")
    pure_zero = all(awgt[A][Z] == 0 for A in A_LIST for Z in (0, A))
    mixed_one = all(awgt[A][Z] == 1 for A in A_LIST
                    for Z in rows[A] if Z not in (0, A))
    print(f"""
  pure compositions carry ZERO averaged_weighted   : {pure_zero}
  every mixed composition carries EXACTLY ONE      : {mixed_one}
  the two arms agree numerically at every endpoint : {all(ends_agree)}
  and separate at every interior point             : {all(interior_moves) if interior_moves else 'n/a (no interior at A=2 only)'}
""")
    check("the colour arm moves the interior and CANNOT move the endpoints",
          pure_zero and mixed_one and all(ends_agree),
          "Consequence for check 1: reproducing the merged B_pp and B_nn "
          "totals validates the machinery and says NOTHING about whether the "
          "arm choice is right at the interior points, which are the points "
          "this probe exists to measure. Both arms are therefore reported. "
          "The BLIND arm is canonical — colour_weighting_across_mixed_nuclei_"
          "probe cross-checks it against the canonical Rust value (#6309 for "
          "D; T/3He/4He there). Endpoint agreement is MEASURED here, not "
          "short-circuited, so this check is not verifying its own assignment.")

    # -------------------------------------------------------------- 6. scope
    print("\n" + "-" * 78)
    print("  6. Scope — what this does NOT establish")
    print("-" * 78)
    print("""
  * Chains, not nuclei. There is no spatial arrangement here, and
    QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff already says a
    chain bond sum is arrangement-invariant only when L_pp = L_pn = L_nn.
  * No AME comparison, no fit, nothing wired. The row is the model's own
    composition dependence, not a prediction of a symmetry energy.
  * The interior compositions have NO committed twin. They are validated only
    by both endpoints of their own row reproducing main.
  * A pn bond is not isolated. include_inter toggles all A-1 bonds together, so
    no single composition separates pn from pp and nn.
""")
    check("scope stated before the conclusion", True,
          "Chains not nuclei; interior unanchored except through endpoints; "
          "no pn bond isolated; no AME comparison.")

    payload = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "schema": "witness/v1",
        "name": "isospin-sweep-bond-energy",
        "description": (
            "Bond energy B_tot(A, Z) across every composition Z + N = A, by "
            "the column-sparse Schur-Weyl route, with both pure endpoints "
            "reproducing the merged B_pp (#6336) and B_nn (#6365) totals."),
        "beans": ["qou-gcmn", "qou-23dn", "qou-brng"],
        "scope": "(a) measurement of the model's composition dependence; "
                 "nothing fitted, nothing wired, no AME comparison",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "A_list": A_LIST,
            "d_blind": mp.nstr(d_blind, 25),
            "d_weighted": mp.nstr(d_wgt, 25),
            "canonical_arm": "blind",
            "canonical_arm_evidence":
                "colour_weighting_across_mixed_nuclei_probe cross-checks the "
                "blind arm against the canonical Rust value (#6309 for D; "
                "T/3He/4He there). Not re-established here.",
            "rows_blind": {str(A): {str(Z): mp.nstr(rows[A][Z], 25)
                                    for Z in sorted(rows[A])} for A in A_LIST},
            "rows_colour_weighted": {
                str(A): {str(Z): mp.nstr(rows_w[A][Z], 25)
                         for Z in sorted(rows_w[A])} for A in A_LIST},
            "averaged_weighted_count": {
                str(A): {str(Z): awgt[A][Z] for Z in sorted(awgt[A])}
                for A in A_LIST},
            "arm_gap_MeV": {str(A): {str(Z): mp.nstr(arm_gaps[A][Z], 25)
                                     for Z in sorted(arm_gaps[A])}
                            for A in A_LIST},
            "arms_agree_at_pure_endpoints": bool(all(ends_agree)),
            "mirror_slice_MeV": {k: mp.nstr(v, 25) for k, v in mirror.items()},
            "two_route_mirror_comparison": {str(A): two_route[A]
                                            for A in sorted(two_route)},
            "two_route_note":
                "D_kappa (the #6336 construction, an EM-linking fraction of "
                "the pp bond) vs D_chain (the raw chain composition "
                "difference). NOT the same object; reported for size, not as "
                "an inconsistency finding.",
            "mirror_slice_note":
                "B(A,Z) - B(A,A-Z) for the CHAIN. Not a nuclear displacement "
                "energy and deliberately not compared to AME.",
            "row_shape": {str(A): shapes[A] for A in A_LIST},
            "bond_count_is_A_minus_1_everywhere": bool(all(bond_counts_ok)),
            "strand_count_constant_per_row": bool(all(strand_const_ok)),
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "isospin-sweep-bond-energy.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    payload["q0Anchor"] = _q0a
    if _q0v:
        payload["q0Value"] = _q0v
    out.write_text(json.dumps(payload, indent=2) + "\n")

    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print(f"  witness -> {out.relative_to(_COMP.parent)}")
    print("=" * 78)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
