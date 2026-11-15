#!/usr/bin/env python3
"""The pn bond factor is strictly BETWEEN the like-pair bond factors, so it can
never be the strict maximum of the three -- which is exactly the pattern bean
`qou-q8vl` shows a positive three-body Ursell coefficient requires.

WHERE THIS SITS
---------------
Bean `qou-q8vl` (PR #7226, on `main`) established two things about the
production `A = 3` chain:

  * a positive `b_3` needs EXACTLY ONE bond factor above 1 -- flipping both
    leaves `b_3` byte-identical, because the chain's Ursell function is a
    PRODUCT `g_01 * g_12`;
  * the sign-mixed assignment that also gives the correct two-nucleon spectrum
    -- unlike pairs bind, like pairs do not -- is the one with the pn bond
    opposite to both like-pair bonds.  Since `B = -alpha log mu > 0` iff
    `mu < 1`, that pattern is

        mu_pn > 1 > mu_pp   and   mu_pn > 1 > mu_nn,

    i.e. `mu_pn` is the STRICT MAXIMUM of the three.

That bean excludes the two derived families at the VALUE level (production
letters by `d <= 0`; isospin projectors by `mu_+ + mu_- = 1`) and records as
open: "a THIRD bond family that supplies the sign-mixed pattern by derivation".

THIS PROBE NARROWS THAT OPEN QUESTION, at the STRUCTURE level.
--------------------------------------------------------------
The pn letter is not an independent third value.  It is DEFINED as a colour
weighted average of the pp and nn letters
(`atom_braid_word_3A`; see `the_pn_bond_is_an_average_and_cannot_be_extremal_probe`):

    d_pn = (1/2 + delta/4) * d_pp + (1/2 - delta/4) * d_nn,

weights summing to 1 and BOTH STRICTLY POSITIVE for delta in (-2, 2).  The
two-strand interface law is affine, `mu = z + d`, and an affine map carries a
convex combination to the same convex combination.  A strict convex combination
lies strictly between its endpoints.  Therefore `mu_pn` is strictly between
`mu_pp` and `mu_nn` -- for EVERY q, EVERY delta in the admissible range, and
every pair of like-pair offsets, whatever their values.

CONSEQUENCE, and it is the point: a third bond family cannot rescue the pattern
merely by moving the letters above 1.  It must break the AVERAGING STRUCTURE
itself, or break affineness of the interface law.  Those are the only two
hypotheses used.

Scope (b) structural exclusion.  Invariant: strict convexity of the averaged
letter + affineness of the two-strand trace.  Both are identities, not
measurements -- see `QOU/MassTheory/PnBetweennessBlocksSignMixed.lean`
(sorry-free).

NOT CLAIMED: that no third family exists.  Only that any such family must break
one of the two named hypotheses.  The magnitude question (`qou-brng`) is
untouched, and nothing here is wired to production.
"""
from __future__ import annotations
import sys, pathlib

_HERE = pathlib.Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE.parent.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp
from qou_substrate import precision as _precision
from qou_substrate.witness import WitnessBuilder

mp.mp.dps = _precision.COMPUTE_DPS

_FAILURES: list[str] = []
_CHECKS: list[dict] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    _CHECKS.append({"name": name, "pass": bool(ok), "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        _FAILURES.append(name)


def q0_proton() -> mp.mpf:
    """The canonical experimental (proton) pin, convention D."""
    from qou_substrate import constants as _c
    return mp.mpf(_c.Q_50_DIGIT_STR)


def letters(q: mp.mpf, delta: mp.mpf) -> dict[str, mp.mpf]:
    """Convention-D two-strand bond factors mu = z + d for the three interfaces."""
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    d_pp = mp.mpf(0)
    d_nn = -h
    d_pn = -h * (1 - delta / 2) / 2
    return {
        "z": z, "h": h,
        "mu_pp": z + d_pp, "mu_pn": z + d_pn, "mu_nn": z + d_nn,
        "d_pp": d_pp, "d_pn": d_pn, "d_nn": d_nn,
    }


def main() -> int:
    q = q0_proton()
    print(f"proton pin q0 = {mp.nstr(q, 25)}   dps = {mp.mp.dps}   convention D")

    # --- 1. the averaging identity, exactly, over a sweep of delta -------------
    print("\n== 1. d_pn is a strict convex combination of d_pp and d_nn ==")
    worst_resid = mp.mpf(0)
    for ds in ("-1.9999", "-1", "-0.5", "0", "0.5", "1", "1.5", "1.9999"):
        delta = mp.mpf(ds)
        L = letters(q, delta)
        w1 = mp.mpf(1) / 2 + delta / 4
        w2 = mp.mpf(1) / 2 - delta / 4
        resid = abs(L["d_pn"] - (w1 * L["d_pp"] + w2 * L["d_nn"]))
        worst_resid = max(worst_resid, resid)
        wsum = abs(w1 + w2 - 1)
        if wsum > mp.mpf(10) ** (-60) or not (w1 > 0 and w2 > 0):
            check(f"weights_admissible_delta_{ds}", False, f"w1={mp.nstr(w1,8)} w2={mp.nstr(w2,8)}")
    check("convex_combination_exact_1e_60", worst_resid < mp.mpf(10) ** (-60),
          f"worst |d_pn - combo| = {mp.nstr(worst_resid, 8)}")

    # --- 2. affineness carries the combination to the bond factors ------------
    print("\n== 2. the affine interface law preserves the combination ==")
    worst_mu = mp.mpf(0)
    for ds in ("-1.9999", "-1", "0", "1", "1.9999"):
        delta = mp.mpf(ds)
        L = letters(q, delta)
        w1 = mp.mpf(1) / 2 + delta / 4
        w2 = mp.mpf(1) / 2 - delta / 4
        worst_mu = max(worst_mu, abs(L["mu_pn"] - (w1 * L["mu_pp"] + w2 * L["mu_nn"])))
    check("affine_preserves_combination_1e_60", worst_mu < mp.mpf(10) ** (-60),
          f"worst |mu_pn - combo(mu)| = {mp.nstr(worst_mu, 8)}")

    # --- 3. betweenness, hence never the strict maximum -----------------------
    print("\n== 3. mu_pn is strictly between mu_pp and mu_nn, so never the max ==")
    rows = []
    all_between = True
    never_max = True
    any_above_one = False
    for ds in ("-1.9999", "-1.5", "-1", "-0.5", "0", "0.5", "1", "1.5", "1.9999"):
        delta = mp.mpf(ds)
        L = letters(q, delta)
        lo, hi = min(L["mu_pp"], L["mu_nn"]), max(L["mu_pp"], L["mu_nn"])
        between = lo < L["mu_pn"] < hi
        is_max = L["mu_pn"] > L["mu_pp"] and L["mu_pn"] > L["mu_nn"]
        above = any(L[k] > 1 for k in ("mu_pp", "mu_pn", "mu_nn"))
        all_between = all_between and between
        never_max = never_max and (not is_max)
        any_above_one = any_above_one or above
        rows.append({
            "delta": ds,
            "mu_pp": mp.nstr(L["mu_pp"], 20), "mu_pn": mp.nstr(L["mu_pn"], 20),
            "mu_nn": mp.nstr(L["mu_nn"], 20),
            "pn_strictly_between": bool(between),
            "pn_is_strict_max": bool(is_max),
            "any_letter_above_one": bool(above),
        })
        print(f"  delta={ds:>8}  mu_pp={mp.nstr(L['mu_pp'],12)}  "
              f"mu_pn={mp.nstr(L['mu_pn'],12)}  mu_nn={mp.nstr(L['mu_nn'],12)}  "
              f"between={between}  pn_max={is_max}")
    check("pn_strictly_between_every_delta", all_between)
    check("pn_never_strict_max_every_delta", never_max)
    check("no_letter_exceeds_one_at_proton_pin", not any_above_one,
          "consistent with qou-q8vl's value-level d<=0 exclusion")

    # --- 4. the structural claim: betweenness is q-independent ----------------
    print("\n== 4. the exclusion does not depend on the pin ==")
    q_independent = True
    for qs in ("1.02", "1.1099785827513808", "1.5", "2.0", "5.0"):
        qq = mp.mpf(qs)
        for ds in ("-1.5", "0", "1.5"):
            L = letters(qq, mp.mpf(ds))
            lo, hi = min(L["mu_pp"], L["mu_nn"]), max(L["mu_pp"], L["mu_nn"])
            if not (lo < L["mu_pn"] < hi):
                q_independent = False
                print(f"  counterexample q={qs} delta={ds}")
    check("betweenness_holds_off_the_pin", q_independent,
          "5 values of q x 3 of delta")

    # --- 5. the sign-mixed pattern is therefore unreachable -------------------
    print("\n== 5. the qou-q8vl sign-mixed pattern ==")
    reachable = False
    for ds in ("-1.9999", "-1", "-0.5", "0", "0.5", "1", "1.9999"):
        L = letters(q, mp.mpf(ds))
        if L["mu_pn"] > 1 and L["mu_pp"] < 1 and L["mu_nn"] < 1:
            reachable = True
    check("sign_mixed_pattern_unreachable", not reachable,
          "mu_pn > 1 > mu_pp, mu_nn requires pn to be the strict max")

    # --- 6. a synthetic family that DOES break the averaging ------------------
    # Not a proposal -- a demonstration that the hypothesis is what binds.
    print("\n== 6. control: break the averaging and the pattern becomes reachable ==")
    L = letters(q, mp.mpf("1"))
    mu_pn_free = mp.mpf("1.25")          # pn set independently, not averaged
    control = mu_pn_free > 1 and L["mu_pp"] < 1 and L["mu_nn"] < 1
    check("pattern_reachable_once_pn_is_free", control,
          "so the averaging hypothesis, not the values, is what excludes it")

    print(f"\nassertions {len(_CHECKS) - len(_FAILURES)}/{len(_CHECKS)}")

    wb = WitnessBuilder("pn-betweenness-blocks-sign-mixed")
    wb.set_description(
        "The pn interface letter is a strict convex combination of the pp and nn "
        "letters and the two-strand interface law is affine, so the pn bond factor "
        "is strictly between the like-pair factors and can never be the strict "
        "maximum. The sign-mixed pattern qou-q8vl shows a positive b_3 requires "
        "(mu_pn > 1 > mu_pp, mu_nn) is therefore unreachable for any q and any "
        "admissible colour weight. Scope (b); invariant = strict convexity + "
        "affineness. A third bond family must break one of those two hypotheses."
    )
    # add_assertion compares computed vs expected (coerced through float), so a
    # boolean check is recorded as 1 vs 1; the human-readable detail rides in
    # `checks` inside the payload rather than being mistaken for `expected`.
    for c in _CHECKS:
        wb.add_assertion(c["name"], "1" if c["pass"] else "0", "1")
    wb.add_caveat(
        "NOT claimed: that no third bond family exists. Only that any such family "
        "must break the averaging of the pn letter or the affineness of tr_2. The "
        "binding magnitude (qou-brng) is untouched and nothing here is wired."
    )
    wb.save({
        "q0_proton": mp.nstr(q, 30),
        "convention": "D",
        "rows": rows,
        "worst_convex_residual": mp.nstr(worst_resid, 10),
        "worst_affine_residual": mp.nstr(worst_mu, 10),
        "scope": "b",
        "invariant": "strict convexity of the averaged pn letter + affineness of tr_2",
        "narrows": "qou-q8vl open item: a third bond family supplying the sign-mixed pattern",
        "checks": _CHECKS,
    })
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
