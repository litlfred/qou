#!/usr/bin/env python3
"""GAP-A-4 T5 probe — candidate-functor search for the s5-so3-fiber-action h⁴ gap.

After T4 closed `conj:s5-so3-fiber-action` claim (2) (ℓ=2 → H icosahedral
matching on 5 strands at q=1), the original framing of claim (3) — `h⁴ = −3/4`
as a bounded computation on (3,2)+(2,2,1) Wedderburn contributions in
h = q − q⁻¹ — turned out to be **wrong**.  Per the 2026-06-01 audit
`docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md`:

  - `h⁴ = −3/4` lives on H_3(q), as the (2,1)/std irrep contribution to
    `tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h²+4)` on 3 strands.
  - `ℓ=2 → H` lives on A_5 ⊂ S_5 ≅ I, on 5 strands.
  - These live in DIFFERENT group algebras (S_3 vs S_5).  The open object
    is the categorical FUNCTOR linking them — supplying a normalisation that
    sends H-amplitude ↦ (2,1)-coefficient would be the empirical-fit the
    discipline review catches.
  - Further: dim_q((3,2)) = dim_q((2,2,1)) = [5]_q is SYMMETRIC under
    q ↔ q⁻¹, so a bar-odd h⁴ leading-order claim on these blocks is
    structurally malformed.

T5 tests three concrete candidate functors that, if any worked, would
constitute the missing categorical map.  The expectation per the audit
is that none of them work; the value of the probe is in PINNING DOWN
which candidates fail and HOW, so the open object's shape sharpens.

Candidates tested:

  F1.  S_5 → S_3 Young's branching restriction.  Compute
       Res^{S_5}_{S_3}((3,2) ⊕ (2,2,1)) via two-step branching
       Res^{S_5}_{S_4} then Res^{S_4}_{S_3}.  Read off the (2,1) /
       standard multiplicity m_{(2,1)} and compute the naive transfer
       m_{(2,1)} · (−3/4) — check whether any natural normalisation
       (by dim_q, by Wenzl weight, by [5]_q/[3]_q) lands on the
       Borromean h⁴ coefficient −3/4 exactly.

  F2.  dim_q ratio transfer.  Compute
       `2 · [5]_q / [3]_q`'s h-expansion (where `[5]_q` is the common
       dim_q for both (3,2) and (2,2,1) and `[3]_q` is dim_q of (2,1)
       on S_3).  Read off the h⁴ coefficient; check whether it
       matches −3/4 via any natural rescaling.

  F3.  Wenzl-weight modulated transfer.  Compute the H_5(q) Wenzl
       weight y_{(3,2)} + y_{(2,2,1)} and the H_3(q) Wenzl weight
       y_{(2,1)} h-expansions; check whether the ratio carries the
       h⁴ = −3/4 signature.

Verdict expectation: all three are off by uncontrolled factors.
EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T5-candidate-functor-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402

# Centralised q=1-safe q-integer / dim_q helpers + Q_0_50DPS
# (addresses Gemini deduplication review on PR #1904).
from _gap_a4_qsafe import (  # noqa: E402
    Q_0_50DPS,
    dim_q_partition,
)

HERE = Path(__file__).resolve().parent


# ── Young's branching rule: Res^{S_n}_{S_{n-1}} V_λ = ⊕ V_μ ─────────


def removable_corners(lam: tuple) -> list:
    """Cells of λ whose removal yields a valid Young diagram.  Returns a
    list of (row, col) 1-indexed."""
    out = []
    rows = list(lam)
    n = len(rows)
    for i in range(n):
        # row i has rows[i] boxes.  cell (i+1, rows[i]) is removable iff
        # rows[i] > rows[i+1] (or i is last row)
        below = rows[i + 1] if i + 1 < n else 0
        if rows[i] > below:
            out.append((i + 1, rows[i]))
    return out


def remove_corner(lam: tuple, cell: tuple) -> tuple:
    """Return λ with cell (i, j) removed.  Drops trailing zeros."""
    rows = list(lam)
    rows[cell[0] - 1] -= 1
    while rows and rows[-1] == 0:
        rows.pop()
    return tuple(rows)


def restrict_sn_to_sn_minus_1(lam: tuple) -> list:
    """Young's branching: Res^{S_n}_{S_{n-1}} V_λ = ⊕ V_μ where μ ranges
    over removable corners.  Returns list of (μ, mult).  Each μ appears
    with multiplicity 1 in Young's rule."""
    return [(remove_corner(lam, c), 1) for c in removable_corners(lam)]


def restrict_s5_to_s3(lam_5: tuple) -> dict:
    """Compose Res^{S_5}_{S_4} then Res^{S_4}_{S_3}.  Returns dict
    {mu_3: total_multiplicity}."""
    s4_decomp = restrict_sn_to_sn_minus_1(lam_5)
    out = {}
    for mu_4, m4 in s4_decomp:
        for mu_3, m3 in restrict_sn_to_sn_minus_1(mu_4):
            out[mu_3] = out.get(mu_3, 0) + m4 * m3
    return out


# ── F1: Young's-branching candidate functor ─────────────────────────


def test_f1_youngs_branching(q_0: mp.mpf) -> dict:
    print("=" * 78)
    print("F1 — Young's-branching candidate functor S_5 → S_3 on (3,2)+(2,2,1)")
    print("=" * 78)
    blocks = [(3, 2), (2, 2, 1)]
    H3_REF = mp.mpf("-0.75")  # Borromean h⁴ coefficient
    total_mults = {}
    for lam in blocks:
        decomp = restrict_s5_to_s3(lam)
        print(f"  Res^{{S_5}}_{{S_3}}{lam} = "
              + " ⊕ ".join(f"{m}·V{mu}" for mu, m in decomp.items()))
        for mu, m in decomp.items():
            total_mults[mu] = total_mults.get(mu, 0) + m
    print(f"  Sum over blocks: "
          + " ⊕ ".join(f"{m}·V{mu}" for mu, m in total_mults.items()))
    m_std = total_mults.get((2, 1), 0)
    print(f"  Multiplicity of (2,1)/std irrep of S_3: {m_std}")
    naive_transfer = m_std * H3_REF
    print(f"  Naive transfer m·(−3/4) = {naive_transfer}")
    print(f"  Borromean h⁴ reference: {H3_REF}")
    # Test natural normalisations
    candidates = {
        "m_(2,1)": mp.mpf(m_std),
        "m_(2,1) · (−3/4) [naive transfer]": naive_transfer,
        "m_(2,1) / 4": mp.mpf(m_std) / 4,
        "(−3/4) / m_(2,1)": H3_REF / m_std if m_std else mp.mpf("nan"),
        "(−3/4) · dim_q((2,1))_3 / [dim_q((3,2))_5 + dim_q((2,2,1))_5]":
            H3_REF * dim_q_partition((2, 1), q_0)
            / (dim_q_partition((3, 2), q_0) + dim_q_partition((2, 2, 1), q_0)),
    }
    matches = []
    tol = mp.mpf("1e-6")
    for label, val in candidates.items():
        match = "✓ matches −3/4" if abs(val - H3_REF) < tol else ""
        print(f"    {label:<70} = {mp.nstr(val, 10):>15} {match}")
        if match:
            matches.append(label)
    return {
        "candidate": "F1 Young's branching S_5 → S_3",
        "decomposition": {str(k): v for k, v in total_mults.items()},
        "m_standard_irrep": m_std,
        "borromean_h4_ref": str(H3_REF),
        "candidate_normalisations_matching": matches,
        "verdict": (
            "no candidate normalisation hits −3/4 cleanly" if not matches
            else "candidate functor FOUND — review"
        ),
    }


# ── F2: dim_q ratio transfer ─────────────────────────────────────


def test_f2_dimq_ratio() -> dict:
    print()
    print("=" * 78)
    print("F2 — dim_q-ratio candidate functor: 2·[5]_q / [3]_q")
    print("=" * 78)
    # [5]_q in h: closed form via [5]_q = h⁴ + 5h² + 5
    # [3]_q in h: [3]_q = h² + 3
    # 2·[5]_q / [3]_q = 2·(h⁴ + 5h² + 5)/(h² + 3)
    # Polynomial division:
    #   h⁴ + 5h² + 5 = (h² + 3)(h² + 2) + (5 − 6) = (h² + 3)(h² + 2) − 1
    # so [5]_q/[3]_q = h² + 2 − 1/(h² + 3)
    #               = h² + 2 − (1/3)(1 − h²/3 + h⁴/9 − …)
    # ⇒ 2·[5]_q/[3]_q = 2h² + 4 − (2/3)(1 − h²/3 + h⁴/9 − …)
    #                 = (4 − 2/3) + (2 + 2/9)h² + (−2/27)h⁴ + …
    #                 = 10/3 + (20/9)h² − (2/27)h⁴ + …
    h4_coeff = mp.mpf(-2) / 27
    print("  Algebraic identity: [5]_q = h⁴ + 5h² + 5;  [3]_q = h² + 3")
    print("  Polynomial division: 2·[5]_q / [3]_q "
          "= 10/3 + (20/9)h² − (2/27)h⁴ + O(h⁶)")
    print(f"    h⁴ coefficient: {mp.nstr(h4_coeff, 10)} = −2/27")
    print(f"    Borromean reference: −3/4")
    ratio = h4_coeff / mp.mpf("-0.75")
    print(f"    Ratio (F2_h4) / (−3/4) = {mp.nstr(ratio, 10)}  "
          f"(= 8/81 — not a clean unit factor)")
    return {
        "candidate": "F2 dim_q ratio 2·[5]_q/[3]_q",
        "h4_coefficient": str(h4_coeff),
        "borromean_h4_ref": "-3/4",
        "ratio": str(ratio),
        "verdict": "off by uncontrolled factor 8/81 ≈ 0.099",
    }


# ── F3: Wenzl-weight ratio ───────────────────────────────────────


def wenzl_weight_at_h0(lam: tuple, n: int) -> mp.mpf:
    """At q=1 (h=0) the Wenzl weight reduces to y_λ(1) = d_λ²/n!
    (the Plancherel measure on S_n irreps).  Per
    `prop:borromean-markov-trace-closed-form`:
      - y_{(3)}(1)   = 1²/6 = 1/6
      - y_{(2,1)}(1) = 2²/6 = 4/6 = 2/3
      - y_{(1,1,1)}(1) = 1²/6 = 1/6
    On S_5: y_{(3,2)}(1) = 5²/120 = 25/120 = 5/24,
            y_{(2,2,1)}(1) = 5²/120 = 5/24.
    """
    from math import factorial
    # Hook-length formula for d_λ at q=1
    n_fact = factorial(n)
    d_lam = n_fact
    for h in hook_lengths(list(lam)):
        d_lam = d_lam // h
    return mp.mpf(d_lam) ** 2 / mp.mpf(n_fact)


def test_f3_wenzl_ratio(q_0: mp.mpf) -> dict:
    print()
    print("=" * 78)
    print("F3 — Wenzl-weight candidate functor at q=1")
    print("=" * 78)
    y_32 = wenzl_weight_at_h0((3, 2), 5)
    y_221 = wenzl_weight_at_h0((2, 2, 1), 5)
    y_21 = wenzl_weight_at_h0((2, 1), 3)
    print(f"  y_{{(3,2)}}(1)   = 5²/120 = 25/120 = 5/24 = {mp.nstr(y_32, 10)}")
    print(f"  y_{{(2,2,1)}}(1) = 5²/120 = 25/120 = 5/24 = {mp.nstr(y_221, 10)}")
    print(f"  y_{{(2,1)}}(1)   = 2²/6  = 4/6     = 2/3  = {mp.nstr(y_21, 10)}")
    naive_sum = y_32 + y_221
    ratio = naive_sum / y_21
    print(f"  (y_(3,2) + y_(2,2,1)) / y_(2,1) = (5/12) / (2/3) "
          f"= 5/8 = {mp.nstr(ratio, 10)}")
    print(f"  Borromean h⁴ reference: −3/4")
    # Is 5/8 related to 3/4 by a clean factor? 5/8 ÷ 3/4 = 5·4/(8·3) = 20/24 = 5/6
    relation = ratio / mp.mpf("0.75")
    print(f"  (Wenzl ratio) / (3/4 magnitude) = {mp.nstr(relation, 10)} = 5/6")
    return {
        "candidate": "F3 Wenzl-weight ratio at q=1",
        "y_(3,2)_at_1": str(y_32),
        "y_(2,2,1)_at_1": str(y_221),
        "y_(2,1)_at_1": str(y_21),
        "summed_ratio": str(ratio),
        "ratio_vs_3_4": str(relation),
        "verdict": "5/8 ≠ −3/4 in sign or magnitude — Wenzl-ratio "
                   "transfer fails to hit the Borromean coefficient",
    }


# ── main ───────────────────────────────────────────────────────────


def main():
    mp.mp.dps = 50
    w = WitnessBuilder("gap-a4-T5-candidate-functor-probe", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md")
    w.set_description(
        "GAP-A-4 T5 — candidate-functor probe for s5-so3-fiber-action "
        "h⁴ gap. Tests 3 candidate functors from 5-strand (3,2)+(2,2,1) "
        "H-icosahedral component → 3-strand (2,1)/std h⁴ = −3/4. "
        "Expected outcome per the 2026-06-01 audit: all candidates "
        "FAIL by uncontrolled factors, confirming the missing-functor gap."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    f1 = test_f1_youngs_branching(q_0)
    f2 = test_f2_dimq_ratio()
    f3 = test_f3_wenzl_ratio(q_0)

    w.add_data("F1_youngs_branching", f1)
    w.add_data("F2_dimq_ratio", f2)
    w.add_data("F3_wenzl_ratio", f3)

    matched = len(f1["candidate_normalisations_matching"]) > 0

    w.add_assertion(
        "F1_standard_irrep_multiplicity_is_four",
        computed=float(f1["m_standard_irrep"]),
        expected=4.0,
        tolerance=1e-10,
        source=(
            "Young's branching Res^{S_5}_{S_3}((3,2)+(2,2,1)) = "
            "V_{(3)} ⊕ 4·V_{(2,1)} ⊕ V_{(1,1,1)} — the (2,1) multiplicity "
            "is 4 by direct Pieri-like rule application."
        ),
    )

    synthesis = (
        "All three candidate functors FAIL to recover the Borromean h⁴ = −3/4 "
        "from the 5-strand (3,2)+(2,2,1) H-icosahedral component: "
        "(F1) Young's branching gives m_{(2,1)} = 4 with no natural "
        "normalisation hitting −3/4; "
        "(F2) the dim_q-ratio transfer 2·[5]_q/[3]_q has h⁴ coefficient "
        "−2/27, off by uncontrolled factor 8/81; "
        "(F3) the Wenzl-weight ratio y_{(3,2)}+y_{(2,2,1)} / y_{(2,1)} "
        "= 5/8 at q=1, off in both sign and magnitude. "
        "This CONFIRMS the 2026-06-01 audit's finding that no canonical "
        "categorical functor links the 5-strand A_5 fiber action to the "
        "3-strand H_3 Borromean Markov trace. The open object remains the "
        "categorical map identified by `conj:inter-nucleon-channel-color-tube` "
        "(K1) — the SO(3)/I level-ℓ functor on 5-strand color×nucleon space "
        "to a Wedderburn coefficient of H_3(q)."
    )
    if matched:
        synthesis = (
            "UNEXPECTED: a candidate functor in the F1/F2/F3 family "
            "matched −3/4 — review for empirical-fit risk before treating "
            "as a derivation."
        )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
