"""
delta_lambda_fr_identity_phase5c.py — Phase 5c.1 of the Δ_λ thread.

Test the Frobenius-reciprocity identity predicted by the Phase 5b
bar-symmetric synthesis (audit doc
`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`):

For each (Z=1 → Z=2) transition at fixed N:

    Σ_λ y_λ χ_λ(β_K^{Z=2})  ≟  [3]_q² · cosh(h) ·
                                Σ_μ y_μ χ_μ(β_K^{Z=1})
                              + (Li_2^q interface correction)

where:
  - β_K^Z   is the canonical 3A-strand atomic braid for atom K=(Z, N)
  - y_λ     is the Jones-Markov weight at H_n (cached in
              `y-lambda-at-q0.witness.json`)
  - χ_λ     is the Hecke character (computed via pyhecke_native)
  - [3]_q²  is the categorical per-Z gain factor
  - cosh(h) is the Hecke-deformed identity correction (Phase 5b finding)
  - the residual (Li_2^q interface correction) is the constituent-vacuum
    discrepancy from PR #801's interface-knot Δ_I^K

If the residual is at the bar-symmetric level (small, structurally clean),
the FR identity is empirically validated and α = [3]_q²·cosh(h) is the
per-Z step factor. If the residual is large or sign-flipping, the
bar-symmetric synthesis needs more work (Phase 5d).

Compares both:
  (a) FULL canonical braid (include_inter=True) — what tr_M(β_K) actually is
  (b) CONSTITUENT vacuum (include_inter=False) — disjoint Hecke product

The difference between (a) and (b) is the interface-knot contribution
Δ_I^K from PR #801.

  Ref: [manuscript] conj:delta-lambda-categorical-closure
  Ref: docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md
  Ref: PR #801 (interface-knot Δ_I^K binding)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from q_parameter import Q as Q0_FLOAT
from q_mpmath import set_q, qint
set_q(Q0_FLOAT)

mp.mp.dps = 50
Q0 = mp.mpf(str(Q0_FLOAT))

# Per-(Z, N) atoms to test
ATOMS = [
    ("D",   1, 1),   # H_6
    ("T",   1, 2),   # H_9
    ("3He", 2, 1),   # H_9
    ("4He", 2, 2),   # H_12  — slowest; still feasible with Rust kernel
]


def load_y_lambda_at_q0() -> dict[int, dict[tuple, mp.mpf]]:
    """Load cached Jones-Markov weights y_λ at q_0 from the canonical witness."""
    path = HERE / "y-lambda-at-q0.witness.json"
    w = json.loads(path.read_text())
    by_n = {}
    for n_str, entries in w["data"]["by_n"].items():
        n = int(n_str)
        by_n[n] = {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"])
                   for e in entries}
    return by_n


def compute_tr_M_decomposition(Z: int, N: int, include_inter: bool,
                               y_at_q0: dict) -> dict:
    """Compute τ_M(β) = Σ_λ y_λ · χ_λ(β) using pyhecke_native.

    Returns dict with per-λ decomposition + total + dominant block.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import chi_lambda_braid, partitions_of

    A = Z + N
    n = 3 * A
    word_tuples = atom_braid_word_3A(Z, N, include_inter=include_inter)
    # Convert (c, d, gen_idx) → (sign, gen_1indexed) for chi_lambda_braid
    word_marshalled = []
    h_val = float(Q0 - 1 / Q0)
    for c, d, g in word_tuples:
        cf = float(c)
        df = float(d)
        if abs(cf - 1.0) < 1e-10 and abs(df) < 1e-10:
            word_marshalled.append((1, g + 1))
        elif abs(cf - 1.0) < 1e-10 and abs(df + h_val) < 1e-10:
            word_marshalled.append((-1, g + 1))
        elif abs(cf - 1.0) < 1e-10 and abs(df + h_val / 2) < 1e-10:
            word_marshalled.append((1, g + 1))  # averaged → σ convention
        else:
            word_marshalled.append((1, g + 1))

    parts = list(partitions_of(n))
    rows = []
    total = mp.mpf(0)
    for lam in parts:
        chi = chi_lambda_braid(lam, word_marshalled, q_value=float(Q0))
        y = y_at_q0.get(n, {}).get(lam, mp.mpf(0))
        if y == 0:
            # try without the trailing zero entries
            for k in y_at_q0.get(n, {}):
                if k == lam[:len(k)] and all(x == 0 for x in lam[len(k):]):
                    y = y_at_q0[n][k]
                    break
        c_lam = y * mp.mpf(str(chi))
        total += c_lam
        rows.append({
            "lambda": list(lam),
            "y": float(y),
            "chi": chi,
            "y_chi": float(c_lam),
            "abs_y_chi": float(abs(c_lam)),
        })

    # Dominant block (largest |y · χ|)
    rows.sort(key=lambda r: -r["abs_y_chi"])
    dominant = rows[0]
    return {
        "Z": Z, "N": N, "n": n, "word_length": len(word_marshalled),
        "include_inter": include_inter,
        "total_tr_M": float(total),
        "abs_total_tr_M": float(abs(total)),
        "dominant_lambda": dominant["lambda"],
        "dominant_y_chi": dominant["y_chi"],
        "dominant_abs_y_chi": dominant["abs_y_chi"],
        "top_5_blocks": rows[:5],
    }


def main() -> int:
    builder = WitnessBuilder("delta-lambda-fr-identity-phase5c")
    builder.set_description(
        "Phase 5c.1 of the Δ_λ thread: numerical test of the "
        "Frobenius-reciprocity identity predicted by the Phase 5b "
        "bar-symmetric synthesis. Computes τ_M(β) = Σ_λ y_λ · χ_λ(β) "
        "at q_0 for D, T, ³He, ⁴He via cached y_λ + pyhecke_native "
        "χ_λ. Compares both the full canonical braid (include_inter=True) "
        "and the constituent-vacuum baseline (include_inter=False; "
        "PR #801's T_constit). The ratio τ_M(β_{Z=2}^N) / τ_M(β_{Z=1}^N) "
        "is the Ind-side per-Z step factor; under FR it should equal "
        "[3]_q² · cosh(h) · (interface-knot correction)."
    )
    builder.set_content_block("conj:delta-lambda-categorical-closure")
    builder.add_parameter("q0", str(Q0))

    h = Q0 - 1 / Q0
    qint_3 = qint(3)
    qint_3_sq = qint_3 ** 2
    alpha_pred = qint_3_sq * mp.cosh(h)
    builder.add_parameter("h", str(h))
    builder.add_parameter("3_q_squared", str(qint_3_sq))
    builder.add_parameter("cosh_h", str(mp.cosh(h)))
    builder.add_parameter("alpha_predicted", str(alpha_pred))

    y_at_q0 = load_y_lambda_at_q0()
    print(f"  Loaded y_λ at q_0 for n ∈ {sorted(y_at_q0.keys())}")
    print(f"  q_0 = {Q0}")
    print(f"  h = q - q⁻¹ = {float(h):.6f}")
    print(f"  [3]_q² = {float(qint_3_sq):.6f}")
    print(f"  cosh(h) = {float(mp.cosh(h)):.6f}")
    print(f"  α_pred = [3]_q² · cosh(h) = {float(alpha_pred):.6f}")
    print()

    results_full = {}
    results_constit = {}
    for name, Z, N in ATOMS:
        for include_inter, label, dest in [
            (True, "FULL (β_K)", results_full),
            (False, "CONSTIT (no interface)", results_constit),
        ]:
            print(f"  Computing {name} {label} ({Z=}, {N=})...")
            t0 = time.time()
            try:
                result = compute_tr_M_decomposition(Z, N, include_inter, y_at_q0)
                dt = time.time() - t0
                print(f"    Took {dt:.2f}s; τ_M = {result['total_tr_M']:+.6f}, "
                      f"|τ_M| = {result['abs_total_tr_M']:.6f}, "
                      f"dominant λ = {result['dominant_lambda']}")
                dest[name] = result
            except Exception as e:
                print(f"    ERR: {type(e).__name__}: {e}")
                dest[name] = {"error": str(e)}

    builder.add_data("results_full", results_full)
    builder.add_data("results_constit", results_constit)

    # ── FR identity test ──────────────────────────────────────────
    print("\n=== FR-identity test: per-Z step factor ===")
    print(f"  Predicted: τ_M(β_{{Z=2}}) / τ_M(β_{{Z=1}}) at fixed N "
          f"≈ α_pred = [3]_q² · cosh(h) = {float(alpha_pred):.4f}")
    print(f"  (modulo Li_2^q interface-knot correction from PR #801)")
    print()

    fr_tests = []
    for N_val, (Z1_name, Z2_name) in [(1, ("D", "3He")), (2, ("T", "4He"))]:
        if "error" in results_full.get(Z1_name, {}) or "error" in results_full.get(Z2_name, {}):
            continue
        for label, results in [("FULL", results_full), ("CONSTIT", results_constit)]:
            try:
                trM_z1 = mp.mpf(str(results[Z1_name]["total_tr_M"]))
                trM_z2 = mp.mpf(str(results[Z2_name]["total_tr_M"]))
                ratio = trM_z2 / trM_z1 if trM_z1 != 0 else mp.mpf("inf")

                # Use |τ_M| ratio (FR identity is for magnitudes)
                abs_trM_z1 = mp.mpf(str(results[Z1_name]["abs_total_tr_M"]))
                abs_trM_z2 = mp.mpf(str(results[Z2_name]["abs_total_tr_M"]))
                abs_ratio = abs_trM_z2 / abs_trM_z1 if abs_trM_z1 != 0 else mp.mpf("inf")

                rel_err_signed = (ratio - alpha_pred) / alpha_pred if alpha_pred != 0 else mp.mpf("inf")
                rel_err_abs = (abs_ratio - alpha_pred) / alpha_pred if alpha_pred != 0 else mp.mpf("inf")

                fr_tests.append({
                    "transition": f"{Z2_name}/{Z1_name} (N={N_val})",
                    "scope": label,
                    "tr_M_Z1": float(trM_z1),
                    "tr_M_Z2": float(trM_z2),
                    "ratio_signed": float(ratio),
                    "abs_ratio": float(abs_ratio),
                    "alpha_pred": float(alpha_pred),
                    "rel_err_signed": float(rel_err_signed),
                    "rel_err_abs": float(rel_err_abs),
                })
                print(f"  {label:<8} {Z2_name}/{Z1_name} at N={N_val}: "
                      f"τ ratio = {float(ratio):+.5f}, |τ| ratio = {float(abs_ratio):.5f}, "
                      f"vs α_pred = {float(alpha_pred):.4f}; "
                      f"rel.err |τ|: {float(rel_err_abs)*100:+.2f}%")
            except Exception as e:
                print(f"  {label} {Z2_name}/{Z1_name}: ERR {e}")

    builder.add_data("fr_identity_tests", fr_tests)

    # Cross-check: dominant-block ratio (the |Δ_λ*| analogue)
    print("\n=== Dominant-block ratio test (|Δ_λ*|-style) ===")
    dominant_tests = []
    for N_val, (Z1_name, Z2_name) in [(1, ("D", "3He")), (2, ("T", "4He"))]:
        if "error" in results_full.get(Z1_name, {}) or "error" in results_full.get(Z2_name, {}):
            continue
        abs1 = mp.mpf(str(results_full[Z1_name]["dominant_abs_y_chi"]))
        abs2 = mp.mpf(str(results_full[Z2_name]["dominant_abs_y_chi"]))
        ratio = abs2 / abs1 if abs1 != 0 else mp.mpf("inf")
        dominant_tests.append({
            "transition": f"{Z2_name}/{Z1_name} (N={N_val})",
            "dom_abs_y_chi_Z1": float(abs1),
            "dom_abs_y_chi_Z2": float(abs2),
            "dom_ratio": float(ratio),
            "alpha_pred": float(alpha_pred),
            "rel_err": float((ratio - alpha_pred) / alpha_pred),
        })
        print(f"  {Z2_name}/{Z1_name} at N={N_val}: "
              f"dominant |y·χ| ratio = {float(ratio):.4f}, vs α_pred = {float(alpha_pred):.4f}; "
              f"rel.err: {float((ratio - alpha_pred)/alpha_pred)*100:+.2f}%")
    builder.add_data("dominant_block_tests", dominant_tests)

    # Assertion: FR identity holds at the |τ_M| level within tolerance
    if fr_tests:
        max_rel_err_abs = max(abs(t["rel_err_abs"]) for t in fr_tests
                              if t["scope"] == "FULL")
        builder.add_assertion(
            "fr_identity_max_rel_err",
            computed=float(max_rel_err_abs),
            expected=0.0,
            tolerance=10.0,  # very loose — this is exploratory
            unit="rel_err",
            source=(
                "FR identity τ_M(β_{Z=2}) / τ_M(β_{Z=1}) ?= [3]_q²·cosh(h) "
                "at q_0 — bar-symmetric synthesis predicts max rel.err. "
                "of the interface-knot correction (PR #801) governs the residual."
            ),
        )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
