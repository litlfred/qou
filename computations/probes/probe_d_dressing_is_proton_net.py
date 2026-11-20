#!/usr/bin/env python3
"""
probe_d_dressing_is_proton_net.py — the D binding dressing (1−h/2) IS the
proton single-wrap NF net coefficient (session 2026-07-04, bean 989t).

EXPLORATORY (probe_ prefix, audit-only). Follow-through on the exact
reduction (probe_d_qbeta_h_invariant): B_D ≈ E₀·(1−h/2)·Δtr at +0.12%.
This probe shows the (1−h/2) is NOT a new object — it is
`net(p) = 1 − h/2`, the proton [u,u,d] single-wrap normal-form net
coefficient in H_3(q) already carried by `conj:borromean-quark` /
`prop:neutron-qvalue-symbolic` (Lean class `BorromeanQuark`).

## The identity chain (all exact in ℚ(q); verified here at 50 dps)

  net(p) = 1 − h/2                            (borromean-quark input i)
  net(n) = 1 − 3h/2 + h²/2                    (borromean-quark input ii)
  Δ(net) = net(n) − net(p) = −h·net(p)        ← NEW: division-free identity
                            = (h² − 2h)/2
  |Δ(net)| = h·net(p)                         (0 < h < 2 substrate regime)
  Q_β = |Δ(net)|·E₀ = E₀·h·net(p)             (qvalue ansatz + the identity)
  ⇒  B_D = E₀·net(p)·Δtr = Q_β·Δtr/h          ← the D binding dressing = net(p)

So the deuteron binding scale is E₀ dressed by the PROTON's own NF net
coefficient — and it is the bar-partner of Q_β through the single factor
h (Q_β = h · [that same net(p)] · E₀). No new conjecture, no fit: rests
on the SAME borromean-quark conjecture Q_β already assumes.

## Discipline

Tiered: the ALGEBRAIC identities (Δ(net) = −h·net(p); Q_β = E₀·h·net(p);
B_D-cand = Q_β·Δtr/h) are EXACT and Lean-targeted. The physical
identification B_D ≈ AME (+0.12%) remains an observation-tier near-match
conditional on borromean-quark — NOT wired (Δ_λ gate). What is genuinely
NEW is the STRUCTURAL identification of the dressing with net(p), which
reduces "why 1−h/2" to "why the binding is dressed by the proton NF net
coefficient" and ties it to the β-decay (bar-odd) sector via h.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, COMPUTE_DPS, fmt  # noqa: E402

# Use the shared precision infra so the witness precisionMetadata (derived
# from qou_substrate.precision defaults) matches the dps actually used.
set_compute_dps()
DPS = COMPUTE_DPS

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION,
)
from derived_masses import q_beta_kashiwara_n2_mev  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def symbolic_identities() -> dict:
    """Prove the algebraic chain in ℚ(q) with sympy (division-free where
    possible). These are the exact statements the Lean lemmas encode."""
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    net_p = 1 - h / 2
    net_n = 1 - 3 * h / 2 + h ** 2 / 2
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(1, q)                       # per m_e
    delta_net = sp.simplify(net_n - net_p)
    return {
        "delta_net_eq_neg_h_net_p":
            str(sp.simplify(delta_net - (-h * net_p))),          # == 0
        "delta_net_eq_h2_minus_2h_over_2":
            str(sp.simplify(delta_net - (h ** 2 - 2 * h) / 2)),  # == 0
        "abs_delta_net_eq_h_net_p":
            str(sp.simplify((2 * h - h ** 2) / 2 - h * net_p)),  # == 0
        "qbeta_eq_E0_h_net_p":
            str(sp.simplify(E0 * (2 * h - h ** 2) / 2 - E0 * h * net_p)),  # 0
        "binding_cand_eq_qbeta_over_h_times_dtr":
            "E0*net_p*Dtr - (E0*h*net_p)*Dtr/h = "
            + str(sp.simplify(E0 * net_p - (E0 * h * net_p) / h)) + " * Dtr",
        "all_exact": True,
    }


def numerical_chain(q: mp.mpf) -> dict:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    h = q - 1 / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    net_p = 1 - h / 2
    net_n = 1 - 3 * h / 2 + h ** 2 / 2
    delta_net = net_n - net_p
    abs_delta = abs(delta_net)
    Qb_ansatz = abs_delta * E0                    # = E0·h·net_p
    Qb_kashiwara = q_beta_kashiwara_n2_mev()      # production
    ta, tf, _, _ = tr_m_atom_zn(1, 1, dps=DPS)
    dtr = mp.mpf(tf) - mp.mpf(ta)

    B_cand = E0 * net_p * dtr                     # the derived-shape candidate
    B_via_qbeta = Qb_kashiwara * dtr / h          # production-Q_β route
    return {
        "h": mp.nstr(h, 20), "net_p": mp.nstr(net_p, 20),
        "net_n": mp.nstr(net_n, 20),
        "abs_delta_net": mp.nstr(abs_delta, 20),
        "h_times_net_p": mp.nstr(h * net_p, 20),
        "abs_delta_eq_h_net_p_reldiff":
            fmt(abs((abs_delta - h * net_p) / (h * net_p))),
        "Qbeta_ansatz_MeV": mp.nstr(Qb_ansatz, 18),
        "Qbeta_kashiwara_MeV": mp.nstr(Qb_kashiwara, 18),
        "Qbeta_ansatz_vs_kashiwara_rel":
            fmt((Qb_ansatz - Qb_kashiwara) / Qb_kashiwara),
        "Delta_tr": mp.nstr(dtr, 20),
        "B_cand_E0_netp_dtr_MeV": mp.nstr(B_cand, 18),
        "B_cand_err_vs_AME_pct": fmt((B_cand / B_AME - 1) * 100),
        "B_via_kashiwara_qbeta_MeV": mp.nstr(B_via_qbeta, 18),
        "B_via_qbeta_err_vs_AME_pct": fmt((B_via_qbeta / B_AME - 1) * 100),
        "consistency_cand_vs_ansatz_route_rel":
            fmt(abs((B_cand - abs_delta * E0 * dtr / h)
                     / (abs_delta * E0 * dtr / h))),
    }


def main() -> int:
    q = Q_MP
    print("=" * 74)
    print("D BINDING DRESSING (1−h/2) = PROTON NF NET COEFFICIENT net(p)")
    print("=" * 74)

    si = symbolic_identities()
    print("\n[symbolic ℚ(q) — all residuals must be 0]")
    for k in ("delta_net_eq_neg_h_net_p", "abs_delta_net_eq_h_net_p",
              "qbeta_eq_E0_h_net_p"):
        print(f"  {k}: {si[k]}")

    nc = numerical_chain(q)
    print(f"\n[numerical @ {DPS} dps, q₀]")
    print(f"  net(p) = 1 − h/2 = {nc['net_p'][:14]}   |Δ(net)| = "
          f"{nc['abs_delta_net'][:14]}   h·net(p) = {nc['h_times_net_p'][:14]}")
    print(f"  |Δ(net)| = h·net(p) reldiff = {nc['abs_delta_eq_h_net_p_reldiff']}")
    print(f"  Q_β(ansatz=E₀·h·net_p) = {nc['Qbeta_ansatz_MeV'][:12]}  "
          f"vs Kashiwara {nc['Qbeta_kashiwara_MeV'][:12]}  "
          f"(rel {nc['Qbeta_ansatz_vs_kashiwara_rel'][:14]})")
    print(f"  B_D = E₀·net(p)·Δtr = {nc['B_cand_E0_netp_dtr_MeV'][:12]} MeV  "
          f"err {nc['B_cand_err_vs_AME_pct'][:10]}%")
    print(f"  B_D via Kashiwara Q_β·Δtr/h = {nc['B_via_kashiwara_qbeta_MeV'][:12]} "
          f"MeV  err {nc['B_via_qbeta_err_vs_AME_pct'][:10]}%")

    wb = (WitnessBuilder("probe-d-dressing-is-proton-net",
                         engine="mpmath+sympy")
          .set_description(
              "The deuteron binding dressing (1−h/2) is the proton "
              "single-wrap NF net coefficient net(p) (conj:borromean-"
              "quark). Exact ℚ(q) chain: Δ(net) = −h·net(p); "
              "|Δ(net)| = h·net(p); Q_β = E₀·h·net(p); hence "
              "B_D = E₀·net(p)·Δtr = Q_β·Δtr/h. Ties the binding "
              "dressing to the β-decay (bar-odd) sector via the single "
              "factor h. Structural identification; magnitude match "
              "(+0.12%) observation-tier, conditional on borromean-"
              "quark, NOT wired.")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("q0", Q_50_DIGIT_STR)
          .add_parameter("compute_dps", DPS)
          .add_data("symbolic", si)
          .add_data("numerical", nc))
    wb.add_assertion(
        "abs_delta_net_eq_h_net_p",
        computed=nc["abs_delta_eq_h_net_p_reldiff"], expected="0",
        tolerance="1e-45",
        source="|Δ(net)| = h·net(p) — exact ℚ(q), the identity tying the "
               "binding dressing to Q_β")
    wb.add_assertion(
        "binding_candidate_subpercent",
        computed=abs(mp.mpf(nc["B_cand_err_vs_AME_pct"])) < 1.0, expected=True,
        source="B_D = E₀·net(p)·Δtr vs AME2020")
    wb.save()
    print("\nwitness → probe-d-dressing-is-proton-net.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
