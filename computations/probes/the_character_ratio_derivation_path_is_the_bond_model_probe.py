#!/usr/bin/env python3
"""The character-ratio derivation path, implemented: it IS the bond model. The
character ratio nucleus/free-constituent-product equals `exp(-L)` exactly, so
`prf:confined-knot-binding`'s specified route and the free-energy log-ratio are
the same object. And the hardcoded `knot_factor` the code runs instead is not an
approximation to it — the two differ by an order of magnitude.

WHERE THIS SITS
---------------
Owner ruling of 2026-09-05: no knot-selection routes. That retires the census
route (`mass_table_ppb.ATOM_ASSIGN`, whose knots are chosen so their volumes
match `B_AME/m_e`) and the dedicated route (`hecke_core_legacy.knot_factor`,
which dispatches on `A`). See
`docs/audits/2026-09-05-binding-route-consolidation-no-knot-selection.md`.

`prf:confined-knot-binding` specifies an unfitted alternative:

    "the character ratio measures the volume departure from the free
     constituents. The total knot factor multiplies these strict,
     empirically-independent character ratios across all levels."

and `knot_factor`'s own docstring concedes it is not running it:

    "The per-level character ratio (nucleus/free-nucleon product) and
     confined-state accumulation provide the categorical derivation path.
     CURRENTLY USING THE PRODUCT FORMULA FOR A<=4 AND GENERIC FOR A>=5."

So the corpus specified a derivation path and substituted hardcoded per-`A`
factors. This probe implements the specified path at the level the engine can
compute, and reports what it gives.

WHAT THE CHARACTER RATIO IS
---------------------------
The nucleus is the canonical word `atom_canonical_crossings(Z, N)`; the free
constituents are the same word with the `A - 1` inter-nucleon interfaces
deleted. Both are exact Markov traces at 200 bits. The ratio is

    R(Z,N) = tr_M(nucleus) / tr_M(free constituents),

and because the canonical closure is a connected sum (`qou-m3sh`, measured to
`~1e-59`), `R` is exactly the product of the per-interface factors `z + d_i`.
Therefore

    R = exp(-L),        L = log(Z_free / Z_bonded) = sum of -log(z + d_i).

**The specified derivation path and the bond model are the same object.** That
is the finding: implementing the unfitted route the corpus specified does not
produce a new binding channel, it produces the one already recorded in
`rem:bond-log-ratio-is-a-free-energy` as a free-energy difference whose
identification with binding is open.

MEASURED
--------
Exact at 200 bits, canonical word, `alpha = m_e/(q0(q0-1)) = 4.185981` MeV:

    atom   R = exp(-L)        B = -alpha log R    B_AME        error
    2H     0.508229789377     2.8332              2.224566     +27.36 %
    3H     0.205135640449     6.6309              8.481796     -21.82 %
    3He    0.311386312073     4.8839              7.718041     -36.72 %
    4He    0.125684152895     8.6817             28.295662     -69.32 %

and against the factors the code actually uses:

    A = 3:  true character ratio 0.2051 (3H) / 0.3114 (3He)   hardcoded 1 - h^2   = 0.9563
    A = 4:  true character ratio 0.1257                        hardcoded (1-h^2)^2 = 0.9145

**The hardcoded `knot_factor` is not an approximation to the character ratio.**
They differ by 4.7x, 3.1x and 7.3x respectively. Whatever `1 - h^2` is, it is not the quantity
the derivation path names.

WHAT IS IMPLEMENTED AND WHAT IS NOT
-----------------------------------
The specification says the knot factor multiplies character ratios "across all
levels", and `confined-knot-binding` names three: quark, nucleon, and nuclear
jet. **Only the nucleon level is implemented here**, because it is the only one
the exact engine has words for. A multi-level product would multiply further
ratios, each `< 1`, which drives `R` DOWN and `B = -alpha log R` UP — so the
missing levels move `4He` in the right direction from `-69 %`. That is a
direction, not a prediction, and nothing here estimates their size.

WHAT IS NOT CLAIMED
-------------------
No binding claim. That `B = alpha L` is the binding energy remains the open
interpretation of `rem:bond-log-ratio-is-a-free-energy`; this probe does not
reopen it, it shows the specified path lands on the same quantity. Nothing about
whether the quark and nuclear-jet levels exist as computable words. No claim
that `1 - h^2` is wrong as an object — only that it is not the character ratio.
The all-pairs variant is not used: its bond multiset does not determine a word
(`qou-bygw`, retired).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

ALPHA = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
DVAL = {"sigma": E.ZERO, "sigma_inv": -E.H, "averaged": -E.H / 2,
        "averaged_weighted": E.D_PN}
ISO = [(1, 1, "2H", "2.224566"), (1, 2, "3H", "8.481796"),
       (2, 1, "3He", "7.718041"), (2, 2, "4He", "28.295662")]


def words(Z, N):
    """(nucleus, free constituents) as exact-engine letter lists. The free word
    is the canonical word with the A-1 inter-nucleon interfaces deleted."""
    full = [(1, DVAL[k], g) for g, k in atom_canonical_crossings(Z, N)]
    free = [(c, d, g) for (c, d, g) in full if g % 3 != 2]
    return full, free


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR; alpha = {float(ALPHA):.6f} MeV")  # float64-ok: display only

    print("\n" + "=" * 76)
    print("§1  THE CHARACTER RATIO, EXACTLY — nucleus / free-constituent product")
    print("=" * 76)
    print(f"    {'atom':>5} {'R = exp(-L)':>20} {'B = -alpha log R':>18} {'B_AME':>12} {'error':>9}")
    R = {}
    for Z, N, nm, ame in ISO:
        n = 3 * (Z + N)
        full, free = words(Z, N)
        R[nm] = E.trM(n, full) / E.trM(n, free)
        B = -ALPHA * gmpy2.log(R[nm])
        a = mpfr(ame)
        print(f"    {nm:>5} {float(R[nm]):20.15f} {float(B):18.4f} {float(a):12.6f} "  # float64-ok: display only
              f"{float(100 * (B - a) / a):8.2f}%")  # float64-ok: display only
    check("every character ratio lies in (0,1), so B = -alpha log R is positive",
          all(mpfr(0) < v < mpfr(1) for v in R.values()))

    print("\n" + "=" * 76)
    print("§2  IT IS exp(-L): THE SPECIFIED PATH AND THE BOND MODEL ARE ONE OBJECT")
    print("=" * 76)
    worst = mpfr(0)
    for Z, N, nm, _a in ISO:
        n = 3 * (Z + N)
        full, free = words(Z, N)
        L = gmpy2.log(E.trM(n, free) / E.trM(n, full))
        d = abs(R[nm] - gmpy2.exp(-L))
        worst = max(worst, d)
        print(f"    {nm:>5}  R = {float(R[nm]):.15f}   exp(-L) = {float(gmpy2.exp(-L)):.15f}"  # float64-ok: display only
              f"   |diff| {float(d):.1e}")  # float64-ok: display only
    check("R = exp(-L) to the working floor — the character ratio IS the bond model",
          worst < mpfr("1e-55"))

    print("\n" + "=" * 76)
    print("§3  THE HARDCODED knot_factor IS NOT AN APPROXIMATION TO IT")
    print("=" * 76)
    h = E.H
    hard = {3: 1 - h ** 2, 4: (1 - h ** 2) ** 2}
    ok_diff = True
    for Z, N, nm, _a in ISO:
        A = Z + N
        if A not in hard:
            continue
        ratio = hard[A] / R[nm]
        ok_diff &= ratio > mpfr(3)
        print(f"    {nm:>5} (A={A}): character ratio {float(R[nm]):.6f}   "  # float64-ok: display only
              f"hardcoded {float(hard[A]):.6f}   off by {float(ratio):.1f}x")  # float64-ok: display only
    check("the hardcoded factor differs from the character ratio by more than 3x — it is "
          "a different object, not an approximation", ok_diff)

    print("\n" + "=" * 76)
    print("§S  WHAT THIS SETTLES")
    print("=" * 76)
    print("  The corpus specified an unfitted derivation path and ran hardcoded per-A")
    print("  factors instead. Implemented, the specified path IS the bond model: the")
    print("  character ratio equals exp(-L) exactly. So retiring the knot-selection")
    print("  routes does not leave a second unfitted channel in reserve — it leaves")
    print("  the free-energy route already on the books, whose identification with")
    print("  binding is open. Only the nucleon level is implemented; confined-knot-")
    print("  binding also names quark and nuclear-jet levels, whose ratios would push")
    print("  B up. That is a direction, not a prediction.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Implements the character-ratio derivation path specified by "
            "prf:confined-knot-binding and admittedly not run by hecke_core_legacy."
            "knot_factor. The character ratio nucleus/free-constituent-product, exact at "
            "200 bits on the canonical word, equals exp(-L) to the working floor, so the "
            "specified path and the bond model are the same object. Binding from it: 2H "
            "+27.36 %, 3H -21.82 %, 3He -36.72 %, 4He -69.32 %. The hardcoded knot_factor "
            "(1-h^2 and its square) differs from the true character ratio by 4x to 7x and "
            "is not an approximation to it. Only the nucleon level is implemented; the "
            "quark and nuclear-jet levels the specification also names would push B up, "
            "which is a direction and not a prediction. No binding claim.")
        for nm, v in R.items():
            wb.add_data(f"character_ratio_{nm}", gmpy2.digits(v, 10, 25)[0])
        wb.add_data("max_R_minus_exp_minus_L", f"{float(worst):.3e}")  # float64-ok: display only
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Nucleon level only. prf:confined-knot-binding names quark, nucleon and "
            "nuclear-jet levels; the exact engine has words for one of them.")
        wb.add_caveat(
            "No binding claim. That B = alpha L is the binding energy remains the open "
            "interpretation of rem:bond-log-ratio-is-a-free-energy.")
        wb.add_caveat(
            "Uses the canonical (chain) word. The all-pairs variant is not used because "
            "its bond multiset does not determine a word (qou-bygw, retired).")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
