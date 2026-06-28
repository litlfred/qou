#!/usr/bin/env python3
"""borromean_binding_recompute.py — the SINGLE Borromean per-knot pipeline.

Complete nuclear-binding recompute through ONE pipeline (no special-casing,
no m_e·Vol(𝓑₃)): every nucleus AND every nucleon mass flows from the same
Borromean H_3 trace τ that `F_Bor` (bean `ovud`) uses for the nucleon rest
mass. Resolves the Li_2^q convergence wall (the atom-word proton trace
1.0653 > 1 diverged the free pp pair; the Borromean τ = 0.9986 < 1 converges
for ALL Z).

Pipeline (derived conventions, per docs/audits/2026-06-28-brane-tower-
formalize-first-plan.md):

  τ := |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4)      Lean BorromeanMarkovTrace
       (τ_p = τ_n at H_3 — GAP-A-4 proton≡neutron; bond type carried by the
        interface factors f, not the nucleon trace)
  interface factors  f_pp = f_pn = z,  f_nn = z − h     (Phase 5q closed form)
  atom trace   tr_atom = τ^A · Π_i f_i ,   tr_free = τ^A
  B_can⁰ = E₀·(tr_free − tr_atom)                        descended (k=0)
  B_tower = B_can⁰ + E₀·z²·Σ_pairs (g(τ_iτ_j) − g(τ_iτ_j·f_ij))
            g(x) = −Li_2^q(−x)   (bar-even binding channel + Hecke −q⁻¹ sign)

Nucleon masses come from the SAME τ via the canonical_mass facade
(m_p = 2(m_μ·F_Bor − 6m_e), F_Bor = |tr_M(β_Bor)|·[3]_q!/q³): one pipeline.

Pure Markov trace × m_e — zero AME, zero CODATA nucleon mass (CAL-1 m_e +
CAL-2 q₀ only). M_meas is the comparison target, in NO predicted formula.

Status: CONVERGES ∀Z; the higher tower does real work (¹⁶O err 31× → 2.3×) but
does NOT close to AME (under-binds mid-mass, over-binds ⁵⁶Fe) — the binding gap
is the known Δ_λ frontier, not a truncation error.
"""
from __future__ import annotations

import sys
import warnings
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV as M_E  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from canonical_mass import proton_neutron_mass_mev  # noqa: E402

# AME2020 totals (MeV) — comparison target only.
ISO = [("2H", 1, 1, 2.224573), ("3H", 1, 2, 8.481821), ("3He", 2, 1, 7.718058),
       ("4He", 2, 2, 28.295673), ("6Li", 3, 3, 31.994564), ("7Li", 3, 4, 39.244533),
       ("12C", 6, 6, 92.161728), ("16O", 8, 8, 127.619), ("56Fe", 26, 30, 492.254)]


def recompute(dps: int = 50):
    mp.mp.dps = dps
    q = mp.mpf(str(Q0)); me = mp.mpf(str(M_E)); qi = 1 / q; h = q - qi
    E0 = me / (q * (q - 1)); z = mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(qi)); z2 = z * z
    tau = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)          # Borromean H_3 trace
    mpc, mnc = (float(x) for x in proton_neutron_mass_mev())
    f_pp = z; f_pn = z; f_nn = z - h

    def g(x):
        return -li_2_q(-x, q, qi)

    def ratio(Z, N):
        return f_pp**max(Z - 1, 0) * (f_pn if Z and N else 1) * f_nn**max(N - 1, 0)

    rows = []
    for nm, Z, N, B_AME in ISO:
        trf = tau**(Z + N); tra = trf * ratio(Z, N); dtr = trf - tra
        B0 = float(E0 * dtr)
        pair = mp.mpf(0)
        for cnt, fb in ((comb(Z, 2), f_pp), (Z * N, f_pn), (comb(N, 2), f_nn)):
            if cnt:
                pair += cnt * (g(tau * tau) - g(tau * tau * fb))
        Bt = float(E0 * (dtr + z2 * pair))
        mu = Z * mpc + N * mnc
        rows.append((nm, Z, N, B_AME, B0, Bt, mu - B_AME, mu - Bt))
    return tau, z, h, mpc, mnc, rows


if __name__ == "__main__":
    tau, z, h, mpc, mnc, rows = recompute()
    print(f"SINGLE Borromean per-knot pipeline  (τ_p=τ_n={float(tau):.6f} <1 ⇒ "
          f"converges ∀Z;  z={float(z):.5f}, z−h={float(z - h):.5f})")
    print(f"  shared nucleon mass (F_Bor, same τ): m_p={mpc:.3f}  m_n={mnc:.3f} MeV\n")
    print(f"{'iso':5s}{'B_AME':>9s}{'B_can⁰':>9s}{'err⁰':>6s}{'B_tower':>9s}"
          f"{'errT':>6s}   {'m_can_T':>9s}{'M_meas':>9s}   err")
    for nm, Z, N, B_AME, B0, Bt, Mmeas, mcan in rows:
        print(f"{nm:5s}{B_AME:9.3f}{B0:9.3f}{B_AME / B0:6.2f}{Bt:9.3f}"
              f"{B_AME / Bt:6.2f}   {mcan:9.2f}{Mmeas:9.2f}  {(mcan / Mmeas - 1) * 1e6:+7.0f}ppm")
    print("\n  CONVERGES ∀Z (atom-word tower diverged for Z≥2). Higher tower does "
          "real work (¹⁶O 31×→2.3×) but does NOT close to AME — the Δ_λ frontier.")
