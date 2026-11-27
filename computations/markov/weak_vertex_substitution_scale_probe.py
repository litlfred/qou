#!/usr/bin/env python3
"""
weak_vertex_substitution_scale_probe.py — wiring |W|² in place of s² into the
half-life predictions multiplies every decay rate by ≈ 1.19·10⁴; the
prescribed substitution is a scope-(a) negative, and the two stale W values
in the corpus are the SAME engine defect at two Markov parameters.

WHAT THIS SETTLES (bean qou-ix74; owner: "the |W|² table-wiring compute
tranche", 2026-09-05).

1. THE WIRING.  prf:hadron-half-life item 1 and rem:hadron-half-life-fermi
   open computation 2 prescribe replacing the single-crossing coupling
   s² = (q^{1/2} − q^{-1/2})² = (q−1)²/q in the decay rate by the full
   weak-vertex form factor |W(q)|², W = tr_M((σ₀σ₁)⁵) =
   q²(q¹²+q⁸−1)/(q²+1)² (qou-egvf, PR #6664).  The rate then scales by
   |W|²/s⁴ and every half-life by s⁴/|W|².  Exact in q, evaluated at the
   proton pin:

       |W(q₀)|²/s⁴(q₀) ≈ 1.1875·10⁴      t_new/t_old ≈ 8.42·10⁻⁵

   so the substitution shortens every predicted half-life by more than four
   orders of magnitude.  It cannot be the 10–17 % heavy-nucleus correction
   the corpus attributed to it.  This is a negative about the PRESCRIBED
   SUBSTITUTION (s² and W are not the same normalisation of a coupling), not
   about W.  Lean: QOU.Braiding.WeakVertexT35.substitutionRateFactor_near_one_hundred_thirty
   (and _lt_twenty_thousand), sorry-free.

   The corpus's own live producer computations/t35-weak-vertex.py has printed
   this factor (as 7.9·10³ with its then-wrong W) since 2026-08-29; nothing
   read it.

2. PROVENANCE OF THE TWO STALE VALUES.  hecke_division._trace_word applied
   only the Markov rotation and never the Hecke relation (fixed this
   tranche), which reduces to tr(word) = z^{len(word)} on every reduced
   monomial.  Applied to the reducer's (correct) reduced form of (σ₀σ₁)⁵:

       Σ c_w · z_C^{|w|} ≈ 0.7036      (the value ex:hadron-half-life-verification published)
       Σ c_w · z_D^{|w|} ≈ 0.9684      (the value t35-weak-vertex.witness.json carried, 2026-08-29)

   Both are asserted below to 4 significant figures.  My audit doc
   docs/audits/2026-09-04-weak-vertex-t35-trace-closed-form.md attributed
   0.7036 to the DEPRECATED t35-full-calculation.py; that was wrong — the
   live engine reproduces it at the excised Markov parameter.  Corrected in
   the companion audit doc of this tranche.

3. THE TABLES.  The six "old" half-life predictions used below are the Lean
   pred_* of ex:hadron-half-life-verification (13.0 yr, 6800 yr, 6.2 yr,
   32 yr, 33 yr, 5.8 d — the s²-based predictions with the 10–17 % overshoot
   the Lean header describes).  Table 4 of that block (12.28, 5896, 5.308,
   28.92, 30.26 yr, 5.022 d, "Skein-Coulomb enhancement, < 3 %") has NO
   producer anywhere in computations/ or docs/ (measured: zero hits on its
   six values outside one unrelated audit line), so it is recorded here as
   an unreproduced published table, not used.

Precision: closed forms exact in sympy; numerics mpmath at 60 dps; the
reducer coefficients for the provenance check are read from the float64
legacy engine and compared at 4 significant figures only (that engine IS
float64; the claim is identification of a historical figure, not a
precision result).

Output: computations/weak-vertex-substitution-scale.witness.json
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
import hecke_symbolic as hs  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = hs.q
W = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2      # qou-egvf closed form
S_SQ = (q - 1) ** 2 / q                                     # (q^{1/2} − q^{-1/2})²
FACTOR = W ** 2 / S_SQ                                      # |W|²/s²  (ONE power: S_SQ IS s²)
FACTOR_CLOSED = q ** 5 * (q ** 12 + q ** 8 - 1) ** 2 / ((q ** 2 + 1) ** 4 * (q - 1) ** 2)

# Lean pred_* of ex:hadron-half-life-verification (s²-based, pre-Coulomb)
NUCLEI = [
    ("3H",    "13.0",  "yr", "12.32"),
    ("14C",   "6800",  "yr", "5730"),
    ("60Co",  "6.2",   "yr", "5.2714"),
    ("90Sr",  "32.0",  "yr", "28.79"),
    ("137Cs", "33.0",  "yr", "30.17"),
    ("210Bi", "5.8",   "d",  "5.012"),
]
TABLE4_PUBLISHED = {"3H": "12.28", "14C": "5896", "60Co": "5.308", "90Sr": "28.92",
                    "137Cs": "30.26", "210Bi": "5.022"}


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP
    f_factor = sp.lambdify(q, FACTOR, "mpmath")
    f_W = sp.lambdify(q, W, "mpmath")
    f_s2 = sp.lambdify(q, S_SQ, "mpmath")
    factor = f_factor(q0)
    Wv, s2 = f_W(q0), f_s2(q0)
    t_scale = 1 / factor

    rows = []
    for name, old, unit, obs in NUCLEI:
        old_m, obs_m = mp.mpf(old), mp.mpf(obs)
        new_m = old_m * t_scale
        rows.append({
            "nucleus": name, "unit": unit,
            "t_old_lean_pred": old, "t_obs_nndc": obs,
            "old_over_obs": mp.nstr(old_m / obs_m, 8),
            "t_new_substituted": mp.nstr(new_m, 8),
            "new_over_obs": mp.nstr(new_m / obs_m, 8),
        })

    # Provenance: the buggy z^{len} rule on the legacy reducer's output.
    from q_parameter import Q as q0f  # noqa: E402  (float64 legacy engine input)
    from hecke_division import HeckeDivision, HeckeElement  # noqa: E402
    div = HeckeDivision(q_val=q0f)
    s1, s2g = div.crossing_positive(0), div.crossing_positive(1)
    e = HeckeElement.identity()
    for _ in range(5):
        e = e * s1 * s2g
    red, _ = div.reduce(e)
    terms = {tuple(w): mp.mpf(c) for w, c in red.terms.items()}
    zC = mp.sqrt(q0) / (q0 + 1)
    zD = q0 ** 3 / (q0 ** 2 + 1)
    buggy_C = sum(c * zC ** len(w) for w, c in terms.items())
    buggy_D = sum(c * zD ** len(w) for w, c in terms.items())
    fixed_D = div.markov_trace(red, 3)   # patched engine → canonical

    assertions = [
        {"name": "factor_closed_form_matches",
         "passed": sp.simplify(FACTOR - FACTOR_CLOSED) == 0,
         "note": "|W|²/s² = q^5 (q^12+q^8-1)^2 / ((q^2+1)^4 (q-1)^2), exactly"},
        {"name": "factor_is_one_hundred_twenty_nine_at_proton_pin",
         "passed": mp.mpf("129") < factor < mp.mpf("130"),
         "note": "|W|²/s² = 129.405107404; the Lean bound is "
                 "substitutionRateFactor_near_one_hundred_thirty. This read "
                 "'between 1e4 and 2e4' until 2026-09-05 because FACTOR squared "
                 "S_SQ, which is already s² (bean qou-xql6)"},
        {"name": "substitution_is_not_a_10_to_17_percent_correction",
         "passed": all(mp.mpf("0.008") < mp.mpf(r["new_over_obs"]) < mp.mpf("0.010")
                       for r in rows),
         "note": "SCOPE-(a) NEGATIVE: every substituted half-life lands at 0.8-0.9 % "
                 "of observed, i.e. ~110x too SHORT, where a 10-17 % shortening was "
                 "wanted. Two-sided on the measured band so the gate fails if the "
                 "numbers MOVE. (Read '< 0.1 %' until 2026-09-05, on the s^4 factor.)"},
        {"name": "published_0_7036_is_buggy_rule_at_zC",
         "passed": abs(buggy_C - mp.mpf("0.7036")) < mp.mpf("0.0001"),
         "note": "Σ c_w z_C^{|w|} over the reduced (σ₀σ₁)^5 — provenance of the published value"},
        {"name": "witness_0_9684_is_buggy_rule_at_zD",
         "passed": abs(buggy_D - mp.mpf("0.9684")) < mp.mpf("0.0001"),
         "note": "Σ c_w z_D^{|w|} — provenance of t35-weak-vertex.witness.json (2026-08-29)"},
        {"name": "patched_engine_matches_closed_form",
         "passed": abs(mp.mpf(fixed_D) - Wv) < mp.mpf(10) ** (-12),
         "note": "hecke_division.markov_trace now delegates to the canonical recursion (float64 engine, 1e-12 tolerance)"},
    ]
    n = lambda x, d=50: mp.nstr(x, d, strip_zeros=False)  # noqa: E731
    witness = {
        "computation": "weak-vertex-substitution-scale",
        "description": (
            "Wiring |W|² in place of s² into the beta-decay rate multiplies every "
            "rate by |W(q0)|²/s²(q0) = 129.405107404 (half-lives by 0.00773): the "
            "prescribed substitution is a scope-(a) negative, not the 10–17 % "
            "heavy-nucleus correction attributed to it — the substituted half-lives "
            "land at 0.8–0.9 % of observed, ~110x too short. THE POWER WAS s⁴ AND "
            "THE FACTOR 1.19e4 UNTIL 2026-09-05: S_SQ is already s², so squaring it "
            "double-counted the amplitude; the rate carries s² once "
            "(prf:trace-ratio-observable). The verdict is unchanged, the magnitude "
            "is 92x smaller (bean qou-xql6). Also fixes the provenance of the two "
            "stale W values: both are hecke_division's former z^{len} trace rule, "
            "at z_C (0.7036, the published figure) and z_D (0.9684, the 2026-08-29 "
            "witness). Table 4 of ex:hadron-half-life-verification has no producer."
        ),
        "convention": {"markov_z": "q**3/(q**2+1) (D)", "hecke_h": "q - 1/q",
                       "anchor": "proton pin (Q_50_DIGIT_STR)"},
        "q0": Q_50_DIGIT_STR,
        "W_q0": n(Wv), "s_sq_q0": n(s2),
        "factor_W2_over_s2_q0": n(factor), "halflife_scale_s2_over_W2_q0": n(t_scale),
        "superseded_factor_W2_over_s4_q0": "11875.4418936763026 (wrong power, bean qou-xql6)",
        "factor_closed_form": str(FACTOR_CLOSED),
        "nuclei": rows,
        "table4_published_unreproduced": TABLE4_PUBLISHED,
        "provenance": {
            "reduced_terms_of_sigma01_pow5": {"".join(f"s{i+1}" for i in w) or "1": n(c, 12)
                                              for w, c in terms.items()},
            "buggy_z_len_rule_at_zC": n(buggy_C, 12),
            "buggy_z_len_rule_at_zD": n(buggy_D, 12),
            "patched_engine_zD": n(mp.mpf(fixed_D), 15),
            "note": "correction to docs/audits/2026-09-04-weak-vertex-t35-trace-closed-form.md, "
                    "which attributed 0.7036 to the deprecated t35-full-calculation.py",
        },
        "lean": ["QOU.Braiding.WeakVertexT35.substitutionRateFactor_eq",
                 "QOU.Braiding.WeakVertexT35.substitutionRateFactor_near_one_hundred_thirty",
                 "QOU.Braiding.WeakVertexT35."
                 "substitutionRateFactor_denominator_vanishes_numerator_does_not"],
        "reference_blocks": ["prf:hadron-half-life", "rem:hadron-half-life-fermi",
                             "ex:hadron-half-life-verification"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+mpmath")
    witness["scriptFile"] = str(pathlib.Path(__file__).resolve().relative_to(REPO / "computations"))
    out = REPO / "computations" / "weak-vertex-substitution-scale.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  factor = {n(factor, 12)}  t_scale = {n(t_scale, 8)}")
    print(f"  buggy@zC = {n(buggy_C, 8)}  buggy@zD = {n(buggy_D, 8)}  patched = {n(mp.mpf(fixed_D), 12)}")
    for r in rows:
        print(f"  {r['nucleus']:6} old {r['t_old_lean_pred']:>6} {r['unit']}  new {r['t_new_substituted']:>12} {r['unit']}  new/obs {r['new_over_obs']}")
    print(f"  allPassed = {witness['allPassed']} -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
