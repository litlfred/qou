#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; evaluates tr_M at q and q⁻¹
# and the bar-norm mass-modulus, no symbolic-q polynomial output.
"""
q-parameterised atom-word builder → tr_M(q) at ANY q → bar-norm mass-modulus.

The canonical color-weighted atom word
([`atom_braid_word_3A`](mass_at_3A_proper.py)) BAKES q₀ into its float crossing
coefficients `d`, so `tr_m_atom_zn` cannot re-lift the trace at q ≠ q₀ (it
raises "unrecognised crossing"). This blocked the **bar-norm mass-modulus**
‖tr_M‖ = √(tr_M(q₀)·tr_M(q₀⁻¹)) — the principled, volume-extracting |·| (the
bar-even / cosh / binding channel; on |q|=1 the bar-involution IS complex
conjugation, so the bar-norm = usual |·|², and it cancels the Chern–Simons /
β-decay phase, leaving the pure hyperbolic volume — see
`rem:mass-modulus-em-phase-color-grading` and
`conj:binding-qbeta-complex-volume`).

Every atom-word crossing has c=1 and d in a FINITE template set
`{0 (σ), −h (σ⁻¹), −h/2 (avg), −h(½−δ/4) (color-pn)}` (verified: intra
`_PROTON_G0/G1`, `_NEUTRON_G0/G1` use only 0, −h/2, −h; the p-n interface uses
the color-pn template). So we **retarget** the word: recognise each crossing's
template at the build-q (q₀) and re-emit its `d` at the target q. The retargeted
word is then a valid word AT q_target — `chi_all_lambda_reduced_block(·, q=q_T)`
re-lifts it cleanly and the trace is consistently evaluated at q_target.

No core refactor: the recognition mirrors `chi_monotone_transfer.word_to_mpfr`
exactly (same order, same `_TOL`), and the trace assembly mirrors
`tr_m_atom_via_transfer.tr_m_atom_zn`.

Run:  python3 -u computations/atom_word_q_retarget.py 2>&1 | tee /tmp/barnorm.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import math
import sys
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from _li_2_q_util import flavor_split_subleading  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402

_TOL = 1e-9  # matches chi_monotone_transfer._TOL


def _retarget_word(word, q_build: "mp.mpf", q_target: "mp.mpf"):
    """Recognise each crossing's template at `q_build`, re-emit `d` at
    `q_target`. Returns a float word valid at `q_target`. Recognition order
    + tolerance match word_to_mpfr; raises on any unrecognised template so
    convention drift fails loudly."""
    hb = float(q_build - 1 / q_build)
    hT = q_target - 1 / q_target
    delta_b = float(flavor_split_subleading(q_build))
    delta_T = flavor_split_subleading(q_target)
    cpn_b = -hb * (0.5 - delta_b / 4.0)             # color-pn d at q_build
    out = []
    for c, d, g in word:
        cf, df = float(c), float(d)
        if abs(cf - 1.0) > _TOL:
            raise ValueError(f"unsupported crossing c={c} at gen={g}")
        if abs(df) < _TOL:
            dT = mp.mpf(0)
        elif abs(df + hb) < _TOL:
            dT = -hT
        elif abs(df + hb / 2) < _TOL:
            dT = -hT / 2
        elif abs(df - cpn_b) < _TOL:
            dT = -hT * (mp.mpf("0.5") - delta_T / 4)
        else:
            raise ValueError(
                f"unrecognised crossing (c={c}, d={d}) at gen={g} when "
                f"retargeting from q_build={float(q_build)}")
        out.append((1.0, float(dT), g))
    return out


def tr_M_at_q(Z: int, N: int, q_target: "mp.mpf", *, include_inter: bool = True,
              dps: int = 50) -> "mp.mpf":
    """tr_M(W) at arbitrary `q_target`, via word retargeting from q₀."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    n = 3 * (Z + N)
    word0 = atom_braid_word_3A(Z, N, include_inter=include_inter)
    word = _retarget_word(word0, mp.mpf(str(Q0)), q_target)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q_target).items()}
    chi = chi_all_lambda_reduced_block(word, n, q=q_target)
    return sum(y[tuple(lam)] * v for lam, v in chi.items())


def bar_norm(Z: int, N: int, *, include_inter: bool = True) -> "mp.mpf":
    """‖tr_M‖ = √(tr_M(q₀)·tr_M(q₀⁻¹)) — the bar-even mass-modulus."""
    q0 = mp.mpf(str(Q0))
    qi = mp.mpf(1) / q0
    prod = tr_M_at_q(Z, N, q0, include_inter=include_inter) * \
        tr_M_at_q(Z, N, qi, include_inter=include_inter)
    return mp.sqrt(prod) if prod > 0 else None


def main() -> int:
    mp.mp.dps = 50
    E0 = float(_ME) / (float(Q0) * (float(Q0) - 1.0))
    iso = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
    b_ame = {"2H": 2.224566, "3H": 8.481821, "3He": 7.718058, "4He": 28.295673}
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0

    print(f"\n  BAR-NORM MASS-MODULUS  ‖tr_M‖ = √(tr_M(q₀)·tr_M(q₀⁻¹))   E₀={E0:.4f} MeV")
    print("  usual binding = E₀·ln(tr_f/tr_a)|q₀ ;  bar binding = E₀·ln(‖tr_f‖/‖tr_a‖)\n")
    print("| iso | tr_a(q₀) | tr_a(q₀⁻¹) | ‖tr_a‖ bar | |tr_a| usual | B_AME | B usual | err | B bar | err |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in iso:
        ta0 = tr_M_at_q(Z, N, q0); tai = tr_M_at_q(Z, N, qi)
        tf0 = tr_M_at_q(Z, N, q0, include_inter=False)
        tfi = tr_M_at_q(Z, N, qi, include_inter=False)
        bar_a = mp.sqrt(ta0 * tai) if ta0 * tai > 0 else None
        bar_f = mp.sqrt(tf0 * tfi) if tf0 * tfi > 0 else None
        b_usual = E0 * math.log(float(tf0) / float(ta0))
        b_bar = (E0 * math.log(float(bar_f) / float(bar_a))
                 if (bar_a and bar_f) else None)
        ba = b_ame[name]
        eu = abs(b_usual - ba) / ba
        eb = abs(b_bar - ba) / ba if b_bar is not None else None
        print(f"| {name} | {float(ta0):.6f} | {float(tai):.6f} "
              f"| {float(bar_a):.6f} | {float(abs(ta0)):.6f} | {ba:.4f} "
              f"| {b_usual:.4f} | {eu*100:.1f}% "
              f"| {b_bar:.4f} | {eb*100:.1f}% |"
              if b_bar is not None else
              f"| {name} | {float(ta0):.6f} | {float(tai):.6f} | n/a | "
              f"{float(abs(ta0)):.6f} | {ba:.4f} | {b_usual:.4f} | {eu*100:.1f}% | n/a | n/a |")
    print("\n  Reading: bar-norm uses tr_M at BOTH q₀ and q₀⁻¹ (CS-cancelled, "
          "volume-extracting); usual uses tr_M(q₀) only. Compare 'B bar' vs "
          "'B usual' errors against AME to see whether the principled |·| "
          "tracks binding better.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
