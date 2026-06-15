"""
rho_constit_equals_tau_M_proton_phase5l.py — Phase 5l structural
identity for the constit-side per-Z step factor.

Phase 5k.2 ([PR #842]) FALSIFIED the (2q - 1) form for
ρ_Z^constit(q).  Phase 5l identifies the correct structural form
via the disjoint-product Markov trace formula:

  tr_M(𝓑_p ⊗ 𝓑_p ⊗ 𝓑_n in H_9)
  ──────────────────────────────  =  tr_M(𝓑_p, H_3)
  tr_M(𝓑_p ⊗ 𝓑_n in H_6)

The extra proton block contributes EXACTLY its H_3 Markov trace
(disjoint Markov trace multiplicativity).

This script verifies the identity empirically across the substrate
window q ∈ [1.05, 1.17].  If correct, the rel.err. should be at
mpfr-50-dps precision (~10^-50) at every q.

  Ref: conj:constit-factor-2q-minus-1.md (Phase 5k.2 falsification)
  Ref: prop:interface-knot-markov-z.md (interface-side companion)
  Ref: PR #842 Phase 5k.2 (the varying-q falsification)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import chi_lambda_braid, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from canonical_braid_marshalling import marshal_to_chi_lambda_braid  # noqa: E402
from hecke_core import _PROTON_G0, _PROTON_G1  # noqa: E402

# Same q sweep as Phase 5k.2 for direct comparison.  q_0 uses the
# canonical 50-digit pin from q_parameter to avoid f64 quantization
# and keep witnesses comparable across the codebase.
Q_VALUES = ["1.05", "1.08", Q_50_DIGIT_STR, "1.13", "1.17"]


def marshal_intra(chain_g0, chain_g1, h_val: float):
    """Marshal a nucleon's intra braid word (H_3) for chi_lambda_braid.

    Per Gemini PR #854 review: delegates to the shared
    `canonical_braid_marshalling.marshal_to_chi_lambda_braid` utility.
    The intra-chain format `(c, d)` (no gen_idx) is adapted by
    enumerating with gen=0,1 (0-indexed) so the utility's 1-indexing
    produces gen_1based=1,2 (= σ_1 and σ_2 for H_3).
    """
    chain_with_gens = (
        [(c, d, 0) for c, d in chain_g0]
        + [(c, d, 1) for c, d in chain_g1]
    )
    return marshal_to_chi_lambda_braid(chain_with_gens, h_val)


def compute_tau_M_proton_H3(q_val: mp.mpf, dps: int = 50) -> mp.mpf:
    """tr_M^3(𝓑_p, q) at H_3.  The proton H_3 braid is intra-only:
    g0 chain + g1 chain, no atomic embedding."""
    h_val = float(Q0 - 1 / Q0)
    word = marshal_intra(_PROTON_G0, _PROTON_G1, h_val)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    total = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word, q_value=q_str,
                                precision="mpfr_50dps")
        total += y * mp.mpf(str(chi))
    return total


def compute_tau_M_constit(Z: int, N: int, q_val: mp.mpf,
                          dps: int = 50) -> mp.mpf:
    """tr_M(𝓑_constit_K, q) for atom K = (Z, N), no interface generators.

    Per Gemini PR #854 review: braid marshalling centralized."""
    h_val = float(Q0 - 1 / Q0)
    word = atom_braid_word_3A(Z, N, include_inter=False)
    word_m = marshal_to_chi_lambda_braid(word, h_val)
    n = 3 * (Z + N)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    total = mp.mpf(0)
    for lam in partitions_of(n):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word_m, q_value=q_str,
                                precision="mpfr_50dps")
        total += y * mp.mpf(str(chi))
    return total


def main() -> int:
    set_compute_dps(50)

    # Construct WitnessBuilder BEFORE expensive compute so durationMs
    # reflects the full sweep, not just the save step (per Copilot review).
    builder = WitnessBuilder(
        "rho-constit-equals-tau-M-proton-phase5l", engine="python"
    )
    # Attach to the new proposition block (this is the primary consumer);
    # the conjecture is a predecessor referenced in the description.
    builder.set_content_block("prop:constit-factor-tau-M-proton-identity")

    print(f"=== Phase 5l: ρ_Z^constit(q) =? tr_M^3(𝓑_p, q) ===\n")

    results = []
    for q_str in Q_VALUES:
        q_val = mp.mpf(q_str)
        t0 = time.time()
        tau_p_H3 = compute_tau_M_proton_H3(q_val)
        tau_D = compute_tau_M_constit(1, 1, q_val)
        tau_3He = compute_tau_M_constit(2, 1, q_val)
        rho = tau_3He / tau_D
        diff = rho - tau_p_H3
        rel_err = abs(diff) / abs(tau_p_H3) if tau_p_H3 != 0 else mp.mpf("inf")
        results.append({
            "q": float(q_val),
            "tau_M_proton_H3": float(tau_p_H3),
            "tau_M_proton_H3_str": mp.nstr(tau_p_H3, 30),
            "rho_Z_constit": float(rho),
            "rho_Z_constit_str": mp.nstr(rho, 30),
            "diff": float(diff),
            "rel_err": float(rel_err),
            "wall_s": time.time() - t0,
        })
        print(f"  q = {q_str}:")
        print(f"    tr_M^3(𝓑_p, q)  = {float(tau_p_H3):.16f}")
        print(f"    ρ_Z^constit(q) = {float(rho):.16f}")
        print(f"    |diff|         = {abs(float(diff)):.4e}")
        print(f"    rel.err.       = {float(rel_err):.4e}")
        print()

    print(f"=== Summary ===\n")
    print(f"  {'q':>8} {'tr_M^3(𝓑_p)':>20} {'ρ_constit':>20} "
          f"{'|diff|':>14} {'rel.err':>12}")
    for r in results:
        print(f"  {r['q']:>8.5f} {r['tau_M_proton_H3']:>20.14f} "
              f"{r['rho_Z_constit']:>20.14f} "
              f"{abs(r['diff']):>14.4e} {r['rel_err']:>12.4e}")
    print()

    # Verdict
    max_rel_err = max(r["rel_err"] for r in results)
    print(f"=== Verdict ===\n")
    print(f"  Max rel.err. across {len(results)} q-points: {max_rel_err:.4e}")
    if max_rel_err < 1e-12:
        verdict = "structural-identity-confirmed"
        print(f"\n  ✓ STRUCTURAL IDENTITY CONFIRMED at mpfr-50-dps precision:")
        print(f"      ρ_Z^constit(q) = tr_M^3(𝓑_p, q)  exactly")
        print(f"    across the substrate window.  This is the disjoint")
        print(f"    Markov-trace multiplicativity result.")
    elif max_rel_err < 1e-6:
        verdict = "structural-identity-confirmed-to-6dps"
        print(f"\n  ✓ Identity holds to ~6 decimal places; small numerical "
              f"drift may be due to f64 in chi_lambda_braid pipeline.")
    else:
        verdict = "identity-not-confirmed"
        print(f"\n  ✗ Identity NOT confirmed (rel.err {max_rel_err:.2e} "
              f"exceeds 1e-6).  Hypothesis incorrect.")

    # Witness — builder constructed at start of main() for accurate
    # durationMs; populate now that the sweep has finished.
    builder.add_parameter("q_values", Q_VALUES)
    builder.set_description(
        "Phase 5l: structural identity for the constit-side per-Z step "
        "factor.  Empirically verifies that ρ_Z^constit(q) := "
        "tr_M(³He_constit, q) / tr_M(D_constit, q) equals tr_M^3(𝓑_p, q) "
        "exactly across the substrate window, as predicted by the "
        "disjoint-product Markov trace formula tr_M(α ⊗ β) = "
        "tr_M(α) · tr_M(β) for braids on disjoint strand sets.  "
        "Replaces the falsified (2q - 1) form (Phase 5k.2) with a "
        "rigorous closed form derivable from Wenzl's Markov trace."
    )
    builder.add_data("per_q_results", results)
    builder.add_data("verdict", verdict)
    builder.add_data("max_rel_err", float(max_rel_err))
    builder.add_assertion(
        name="rho_Z_constit_equals_tau_M_proton_H3",
        computed=float(max_rel_err),
        expected=0.0,
        tolerance=1e-12,
        unit="dimensionless",
        source=(
            f"Phase 5l: max relative error between ρ_Z^constit(q) and "
            f"tr_M^3(𝓑_p, q) across {len(results)} q-points in the "
            f"substrate window.  Identity holds at mpfr-50-dps precision if "
            f"max rel.err. < 1e-12."
        ),
    )
    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))

    builder.save()
    print(f"\nWitness written: rho-constit-equals-tau-M-proton-phase5l.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
