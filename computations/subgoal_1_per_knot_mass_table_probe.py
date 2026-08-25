"""subgoal_1_per_knot_mass_table_probe.py — Phase B/C deliverable.

Side-by-side mass-table comparison: uniform Vol(𝓑₃) (production
default) vs per-knot Vol(K_atom) via the canonical atom-knot atlas
(per-atom-hyperbolic-volume.witness.json).

Tests three Subgoal-1 hypotheses:

  H1 (per-atom-Vol + uniform Family A):
      m(K) = m_e · Vol(K_atom)/ℏ_q² · linking_weight_family_a

  H2 (magic-A extension to all atoms):
      m(K) = m_e · A · Vol(𝓑₃)/ℏ_q² · linking_weight_family_a
           = A · m_proton_pred

  H3 (per-atom Vol + per-atom tr_M, the canonical Subgoal-1 path):
      m(K) = m_e · Vol(K_atom)/ℏ_q² · |tr_M(β_atom)|
           = m_e · per_knot_density_per_block(Vol(K_atom), |tr_M|, q)

Compares each to CODATA for A=1 (p, n) and A≥2 (D, T, ³He, ⁴He).
Documents which mechanism (if any) closes the +2.89% gap with the
atom-specific data.

NOT wired into production: this is a probe for Subgoal-1 assessment.
See docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md
for the wiring plan once a mechanism is identified.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import (  # noqa: E402
    linking_weight_family_a,
)
from q_parameter import Q_MP as Q_CANONICAL  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION, M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = M_E_MEV
hbar_q = 1 - 1 / q
vol_b3 = 8 * mp.catalan
lw_FA = linking_weight_family_a(q)

# Atom data: A, Z, N, atlas Vol, CODATA (central registry), tr_M (markov_peel @ q_0)
ATOMS = [
    # (atom, A, Z, N, Vol(K_atom), CODATA_MeV, tr_M_abs)
    ("p",   1, 1, 0, mp.mpf("7.32772475341775"),  M_P_MEV_VALIDATION,   mp.mpf("1.06530622861")),
    ("n",   1, 0, 1, mp.mpf("7.32772475341775"),  M_N_MEV_VALIDATION,   mp.mpf("0.92323329718")),
    ("D",   2, 1, 1, mp.mpf("4.40083251608"),     M_D_MEV_VALIDATION,   mp.mpf("0.38828647154")),
    ("T",   3, 1, 2, mp.mpf("8.28631681780"),     M_T_MEV_VALIDATION,   mp.mpf("0.10405210674")),
    ("3He", 3, 2, 1, mp.mpf("7.32772475341775"),  M_HE3_MEV_VALIDATION, mp.mpf("0.20654081702")),
    ("4He", 4, 2, 2, mp.mpf("29.31089901367"),    M_HE4_MEV_VALIDATION, mp.mpf("0.05534833516")),
]


def main() -> int:
    print(f"Subgoal-1 per-knot mass-table probe @ q_0 = {mp.nstr(q, 12)}")
    print(f"  m_e = {m_e} MeV")
    print(f"  Vol(𝓑₃)/ℏ_q² = {mp.nstr(vol_b3/hbar_q**2, 10)}")
    print(f"  linking_weight_family_a = {mp.nstr(lw_FA, 10)}")
    print()
    print(f"  Hypotheses:")
    print(f"    H0 — Production (uniform Vol(𝓑₃) + Family A) — baseline")
    print(f"    H1 — Per-atom Vol(K) + uniform Family A")
    print(f"    H2 — Magic-A extension: m(K) = A · m_proton")
    print(f"    H3 — Per-atom Vol(K) + per-atom |tr_M(β_K)|")
    print()
    header = (
        f"{'atom':>4s} {'A':>2s}  "
        f"{'H0 m_FA':>11s} {'err':>7s}   "
        f"{'H1 perVolFA':>11s} {'err':>7s}   "
        f"{'H2 A·m_p':>11s} {'err':>7s}   "
        f"{'H3 perVol·trM':>13s} {'err':>7s}   "
        f"{'CODATA':>11s}"
    )
    print(header)
    print("-" * len(header))

    m_p_pred = m_e * vol_b3 / hbar_q ** 2 * lw_FA  # H0 proton baseline

    for (atom, A, Z, N, vol_K, codata, trM) in ATOMS:
        # H0: uniform Vol(𝓑₃) · Family A (loop-invariant; == m_p_pred above)
        m_H0 = m_p_pred
        # H1: per-atom Vol(K) · Family A
        m_H1 = m_e * vol_K / hbar_q ** 2 * lw_FA
        # H2: A · m_proton
        m_H2 = mp.mpf(A) * m_p_pred
        # H3: per-atom Vol(K) · per-atom tr_M
        m_H3 = m_e * vol_K / hbar_q ** 2 * trM

        def err(p):
            return (p / codata - 1) * 100

        print(
            f"{atom:>4s} {A:>2d}  "
            f"{mp.nstr(m_H0, 7):>11s} {mp.nstr(err(m_H0), 4):>7s} %  "
            f"{mp.nstr(m_H1, 7):>11s} {mp.nstr(err(m_H1), 4):>7s} %  "
            f"{mp.nstr(m_H2, 7):>11s} {mp.nstr(err(m_H2), 4):>7s} %  "
            f"{mp.nstr(m_H3, 7):>13s} {mp.nstr(err(m_H3), 4):>7s} %  "
            f"{mp.nstr(codata, 7):>11s}"
        )

    print()
    print("VERDICT:")
    print("  H0 (production): catastrophic for D, T, ³He (~48-66% off)")
    print("  H1 (per-atom Vol + Family A): partially fixes ⁴He, regresses D, T")
    print("  H2 (A · m_proton magic-A everywhere): quasi-uniform +2.9% to +3.9% gap")
    print("  H3 (canonical per-knot Subgoal-1): catastrophic regression for all atoms")
    print()
    print("KEY FINDING: H2 (magic-A extension) is the most consistent — gap is")
    print("nearly uniform across atoms. Closing the +2.89% gap on m_proton (the")
    print("Subgoal-1 owner-active research) would close all atomic masses to ~1%.")
    print()
    print("This recasts Subgoal-1: instead of needing per-atom corrections,")
    print("the central question is the SINGLE +2.89% structural gap on m_p.")
    print("Per-atom Vol(K) data is now available but does NOT by itself close")
    print("the structural gap (H1 fails); the magic-A formula scales the gap")
    print("uniformly (H2) without explaining its origin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
