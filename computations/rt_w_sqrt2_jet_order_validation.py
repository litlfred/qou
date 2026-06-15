"""Rigorous jet-order validation of W = √[2]_q claim.

User challenge (2026-05-24): "Is this proved formally? Are you sure
you have a hold of the factors? you check the complete GB filtration
and jet order"

Honest answer: NO. The √[2]_q W-correction in PR #1122 was a SCALAR
empirical fit at q_0, comparing only |J_N(T(2,k))| magnitudes. If the
correction is structurally correct, it must hold AT EVERY JET ORDER
of the h-expansion (h⁰, h², h⁴, h⁶, ...), not just the scalar value.

This probe is the rigorous check. For W = T(2,4), Z = T(2,6), H = T(2,8):

1. Compute |J_N(T(2,k))| at q values around q_0 to extract h-expansion
2. For each jet order (h^{2j}, j = 0..3), report the per-particle coefficient
3. Apply √[2]_q correction to W AT EACH ORDER
4. Check whether W/Z, W/H ratios match SM at EVERY order

**If √[2]_q holds at every order: structural confirmation.**
**If √[2]_q holds only at h⁰ (scalar): just coincidence at the substrate point.**

Status: EXPLORATORY — rigorous jet-order validation test.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpc, mpf

mp.mp.dps = 80  # Higher precision needed for jet-order extraction

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
M_E_MEV = mpf("0.510998950")
M_W_MEV = mpf("80379.0")
M_Z_MEV = mpf("91187.6")
M_H_MEV = mpf("125100.0")

RATIO_W_Z_EXP = M_W_MEV / M_Z_MEV
RATIO_W_H_EXP = M_W_MEV / M_H_MEV
RATIO_Z_H_EXP = M_Z_MEV / M_H_MEV


def quantum_integer(N: int, q):
    sq = mp.sqrt(q)
    sqi = mpf(1) / sq
    return (sq ** N - sqi ** N) / (sq - sqi)


def colored_jones_T2n(N: int, n: int, q) -> mpc:
    bracket_N = quantum_integer(N, q)
    if abs(bracket_N) < mpf("1e-60"):
        return mp.nan
    total = mpc(0)
    for j in range(N):
        exponent = mpf(n) * (N - 1 - 2 * j) * (N + 1 - 2 * j) / 4
        sign = (-1) ** j
        total += sign * q ** exponent
    return total / bracket_N


def extract_h_expansion(N: int, n: int, n_orders: int = 4) -> list:
    """Extract h-expansion coefficients of |J_N(T(2,n), q)| around q=1.

    h = q - q⁻¹. Expand: |J_N| = c_0 + c_2 h² + c_4 h⁴ + c_6 h⁶ + ...
    Returns coefficients c_{2j} for j = 0..n_orders-1.

    Method: sample at multiple small h values, fit polynomial.
    """
    n_samples = 2 * n_orders + 2  # over-sampled
    h_values = [mpf("0.005") * (i + 1) for i in range(n_samples)]
    samples = []
    for h_val in h_values:
        # q from h: q² - h·q - 1 = 0 → q = (h + √(h² + 4))/2
        q_val = (h_val + mp.sqrt(h_val ** 2 + 4)) / 2
        J = colored_jones_T2n(N, n, q_val)
        # take magnitude (real for real q)
        mag = abs(J) if isinstance(J, mpc) else abs(J)
        samples.append((h_val, mag))

    # Fit polynomial in h² (even-only expansion expected for even n)
    # |J_N|(h) = c_0 + c_2 h² + c_4 h⁴ + c_6 h⁶
    H = mp.matrix(n_samples, n_orders)
    R = mp.matrix(n_samples, 1)
    for i, (h_val, m) in enumerate(samples):
        for j in range(n_orders):
            H[i, j] = h_val ** (2 * j)
        R[i, 0] = m

    HT = H.T
    try:
        coeffs = mp.lu_solve(HT * H, HT * R)
        return [float(coeffs[j, 0]) for j in range(n_orders)]
    except Exception:
        return [None] * n_orders


def main():
    print("Rigorous jet-order validation of W = √[2]_q claim")
    print(f"80-dps mpmath; q_0 = {Q_0}")
    print("=" * 80)

    # √[2]_q at q_0
    bracket_2_q0 = abs(quantum_integer(2, Q_0))
    sqrt_bracket_2 = mp.sqrt(bracket_2_q0)
    print(f"\n√[2]_q at q_0 = {float(sqrt_bracket_2):.8f}")
    print(f"For comparison: √2 = {float(mp.sqrt(2)):.8f}")

    # Test at N = 2 (best ratio match per PR #1119)
    N = 2
    n_orders = 4  # h⁰, h², h⁴, h⁶

    print(f"\nExtracting h-expansion at N = {N} for W = T(2,4), Z = T(2,6), H = T(2,8):")
    print("=" * 80)

    coeffs_W = extract_h_expansion(N, 4, n_orders)
    coeffs_Z = extract_h_expansion(N, 6, n_orders)
    coeffs_H = extract_h_expansion(N, 8, n_orders)

    print(f"\n{'jet order':<12} {'W = T(2,4)':>16} {'Z = T(2,6)':>16} {'H = T(2,8)':>16}")
    print("-" * 65)
    for j in range(n_orders):
        print(f"{'h^{' + str(2*j) + '}':<12} {coeffs_W[j]:>+16.6f} {coeffs_Z[j]:>+16.6f} {coeffs_H[j]:>+16.6f}")

    # Now check ratios at EACH jet order, with and without √[2]_q correction
    print("\n" + "=" * 80)
    print("Per-jet-order ratios: WITH √[2]_q correction on W")
    print("=" * 80)
    print(f"{'jet':<8} {'W_corr':>14} {'W/Z':>10} {'SM W/Z':>10} {'dev %':>9} "
          f"{'Z/H':>10} {'SM Z/H':>10} {'dev %':>9} {'W/H':>10} {'SM W/H':>10} {'dev %':>9}")
    print("-" * 115)

    per_jet_results = []
    for j in range(n_orders):
        c_W = mpf(str(coeffs_W[j]))
        c_Z = mpf(str(coeffs_Z[j]))
        c_H = mpf(str(coeffs_H[j]))
        if c_Z == 0 or c_H == 0:
            print(f"h^{2*j:<5}    DIV-BY-ZERO at this order; skipping")
            per_jet_results.append({
                "jet_order": 2 * j,
                "coeff_W": float(c_W),
                "coeff_Z": float(c_Z),
                "coeff_H": float(c_H),
                "skipped_div_by_zero": True,
            })
            continue

        c_W_corr = c_W * sqrt_bracket_2
        # Ratios
        wz = float(c_W_corr / c_Z)
        zh = float(c_Z / c_H)
        wh = float(c_W_corr / c_H)

        d_wz = (wz - float(RATIO_W_Z_EXP)) / float(RATIO_W_Z_EXP) * 100
        d_zh = (zh - float(RATIO_Z_H_EXP)) / float(RATIO_Z_H_EXP) * 100
        d_wh = (wh - float(RATIO_W_H_EXP)) / float(RATIO_W_H_EXP) * 100

        print(f"h^{2*j:<5} {float(c_W_corr):>+14.4f} {wz:>10.4f} {float(RATIO_W_Z_EXP):>10.4f} "
              f"{d_wz:>+9.2f} {zh:>10.4f} {float(RATIO_Z_H_EXP):>10.4f} {d_zh:>+9.2f} "
              f"{wh:>10.4f} {float(RATIO_W_H_EXP):>10.4f} {d_wh:>+9.2f}")

        per_jet_results.append({
            "jet_order": 2 * j,
            "coeff_W": float(c_W),
            "coeff_Z": float(c_Z),
            "coeff_H": float(c_H),
            "coeff_W_with_sqrt2q_correction": float(c_W_corr),
            "ratio_W_over_Z": wz,
            "ratio_Z_over_H": zh,
            "ratio_W_over_H": wh,
            "deviation_W_over_Z_pct": d_wz,
            "deviation_Z_over_H_pct": d_zh,
            "deviation_W_over_H_pct": d_wh,
            "total_abs_deviation_pct": abs(d_wz) + abs(d_zh) + abs(d_wh),
            "skipped_div_by_zero": False,
        })

    # Verdict
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    valid_jets = [j for j in per_jet_results if not j["skipped_div_by_zero"]]
    if not valid_jets:
        print("No valid jet orders to compare. Probe inconclusive.")
        return

    devs_per_jet = [(j["jet_order"], j["total_abs_deviation_pct"]) for j in valid_jets]
    print(f"\nTotal |deviation| per jet order (with √[2]_q on W):")
    for jet, dev in devs_per_jet:
        marker = ""
        if dev < 10:
            marker = " ← STRONG"
        elif dev < 30:
            marker = " ← MODERATE"
        else:
            marker = " ← FAILS"
        print(f"  h^{jet}:  {dev:>8.2f}%{marker}")

    # Honest assessment
    all_strong = all(d < 10 for _, d in devs_per_jet)
    h0_strong = devs_per_jet[0][1] < 10
    higher_fails = any(d > 30 for j, d in devs_per_jet if j > 0)

    print()
    if all_strong:
        print("✓ STRUCTURAL CONFIRMATION: √[2]_q correction holds at ALL jet orders.")
        print("  The W = √[2]_q claim is jet-order robust — NOT a scalar coincidence.")
    elif h0_strong and higher_fails:
        print("✗ COINCIDENCE AT JET 0: √[2]_q works at h⁰ (scalar) but FAILS at higher")
        print("  jet orders. The W-correction is more subtle than a single multiplicative")
        print("  factor — it must depend on h (i.e., be a function √[2]_q(q) not a constant).")
        print("  The PR #1122 'STRONG result' overclaims; the correction is empirical at q_0,")
        print("  not structurally jet-universal.")
    elif h0_strong:
        print("~ PARTIAL: √[2]_q works at jet 0 and (partially) at h². Suggests the")
        print("  correction has a leading-order match but needs higher-order refinement.")
    else:
        print("✗ FAILS: √[2]_q correction doesn't hold cleanly at any jet order.")

    # Witness
    witness = {
        "compute": "rt_w_sqrt2_jet_order_validation",
        "description": (
            "Rigorous jet-order validation of the W = √[2]_q correction "
            "claim from PR #1122. Extracts h-expansion coefficients "
            "(jet orders h⁰, h², h⁴, h⁶) for |J_N(T(2,k))| at N=2, "
            "k=4 (W), 6 (Z), 8 (H), and checks whether the √[2]_q "
            "correction on W gives ratios matching SM at EVERY jet "
            "order. Tests user challenge: 'Are you sure you have a "
            "hold of the factors? you check the complete GB filtration "
            "and jet order'."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 80,
            "Q_0": str(Q_0),
            "N_color": N,
            "n_orders": n_orders,
            "sqrt_bracket_2_q0": float(sqrt_bracket_2),
        },
        "h_expansion_coefficients": {
            "W_T24": coeffs_W,
            "Z_T26": coeffs_Z,
            "H_T28": coeffs_H,
        },
        "per_jet_results": per_jet_results,
        "verdict": {
            "all_jet_orders_strong": all_strong,
            "h0_strong_only": h0_strong and higher_fails,
            "h0_strong": h0_strong,
            "total_deviations_per_jet": dict(devs_per_jet),
            "interpretation": (
                "STRUCTURAL CONFIRMATION (all jets strong)"
                if all_strong
                else "COINCIDENCE AT JET 0 (PR #1122 overclaims)"
                if (h0_strong and higher_fails)
                else "PARTIAL (leading-order match, higher-order refinement needed)"
                if h0_strong
                else "FAILS at all orders"
            ),
        },
        "user_challenge_response": (
            "User asked: 'Is this proved formally?' Answer: NO — PR #1122 was an "
            "empirical scalar fit, not a formal proof. User asked: 'you check the "
            "complete GB filtration and jet order' — Answer: NO previously, this "
            "probe IS that check. The verdict above settles whether the √[2]_q "
            "claim holds across jet orders or is a coincidence at jet 0."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "jet-order-validation",
            "w-correction",
            "structural-vs-empirical",
            "user-challenge-response",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "rt-w-sqrt2-jet-order-validation.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
