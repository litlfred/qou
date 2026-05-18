#!/usr/bin/env python3
"""Brane-tower regularization probe — finite Laurent vs Φ_q specialisation.

Per [`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
the brane-tower has TWO equivalent forms:

(A) **Algebraic form** (canonical, archimedean evaluation):
      Vol_q^tower(β) = |∏ V̂_i^full|
                     + Σ_{|S|=1} z·V̂_i^full
                     + Σ_{|S|=2} z²·V̂_i^full·V̂_j^full
    The pre-archimedean Laurent statement
    Vol_q^(S)(β) ∈ ℤ[q^{1/2}, q^{-1/2}] is signed; the archimedean
    realisation of the descended product takes |·| (matching the
    Φ_q form's `|∏ V̂_i|`). The implementation below uses
    `mp.fabs(prod_term)` consistently with this convention.

(B) **Quantum-dilogarithm form** (archimedean specialisation
    via Kashaev limit):
      m(β) = |∏ V̂_i| + Σ Φ_q(|V̂_i|) + Σ z² Φ_q(|V̂_i V̂_j|)
    where Φ_q(z) = ∏(1 - q^{-k} z)^{-1}.

The Φ_q form is the **expanded** archimedean realisation of the
algebraic form. The prop says: *"no quantum-dilogarithm evaluation
is required to state the tower"* — Φ_q only enters via the
Kashaev specialisation.

For atom braids of D under `atom_braid_word_3A(1, 1)` with
`include_inter=True`, the per-generator full-channel volumes are
~0.99 (close to q_0 ≈ 1.11). Φ_q(z) has a pole at z=q_0; volumes
within ~10% of q_0 give Φ_q ≈ 10⁵-10⁶, hence T2_total ~10⁶
(numerically *finite* but pathologically large; not a divergence
in the strict sense).

The algebraic form gives O(1) values for the same volumes at q_0:
ρ_q · Vol_q^tower ≈ 100 × O(1) = O(100), in physical-magnitude
range (rather than pathological 10⁶).

This probe contrasts the two forms numerically.

Output: `brane-tower-finite-laurent.witness.json`
"""
from __future__ import annotations
import json
import sys
import math
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from q_parameter import Q as Q0_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402
from mass_endomorphism import Phi_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 30


def vol_q_tower_algebraic(vols, q):
    """Algebraic form of Vol_q^tower at substrate q."""
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    prod_term = mp.mpf(1)
    for v in vols:
        prod_term *= mp.mpf(repr(v))
    single = z * sum(mp.mpf(repr(v)) for v in vols)
    pair = z**2 * sum(
        mp.mpf(repr(vols[i])) * mp.mpf(repr(vols[j]))
        for i, j in combinations(range(len(vols)), 2)
    )
    return mp.fabs(prod_term) + single + pair, {
        "product": float(mp.fabs(prod_term)),
        "single_sum": float(single),
        "pair_sum": float(pair),
    }


def brane_tower_phi_q(vols):
    """Φ_q form — used in mass_formula_6term.py."""
    z = 1 / (math.sqrt(Q0_FLOAT) + 1 / math.sqrt(Q0_FLOAT))
    single = sum(Phi_q(abs(v)) for v in vols)
    pair = z**2 * sum(
        Phi_q(abs(vols[i] * vols[j]))
        for i, j in combinations(range(len(vols)), 2)
    )
    return single + pair, {"single_sum": single, "pair_sum": pair}


def main() -> int:
    print("=" * 100)
    print("Brane-tower regularization probe — finite Laurent vs Φ_q form")
    print("=" * 100)

    with mp.workdps(_DPS):
        q = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised
        hbar_q = (q - 1) / q
        rho_q = 1 / hbar_q**2
        m_e = mp.mpf(str(M_E_MEV))
        z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))

        results = []
        for label, Z, N in [("D", 1, 1)]:
            vols_atom = [v['full'] for v in atom_per_generator_volumes(Z, N, include_inter=True)]

            print(f"\n  {label} (Z={Z}, N={N}, n={3*(Z+N)}):")
            print(f"    |V̂_i^full| at q_0: {[abs(v) for v in vols_atom]}")

            # Algebraic form
            vol_alg, alg_breakdown = vol_q_tower_algebraic(vols_atom, q)
            m_invariant_alg = rho_q * vol_alg
            B_alg = m_e * m_invariant_alg

            # Φ_q form
            phi_total, phi_breakdown = brane_tower_phi_q(vols_atom)
            B_phi = m_e * mp.mpf(repr(phi_total))

            print()
            print(f"    Algebraic form Vol_q^tower (Laurent in q^{{1/2}}):")
            print(f"      ∏ |V̂_i|     = {alg_breakdown['product']:.6f}")
            print(f"      Σ z V̂_i      = {alg_breakdown['single_sum']:.6f}")
            print(f"      Σ z² V̂_i V̂_j = {alg_breakdown['pair_sum']:.6f}")
            print(f"      Vol_q^tower  = {float(vol_alg):.6f}")
            print(f"      ρ_q · Vol_q  = {float(m_invariant_alg):.4f}  (categorical m(ρ))")
            print(f"      m_e · m(ρ)   = {float(B_alg):.4f} MeV")
            print()
            print(f"    Φ_q form (Kashaev specialisation):")
            print(f"      Σ Φ_q(|V̂_i|)         = {phi_breakdown['single_sum']:.4e}")
            print(f"      Σ z² Φ_q(|V̂_i V̂_j|)  = {phi_breakdown['pair_sum']:.4e}")
            print(f"      Total                = {float(phi_total):.4e}")
            print(f"      m_e · Total          = {float(B_phi):.4e} MeV")
            print()
            print(f"    Ratio (Φ_q / algebraic):  {float(phi_total)/float(vol_alg):.4e}")
            print(f"    AME B(D)                = 2.2246 MeV")

            results.append({
                "atom": label, "Z": Z, "N": N,
                "vols_full": [float(v) for v in vols_atom],
                "vols_abs": [abs(float(v)) for v in vols_atom],
                "max_vol_over_q0": max(abs(float(v)) for v in vols_atom) / float(Q0_FLOAT),
                "algebraic_form": {
                    "Vol_q_tower": float(vol_alg),
                    "breakdown": alg_breakdown,
                    "rho_q_times_Vol": float(m_invariant_alg),
                    "B_pred_via_m_e_MeV": float(B_alg),
                },
                "Phi_q_form": {
                    "total": float(phi_total),
                    "breakdown": phi_breakdown,
                    "B_pred_via_m_e_MeV": float(B_phi),
                },
                "ratio_phi_q_over_algebraic": float(phi_total) / float(vol_alg),
            })

    print()
    print("─" * 100)
    print("FINDING")
    print("─" * 100)
    print()
    print(" 1. The Φ_q form is finite (volumes < q_0), not divergent.")
    print(" 2. But it is pathologically LARGE because volumes ~0.99 → Φ_q ~10⁵.")
    print(" 3. The algebraic form Vol_q^tower ∈ ℤ[q^{1/2}, q^{-1/2}] gives")
    print("    O(1) values — physical-magnitude.")
    print(" 4. Per the prop: \"no quantum-dilogarithm evaluation is required")
    print("    to STATE the tower\". The Φ_q form is the *Kashaev limit*")
    print("    specialisation of Vol_q^(S) — appropriate for asymptotics, not")
    print("    necessarily for substrate-q_0 numerical evaluation.")
    print(" 5. RECOMMENDATION: use the algebraic form for numerical evaluation")
    print("    at q_0 and treat the Φ_q form as the analytic continuation /")
    print("    asymptotic shadow.")
    print()
    print(" The remaining residual under the algebraic form (B ~ 199 MeV vs")
    print(" AME 2.225 MeV) is a SEPARATE prefactor question (m_e vs m_e/ρ_q vs")
    print(" m_e ℏ_q² etc.) — paper-level theory work.")

    w = (
        WitnessBuilder("brane-tower-finite-laurent", engine="mpmath")
        .set_description(
            "Diagnostic probe contrasting the algebraic (finite Laurent) "
            "form of Vol_q^tower against the Φ_q (Kashaev-specialisation) "
            "form on D's atom braid. Shows the Φ_q form's pathologically "
            "large values are a Kashaev-limit artefact at substrate-q "
            "evaluation, not an actual divergence."
        )
        .set_content_block("prop:mass-endomorphism-tower")
        .add_parameter("q_0", float(Q0_FLOAT))
        .add_parameter("hbar_q", float(hbar_q))
        .add_parameter("rho_q", float(rho_q))
        .add_parameter("z_markov", float(z))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("results", results)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
