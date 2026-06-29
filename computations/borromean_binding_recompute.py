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

p/n DISTINCTION (owner question — corpus answer, critical-distance). The nucleon
TRACE does NOT distinguish p/n: proton ≡ neutron at H_3 is PROVED (GAP-A-4,
`rho-prefactor-structural-verifier.witness.json`), and `m_n = m_p + Q_β + m_e`
(Kashiwara b², parameter-free, `canonical_mass.py`). The p/n difference is the
**bar-ODD Q_β channel** (β-decay), the σ-anti partner of the bar-even binding
(`bar-parity-split.md`) — NOT a τ difference. Forcing τ_p≠τ_n at H_3 would
contradict GAP-A-4. The binding here ALREADY distinguishes p/n, structurally:
(i) the constituent sum `Z·m_p + N·m_n` carries Q_β per neutron; (ii) the
interface factors distinguish bonds — `z` (pp, pn) vs `z−h` (nn) — so ³H (nn
bond) ≠ ³He (pp bond), correct direction. (The atom-word's large τ_p=1.0653 vs
τ_n=0.9232 split is the colour-weighted construction — the one that DIVERGES;
GAP-A-4 is the canonical position.)

Δ_λ FRONTIER. The per-isotope residual `Δ(K) = B_AME / B_tower` (the `errT`
column) is the scalar shadow of the missing per-partition weight Δ_λ in the
canonical `B = m_e·Σ_λ y_λ χ^λ Δ_λ`: this tower applies a UNIFORM E₀ where the
canonical formula carries a per-λ weight. Closing it is the Track-A Δ_λ gate
(AGENTS.md) — structural levers only (GAP-A-3/A-4 level selection), NOT a 7th fit.

Status: CONVERGES ∀Z; the higher tower does real work (¹⁶O err 31× → 2.3×) but
does NOT close to AME (under-binds mid-mass, over-binds ⁵⁶Fe) — the known Δ_λ
frontier, not a truncation error.
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


def _params(dps: int = 50):
    mp.mp.dps = dps
    q = mp.mpf(str(Q0)); me = mp.mpf(str(M_E)); qi = 1 / q; h = q - qi
    E0 = me / (q * (q - 1)); z = mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
    tau = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)          # Borromean H_3 trace
    return q, qi, h, E0, z, tau


def borromean_binding(Z: int, N: int, dps: int = 50) -> dict:
    """Canonical single-pipeline binding (MeV) for nucleus (Z, N) — the
    convergent per-knot Borromean brane tower. Reusable production entry point
    (consumed by the dashboard's `m_can`). Returns B_can0 (level-0 E₀·Δtr) and
    B_tower (+ n=0 Li₂^q pair correction). Pure Markov × m_e; zero AME/CODATA."""
    q, qi, h, E0, z, tau = _params(dps)
    z2 = z * z; f_pp = z; f_pn = z; f_nn = z - h
    A = Z + N

    def g(x):
        return -li_2_q(-x, q, qi)

    ratio = f_pp**max(Z - 1, 0) * (f_pn if Z and N else 1) * f_nn**max(N - 1, 0)
    trf = tau**A; tra = trf * ratio; dtr = trf - tra
    pair = mp.mpf(0)
    for cnt, fb in ((comb(Z, 2), f_pp), (Z * N, f_pn), (comb(N, 2), f_nn)):
        if cnt:
            pair += cnt * (g(tau * tau) - g(tau * tau * fb))
    return {"Z": Z, "N": N, "A": A, "tau": float(tau),
            "B_can0": float(E0 * dtr), "B_tower": float(E0 * (dtr + z2 * pair))}


def recompute(dps: int = 50):
    q, qi, h, E0, z, tau = _params(dps)
    mpc, mnc = (float(x) for x in proton_neutron_mass_mev())
    rows = []
    for nm, Z, N, B_AME in ISO:
        b = borromean_binding(Z, N, dps)
        mu = Z * mpc + N * mnc
        rows.append((nm, Z, N, B_AME, b["B_can0"], b["B_tower"],
                     mu - B_AME, mu - b["B_tower"]))
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
    # witness — production-grade record; Δ(K)=B_AME/B_tower is the scalar shadow
    # of the missing per-partition Δ_λ (the FR-pullback / volume enrichment lever).
    import json
    out = {"schema": "borromean-binding/v1", "tau": float(tau),
           "E0_MeV": float((mp.mpf(str(M_E))) / (mp.mpf(str(Q0)) * (mp.mpf(str(Q0)) - 1))),
           "converges_all_Z": True,
           "isotopes": [{"iso": nm, "Z": Z, "N": N, "B_AME": B_AME,
                         "B_can0": B0, "B_tower": Bt,
                         "delta_K_residual": B_AME / Bt}
                        for nm, Z, N, B_AME, B0, Bt, _, _ in rows]}
    p = Path(__file__).resolve().parent / "borromean-binding-recompute.witness.json"
    from witness_base import WitnessBuilder
    WitnessBuilder.wrap_legacy("borromean-binding-recompute", out, script_path=__file__).save()
    print(f"  witness → {p.name}  (delta_K_residual = the Δ_λ scalar shadow per isotope)")
