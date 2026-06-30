#!/usr/bin/env python3
"""
Bar-even / bar-odd binding probe — does tracking q₀ AND q₀⁻¹ (instead of
forcing the real anchor) split binding into a cosh (binding) + sinh (Q_β)
pair, and does the bar-even part fix the binding residual?

Motivation (owner question, 2026-06-30): the production binding takes
`|tr_M|` / evaluates at the real anchor q₀ only — it *forces q real* and
drops the bar-odd shadow. Per conj:binding-qbeta-complex-volume the dropped
shadow is Im 𝔙 = Q_β. This probe keeps BOTH evaluations:

    B(q)   = E₀ · ln( tr_M(W_free; q) / tr_M(W_atom; q) )
    B_even = ½[ B(q₀) + B(q₀⁻¹) ]   (bar-EVEN, cosh, P_avg — principled binding)
    B_odd  = ½[ B(q₀) − B(q₀⁻¹) ]   (bar-ODD,  sinh, P_skew — the Q_β-like part)

bar-even is the P_avg projection the corpus calls the canonical one
(bar-involution.md); the current B(q₀) is neither parity, it is the raw
real-anchor value. Tests:
  (1) does B_even match AME binding better than B(q₀)?
  (2) is B_odd ∝ Q_β (the bar-odd partner)?
  (3) is the bar/usual ratio a clean q-power (Askey/Rogers-Szegő tell)?

Audit-only; no production wiring. E₀ = m_e/(q₀(q₀−1)) (CAL-1 + CAL-2).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from q_parameter import Q as Q0  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV as _ME,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402

ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
B_AME = {
    "2H": float(AME_B_DEUTERON_MEV_VALIDATION),
    "3H": float(AME_B_TRITIUM_MEV_VALIDATION),
    "3He": float(AME_B_HE3_MEV_VALIDATION),
    "4He": float(AME_B_HE4_MEV_VALIDATION),
}


def main() -> int:
    mp.mp.dps = 50
    q0 = mp.mpf(str(Q0))
    qi = mp.mpf(1) / q0
    E0 = mp.mpf(str(_ME)) / (q0 * (q0 - 1))
    qbeta_codata = float(Q_NEUTRON_MEV)

    print(f"\n  BAR-EVEN / BAR-ODD BINDING PROBE")
    print(f"  q₀ = {float(q0):.10f}  q₀⁻¹ = {float(qi):.10f}  E₀ = {float(E0):.4f} MeV")
    print(f"  B(q) = E₀·ln(tr_free(q)/tr_atom(q));  B_even=½[B(q₀)+B(q₀⁻¹)], "
          f"B_odd=½[B(q₀)−B(q₀⁻¹)]\n")
    print("| iso | B(q₀) | B(q₀⁻¹) | B_even (cosh) | B_AME | even err | B(q₀) err | B_odd (sinh) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")

    rows = []
    for name, Z, N in ISOTOPES:
        ta0, tf0, _, _ = tr_m_atom_zn(Z, N, dps=50)
        tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=50)
        ta0, tf0, tai, tfi = (mp.mpf(str(x)) for x in (ta0, tf0, tai, tfi))
        B0 = E0 * mp.log(tf0 / ta0)
        Bi = E0 * mp.log(tfi / tai)
        B_even = (B0 + Bi) / 2
        B_odd = (B0 - Bi) / 2
        b_ame = mp.mpf(str(B_AME[name]))
        even_err = abs(B_even - b_ame) / b_ame
        raw_err = abs(B0 - b_ame) / b_ame
        rows.append((name, Z, N, B0, Bi, B_even, B_odd, b_ame, even_err, raw_err))
        print(f"| {name} | {float(B0):.4f} | {float(Bi):.4f} | {float(B_even):.4f} "
              f"| {float(b_ame):.4f} | {float(even_err)*100:.2f}% | {float(raw_err)*100:.2f}% "
              f"| {float(B_odd):.4f} |")

    # mean abs err comparison
    mae_even = sum(r[8] for r in rows) / len(rows)
    mae_raw = sum(r[9] for r in rows) / len(rows)
    print(f"\n  MAE: B_even = {float(mae_even)*100:.2f}%   B(q₀) raw = {float(mae_raw)*100:.2f}%")
    print(f"  Q_β (CODATA) = {qbeta_codata:.4f} MeV  — compare B_odd column "
          f"(is the bar-odd part the decay partner?)")

    # bar/usual ratio structure (Askey/Rogers-Szegő tell): is tr(q⁻¹)/tr(q₀) a q-power?
    print("\n  bar ratio tr_atom(q₀⁻¹)/tr_atom(q₀) vs q₀^{-k} (Askey/Rogers-Szegő structure):")
    print("| iso | ratio | ln(ratio)/ln(q₀) (≈ −k?) |")
    print("|---|--:|--:|")
    for name, Z, N, *_ in rows:
        ta0, _, _, _ = tr_m_atom_zn(Z, N, dps=50)
        tai, _, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=50)
        ratio = mp.mpf(str(tai)) / mp.mpf(str(ta0))
        kpow = mp.log(ratio) / mp.log(q0)
        print(f"| {name} | {float(ratio):.6e} | {float(kpow):.4f} |")

    witness = {
        "description": "Bar-even/bar-odd binding probe: split B into cosh (P_avg) + sinh (P_skew) by keeping q₀ AND q₀⁻¹; test bar-even vs AME and bar-odd vs Q_β",
        "computation": "binding_bar_even_odd_probe",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "tests": "conj:binding-qbeta-complex-volume — does the principled bar-even (P_avg) binding fix the residual that the raw real-anchor B(q₀) leaves?",
            "owner_question": "are we forcing q real / dropping an imaginary part that fixes the binding error?",
        },
        "constants": {"q_0": str(q0), "q_inv": str(qi), "E0_MeV": str(E0),
                      "Q_beta_codata_MeV": str(qbeta_codata)},
        "mae_bar_even": str(mae_even),
        "mae_raw_q0": str(mae_raw),
        "isotopes": {
            r[0]: {
                "B_q0_MeV": str(r[3]), "B_qinv_MeV": str(r[4]),
                "B_even_cosh_MeV": str(r[5]), "B_odd_sinh_MeV": str(r[6]),
                "B_AME_MeV": str(r[7]), "even_rel_err": str(r[8]),
                "raw_q0_rel_err": str(r[9]),
            } for r in rows
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "binding-bar-even-odd-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
