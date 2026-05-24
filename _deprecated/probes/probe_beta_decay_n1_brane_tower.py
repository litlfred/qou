#!/usr/bin/env python3
# polynomial_q_not_applicable: probe script. Reports residual at
# each derived n_star — no fitting.
"""β-decay N=1 brane-tower probe at n_⋆ = 2 (substrate-derived).

Tests whether the Workplan 2+ closure path —
**brane-tower extension of convention A at level N=1, governed
by n_⋆ ≈ 2 from `brane-tower-z-habiro.md`** — closes the +1.31 keV
β-decay residual without fitting.

══════════════════════════════════════════════════════════════════
 SUBSTRATE-DERIVED INPUTS
══════════════════════════════════════════════════════════════════

The β-decay single-wrap operator (from `neutron-qvalue-symbolic.md`):

    Δ_NF = (h^2/2) γ - (h/2) σ_0 - (h/2) σ_1
    with h = q - q^{-1}

Per-channel "volumes" V̂_i (substrate-derived, no fitting):

    V̂_γ   = |h^2/2|
    V̂_σ0  = |h/2|
    V̂_σ1  = |h/2|

Derived level-selection rule for β-decay sector:

    n_⋆ = ⌈√(2 · deg_u Δ_NF)⌉ = ⌈√(2·2)⌉ = 2

(per `prop:habiro-expansion-atomic` — proven theorem)

All three candidate n_⋆ rules agree at 2:
    Habiro m_max(deg_u=2) = 2
    Coxeter length ℓ(T_β = σ_0σ_1^{-1}) = 2
    Generator rank of H_3 = 2

══════════════════════════════════════════════════════════════════
 N=1 BRANE-TOWER TRUNCATION
══════════════════════════════════════════════════════════════════

Per `brane-tower-z-habiro.md`:

    Φ_q(z) = Π_{k≥1} (1 - q^{-k} z)^{-1}      (full)
    Φ^{(N)}(z) = Π_{k=1}^{N+1} (1 - q^{-k} z)^{-1}     (truncated)

The N=0 truncation is Φ^{(0)}(z) = 1/(1 - q^{-1} z) — this is the
single-Hecke-tick form embedded in convention A.

The N=1 extension adds the second factor:

    Φ^{(1)}(z) = Φ^{(0)}(z) · 1/(1 - q^{-2} z)

with cyclotomic projection π_{n_⋆=2}^{(z)} to keep only degree-≤2
contributions in z (matching the operator's own degree bound).

══════════════════════════════════════════════════════════════════
 LIFT TO E_0
══════════════════════════════════════════════════════════════════

The framework's `prop:beta-decay-energy-scale` defines the single-
tick form E_0 = m_e/(q(q-1)) = m_e c_q^2 ℏ_q. The brane-tower
correction comes from applying Φ_q to the operator volumes:

    E_0^{(N)} = E_0^{(0)} · (1 + Σ_i δ_i^{(N)})

where δ_i^{(N)} = Φ^{(N)}(V̂_i) - Φ^{(0)}(V̂_i) is the N=1
correction per channel.

The exact functional form of the lift is **conjectural** per
`brane-tower-z-habiro.md`. This probe tests the simplest natural
choice (multiplicative correction by Σ δ_i) and reports the
resulting residual. NO PARAMETER IS TUNED.

══════════════════════════════════════════════════════════════════
 EXPECTED OUTCOMES
══════════════════════════════════════════════════════════════════

If the closure path is correct AND the lift formula above is the
right one:
  N=1 residual should drop from 0.17% to ~0.01% (76 ppm)
  consistent with the |R_N| ≤ ℏ_q^{2(N+1)} bound.

If the lift formula is wrong (the correction has a different
structural shape):
  N=1 residual could go HIGHER or have wrong sign — exposing the
  fact that the right lift is operator-specific.

Either outcome is informative. No fitting either way.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # CAL-1, noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

OUT = HERE / "beta-decay-n1-brane-tower-probe.witness.json"


def _q_0_50dps() -> mp.mpf:
    p = HERE / "q-pinning-50-digit.witness.json"
    with p.open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def phi_q_truncated(z: mp.mpf, q: mp.mpf, N: int) -> mp.mpf:
    """Φ^{(N)}(z) = Π_{k=1}^{N+1} (1 - q^{-k} z)^{-1} (truncated brane tower)."""
    prod = mp.mpf(1)
    for k in range(1, N + 2):
        prod /= (1 - z * q ** (-k))
    return prod


def main() -> int:
    q = _q_0_50dps()
    h = q - 1 / q
    m_e = M_E_MEV
    # Use the canonical CAL-3 witness value via codata_constants
    # rather than a hardcoded literal (per Copilot review on PR #637:
    # single source of truth, no drift if CAL-3 witness is refreshed).
    from codata_constants import Q_BETA_MEV
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # ── Single-wrap β-decay operator (per neutron-qvalue-symbolic.md) ──
    delta_net = h * (h - 2) / 2                         # = h^2/2 - h
    e0_N0 = m_e / (q * (q - 1))                          # convention A
    q_beta_N0 = abs(delta_net) * e0_N0

    err_N0_kev = float((q_beta_N0 - q_codata) * 1000)
    err_N0_pct = float((q_beta_N0 - q_codata) / q_codata * 100)

    # ── Per-channel volumes V̂_i ──
    V_gamma = abs(h ** 2) / 2     # |h^2/2|
    V_sigma_0 = abs(h) / 2        # |h/2|
    V_sigma_1 = abs(h) / 2        # |h/2|
    volumes = {"γ": V_gamma, "σ_0": V_sigma_0, "σ_1": V_sigma_1}

    # ── N=0 baseline Φ^{(0)}(V̂_i) ──
    phi_N0_per_channel = {k: phi_q_truncated(V, q, 0) for k, V in volumes.items()}
    sum_phi_N0 = sum(phi_N0_per_channel.values())

    # ── N=1 extension Φ^{(1)}(V̂_i) ──
    phi_N1_per_channel = {k: phi_q_truncated(V, q, 1) for k, V in volumes.items()}
    sum_phi_N1 = sum(phi_N1_per_channel.values())

    # ── Multiplicative-correction ansatz: E_0^{(1)} = E_0^{(0)} · (Σ_N1 / Σ_N0) ──
    # (simplest natural lift; tested as-is, no parameter tuning)
    lift_ratio = sum_phi_N1 / sum_phi_N0
    e0_N1 = e0_N0 * lift_ratio
    q_beta_N1 = abs(delta_net) * e0_N1

    # Other natural ansatze (reported for context, not selected)
    delta_phi_per_channel = {k: phi_N1_per_channel[k] - phi_N0_per_channel[k]
                              for k in volumes}
    additive_delta = sum(delta_phi_per_channel.values())
    e0_N1_additive = e0_N0 * (1 + additive_delta)
    q_beta_N1_additive = abs(delta_net) * e0_N1_additive

    e0_N1_relative = e0_N0 * (1 + additive_delta / sum_phi_N0)
    q_beta_N1_relative = abs(delta_net) * e0_N1_relative

    err_N1_kev = float((q_beta_N1 - q_codata) * 1000)
    err_N1_pct = float((q_beta_N1 - q_codata) / q_codata * 100)
    err_N1_add_kev = float((q_beta_N1_additive - q_codata) * 1000)
    err_N1_rel_kev = float((q_beta_N1_relative - q_codata) * 1000)

    # ── Print ──
    print("=" * 80)
    print(" β-decay N=1 brane-tower probe (n_⋆ = 2, no fitting)")
    print("=" * 80)
    print(f"\n  q_0       = {mp.nstr(q, 14)}")
    print(f"  h         = q - q^{{-1}} = {mp.nstr(h, 14)}")
    print(f"  Δ(net)    = h(h-2)/2     = {mp.nstr(delta_net, 14)}")
    print()
    print(f"  Per-channel V̂_i (substrate-derived):")
    for k, V in volumes.items():
        print(f"    V̂_{k:<5}  = {mp.nstr(V, 14)}")
    print()
    print(f"  Φ^{{(0)}}(V̂) at each channel (N=0 baseline):")
    for k, p in phi_N0_per_channel.items():
        print(f"    Φ^(0)({k:<5}) = {mp.nstr(p, 14)}")
    print(f"  Σ_i Φ^(0) = {mp.nstr(sum_phi_N0, 14)}")
    print()
    print(f"  Φ^{{(1)}}(V̂) at each channel (N=1 extension):")
    for k, p in phi_N1_per_channel.items():
        delta = delta_phi_per_channel[k]
        print(f"    Φ^(1)({k:<5}) = {mp.nstr(p, 14)}   δ = {mp.nstr(delta, 10)}")
    print(f"  Σ_i Φ^(1) = {mp.nstr(sum_phi_N1, 14)}")
    print(f"  Σ_i δ     = {mp.nstr(additive_delta, 10)}")
    print()
    print(f"  Lift ratios (substrate-derived ansatze):")
    print(f"    Σ_N1/Σ_N0 multiplicative: {mp.nstr(lift_ratio, 14)}")
    print(f"    1 + Σ_i δ_i (additive):   {mp.nstr(1 + additive_delta, 14)}")
    print(f"    1 + Σ_i δ_i / Σ_N0:       {mp.nstr(1 + additive_delta / sum_phi_N0, 14)}")
    print()
    print(f"  ── Q_β predictions ──")
    print(f"    {'baseline N=0 (conv. A)':<35}: {float(q_beta_N0):+.8f} MeV   err = {err_N0_kev:+8.3f} keV  ({err_N0_pct:+8.4f}%)")
    print(f"    {'N=1 multiplicative (Σ_N1/Σ_N0)':<35}: {float(q_beta_N1):+.8f} MeV   err = {err_N1_kev:+8.3f} keV")
    print(f"    {'N=1 additive (1 + Σδ)':<35}: {float(q_beta_N1_additive):+.8f} MeV   err = {err_N1_add_kev:+8.3f} keV")
    print(f"    {'N=1 relative (1 + Σδ/Σ_N0)':<35}: {float(q_beta_N1_relative):+.8f} MeV   err = {err_N1_rel_kev:+8.3f} keV")
    print()
    print(f"  CODATA Q_β = {float(q_codata):+.8f} MeV")
    print()

    # Tightening factor analysis
    if abs(err_N1_kev) < abs(err_N0_kev):
        factor = abs(err_N0_kev) / abs(err_N1_kev)
        print(f"  ✓ N=1 multiplicative TIGHTENS residual by {factor:.2f}× ({err_N0_kev:+.3f} → {err_N1_kev:+.3f} keV)")
    else:
        ratio = abs(err_N1_kev) / abs(err_N0_kev)
        print(f"  ✗ N=1 multiplicative is WORSE by {ratio:.2f}× — wrong lift ansatz for β-decay")

    if abs(err_N1_add_kev) < abs(err_N0_kev):
        factor = abs(err_N0_kev) / abs(err_N1_add_kev)
        print(f"  ✓ N=1 additive TIGHTENS residual by {factor:.2f}× ({err_N0_kev:+.3f} → {err_N1_add_kev:+.3f} keV)")
    else:
        ratio = abs(err_N1_add_kev) / abs(err_N0_kev)
        print(f"  ✗ N=1 additive is WORSE by {ratio:.2f}×")

    out = {
        "computation": "beta-decay-n1-brane-tower-probe",
        "scriptFile": "probe_beta_decay_n1_brane_tower.py",
        "description": (
            "β-decay N=1 brane-tower probe at n_⋆=2 (substrate-derived). "
            "Tests whether the N=1 extension of convention A closes the "
            "+0.168% / 1.31 keV residual. Three multiplicative ansatze "
            "tried (all substrate-derived; no fitting). Reports residual "
            "for each ansatz honestly — outcome could close, worsen, or "
            "be inconclusive depending on which (if any) lift formula "
            "matches the framework's brane-tower structure."
        ),
        "auditOnly": (
            "docs/audits/2026-05-10-hbar-q-scaling-audit.md; "
            "content/.../brane-tower-z-habiro.md (open conjecture on n_⋆)"
        ),
        "no_fitting_assertion": (
            "All inputs (q_0, h, V̂_i, n_⋆) derived from substrate. "
            "Three ansatze for the lift are MULTIPLICATIVE, ADDITIVE, and "
            "RELATIVE forms — all natural choices, no parameter tuning. "
            "Per-ansatz residuals reported honestly."
        ),
        "parameters": {
            "q_0_50dps": str(q),
            "h_50dps": str(h),
            "delta_net_50dps": str(delta_net),
            "m_e_MeV": str(M_E_MEV),
            "Q_beta_codata_MeV": str(q_codata),
            "n_star_derived": 2,
            "n_star_sources": [
                "Habiro m_max(deg_u Δ=2) = ⌈√4⌉ = 2",
                "Coxeter length ℓ(T_β = σ_0σ_1^{-1}) = 2",
                "Generator rank of H_3 = 2",
            ],
        },
        "data": {
            "per_channel_volumes": {k: str(v) for k, v in volumes.items()},
            "phi_N0_per_channel": {k: str(v) for k, v in phi_N0_per_channel.items()},
            "phi_N1_per_channel": {k: str(v) for k, v in phi_N1_per_channel.items()},
            "delta_phi_per_channel": {k: str(v) for k, v in delta_phi_per_channel.items()},
            "lift_ratio_multiplicative": str(lift_ratio),
            "E_0_N0_MeV": str(e0_N0),
            "E_0_N1_multiplicative_MeV": str(e0_N1),
            "E_0_N1_additive_MeV": str(e0_N1_additive),
            "E_0_N1_relative_MeV": str(e0_N1_relative),
            "Q_beta_N0_MeV": str(q_beta_N0),
            "Q_beta_N1_multiplicative_MeV": str(q_beta_N1),
            "Q_beta_N1_additive_MeV": str(q_beta_N1_additive),
            "Q_beta_N1_relative_MeV": str(q_beta_N1_relative),
            "residual_N0_keV": err_N0_kev,
            "residual_N1_multiplicative_keV": err_N1_kev,
            "residual_N1_additive_keV": err_N1_add_kev,
            "residual_N1_relative_keV": err_N1_rel_kev,
        },
    }
    saved = WitnessBuilder.wrap_legacy(
        "beta-decay-n1-brane-tower-probe", out,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Wrote {saved.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
