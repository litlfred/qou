#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical multi-anchor cross-check
"""Substrate derivation probe v6 — interface-type-resolved Δ_coupling.

v1 falsified universal [A−2]_q.  v2 falsified four simple
multiplicative corrections.  v3 identified the dominant partition
as the hook λ_⋆ = (Z+2N+1, 1^{2Z+N−1}) and the Z↔N asymmetry as
≈ h · E_0 per unit (w − d).  v4 separated three notions of
"dominant partition" (Path A pole vs PR #639 operator-Φq vs SDP
shadow-price).  v5 promoted the hook formula to a conditional
proposition.

This v6 isolates the residual 16% ³He proton-heavy anomaly via
**interface-type decomposition** of the canonical atomic braid:

  Interface types in β(Z, N) at H_{3A}:
    - pp interface (between two protons):   σ  (positive Hecke gen)
    - pn interface (heterogeneous):        avg (Δ_I = σ − h/2)
    - nn interface (between two neutrons): σ⁻¹ (negative Hecke gen)

  Interface composition per atom (Z, N) with ordering pppnnn:
    n_pp = max(0, Z − 1)
    n_pn = (1 if Z ≥ 1 and N ≥ 1 else 0)   # single boundary
    n_nn = max(0, N − 1)
    total = n_pp + n_pn + n_nn = A − 1

  ³He (Z=2, N=1): n_pp = 1, n_pn = 1, n_nn = 0
  T   (Z=1, N=2): n_pp = 0, n_pn = 1, n_nn = 1
  ⁴He (Z=2, N=2): n_pp = 1, n_pn = 2, n_nn = 1  (balanced)
  D   (Z=1, N=1): n_pp = 0, n_pn = 1, n_nn = 0

At doubly-magic (2, 2), pp and nn interfaces appear in equal numbers
and the contributions to the u-pole CANCEL by the σ ↔ σ⁻¹ eigenvalue
inversion.  At single-magic ³He, pp excess (1 pp + 0 nn) breaks the
balance — that's the structural source of the 16% anomaly.

Hypothesis tested:

  Δ_coupling(Z, N) ≈ [A − 2]_q · E_0 · log(1/h)
                     + (n_pp − n_nn) · h · E_0 · κ_iface

with κ_iface a small q-dependent constant.  At (2,2): (n_pp − n_nn)
= 0, recovers H7a exactly.  At ³He: +1; at T: −1.

The empirical Z↔N asymmetry Δ_coupling(T) − Δ_coupling(³He) = h · E_0
(found in v3) is consistent with this: (−1) − (+1) = −2 units of
(n_pp − n_nn), times the per-unit slope, gives the −0.868 MeV ≈
−h·E_0 difference per (n_pp − n_nn) unit ≈ 0.434 MeV ≈ (½·h·E_0).

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `interface-type-resolved-coupling-probe.witness.json`

@module computations/probe_interface_type_resolved_coupling
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def q_int(n, q):
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def interface_composition(Z, N):
    """Compositional count of inter-nucleon interfaces in canonical pppnnn ordering."""
    n_pp = max(0, Z - 1)
    n_nn = max(0, N - 1)
    n_pn = 1 if (Z >= 1 and N >= 1) else 0
    return n_pp, n_pn, n_nn


def main() -> int:
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        k: _mpf_from_str(pad[k]["delta_cat_MeV_50dps"])
        for k in ("deuteron", "tritium", "he3", "he4")
    }

    q0 = Q_MP
    h_q = HA_MP
    log_inv_h = mp.log(1 / h_q)
    m_e = M_E_MEV
    E0 = m_e / (q0 * (q0 - 1))
    base = E0 * log_inv_h
    iface_step = h_q * E0  # the empirical Z↔N asymmetry step from v3

    builder = (
        WitnessBuilder(
            "interface-type-resolved-coupling-probe", engine="mpmath"
        )
        .set_description(
            "v6 follow-up: tests interface-type decomposition of the "
            "canonical braid word as the source of the Z↔N asymmetry "
            "in Δ_coupling.  Hypothesis: Δ_coupling(Z,N) ≈ "
            "[A−2]_q · E_0 · log(1/h) + (n_pp − n_nn) · κ · h · E_0 "
            "with n_pp, n_nn the inter-nucleon homogeneous interface "
            "counts.  Reads κ off the single-magic anchors; tests "
            "self-consistency at the doubly-magic anchor."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("mp_dps", mp.dps)
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_parameter("h_q_50dps", mp.nstr(h_q, 50))
        .add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
        .add_parameter("base_MeV_50dps", mp.nstr(base, 50))
        .add_parameter("iface_step_MeV_50dps", mp.nstr(iface_step, 50))
    )

    anchor_def = {
        (2, 1): ("³He", dc["he3"]    - dc["deuteron"]),
        (1, 2): ("T",   dc["tritium"] - dc["deuteron"]),
        (2, 2): ("⁴He", dc["he4"]    - 2 * dc["he3"]),
    }

    # Build per-anchor data.
    rows = []
    for (Z, N), (label, anchor) in anchor_def.items():
        A = Z + N
        n_pp, n_pn, n_nn = interface_composition(Z, N)
        iface_excess = n_pp - n_nn  # signed pp-vs-nn imbalance

        h7a_pred = q_int(A - 2, q0) * base
        residual = anchor - h7a_pred  # signed: positive = anchor exceeds H7a

        # Test linearity: residual / iface_excess should be ~constant
        # across atoms (the slope κ · iface_step).  At (2, 2) excess = 0
        # so we expect residual ≈ 0 and the test is the (2, 2) gap.
        slope_per_excess = (
            residual / iface_excess if iface_excess != 0 else mp.mpf(0)
        )
        slope_in_iface_step_units = (
            slope_per_excess / iface_step if iface_excess != 0
            else mp.mpf(0)
        )

        rows.append({
            "label": label, "Z": Z, "N": N, "A": A,
            "anchor_MeV": float(anchor),
            "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            "iface_excess_pp_minus_nn": iface_excess,
            "H7a_prediction_MeV": float(h7a_pred),
            "H7a_residual_MeV": float(residual),
            "slope_per_excess_unit_MeV": (
                float(slope_per_excess) if iface_excess != 0 else None
            ),
            "slope_in_h_E0_units": (
                float(slope_in_iface_step_units) if iface_excess != 0
                else None
            ),
        })

    builder.add_data("anchors", rows)

    # ── Print summary ──────────────────────────────────────────────
    print("=" * 100)
    print("  v6 — Interface-type-resolved Δ_coupling probe")
    print(f"  E_0 · log(1/h) = {float(base):.4f} MeV   h · E_0 = "
          f"{float(iface_step):.4f} MeV")
    print("=" * 100)
    print()
    print(f"  {'atom':<5}{'(Z,N)':<8}{'n_pp':>5}{'n_pn':>5}{'n_nn':>5}"
          f"{'excess':>8}{'anchor':>10}{'H7a':>10}{'resid':>10}"
          f"{'κ (h·E0)':>12}")
    print("  " + "-" * 88)
    for r in rows:
        zn = f"({r['Z']},{r['N']})"
        excess = r["iface_excess_pp_minus_nn"]
        slope_str = (
            f"{r['slope_in_h_E0_units']:+12.4f}"
            if r['slope_in_h_E0_units'] is not None else "    (excess=0)"
        )
        print(f"  {r['label']:<5}{zn:<8}{r['n_pp']:>5}{r['n_pn']:>5}"
              f"{r['n_nn']:>5}{excess:>+8}"
              f"{r['anchor_MeV']:>10.4f}{r['H7a_prediction_MeV']:>10.4f}"
              f"{r['H7a_residual_MeV']:>+10.4f}{slope_str}")
    print()

    # ── Verdict ────────────────────────────────────────────────────
    # If the interface-excess hypothesis is correct, slope_in_h_E0_units
    # at ³He and T should be the SAME (the same κ).
    he3_slope = next(r["slope_in_h_E0_units"] for r in rows
                     if (r["Z"], r["N"]) == (2, 1))
    t_slope = next(r["slope_in_h_E0_units"] for r in rows
                   if (r["Z"], r["N"]) == (1, 2))
    he4_resid = next(r["H7a_residual_MeV"] for r in rows
                     if (r["Z"], r["N"]) == (2, 2))

    slope_consistent = abs(he3_slope - t_slope) / max(
        abs(he3_slope), abs(t_slope)
    ) <= 0.05
    he4_residual_small = abs(he4_resid) <= 0.05 * float(base)

    print(f"  ³He slope (κ in units of h·E_0): {he3_slope:+.4f}")
    print(f"  T slope (κ in units of h·E_0):  {t_slope:+.4f}")
    print(f"  Slopes consistent (±5%): {slope_consistent}")
    print(f"  ⁴He residual: {he4_resid:+.4f} MeV (≤ 5% of base = "
          f"{0.05 * float(base):.4f}): {he4_residual_small}")
    print()
    print(f"  Hypothesis status: "
          f"{'SUPPORTED' if slope_consistent and he4_residual_small else 'NOT CLOSED'}")

    builder.add_data(
        "verdict",
        {
            "he3_slope": he3_slope,
            "t_slope": t_slope,
            "slope_consistent_to_5pct": bool(slope_consistent),
            "he4_residual_small": bool(he4_residual_small),
            "hypothesis_supported": bool(
                slope_consistent and he4_residual_small
            ),
            "interpretation": (
                "The interface-excess hypothesis predicts a single "
                "constant κ (in units of h · E_0) across all atoms. "
                "If ³He and T give the same κ to ≤ 5% AND ⁴He has "
                "residual ≤ 5% of base, the hypothesis is supported. "
                "The pp interface (σ) and nn interface (σ⁻¹) "
                "contribute opposite-sign u-pole corrections; "
                "doubly-magic atoms have balanced (pp = nn) counts "
                "and the corrections cancel."
            ),
        },
    )

    builder.add_assertion(
        name="interface_excess_slope_consistent",
        computed=float(abs(he3_slope - t_slope) /
                       max(abs(he3_slope), abs(t_slope), 1e-12)),
        expected=0.0,
        tolerance=0.05,
    )

    out = builder.save()
    print(f"  Witness emitted: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
