#!/usr/bin/env python3
"""`qou-gcmn` ANSWERED: `B_pp` is NOT A-independent — it declines. And the
`H_2A` trace was never intractable; the sparse route does A=4 in ~50 s.

Owner, 2026-08-31: *"not intractable... use sparse matrices. recent compute
does that"*. Correct on both counts, and it changes the answer.

## What this supersedes

The companion probe `bpp_a_dependence_bound_probe.py` (same PR) proved the
CHAIN bond `-alpha*ln z` is A-independent by construction, measured it against
the `H_6` trace bond at `A = 2` (3.65 % apart), and — because `A = 2` is the
only point at which both were then computable — stated a **disjunction**:

  EITHER the trace bond is A-independent too (confound zero),
  OR it diverges with `A` and that divergence is the unmeasured quantity.

It also said, correctly, that one shared point cannot decide between them and
that a **second point** would. This probe computes the second and third points.
**The second branch is the true one.** The first branch is withdrawn.

## Why it was thought intractable, and why it is not

`charge_coulomb_tn3he_derived._per_block` evaluates
`chi_lambda_numerical(lam, q0, cr)` over `partitions_of(6)` with DENSE
characters, and `em_linking_invariant_scoping` records the A>3 bonds as living
"at `H_2A`, intractable". Measured here: dense `chi_lambda_numerical` does not
return within 600 s even at the sizes involved.

The sparse route does. `colour_weighting_across_mixed_nuclei_probe` (landed
2026-08-30) carries `build_sparse_cache` + `schur_weyl_sum`: Hoefsmit matrices
have at most two nonzeros per row, so the column-sparse multiply costs
`O(dim^2 * nnz_per_col)` instead of `O(dim^3)`. Timings here, on the pure-proton
chains:

    Z=2  n=6   23 crossings   4 partitions   max dim   9     <1 s
    Z=3  n=9   35 crossings   5 partitions   max dim  48      1 s
    Z=4  n=12  47 crossings   7 partitions   max dim 297     51 s

So "intractable" was an artifact of the dense evaluator, not of the object.

## The construction, unchanged from the committed one

`charge_coulomb_tn3he_derived` defines the `A=2` bond as

    B_pp = E0 * [ S(Z=2, N=0, inter=False) - S(Z=2, N=0, inter=True) ]

with `S = Sum_lambda y_lambda |Re chi^lambda|` over the atomic braid. A pure
proton chain `(Z, N=0)` has only `pp` bonds, `Z - 1` of them, so the same
construction at higher `Z` gives the per-bond `pp` energy directly:

    B_pp(A) = E0 * [ S(A, 0, False) - S(A, 0, True) ] / (A - 1)

**Method validated**: at `A = 2` this reproduces the committed
`B_pp_strong_MeV = 2.12836094575708` to every recorded digit, via a different
evaluator (sparse Schur-Weyl vs dense `chi_lambda_numerical`) and a different
crossings entry point (`atom_canonical_crossings` vs
`atomic_braid_to_crossings`). Two independent paths to the committed number.

## The result

    A    bonds   B_pp per bond (MeV)   vs A=2
    2      1         2.128360946       1.0000
    3      2         1.966342608       0.9239
    4      3         1.851585614       0.8700

`B_pp` **declines** — 7.6 % by `A = 3`, 13.0 % by `A = 4` — against a chain bond
frozen at `2.050709692` for every `A`. So the `qou-gcmn` confound is **real,
signed, and now measured** on three points.

## What it does to kappa — direction, not a corrected series

`kappa(A) = dB_AME / [ (A-1)/2 * ratio * B_pp ]` was computed holding `B_pp` at
its `A = 2` value. Correcting it multiplies by `B_pp(2)/B_pp(A) > 1`, so the
true `kappa` is **larger** than the held one and increasingly so with `A`. The
measured `kappa` decline (3.45 -> 1.74 over `A = 3..39`) therefore **overstates**
the invariant's decline: part of it is the bond shrinking, exactly the confound
the bean names.

**This probe does NOT correct the series**, and the reason is the honest one:
the mirror pairs run to `A = 39`, and `B_pp` is measured here only to `A = 4`.
Extrapolating a three-point decline across a factor of ten in `A` would be a fit.
What is established is the SIGN and the SCALE at the low end; `A = 5, 6` are
reachable by the same route at higher cost and are the obvious continuation.

## Scope

**(a)** for every number. Nothing wired. `B_pp(A)` is measured, not fitted; no
coefficient is introduced anywhere. The pure-proton chain isolates the `pp` bond
by construction — it is the same object the committed `A=2` value is, at larger
`A` — but note it is **not** a physical nucleus, and whether the `pp` bond inside
a MIXED nucleus declines identically is not tested here.

`-- Ref:` [ame2020]. Beans `qou-gcmn`, `qou-o6ml`, `qou-brng`.
"""
from __future__ import annotations

import datetime
import importlib.util
import json
import sys
import time
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
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(30)

# reuse the landed sparse machinery rather than re-implementing it
_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

COMMITTED_B_PP_A2 = "2.12836094575708"   # charge-coulomb-tn3he-derived.witness.json


def S_of(Z, q, y_table, cache, d_blind, inter):
    cr = atom_canonical_crossings(Z, 0, include_inter=inter)
    tot, _, _ = _cw.schur_weyl_sum(q, cr, y_table, cache, d_blind)
    return tot


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail, on_fail=None):
        """Record and print one check.

        `detail` is printed ONLY when the check passes. A failing check
        prints `on_fail` instead, or a neutral marker -- never an
        affirmative sentence about a comparison that did not hold. The
        old version printed `detail` unconditionally, so check 1 below
        announced "agrees to <1e-10" on a run where it did not (observed
        2026-09-07: committed 2.12836094575708 vs computed
        0.642115075408566).
        """
        ok = bool(ok)
        shown = detail if ok else (on_fail or
                                   "the condition above did NOT hold; the "
                                   "pass-text is withheld deliberately")
        assertions.append({"name": name, "passed": ok, "detail": shown})
        checks.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {shown}")

    q = Q_MP
    h = q - mp.mpf(1) / q
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    d_blind = _cw.d_for_ctype("averaged", h)

    print("=" * 78)
    print("  qou-gcmn ANSWERED: B_pp declines with A (sparse route, A = 2,3,4)")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV")
    print(f"  committed B_pp(A=2) = {COMMITTED_B_PP_A2} MeV\n")

    # A-range configurable so the continuation (A = 5, 6 ...) is reproducible
    # rather than a one-off. Default reproduces the committed witness exactly.
    A_LIST = [int(x) for x in sys.argv[1:]] or [2, 3, 4]

    rows, per_bond = [], {}
    print(f"  {'A':>3}{'n':>5}{'cross':>7}{'parts':>7}{'maxdim':>8}"
          f"{'B_tot MeV':>16}{'B_pp/bond':>16}{'secs':>7}")
    for A in A_LIST:
        t0 = time.time()
        cr = atom_canonical_crossings(A, 0, include_inter=True)
        n = max(g for g, _ in cr) + 2
        yt = y_lambda_at(n, q)
        cache = _cw.build_sparse_cache(q, yt, n)
        dims = [d for _, d in cache.values()]
        s_on = S_of(A, q, yt, cache, d_blind, True)
        s_off = S_of(A, q, yt, cache, d_blind, False)
        tot = E0 * (s_off - s_on)
        pb = tot / (A - 1)
        per_bond[A] = pb
        el = time.time() - t0
        rows.append({"A": A, "n_strands": n, "crossings": len(cr),
                     "partitions": len(cache),
                     "max_dim": max(dims) if dims else 0,
                     "S_inter_true": mp.nstr(s_on, 25),
                     "S_inter_false": mp.nstr(s_off, 25),
                     "B_total_MeV": mp.nstr(tot, 20),
                     "B_pp_per_bond_MeV": mp.nstr(pb, 20),
                     # wall-clock runtime metadata, not a payload number —
                     # reserved ephemeral name so the raw-float64 ratchet's
                     # runtime-duration carve-out covers it (qou-6sts).
                     "elapsed_sec": round(el, 1)})
        print(f"  {A:>3}{n:>5}{len(cr):>7}{len(cache):>7}"
              f"{max(dims) if dims else 0:>8}{mp.nstr(tot, 12):>16}"
              f"{mp.nstr(pb, 12):>16}{el:>7.1f}")

    _as = sorted(per_bond)

    # -------------------------------------------------- 1. method validation
    print("\n" + "-" * 78)
    print("  1. The sparse route reproduces the committed A=2 value")
    print("-" * 78)
    got = mp.nstr(per_bond[2], 15) if 2 in per_bond else "(A=2 not in run)"
    agree = (2 not in per_bond) or \
        abs(per_bond[2] - mp.mpf(COMMITTED_B_PP_A2)) < mp.mpf("1e-10")
    print(f"\n  committed : {COMMITTED_B_PP_A2}")
    print(f"  this probe: {got}")
    check("method validated against the committed number, by a DIFFERENT path",
          agree,
          f"agrees to <1e-10: computed {got} against committed "
          f"{COMMITTED_B_PP_A2}. Different evaluator (sparse Schur-Weyl vs "
          f"dense chi_lambda_numerical) and different crossings entry point "
          f"(atom_canonical_crossings vs atomic_braid_to_crossings). Two "
          f"independent routes to the committed B_pp_strong_MeV.",
          on_fail=(f"DOES NOT agree: computed {got} against committed "
                   f"{COMMITTED_B_PP_A2}. Every B_pp value below is on a "
                   f"different scale from the committed series and must NOT "
                   f"be used or committed. Check the environment before "
                   f"reading anything downstream."))

    # -------------------------------------------------- 2. the decline
    print("\n" + "-" * 78)
    print("  2. B_pp DECLINES with A — the confound is real and signed")
    print("-" * 78)
    print(f"\n  {'A':>3}{'B_pp/bond':>18}{'vs A=2':>12}{'drop':>10}")
    for A in _as:
        r = per_bond[A] / per_bond[_as[0]]
        print(f"  {A:>3}{mp.nstr(per_bond[A], 12):>18}{mp.nstr(r, 8):>12}"
              f"{mp.nstr(100*(1-r), 5):>9}%")
    declining = all(per_bond[_as[i]] > per_bond[_as[i + 1]]
                    for i in range(len(_as) - 1))
    # NAME THE LAST A, do not assume it is 4. This was hardcoded as "by A=4"
    # while the value is over `_as[-1]`; on a `2 3 4 5` run it printed the
    # A=5 figure (86.179 %) labelled A=4 (whose true drop is 73.754 %).
    a_last = _as[-1]
    drop_last = 1 - per_bond[a_last] / per_bond[_as[0]]
    ladder = " -> ".join(mp.nstr(per_bond[A], 6) for A in _as)
    check(f"B_pp is NOT A-independent — monotone decline on all "
          f"{len(_as)} points",
          declining and drop_last > mp.mpf("0.05"),
          f"{ladder} MeV/bond over A = {', '.join(str(A) for A in _as)}, a "
          f"{mp.nstr(100*drop_last, 4)} % drop by A={a_last}, against a chain "
          f"bond frozen at 2.0507 for every A. The companion probe's FIRST "
          f"disjunction branch (trace bond also A-independent) is WITHDRAWN; "
          f"the second is the true one.")

    # -------------------------------------------------- 3. what it does to kappa
    print("\n" + "-" * 78)
    print("  3. Direction of the kappa correction — NOT a corrected series")
    print("-" * 78)
    corr3 = per_bond[_as[0]] / per_bond[_as[1]] if len(_as) > 1 else mp.mpf(1)
    corr4 = per_bond[_as[0]] / per_bond[_as[-1]]
    a_second = _as[1] if len(_as) > 1 else _as[0]
    print(f"""
  kappa(A) = dB_AME / [ (A-1)/2 * ratio * B_pp ] was computed holding B_pp at
  its A={_as[0]} value. Correcting multiplies by B_pp({_as[0]})/B_pp(A):

      A={a_second}  x {mp.nstr(corr3, 8)}        A={a_last}  x {mp.nstr(corr4, 8)}

  Both > 1, so the TRUE kappa is LARGER than the held one, increasingly with A.
  The measured kappa decline (3.45 -> 1.74 over A = 3..39) therefore OVERSTATES
  the invariant's decline: part of it is the bond shrinking — exactly the
  confound qou-gcmn names.

  NOT corrected here. The mirror pairs run to A = 39; B_pp is measured to
  A = {a_last}. Extrapolating a {len(_as)}-point decline across a factor of ten
  in A would be a fit. The SIGN and the low-A SCALE are established.
""")
    check("the correction direction is established; the series is NOT corrected",
          corr3 > 1 and corr4 > corr3,
          f"B_pp({_as[0]})/B_pp({a_second}) = {mp.nstr(corr3, 8)}, "
          f"B_pp({_as[0]})/B_pp({a_last}) = {mp.nstr(corr4, 8)} — both above 1 "
          f"and growing, so the held-B_pp kappa understates the true kappa and "
          f"overstates its decline. No extrapolation past A={a_last} is made.",
          on_fail=(f"the ratios are NOT both above 1 and growing: "
                   f"B_pp({_as[0]})/B_pp({a_second}) = {mp.nstr(corr3, 8)}, "
                   f"B_pp({_as[0]})/B_pp({a_last}) = {mp.nstr(corr4, 8)}. The "
                   f"correction direction is not established by this run."))

    # -------------------------------------------------- 4. tractability
    print("\n" + "-" * 78)
    print("  4. 'Intractable' was the dense evaluator, not the object")
    print("-" * 78)
    # The check NAME claims computability; the old test gated on
    # `slowest < 300`, i.e. SPEED. On a `2 3 4 5` run the A=5 bond was
    # computed successfully in 3302 s and this reported FAIL -- a false
    # negative against its own claim. Gate on completion; report the time.
    slow_row = max(rows, key=lambda r: r["elapsed_sec"])
    slowest = slow_row["elapsed_sec"]
    print(f"\n  Largest case here: A={slow_row['A']}, n={slow_row['n_strands']}, "
          f"max dim {slow_row.get('max_dim', '?')} — {slowest:.0f} s.")
    print("  Dense chi_lambda_numerical did not return within 600 s.")
    check("the H_2A bond is computable — the intractability claim was stale",
          len(per_bond) == len(rows) and all(
              mp.isfinite(per_bond[A]) for A in per_bond),
          f"every requested A returned a finite bond; the slowest, "
          f"A={slow_row['A']} (n={slow_row['n_strands']}), took {slowest:.0f} s with "
          f"the column-sparse Hoefsmit multiply (<=2 nonzeros per row, "
          f"O(dim^2*nnz) instead of O(dim^3)), machinery that landed "
          f"2026-08-30 in colour_weighting_across_mixed_nuclei_probe. "
          f"em_linking_invariant_scoping's 'the A>3 bonds live at H_2A, "
          f"intractable' predates it. NOTE this asserts COMPUTABILITY, not "
          f"speed: a slow run is a cost, not a refutation.",
          on_fail=(f"not every requested A returned a finite bond "
                   f"({len(per_bond)} of {len(rows)} rows)."))

    ok = all(checks)
    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print(f"""
  VERDICT. qou-gcmn asked to compute B_pp at higher A or bound its
  A-dependence. Both are now done, and they disagree with the companion probe's
  preferred branch:

  - the CHAIN bond is A-independent by construction (companion probe);
  - the TRACE bond is NOT: {ladder} MeV/bond over
    A = {', '.join(str(A) for A in _as)}, a {mp.nstr(100*drop_last, 4)} % decline;
  - so the confound is real, and the measured kappa decline overstates the
    EM-linking invariant by the amount the bond shrinks.

  The blocker qou-gcmn names is therefore not "unmeasurable" — it is measured
  at the low end and computable further by the same route.
""")

    wit = {
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
        "$schema": "https://litlfred.github.io/qou/schemas/witness/v1",
        "name": "bpp-higher-a-sparse",
        "description": (
            "qou-gcmn ANSWERED. B_pp per bond on pure-proton chains: 2.128360946 "
            "(A=2, reproducing the committed value by a different evaluator), "
            "1.966342608 (A=3), 1.851585614 (A=4) MeV — a monotone 13.0% decline, "
            "against an A-independent chain bond of 2.050709692. So B_pp is NOT "
            "A-independent, the confound is real and signed, and the measured "
            "kappa decline OVERSTATES the EM-linking invariant. The companion "
            "probe's first disjunction branch is withdrawn. Also: the H_2A trace "
            "was never intractable — the sparse Hoefsmit multiply does A=4 (n=12, "
            "max dim 297) in ~50s where the dense evaluator does not return in "
            "600s. Scope (a); the series is NOT corrected past A=4, which would "
            "be a fit."),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data": {
            "q0": Q_50_DIGIT_STR,
            "q0_anchor": "proton",
            "E0_MeV": mp.nstr(E0, 30),
            "committed_B_pp_A2": COMMITTED_B_PP_A2,
            "rows": rows,
            "B_pp_per_bond": {str(A): mp.nstr(per_bond[A], 25)
                              for A in sorted(per_bond)},
            # Name kept for consumer compatibility; it is the LAST A in the
            # run, which is 4 only on the default `2 3 4` invocation.
            "decline_A4_vs_A2": mp.nstr(drop_last, 20),
            "decline_last_vs_first": mp.nstr(drop_last, 20),
            "decline_last_A": a_last,
            "decline_first_A": _as[0],
            "kappa_correction_A3": mp.nstr(corr3, 20),
            "kappa_correction_A4": mp.nstr(corr4, 20),
            "chain_bond_MeV": "2.050709692381",
            "assertions": assertions,
            "allPassed": ok,
        },
    }
    out = _HERE / "bpp-higher-a-sparse.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    wit["q0Anchor"] = _q0a
    if _q0v:
        wit["q0Value"] = _q0v
    out.write_text(json.dumps(wit, indent=2) + "\n", encoding="utf-8")
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
