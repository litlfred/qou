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

from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402

# Use the shared precision infra so the witness precisionMetadata (derived
# from qou_substrate.precision defaults) matches the dps actually used.
set_compute_dps()
DPS = COMPUTE_DPS

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
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
    # The corpus's live binding law, exactly as binding_log_free_energy.py:95
    # (owner ruling relayed 2026-11-25, AGENTS.md exemption 2, bean qou-xj4p):
    # B = E_0 . log(|tr_free| / |tr_atom|). B_cand above is a RAW trace
    # difference = tr_free . (1 - r); tr_free is a per-nucleon self-trace that
    # the 2026-09-05 intra reordering moved 3.785x, so B_cand is not a function
    # of the bond ratio r = prod(z + d_e). The log law is.
    B_law = E0 * mp.log(abs(mp.mpf(tf)) / abs(mp.mpf(ta)))
    return {
        "h": mp.nstr(h, 20), "net_p": mp.nstr(net_p, 20),
        "net_n": mp.nstr(net_n, 20),
        "abs_delta_net": mp.nstr(abs_delta, 20),
        "h_times_net_p": mp.nstr(h * net_p, 20),
        "abs_delta_eq_h_net_p_reldiff":
            mp.nstr(abs((abs_delta - h * net_p) / (h * net_p)), 20),
        "Qbeta_ansatz_MeV": mp.nstr(Qb_ansatz, 18),
        "Qbeta_kashiwara_MeV": mp.nstr(Qb_kashiwara, 18),
        "Qbeta_ansatz_vs_kashiwara_rel":
            mp.nstr((Qb_ansatz - Qb_kashiwara) / Qb_kashiwara, 20),
        "Delta_tr": mp.nstr(dtr, 20),
        "B_cand_E0_netp_dtr_MeV": mp.nstr(B_cand, 18),
        "B_cand_err_vs_AME_pct": mp.nstr((B_cand / B_AME - 1) * 100, 20),
        "B_via_kashiwara_qbeta_MeV": mp.nstr(B_via_qbeta, 18),
        "B_via_qbeta_err_vs_AME_pct": mp.nstr((B_via_qbeta / B_AME - 1) * 100, 20),
        "tr_free": mp.nstr(mp.mpf(tf), 20),
        "tr_atom": mp.nstr(mp.mpf(ta), 20),
        "B_canonical_log_law_MeV": mp.nstr(B_law, 18),
        "B_canonical_log_law_err_vs_AME_pct":
            mp.nstr((B_law / B_AME - 1) * 100, 20),
        "consistency_cand_vs_ansatz_route_rel":
            mp.nstr(abs((B_cand - abs_delta * E0 * dtr / h)
                        / (abs_delta * E0 * dtr / h)), 20),
    }


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    print("=" * 74)
    print("D BINDING DRESSING (1−h/2) = PROTON NF NET COEFFICIENT net(p)")
    print("=" * 74)

    si = symbolic_identities()
    print("\n[symbolic ℚ(q) — all residuals must be 0]")
    for k in ("delta_net_eq_neg_h_net_p", "abs_delta_net_eq_h_net_p",
              "qbeta_eq_E0_h_net_p"):
        print(f"  {k}: {si[k]}")

    nc = numerical_chain(q)
    print("\n[numerical @ 50 dps, q₀]")
    print(f"  net(p) = 1 − h/2 = {nc['net_p'][:14]}   |Δ(net)| = "
          f"{nc['abs_delta_net'][:14]}   h·net(p) = {nc['h_times_net_p'][:14]}")
    print(f"  |Δ(net)| = h·net(p) reldiff = {nc['abs_delta_eq_h_net_p_reldiff']}")
    print(f"  Q_β(ansatz=E₀·h·net_p) = {nc['Qbeta_ansatz_MeV'][:12]}  "
          f"vs Kashiwara {nc['Qbeta_kashiwara_MeV'][:12]}  "
          f"(rel {nc['Qbeta_ansatz_vs_kashiwara_rel']})")
    print(f"  B_D = E₀·net(p)·Δtr = {nc['B_cand_E0_netp_dtr_MeV'][:12]} MeV  "
          f"err {nc['B_cand_err_vs_AME_pct'][:8]}%")
    print(f"  B_D canonical law E₀·log(tr_free/tr_atom) = "
          f"{nc['B_canonical_log_law_MeV'][:12]} MeV  "
          f"err {nc['B_canonical_log_law_err_vs_AME_pct'][:8]}%")
    print(f"  B_D via Kashiwara Q_β·Δtr/h = {nc['B_via_kashiwara_qbeta_MeV'][:12]} "
          f"MeV  err {nc['B_via_qbeta_err_vs_AME_pct'][:8]}%")

    wb = (WitnessBuilder("probe-d-dressing-is-proton-net",
                         engine="mpmath+sympy")
          .set_description(
              "The deuteron binding dressing (1−h/2) is the proton "
              "single-wrap NF net coefficient net(p) (conj:borromean-"
              "quark). Exact ℚ(q) chain: Δ(net) = −h·net(p); "
              "|Δ(net)| = h·net(p); Q_β = E₀·h·net(p); hence "
              "B_D = E₀·net(p)·Δtr = Q_β·Δtr/h. Ties the binding "
              "dressing to the β-decay (bar-odd) sector via the single "
              "factor h. The exact identities are the probe's content. "
              "The binding magnitude B_D vs AME is recorded as a NEGATIVE "
              "(owner ruling 2026-11-25, bean qou-xj4p): the 2026-07-04 "
              "+0.29% hit came only from the superseded grouped word under "
              "the excised Markov convention C (attribution: "
              "probes/probe_d_dressing_is_proton_net/attribution/); on the "
              "ruled inputs the raw-difference B_D misses AME by about -75%, "
              "because it is not normalised by tr_free. The binding magnitude "
              "is now reported on the corpus's live law, exactly "
              "binding_log_free_energy.py: B = E_0*log(|tr_free|/|tr_atom|) "
              "(about +27% for the deuteron, on the superseded single-crossing p-n "
              "interface letter: a record, not a current prediction). NOT wired.")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("q0", Q_50_DIGIT_STR)
          .add_parameter("compute_dps", DPS)
          .add_data("symbolic", si)
          .add_data("numerical", nc)
          .add_data("binding_candidate_status", {
              "verdict": "negative",
              "B_cand_err_vs_AME_pct": nc["B_cand_err_vs_AME_pct"],
              "B_cand_defect": "raw trace difference tr_free*(1-r); tr_free is a "
                               "per-nucleon self-trace, not bond data",
              "reported_binding_form": "B = E_0*log(|tr_free|/|tr_atom|), "
                                       "computations/binding_log_free_energy.py:95",
              "B_canonical_log_law_err_vs_AME_pct":
                  nc["B_canonical_log_law_err_vs_AME_pct"],
              "B_canonical_log_law_scope": "evaluated on the single-crossing interface letter of atom_braid_word_3A, superseded by the 2026-11-15 owner ruling that the gamma-gamma rule covers bond letters: a record on a superseded word, not a current prediction",
              "ruling": "owner 2026-11-25 (qou-xj4p): keep the exact identities; "
                        "record the binding match as a negative; the sub-percent "
                        "assertion is removed",
              "attribution": "probes/probe_d_dressing_is_proton_net/attribution/RESULTS.md",
          }))
    wb.add_assertion(
        "abs_delta_net_eq_h_net_p",
        computed=nc["abs_delta_eq_h_net_p_reldiff"], expected="0",
        tolerance="1e-45",
        source="|Δ(net)| = h·net(p) — exact ℚ(q), the identity tying the "
               "binding dressing to Q_β")
    wb.save()
    print("\nwitness → probe-d-dressing-is-proton-net.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
