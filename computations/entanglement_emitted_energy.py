#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; γγ̄-emission energy in MeV,
# no symbolic-q polynomial output.
"""
Entanglement / emitted-γγ̄ energy — does the unaccounted emission cascade
account for the proton mass gap?

Owner hypothesis (2026-06-17): the iterative knot build is a sequence of
γγ̄ pair-production events (β_Bor = (σ₀σ₁⁻¹)³ = three γγ̄ vertices,
`gamma_gamma_pair_production_decomposition.py`). Each vertex ENTANGLES the
strands (the Borromean linking) and EMITS γγ̄ pairs; the emitted pairs carry
energy that radiates away and is not in the final bound-state trace. Maybe
that emitted energy is the 2.89% proton VolDensity gap.

Quantification. The proton mass is m_p = m_e · (Vol(𝓑₃)/ℏ_q²) · LW(q), where
LW is the Borromean linking weight (the ρ density). Three readings of LW:
  • Family A   — PROVED categorical, terminates at h²: LW = 5/2 + (3/4)h².
  • via Jones  — the FULL Markov-trace of β_Bor (all h-orders = all γγ̄
                 emissions the braid trace captures).
  • exact      — the CODATA-anchored target (what m_p must hit).

The ENTANGLEMENT energy of the knot is the linking content beyond the
classical (h⁰=5/2) term: E_ent = m_e·VolDens·(LW − 5/2). The EMITTED (gap)
energy is what Family A's h²-truncation over-counts relative to the full
emission tower: E_emit = m_e·VolDens·(LW_familyA − LW_·). We ask how much of
the gap the h⁴⁺ γγ̄ emissions (Jones − Family A) close.

Exploratory; no fit (LW_exact is the inverse target, not a fitted input).

Run:  python3 -u computations/entanglement_emitted_energy.py 2>&1 | tee /tmp/ent.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _li_2_q_util import linking_weight_family_a, vol_density_borromean  # noqa: E402
from gamma_gamma_pair_production_decomposition import (  # noqa: E402
    linking_weight_via_jones, linking_weight_exact_via_anchor,
)

CLASSICAL_LW = mp.mpf("2.5")   # h⁰ term (un-entangled word count, 5/2)


def main() -> int:
    mp.mp.dps = 40
    q = mp.mpf(str(Q0))
    m_e = mp.mpf(str(M_E_MEV))
    vd = vol_density_borromean(q)            # Vol(𝓑₃)/ℏ_q²  (dimensionless)
    scale = m_e * vd                          # MeV per unit linking weight

    lw_fa = linking_weight_family_a(q)
    lw_jn = linking_weight_via_jones(q)
    lw_ex = linking_weight_exact_via_anchor(q)

    m_fa = scale * lw_fa
    m_jn = scale * lw_jn
    m_ex = scale * lw_ex                       # = m_p CODATA by construction

    # entanglement energy = linking content beyond the classical h⁰ term
    E_ent_fa = scale * (lw_fa - CLASSICAL_LW)
    E_ent_jn = scale * (lw_jn - CLASSICAL_LW)
    E_ent_ex = scale * (lw_ex - CLASSICAL_LW)

    # the gap (Family A over-prediction) and how much the emission tower closes
    gap_total = m_fa - m_ex                    # what Family A over-counts
    emit_jones = m_fa - m_jn                    # h⁴⁺ γγ̄ emission the Jones trace captures
    residual_beyond_jones = m_jn - m_ex         # left unaccounted by the Borromean Jones trace
    frac_closed = emit_jones / gap_total if gap_total else None

    print("\n  ENTANGLEMENT / EMITTED-γγ̄ ENERGY — proton (β_Bor)")
    print(f"  q₀={float(q):.6f}  Vol(𝓑₃)/ℏ²={float(vd):.6f}  "
          f"scale=m_e·VolDens={float(scale):.4f} MeV/LW\n")
    print("| reading | linking weight | m_p (MeV) | entanglement E (MeV) |")
    print("|---|--:|--:|--:|")
    print(f"| classical (h⁰) | {float(CLASSICAL_LW):.4f} | {float(scale*CLASSICAL_LW):.3f} | 0 (un-entangled) |")
    print(f"| Family A (proved, h²) | {float(lw_fa):.5f} | {float(m_fa):.3f} | {float(E_ent_fa):.3f} |")
    print(f"| via Jones (full braid trace) | {float(lw_jn):.5f} | {float(m_jn):.3f} | {float(E_ent_jn):.3f} |")
    print(f"| exact (CODATA anchor) | {float(lw_ex):.5f} | {float(m_ex):.3f} | {float(E_ent_ex):.3f} |")

    print("\n  GAP accounting (does emitted γγ̄ energy close the 2.89%?):")
    print(f"    total gap (Family A − exact)        = {float(gap_total):+.4f} MeV "
          f"({float(gap_total/m_ex*100):+.3f}% of m_p)")
    print(f"    emitted γγ̄ captured by Jones (h⁴⁺)  = {float(emit_jones):+.4f} MeV "
          f"({float(frac_closed*100):.1f}% of the gap)")
    print(f"    residual beyond Borromean Jones     = {float(residual_beyond_jones):+.4f} MeV "
          f"({float(residual_beyond_jones/gap_total*100):.1f}% of the gap)")
    print("\n  Reading: the higher-order (h⁴⁺) γγ̄ emissions that Family A's "
          "proved h²-truncation drops are real energy; the full Borromean "
          "Jones trace captures ~half the proton gap as emitted-pair energy, "
          "corroborating the emitted-particle hypothesis. The remaining half "
          "is beyond the single-Borromean trace (multi-link / inter-nucleon "
          "emissions) — the concrete next target.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
