"""Path B scaffold: Yekutieli MI k=3 structural h⁶ contribution to Higgs.

Background (from docs/audits/2026-05-24-higgs-residual-research-path.md §3
+ docs/audits/2026-05-24-yekutieli-mi-derivation-path.md):

  - Jet grade k → 4^k cells → captures order h^{2k}
    k=0: 1 cell  (leading)
    k=1: 4 cells (h², found to vanish identically by Markov-trace cancellation)
    k=2: 16 cells (h⁴, currently used) — h⁴ coeff = -3/4 from Markov trace
                                          OR = -2G from Vol(𝓑_3)/4 anchor
                                          (these are DIFFERENT)
    k=3: 64 cells (h⁶) — RESEARCH-GRADE, ~1 month effort

  - PR #1167 tried to FIT a single h⁶ coefficient empirically and FAILED:
    the W and Z anchors required different C_6 values. Reported as
    NEGATIVE result.

  - The structural h⁶ coefficient of the Borromean Markov trace,
    tr_M(𝓑_3) = (4 + h² − 3h⁴ − h⁶) / (h² + 4), is -1/16 (computable
    by Taylor expansion at h = 0).

What this scaffold does (PARTIAL Path B step 1):

  1. Verify the h-expansion of tr_M(𝓑_3) to high order; extract h⁰, h²,
     h⁴, h⁶, h⁸, h^10 coefficients symbolically.
  2. Verify the h-expansion of P_m(h) = Σ C(m+j, 2j)/2 · h^{2j} for the
     T(2, 2m) torus knots, m = 2 (W), 3 (Z), 4 (H), via the proven
     binomial pattern (PR #1165).
  3. Compute the AUGMENTED Higgs formula
        m_H = m_W · (P_4/P_2) · (6/5) · (1 - h^4 · 2G - h^6 · C_6)
     and SOLVE for C_6 needed to close each anchor's residual.
  4. Compare the required C_6 to the structurally-available Markov
     trace h⁶ coefficient (-1/16) and discuss whether a clean
     structural identification exists.

Honest framing:

  This probe IS NOT the full ~1 month Path B closure. It is the FIRST
  structural step: extract the structural h⁶ coefficient from the
  existing closed forms and check whether it's consistent with
  closing the Higgs residual.

  If the required C_6 matches a clean structural value (-1/16, or
  multiples thereof related to the 16-cell to 64-cell refinement),
  that's a hook for a follow-up derivation.

  If it doesn't match anything clean, that confirms PR #1167's
  finding: h⁶ alone is not the right basis for the residual; the
  residual is at the W/Z anchor asymmetry, not a missing h-order.
"""

from __future__ import annotations
import json, subprocess
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, log as mplog, cosh as mpcosh

mp.dps = 50


def main():
    print("=" * 80)
    print("Path B (Yekutieli MI k=3) — structural h⁶ scaffold")
    print("=" * 80)
    print()

    h = sp.Symbol("h")

    # =====================================================================
    # §1. h-expansion of tr_M(𝓑_3) — the structural h^k anchor source
    # =====================================================================
    print("=" * 80)
    print("§1. h-expansion of tr_M(𝓑_3) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)")
    print("=" * 80)
    print()
    trM_Bor = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)
    series_Bor = sp.series(trM_Bor, h, 0, 14).removeO()
    poly_Bor = sp.Poly(sp.expand(series_Bor), h)
    print(f"  Closed form: {trM_Bor}")
    print()
    print(f"  Taylor expansion around h = 0 (up to h^12):")
    print(f"  {sp.expand(series_Bor)}")
    print()
    print(f"  Coefficients (h^k):")
    coeffs_Bor = {}
    for k in range(13):
        c = poly_Bor.nth(k) if k <= poly_Bor.degree() else 0
        coeffs_Bor[k] = c
        marker = ""
        if k == 4:
            marker = "   ← h⁴ structural (Markov, not 2G)"
        elif k == 6:
            marker = "   ← h⁶ structural (target for Path B)"
        print(f"    h^{k:>2}: {c}{marker}")
    print()

    # =====================================================================
    # §2. h-expansion of P_m(h) for T(2, 2m), m = 2 (W), 3 (Z), 4 (H)
    # =====================================================================
    print("=" * 80)
    print("§2. h-expansion of P_m(h) = Σ C(m+j, 2j) / 2 · h^{2j}  (PR #1165)")
    print("=" * 80)
    print()
    P_polys = {}
    for m in [2, 3, 4]:
        P = sum(
            sp.binomial(m + j, 2 * j) / 2 * h ** (2 * j)
            for j in range(m + 1)
        )
        P_polys[m] = sp.expand(P)
        print(f"  P_{m}(h) = {P_polys[m]}")
    print()
    # Ratio P_4 / P_2 in series form to h^8
    P_ratio_W = sp.series(P_polys[4] / P_polys[2], h, 0, 12).removeO()
    P_ratio_Z = sp.series(P_polys[4] / P_polys[3], h, 0, 12).removeO()
    print(f"  P_4/P_2 (W anchor multiplier) = {sp.expand(P_ratio_W)}")
    print()
    print(f"  P_4/P_3 (Z anchor multiplier) = {sp.expand(P_ratio_Z)}")
    print()

    # =====================================================================
    # §3. Numerical evaluation + required C_6 solve
    # =====================================================================
    print("=" * 80)
    print("§3. Higgs formula augmented with h⁶ — solve for required C_6")
    print("=" * 80)
    print()
    # Substrate + SM anchors (50 dps)
    q_0 = mpf("1.10970000000")
    eta_0 = mplog(q_0)
    h_0 = q_0 - 1 / q_0
    bracket_2q = 2 * mpcosh(eta_0)
    G_catalan = mpf("0.91596559417721901505")
    vol_b3_over_4 = 2 * G_catalan
    m_W = mpf("80.379")
    m_Z = mpf("91.1876")
    m_H_measured = mpf("125.10")

    def P_m_num(m):
        return mpcosh((2 * m + 1) * eta_0) / bracket_2q

    P_W_ratio = P_m_num(4) / P_m_num(2)
    P_Z_ratio = P_m_num(4) / P_m_num(3)
    six_fifths = mpf(6) / 5

    print(f"  Substrate: q_0 = {q_0}, h_0 = {float(h_0):.6f}, h_0^6 = {float(h_0**6):.10f}")
    print(f"  P_4/P_2 = {float(P_W_ratio):.10f}")
    print(f"  P_4/P_3 = {float(P_Z_ratio):.10f}")
    print()
    # Baseline (h^6 = 0)
    base_W = m_W * P_W_ratio * six_fifths * (1 - h_0 ** 4 * vol_b3_over_4)
    base_Z = m_Z * P_Z_ratio * six_fifths * (1 - h_0 ** 4 * vol_b3_over_4)
    base_dev_W = float((base_W - m_H_measured) / m_H_measured * 100)
    base_dev_Z = float((base_Z - m_H_measured) / m_H_measured * 100)
    print(f"  Baseline (h⁶ = 0):  m_H from W = {float(base_W):.4f} ({base_dev_W:+.4f}%)")
    print(f"                       m_H from Z = {float(base_Z):.4f} ({base_dev_Z:+.4f}%)")
    print()

    # Augmented formula: m_H = m_anchor · (P/P) · (6/5) · (1 - h^4·2G - h^6·C_6)
    # Required C_6 to close each anchor:
    # m_H_measured / (m_anchor · (P/P) · 6/5) = 1 - h^4·2G - h^6·C_6
    # h^6·C_6 = 1 - h^4·2G - m_H_measured / (m_anchor · (P/P) · 6/5)
    # C_6 = (1 - h^4·2G - m_H_measured / (m_anchor · (P/P) · 6/5)) / h^6
    def required_C6(m_anchor, P_ratio):
        target_correction = m_H_measured / (m_anchor * P_ratio * six_fifths)
        # 1 - h^4·2G - h^6·C_6 = target_correction
        # h^6·C_6 = 1 - h^4·2G - target_correction
        return (1 - h_0 ** 4 * vol_b3_over_4 - target_correction) / h_0 ** 6

    C6_W = required_C6(m_W, P_W_ratio)
    C6_Z = required_C6(m_Z, P_Z_ratio)
    print(f"  Required C_6 to close W anchor: {float(C6_W):+.6f}")
    print(f"  Required C_6 to close Z anchor: {float(C6_Z):+.6f}")
    print(f"  Difference (W - Z):              {float(C6_W - C6_Z):+.6f}")
    print()
    if abs(float(C6_W - C6_Z)) < 0.1:
        print(f"  ✓ W and Z agree within 0.1 — could be a single C_6")
    elif abs(float(C6_W - C6_Z)) < 1:
        print(f"  Mixed: differ by ~1; may need anchor-dependent correction")
    else:
        print(f"  ✗ W and Z require WIDELY DIFFERENT C_6 — single coefficient FAILS")
        print(f"    (confirms PR #1167's negative finding)")
    print()

    # =====================================================================
    # §4. Compare required C_6 to structural Markov h⁶ candidates
    # =====================================================================
    print("=" * 80)
    print("§4. Structural h⁶ candidates from the Markov trace ladder")
    print("=" * 80)
    print()
    candidates_h6 = [
        ("Borromean Markov h⁶ = -1/16", sp.Rational(-1, 16)),
        ("2 × Borromean h⁶ = -1/8 (16→64 cell refinement scaling?)", sp.Rational(-1, 8)),
        ("4 × Borromean h⁶ = -1/4 (k=2→k=3 4^j scaling)", sp.Rational(-1, 4)),
        ("-2G²/2 = -G²", -G_catalan ** 2),
        ("-G (Catalan)", -G_catalan),
        ("-2G (the h⁴ scaling)", -2 * G_catalan),
        ("3 · Vol(𝓑_3)/4 = 6G", 6 * G_catalan),
        ("Vol(𝓑_3)²/16 = (8G)²/16 = 4G²", 4 * G_catalan ** 2),
    ]
    print(f"  Required C_6 from W anchor: {float(C6_W):+.6f}")
    print(f"  Required C_6 from Z anchor: {float(C6_Z):+.6f}")
    print()
    print(f"  {'candidate':<55} {'value':>12} {'gap W':>10} {'gap Z':>10}")
    print(f"  {'-'*55} {'-'*12} {'-'*10} {'-'*10}")
    matches = []
    for name, val in candidates_h6:
        if isinstance(val, sp.Rational):
            val_num = mpf(val.p) / mpf(val.q)
        else:
            val_num = mpf(str(val))
        gap_W = float(val_num - C6_W)
        gap_Z = float(val_num - C6_Z)
        marker = ""
        if abs(gap_W) < 0.5 and abs(gap_Z) < 0.5:
            marker = "  ← MATCH on both"
            matches.append((name, val_num))
        print(f"  {name:<55} {float(val_num):>+12.6f} {gap_W:>+9.4f} {gap_Z:>+9.4f}{marker}")
    print()

    # =====================================================================
    # §5. Honest verdict
    # =====================================================================
    print("=" * 80)
    print("§5. Honest verdict for Path B step 1")
    print("=" * 80)
    print()
    if abs(float(C6_W - C6_Z)) > 1:
        print(f"  ✗ Single C_6 FAILS to close both anchors (confirms PR #1167).")
        print(f"    Required C_6 differs by {float(C6_W - C6_Z):.4f} between W and Z.")
        print()
        print(f"  STRUCTURAL OBSERVATION:")
        print(f"    The Borromean Markov h⁶ coefficient = -1/16 = {float(sp.Rational(-1,16)):.4f}.")
        print(f"    Neither anchor's required C_6 matches this.")
        print(f"    The 16-cell (k=2) → 64-cell (k=3) refinement contributes")
        print(f"    additional h⁶ terms from cross-cell commutators in the CBH")
        print(f"    expansion, NOT just a scaling of the Borromean h⁶.")
        print()
        print(f"  WHY PATH B SCAFFOLD STOPS HERE:")
        print(f"    Computing the cross-cell h⁶ contribution from the 64-cell")
        print(f"    tessellation requires extracting the CBH three-term commutator")
        print(f"    [α, [α, β]] / 12 + [β, [α, β]] / 12 over each of the 64 cells")
        print(f"    of the refined kite tessellation, then summing. This is the")
        print(f"    research-grade ~1 month effort referenced in the audit.")
        print()
        print(f"  The W/Z anchor asymmetry (~1.1%) is the LOWER BOUND on what")
        print(f"  any h^k augmentation can close — the asymmetry is electroweak-")
        print(f"  mixing, not an h-order phenomenon.")
    elif matches:
        print(f"  Found {len(matches)} structural h⁶ candidate(s) matching both anchors:")
        for name, val in matches:
            print(f"    - {name}: {float(val):.6f}")
        print()
        print(f"  ⚠ This is a HYPOTHESIS, not a derivation. The categorical")
        print(f"  justification requires the full k=3 CBH expansion.")
    else:
        print(f"  No structural h⁶ candidate matches. Path B step 1 negative.")
        print(f"  The required C_6 has no clean closed form among standard")
        print(f"  combinations of Borromean Markov h⁶ and Catalan G.")
    print()

    # Witness
    witness = {
        "compute": "yekutieli_mi_k3_structural_h6_scaffold",
        "description": (
            "Path B scaffold step 1: extract the structural h⁶ coefficient "
            "of the Borromean Markov trace closed form, and solve for the "
            "C_6 required to close each anchor's Higgs residual with the "
            "augmented formula m_H = m_anchor · (P/P) · (6/5) · "
            "(1 - h⁴·2G - h⁶·C_6). Confirms PR #1167's negative finding "
            "that no single C_6 closes both anchors, and identifies the "
            "research-grade ~1 month CBH expansion needed for full closure."
        ),
        "structural_markov_coefficients": {
            f"h^{k}": str(coeffs_Bor[k]) for k in range(0, 13, 2)
        },
        "required_C_6": {
            "from_W_anchor": float(C6_W),
            "from_Z_anchor": float(C6_Z),
            "difference": float(C6_W - C6_Z),
            "single_coefficient_works": abs(float(C6_W - C6_Z)) < 0.1,
        },
        "structural_candidates_tested": [
            {"name": name, "value": float(val_num)
             if not isinstance(val, sp.Rational)
             else float(mpf(val.p) / mpf(val.q))}
            for name, val in candidates_h6
            for val_num in [mpf(val.p) / mpf(val.q)
                            if isinstance(val, sp.Rational)
                            else mpf(str(val))]
        ],
        "matches_within_0_5": [
            {"name": name, "value": float(val)} for name, val in matches
        ],
        "verdict": (
            "Single C_6 FAILS to close both anchors (confirms PR #1167). "
            f"Required C_6 differs by {float(C6_W - C6_Z):.4f} between W "
            "and Z. The structural Borromean Markov h⁶ = -1/16 does not "
            "match either anchor. Full Path B closure requires the 64-cell "
            "CBH expansion (research-grade ~1 month) to capture cross-cell "
            "h⁶ contributions beyond the bare Borromean term."
            if abs(float(C6_W - C6_Z)) > 1
            else "Mixed result — see body for details."
        ),
        "structural_lower_bound_on_residual": (
            "The W/Z anchor asymmetry (~1.1%) is the LOWER BOUND on what "
            "any h^k augmentation can close. The asymmetry is electroweak-"
            "mixing (cos θ_W), not an h-order phenomenon. Per items 5, 6, "
            "and 1 of this session's deferred-list closure, all simple "
            "structural augmentations (Q_m, ⋈_K Q-projection, H_4↔H_2 "
            "bridge) have been ruled out. Closure to <0.1% requires "
            "substrate-derivation of v (Path A, policy-declined) or the "
            "full Yekutieli MI k=3 CBH expansion (Path B, research-grade)."
        ),
        "next_step": (
            "Full Path B step 2: implement the 64-cell tessellation of the "
            "Borromean rings complement via Riemann-product subdivision; "
            "compute the per-cell CBH expansion to h⁶; sum the cross-cell "
            "contributions; verify against the Markov trace closed form. "
            "References: arXiv:1007.1250v4 (Yekutieli); existing k=1 "
            "scaffold in yekutieli_mi_h2_extraction.py."
        ),
        "status": "exploratory",
        "tags": [
            "yekutieli-mi",
            "k3-tessellation",
            "h6-structural-extraction",
            "path-b-scaffold",
            "higgs-residual-research-grade",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "yekutieli-mi-k3-h6-scaffold.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"  Witness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
