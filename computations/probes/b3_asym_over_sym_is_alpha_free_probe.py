#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form evaluation at the substrate q0; every
# quantity is mpmath mpf end to end, no float64 anywhere.
"""b3_asym/b3_sym is an ALPHA-FREE prediction of the chain assembly -- derived, and it MISSES.

Bean `qou-o6ml` (the two-like-charge EM-linking arc). Owner instruction
2026-09-14: "Merge then try derivation" -- option (a), derive whether a
tr_M-LEVEL quantity can carry a charge-antisymmetric part at all.

## Why this is the right object to derive

`qou-9v7t` splits the measured A=3 three-body cumulant by isospin and names the
halves: `b3_sym = 1.4262225` MeV "the strong channel's obligation" against
`b3_asym = 0.3818775` MeV "the EM channel's".  The arc owes the asym half.

Every previous route on this arc needed a LINK (Milnor invariants) or an
EMBEDDING (Mobius energy), and the canonical object is neither -- it is an
element of `H_{3A}(q)`, so those routes ask for something the object does not
have (bean `qou-o6ml`, section 10/11 of PR #7339).  `tr_M` is a LINEAR FUNCTIONAL
on the algebra, so it evaluates on the element directly.  That is the whole
reason to try this direction and not another.

## The derivation, and it is parameter-free

The chain assembly lays `A-1` bonds in a line (`assembly_shortfall_shape_probe`
section 10a, line 30):

    B(Z,N) = -alpha * [ (Z-1) ln f_pp + ln f_pn + (N-1) ln f_nn ]

With `b3(X) = B(X) - 3*e2` and `e2 = B(2H) = -alpha ln f_pn`:

    b3(3H)  = -alpha [ ln f_nn - 2 ln f_pn ]
    b3(3He) = -alpha [ ln f_pp - 2 ln f_pn ]

so

    b3_sym  = alpha [ 2 ln f_pn - (ln f_nn + ln f_pp)/2 ]
    b3_asym = alpha [ (ln f_pp - ln f_nn) / 2 ]

**`alpha` cancels in the RATIO.**  `b3_asym / b3_sym` is therefore a derived,
parameter-free prediction -- no CAL-4, no tuned constant, nothing selected
against the target.  `alpha` is the one free object in `B = -alpha log mu`
(`alpha_direction_two_sided_squeeze_probe`), and the ratio is exactly the
combination that does not see it.

## PRIOR ART 1 -- `qou-1pig` ALREADY HOLDS THE NUMERATOR, and says more about it

Found by corpus-grep, and it is the closer of the two.  Bean `qou-1pig` (status
`todo`) measures

    B(3H) - B(3He) = alpha * ln(f_pp/f_nn) = 1.74707324276 MeV

which is EXACTLY twice the `b3_asym` derived below -- the same quantity, in the
`(3H - 3He)` convention rather than the `(3H - 3He)/2` one.  It is not new here.
It also carries the better diagnosis, which is not re-derived and should be read
first: `f_pn` is the arithmetic mean of `f_pp` and `f_nn` to 1.4e-4, so the bond
factor is a LINEAR RAMP in neutron count, hence **odd in T_z**, where charge
symmetry demands the strong part be even.  And the ordering is backwards --
`B_nn > B_pn > B_pp` puts the unbound dineutron as the most bound pair.

## What this adds over it: ONE number, and it is that the residual is alpha-free

`qou-1pig` compares the model's antisymmetric part to the observed one and gets
`2.287479x`.  That figure is LINEAR IN alpha: an alpha 2.287x smaller removes it
entirely.  The same is true of the symmetric comparison, `1.922620x`.  Neither
is a parameter-free statement on its own.

Their QUOTIENT is, and it is the ratio derived here:

    (model asym / observed asym) / (model sym / observed sym)
      = 2.287479 / 1.922620
      = 1.189772          <- alpha cancels; verified identical to the ratio below

So the alpha-free content of the A=3 mirror failure is: **the chain assembly
overshoots the antisymmetric part by 19.0% MORE than it overshoots the symmetric
part.**  No choice of alpha touches that 19.0%.

## What the SIGN is NOT

The ratio comes out NEGATIVE (-0.3186) against the AME `+0.2678`, and it would
be wrong to report that as a second, independent failure.  It is not:

  * the numerator is POSITIVE and has the right sign -- `qou-1pig` establishes
    that directly;
  * the denominator is negative because `b3_sym` is negative, which is the
    corpus's OWN standing result (`QOU.MassTheory.B3SignOneRoot.b3corpus_chain_neg`,
    sorry-free: the Ursell alternation forces `b3 < 0` for every bond triple);
  * so the sign of the ratio is that known problem appearing in the denominator,
    and repairing it repairs the sign of the ratio too.

Grant the sign repair, and 19.0% is what is left.  That residual is the finding.
An earlier draft of this file claimed the sign disagreement "survives an overall
sign flip" -- true for flipping BOTH parts, and irrelevant, because the repair
the corpus actually indicates is to the symmetric part alone.

## PRIOR ART 2 -- this does not discover the split, it adds one column

`b3_charge_decomposition_a3_probe.py` (witness
`computations/b3-charge-decomposition-a3.witness.json`) already owns this
ground, and the corpus-grep found it before any claim was written here:

  * it DEFINES the mirror split used above, and derives the same
    `b3_sym = 1.42622016`, `b3_asym = 0.38187744` MeV from AME2020;
  * it already identifies `b3(3H) - b3(3He)` as the Coulomb displacement
    energy, up to the Nolen-Schiffer residual [nolen1969];
  * it already tabulates TEN candidate 3-body objects and already carries an
    `asym_sign_matches_coulomb` column;
  * and it already concludes -- this is the part not to re-derive -- that
    "the per-bond factors carry no EM term, so the A=3 charge asymmetry is a
    missing CHANNEL, not a wrong 3-body operator."

Two things it does NOT have, which is the whole of what this file adds:

  1. **The chain assembly is not among its ten candidates.**  Its rows are
     product models (`product_*`), joint traces (`joint_trace_*`) and chirality
     weightings (`chiral_*`).  The production assembly is log-additive
     (`B = -alpha log mu`), which is a different object and is the one the mass
     arc actually uses.
  2. **It reports no INTERNAL `asym/sym` ratio.**  Its columns are `sym_MeV`,
     `asym_MeV`, `b3_sym_over_sym` and `asym_over_b3_asym` -- each carries the
     candidate's own overall scale, so each is a scale-dependent comparison.
     The internal ratio is the one combination that is not, and it is the
     alpha-free discriminant derived above.  This probe computes it for all ten
     of its candidates as well, from the committed witness, so the chain
     assembly is ranked against them rather than reported alone.

## What is ASSERTED vs what is merely REPORTED

Asserted (each can genuinely fail):

  * the alpha-cancellation itself, checked by recomputing at 7*alpha;
  * `f_pp != f_nn`, without which the whole asym channel is identically zero;
  * the SIGN of the derived `b3_asym`.

**The accuracy is REPORTED, never asserted.**  An assertion with a tolerance
sized to its own miss is a fit (AGENTS.md).  The number is printed and recorded
whatever it is.

## What this does NOT establish

That the predicted asymmetry is ELECTROMAGNETIC.  `f_pp = interface_factor
("positive")` and `f_nn = interface_factor("negative")` differ by the Hecke
deformation parameter `h = q - 1/q`, not by any electromagnetic coupling --
AGENTS.md records the three factors as charge-LABELLED but not charge-COUPLED.
So a nonzero answer here is an ISOSPIN-LABELLING asymmetry that lands in the
same observable slot as the EM one, which is a different claim and a weaker one.
"""

from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, interface_factor, markov_z  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

# AME2020 isospin split of the A=3 three-body cumulant -- DERIVED here, not
# transcribed.  `b3(X) = B(X) - 3*B(2H)`; the mirror split is `(3H +- 3He)/2`.
# This is exactly the definition in `b3_charge_decomposition_a3_probe.py`, and
# reusing it is what makes the two probes commensurable.
#
# An earlier version of this file hardcoded `mpf("1.4262225")` / `mpf("0.3818775")`
# -- the 8-figure roundings bean `qou-9v7t` quotes.  They are correct to those
# figures, and they are still the wrong thing to write: a transcribed constant
# cannot follow AME when it moves, and the rounding had already propagated into
# the reported ratio (0.26775450 against the derived 0.26775451).
# Module scope runs before main()'s set_compute_dps(); without this the
# subtraction below executes at mpmath's default 15 dps and `str()` later
# prints that 53-bit result padded to 70 digits (float64-padding gate).
set_compute_dps()
_B3_EMPIRICAL = {
    "T": AME_B_TRITIUM_MEV_VALIDATION - 3 * AME_B_DEUTERON_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION - 3 * AME_B_DEUTERON_MEV_VALIDATION,
}
B3_SYM_MEV = (_B3_EMPIRICAL["T"] + _B3_EMPIRICAL["3He"]) / 2
B3_ASYM_MEV = (_B3_EMPIRICAL["T"] - _B3_EMPIRICAL["3He"]) / 2

# The ten 3-body candidates already tabulated by the corpus, with their INTERNAL
# asym/sym ratio -- the alpha-free discriminant -- read off the committed witness.
PRIOR_WITNESS = _COMP / "b3-charge-decomposition-a3.witness.json"

_CHECKS: list[dict] = []


def check(name: str, ok: bool, detail: str) -> bool:
    _CHECKS.append({"name": name, "passed": bool(ok), "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    return bool(ok)


def b3_parts(f_pp, f_pn, f_nn, alpha):
    """(b3_sym, b3_asym) for the chain assembly at a given alpha."""
    lpp, lpn, lnn = mp.log(f_pp), mp.log(f_pn), mp.log(f_nn)
    b3_3H = -alpha * (lnn - 2 * lpn)
    b3_3He = -alpha * (lpp - 2 * lpn)
    return (b3_3H + b3_3He) / 2, (b3_3H - b3_3He) / 2


def main() -> int:
    set_compute_dps()
    q = Q_MP
    h = hecke_h(q)
    z = markov_z(q)
    d = flavor_split_leading(q)

    from qou_substrate.constants import M_E_MEV as _ME

    alpha = mpf(str(_ME)) / (q * (q - 1))

    f_pp = interface_factor("positive", q)
    f_pn = z - h * (mpf(1) / 2 - d / 4)
    f_nn = interface_factor("negative", q)

    print("SUBSTRATE (proton pin)")
    print(f"  q     = {mp.nstr(q, 20)}")
    print(f"  h     = {mp.nstr(h, 20)}")
    print(f"  z     = {mp.nstr(z, 20)}")
    print(f"  delta = {mp.nstr(d, 20)}")
    print("BOND FACTORS")
    print(f"  f_pp  = {mp.nstr(f_pp, 25)}")
    print(f"  f_pn  = {mp.nstr(f_pn, 25)}")
    print(f"  f_nn  = {mp.nstr(f_nn, 25)}")
    print(f"  alpha = {mp.nstr(alpha, 20)}  MeV   (the one free object; cancels below)")
    print()

    sym, asym = b3_parts(f_pp, f_pn, f_nn, alpha)
    ratio = asym / sym

    # -- 1. the structural claim: alpha cancels in the ratio ------------------
    sym7, asym7 = b3_parts(f_pp, f_pn, f_nn, 7 * alpha)
    ratio7 = asym7 / sym7
    drift = abs(ratio7 - ratio)
    check(
        "ALPHA_CANCELS_in_the_ratio",
        drift < mpf("1e-40"),
        f"ratio(alpha) = {mp.nstr(ratio, 20)}; ratio(7*alpha) = {mp.nstr(ratio7, 20)}; "
        f"|drift| = {mp.nstr(drift, 6)} < 1e-40.  The individual parts DO move: "
        f"b3_sym {mp.nstr(sym, 10)} -> {mp.nstr(sym7, 10)}.",
    )

    # -- 2. the channel is not identically zero -------------------------------
    gap = abs(f_pp - f_nn)
    check(
        "CHANNEL_NONVACUOUS_f_pp_ne_f_nn",
        gap > mpf("1e-30"),
        f"|f_pp - f_nn| = {mp.nstr(gap, 20)} = h = {mp.nstr(h, 20)}.  If these were "
        f"equal the derived b3_asym would be 0 identically and nothing below "
        f"would mean anything.",
    )

    # -- 3. sign --------------------------------------------------------------
    check(
        "SIGN_derived_b3_asym_is_POSITIVE_like_AME",
        asym > 0,
        f"derived b3_asym = {mp.nstr(asym, 12)} MeV; AME b3_asym = "
        f"{mp.nstr(B3_ASYM_MEV, 12)} MeV.  Both positive."
        if asym > 0
        else f"derived b3_asym = {mp.nstr(asym, 12)} MeV is NEGATIVE against AME "
        f"{mp.nstr(B3_ASYM_MEV, 12)} MeV -- wrong sign.",
    )

    # -- REPORTED, not asserted ----------------------------------------------
    ratio_ame = B3_ASYM_MEV / B3_SYM_MEV
    print()
    print("THE PARAMETER-FREE PREDICTION (reported, NOT asserted)")
    print(f"  derived  b3_asym / b3_sym = {mp.nstr(ratio, 20)}")
    print(f"  AME      b3_asym / b3_sym = {mp.nstr(ratio_ame, 20)}"
          f"   ( {mp.nstr(B3_ASYM_MEV,8)} / {mp.nstr(B3_SYM_MEV,8)} )")
    rel = (ratio - ratio_ame) / ratio_ame
    print(f"  relative miss             = {mp.nstr(rel * 100, 8)} %")
    print(f"  factor                    = {mp.nstr(ratio / ratio_ame, 8)}x")
    print()
    print("ABSOLUTE PARTS AT THE LIVE alpha (alpha is NOT derived -- context only)")
    print(f"  derived b3_sym  = {mp.nstr(sym, 12)} MeV   vs AME {mp.nstr(B3_SYM_MEV, 8)}"
          f"   ({mp.nstr((sym - B3_SYM_MEV) / B3_SYM_MEV * 100, 6)} %)")
    print(f"  derived b3_asym = {mp.nstr(asym, 12)} MeV   vs AME {mp.nstr(B3_ASYM_MEV, 8)}"
          f"   ({mp.nstr((asym - B3_ASYM_MEV) / B3_ASYM_MEV * 100, 6)} %)")

    # -- the identity that makes this alpha-free, stated as an identity -------
    over_asym = asym / B3_ASYM_MEV
    over_sym = sym / B3_SYM_MEV
    print()
    print("WHY THIS IS THE alpha-FREE PART OF qou-1pig'S MEASUREMENT")
    print(f"  model asym / observed asym  = {mp.nstr(over_asym, 10)}"
          f"   (qou-1pig reports 2.287479 on 2x this quantity)")
    print(f"  model sym  / observed sym   = {mp.nstr(over_sym, 10)}")
    print(f"  quotient                    = {mp.nstr(over_asym / over_sym, 10)}"
          f"   <- alpha cancels")
    print(f"  ratio / ratio_ame           = {mp.nstr(ratio / ratio_ame, 10)}"
          f"   <- same number, by construction")
    print("  Each overshoot alone is LINEAR in alpha and could be removed by")
    print("  rescaling it. The quotient cannot: 19.0% is what no alpha touches.")

    # -- the same discriminant, applied to the corpus's ten candidates --------
    prior_rows: list[dict] = []
    if PRIOR_WITNESS.exists():
        prior = json.loads(PRIOR_WITNESS.read_text())
        print()
        print("THE SAME alpha-FREE DISCRIMINANT ON THE CORPUS'S TEN CANDIDATES")
        print("  (computed here from b3-charge-decomposition-a3.witness.json, which")
        print("   reports sym and asym separately but never their internal ratio)")
        print(f"  {'candidate':<34} {'asym/sym':>14}   sign")
        for r in prior["data"]["rows"]:
            r_sym, r_asym = mpf(r["sym_MeV"]), mpf(r["asym_MeV"])
            if r_sym == 0:
                continue
            rr = r_asym / r_sym
            prior_rows.append({"candidate": r["candidate"],
                               "ratio_asym_over_sym": mp.nstr(rr, 20)})
            print(f"  {r['candidate']:<34} {mp.nstr(rr, 10):>14}   "
                  f"{'+' if rr > 0 else '-'}")
        print(f"  {'>> CHAIN ASSEMBLY (this probe)':<34} {mp.nstr(ratio, 10):>14}   "
              f"{'+' if ratio > 0 else '-'}")
        print(f"  {'-- AME2020 (the target)':<34} {mp.nstr(ratio_ame, 10):>14}   +")
        pos = [mpf(x["ratio_asym_over_sym"]) for x in prior_rows]
        print()
        print(f"  No prior candidate reaches the AME ratio in MAGNITUDE: the ten span "
              f"[{mp.nstr(min(pos), 6)}, {mp.nstr(max(pos), 6)}] against "
              f"{mp.nstr(ratio_ame, 6)}.")
        print(f"  The chain assembly is the first candidate whose |asym/sym| EXCEEDS it "
              f"({mp.nstr(abs(ratio), 6)} vs {mp.nstr(ratio_ame, 6)}) -- and its sign is wrong.")

    payload = {
        "description": (
            "b3_asym/b3_sym is an alpha-free prediction of the chain assembly. "
            "Derived from B = -alpha[(Z-1)ln f_pp + ln f_pn + (N-1)ln f_nn]; alpha "
            "cancels in the ratio. Accuracy is REPORTED, not asserted. A nonzero "
            "result is an ISOSPIN-LABELLING asymmetry (f_pp and f_nn differ by the "
            "Hecke h, not by an EM coupling), not an electromagnetic one."
        ),
        "bean": "qou-o6ml",
        "q0Anchor": "proton",
        "q0AnchorReason": "Physical-Observations layer (manifest key physical_proton): q0 = Q_50_DIGIT_STR, the proton m_p/m_e pin",
        "q0Value": mp.nstr(q, 30),
        "bond_factors": {
            "f_pp": mp.nstr(f_pp, 30),
            "f_pn": mp.nstr(f_pn, 30),
            "f_nn": mp.nstr(f_nn, 30),
            "h": mp.nstr(h, 30),
        },
        "derived": {
            "ratio_asym_over_sym": mp.nstr(ratio, 30),
            "b3_sym_MeV_at_live_alpha": mp.nstr(sym, 30),
            "b3_asym_MeV_at_live_alpha": mp.nstr(asym, 30),
        },
        "ame": {
            "b3_sym_MeV": str(B3_SYM_MEV),
            "b3_asym_MeV": str(B3_ASYM_MEV),
            "ratio_asym_over_sym": mp.nstr(ratio_ame, 30),
        },
        "relative_miss_on_ratio_pct": mp.nstr(rel * 100, 20),
        "prior_candidates_same_discriminant": prior_rows,
        "alpha_free_identity": {
            "model_asym_over_observed_asym": mp.nstr(over_asym, 20),
            "model_sym_over_observed_sym": mp.nstr(over_sym, 20),
            "quotient": mp.nstr(over_asym / over_sym, 20),
            "note": (
                "qou-1pig reports the antisym overshoot as 2.287479x on the "
                "(3H - 3He) convention; it is linear in alpha. The quotient of "
                "the two overshoots is not, and is the content of this probe."
            ),
        },
        "sources": [
            {
                "witness": "b3-charge-decomposition-a3.witness.json",
                "why": (
                    "defines the mirror split and the AME target; its ten candidates "
                    "are re-ranked here on the internal asym/sym ratio, which it does "
                    "not itself report"
                ),
            }
        ],
        "scope": (
            "(a) scope-limited. The chain assembly with the live per-bond factors, "
            "at the proton pin. Does NOT establish that the predicted asymmetry is "
            "electromagnetic."
        ),
        "assertions": _CHECKS,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    out = _HERE / "b3-asym-over-sym-is-alpha-free.witness.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out}")

    npass = sum(1 for c in _CHECKS if c["passed"])
    print(f"\n{npass}/{len(_CHECKS)} assertions passed")
    return 0 if npass == len(_CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
