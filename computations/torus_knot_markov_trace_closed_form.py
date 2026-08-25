"""Q3: Markov trace closed form for the torus link T(2, 8) — the
Higgs's cohomological identification per `electroweak-higgs-torus-link-triplet.md`.

The braid σ_1⁸ in B_2 is the Higgs's categorical knot
representative (Higgs = T(2,8), genus 3, embeds in Bring genus 4).

This script:

1. Computes the closed-form Markov trace `tr_M(σ_1^k)` in H_2(q) for
   k = 2, 4, 6, 8 (the entire even-twist torus-link triplet
   {T(2,4) = W±, T(2,6) = Z, T(2,8) = H}).
2. Extracts the h-expansion (h = q − q⁻¹) of each.
3. Compares structure to the Borromean Markov trace
   (h² = 0 cancellation, h⁴ = −3/4) from PR #1081
   `borromean-markov-trace-closed-form.md` — checking whether the
   torus knots have analogous structural cancellations.
4. Computes the value at q₀ ≈ 1.1097 (substrate) for completeness.

Note: T(2, k) torus links have **hyperbolic volume ZERO**
(Seifert-fibered, not hyperbolic), so the canonical mass formula
m(K) = m_e · Vol(K)/ℏ_q² · linking_weight(q) gives ZERO for them.
The mass prediction for Higgs/W/Z must go through a DIFFERENT
categorical chain — likely Reshetikhin-Turaev at root-of-unity
(see Q2: pentagon-rt-torus-knot-higgs-probe.py).

Status: EXPLORATORY. Probe document; no production wiring proposed.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from markov_trace_for_knot import trM_torus_2_k_mpf  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
def h_of_q(q: mpf) -> mpf:
    return q - mpf(1) / q


def trM_sigma1_k_H2(k: int, q: mpf) -> mpf:
    """Markov trace of σ_1^k in H_2(q), via Wedderburn decomposition.

    H_2(q) ≅ M_1(F) ⊕ M_1(F) (two 1-dim irreps):
      λ = (2):   σ_1 acts as q
      λ = (1,1): σ_1 acts as −q⁻¹

    Markov trace (q-Schur Plancherel convention):
      tr_M(σ_1^k) = y_(2) · q^k + y_(1,1) · (-q⁻¹)^k
      y_(2)   = q   / [2]_q,  [2]_q = q + q⁻¹
      y_(1,1) = q⁻¹ / [2]_q
    so y_(2) + y_(1,1) = 1 (Plancherel normalization).

    Delegates to the common infra `trM_torus_2_k_mpf` (which calls
    `y_lambda_h2_q_schur_mpf`) — keeps the H_2 closed form in one
    place. Generic q ⇒ preserves mp.mpf 50-dps precision.

    Cross-checked against `pn.trace_weights_n_q_schur(2, q)` (f64);
    see `torus_knot_markov_trace_generalized.py` (sibling).
    """
    return trM_torus_2_k_mpf(k, q)


def trM_in_h(k: int, q: mpf) -> dict:
    """Extract h-expansion of tr_M(σ_1^k) by numerical evaluation
    at multiple small-h values and polynomial fit.

    Returns coefficients c_0, c_1, c_2, c_3, c_4, c_5, c_6.
    """
    n_samples = 8
    h_values = [mpf("0.005") * (i + 1) for i in range(n_samples)]
    samples = []
    for h_val in h_values:
        # h = q - q⁻¹ ⟹ q² − h·q − 1 = 0 ⟹ q = (h + √(h² + 4))/2
        q_val = (h_val + mp.sqrt(h_val ** 2 + 4)) / 2
        tr_val = trM_sigma1_k_H2(k, q_val)
        samples.append((h_val, tr_val))

    # Fit polynomial up to h^6: tr = c0 + c1 h + c2 h² + c3 h³ + c4 h⁴ + c5 h⁵ + c6 h⁶
    n_coeffs = min(7, n_samples)
    H = mp.matrix(n_samples, n_coeffs)
    R = mp.matrix(n_samples, 1)
    for i, (h_val, t) in enumerate(samples):
        for j in range(n_coeffs):
            H[i, j] = h_val ** j
        R[i, 0] = t

    HT = H.T
    try:
        coeffs = mp.lu_solve(HT * H, HT * R)
        return {f"c_{j}": float(coeffs[j, 0]) for j in range(n_coeffs)}
    except Exception as e:
        return {"error": str(e)}


def torus_link_props(k: int) -> dict:
    """Standard properties of T(2, k) torus link."""
    n_components = 1 if k % 2 == 1 else 2
    # Genus: g(T(p,q)) = (p-1)(q-1)/2 for coprime; for gcd(p,q)=2: see formula
    from math import gcd
    g_pq = gcd(2, k)
    if g_pq == 1:
        genus = (2 - 1) * (k - 1) // 2  # (p-1)(q-1)/2
    else:
        # T(2, 2m) torus link genus = m - 1 (per Murasugi)
        m = k // 2
        genus = m - 1
    return {
        "k": k,
        "n_components": n_components,
        "genus": genus,
        "is_knot": n_components == 1,
        "braid_word": f"σ_1^{k}",
        "hyperbolic": False,  # T(p, q) is Seifert-fibered, not hyperbolic
        "Vol_complement": 0.0,
    }


def particle_assignment(k: int) -> str:
    """Per electroweak-higgs-torus-link-triplet.md."""
    return {
        2: "(trivial — unknot, T(2,2) = Hopf link)",
        3: "T(2,3) = trefoil — gluon / strong-force placeholder",
        4: "T(2,4) = W± (electroweak charged boson)",
        5: "T(2,5) = Solomon's link",
        6: "T(2,6) = Z (electroweak neutral boson)",
        7: "T(2,7) = knot 7_1",
        8: "T(2,8) = H (Higgs boson)",
        9: "T(2,9) — strong-force EM-side anchor (genus 4)",
    }.get(k, f"T(2,{k}) — no SM assignment")


def main() -> None:
    print("Q3: Markov trace closed form for T(2, k) torus knots/links")
    print(f"50-dps mpmath; Q_0 = {Q_0}; h_0 = {float(h_of_q(Q_0)):.6f}")
    print("Targeting Higgs = T(2,8); also Z = T(2,6), W± = T(2,4)")
    print("=" * 75)

    targets = [2, 3, 4, 5, 6, 7, 8, 9]
    results = []

    for k in targets:
        props = torus_link_props(k)
        sm_assign = particle_assignment(k)

        # Value at substrate q_0
        tr_at_q0 = trM_sigma1_k_H2(k, Q_0)

        # h-expansion
        h_exp = trM_in_h(k, Q_0)

        print(f"\nT(2,{k}) — {sm_assign}")
        print(f"  n_components = {props['n_components']}, genus = {props['genus']}, hyperbolic = {props['hyperbolic']}")
        print(f"  tr_M(σ_1^{k})(q_0) = {float(tr_at_q0):.6f}")
        print(f"  h-expansion coefficients:")
        for cn, val in sorted(h_exp.items()):
            if not cn.startswith("c_"):
                continue
            n = int(cn[2:])
            marker = "  ← non-trivial" if abs(val) > 1e-10 else "  ≈ 0"
            print(f"    {cn} (h^{n}): {val:+.6f}{marker}")

        results.append({
            "k": k,
            "sm_particle": sm_assign,
            "properties": props,
            "tr_M_at_q0": float(tr_at_q0),
            "h_expansion": h_exp,
        })

    # Compare Higgs T(2,8) h-structure to Borromean's structural pattern
    print("\n" + "=" * 75)
    print("STRUCTURAL COMPARISON: Higgs T(2,8) vs Borromean h-expansion patterns")
    print("=" * 75)
    print("Borromean (PR #1081):  tr_M ~ 1 + 0·h² − (3/4)·h⁴ − (1/16)·h⁶ + ...")
    print("                        ↑ h² cancellation; h⁴ first non-trivial")
    higgs_h_exp = next(r for r in results if r["k"] == 8)["h_expansion"]
    higgs_c0 = higgs_h_exp.get("c_0", 0)
    higgs_c2 = higgs_h_exp.get("c_2", 0)
    higgs_c4 = higgs_h_exp.get("c_4", 0)
    higgs_c6 = higgs_h_exp.get("c_6", 0)
    print(f"Higgs T(2,8):            tr_M ~ {higgs_c0:+.4f} + {higgs_c2:+.4f}·h² + "
          f"{higgs_c4:+.4f}·h⁴ + {higgs_c6:+.4f}·h⁶ + ...")
    if abs(higgs_c2) < 1e-6:
        print("                          → h² cancellation (analogous to Borromean!)")
    else:
        print(f"                          → h² coefficient is NON-ZERO ({higgs_c2:+.4f})")
        print("                            (different structure from Borromean)")

    # CRITICAL: torus knots are NOT hyperbolic; VolDensity fails
    print("\n" + "=" * 75)
    print("CRITICAL: torus knots have Vol = 0 (Seifert-fibered, not hyperbolic)")
    print("=" * 75)
    print("The canonical mass formula m(K) = m_e · Vol(K)/ℏ_q² · linking_weight")
    print("gives ZERO for all T(2, k). The Higgs/W/Z mass predictions must")
    print("go through a DIFFERENT categorical chain — most likely Reshetikhin-")
    print("Turaev at root-of-unity q (see Q2: pentagon-rt-torus-knot-higgs-probe.py).")
    print("\nThis is a foundational separation:")
    print("  - Hyperbolic knots/links (4_1 muon, 𝓑_3 baryons): VolDensity chain")
    print("  - Torus knots/links (H/W/Z/strong-force): RT-at-root-of-unity chain")
    print("\nThe Markov-trace closed forms computed here ARE the input data for")
    print("the RT chain — they're the (uncolored) Jones polynomial values that")
    print("the colored Jones invariant J_N specializes to at small N.")

    # Witness
    witness = {
        "compute": "torus_knot_markov_trace_closed_form",
        "description": (
            "Q3: Markov trace closed form for T(2, k) torus links in "
            "H_2(q), k = 2..9. Targets the Higgs T(2,8), Z T(2,6), "
            "W± T(2,4) per electroweak-higgs-torus-link-triplet.md. "
            "Highlights: torus knots have ZERO hyperbolic volume — "
            "canonical mass formula gives zero — Higgs/W/Z mass prediction "
            "needs RT-at-root-of-unity chain (Q2)."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "k_range": targets,
        },
        "results": results,
        "structural_comparison_to_borromean": {
            "borromean_h_expansion": "1 + 0·h² − (3/4)·h⁴ − (1/16)·h⁶ + ...",
            "borromean_h2_cancellation": True,
            "borromean_first_nontrivial_h_order": 4,
            "higgs_T28_h_expansion": {
                "c_0": higgs_c0,
                "c_2": higgs_c2,
                "c_4": higgs_c4,
                "c_6": higgs_c6,
            },
            "higgs_T28_h2_cancellation": bool(abs(higgs_c2) < 1e-6),
        },
        "critical_finding": (
            "Torus knots are NOT hyperbolic. Vol(T(2,k)) = 0 for all k. "
            "The canonical mass formula m = m_e · Vol/ℏ_q² · LW gives "
            "ZERO for the Higgs/W/Z. These particles need a separate "
            "categorical mass-derivation chain — Reshetikhin-Turaev at "
            "root-of-unity q is the canonical candidate (Q2 probe)."
        ),
        "status": "exploratory",
        "tags": [
            "torus-knot",
            "higgs",
            "electroweak",
            "T28",
            "markov-trace",
            "h-expansion",
            "rt-route-prep",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "torus-knot-markov-trace-closed-form.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
