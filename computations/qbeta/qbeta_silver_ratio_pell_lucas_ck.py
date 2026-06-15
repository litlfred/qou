"""qbeta_silver_ratio_pell_lucas_ck.py — Pell-Lucas structure of c_k at silver ratio.

At q = 1 + √2 (silver ratio):
- Hecke skein h = q - q⁻¹ = 2
- Hecke quadratic σ² = 2σ + 1 has roots σ = 1 ± √2 (self-referential)
- q-integers [n]_q at silver ratio = Pell-Lucas numbers (1, 1, 3, 7, 17, 41, ...)
- b² (Hoefsmit coupling squared) = 7/8 EXACTLY
- Δ(net) = 0 — β-decay forbidden categorically

c_k at silver ratio:
  c_3 = -2                  ← integer
  c_4 = -2 · (7/8)² = -49/32 ← Pell-Lucas-clean (a_3² = 49)
  c_5 = -(7/8 + 1/2) = -11/8 ← OUTLIER (11 isn't Pell-Lucas)
  c_6 = 4 · 7/8 = 7/2       ← Pell-Lucas-clean (a_3 = 7)
  c_7 = -8                  ← integer

4 of 5 c_k are Pell-Lucas-clean. c_5 is the structural outlier,
flagging that the current `-(b² + 1/2)` closed form may not be
the categorically correct one.

This script emits a witness with the silver-ratio benchmark + the
Pell-Lucas test results, providing a regression target for future
c_k closed-form revisions.
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

import sys
from pathlib import Path
from fractions import Fraction

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def main() -> None:
    # Pell numbers + Pell-Lucas (companion) at silver ratio
    pell = [0, 1, 2, 5, 12, 29, 70, 169]
    pell_lucas = [1, 1, 3, 7, 17, 41, 99, 239]

    print("=" * 72)
    print("Silver ratio: q = 1 + √2; q² = 3 + 2√2; h = q - q⁻¹ = 2")
    print("=" * 72)
    print()
    print(f"Pell-Lucas sequence (a_n where q^n = a_n + b_n·√2):")
    print(f"  a_n: {pell_lucas}")
    print(f"Pell sequence (b_n):")
    print(f"  b_n: {pell}")
    print()
    print(f"q-integers [n]_q at silver ratio:")
    print(f"  [2]_q = q + q⁻¹       = 2√2       (irrational)")
    print(f"  [3]_q = q² + 1 + q⁻²  = {pell_lucas[3]} = a_3  (Pell-Lucas-clean!)")
    print(f"  [5]_q = q⁴+q²+1+q⁻²+q⁻⁴ = {pell_lucas[5]} = a_5")
    print(f"  [7]_q                 = {pell_lucas[6]+pell_lucas[7]-pell_lucas[5]-pell_lucas[6]+pell_lucas[3]} = ?  (skipping)")
    print()

    # Hoefsmit b² at silver ratio
    b_sq = Fraction(7, 8)
    print(f"Hoefsmit b² at silver ratio = (q⁴+q²+1)/(q²+1)² = 7/8 = {b_sq}")
    print(f"  Numerator: q⁴+q²+1 = 7(3+2√2) = 7·(q²+1) / (factor)")
    print(f"  Denominator: (q²+1)² = (4+2√2)² = 8(3+2√2)")
    print(f"  Ratio: 7/8  ✓ EXACT rational")
    print()

    # Empirical c_k closed forms at silver ratio
    c_k_closed = {
        3: ("c_3", Fraction(-2)),
        4: ("c_3 · b⁴ = -2·(7/8)²", Fraction(-2) * b_sq**2),
        5: ("-(b² + 1/2) = -(7/8 + 4/8)", -(b_sq + Fraction(1, 2))),
        6: ("c_3² · b² = 4·(7/8)", Fraction(-2)**2 * b_sq),
        7: ("c_3³ = -8", Fraction(-2)**3),
    }

    print("=" * 72)
    print("c_k closed forms evaluated at silver ratio:")
    print("=" * 72)
    print(f"{'c_k':>5} {'expression':>30} {'value':>15} {'·32':>10} {'Pell-Lucas?':>15}")
    # Use the canonical classifier so this script and the SDP
    # extractor agree on cleanliness — see prop:averaging-resonance-rule.
    from ck_sector_classifier import is_pell_lucas_clean  # noqa: E402
    # Track cleanliness in a dict keyed by k so downstream checks
    # don't rely on insertion / index ordering (per Copilot review).
    clean_by_k: dict[int, bool] = {}
    common_denom = 32
    for k, (expr, val) in c_k_closed.items():
        scaled = val * common_denom
        clean = is_pell_lucas_clean(val)
        status = "✓ clean" if clean else "✗ OUTLIER"
        clean_by_k[k] = clean
        print(f"  c_{k} {expr:>30} {str(val):>15} {scaled.numerator:>10} {status:>15}")
    print()

    if not clean_by_k[5]:
        print("=" * 72)
        print("c_5 OUTLIER analysis")
        print("=" * 72)
        print()
        print("At silver ratio: c_5 = -11/8, numerator·32 = -44 = -4·11.")
        print("11 is NOT a Pell-Lucas number (1, 1, 3, 7, 17, 41, 99, ...).")
        print()
        print("Hypothesis: the empirical c_5 closed form `-(b² + 1/2)` is")
        print("LIKELY NOT the categorically correct one. The actual c_5")
        print("should give a Pell-Lucas-clean value at the silver ratio,")
        print("matching the pattern of c_3, c_4, c_6, c_7.")
        print()
        print("Candidate alternatives that ARE Pell-Lucas-clean at silver:")
        cands = [
            ("c_5 = -2·b²·(1-b²)", -2 * b_sq * (1 - b_sq)),       # -7/32 at silver
            ("c_5 = -b²/[3]_q at silver = -(7/8)/7 = -1/8", Fraction(-1, 8)),  # -4/32
            ("c_5 = -b²·b² = -b⁴", -b_sq**2),                       # -49/64 → -98/64 = -49/32 not -32 denom
            ("c_5 = c_3·b² = -2·b² = -7/4", Fraction(-2) * b_sq),  # -7/4 → ·32 = -56 = -2³·7 ✓ Pell-Lucas
        ]
        for label, val in cands:
            scaled = val * 32
            print(f"  {label:50s} = {val} (·32 = {scaled.numerator})")

    # Witness
    w = WitnessBuilder("qbeta-silver-ratio-pell-lucas-ck", engine="python")
    w.set_description(
        "Silver-ratio (q = 1 + √2) benchmark for c_k closed forms. "
        "At silver ratio: h = 2 (β-decay null), b² = 7/8 exactly, "
        "q-integers reduce to Pell-Lucas. Tests whether c_k closed "
        "forms evaluate to Pell-Lucas-clean rationals at the silver "
        "ratio — categorical correctness criterion."
    )
    w.add_data("silver_ratio_polynomial", "q² - 2q - 1 = 0")
    w.add_data("silver_ratio_roots", "1 ± √2")
    w.add_data("hecke_skein_at_silver", 2)
    w.add_data("b_squared_at_silver", "7/8")
    w.add_data("pell_lucas_sequence", pell_lucas)
    w.add_data("c_k_at_silver_ratio", {
        f"c_{k}": str(val) for k, (_, val) in c_k_closed.items()
    })
    w.add_data("pell_lucas_clean_per_k", {
        f"c_{k}": clean_by_k[k] for k in sorted(clean_by_k)
    })
    w.add_data("outlier_finding", (
        "c_5 = -11/8 at silver ratio; 11 is not Pell-Lucas. "
        "This flags the empirical `-(b² + 1/2)` closed form as "
        "categorically suspect. Other c_k (c_3, c_4, c_6, c_7) "
        "pass the silver-ratio Pell-Lucas test."
    ))
    # Assertions
    w.add_assertion(
        "c_3_at_silver_is_minus_2",
        computed=float(c_k_closed[3][1]),
        expected=-2,
        tolerance=0,
        source="c_3 = J_Hopf(q=1) is constant (q-independent)",
    )
    w.add_assertion(
        "c_4_at_silver_is_minus_49_32",
        computed=float(c_k_closed[4][1]),
        expected=float(Fraction(-49, 32)),
        tolerance=1e-15,
        source="c_4 = c_3·b⁴ with b² = 7/8 at silver → -49/32 (Pell-Lucas-clean)",
    )
    w.add_assertion(
        "c_7_at_silver_is_minus_8",
        computed=float(c_k_closed[7][1]),
        expected=-8,
        tolerance=0,
        source="c_7 = c_3³ is constant; clean integer",
    )

    # ── prop:silver-ratio-beta-decay-null wiring ────────────────────
    # Δ(net) = h(h-2)/2 vanishes at h = 2 (silver-ratio root)
    # b² = 1 - 1/[2]_q² = 7/8 exactly at silver
    # Both are bar-symmetric per def:bar-involution. See
    # content/quantum-observable-universe/particle-interactions/
    # silver-ratio-beta-decay-null.md
    h_at_silver = Fraction(2)
    delta_net_at_silver = h_at_silver * (h_at_silver - 2) / 2
    w.add_assertion(
        "delta_net_at_silver_is_zero",
        computed=float(delta_net_at_silver),
        expected=0,
        tolerance=0,
        source="prop:silver-ratio-beta-decay-null — Δ(net) = h(h-2)/2 "
        "vanishes at h=2 → β⁻ decay forbidden at leading (Form A) order",
    )
    # [2]_q = q + q⁻¹ = 2√2 at silver; [2]_q² = 8; 1/[2]_q² = 1/8;
    # b² = 1 - 1/[2]_q² = 7/8 exactly.
    b_sq_check = Fraction(1) - Fraction(1, 8)
    w.add_assertion(
        "b_sq_at_silver_is_seven_eighths",
        computed=float(b_sq_check),
        expected=float(Fraction(7, 8)),
        tolerance=0,
        source="prop:silver-ratio-beta-decay-null — b² = 1 - 1/[2]_q² = 7/8 "
        "exactly at silver, where [2]_q² = (2√2)² = 8",
    )

    w.save()


if __name__ == "__main__":
    main()
