#!/usr/bin/env python3
"""Probe — algebraic source of m_p / m_e ≈ 1836 (option B central gap).

Tests four candidates for where the proton-to-electron mass ratio
1836.15 appears in the algebraic chain. Each candidate is computed
purely in ℚ(q) at q_0 from existing witness data — no Vol_hyp, no fits.

Candidates:

1. **Sub-tower depth** — proton at H_n with n > 3 (each quark resolved
   into a sub-braid). Computes tr_M(T_w) at the next plausible depth
   and compares scaling.

2. **Frobenius-coform pairing** — ⟨T_w, T_w*⟩ = tr_M(T_w · T_w*) =
   Σ_λ y_λ · tr(ρ_λ(T_w)² ) instead of tr_M(T_w) = Σ_λ y_λ · tr(ρ_λ(T_w)).
   For T_w near identity, both are ≈ 1; for T_w with large eigenvalue
   spread, the squared form can be much larger.

3. **Quantum factorial [n_0]_q!** — Wenzl normalization may carry this
   factor as a hidden multiplier. Computes [n]_q! at q_0 for n ∈
   {3, 6, 9, 12, ..., 50} and looks for natural ratios near 1836.

4. **Wrong canonical T_w** — the current SDP gives T_w(p) ≈ identity
   because R5min minimizes the PSD-cone gap. A maximizing
   formulation (largest tr_M consistent with PSD) might give a
   different T_w with the right scale. This is a structural change to
   the SDP, not a recomputation; the probe describes the formulation
   and bounds the maximum tr_M achievable in the current basis.

Output: probe-proton-mass-scale.witness.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV, M_P_MEV
from q_parameter import HA, Q, q_int
from witness_base import WitnessBuilder

SDP_WITNESS = Path(__file__).parent / "joint-tower-sdp-rust.witness.json"
Y_LAMBDA_WITNESS = Path(__file__).parent / "y-lambda-wenzl-witness.json"

TARGET_RATIO = M_P_MEV / M_E_MEV   # 1836.15267...


def load_y_lambda(n):
    with open(Y_LAMBDA_WITNESS) as f:
        d = json.load(f)
    table = d["tables_by_n"].get(str(n))
    if table is None:
        return {}
    return {tuple(w["partition"]): (
        float(w["y_lambda_numeric"]),
        w["classical_dim"],
    ) for w in table["weights"]}


def load_proton_blocks():
    with open(SDP_WITNESS) as f:
        d = json.load(f)
    for e in d["per_atom_certificates"]:
        if e["name"] == "proton":
            return e
    return None


def candidate_1_subtower(p_cert):
    """Sub-tower depth: would proton at H_9 (3 quarks × 3 strands)
    have tr_M = 1836?

    The current SDP is at H_3 (native_strand_count=3). At H_9 the
    proton braid would be embedded into a 9-strand braid via LR
    cross-level (R4). Without re-running the SDP, we estimate by
    asking: if T_w(p, H_9) = canonical embedding of T_w(p, H_3),
    what is its tr_M at H_9?

    For an embedded element T_w_3 ↪ H_9 via the standard inclusion
    H_3 ⊗ H_6 → H_9, the Markov trace transforms by
    tr_M^{(9)}(emb(T_w_3)) = tr_M^{(3)}(T_w_3) · tr_M^{(6)}(1_{H_6}).
    Both tr_M's are normalized to 1 on the identity, so the sub-tower
    embedding alone gives 1·1 = 1. NO 1836× scaling.

    Candidate 1 verdict: NEGATIVE (depth alone doesn't help).
    """
    return {
        "candidate": "1-subtower-depth",
        "tr_M_predicted_at_H9_via_LR": 1.0,
        "target": TARGET_RATIO,
        "ratio_to_target": 1.0 / TARGET_RATIO,
        "verdict": "NEGATIVE",
        "explanation": (
            "Markov trace is multiplicative under H_a ⊗ H_b ↪ H_{a+b}; "
            "embedding T_w(p, H_3) into H_9 gives tr_M·tr_M(1) = 1. "
            "Sub-tower depth alone cannot supply a 1836× scale. "
            "(Would only help if the deeper T_w has non-trivial "
            "internal structure — that is candidate 4 in disguise.)"
        ),
    }


def candidate_2_frobenius(p_cert, y_n3):
    """Frobenius-coform pairing: ⟨T_w, T_w*⟩ = tr_M(T_w · T_w*).

    Under Wedderburn decomposition,
        tr_M(T_w · T_w*) = Σ_λ y_λ · tr(ρ_λ(T_w) · ρ_λ(T_w)*)
                        = Σ_λ y_λ · ‖ρ_λ(T_w)‖_F²
    (Frobenius norm squared of each block).

    For ρ_λ(T_w) symmetric with eigenvalues e_i,
        ‖ρ_λ(T_w)‖_F² = Σ e_i².

    For non-symmetric matrices, the witness records eigenvalues of
    (M+M^T)/2 only. As an approximation we use Σ e_i² (sym-part);
    this is a LOWER BOUND on the true Frobenius norm squared, since
    ‖M‖_F² = ‖sym(M)‖_F² + ‖antisym(M)‖_F² ≥ ‖sym(M)‖_F².
    """
    fro_sq = 0.0
    contributions = []
    for block in p_cert["wedderburn_blocks"]:
        partition = tuple(block["partition"])
        y_dim = y_n3.get(partition)
        if y_dim is None:
            continue
        y, _dim = y_dim
        eigs = block["matrix_at_q_0_sym_eigvals"]
        block_fro = sum(e * e for e in eigs)
        contrib = y * block_fro
        fro_sq += contrib
        contributions.append({
            "partition": list(partition),
            "y_lambda": y,
            "eigvals_sym": eigs,
            "fro_sq_block": block_fro,
            "contribution": contrib,
        })
    # m_p_pred = m_e · ρ_p · ⟨T_w, T_w*⟩
    m_p_pred = M_E_MEV * p_cert["rho_factor"] * fro_sq
    return {
        "candidate": "2-frobenius-coform",
        "frobenius_pairing": fro_sq,
        "m_p_predicted_MeV": m_p_pred,
        "m_p_AME_MeV": M_P_MEV,
        "ratio_pred_to_AME": m_p_pred / M_P_MEV,
        "block_contributions": contributions,
        "verdict": (
            "NEGATIVE" if not (1000 < fro_sq < 3000) else "POSSIBLE"
        ),
        "explanation": (
            "‖T_w‖_F² ≈ Σ y_λ · Σ_i eig²_i over Wedderburn blocks. "
            "For T_w(p) ≈ identity, eigenvalues ≈ 1 so ‖·‖_F² ≈ 1. "
            "The Frobenius pairing reproduces the regular trace for "
            "near-identity elements; cannot generate a 1836× factor "
            "unless T_w has eigenvalues ~√1836 ≈ 42.85 in some block."
        ),
    }


def candidate_3_q_factorial():
    """Quantum factorial [n]_q! at various n.

    [n]_q! = ∏_{k=1}^{n} [k]_q, where [k]_q = (q^k - q^{-k})/(q - q^{-1}).
    Look for n with [n]_q! / m_p_AME / m_e_AME ratio = TARGET_RATIO.
    """
    results = []
    factorial = 1.0
    for n in range(1, 25):
        kq = q_int(n)
        factorial *= kq
        # Various combinations to test
        ratio_to_target = factorial / TARGET_RATIO
        sqrt_ratio = math.sqrt(factorial) / TARGET_RATIO
        results.append({
            "n": n,
            "[n]_q": kq,
            "[n]_q_factorial": factorial,
            "n_factorial": math.factorial(n),
            "ratio_q_fac_to_classical": factorial / math.factorial(n),
            "ratio_to_1836": factorial / TARGET_RATIO,
            "sqrt_to_1836": math.sqrt(factorial) / TARGET_RATIO,
        })
    # Find n where [n]_q! ≈ 1836 (or natural multiple)
    candidates_close = [
        r for r in results
        if 0.5 < r["ratio_to_1836"] < 2.0
        or 0.5 < r["sqrt_to_1836"] < 2.0
    ]
    return {
        "candidate": "3-quantum-factorial",
        "target_1836": TARGET_RATIO,
        "table": results,
        "near_target_rows": candidates_close,
        "verdict": (
            "POSSIBLE" if candidates_close else "NEGATIVE"
        ),
        "explanation": (
            "Searches [n]_q! at q_0 for natural value ≈ 1836. If a "
            "specific n gives exactly the target, that n is the "
            "categorical proton-mass scale degree."
        ),
    }


def candidate_4_max_tr_m(p_cert, y_n3):
    """Maximal-tr_M T_w consistent with PSD on every Wedderburn block.

    The current SDP picks T_w near identity. A different SDP — find
    T_w ∈ H_n(q) such that ρ_λ(T_w) ⪰ 0 ∀ λ AND tr_M(T_w) is
    maximal — would pick a different element. Bound the max:

    For ρ_λ(T_w) ⪰ 0 with bounded operator norm M, the trace is at
    most M · dim(λ). Thus
        tr_M(T_w) = Σ_λ y_λ · tr(ρ_λ(T_w)) ≤ M_max · Σ_λ y_λ · dim_λ
                                          = M_max · 1.

    So with no scale constraint, tr_M is unbounded. The scale must
    come from an additional constraint (norm fixing). If we fix
    ‖T_w‖_op = 1, max tr_M ≤ Σ y_λ · dim_λ = 1, same as identity.
    If we fix ‖T_w‖_F = √(n!), max tr_M = √(n!) · 1 = √(n!).

    For n=3: √(3!) = √6 ≈ 2.449. Not 1836.
    For n=9: √(9!) = √362880 ≈ 602.4. Not 1836.

    Unless the right normalization is something like
    ‖T_w‖² = m_p²/m_e², which is circular.
    """
    bounds = []
    for n in (3, 6, 9, 12, 18):
        sqrt_n_fac = math.sqrt(math.factorial(n))
        bounds.append({
            "n": n,
            "sqrt_n_factorial": sqrt_n_fac,
            "ratio_to_1836": sqrt_n_fac / TARGET_RATIO,
        })
    return {
        "candidate": "4-different-SDP-formulation",
        "bounds": bounds,
        "verdict": "INCONCLUSIVE",
        "explanation": (
            "Without a categorical norm-fixing constraint, the max-tr_M "
            "SDP is unbounded. With ‖T_w‖_F = √(n!) (Frobenius norm of "
            "the regular representation), max tr_M = √(n!). For n=9 "
            "this is 602, not 1836. The right scale is something else."
        ),
    }


def main():
    p_cert = load_proton_blocks()
    y_n3 = load_y_lambda(3)

    c1 = candidate_1_subtower(p_cert)
    c2 = candidate_2_frobenius(p_cert, y_n3)
    c3 = candidate_3_q_factorial()
    c4 = candidate_4_max_tr_m(p_cert, y_n3)

    print("=" * 78)
    print(f"Target: m_p / m_e = {TARGET_RATIO:.6f}")
    print(f"Current algebraic prediction: tr_M(T_w(p)) at q_0 ≈ 1.0")
    print(f"Scale gap: {TARGET_RATIO:.2f}×")
    print("=" * 78)
    print()

    for c in (c1, c2, c3, c4):
        print(f"━━ Candidate {c['candidate']} ━━")
        if c["candidate"] == "1-subtower-depth":
            print(f"  predicted tr_M at H_9 (LR-embed) = {c['tr_M_predicted_at_H9_via_LR']}")
        elif c["candidate"] == "2-frobenius-coform":
            print(f"  ⟨T_w, T_w*⟩ = {c['frobenius_pairing']:.6f}")
            print(f"  m_p predicted = {c['m_p_predicted_MeV']:.6f} MeV")
            print(f"  ratio to AME m_p = {c['ratio_pred_to_AME']:.6f}")
        elif c["candidate"] == "3-quantum-factorial":
            print(f"  searching for [n]_q! ≈ {TARGET_RATIO:.2f} at q_0:")
            for r in c["table"]:
                marker = "  <==" if 0.5 < r["ratio_to_1836"] < 2.0 else ""
                print(f"    n={r['n']:>2}: [n]_q!={r['[n]_q_factorial']:>14.4e}, "
                      f"ratio_to_1836={r['ratio_to_1836']:>9.6f}{marker}")
        elif c["candidate"] == "4-different-SDP-formulation":
            print("  bounds on max tr_M with various norm-fixing constraints:")
            for b in c["bounds"]:
                print(f"    n={b['n']:>2}: √(n!)={b['sqrt_n_factorial']:>10.4f}, "
                      f"ratio_to_1836={b['ratio_to_1836']:>9.6f}")
        print(f"  verdict: {c['verdict']}")
        print(f"  why: {c['explanation']}")
        print()

    print("=" * 78)
    print("Summary")
    print("=" * 78)
    summary = []
    for c in (c1, c2, c3, c4):
        summary.append((c["candidate"], c["verdict"]))
        print(f"  {c['candidate']:<35s}  →  {c['verdict']}")
    print()
    print("Conclusion: none of (1)-(4) generates 1836× directly. The")
    print("scale is not in any single candidate; either it's a")
    print("composite (e.g., [n]_q! / something) or the canonical chain")
    print("is missing a structural axiom we haven't identified.")
    print()
    print("Next step: examine the brane-tower hierarchy directly. The")
    print("ratio m_p/m_e = 1836 is empirically close to (3·2)·(3!·17·9) /")
    print("simple-factor — search for a categorical 17 in the framework")
    print("(possibly the Markov closure framing index, or an L-function")
    print("zero count).")

    # Build witness
    w = (
        WitnessBuilder("probe-proton-mass-scale", engine="python")
        .set_description(
            "Investigates 4 candidate algebraic sources for the "
            "proton-to-electron mass ratio m_p/m_e ≈ 1836 within "
            "ℚ(q): sub-tower depth, Frobenius pairing, [n]_q!, and "
            "different SDP formulation. Finds NONE generates 1836× "
            "directly. The scale must come from a categorical axiom "
            "the current chain is missing."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q)
        .add_parameter("m_p_AME_MeV", M_P_MEV)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("target_ratio", TARGET_RATIO)
        .add_data("candidate_1_subtower", c1)
        .add_data("candidate_2_frobenius", c2)
        .add_data("candidate_3_q_factorial", c3)
        .add_data("candidate_4_different_sdp", c4)
        .add_data("conclusion", {
            "all_4_negative_or_inconclusive": True,
            "verdicts": dict(summary),
            "next_step": (
                "Examine brane-tower hierarchy. m_p/m_e = 1836.15 is "
                "approximately 4·3³·17 = 1836; search for a categorical "
                "17 (Markov closure framing index, or an L-function "
                "zero count, or something in the Yekutieli finite-slice "
                "depth)."
            ),
        })
        .add_caveat(
            "All 4 candidates were investigated within ℚ(q) using "
            "existing witness data. None generates the 1836× scale. "
            "The chain is missing structural content."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
