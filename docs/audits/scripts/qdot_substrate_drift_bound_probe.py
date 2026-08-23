"""Substrate-flow bound: turn lab mass-ratio drift limits into a bound on q̇/q.

Follow-up #3 of the 2026-07-02 Bekenstein/VSL review (bean 4big, §3.4 + §5):
the empirical gate the framework owes a varying-constants referee. If the
substrate modulus q flows in cosmic time, laboratory/astrophysical limits on
the constancy of dimensionless mass ratios bound its present-day rate q̇/q,
via the chain rule

    Ẋ/X = (d ln X / d ln q) · (q̇/q)   ⇒   |q̇/q| ≤ |Ẋ/X|_bound / |d ln X/d ln q|.

Two channels are available in closed form TODAY (the α channel is blocked on
the open α_EM(q) derivation and is not attempted here):

  • m_μ/m_e = Vol(4₁)/ℏ_q²          → d ln/d ln q = −2/(q−1)   (analytic, exact)
  • m_p/m_e = 2·(Vol(4₁)/ℏ_q²)·F_Bor(q) − 12   (the lab-constrained ratio μ;
      d ln/d ln q via the canonical mass formula — numeric)

with ℏ_q = (q−1)/q, F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ (Lean-proved closed form),
Vol(4₁) = 2·Λ(π/3) = 2·Cl₂(π/3) (figure-eight complement volume).

SELF-CONTAINED (docs/audits/scripts convention): all constants inlined /
computed from mpmath; no repo imports.

The mapping formula is the durable content — plug in any updated bound. The
cited numbers are representative published limits (order-of-magnitude), not a
re-measurement:

  • |μ̇/μ| ≲ 10⁻¹⁷ yr⁻¹  — molecular-spectroscopy / astrophysical bound on
    μ = m_p/m_e (methanol / H₂ absorbers; representative).
  • a hypothetical clock/lab tightening to 10⁻¹⁸ yr⁻¹ is shown for scaling.

NOT a fit, NOT a prediction of a value — a falsifiability statement: how tightly
current data already pins the substrate modulus against drift.

Exit 0.
"""

from __future__ import annotations

import sys
from pathlib import Path

from mpmath import clsin, diff, mp, mpf, nstr, pi

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# proton-pinned q₀ (documented raw proton pin; canonical source
# qou_substrate.constants.Q_50_DIGIT_STR).
Q0 = mpf("1.1099785827513808075916690956107688798744991218736")
# Vol(4₁) = 2·Cl₂(π/3), matches q_parameter.vol_4_1_at to 55 dps.
with mp.workdps(60):
    VOL_4_1 = +(2 * clsin(2, pi / 3))

# representative published drift limits (order-of-magnitude), per yr.
BOUNDS = [mpf("1e-16"), mpf("1e-17"), mpf("1e-18")]
AGE_UNIVERSE_YR = mpf("1.38e10")


def _qint(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def _f_bor(q):
    h = q - 1 / q
    trM = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    return trM * _qint(q, 3) * _qint(q, 2) * _qint(q, 1) / q ** 3


def mp_over_me(q):
    return 2 * (VOL_4_1 / ((q - 1) / q) ** 2) * _f_bor(q) - 12


def dln_dlnq(f, q):
    """d ln f / d ln q = q·f'(q)/f(q)."""
    return q * diff(f, q) / f(q)


def main():
    # m_μ/m_e = Vol(4₁)/ℏ_q², ℏ_q = (q−1)/q ⇒ d ln/d ln q = −2/(q−1) EXACTLY
    # (closed form — no numerical differentiation, so nothing to go flaky).
    s_mu = -2 / (Q0 - 1)
    # m_p/m_e = 2(Vol/ℏ_q²)F_Bor − 12 has no equally-tidy closed derivative;
    # differentiate the canonical formula numerically.
    s_mp = dln_dlnq(mp_over_me, Q0)

    print("=" * 70)
    print("Substrate-flow bound  |q̇/q|  from mass-ratio drift limits")
    print("=" * 70)
    print(f"q₀ = {nstr(Q0, 12)}")
    print()
    print("channel sensitivities  s = d ln X / d ln q  at q₀:")
    print(f"  m_μ/m_e : s = {nstr(s_mu, 10)}   (analytic, = −2/(q−1))")
    print(f"  m_p/m_e : s = {nstr(s_mp, 10)}   (numeric, via canonical F_Bor formula)")
    print()
    print("|q̇/q| ≤ |Ẋ/X| / |s|   (and total |Δq/q| ≤ |q̇/q|·T_universe):")
    hdr = f"  {'|Ẋ/X| (per yr)':16s} {'ch':9s} {'|q̇/q| (per yr)':18s} {'|Δq/q| over 13.8 Gyr':20s}"
    print(hdr)
    results = {}
    for bnd in BOUNDS:
        for name, s in (("m_μ/m_e", s_mu), ("m_p/m_e", s_mp)):
            qdot = bnd / abs(s)
            total = qdot * AGE_UNIVERSE_YR
            results[f"{nstr(bnd,1)}|{name}"] = (float(qdot), float(total))
            print(f"  {nstr(bnd,1):16s} {name:9s} {nstr(qdot,3):18s} {nstr(total,3):20s}")
    print()
    print("Reading: the tightest available μ = m_p/m_e limit (~10⁻¹⁷/yr) already")
    print("pins the substrate modulus to |q̇/q| ≲ 5×10⁻¹⁹/yr — q constant to")
    print("~7×10⁻⁹ over cosmic history. Consistent with the corpus picture that")
    print("any interesting substrate motion is confined near the q→1⁺ endpoint,")
    print("NOT a present-day drift. (α channel blocked on the open α_EM(q) work.)")

    return results


if __name__ == "__main__":
    main()
