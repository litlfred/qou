#!/usr/bin/env python3
# polynomial_q_not_applicable: derived-quantity module; consumes
# upstream beta-decay-energy-scale witness, exposes predicted MeV
# observables.
"""Framework-derived energy observables for the QOU mass / β-decay
sector.

Predictions come from the **FULL** chain per
[`prop:beta-decay-energy-scale`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md)
and [`prop:meson-to-proton-via-borromean`](../../content/quantum-observable-universe/descartes-universe/meson-to-proton-via-borromean.md),
NOT from the LO simplification (where |tr_M| cancels exactly between
numerator and denominator of ρ_K^LO and the prediction reduces to
the constituent sum Z·m_p + N·m_n; cf.
`atomic_mass_via_rho_k.py:188-194`). The LO form is structurally
unable to predict binding — it returns CODATA inputs verbatim. Use
the FULL form below.

══════════════════════════════════════════════════════════════════
 FULL CHAIN FOR β-DECAY (Q_β prediction)
══════════════════════════════════════════════════════════════════

The β-decay Q-value is a FRAMEWORK PREDICTION (not a calibration
input) via:

    E_0 = m_e / (q_0 · (q_0 - 1)) = m_e · c_q² · ℏ_q   ≈ 4.186 MeV

(uses CAL-1 m_e and CAL-2 q_0 only; CAL-3 Q_β is the OUTPUT)

    Q_β = |Δ(net)| · E_0                          ≈ 0.788 MeV
                                              (vs CODATA 0.782; 0.75% err)

with Δ(net) = net(n) - net(p) the difference of GS-NF coefficient
sums between the canonical neutron and proton braids
(`free-neutron-decay.witness.json` typed crossings):

    net(n) = +0.81083, net(p) = +0.99913  →  Δ(net) = -0.18829

══════════════════════════════════════════════════════════════════
 OBSERVABLE vs VIRTUAL DECOMPOSITION
══════════════════════════════════════════════════════════════════

For β-decay specifically, NF terms split by Coxeter length ℓ
(per beta-decay-energy-scale.md §"Observable vs virtual"):

  * **Observable** (ℓ ≥ 2): Hopf links L_±, trefoil e^-
    — topologically non-trivial, physically observable
    Δ(obs) = -0.11007 → Q_obs ≈ 0.457 MeV (58.5% of Q_β)

  * **Virtual** (ℓ < 2): identity γ, single crossings σ_0, σ_1
    — topologically trivial, gauge / off-shell debt
    Δ(virt) = -0.07822 → Q_virt ≈ 0.325 MeV (41.5% of Q_β)

The observable-only Q is the part that corresponds to physical
kinetic energy released in the β-decay event; the virtual part is
the framework's gauge / vacuum-debt contribution that cancels in
asymptotic states.

══════════════════════════════════════════════════════════════════
 NUCLEON MASSES — FULL CHAIN NOT YET WIRED
══════════════════════════════════════════════════════════════════

The proton and neutron rest masses in the FULL form require the
multi-term unified knot mass formula
([`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)):

    M(𝔥) = ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_dim_q)]
    m_𝔥 = m_e · M(𝔥)|_{q = q_0}

with T_w = atom_braid_word_3A(Z, N).

The Strategy-3 implementation in `atomic_braid_mass_table.py` has
a known structural bug (multiplicative T1 base instead of additive
LP active-set; see lines 24-46 of that file) that produces 8-54 %
residuals on n, D, T, ³He. The LO implementation in
`atomic_mass_via_rho_k.py` is structurally tautological. Neither
is the framework's FULL prediction.

So `proton_mass_mev()` and `neutron_mass_mev()` raise
`NotImplementedError` until either (a) the multiplicative-T1 bug
is fixed via the LP-dual shadow-price scheme of
[`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md),
or (b) a separate brane-tower-clean derivation is wired (Workplan 2
Phase 2 50-dps m_e_Hecke).

For now, consumers should:
  * Use `q_beta_predicted_mev()` for Q_β predictions
  * Use `q_beta_observable_mev()` / `q_beta_virtual_mev()` for the
    decomposition
  * Use `e_0_full_mev()` for the energy-scale anchor
  * NOT consume CODATA `M_P_MEV_VALIDATION` / `M_N_MEV_VALIDATION`
    as inputs to mass-prediction scripts (discipline violation,
    Workplan 0b)
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: F401  (re-export)

_HERE = Path(__file__).resolve().parent
_BETA_DECAY_WITNESS = _HERE / "beta-decay-energy-scale.witness.json"
_Q_PINNING_WITNESS = _HERE / "q-pinning-50-digit.witness.json"


@lru_cache(maxsize=None)
def _q_0() -> mp.mpf:
    """Substrate parameter q_0 at 50-dps from the q-pinning witness.

    Pulled from `q-pinning-50-digit.witness.json:derived_50_digit.q`
    (the canonical CAL-2-derived q_0); legacy float64 fallback in
    `q_parameter.Q_50_DIGIT_STR` is identical to ~50 digits.
    """
    with _Q_PINNING_WITNESS.open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


@lru_cache(maxsize=None)
def _beta_witness() -> dict:
    """Read the β-decay-energy-scale witness."""
    if not _BETA_DECAY_WITNESS.exists():
        raise FileNotFoundError(
            f"derived_masses: β-decay witness not found at "
            f"{_BETA_DECAY_WITNESS}. Run the beta-decay-energy-scale "
            f"compute first."
        )
    with _BETA_DECAY_WITNESS.open() as fh:
        return json.load(fh)


# ── Energy scale (FULL chain, derived from CAL-1 + CAL-2) ───────

@lru_cache(maxsize=None)
def e_0_full_mev() -> mp.mpf:
    """E_0 from the FULL chain: m_e / (q_0 · (q_0 - 1)).

    Per [`prop:beta-decay-energy-scale`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md):
    derived from CAL-1 m_e and CAL-2 q_0 only — no CAL-3 (Q_β)
    needed here. CAL-3 becomes the *prediction*, not an input.

    Returns ≈ 4.186 MeV at q_0 ≈ 1.110. Calibrated cross-check
    via Q_β / |Δ(net)| gives 4.155 MeV (0.75% agreement; the
    0.75% residual is the brane-tower correction).
    """
    q0 = _q_0()
    return M_E_MEV / (q0 * (q0 - 1))


@lru_cache(maxsize=None)
def e_0_calibrated_mev() -> mp.mpf:
    """E_0 cross-check via CODATA Q_β / |Δ(net)| ≈ 4.155 MeV.

    Reads `Q_decay_MeV / hecke_nf_differences.delta_net` from the
    β-decay witness. Used only for the 0.75% derived-vs-calibrated
    consistency check, not for mass predictions.
    """
    w = _beta_witness()
    q_beta_codata = mp.mpf(str(w["observed"]["Q_decay_MeV"]))
    delta_net = mp.mpf(str(w["hecke_nf_differences"]["delta_net"]))
    return q_beta_codata / abs(delta_net)


# ── Q_β predictions (FULL framework chain) ──────────────────────

@lru_cache(maxsize=None)
def q_beta_predicted_mev() -> mp.mpf:
    """Q_β prediction = |Δ(net)| · E_0 (FULL chain).

    All terms (γ, σ_0, σ_1, L_±, e^-) — observable + virtual.
    ≈ 0.788 MeV vs CODATA 0.782 MeV (0.75% framework prediction).
    """
    w = _beta_witness()
    delta_net = mp.mpf(str(w["hecke_nf_differences"]["delta_net"]))
    return abs(delta_net) * e_0_full_mev()


@lru_cache(maxsize=None)
def q_beta_observable_mev() -> mp.mpf:
    """Q_β observable component = |Δ(obs)| · E_0.

    Observable terms have Coxeter length ℓ ≥ 2 (Hopf links L_±,
    trefoil e^-) — topologically non-trivial, physically observed.
    ≈ 0.457 MeV (58.5% of full Q_β).

    Per [`beta-decay-energy-scale`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md)
    §"Observable vs virtual: Q_{≥2}".
    """
    w = _beta_witness()
    delta_obs = mp.mpf(str(w["observable_split"]["delta_obs"]))
    return abs(delta_obs) * e_0_full_mev()


@lru_cache(maxsize=None)
def q_beta_virtual_mev() -> mp.mpf:
    """Q_β virtual component = |Δ(virt)| · E_0.

    Virtual terms have Coxeter length ℓ < 2 (identity γ, single
    crossings σ_0, σ_1) — topologically trivial, gauge / vacuum
    debt. ≈ 0.325 MeV (41.5% of full Q_β).

    Sums to q_beta_predicted_mev() within rounding.
    """
    w = _beta_witness()
    delta_virt = mp.mpf(str(w["observable_split"]["delta_virt"]))
    return abs(delta_virt) * e_0_full_mev()


# ── Nucleon + light-nucleus masses (FULL chain not yet wired) ──

def _full_chain_stub(observable: str, blocker: str) -> mp.mpf:
    raise NotImplementedError(
        f"derived_masses.{observable}: FULL-chain prediction not yet "
        f"wired. {blocker} The LO chain in atomic_mass_via_rho_k.py "
        f"is structurally tautological (|tr_M| cancels in ρ_K · m_e · "
        f"|tr_M|, so M_pred = Z·m_p + N·m_n with CODATA inputs); the "
        f"Strategy-3 chain in atomic_braid_mass_table.py uses a "
        f"multiplicative T1 base that's structurally wrong (atomic-"
        f"scale composition is additive, not multiplicative; see lines "
        f"24-46 of that file). Neither is the FULL framework "
        f"prediction. Per owner directive 2026-05-10: do not consume "
        f"either as a substitute. Wire the FULL multi-term unified "
        f"knot mass formula (prop:atom-knot-mass-derivation) once the "
        f"LP-dual shadow-price closure (prop:operator-selection-lp) "
        f"or Phase 2 m_e_Hecke 50-dps lift lands."
    )


def proton_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "proton_mass_mev",
        "Proton-specific blocker: the brane tower component "
        "tower(T_w) at H_3 with T_w = atom_braid_word_3A(1, 0) "
        "needs the Φ_q-tower truncation to <1 ppb (currently ~1.8% "
        "systematic in mass_endomorphism.py:5,26).",
    )


def neutron_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "neutron_mass_mev",
        "Neutron-specific blocker: same as proton, plus the n/p "
        "split should reproduce Q_β + m_e to <1 ppb under the "
        "FULL chain (currently checked only via |Δ(net)| · E_0 = "
        "0.788 MeV vs CODATA 0.782 MeV at 0.75%).",
    )


def deuteron_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "deuteron_mass_mev",
        "Light-nucleus blocker: requires nucleon FULL chain plus "
        "categorical Δ_λ derivation (open per recomputed-low-isotope-"
        "mass-table.md:99; 5 closure principles tested in PRs "
        "#600/#602/#603, all fail or reproduce Occam).",
    )


def triton_mass_mev() -> mp.mpf:
    return _full_chain_stub("triton_mass_mev", "Same as deuteron.")


def helium3_mass_mev() -> mp.mpf:
    return _full_chain_stub("helium3_mass_mev", "Same as deuteron.")


def helium4_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "helium4_mass_mev",
        "Light-nucleus blocker: same as deuteron, plus ⁴He H_12 "
        "Wenzl-bridge intractable in current Python mpmath (77 "
        "partitions, max dim 7700, ~2×10¹³ ops/partition × 47 "
        "crossings); needs Rust kernel or Wenzl 1988 LR branching.",
    )


def derivation_summary() -> dict:
    """Document the current state for sibling-agent / consumer use."""
    w = _beta_witness()
    return {
        "phase": "0b.4 (FULL Q_β chain wired; nucleon + light-nucleus masses stubbed)",
        "calibration_inputs_loaded": {
            "CAL-1_m_e_MeV": str(M_E_MEV),
            "CAL-2_q_0": str(_q_0()),
            "CAL-3_Q_beta_MeV": str(Q_BETA_MEV) + " (cross-check only; predicted by framework below)",
        },
        "wired_predictions": {
            "E_0_full_MeV": str(e_0_full_mev()),
            "E_0_calibrated_MeV": str(e_0_calibrated_mev()),
            "E_0_derived_vs_calibrated_pct": float(
                (e_0_full_mev() - e_0_calibrated_mev()) / e_0_calibrated_mev() * 100
            ),
            "Q_beta_predicted_MeV": str(q_beta_predicted_mev()),
            "Q_beta_observable_MeV": str(q_beta_observable_mev()),
            "Q_beta_virtual_MeV": str(q_beta_virtual_mev()),
            "Q_beta_codata_MeV": str(w["observed"]["Q_decay_MeV"]),
            "Q_beta_pred_vs_codata_pct": float(
                (q_beta_predicted_mev() - mp.mpf(str(w["observed"]["Q_decay_MeV"])))
                / mp.mpf(str(w["observed"]["Q_decay_MeV"])) * 100
            ),
            "Q_beta_observable_fraction": float(
                q_beta_observable_mev() / q_beta_predicted_mev()
            ),
        },
        "stubbed_predictions": [
            "proton_mass_mev", "neutron_mass_mev",
            "deuteron_mass_mev", "triton_mass_mev",
            "helium3_mass_mev", "helium4_mass_mev",
        ],
        "owner_directive_2026_05_10": (
            "do not use LO -- use full. look at discussion on observable "
            "vs nonobservable energy in case of beta decay. Per this "
            "directive: do NOT pull mass predictions from LO ρ_K (which "
            "is tautological by |tr_M| cancellation) or Strategy-3 "
            "(which has the multiplicative T1 bug). Q_β has a clean FULL "
            "chain — wired above. Nucleon + light-nucleus masses don't "
            "yet have a FULL chain implementation; stubs raise "
            "NotImplementedError pointing at the blockers."
        ),
        "handoff_doc": (
            "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"
        ),
    }


__all__ = [
    "e_0_full_mev", "e_0_calibrated_mev",
    "q_beta_predicted_mev", "q_beta_observable_mev", "q_beta_virtual_mev",
    "proton_mass_mev", "neutron_mass_mev",
    "deuteron_mass_mev", "triton_mass_mev",
    "helium3_mass_mev", "helium4_mass_mev",
    "derivation_summary",
]


if __name__ == "__main__":
    print(json.dumps(derivation_summary(), indent=2))
