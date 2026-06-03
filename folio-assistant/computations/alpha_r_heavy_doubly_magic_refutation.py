#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation campaign — DECISIVE refutation
#   of the r=4A-1 single-rank q-Pochhammer rule via the q>1 asymptotic
#   divergence.  Reads canonical witness data only.  NO fits.
"""
r=4A-1 single-rank rule — DECISIVE refutation via q-Pochhammer divergence.

# Ref: docs/audits/2026-06-03-alpha-r-q-pochhammer-derivation-design.md
# Ref: alpha_r_4A_minus_1_cross_isotope.py (the doubly-magic reframe this
#      script CORRECTS)

## What this resolves

Commit 1-2 found that for ⁴He the single-rank correction
`B_corrected = B_leading − m_e · |(q;q)_{4A-1=15}|` lands at +1.79 %
(3.3× better than canonical +5.87 %), and commit 2 reframed this as
a possible "doubly-magic-only" rule (⁴He being the only doubly-magic
isotope in the D/T/³He/⁴He set).

**This commit DECISIVELY REFUTES the r=4A-1 rule** — including the
doubly-magic reframe — by evaluating the rule on the OTHER doubly-
magic atoms (¹⁶O, ⁴⁰Ca, ⁴⁸Ca, ²⁰⁸Pb).

## The mechanism: q-Pochhammer super-exponential growth at q>1

For q > 1, `|(q;q)_r| = Π_{k=1..r}|1 − q^k|` grows like
`q^{r(r+1)/2}` (each factor |1−q^k| ≈ q^k for large k).  So the
single-rank correction term `m_e · |(q;q)_{4A-1}|`:

**Elementary identity (provable from q-Pochhammer algebra, q > 1):**

    |(q; q)_r|  =  ∏_{k=1}^{r} (q^k − 1)             (since q^k > 1)
                =  ∏_{k=1}^{r} q^k · (1 − q^{-k})
                =  q^{r(r+1)/2}  ·  ∏_{k=1}^{r} (1 − q^{-k})

The first factor q^{r(r+1)/2} grows super-exponentially in r.
The second factor is a partial product whose limit is
`(q^{-1}; q^{-1})_∞` — bounded in (0, 1), so |(q;q)_r| / q^{r(r+1)/2}
saturates to a numerical constant of order 1.10×10⁻⁶ at q_0.
Therefore the rank-r single-rank correction grows as q_0^{r(r+1)/2}
to leading order:


| atom  | A   | r=4A−1 | log₁₀|(q;q)_r| | m_e·|(q;q)_r| (MeV) |
|-------|-----|--------|----------------|---------------------|
| ⁴He   | 4   | 15     | 0.35           | 1.15 (O(1) ✓)       |
| ¹⁶O   | 16  | 63     | 85.4           | ~10⁸⁵ ✗             |
| ⁴⁰Ca  | 40  | 159    | 570            | ~10⁵⁷⁰ ✗            |
| ⁴⁸Ca  | 48  | 191    | 825            | ~10⁸²⁵ ✗            |
| ²⁰⁸Pb | 208 | 831    | 15659          | ~10¹⁵⁶⁵⁹ ✗          |

For every doubly-magic atom heavier than ⁴He, the r=4A−1 correction
overshoots B_AME (~tens to thousands of MeV) by hundreds-to-tens-of-
thousands of orders of magnitude.

## Verdict

**The r=4A−1 rule is FALSE.**  ⁴He is the unique mass number where
`4A−1 = 15` lands in the narrow window (r ≈ 13–16) where `|(q;q)_r|`
is still O(1) — just before the super-exponential blowup begins
(the q-Pochhammer at q_0 ≈ 1.11 has its magnitude-minimum near
r ≈ 6, climbs through O(1) around r ≈ 15, then diverges).  The
⁴He +1.79 % match is therefore a **low-A numerical coincidence**,
NOT a doubly-magic structural rule.

This CORRECTS the commit-2 reframe ("doubly-magic-specific, not
refuted"): a genuine doubly-magic rule would have to hold for ¹⁶O,
⁴⁰Ca, ²⁰⁸Pb, and it catastrophically fails there.

## Implication for the campaign

The single-rank q-Pochhammer ansatz is closed (refuted).  Any
magic-A residual closure must be:
- **bounded for all A** (the q-Pochhammer single-rank is not), and
- **derived, not rank-searched** (the r=4A−1 was a per-⁴He search
  hit, not a forward prediction).

The honest remaining direction is the GS-NF jet-tower extraction of
the per-derivation weights (`prop:six-term-per-derivation-weights`),
which is bounded by construction (it is a truncation of a convergent
q-expansion, not a divergent q-Pochhammer).

## Usage

    cd folio-assistant/computations
    python3 alpha_r_heavy_doubly_magic_refutation.py
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
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

Q = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV_F))
M_E_LOG10 = mp.log10(M_E)

# Doubly-magic atoms (Z and N both in {2,8,20,28,50,82,126}) +
# approximate AME binding energies (MeV) for scale comparison.
DOUBLY_MAGIC = [
    ("4He",   2,   2,   28.30),
    ("16O",   8,   8,   127.62),
    ("40Ca",  20,  20,  342.05),
    ("48Ca",  20,  28,  416.00),
    ("208Pb", 82,  126, 1636.43),
]


def qpoch_log10(r: int) -> mp.mpf:
    """log₁₀|(q;q)_r| — summed in log space to avoid overflow at large r."""
    s = mp.mpf(0)
    for k in range(1, r + 1):
        s += mp.log10(abs(1 - Q ** k))
    return s


rows = []
for atom, Z, N, B_AME in DOUBLY_MAGIC:
    A = Z + N
    r = 4 * A - 1
    lg = qpoch_log10(r)
    term_log10 = lg + M_E_LOG10           # log₁₀(m_e·|(q;q)_r|)
    b_ame_log10 = mp.log10(mp.mpf(B_AME))
    overshoot_orders = float(term_log10 - b_ame_log10)
    rows.append({
        "atom": atom, "Z": Z, "N": N, "A": A,
        "r_4A_minus_1": r,
        "log10_qpoch": float(lg),
        "log10_correction_term_MeV": float(term_log10),
        "B_AME_MeV": B_AME,
        "log10_B_AME": float(b_ame_log10),
        "overshoot_orders_of_magnitude": overshoot_orders,
        "term_is_O1": bool(abs(float(term_log10)) < 2),
    })

# Verdict: rule holds (term O(1)) ONLY for ⁴He; diverges for all heavier.
n_O1 = sum(1 for r in rows if r["term_is_O1"])
rule_is_universal_doubly_magic = (n_O1 == len(rows))

wb = (WitnessBuilder("alpha-r-heavy-doubly-magic-refutation", engine="mpmath")
      .set_description(
          "DECISIVE refutation of the r=4A-1 single-rank q-Pochhammer "
          "rule.  Evaluates m_e·|(q;q)_{4A-1}| on all doubly-magic atoms "
          "⁴He/¹⁶O/⁴⁰Ca/⁴⁸Ca/²⁰⁸Pb.  The q>1 super-exponential growth "
          "(q^{r(r+1)/2}) makes the correction term ~10^85 MeV at ¹⁶O and "
          "~10^15659 MeV at ²⁰⁸Pb — refuting the rule for every "
          "doubly-magic atom except ⁴He, where r=15 is a low-A coincidence."
      ))
wb.add_data("constants", {"q_0": str(Q), "m_e_MeV": str(M_E)})
wb.add_data("per_atom", rows)
wb.add_data("verdict", {
    "rule": "B_corrected = B_leading - m_e·|(q;q)_{4A-1}|",
    "holds_for": "⁴He only (r=15, term O(1))",
    "refuted_for": "¹⁶O, ⁴⁰Ca, ⁴⁸Ca, ²⁰⁸Pb (term diverges as q^{r(r+1)/2})",
    "conclusion": "r=4A-1 is a low-A coincidence, NOT a doubly-magic rule",
    "corrects": "alpha_r_4A_minus_1_cross_isotope.py commit-2 reframe",
})
wb.add_assertion(
    "r_4A_minus_1_refuted_for_heavy_doubly_magic",
    computed=int(rule_is_universal_doubly_magic),
    expected=0,
    tolerance=0,
    source=(
        "m_e·|(q;q)_{4A-1}| is O(1) only for ⁴He (r=15); for ¹⁶O "
        "(r=63) it is ~10^85 MeV, refuting the rule for every "
        "doubly-magic atom heavier than ⁴He.  The ⁴He match is a "
        "low-A coincidence in the narrow O(1) window of |(q;q)_r| "
        "before its super-exponential blowup at q>1."
    ),
)
out_path = wb.save()

print("=" * 84)
print(" r=4A-1 single-rank rule — DECISIVE refutation (heavy doubly-magic)")
print("=" * 84)
print(f"  q_0 = {float(Q):.6f}, m_e = {float(M_E):.6f} MeV")
print()
print(f"  {'atom':>6} {'A':>4} {'r=4A-1':>7} {'log10|(q;q)_r|':>15} "
      f"{'corr term (MeV)':>18} {'B_AME':>9} {'overshoot':>12}")
for r in rows:
    tl = r["log10_correction_term_MeV"]
    term_str = f"{10**tl:.2e}" if tl < 6 else f"~10^{tl:.0f}"
    over = r["overshoot_orders_of_magnitude"]
    over_str = "O(1) ✓" if r["term_is_O1"] else f"+{over:.0f} orders ✗"
    print(f"  {r['atom']:>6} {r['A']:>4} {r['r_4A_minus_1']:>7} "
          f"{r['log10_qpoch']:>15.2f} {term_str:>18} "
          f"{r['B_AME_MeV']:>9.1f} {over_str:>12}")
print()
print(f"  VERDICT: r=4A-1 holds for {n_O1}/{len(rows)} doubly-magic atoms (⁴He only).")
print(f"  → REFUTED as a doubly-magic rule; ⁴He r=15 is a low-A coincidence")
print(f"    (only A where |(q;q)_{{4A-1}}| is still O(1) before q>1 blowup).")
print(f"  → Corrects the commit-2 'doubly-magic-specific' reframe.")
print()
print(f"  Witness: {out_path}")
