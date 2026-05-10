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
 STATUS — NONE OF THE BELOW IS WIRED YET (Phase 0b.2 scaffolding)
══════════════════════════════════════════════════════════════════

All accessors raise `NotImplementedError` with detailed pointers.
The derivation chain is itself an open question:

  * The paper's symbolic formula
    [`prop:three-calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)
    states E_0 = Q_β(n) / |Δ(net)| with Δ(net) = h(h-2)/2 from the
    symbolic NF difference; the framework value is left implicit.
  * `hecke_core.E_0_CALIBRATION_MEV` is currently set to Q_β(n)
    directly (≈ 0.782 MeV/cat-unit) — this is ONE choice of the
    "|Δ(net)|=1" normalisation but skips the symbolic Δ(net) step.
  * `atomic_braid_mass_table.py` uses E_0 ≈ 199.86 MeV/cat-unit, which
    is BACK-FITTED from `total_hecke[p] · E_0 = 938.272 MeV` (per
    `derivation_chain.py:91`). Per CLAUDE.md three-calibration
    discipline, this is a 4th calibration silently introduced — a
    discipline violation parallel to the codata_constants one this
    module is meant to fix.
  * `canonical-mass-table.witness.json` parameters block records
    `E_0_MeV: 0.782` (truncated 4 sig figs of Q_β).

The naive single-term derivation `m_p = |tr_M(p, q_0)| · E_0` with
`E_0 = Q_β` gives `1.065 × 0.782 ≈ 0.83 MeV` — off by 3 orders of
magnitude vs CODATA m_p = 938.272 MeV. The full categorical chain
(per `atomic_braid_mass_table.py` "Strategy-3") uses a multi-term
sum `total_hecke[p] = T1+T2+T3+T4 ≈ 4.6912` cat-units PLUS a
back-fitted E_0; both pieces need their own derivation before this
module can wire `proton_mass_mev()` honestly.

Sibling agent: see Phase 0b.2 §"E_0 provenance" in the handoff doc.

══════════════════════════════════════════════════════════════════
 TARGET DERIVATION CHAIN (per neutron-gap-probes-round3.witness.json)
══════════════════════════════════════════════════════════════════

    m_p_pred = total_hecke[p](q_0) · E_0                  (CAL-3-derived)
    m_n_pred = m_p_pred + Q_β + m_e                       (3-input convention)
    m_K_pred = (Z·m_p + N·m_n)_pred + Binding(K)          (categorical binding)

Once each piece is wired (with E_0 derived as Q_β / |Δ(net)| from
first principles, not back-fitted), every accessor below can drop
its `NotImplementedError` and return an `mp.mpf` predicted value.
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
        f"three-calibration discipline. The replacement chain "
        f"(m_p = total_hecke[p] · E_0; m_n = m_p + Q_β + m_e; "
        f"m_K = Z·m_p + N·m_n + Binding(K)) requires E_0 to itself be "
        f"derived as Q_β / |Δ(net)| rather than back-fitted to CODATA m_p. "
        f"Migrate per docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md "
        f"to fill in this stub. Until then, use codata_constants."
        f"M_{atom.upper()}_MEV_VALIDATION as a comparator only.{extra}"
    )


def proton_mass_mev():
    return _stub(
        "p",
        extra=(
            " Specific blocker for the proton: total_hecke[p] needs the "
            "Wenzl-bridge multi-term sum from atomic_braid_mass_terms.py, "
            "and E_0 needs the symbolic Δ(net) = h(h-2)/2 chain (currently "
            "hecke_core.E_0_CALIBRATION_MEV simplifies Δ(net) → 1)."
        ),
    )


def neutron_mass_mev():
    return _stub(
        "n",
        extra=(
            " Specific blocker for the neutron: depends on proton_mass_mev() "
            "via the 3-input convention m_n = m_p + Q_β + m_e per "
            "neutron-gap-probes-round3.witness.json:recommendation."
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
