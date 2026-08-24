"""H_4(q) ↔ H_2(q) cross-algebra bridge — Path D from the Higgs residual audit.

Background.
  PR #1159 constructed the Higgs categorical mass formula
     m_H = m_W · (P_4(h)/P_2(h)) · (6/5) · (1 - h^4 · 2G)
  with empirical residuals -0.67% (W anchor) and +0.44% (Z anchor).
  PR #1167 NEGATIVE on h^6 single-coefficient closure.

  The 6/5 leading ratio is structurally identified as
     6/5  =  |S_3| / |partitions(4)|
  where |S_3| = 6 (group order = Σ d²_λ for λ ⊢ 3 = 1²+2²+1²) and
  |partitions(4)| = 5 (the 5 irreps of S_4: (4), (3,1), (2,2), (2,1,1),
  (1,1,1,1)).

  Path D from docs/audits/2026-05-24-higgs-residual-research-path.md:
    "The Higgs is T(2, 8) in B_2 (H_2(q)). But the FRAMEWORK's
     derivation of the 6/5 ratio uses H_4(q) (5 partitions). The
     bridge between H_2 and H_4 trace structures might supply the
     missing 0.5%."

This probe investigates the H_4(q) ↔ H_2(q) cross-algebra bridge
SYMBOLICALLY by:
  1. Tabulating Wedderburn dimensions for H_n(q) for n = 2, 3, 4, 5
  2. Computing branching multiplicities for the embedding chain
        S_2 ↪ S_3 ↪ S_4 ↪ S_5
     (the standard Young-tower inclusion)
  3. Searching for structural ratios involving 6, 5, and the residual
     ~1.00554 (=1/(1-0.00551) from W-anchor h^4 correction beyond the
     leading h^4·2G already in the formula)
  4. Testing whether including the bridge term as a multiplicative
     factor improves the residual

Honest framing.
  This probe is a STRUCTURAL SEARCH. Like item 5 (Q_m channel),
  the answer may be NEGATIVE (no clean bridge closes the residual)
  or POSITIVE (a structural multiplicative factor emerges with
  clear categorical meaning). Either outcome is honest.

  Constraint: we will NOT fit a free parameter. Any "bridge"
  candidate must be a fixed combinatorial expression (a partition
  count, a dimension ratio, a branching multiplicity).
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge
import json, subprocess
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, log as mplog, cosh as mpcosh
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()


def partitions_of(n):
    """Generate all partitions of n in dominance order."""
    def gen(n, max_part):
        if n == 0:
            yield ()
            return
        for k in range(min(n, max_part), 0, -1):
            for rest in gen(n - k, k):
                yield (k,) + rest
    return list(gen(n, n))


def hook_length_product(lam):
    """∏ h_λ(box) for partition λ. Used in dim_S_n(λ) = n! / ∏ hooks."""
    n = sum(lam)
    # Build the Young diagram coordinates
    boxes = [(i, j) for i in range(len(lam)) for j in range(lam[i])]
    transpose = [[lam[i] > j for i in range(len(lam))] for j in range(max(lam))]
    transpose_cols = [sum(1 for b in col if b) for col in transpose]
    prod = 1
    for (i, j) in boxes:
        # hook length: row-arm + col-leg + 1
        arm = lam[i] - j - 1
        leg = transpose_cols[j] - i - 1
        prod *= (arm + leg + 1)
    return prod


def dim_sn(lam):
    """Dimension of S_n irrep λ via hook-length formula."""
    n = sum(lam)
    n_factorial = sp.factorial(n)
    hp = hook_length_product(lam)
    return int(n_factorial // hp)


def main():
    print("=" * 80)
    print("H_4(q) ↔ H_2(q) cross-algebra bridge — Path D analysis")
    print("=" * 80)
    print()

    # =====================================================================
    # §1.  Wedderburn dimensions for H_n(q), n = 2..5
    # =====================================================================
    print("=" * 80)
    print("§1. Wedderburn dimensions for H_n(q) (= S_n at q = 1)")
    print("=" * 80)
    print()
    wedderburn = {}
    for n in range(2, 6):
        parts = partitions_of(n)
        dims = [(lam, dim_sn(lam)) for lam in parts]
        wedderburn[n] = dims
        n_factorial = int(sp.factorial(n))
        sum_d2 = sum(d ** 2 for _, d in dims)
        print(f"  H_{n}(q) Wedderburn  (|S_{n}| = n! = {n_factorial}):")
        for lam, d in dims:
            print(f"    λ = {lam}: dim = {d}")
        print(f"    Σ d² = {sum_d2}   (should = |S_{n}| = {n_factorial}: "
              f"{'✓' if sum_d2 == n_factorial else '✗'})")
        print(f"    # irreps = |partitions({n})| = {len(parts)}")
        print()

    # =====================================================================
    # §2.  The 6/5 ratio structural identification
    # =====================================================================
    print("=" * 80)
    print("§2. The 6/5 ratio — structural identification (PR #1159)")
    print("=" * 80)
    print()
    s3_card = int(sp.factorial(3))
    p4_card = len(partitions_of(4))
    p3_card = len(partitions_of(3))
    s4_card = int(sp.factorial(4))
    print(f"  Per PR #1159: 6/5 = |S_3| / |partitions(4)| = {s3_card}/{p4_card}")
    print(f"  Verify: |S_3| = {s3_card}, |partitions(4)| = {p4_card}, "
          f"ratio = {sp.Rational(s3_card, p4_card)}")
    print()
    print("  Other related ratios at the H_3 ↔ H_4 cross-level:")
    print(f"    |partitions(3)| / |partitions(4)| = {p3_card}/{p4_card} = "
          f"{sp.Rational(p3_card, p4_card)}")
    print(f"    |partitions(4)| / |partitions(3)| = {p4_card}/{p3_card} = "
          f"{sp.Rational(p4_card, p3_card)}")
    print(f"    |S_4| / |S_3| = {s4_card}/{s3_card} = "
          f"{sp.Rational(s4_card, s3_card)} = 4")
    print(f"    |S_3| / |S_4| = {s3_card}/{s4_card} = "
          f"{sp.Rational(s3_card, s4_card)} = 1/4")
    print()

    # =====================================================================
    # §3.  Branching multiplicities S_n ↑ S_{n+1} via Young's lattice
    # =====================================================================
    print("=" * 80)
    print("§3. Young-lattice branching S_n ↑ S_{n+1}")
    print("   (S_2 ↪ S_3 ↪ S_4 — standard inclusion via box-addition)")
    print("=" * 80)
    print()
    for n in [2, 3, 4]:
        print(f"  S_{n} ↪ S_{n+1}: each irrep λ ⊢ {n} lifts to all λ' ⊢ {n+1}")
        print(f"  obtained by adding ONE box to λ:")
        parts_n = partitions_of(n)
        parts_n1 = partitions_of(n + 1)
        for lam in parts_n:
            lifts = []
            for lam1 in parts_n1:
                # Check if lam1 is obtained from lam by adding one box
                # (i.e., lam1 ⊃ lam with |lam1| = |lam|+1)
                diff = 0
                valid = True
                lam_ext = list(lam) + [0] * (len(lam1) - len(lam))
                lam1_ext = list(lam1)
                # Pad both to same length
                maxlen = max(len(lam_ext), len(lam1_ext))
                lam_ext += [0] * (maxlen - len(lam_ext))
                lam1_ext += [0] * (maxlen - len(lam1_ext))
                for a, b in zip(lam_ext, lam1_ext):
                    if b < a:
                        valid = False
                        break
                    diff += b - a
                if valid and diff == 1:
                    # Confirm box-addition pattern
                    lifts.append(lam1)
            lifts_str = ", ".join(str(l) for l in lifts)
            print(f"    {lam} → {{{lifts_str}}}")
        print()

    # =====================================================================
    # §4.  Compute the Higgs residual at substrate and search for bridge
    #      candidates that match it.
    # =====================================================================
    print("=" * 80)
    print("§4. Searching for cross-algebra bridge that closes the residual")
    print("=" * 80)
    print()
    # Recompute residual from item 5 probe
    q_0 = mpf(Q_50_DIGIT_STR)
    # Was mpf("1.10970000000") -- a coarse pre-calibration literal, 251,000 ppb
    # (0.025 %) from BOTH live pins, i.e. ~22,000x the ~11.5 ppb mu-p substrate
    # tension. It was labelled "Substrate numerical value" and fed straight into
    # the tr_M / h_0 evaluation, so every number downstream of it was computed
    # at a q0 four orders of magnitude off the declared pin.
    eta_0 = mplog(q_0)
    h_0 = q_0 - 1 / q_0
    bracket_2q = 2 * mpcosh(eta_0)
    G_catalan = mpf("0.91596559417721901505")
    vol_b3_over_4 = 2 * G_catalan

    def P_m(m):
        return mpcosh((2 * m + 1) * eta_0) / bracket_2q

    P_dict = {m: P_m(m) for m in range(1, 6)}
    m_W = mpf("80.379")
    m_Z = mpf("91.1876")
    m_H_measured = mpf("125.10")

    m_H_W_baseline = m_W * (P_dict[4] / P_dict[2]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    m_H_Z_baseline = m_Z * (P_dict[4] / P_dict[3]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    dev_W = float((m_H_W_baseline - m_H_measured) / m_H_measured * 100)
    dev_Z = float((m_H_Z_baseline - m_H_measured) / m_H_measured * 100)

    # "Required correction" to close each anchor's residual:
    factor_W = float(m_H_measured / m_H_W_baseline)
    factor_Z = float(m_H_measured / m_H_Z_baseline)
    print(f"  Baseline residuals: W = {dev_W:+.4f}%, Z = {dev_Z:+.4f}%")
    print(f"  Required multiplier from baseline → measured:")
    print(f"    W: {factor_W:.6f} (anchor underestimates; need +{(factor_W-1)*100:+.4f}%)")
    print(f"    Z: {factor_Z:.6f} (anchor overestimates; need {(factor_Z-1)*100:+.4f}%)")
    print()
    print(f"  Mean factor: {(factor_W + factor_Z) / 2:.6f}")
    print(f"  W/Z asymmetry: {(factor_W - factor_Z) * 100:+.4f}%")
    print()

    # Bridge candidates: structural cross-algebra factors that might fit
    print("=" * 80)
    print("§5. Structural bridge candidates (no fitting)")
    print("=" * 80)
    print()
    print(f"  Required factor from W: {factor_W:.6f}")
    print(f"  Required factor from Z: {factor_Z:.6f}")
    print()
    print(f"  Bridge candidate                            value      W-gap%    Z-gap%")
    print(f"  ----------------------------------------- ---------- --------- ---------")
    candidates = [
        ("|partitions(3)|/|partitions(2)| = 3/2", sp.Rational(3, 2)),
        ("|partitions(4)|/|partitions(3)| = 5/3", sp.Rational(5, 3)),
        ("|partitions(5)|/|partitions(4)| = 7/5", sp.Rational(7, 5)),
        ("|S_3|/|partitions(4)| = 6/5", sp.Rational(6, 5)),
        ("|S_3|·|partitions(3)|/|S_4|/|partitions(4)| = 18/120 = 3/20", sp.Rational(3, 20)),
        ("dim_S4(2,2) / dim_S3(2,1) = 2/2 = 1", sp.Rational(1, 1)),
        ("dim_S4(3,1) / dim_S3(3) = 3/1 = 3", sp.Rational(3, 1)),
        ("1 + 1/|partitions(4)| = 1 + 1/5 = 6/5", sp.Rational(1) + sp.Rational(1, 5)),
        ("1 + 1/|partitions(5)| = 1 + 1/7 = 8/7", sp.Rational(1) + sp.Rational(1, 7)),
        ("1 + h_0^4 = 1 + (q-1/q)^4 (sub-leading correction)", None),
        ("1 + h_0^6", None),
    ]
    structural_matches = []
    for name, val in candidates:
        if val is None:
            if "h_0^4" in name:
                val_mp = mpf("1") + h_0 ** 4
            elif "h_0^6" in name:
                val_mp = mpf("1") + h_0 ** 6
            else:
                val_mp = mpf("1")
        else:
            val_mp = mpf(int(val.p)) / mpf(int(val.q))
        gap_W = float((val_mp - factor_W) * 100)
        gap_Z = float((val_mp - factor_Z) * 100)
        match = ""
        if abs(gap_W) < 0.5 and abs(gap_Z) < 0.5:
            match = "  ← potential match"
            structural_matches.append((name, float(val_mp)))
        print(f"  {name:<42} {float(val_mp):>10.6f} {gap_W:+8.4f}%  {gap_Z:+8.4f}%{match}")
    print()

    # =====================================================================
    # §6.  Honest verdict
    # =====================================================================
    print("=" * 80)
    print("§6. Honest verdict")
    print("=" * 80)
    print()
    if structural_matches:
        print(f"  Found {len(structural_matches)} structural candidate(s)")
        print(f"  within 0.5% of the required factor for both anchors:")
        for name, val in structural_matches:
            print(f"    - {name}: {val:.6f}")
        print()
        print("  These are CANDIDATES, not derivations. A categorical")
        print("  justification is required before any could be admitted")
        print("  into the production formula.")
    else:
        print("  ✗ NO structural candidate within 0.5% of the required")
        print("    factor for BOTH anchors.")
        print()
        print("  Implication: a SIMPLE cross-algebra multiplicative factor")
        print("  (counting partitions, group orders, etc.) does NOT close")
        print("  the residual. The bridge — if it exists — must be more")
        print("  subtle (e.g. an h-dependent factor, or a branching-multiplicity")
        print("  sum, not a single ratio).")
        print()
        print("  Cross-reference: Path A (substrate v) and Path B (Yekutieli")
        print("  k=3) remain the more plausible closure paths per the")
        print("  Higgs residual audit.")
    print()

    # =====================================================================
    # §7.  W/Z anchor asymmetry isolated structurally
    # =====================================================================
    print("=" * 80)
    print("§7. The W/Z anchor asymmetry (~1.11%) is the fundamental obstruction")
    print("=" * 80)
    print()
    print(f"  W-anchor m_W/m_Z required for prediction agreement:")
    # From higgsMassFormula matching higgsMassFromZ:
    #   m_W · (P_4/P_2) = m_Z · (P_4/P_3)   ⇒   m_W/m_Z = P_2/P_3
    expected_WZ = float(P_dict[2] / P_dict[3])
    observed_WZ = float(m_W / m_Z)
    print(f"    expected:  P_2/P_3 at substrate = {expected_WZ:.6f}")
    print(f"    observed:  m_W/m_Z (PDG)         = {observed_WZ:.6f}")
    print(f"    ratio:     {observed_WZ/expected_WZ:.6f}")
    print(f"    gap:       {(observed_WZ - expected_WZ)/expected_WZ*100:+.4f}%   (relative)")
    print()
    print("  → The W/Z anchor asymmetry IS the residual.")
    print("    Per Path A: this gap reflects the SM electroweak mixing")
    print("    (cos θ_W ≠ exact substrate ratio), which the H_2(q) trace")
    print("    formula alone does not capture. Closure requires substrate")
    print("    derivation of v (declined 2026-05-08 by policy).")
    print()

    # Witness
    witness = {
        "compute": "h4_h2_cross_algebra_bridge_probe",
        "description": (
            "Investigates the H_4(q) ↔ H_2(q) cross-algebra bridge "
            "(Path D from the Higgs residual audit). Tabulates Wedderburn "
            "dimensions, branching multiplicities for S_2 ↪ S_3 ↪ S_4, "
            "and searches for a structural multiplicative factor that "
            "closes the ~0.5% residual without fitting."
        ),
        "wedderburn_dimensions": {
            f"H_{n}": {str(lam): d for lam, d in wedderburn[n]}
            for n in range(2, 6)
        },
        "partition_counts": {
            f"|partitions({n})|": len(partitions_of(n))
            for n in range(2, 6)
        },
        "six_fifths_identification": {
            "ratio": "6/5",
            "numerator": f"|S_3| = {s3_card}",
            "denominator": f"|partitions(4)| = {p4_card}",
            "source": "PR #1159 categorical Higgs mass formula",
        },
        "baseline_residuals": {
            "W_anchor_deviation_percent": dev_W,
            "Z_anchor_deviation_percent": dev_Z,
            "required_factor_W": factor_W,
            "required_factor_Z": factor_Z,
            "WZ_asymmetry_percent": float((m_H_Z_baseline - m_H_W_baseline) /
                                          m_H_W_baseline * 100),
        },
        "structural_candidates_searched": [name for name, _ in candidates],
        "candidates_within_0_5_percent": [
            {"name": name, "value": val} for name, val in structural_matches
        ],
        "verdict": (
            f"Found {len(structural_matches)} structural candidates within "
            f"0.5% of required factor" if structural_matches
            else "NO structural cross-algebra factor within 0.5% of required; "
                 "Path D as a SINGLE multiplicative bridge FAILS. The W/Z "
                 "anchor asymmetry IS the residual; closure requires Path A "
                 "(substrate v derivation, policy-declined) or Path B "
                 "(Yekutieli MI k=3 tessellation, ~1 month research)."
        ),
        "fundamental_obstruction": (
            "Higgs prediction consistency requires m_W/m_Z = P_2/P_3 "
            "(from PR #1159 theorem higgs_W_Z_predictions_consistent_hypothesis). "
            f"Observed m_W/m_Z = {float(m_W/m_Z):.6f}; "
            f"predicted P_2/P_3 = {expected_WZ:.6f}; "
            f"relative gap = {(float(m_W/m_Z) - expected_WZ)/expected_WZ*100:.4f}%. "
            "This ~1.1% gap IS the W/Z anchor asymmetry seen as the Higgs "
            "residual — reflecting SM electroweak mixing not in the H_2(q) "
            "trace formula."
        ),
        "status": "exploratory",
        "tags": [
            "h4-h2-cross-algebra-bridge",
            "higgs-residual-path-d",
            "wedderburn-branching",
            "structural-search-no-fit",
            "WZ-anchor-asymmetry",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "h4-h2-cross-algebra-bridge-probe.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"  Witness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
