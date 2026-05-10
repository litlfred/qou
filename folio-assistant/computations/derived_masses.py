#!/usr/bin/env python3
# polynomial_q_not_applicable: derived-quantity module; consumes
# upstream tr_M and Q_β, exposes predicted MeV masses.
"""Framework-derived rest masses for nucleons + light nuclei.

This module exposes the QOU framework's PREDICTIONS for nucleon and
light-nucleus rest masses, derived from the three calibration inputs
(CAL-1 = m_e, CAL-2 = q_0 via m_μ/m_e, CAL-3 = Q_β(n)) per
[`prop:three-calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md).

It is the **categorical** counterpart to the `*_VALIDATION` literals
exposed by `codata_constants.py`. Production prediction scripts that
currently inject `M_P_MEV` / `M_N_MEV` / etc. as upstream inputs
violate the three-calibration discipline (Workplan 0a discovery,
2026-05-10) and should migrate to:

    from derived_masses import proton_mass_mev, neutron_mass_mev
    # ...
    m_pred = proton_mass_mev()   # framework prediction, NOT CODATA

The migration plan is documented in
[`docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md`](../../docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md).
This module is the **target of that migration** (Phase 0b.2).

══════════════════════════════════════════════════════════════════
 TARGET DERIVATION CHAIN — UNIFIED KNOT MASS FORMULA (paper)
══════════════════════════════════════════════════════════════════

Per `prop:atom-knot-mass-derivation`
([`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)),
the categorical mass invariant of a confined particle 𝔥 is

    M(𝔥) = ρ · m(𝔥) = ρ · [ |tr_M(T_w)| + tower(T_w) + tr_M(C_dim_q) ]

with three components:
  (i)   |tr_M(T_w)|        — descended Markov trace via Wenzl bridge
                             Σ_λ y_λ(q) χ_λ(T_w)
  (ii)  tower(T_w)         — brane tower Σ_i Φ_q(|V̂_i|)
                             + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)
                             from per-generator additive-Wedderburn volumes
  (iii) tr_M(C_dim_q)      — Frobenius co-Casimir trace
                             Σ_{λ ⊢ n_0} 1/dim_q(λ)

After the Archimedean realization functor (CAL-1 = m_e):

    B(𝔥) = m_e · M(𝔥)|_{q = q_0}

The canonical Hecke element T_w(𝔥) is built by `mass_at_3A_proper.
atom_braid_word_3A(Z, N)` — the **β-decay-operator-unfolded** 3A-strand
braid word. For the proton (Z=1, N=0): an 11-letter word in H_3(q),
since the β-decay operator T_β = σ_0σ_1^{-1} lives in H_3(q) and the
nucleon lives at the same coarsest level (k_max ≤ 3, so unfolding to
deeper levels is superfluous per `prop:level-sufficiency`).

══════════════════════════════════════════════════════════════════
 STATUS — NONE OF THE BELOW IS WIRED YET (Phase 0b.2 scaffolding)
══════════════════════════════════════════════════════════════════

All accessors raise `NotImplementedError` with detailed pointers.
The derivation chain is functionally specified above but is not
wired here because:

  * The brane-tower component (Φ_q expansion in `mass_endomorphism.py`)
    has a known ~1.8% systematic residual at proton scale (Phase 2
    m_e_Hecke 50-dps lift not yet landed; Workplan 2 in 1ppb workplan).
  * The Frobenius co-Casimir component is straightforward (just sum
    1/dim_q(λ) over λ ⊢ 3 for the proton) but not yet exposed as a
    standalone helper.
  * The closest existing assembly, `atomic_braid_mass_table.py`,
    is "Strategy-3" with its own deprecation notice (lines 5–22 of
    that file): it back-fits a single-anchor E_0 from CODATA m_p
    (line 441), which is a 4th-calibration violation but only in the
    deprecated script. The canonical replacement is
    `atomic_mass_via_rho_k.py`, which uses
    M(K) = ρ_K · m_e · |tr_M(K)| (Options A + C in PR #564).
    Even there, ρ_K^LO consumes M_P_MEV / M_N_MEV as inputs — the
    discipline violation this module addresses.

Sibling agent (Phase 0b.4): wire each accessor to call into the
canonical pipeline, using `atom_braid_word_3A` for T_w and the
multi-term assembly for M(𝔥); add the m_e factor; emit a witness
recording the input chain.
"""
from __future__ import annotations

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: F401  (consumers)


# ── All accessors are stubs (Phase 0b.2 scaffolding) ────────────

def _stub(atom: str, extra: str = "") -> "mp.mpf":  # noqa: F821
    raise NotImplementedError(
        f"Categorical mass prediction for {atom!r} is not wired yet "
        f"(Workplan 0b Phase 0b.2 — derivation skeleton). "
        f"Currently the production prediction scripts (binding_K_direct.py, "
        f"atomic_mass_via_rho_k.py, applied_uniqueness_mass_table.py, "
        f"rho_k_h3a_*.py, sigma_shell_from_beta_chain.py) consume CODATA "
        f"m_p/m_n/m_D/m_T/m_3He/m_4He as upstream inputs, violating the "
        f"three-calibration discipline. The replacement chain is the "
        f"unified knot mass formula M(𝔥) = ρ · [|tr_M(T_w)| + tower(T_w) "
        f"+ tr_M(C_dim_q)] with B(𝔥) = m_e · M(𝔥)|_{{q=q_0}} per "
        f"prop:atom-knot-mass-derivation, and T_w via "
        f"mass_at_3A_proper.atom_braid_word_3A(Z, N) — the "
        f"β-decay-operator-unfolded canonical 3A-strand braid. "
        f"Migrate per docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md "
        f"to fill in this stub. Until then, use codata_constants."
        f"M_{atom.upper()}_MEV_VALIDATION as a comparator only.{extra}"
    )


def proton_mass_mev():
    return _stub(
        "p",
        extra=(
            " Specific wiring path for the proton: "
            "(1) T_w_p = mass_at_3A_proper.atom_braid_word_3A(1, 0) — "
            "11-letter word in H_3(q) (β-decay-operator-unfolded form); "
            "(2) |tr_M(T_w_p)| via Wenzl-bridge multi-term sum (≈ 1.0653 at q_0); "
            "(3) tower(T_w_p) via mass_endomorphism Φ_q expansion "
            "(currently ~1.8% systematic residual; Workplan 2 closes this); "
            "(4) tr_M(C_dim_q) = Σ_{λ⊢3} 1/dim_q(λ); "
            "(5) M_p = ρ_p · [(1) + (3) + (4)]; m_p_MeV = m_e · M_p|_{q=q_0}. "
            "All factors are CAL-1 (m_e) and CAL-2 (q_0) only — no CAL-3, no "
            "CODATA m_p back-fit."
        ),
    )


def neutron_mass_mev():
    return _stub(
        "n",
        extra=(
            " Specific wiring path for the neutron: same chain as proton with "
            "T_w_n = atom_braid_word_3A(0, 1). Cross-check: "
            "m_n - m_p should equal Q_β + m_e per "
            "neutron-gap-probes-round3.witness.json:recommendation; if the "
            "categorical chain reproduces this within Φ_q-tower truncation, "
            "CAL-3 is overdetermined (consistency check, not extra calibration)."
        ),
    )


def deuteron_mass_mev():
    return _stub("D")


def triton_mass_mev():
    return _stub("T")


def helium3_mass_mev():
    return _stub("HE3")


def helium4_mass_mev():
    return _stub("HE4")


def derivation_summary() -> dict:
    """Document the current state for sibling-agent / consumer use."""
    return {
        "phase": "0b.2 (skeleton only — no accessors are wired)",
        "calibration_inputs_loaded": {
            "CAL-1_m_e_MeV": str(M_E_MEV),
            "CAL-3_Q_beta_MeV": str(Q_BETA_MEV),
        },
        "wired_accessors": [],
        "stubbed_accessors": [
            "proton_mass_mev",
            "neutron_mass_mev",
            "deuteron_mass_mev",
            "triton_mass_mev",
            "helium3_mass_mev",
            "helium4_mass_mev",
        ],
        "primary_blocker": (
            "E_0 provenance: paper says E_0 = Q_β / |Δ(net)| with "
            "Δ(net) = h(h-2)/2 from symbolic NF difference; "
            "hecke_core.E_0_CALIBRATION_MEV simplifies to Q_β (Δ(net)=1); "
            "atomic_braid_mass_table.py back-fits E_0 ≈ 199.86 MeV/cat-unit "
            "from proton CODATA — a 4th-calibration discipline violation "
            "parallel to the m_p/m_n one this module fixes. Resolve E_0 "
            "first per Phase 0b.2 §\"E_0 provenance\" in the handoff."
        ),
        "secondary_blocker": (
            "total_hecke[p] cat-unit sum: production uses 4-term "
            "T1+T2+T3+T4 ≈ 4.6912 cat-units (atomic_braid_mass_terms.py); "
            "naive |tr_M(p)| ≈ 1.065 alone is wrong by 3 OOM. Phase 2 "
            "m_e_Hecke 50-dps derivation (Workplan 2 in 1ppb workplan) "
            "must land before this is honestly wired."
        ),
        "handoff_doc": (
            "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"
        ),
    }


__all__ = [
    "proton_mass_mev", "neutron_mass_mev",
    "deuteron_mass_mev", "triton_mass_mev",
    "helium3_mass_mev", "helium4_mass_mev",
    "derivation_summary",
]


if __name__ == "__main__":
    import json
    print(json.dumps(derivation_summary(), indent=2))
