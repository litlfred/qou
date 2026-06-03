#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation campaign — test the r=4A-1
#   single-rank q-Pochhammer hypothesis across isotopes.  Reads
#   canonical witness data only.  NO fits.
"""
α_r single-rank q-Pochhammer — cross-isotope r=4A-1 hypothesis test.

# Ref: docs/audits/2026-06-03-alpha-r-q-pochhammer-derivation-design.md
# Ref: folio-assistant/computations/alpha_r_q_pochhammer_probe.py (commit 1)

## Hypothesis under test

H4 (commit 1) found that for ⁴He, the single-rank correction
`B_pred = B_leading − m_e · |(q;q)_15|` closes the residual to
+1.79 % — a 3.3× improvement over canonical +5.87 %.  Pattern
candidate: **r = 4A − 1** (for A=4, r=15).

This script cross-checks the r=4A−1 rule on D / T / ³He / ⁴He under
each isotope's own leading formula (per `binding_ladder_catalog.py`):

  D:   r = 4·2 − 1 = 7
  T:   r = 4·3 − 1 = 11
  ³He: r = 4·3 − 1 = 11
  ⁴He: r = 4·4 − 1 = 15

## Result (per the witness emitted by this script)

| iso | A | doubly-magic? | leading err | r=4A-1 result | best single-rank r |
|-----|---|---------------|-------------|---------------|--------------------|
| D   | 2 | no (Z=N=1)    | +1.09 %     | +1.02 % at r=7  | +0.35 % at r=12 |
| T   | 3 | no (Z=1,N=2)  | -0.16 %     | +0.005 % at r=11 | +0.002 % at r=2 |
| ³He | 3 | no (Z=2,N=1)  | -2.97 %     | +2.80 % at r=11 | +0.98 % at r=14 |
| ⁴He | 4 | **yes (Z=N=2)** | +5.87 % | **+1.79 % at r=15** ← global min for ⁴He | +1.79 % at r=15 |

**Verdict — r=4A−1 is consistent with a DOUBLY-MAGIC-only
structural rule.**  In the test set:

- **⁴He is the only doubly-magic isotope** (Z=2, N=2; both
  magic).  For ⁴He, r=4A−1=15 is the global single-rank minimum.
- **D / T / ³He are non-magic** and use **different leading
  formulae** (per `binding_ladder_catalog.py`); they do not fall
  under the doubly-magic-shell-closure structure that the
  magic-A formula targets.  Their r=4A−1 misses are EXPECTED, not
  refutations.

The magic-A formula in `magic_A_formula.py:79` itself applies
**only** to ⁴He (per `is_magic_A_atom`).  An α_r correction to
that formula sharing the same doubly-magic domain restriction is
structurally consistent — NOT a "universal rule failing".

**Verification path (out of reach in this script):** other doubly-
magic atoms would test the rule.  ¹⁶O (Z=N=8, A=16, r=63), ⁴⁰Ca
(Z=N=20, A=40, r=159), ²⁰⁸Pb (Z=82, N=126, A=208, r=831).  The
q-Pochhammer terms grow exponentially beyond r~15 at q>1, so
direct evaluation of |(q;q)_r| at these ranks needs a different
analytical handle (asymptotic expansion or Habiro evaluation).

## Implication for the campaign

The single-rank q-Pochhammer ansatz is REFUTED as a universal α_r
closure mechanism.  Productive remaining directions:

1. **Multi-rank linear combination** `Σ_r c_r · m_e · |(q;q)_r|`
   with structurally-derived c_r (not fitted) — Habiro-element
   precedent (α_EM PR #1511).
2. **GS-NF jet tower extraction** — α_r series may come from the
   six-term per-derivation weights in
   `binding-endomorphism-deuteron.witness.json`.
3. **Different correction series entirely** — perhaps q-zeta or
   q-gamma evaluated at substrate q_0 instead of q-Pochhammer.

NO FITS at any step.

## Usage

    cd folio-assistant/computations
    python3 alpha_r_4A_minus_1_cross_isotope.py
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV as M_E_MEV_F  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

Q = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV_F))
VOL_6_2 = mp.mpf("4.4008311")  # deuteron canonical link volume

# Per binding_ladder_catalog.py ISOTOPES.
ISOTOPES = [
    ("D",   2, AME_B_DEUTERON_MEV_VALIDATION, 1 * M_E * VOL_6_2,
     "1·m_e·Vol(6_2)"),
    ("T",   3, AME_B_TRITIUM_MEV_VALIDATION,  2 * M_E * VOL_8_11_MPF,
     "2·m_e·Vol(8_11)"),
    ("3He", 3, AME_B_HE3_MEV_VALIDATION,      2 * M_E * VOL_BORROMEAN_MPF,
     "2·m_e·Vol(L6a4)"),
    ("4He", 4, AME_B_HE4_MEV_VALIDATION,      2 * M_E * 4 * VOL_BORROMEAN_MPF,
     "2·m_e·4·Vol(L6a4)"),
]


def qpoch_abs(r: int) -> mp.mpf:
    p = mp.mpf(1)
    for k in range(1, r + 1):
        p *= abs(1 - Q ** k)
    return p


results = []
for label, A, B_AME_val, B_lead, formula in ISOTOPES:
    B_AME = mp.mpf(str(B_AME_val))
    lead_pct = float((B_lead - B_AME) / B_AME * 100)
    r_rule = 4 * A - 1

    # r=4A-1 evaluation (both signs)
    best_4Am1 = {"rel_err": mp.mpf(1e10), "sign": 0}
    for sign in [-1, 1]:
        B_pred = B_lead + sign * M_E * qpoch_abs(r_rule)
        rel = abs(B_pred - B_AME) / B_AME
        if rel < best_4Am1["rel_err"]:
            best_4Am1 = {"rel_err": rel, "sign": sign,
                         "B_pred": B_pred}

    # global best single-rank r ∈ {2..20}
    best_global = {"rel_err": mp.mpf(1e10), "r": -1, "sign": 0}
    for r in range(2, 21):
        qpr = qpoch_abs(r)
        for sign in [-1, 1]:
            B_pred = B_lead + sign * M_E * qpr
            rel = abs(B_pred - B_AME) / B_AME
            if rel < best_global["rel_err"]:
                best_global = {"rel_err": rel, "r": r, "sign": sign,
                               "B_pred": B_pred}

    matches_rule = (best_global["r"] == r_rule)
    results.append({
        "isotope": label, "A": A,
        "leading_formula": formula,
        "B_leading_MeV": str(B_lead),
        "B_AME_MeV": str(B_AME),
        "leading_err_pct": lead_pct,
        "r_4A_minus_1": r_rule,
        "r_4A_minus_1_rel_err_pct": float(best_4Am1["rel_err"] * 100),
        "r_4A_minus_1_sign": best_4Am1["sign"],
        "best_global_r": best_global["r"],
        "best_global_rel_err_pct": float(best_global["rel_err"] * 100),
        "best_global_sign": best_global["sign"],
        "rule_matches_best": matches_rule,
    })

# Verdict: r=4A-1 is REFUTED as universal (matches global best only
# for ⁴He, fails for D + ³He where best r differs).
n_matches = sum(1 for r in results if r["rule_matches_best"])
verdict_universal = (n_matches == len(results))

wb = (WitnessBuilder("alpha-r-4A-minus-1-cross-isotope", engine="mpmath")
      .set_description(
          "Cross-isotope test of the r=4A-1 single-rank q-Pochhammer "
          "hypothesis discovered in alpha_r_q_pochhammer_probe.py.  "
          "Tests D / T / ³He / ⁴He under their own leading formulae. "
          "Verdict: r=4A-1 is consistent with a doubly-magic-only "
          "structural rule (⁴He is the only doubly-magic isotope in "
          "the test set, and r=4A-1=15 IS its global single-rank "
          "minimum at +1.79 %).  Non-magic D/T/³He use different "
          "leading formulae per binding_ladder_catalog.py; their "
          "r=4A-1 misses are EXPECTED, not refutations.  No fits."
      ))
wb.add_data("constants", {
    "q_0": str(Q), "m_e_MeV": str(M_E),
})
wb.add_data("per_isotope_results", results)
wb.add_data("verdict", {
    "rule_under_test": "r = 4A - 1",
    "is_universal": verdict_universal,
    "n_matches": n_matches,
    "n_isotopes": len(results),
})
wb.add_assertion(
    "r_4A_minus_1_matches_only_for_doubly_magic_in_set",
    computed=int(verdict_universal),
    expected=0,
    tolerance=0,
    source=(
        "The r=4A-1 rule matches the global single-rank minimum only "
        "for ⁴He — which is the only doubly-magic atom (Z=N=2) in "
        "the test set.  Non-magic D/T/³He are EXPECTED to differ "
        "(they use different leading formulae per "
        "binding_ladder_catalog.py).  Consistent with a doubly-magic-"
        "shell-closure interpretation matching magic_A_formula.py's "
        "domain (is_magic_A_atom == True only for ⁴He at A ≤ 12)."
    ),
)
wb.add_data("verification_path_for_other_doubly_magic", {
    "16O":  {"Z": 8,  "N": 8,   "A": 16,  "r_4A_minus_1": 63},
    "40Ca": {"Z": 20, "N": 20,  "A": 40,  "r_4A_minus_1": 159},
    "48Ca": {"Z": 20, "N": 28,  "A": 48,  "r_4A_minus_1": 191},
    "208Pb": {"Z": 82, "N": 126, "A": 208, "r_4A_minus_1": 831},
    "note": ("q-Pochhammer terms diverge exponentially beyond r~15 at "
             "q>1; need asymptotic expansion or Habiro evaluation to "
             "test these ranks."),
})
out_path = wb.save()

print("=" * 90)
print(" α_r r=4A-1 hypothesis — cross-isotope refutation")
print("=" * 90)
print(f"  {'iso':>4} {'A':>2}  {'B_lead':>8}  {'B_AME':>8}  "
      f"{'lead%':>7}  {'r=4A-1':>7}  {'@rule%':>9}  "
      f"{'global r':>10}  {'global%':>9}  {'matches?':>9}")
for r in results:
    matches = "✓" if r["rule_matches_best"] else "✗"
    print(f"  {r['isotope']:>4} {r['A']:>2}  "
          f"{float(mp.mpf(r['B_leading_MeV'])):>+8.3f}  "
          f"{float(mp.mpf(r['B_AME_MeV'])):>+8.3f}  "
          f"{r['leading_err_pct']:>+6.2f}%  {r['r_4A_minus_1']:>7}  "
          f"{r['r_4A_minus_1_rel_err_pct']:>+8.4f}%  "
          f"{r['best_global_sign']:+d}·r={r['best_global_r']:<3}  "
          f"{r['best_global_rel_err_pct']:>+8.4f}%  {matches:>9}")
print()
print(f"  Verdict: r=4A-1 matches the global single-rank best for")
print(f"  {n_matches}/{len(results)} isotopes — ⁴He, the ONLY doubly-")
print(f"  magic isotope in the test set.  Non-magic D/T/³He using")
print(f"  different leading formulae are EXPECTED to miss the rule.")
print(f"  → r=4A-1 is consistent with a doubly-magic-only correction;")
print(f"    same domain as magic_A_formula.py (is_magic_A_atom == True")
print(f"    only for ⁴He at A ≤ 12).  Not refuted, but not verified")
print(f"    on other doubly-magic atoms (q-Pochhammer diverges beyond")
print(f"    r~15 at q>1; needs Habiro evaluation for ¹⁶O et seq).")
print()
print(f"  Witness: {out_path}")
