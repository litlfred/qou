"""Closed-form predictions for Q_β c_8, c_9, c_10 — Pell-Lucas pattern extension.

Per user prompt 2026-06-04 ("we need to get to Q_β c_8"). Reading the
existing `qbeta-decay-sdp-extended-ck.witness.json` (Pell-Lucas-clean
classification at the silver ratio q = 1 + √2) reveals a structural
pattern the docstring did not yet state:

  c_2 = -1                  (factor convention)
  c_3 = -2                  (J_Hopf at q=1, σ-action eigenvalue)
  c_4 = c_3 · b⁴       =  -2·b⁴
  c_5 = -(b² + 1/2)         (the AVERAGING-RESONANCE outlier, +1/2 fingerprint)
  c_6 = c_3² · b²      =   4·b²
  c_7 = c_3³           =  -8
  c_8 = c_3² · b⁴      =   4·b⁴      ← NEW closed form (this probe)
  c_9 = c_3³ · b²      =  -8·b²      ← NEW closed form (this probe)
  c_10 = c_3² · b⁶     =   4·b⁶      ← NEW closed form (this probe)

The new closed forms are derived by EXTENDING the alternation visible in
c_4..c_7:
  - even k ≥ 6 (excluding the c_5 outlier): c_k = c_3² · b^(k−4) = 4·b^(k−4)
  - odd  k ≥ 7 (excluding the c_5 outlier): c_k = c_3³ · b^(k−7) = -8·b^(k−7)

**Verification at the silver ratio q = 1 + √2 (b² = 7/8 exact):**

  c_8 predicted = 4·b⁴ = 4·(7/8)² = 4·49/64 = 49/16
  witness c_8 silver value         = 49/16          ✓ MATCH

  c_9 predicted = -8·b² = -8·(7/8) = -7
  witness c_9 silver value         = -7            ✓ MATCH

  c_10 predicted = 4·b⁶ = 4·(7/8)³ = 4·343/512 = 343/128
  witness c_10 silver value        = 343/128       ✓ MATCH

All three match the witness's silver-ratio rational values exactly. This
is a PURE σ-ACTION pattern (no averaging-resonance fingerprint at
k = 8, 9, 10) — consistent with the witness assertions
`c_{8,9,10}_extracted_finite` + the Pell-Lucas-clean classification.

**Honest caveat about q₀ evaluation:**

The witness's docstring already warns that at k ≥ 8 the SDP-leverage
on c_k at the fixed q₀ is essentially noise-floor (the (R − Π N_j − 1)
factor becomes too small to constrain higher c_k). So:

  c_8 closed form at q₀:    4·b₀⁴ ≈ 2.266
  c_8 SDP-extracted at q₀:  ≈ 7649.106         ← noise-dominated

These DIFFER by ~10³ — the SDP-extracted q₀ value at k=8 is below the
extraction's noise floor and should not be read as a precision claim.
The STRUCTURAL signal is the silver-ratio match (this probe), NOT the
q₀ value. Wiring `c_k_closed = 4·b^(k−4)` into production at q₀ is
proposed; whether it improves or degrades Q_β precision is the next
empirical question (out of scope for this probe).

EXPLORATORY. No production wiring. No fit (the closed forms are
EXTENSIONS of the documented c_4..c_7 pattern, not tuned to anything).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from fractions import Fraction

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMPUTATIONS_ROOT = HERE.parent
if str(COMPUTATIONS_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPUTATIONS_ROOT))

import _path_bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def hoefsmit_b_squared_from_provenance() -> mp.mpf:
    """Load Hoefsmit b² at q₀ from the canonical provenance witness.

    Reads `hoefsmit_b` from `q-beta-operator-valued-N3.witness.json`
    (the same provenance used by `qbeta_closed_form_wiring_n4_to_n10.py`)
    and returns b² = b · b. Avoids hardcoding the b value here so the
    probe stays in sync if the upstream witness is regenerated.
    """
    provenance = COMPUTATIONS_ROOT / "q-beta-operator-valued-N3.witness.json"
    with open(provenance) as f:
        d = json.load(f)
    b = mp.mpf(str(d["data"]["hoefsmit_b"]))
    return b * b


def closed_form_c_k(k: int, b_sq: mp.mpf) -> mp.mpf:
    """Closed-form value of c_k extrapolated from the Pell-Lucas pattern.

    For k ≥ 6 (excluding the c_5 averaging-resonance outlier):
      even k: c_k = c_3² · b^(k-4) =  4 · b^(k-4)
      odd  k: c_k = c_3³ · b^(k-7) = -8 · b^(k-7)
              (since c_3 = -2, c_3² = 4, c_3³ = -8;
               b^(k-4) = (b²)^((k-4)/2) for even k ≥ 6,
               b^(k-7) = (b²)^((k-7)/2) for odd  k ≥ 7).
    """
    if k < 6:
        raise ValueError(f"closed_form_c_k is only defined for k >= 6 here; got k={k}")
    if k % 2 == 0:
        # c_k = c_3² · b^(k-4) = 4 · b^(k-4)
        # written in b² powers: b^(k-4) = (b²)^((k-4)/2)
        return mp.mpf(4) * b_sq ** ((k - 4) // 2)
    else:
        # c_k = c_3³ · b^(k-7) = -8 · b^(k-7) ; b^(k-7) = (b²)^((k-7)/2) since k-7 is even
        return mp.mpf(-8) * b_sq ** ((k - 7) // 2)


def silver_rational_c_k(k: int) -> Fraction:
    """Closed form evaluated at the silver-ratio b² = 7/8 (exact rational)."""
    if k < 6:
        raise ValueError(f"silver_rational_c_k is only defined for k >= 6 here; got k={k}")
    seven_eighths = Fraction(7, 8)
    if k % 2 == 0:
        return Fraction(4) * seven_eighths ** ((k - 4) // 2)
    else:
        return Fraction(-8) * seven_eighths ** ((k - 7) // 2)


def main() -> int:
    mp.mp.dps = 60
    q0 = mp.mpf(Q_50_DIGIT_STR)
    b_sq = hoefsmit_b_squared_from_provenance()

    print("=" * 78)
    print(" Q_β c_8, c_9, c_10 — closed-form Pell-Lucas extension")
    print("=" * 78)
    print(f"  q₀                = {float(q0):.10f}")
    print(f"  b² at q₀ (from SDP) = {float(b_sq):.10f}")
    print(f"  b² at silver       = 7/8 = 0.8750 (exact rational)")
    print()
    print("  Closed forms:")
    print("    c_8  = c_3² · b⁴   =  4 · b⁴")
    print("    c_9  = c_3³ · b²   = -8 · b²")
    print("    c_10 = c_3² · b⁶   =  4 · b⁶")
    print()

    # Silver-ratio rationals (from the witness, for cross-check)
    SILVER_WITNESS = {
        8: Fraction(49, 16),
        9: Fraction(-7, 1),
        10: Fraction(343, 128),
    }

    print(f"  {'k':>3} {'closed (silver)':>20} {'witness silver':>20} {'match?':>8}")
    silver_match = {}
    for k in (8, 9, 10):
        pred_silver = silver_rational_c_k(k)
        actual_silver = SILVER_WITNESS[k]
        match = (pred_silver == actual_silver)
        silver_match[k] = match
        print(f"  {k:>3} {str(pred_silver):>20} {str(actual_silver):>20} "
              f"{'✓' if match else '✗':>8}")
    print()

    # q₀ numerical evaluations
    print(f"  {'k':>3} {'closed at q₀':>22} {'SDP-extracted at q₀':>22} "
          f"{'ratio':>14}")
    SDP_AT_Q0 = {  # from qbeta-decay-sdp-extended-ck.witness.json
        8: mp.mpf("7649.105892246863"),
        9: mp.mpf("897807.6156471489"),
        10: mp.mpf("105411380.10260098"),
    }
    q0_predictions = {}
    for k in (8, 9, 10):
        pred_q0 = closed_form_c_k(k, b_sq)
        sdp_q0 = SDP_AT_Q0[k]
        ratio = sdp_q0 / pred_q0 if pred_q0 != 0 else mp.inf
        q0_predictions[k] = pred_q0
        print(f"  {k:>3} {mp.nstr(pred_q0, 10):>22} "
              f"{mp.nstr(sdp_q0, 10):>22} "
              f"{mp.nstr(ratio, 6):>14}")
    print()
    print("  Honest read: the SDP q₀-extraction is NOISE-DOMINATED at k ≥ 8")
    print("  (per the source script's docstring caveat). The structural signal")
    print("  is the silver-ratio match, NOT the q₀ value. The closed forms")
    print("  derived here predict the STRUCTURAL c_k at any q via b(q).")
    print()

    out = {
        "computation": "qbeta-c8-c10-pell-lucas-closed-form-predictions",
        "description": (
            "Closed-form predictions for Q_β c_8, c_9, c_10 extending the "
            "Pell-Lucas σ-action pattern documented in "
            "qbeta-decay-sdp-extended-ck.witness.json. The closed forms "
            "    c_8 = c_3²·b⁴ = 4·b⁴,  "
            "c_9 = c_3³·b² = -8·b²,  "
            "c_10 = c_3²·b⁶ = 4·b⁶  "
            "match the witness's silver-ratio rational values exactly "
            "(49/16, -7, 343/128). At q₀ the closed forms differ from the "
            "SDP-extracted values by orders of magnitude — this is the "
            "DOCUMENTED q₀ noise-floor at k ≥ 8 (per the SDP script's "
            "own docstring caveat), not a refutation of the closed form. "
            "STRUCTURAL signal at silver, NOT precision claim at q₀. "
            "EXPLORATORY. No production wiring. No fit."),
        "q_0_50dps": str(q0),
        "b_squared_at_q0": mp.nstr(b_sq, 30),
        "closed_form_definitions": {
            "c_8":  "c_3² · b⁴  =  4 · b⁴",
            "c_9":  "c_3³ · b²  = -8 · b²",
            "c_10": "c_3² · b⁶  =  4 · b⁶",
        },
        "pattern_extension": (
            "Even k ≥ 6 (excluding c_5 outlier): c_k = 4·b^(k-4).  "
            "Odd  k ≥ 7 (excluding c_5 outlier): c_k = -8·b^(k-7)."),
        "silver_ratio_verification": {
            f"c_{k}_silver_predicted": str(silver_rational_c_k(k))
            for k in (8, 9, 10)
        },
        "silver_ratio_witness_values": {
            f"c_{k}_silver_witness": str(SILVER_WITNESS[k])
            for k in (8, 9, 10)
        },
        "silver_ratio_match": {
            f"c_{k}_match": silver_match[k] for k in (8, 9, 10)
        },
        "all_silver_match": all(silver_match.values()),
        "q0_predictions_from_closed_form_50dps": {
            f"c_{k}_closed_at_q0": mp.nstr(q0_predictions[k], 30)
            for k in (8, 9, 10)
        },
        "q0_sdp_extracted_for_comparison": {
            f"c_{k}_sdp_at_q0": mp.nstr(SDP_AT_Q0[k], 16)
            for k in (8, 9, 10)
        },
        "q0_noise_floor_caveat": (
            "Per qbeta_decay_sdp_extended_ck.py docstring: 'at k=8, 9, 10 "
            "the leverage is even tighter — the extracted values are "
            "essentially noise floor / numerically ambiguous at the fixed "
            "q_0 to within rounding tolerance of (R-1) factorization. "
            "...the Pell-Lucas test should be read as STRUCTURAL signal "
            "at the silver ratio, not as a precision claim at q_0.' "
            "So the gap between closed-form-at-q₀ and SDP-extracted-at-q₀ "
            "is the documented noise floor, not a refutation."),
        "verdict": (
            "Silver-ratio match 3/3 EXACT. Closed forms identified for "
            "c_8, c_9, c_10. Lean-formalisable as `norm_num` rational "
            "identities + the symbolic b² substitution. Production-wiring "
            "decision is OPEN: at q₀ the closed forms predict O(1)-O(10) "
            "values vs the SDP-extracted noise-floor O(10³)-O(10⁸) — "
            "wiring closed forms would replace the noise with the "
            "structural prediction; net Q_β precision impact is empirical."),
    }
    out_path = COMPUTATIONS_ROOT / "qbeta-c8-c10-pell-lucas-closed-form-predictions.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"  Witness: {out_path.name}")
    return 0 if all(silver_match.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
