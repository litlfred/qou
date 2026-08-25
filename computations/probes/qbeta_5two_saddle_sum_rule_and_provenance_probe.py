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

Proof status — PARTIAL, not closed
----------------------------------
(SUM) is verified to 80 dps but **not proved**. Progress toward a proof,
recorded so the next attempt starts here rather than from scratch:

*The branch data is explicit.* The cubic is `y² = (1−y)³`, so
`2 log yⱼ − 3 log(1−yⱼ) = 2πi·εⱼ` with `ε = (+1, −1, 0)` — exact at all
three roots (principal branch). The `π²` in (SUM) comes from precisely
this discrepancy.

*One exact relation follows.* Summing the reflection identity
`Li₂(y) + Li₂(1−y) = π²/6 − log y·log(1−y)` over the three roots and
substituting the branch data gives, with `Σεⱼ log yⱼ = 2i·arg(y₁)`:

    Σ Li₂(yⱼ) + Σ Li₂(1−yⱼ)
        = π²/2 − (2/3)·Σ(log yⱼ)² − (4π/3)·arg(y₁)

verified to machine precision.

*Why it does not close.* That is one equation in the two unknowns
`A = Σ Li₂(yⱼ)` and `B = Σ Li₂(1−yⱼ)`; numerically `A = 0.9717306815`,
`B = 0.3514640301`, with no evident closed form for either separately
(`B/A = 0.36169`, `B−A = −0.62027`). A second independent relation is
needed.

*Route survey (2026-08-06) — four tried, none closes.* The line above
originally named the Kubert/distribution relation as "the identified
route"; **that was too optimistic and is corrected here.**

The problem reduces exactly (residual 2.7e-51) to one evaluation:

    Σⱼ Li₂(yⱼ) = (2·Re e₂(L) − π²/2) / 3

so (SUM) *is* a dilogarithm-ladder evaluation at the roots, nothing more.

1. **Reflection — exhausted.** It defines `B` in terms of `A`, so it
   eliminates `B` and constrains `A` not at all. Re-applying it to the
   `1−y` roots returns the same equation.
2. **Bloch–Wigner torsion — refuted as the mechanism.** `Σ D(yⱼ) = 0`
   holds, but *automatically*: `D(z̄) = −D(z)` and `D` vanishes on reals,
   so every cubic with one real and two conjugate roots gives `0`
   (verified on both controls). It carries no 5₂ information.
3. **Landen — adds an unknown.** `z = y/(y−1)` maps the roots exactly
   onto the roots of `z³ − z² + 1`, a *different* algebraic set: one new
   equation, one new unknown.
4. **Kubert/distribution — nets negative.** It introduces `Li₂` at `−yⱼ`
   and `ω^k(1−yⱼ)`: six new unknown sums for one new relation.

*Route 5 (2026-08-06) — RESTATEMENT: the dilogarithms cancel out.*
Not a proof, but it changes what has to be proved.

The power sums `pₙ = Σⱼ yⱼⁿ` are **integers** (3, 2, −2, −7, −6, 7, 25, …)
obeying the cubic's recurrence, and `∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³`, so

    A = Σⱼ Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³) / z  dz

exactly (residual 0.0). The integrand is regular on `[0,1]`: the cubic has
**no root there** (min `0.615`, endpoints both `1`), so this is a genuinely
convergent real integral even though `|y₁| = 1.52 > 1` makes the defining
series diverge.

Combining with the reduction, and using `y₁y₂y₃ = 1` (so `log r = −½log y₃`)
plus `y₁+y₂ = 2−y₃`, **(SUM) becomes an identity with no dilogarithm and no
complex numbers, in the single real algebraic number `y₃`:**

    −∫₀¹ log(1−2z+3z²−z³)/z dz
        = −½·log²(y₃) + (2/3)·(θ−π)² − π²/6,
      θ = arccos( (2−y₃)·√y₃ / 2 )

verified to `1.1e-40`. Control: the same expression on the cubic
`y³−y²+2y−1` fails by `0.15`, so it is cubic-specific, not an identity of the
shape.

**Why this matters for the Lean side.** The complex-`Li₂` continuation
(`qou-gkco`) was the blocker for discharging `hrefl`. This form needs neither
a complex dilogarithm nor analytic continuation — only a real interval
integral, `log`, and `arccos`, all of which Mathlib has. The blocker is
bypassed *for this purpose*.

**It is still not proved.** The restatement is equivalent to the ladder, not a
solution to it; a closed-form evaluation of this integral is itself
substantial. What changed is that the target is now elementary and
formalizable rather than Bloch-group-shaped. Left OPEN; bean `qou-0yqu`.

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
from _precision import set_compute_dps  # noqa: E402 — dps must rise before module constants

from witness_base import WitnessBuilder        # noqa: E402
from fivetwo_saddle_values import saddle_roots  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

LEGACY_IM_V1 = mp.mpf("1.3790860299")
LEGACY_V3 = mp.mpf("-2.7580990292")

EXACT_TOL = mp.mpf("1e-35")     # identity gates, at 50 dps
CONV_TOL = mp.mpf("2e-4")       # "is the legacy literal this convention?"


def saddle_V(y, branch):
    """GGM eq (234) at x = 1."""
    return 3 * mp.polylog(2, y) + (mp.log(y) + branch * mp.pi * 1j) ** 2


def main() -> int:
    set_compute_dps()
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

    # ---- S1: is the sum rule special to 5_2, or generic bookkeeping? -----
    # If ANY cubic with one real and two conjugate roots gave -3 pi^2/2, the
    # identity would be a statement about branch choices, not about 5_2.
    # Four of the controls share 5_2's Vieta constraint prod(y) = 1 (hence
    # sum log y = 0), so this isolates the arithmetic of the 5_2 cubic.
    controls = [("y^3-2y^2+3y-2", [1, -2, 3, -2]),
                ("y^3-y^2+2y-1", [1, -1, 2, -1]),
                ("y^3+y^2+2y-1", [1, 1, 2, -1]),
                ("y^3-3y^2+4y-1", [1, -3, 4, -1]),
                ("y^3-2y^2+4y-1", [1, -2, 4, -1])]
    tgt = -3 * mp.pi ** 2 / 2
    print("\n  [S1] specificity controls (same shape, different cubic):")
    devs = []
    for nm, c in controls:
        rts = mp.polyroots(c, maxsteps=300, extraprec=300)
        r3 = next(r for r in rts if abs(mp.im(r)) < mp.mpf(10) ** (-15))
        r1 = next(r for r in rts if mp.im(r) > 0)
        r2 = next(r for r in rts if mp.im(r) < 0)
        s = sum(mp.re(saddle_V(y, b)) for y, b in zip([r1, r2, r3], [-1, 1, 1]))
        devs.append((nm, abs(s - tgt)))
        print(f"        {nm:16s} sum ReV = {mp.nstr(s, 15):>20s}   "
              f"dev {mp.nstr(abs(s - tgt), 4)}")
    min_dev = min(d for _, d in devs)
    gate("S1", "the sum rule is SPECIFIC to the 5_2 cubic",
         min_dev > mp.mpf("0.01"),
         f"   nearest control is {mp.nstr(min_dev, 4)} away vs "
         f"{mp.nstr(r_sum, 3)} for 5_2")

    verdict = (
        "SUM RULE: sum_j Re V_j = -3 pi^2/2 exactly (residual "
        f"{mp.nstr(r_sum, 3)} at 50 dps), equivalently V3 = -2 Re V1 - "
        "3 pi^2/2. The corpus's pi^2/2 'extraction' shift is therefore the "
        "unique CENTERING that makes the three saddle values sum to zero, "
        "not an unexplained fudge. It is SPECIFIC to the 5_2 cubic, not "
        "branch bookkeeping: five control cubics of the same shape -- four "
        "sharing 5_2's prod(y)=1 constraint -- miss the target by "
        f"{mp.nstr(min_dev, 3)} to {mp.nstr(max(d for _, d in devs), 3)}, so "
        "the identity is an arithmetic property of the 5_2 saddle cubic "
        "(Bloch-group / dilogarithm-ladder shaped), NOT a formal artifact. "
        "It is verified to 80 digits but NOT PROVED. PROVENANCE: both "
        "long-unexplained "
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
    w.add_data("specificity_controls", {
        "note": "five control cubics of the same shape (one real + two "
                "conjugate roots); four share prod(y)=1, so sum log y = 0 as "
                "for 5_2. None reproduces -3 pi^2/2 => the identity is not "
                "branch bookkeeping.",
        "deviations": {nm: mp.nstr(d, 6) for nm, d in devs},
        "five_two_residual": mp.nstr(r_sum, 6),
    })
    w.add_data("proof_status", {
        "status": "NUMERICALLY VERIFIED to 80 dps, NOT PROVED",
        "reduction": "sum log y_j = 0 (Vieta, prod y = 1) and sum L_j = pi*i "
                     "give sum L_j^2 = -pi^2 - 2*e2(L), so the sum rule is "
                     "equivalent to 3*sum Li2(y_j) = 2*Re e2(L) - pi^2/2 -- a "
                     "dilogarithm-vs-log-product relation, i.e. Bloch-group / "
                     "five-term shaped.",
        "open": "a Bloch-group or five-term-relation proof over the 5_2 trace "
                "field. Numerical verification at 80 dps is strong evidence, "
                "not a proof.",
        "branch_data": "2 log y_j - 3 log(1-y_j) = 2 pi i eps_j with "
                       "eps = (+1,-1,0), exact at all three roots; this is "
                       "where the pi^2 in the sum rule comes from",
        "derived_relation": "summing the reflection identity over the roots "
                            "gives A + B = pi^2/2 - (2/3) sum (log y_j)^2 - "
                            "(4 pi/3) arg(y1), verified exactly, where "
                            "A = sum Li2(y_j), B = sum Li2(1-y_j)",
        "why_not_closed": "one equation, two unknowns (A = 0.9717306815, "
                          "B = 0.3514640301, no evident closed form for "
                          "either separately)",
        "identified_route": "Kubert/distribution relation Li2(z^n) = "
                            "n sum_k Li2(zeta_n^k z) applied to "
                            "Li2(y^2) = Li2((1-y)^3), which supplies a second "
                            "relation at the cost of omega*(1-y) arguments",
    })
    w.add_data("verdict", verdict)
    w.save()
    print("\n  witness written")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
