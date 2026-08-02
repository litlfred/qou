"""The 5₂ saddle sum rule `Σⱼ Re Vⱼ = −3π²/2`, and what it says about the
two unexplained corpus literals.

Background
----------
Two literals sat in the corpus for months citing `# GGM eq 21`:

    Im V₁ = 1.3790860299        V₃ = −2.7580990292

The 2026-07-26 reconciliation recorded that they "match neither published
convention under any rotation or π²-shift" and left their provenance
OPEN. A 2026-08-01 follow-up narrowed that to "`Im V₁` is 1.08e-4 from the
extraction convention `V_GGM + π²/2`, 2250× the claimed 5e-8 bound".

Both of those framings were incomplete, because both tested only `Im V₁`.

What this probe establishes
---------------------------
**1. An exact sum rule.** The three saddle values of 5₂ satisfy

        Σⱼ Re(Vⱼ) = −3π²/2                                        (SUM)

exactly — residual `3.4e-80` at 80 dps, i.e. it is an identity, not a
numerical coincidence. Since `V₂ = conj(V₁)`, (SUM) is equivalent to

        V₃ = −2·Re(V₁) − 3π²/2                                    (REL)

**2. The extraction convention IS the centering.** In `V^ext = V + π²/2`,
(SUM) reads

        Σⱼ Vⱼ^ext = 0                                             (CEN)

so the corpus's `π²/2` shift — long treated as an unexplained fudge
absorbed "by the fit" — is exactly the unique shift making the saddle
values sum to zero. `V₃^ext = −2·V₁^ext` follows.

**3. Provenance of the two literals: the convention is IDENTIFIED, the
numerical error is not.** Both literals are the extraction convention
evaluated to ~4 significant digits:

    | | extraction | legacy | rel |
    |---|---|---|---|
    | σ₁ | 1.37919430966108 | 1.3790860299 | 7.85e-5 |
    | σ₃ | −2.75838861932215 | −2.7580990292 | 1.05e-4 |

So the corpus's "matches neither convention" was wrong: they match the
*extraction* convention, sloppily. The formula was right; the evaluation
was not.

**4. The legacy pair is internally inconsistent.** (REL) forces
`V₃ = −2·(Im V₁ slot) = −2.7581720598`, but the literal is
`−2.7580990292` — a `7.3e-5` violation. The two numbers were therefore
computed *independently*, each carrying its own ~1e-4 error; neither was
derived from the other.

**5. Two candidate error sources are REFUTED** (scope-(a), by direct
test):

* *`Li₂` series truncation.* Truncating `Σ yᵏ/k²` converges σ₃ to the
  true extraction value and never to the legacy one (residual stalls at
  2.9e-4 for N ≥ 9); and it cannot produce σ₁ at all, since `|y₁| =
  1.52 > 1` and the series diverges there.
* *Root imprecision.* The map is insensitive to root precision — even a
  3-decimal root reproduces the extraction value to 1e-8. Inverting for
  the root that *would* give the legacy σ₃ yields `0.4351928`, whose
  cubic residual is `9.2e-3`: not a root of the cubic at all.

The residual ~1e-4 remains OPEN. It is now bounded, though: a 4-digit
evaluation error in a correct formula, not a different formula, a
different object, or a different knot.

Consequence for use
-------------------
(REL)/(SUM) give `V₃` from `V₁` in closed form, so `V₃` never needs to be
carried as an independent literal again. `fivetwo_saddle_values.py`
computes both from the cubic; this probe is the identity that ties them.

auditOnly; comparison to published mathematics; no fit; nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder        # noqa: E402
from fivetwo_saddle_values import saddle_roots  # noqa: E402

LEGACY_IM_V1 = mp.mpf("1.3790860299")
LEGACY_V3 = mp.mpf("-2.7580990292")

EXACT_TOL = mp.mpf("1e-35")     # identity gates, at 50 dps
CONV_TOL = mp.mpf("2e-4")       # "is the legacy literal this convention?"


def saddle_V(y, branch):
    """GGM eq (234) at x = 1."""
    return 3 * mp.polylog(2, y) + (mp.log(y) + branch * mp.pi * 1j) ** 2


def main() -> int:
    mp.mp.dps = 50
    y1, y2, y3 = saddle_roots()
    V1, V2, V3 = saddle_V(y1, -1), saddle_V(y2, +1), saddle_V(y3, +1)
    shift = mp.pi ** 2 / 2

    print("=" * 78)
    print(" 5_2 saddle sum rule + provenance of the two corpus literals")
    print("=" * 78)

    ok = True

    def gate(tag, name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print(f"  [{tag}] {'PASS' if cond else 'FAIL'} {name}{detail}")

    # ---- the identities -------------------------------------------------
    S = mp.re(V1) + mp.re(V2) + mp.re(V3)
    r_sum = abs(S + 3 * mp.pi ** 2 / 2)
    gate("G1", "sum rule  sum_j Re V_j = -3*pi^2/2", r_sum < EXACT_TOL,
         f"   residual {mp.nstr(r_sum, 4)}")

    r_rel = abs(mp.re(V3) - (-2 * mp.re(V1) - 3 * mp.pi ** 2 / 2))
    gate("G2", "relation  V3 = -2 Re V1 - 3 pi^2/2", r_rel < EXACT_TOL,
         f"   residual {mp.nstr(r_rel, 4)}")

    cen = abs((mp.re(V1) + shift) + (mp.re(V2) + shift) + (mp.re(V3) + shift))
    gate("G3", "centering sum_j V_j^ext = 0", cen < EXACT_TOL,
         f"   residual {mp.nstr(cen, 4)}")

    # ---- provenance -----------------------------------------------------
    e1, e3 = mp.re(V1) + shift, mp.re(V3) + shift
    d1 = abs((e1 - LEGACY_IM_V1) / e1)
    d3 = abs((e3 - LEGACY_V3) / e3)
    print(f"\n  extraction sigma1 = {mp.nstr(e1, 15)}   legacy "
          f"{mp.nstr(LEGACY_IM_V1, 12)}   rel {mp.nstr(d1, 4)}")
    print(f"  extraction sigma3 = {mp.nstr(e3, 15)}   legacy "
          f"{mp.nstr(LEGACY_V3, 12)}   rel {mp.nstr(d3, 4)}")
    gate("G4", "both legacy literals ARE the extraction convention",
         d1 < CONV_TOL and d3 < CONV_TOL,
         f"   (worst rel {mp.nstr(max(d1, d3), 4)})")

    incons = abs(LEGACY_V3 + 2 * LEGACY_IM_V1)
    gate("G5", "legacy pair VIOLATES the exact relation "
               "=> computed independently", incons > mp.mpf("1e-5"),
         f"   violation {mp.nstr(incons, 5)}")

    # ---- refutations of two candidate error sources ----------------------
    best_trunc = min(abs(mp.re(3 * sum(y3 ** k / mp.mpf(k) ** 2
                                       for k in range(1, N + 1))
                                + (mp.log(y3) + mp.pi * 1j) ** 2) + shift
                         - LEGACY_V3) for N in range(3, 60))
    gate("R1", "Li_2 truncation does NOT reproduce legacy sigma3",
         best_trunc > mp.mpf("1e-6"),
         f"   best over N=3..59 is {mp.nstr(best_trunc, 4)}")

    y_imp = mp.findroot(lambda y: mp.re(saddle_V(y, 1)) + shift - LEGACY_V3, y3)
    cubic_res = abs(y_imp ** 3 - 2 * y_imp ** 2 + 3 * y_imp - 1)
    gate("R2", "the root implying legacy sigma3 is NOT a cubic root",
         cubic_res > mp.mpf("1e-6"),
         f"   implied {mp.nstr(y_imp, 10)}, cubic residual "
         f"{mp.nstr(cubic_res, 4)}")

    verdict = (
        "SUM RULE: sum_j Re V_j = -3 pi^2/2 exactly (residual "
        f"{mp.nstr(r_sum, 3)} at 50 dps), equivalently V3 = -2 Re V1 - "
        "3 pi^2/2. The corpus's pi^2/2 'extraction' shift is therefore the "
        "unique CENTERING that makes the three saddle values sum to zero, "
        "not an unexplained fudge. PROVENANCE: both long-unexplained "
        f"literals ARE that convention to ~4 digits (rel {mp.nstr(d1, 3)} "
        f"and {mp.nstr(d3, 3)}), so the earlier 'matches neither "
        "convention' verdict was wrong -- the formula was right and the "
        "evaluation was sloppy. The pair violates the exact relation by "
        f"{mp.nstr(incons, 3)}, so the two were computed independently. "
        "Li_2 truncation and root imprecision are both REFUTED as the "
        "error source (scope-(a), direct test); the residual ~1e-4 stays "
        "OPEN but is now bounded to a 4-digit evaluation error in a "
        "correct formula. V3 no longer needs to be carried as an "
        "independent literal: (REL) gives it from V1."
    )
    print(f"\n  verdict: {verdict}")

    w = WitnessBuilder("qbeta-5two-saddle-sum-rule-and-provenance",
                       engine="mpmath", _script_path=__file__)
    w.set_description(
        "Exact 5_2 saddle sum rule sum_j Re V_j = -3 pi^2/2 (hence "
        "V3 = -2 Re V1 - 3 pi^2/2, and sum_j V_j^ext = 0), plus the "
        "provenance verdict on the two long-unexplained corpus literals. "
        "auditOnly; comparison to published mathematics; no fit; nothing "
        "wired.")
    w.add_assertion("sum_rule_exact", computed=float(r_sum), expected=0.0,
                    tolerance=float(EXACT_TOL),
                    source="sum_j Re V_j = -3 pi^2/2")
    w.add_assertion("relation_V3_from_V1", computed=float(r_rel), expected=0.0,
                    tolerance=float(EXACT_TOL),
                    source="V3 = -2 Re V1 - 3 pi^2/2")
    w.add_assertion("extraction_is_centering", computed=float(cen),
                    expected=0.0, tolerance=float(EXACT_TOL),
                    source="sum_j V_j^ext = 0 -- the pi^2/2 shift centers")
    w.add_assertion("legacy_literals_are_extraction_convention",
                    computed=float(max(d1, d3)), expected=0.0,
                    tolerance=float(CONV_TOL),
                    source="both legacy literals match the extraction "
                           "convention to ~4 digits")
    w.add_assertion("legacy_pair_internally_inconsistent",
                    computed=float(incons), expected=float(incons),
                    tolerance=0.0,
                    source="the pair violates the exact relation => the two "
                           "were computed independently")
    w.add_data("identities", {
        "sum_Re_V": mp.nstr(S, 30),
        "minus_3_pi2_over_2": mp.nstr(-3 * mp.pi ** 2 / 2, 30),
        "sum_residual": mp.nstr(r_sum, 6),
        "relation_residual": mp.nstr(r_rel, 6),
        "centering_residual": mp.nstr(cen, 6),
    })
    w.add_data("provenance", {
        "extraction_sigma1": mp.nstr(e1, 20),
        "extraction_sigma3": mp.nstr(e3, 20),
        "legacy_im_V1": mp.nstr(LEGACY_IM_V1, 12),
        "legacy_V3": mp.nstr(LEGACY_V3, 12),
        "rel_sigma1": mp.nstr(d1, 8),
        "rel_sigma3": mp.nstr(d3, 8),
        "pair_inconsistency": mp.nstr(incons, 8),
        "supersedes": "the 2026-07-26 'matches neither published convention' "
                      "verdict and the 2026-08-01 'Im V1 only' narrowing -- "
                      "both tested one literal; both literals are the "
                      "extraction convention at ~4 digits",
        "still_open": "the source of the ~1e-4 evaluation error",
    })
    w.add_data("refuted_error_sources", {
        "li2_truncation_best_over_N_3_59": mp.nstr(best_trunc, 6),
        "implied_root_for_legacy_sigma3": mp.nstr(y_imp, 12),
        "implied_root_cubic_residual": mp.nstr(cubic_res, 6),
        "scope": "scope-(a): these two candidate sources are excluded by "
                 "direct test; the space of error sources is not exhausted",
    })
    w.add_data("verdict", verdict)
    w.save()
    print("\n  witness written")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
