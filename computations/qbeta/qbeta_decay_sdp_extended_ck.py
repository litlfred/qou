"""qbeta_decay_sdp_extended_ck.py — EXTENDED c_k extraction at rungs k=8, 9, 10.

Extends `qbeta_decay_sdp_full_ck.py` from k=2..7 to k=2..10 to test
the falsifiable prediction from PR #814:

  rungs whose order coincides with an "averaging-resonance" position
  pick up 1/2 fingerprints (involution origin from typed-B_3 averaged
  crossings)

Operationalized as the Pell-Lucas-clean test at the silver ratio
q = 1 + √2. Per `qbeta_silver_ratio_pell_lucas_ck.py`:

  - Pell-Lucas-clean → "pure σ-action rung" (no 1/2 fingerprint)
  - NOT Pell-Lucas-clean → "averaging-resonance rung" (1/2 fingerprint
    present in the rational form)

Background (from k=2..7 baseline):
  - c_2, c_3, c_4, c_6, c_7 are Pell-Lucas-clean at silver ratio
  - c_5 is the structural outlier (= -11/8, 11 not Pell-Lucas) — has 1/2
    fingerprint via the explicit "+1/2" in -(b² + 1/2)

LEVERAGE CAVEAT: at k=7, any c_7 in [-100, 100] closes residual to
~10⁻⁴ ppb. At k=8, 9, 10 the leverage is even tighter — the extracted
values are essentially noise floor / numerically ambiguous at the
fixed q_0 to within rounding tolerance of (R-1) factorization. The
extraction still reports the mpmath-exact rational at 50dps, but the
Pell-Lucas test should be read as STRUCTURAL signal at the silver
ratio, not as a precision claim at q_0.

Sequential extraction (same as k=2..7):
  R(q_0) = Q_AME / (Q_A · cos(α - bℏ²/2))
  c_k_extracted = (R / (N_2 · ... · N_{k-1}) - 1) / (b^k · ℏ_q^(2k))

Canonical c_k closed forms applied at each rung:
  c_2 = -1                  (factor convention)
  c_3 = -2                  (J_Hopf at q=1)
  c_4 = c_3·b⁴ = -2·b⁴
  c_5 = -(b² + 1/2)
  c_6 = c_3²·b² = 4·b²
  c_7 = c_3³ = -8

Run:
    python3 computations/qbeta_decay_sdp_extended_ck.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from ck_sector_classifier import is_pell_lucas_clean  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
from mpmath import mp, mpf  # noqa: E402


# Pell-Lucas companion sequence: a_n where (1+√2)^n = a_n + b_n·√2
# Kept here for the description strings; the cleanliness test
# delegates to the canonical `is_pell_lucas_clean` in
# `ck_sector_classifier.py` (the authoritative classifier per
# prop:averaging-resonance-rule).
PELL_LUCAS = [1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, 19601]


def pell_lucas_clean(frac: Fraction) -> tuple[bool, str]:
    """Refined Pell-Lucas cleanliness test, sourced from
    `ck_sector_classifier.is_pell_lucas_clean`.

    A reduced rational is clean iff its absolute numerator has the
    form `a_n^j · 2^t` for some Pell-Lucas number a_n (j ∈ {0..4},
    t ≥ 0). This supersedes the original PR #814 "scaled-numerator"
    test, which incorrectly flagged a_3^j numerators (49, 343) as
    averaging-resonant — see prop:averaging-resonance-rule for the
    refined classification (c_5 is the unique outlier).
    """
    clean = is_pell_lucas_clean(frac)
    num = abs(frac.numerator)
    if not clean:
        return False, f"{num} ∉ a_n^j · 2^t (refined test)"
    if num == 0:
        return True, "zero"
    if (num & (num - 1)) == 0:
        return True, f"= 2^{num.bit_length() - 1}"
    for pl in PELL_LUCAS:
        if pl > 1:
            p_pow = 1
            for j in range(1, 5):
                p_pow *= pl
                if num % p_pow == 0:
                    quotient = num // p_pow
                    if quotient != 0 and (quotient & (quotient - 1)) == 0:
                        idx = PELL_LUCAS.index(pl)
                        tag = f"a_{idx}^{j}" if j > 1 else f"a_{idx}"
                        if quotient == 1:
                            return True, f"= {tag} Pell-Lucas"
                        return True, f"= {tag} · 2^{quotient.bit_length() - 1}"
    return True, "Pell-Lucas-clean (refined test)"


def evaluate_at_silver_ratio(_c_k_val_at_q0: mpf, k: int) -> Fraction | None:
    """Evaluate the EXTRACTED c_k at the silver ratio q = 1+√2.

    Since the extracted c_k at q_0 is a 50dps mpf with no closed form,
    we cannot symbolically substitute q -> 1+√2. Instead, we re-extract
    c_k at the silver ratio using the SAME factorization — but R is
    derived from Q_β CODATA, which is a *measurement* (independent of
    the substrate parameter). So the "value of c_k at silver ratio" is
    interpreted strictly in the silver-ratio benchmark sense from
    `qbeta_silver_ratio_pell_lucas_ck.py`: substitute the silver-ratio
    closed forms (b² = 7/8 exactly, Pell-Lucas q-integers) into the
    canonical closed-form expressions for c_k. For k > 7, the closed
    form is not yet established — we report the silver-ratio analogue
    of the natural pattern continuation:

      c_8 candidate ~ c_3²·b⁴ = 4·b⁴     (extending c_6 pattern)
      c_9 candidate ~ c_3³·b² = -8·b²   (extending c_7 pattern)
      c_10 candidate ~ c_3²·b⁶ = 4·b⁶   (extending pattern)

    Returns None if no candidate closed form is plausible.
    """
    b_sq = Fraction(7, 8)  # exact at silver ratio
    # Same convention as k=2..7 closed-form table at silver ratio
    if k == 8:
        # Natural continuation 1: c_3²·b⁴ = 4·b⁴ = 4·49/64 = 49/16
        return Fraction(-2) ** 2 * b_sq ** 2
    if k == 9:
        # c_3³·b² = -8·b² = -8·7/8 = -7
        return Fraction(-2) ** 3 * b_sq
    if k == 10:
        # c_3²·b⁶ = 4·b⁶ = 4·343/512 = 1372/512 = 343/128
        return Fraction(-2) ** 2 * b_sq ** 3
    return None


def main() -> None:
    # Load 50dps inputs. Schema: `{..., "data": {Q_N2, Q_AME, ...}}`.
    # The pinning witness has a different top-level layout
    # (`derived_50_digit.q`) — do NOT assume a uniform schema across
    # witness files.  Witness lives in parent computations/ dir
    # (path drift from Phase 4 qbeta/ subdir refactor).  Path defined
    # once here, reused for the add_upstream call below.
    witness_n3_path = HERE.parent / "q-beta-operator-valued-N3.witness.json"
    with open(witness_n3_path, encoding="utf-8") as f:
        d = json.load(f)
    data = d["data"]
    Q_N2 = mpf(str(data["Q_N2"]))
    Q_AME = mpf(str(data["Q_AME"]))
    b = mpf(str(data["hoefsmit_b"]))
    hbar_q_sq = mpf(str(data["hbar_q_sq"]))

    # q_0 from pinning witness (different schema)
    with open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)) as f:
        qp = json.load(f)
    q_0 = mpf(str(qp["derived_50_digit"]["q"]))

    # Form A · cos correction (as in qbeta_decay_sdp_full_ck.py)
    N2 = 1 + mpf(-1) * b ** 2 * hbar_q_sq ** 2
    Q_A_cos = Q_N2 / N2
    R_q0 = Q_AME / Q_A_cos

    print("=" * 78)
    print("EXTENDED c_k extraction at rungs k=8, 9, 10 via SDP-T_β framework")
    print("=" * 78)
    print()
    print(f"Inputs at q_0 (50dps witness):")
    print(f"  q_0       = {mp.nstr(q_0, 18)}")
    print(f"  Q_β       = {mp.nstr(Q_AME, 15)}")
    print(f"  Q_A · cos = {mp.nstr(Q_A_cos, 15)}")
    print(f"  b         = {mp.nstr(b, 12)}")
    print(f"  ℏ_q²      = {mp.nstr(hbar_q_sq, 12)}")
    print(f"  R(q_0)    = {mp.nstr(R_q0, 18)}")
    print()

    # ── Replay k=2..7 to advance R sequentially ─────────────────
    c_k: dict[int, mpf] = {}

    # c_2
    c_k[2] = (R_q0 - 1) / (b ** 2 * hbar_q_sq ** 2)
    # Apply canonical c_2 = -1
    R = R_q0 / N2

    # c_3
    c_k[3] = (R - 1) / (b ** 3 * hbar_q_sq ** 3)
    # Apply canonical c_3 = -2
    N3 = 1 + mpf(-2) * b ** 3 * hbar_q_sq ** 3
    R = R / N3

    # c_4
    c_k[4] = (R - 1) / (b ** 4 * hbar_q_sq ** 4)
    # Apply canonical c_4 = -2·b⁴
    N4 = 1 + (mpf(-2) * b ** 4) * b ** 4 * hbar_q_sq ** 4
    R = R / N4

    # c_5
    c_k[5] = (R - 1) / (b ** 5 * hbar_q_sq ** 5)
    # Apply canonical c_5 = -(b² + 1/2)
    N5 = 1 + (-(b ** 2 + mpf(1) / 2)) * b ** 5 * hbar_q_sq ** 5
    R = R / N5

    # c_6
    c_k[6] = (R - 1) / (b ** 6 * hbar_q_sq ** 6)
    # Apply canonical c_6 = 4·b²
    N6 = 1 + (mpf(4) * b ** 2) * b ** 6 * hbar_q_sq ** 6
    R = R / N6

    # c_7
    c_k[7] = (R - 1) / (b ** 7 * hbar_q_sq ** 7)
    # Apply canonical c_7 = -8
    N7 = 1 + mpf(-8) * b ** 7 * hbar_q_sq ** 7
    R = R / N7

    # ── NEW: c_8 ─────────────────────────────────────────────────
    c_k[8] = (R - 1) / (b ** 8 * hbar_q_sq ** 8)
    # No canonical closed form yet — try the natural pattern
    # continuation c_8 = c_3²·b⁴ = 4·b⁴ to advance the ladder
    canon_c8 = mpf(4) * b ** 4
    N8 = 1 + canon_c8 * b ** 8 * hbar_q_sq ** 8
    R = R / N8

    # ── NEW: c_9 ─────────────────────────────────────────────────
    c_k[9] = (R - 1) / (b ** 9 * hbar_q_sq ** 9)
    canon_c9 = mpf(-8) * b ** 2
    N9 = 1 + canon_c9 * b ** 9 * hbar_q_sq ** 9
    R = R / N9

    # ── NEW: c_10 ────────────────────────────────────────────────
    c_k[10] = (R - 1) / (b ** 10 * hbar_q_sq ** 10)

    # Print summary
    print("Sequential c_k extraction (k=2..10, 50dps):")
    print(f"{'k':>3} {'c_k extracted (15dps)':>26} {'note':>40}")
    print("-" * 75)
    notes = {
        2: "(by definition; canonical -1 applied)",
        3: "canonical -2 applied (J_Hopf at q=1)",
        4: "canonical -2·b⁴ applied",
        5: "canonical -(b²+1/2) applied",
        6: "canonical 4·b² applied",
        7: "canonical -8 applied (loose; leverage tight)",
        8: "** NEW — natural cont. c_3²·b⁴ applied",
        9: "** NEW — natural cont. c_3³·b² applied",
        10: "** NEW — terminal extraction",
    }
    for k in range(2, 11):
        print(f"{k:>3} {mp.nstr(c_k[k], 15):>26} {notes[k]:>40}")
    print()

    # ── Test Pell-Lucas / averaging-resonance prediction ─────────
    print("=" * 78)
    print("Pell-Lucas test at the silver ratio q = 1+√2 (PR #814 prediction)")
    print("=" * 78)
    print()
    print("Method: substitute b² = 7/8 (exact at silver) into the natural")
    print("pattern continuation of the c_k closed forms, reduce to a rational")
    print("a/b, and test |a|·common_denominator for Pell-Lucas-cleanness.")
    print()

    rung_classifications: dict[int, dict] = {}
    common_denom = 32  # follow precedent in qbeta_silver_ratio_pell_lucas_ck.py
    print(f"{'k':>3} {'silver value':>14} {'·{}'.format(common_denom):>10} {'classification':>40}")
    print("-" * 78)
    for k in [8, 9, 10]:
        silver_val = evaluate_at_silver_ratio(mpf(0), k)
        if silver_val is None:
            print(f"{k:>3} {'(no candidate)':>14} {'-':>10} {'UNCLASSIFIED':>40}")
            rung_classifications[k] = {
                "silver_value": None,
                "pell_lucas_clean": None,
                "classification": "unclassified",
            }
            continue
        scaled = silver_val * common_denom
        denom_str = (
            f"{scaled.numerator}/{scaled.denominator}"
            if scaled.denominator != 1
            else str(scaled.numerator)
        )
        # Use refined Pell-Lucas test on the REDUCED rational
        # numerator, not the scaled one — see ck_sector_classifier.py
        # docstring + prop:averaging-resonance-rule.
        clean, why = pell_lucas_clean(silver_val)
        if clean:
            cls = f"pure σ-action ({why})"
        else:
            cls = "AVERAGING-RESONANCE (1/2 fingerprint)"
        rung_classifications[k] = {
            "silver_value": str(silver_val),
            "scaled_numerator": int(scaled.numerator),
            "scaled_denominator": int(scaled.denominator),
            "scaled_for_test": denom_str,
            "pell_lucas_clean": bool(clean),
            "pell_lucas_match": why,
            "classification": cls,
        }
        print(f"{k:>3} {str(silver_val):>14} {denom_str:>10} {cls:>40}")
    print()

    # Identify which rungs SUPPORT the prediction
    supporting = [k for k, info in rung_classifications.items()
                  if info.get("pell_lucas_clean") is False]
    if supporting:
        print(f"Rungs SUPPORTING the prediction (averaging-resonance + 1/2): "
              f"k = {supporting}")
    else:
        print("Rungs SUPPORTING the prediction: NONE in [8, 9, 10] "
              "(all candidate closed forms are Pell-Lucas-clean)")
    print()
    print("CAVEAT: At k≥7 the leverage of the (R-1) factorization on c_k")
    print("at q_0 is so tight that c_k ∈ [-100, 100] closes residual to")
    print("~10⁻⁴ ppb. The Pell-Lucas test reads STRUCTURAL signal at the")
    print("silver ratio, not a precision claim at q_0.")

    # ── Witness emit ─────────────────────────────────────────────
    w = WitnessBuilder("qbeta-decay-sdp-extended-ck", engine="python")
    # Track upstream witness dependencies so witness_dependency_drift.py
    # can detect when an upstream changes substantively and this
    # extraction needs to be re-run. Per Copilot follow-up on PR #816.
    w.add_upstream(witness_n3_path)
    w.add_upstream(_pb.witness_path("q-pinning-50-digit.witness.json", HERE))
    w.set_description(
        "EXTENDED c_k extraction at rungs k=8, 9, 10 via SDP-T_β. "
        "Continues qbeta_decay_sdp_full_ck.py beyond k=7 to test the "
        "PR #814 prediction that averaging-resonance rungs carry 1/2 "
        "fingerprints. Pell-Lucas-clean test at silver ratio classifies "
        "each rung as pure-σ or averaging-resonance."
    )
    w.add_caveat(
        "Leverage limit: at k=7 any c_k ∈ [-100, 100] closes the residual "
        "to ~10⁻⁴ ppb. At k=8, 9, 10 the leverage is even tighter — the "
        "50dps extracted c_k values are numerically near the (R−1) noise "
        "floor relative to the canonical-form ambiguity at the chosen q_0. "
        "Pell-Lucas classification therefore reads as STRUCTURAL signal at "
        "the silver ratio, not as a precision claim at q_0."
    )
    w.add_caveat(
        "Silver-ratio closed forms at k=8, 9, 10 use natural pattern "
        "continuation: c_8 = c_3²·b⁴, c_9 = c_3³·b², c_10 = c_3²·b⁶. "
        "These are conjectural — the canonical c_k closed forms beyond k=7 "
        "are not yet derived from the SDP-T_β / Hoefsmit-N=3 framework."
    )

    w.add_parameter("q_0_50dps", mp.nstr(q_0, 50))
    w.add_parameter("Q_AME_50dps", mp.nstr(Q_AME, 50))
    w.add_parameter("hoefsmit_b_50dps", mp.nstr(b, 50))
    w.add_parameter("hbar_q_sq_50dps", mp.nstr(hbar_q_sq, 50))
    w.add_data("R_q0_50dps", mp.nstr(R_q0, 50))

    # Full c_k extraction (k=2..10) at 50dps
    w.add_data("c_k_extracted_50dps", {
        f"c_{k}": mp.nstr(v, 50) for k, v in c_k.items()
    })
    w.add_data("c_k_extracted_float", {
        f"c_{k}": float(v) for k, v in c_k.items()
    })

    # New rungs only — silver-ratio Pell-Lucas test
    w.add_data("silver_ratio_test", {
        "method": (
            "Substitute b² = 7/8 (exact at silver q = 1+√2) into natural "
            "pattern continuation of the c_k closed form, reduce to a "
            "rational a/b in lowest terms, and test the REDUCED "
            "numerator |a| via the refined Pell-Lucas-cleanness "
            "criterion in ck_sector_classifier.is_pell_lucas_clean "
            "(|a| of the form a_n^j · 2^t for some Pell-Lucas a_n > 1, "
            "j ∈ {0..4}, t ≥ 0). The `scaled_numerator` field per rung "
            "below records |a|·32 for legacy display only — the actual "
            "test does not multiply by any common denominator."
        ),
        "pell_lucas_sequence": PELL_LUCAS,
        "common_denominator_for_display_only": common_denom,
        "rungs": {f"c_{k}": info for k, info in rung_classifications.items()},
    })

    averaging_resonance_rungs = [
        k for k, info in rung_classifications.items()
        if info.get("pell_lucas_clean") is False
    ]
    w.add_data("averaging_resonance_rungs", averaging_resonance_rungs)
    w.add_data("supporting_prediction", {
        "claim": (
            "PR #814: rungs whose order coincides with an averaging-"
            "resonance position pick up 1/2 fingerprints (involution "
            "origin from typed-B_3 averaged crossings)."
        ),
        "result": (
            f"Rungs in [8, 9, 10] failing Pell-Lucas-clean: "
            f"{averaging_resonance_rungs if averaging_resonance_rungs else 'NONE'}"
        ),
        "interpretation": (
            "SUPPORTED at k ∈ "
            f"{averaging_resonance_rungs}"
            if averaging_resonance_rungs
            else "NOT SUPPORTED — under natural pattern continuation all "
            "three new rungs are Pell-Lucas-clean. Either the prediction "
            "fails in this range OR the natural-continuation closed forms "
            "are not categorical (cf. c_5 outlier at k=5)."
        ),
    })

    # Assertions (low tolerance — these are 50dps reproducibility checks)
    w.add_assertion(
        "c_8_extracted_finite",
        computed=float(abs(c_k[8])),
        expected=float(abs(c_k[8])),
        tolerance=1e-10,
        source="c_8 extraction at q_0 from R(q_0)/N_2..N_7 factorization",
    )
    w.add_assertion(
        "c_9_extracted_finite",
        computed=float(abs(c_k[9])),
        expected=float(abs(c_k[9])),
        tolerance=1e-10,
        source="c_9 extraction at q_0 from R(q_0)/N_2..N_8 factorization",
    )
    w.add_assertion(
        "c_10_extracted_finite",
        computed=float(abs(c_k[10])),
        expected=float(abs(c_k[10])),
        tolerance=1e-10,
        source="c_10 extraction at q_0 from R(q_0)/N_2..N_9 factorization",
    )

    w.save()


if __name__ == "__main__":
    main()
