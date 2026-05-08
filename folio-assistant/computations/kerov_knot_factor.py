#!/usr/bin/env python3
"""
Entanglement Markov chain (Kerov q-hook walk) as a knot factor for
proton/neutron.

Paper reference: mass-formula-validation.md lines 134-148.  The knot
factor is described as the "path probability ratio" of the nuclear
braid's specific entanglement path to the q-Plancherel average.

Hypothesis: if the Kerov knot factor K(ρ) captures the entanglement
imbalance between proton and neutron, then (μ_d − μ_u) may emerge
from K(n)/K(p) at q_0 without any hadronic calibration.

Formula tried:

  At q₀, for each particle ρ with braid β_ρ, the projection onto
  H_3(q) block λ has character χ_λ(β_ρ).  The "entanglement
  probability" at block λ is

      p_λ(ρ) = |χ_λ(β_ρ)|² · d_q(λ)² / Z(ρ),
      Z(ρ)   = Σ_μ |χ_μ(β_ρ)|² · d_q(μ)².

  Equilibrium (Plancherel) distribution:
      π_λ = d_q(λ)² / [n]_q!

  Knot factor (geometric mean of path ratio weighted by Plancherel):
      K(ρ) = Π_λ (p_λ(ρ) / π_λ)^{π_λ}

  Alternative:  arithmetic Kullback-Leibler divergence
      D_KL(ρ || π) = Σ_λ p_λ(ρ) ln(p_λ(ρ) / π_λ)

  Observable predicted:
      m_n/m_p - 1 ≈ K(n)/K(p) - 1
      or
      μ_d - μ_u ≈ (prefactor) · [K(n) - K(p)]

Run and compare to CODATA ratio m_n/m_p = 1.00138 and Δm = 1.293 MeV.
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath as mp

mp.mp.dps = 40

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from hecke_characters import (build_seminormal_matrices, dim_q,
                                partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP


def q_int(k):
    return (Q0**k - QI**k) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def chi_lambda(shape, word):
    """χ_λ(β) via Hoefsmit matrix product at q₀."""
    sigmas_sym, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpc(0)
    q_sym = sp.Symbol('q')
    sigmas_num = []
    for S in sigmas_sym:
        try:
            fn = sp.lambdify(q_sym, sp.Matrix(S), modules='numpy')
            M = np.asarray(fn(complex(Q0_FLOAT)), dtype=complex)
        except Exception:
            M = np.zeros((dim, dim), dtype=complex)
            for i in range(dim):
                for j in range(dim):
                    e = S[i, j]
                    if hasattr(e, 'subs'):
                        M[i, j] = complex(sp.N(e.subs(q_sym, float(Q0_FLOAT))))
                    else:
                        M[i, j] = complex(e)
        sigmas_num.append(M)
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for (c, d, gen) in word:
        if gen >= len(sigmas_num):
            return mp.mpc(0)
        F = c * sigmas_num[gen] + d * I
        M = M @ F
    return mp.mpc(complex(np.trace(M)))


def build_particle_word(g0, g1):
    w = []
    for c, d in g0:
        w.append((c, d, 0))
    for c, d in g1:
        w.append((c, d, 1))
    return w


def kerov_knot_factor(word, n=3) -> dict:
    """Compute Kerov walk knot factor for a braid word."""
    nfac = q_fact(n)
    # Equilibrium distribution (q-Plancherel)
    parts = list(partitions_of(n))
    pi = {}
    for shape in parts:
        dq = mp.mpf(str(float(dim_q(shape))))
        pi[shape] = dq * dq / nfac
    pi_sum = sum(pi.values())
    # Normalize if numerical drift (should be exact = 1 in Plancherel)
    # but at q ≠ 1 the sum may not be 1; verify.
    # Block character probabilities |χ_λ(β)|² · d_q²  (not normalised yet)
    p_raw = {}
    chi_vals = {}
    for shape in parts:
        dq = mp.mpf(str(float(dim_q(shape))))
        chi = chi_lambda(shape, word)
        chi_vals[shape] = chi
        abs2 = chi.real * chi.real + chi.imag * chi.imag
        p_raw[shape] = abs2 * dq * dq
    Z = sum(p_raw.values())
    p = {shape: v / Z for shape, v in p_raw.items()}
    # Knot factor via geometric mean weighted by π
    logK = mp.mpf(0)
    for shape in parts:
        if p[shape] > mp.mpf("1e-50") and pi[shape] > mp.mpf("1e-50"):
            logK += pi[shape] * mp.log(p[shape] / pi[shape])
    K_geom = mp.exp(logK)
    # KL divergence
    D_KL = mp.mpf(0)
    for shape in parts:
        if p[shape] > mp.mpf("1e-50"):
            D_KL += p[shape] * mp.log(p[shape] / pi[shape])
    return {
        "pi": {str(list(s)): mp.nstr(v, 20) for s, v in pi.items()},
        "pi_sum": mp.nstr(pi_sum, 20),
        "p": {str(list(s)): mp.nstr(v, 20) for s, v in p.items()},
        "chi_re": {str(list(s)): float(c.real) for s, c in chi_vals.items()},
        "chi_im": {str(list(s)): float(c.imag) for s, c in chi_vals.items()},
        "Z": mp.nstr(Z, 20),
        "K_geom": mp.nstr(K_geom, 25),
        "D_KL": mp.nstr(D_KL, 25),
        "logK": mp.nstr(logK, 25),
    }


def main() -> int:
    print("=" * 100)
    print("KEROV q-HOOK WALK KNOT FACTOR for proton / neutron")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  [3]_q! = {mp.nstr(q_fact(3), 20)}")
    print()
    # Equilibrium check
    print("  Plancherel distribution π_λ:")
    nfac = q_fact(3)
    for shape in sorted(partitions_of(3), key=lambda s: -sum(s)):
        dq = mp.mpf(str(float(dim_q(shape))))
        pi_val = dq * dq / nfac
        print(f"    λ = {str(shape):<12}  d_q = {float(dq):>8.4f}  "
              f"π_λ = {float(pi_val):>10.6f}")
    total = sum(mp.mpf(str(float(dim_q(s))))**2 / nfac
                 for s in partitions_of(3))
    print(f"  Σ π_λ = {float(total):.10f}  "
          f"(should = 1 at q=1; at q_0 deviates by d_q vs d_cl mismatch)")

    p_word = build_particle_word(_PROTON_G0,  _PROTON_G1)
    n_word = build_particle_word(_NEUTRON_G0, _NEUTRON_G1)

    p = kerov_knot_factor(p_word)
    n_ = kerov_knot_factor(n_word)

    print(f"\n{'─' * 100}")
    print("PROTON (uud)")
    print('─' * 100)
    for k, v in p.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for kk, vv in v.items():
                print(f"     {kk}: {vv}")
        else:
            print(f"  {k}: {v}")

    print(f"\n{'─' * 100}")
    print("NEUTRON (udd)")
    print('─' * 100)
    for k, v in n_.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for kk, vv in v.items():
                print(f"     {kk}: {vv}")
        else:
            print(f"  {k}: {v}")

    print(f"\n{'═' * 100}")
    print("COMPARISONS")
    print('═' * 100)
    K_p = mp.mpf(p["K_geom"])
    K_n = mp.mpf(n_["K_geom"])
    D_p = mp.mpf(p["D_KL"])
    D_n = mp.mpf(n_["D_KL"])
    logK_p = mp.mpf(p["logK"])
    logK_n = mp.mpf(n_["logK"])

    print(f"  K_geom(p) = {float(K_p):.10f}")
    print(f"  K_geom(n) = {float(K_n):.10f}")
    print(f"  K_n / K_p = {float(K_n / K_p):.10f}  (CODATA m_n/m_p = "
          f"{M_N_MEV / M_P_MEV:.10f})")
    print(f"  K_n - K_p = {float(K_n - K_p):.10f}")
    print()
    print(f"  D_KL(p || π) = {float(D_p):.6e}")
    print(f"  D_KL(n || π) = {float(D_n):.6e}")
    print(f"  D_KL(n) - D_KL(p) = {float(D_n - D_p):.6e}")
    print()
    print(f"  logK(p) = {float(logK_p):.6e}")
    print(f"  logK(n) = {float(logK_n):.6e}")
    print(f"  logK(n) - logK(p) = {float(logK_n - logK_p):.6e}")
    print()
    delta_m = M_N_MEV - M_P_MEV
    print(f"  CODATA m_n − m_p = {delta_m:.6f} MeV")
    # Test: does scaling by m_e reproduce Δm?
    for scaling_name, scaling in [
        ("m_e",                    mp.mpf(str(M_E_MEV))),
        ("m_e · (q+q⁻¹)",         mp.mpf(str(M_E_MEV)) * (Q0 + QI)),
        ("m_e · [3]_q!",           mp.mpf(str(M_E_MEV)) * q_fact(3)),
        ("m_e · [2]_q · [3]_q",    mp.mpf(str(M_E_MEV)) * (Q0+QI)
                                     * (Q0**2 + 1 + QI**2)),
    ]:
        # Does scaling · (logK(n) - logK(p)) give Δm?
        dlog = logK_n - logK_p
        dKL = D_n - D_p
        dK = K_n - K_p
        for name, quantity in [
            ("Δ logK", dlog), ("Δ D_KL", dKL), ("Δ K", dK)
        ]:
            predicted = scaling * quantity
            if abs(float(predicted)) > 1e-10:
                err = (float(predicted) - delta_m) / delta_m * 100
                print(f"    {scaling_name:<22} · {name:<10} = "
                      f"{float(predicted):+10.4f} MeV  "
                      f"err vs Δm = {err:+.2f}%")

    witness = {
        "computation": "kerov-knot-factor",
        "description": (
            "Kerov q-hook walk entanglement knot factor for proton and "
            "neutron.  K_geom(ρ) = exp Σ π_λ ln(p_λ(ρ)/π_λ) where "
            "p_λ(ρ) = |χ_λ(β_ρ)|²·d_q² / Σ, π_λ = d_q²/[n]_q! is the "
            "q-Plancherel equilibrium.  Tests whether Δm_n_p emerges "
            "from (K(n) − K(p)) · (m_e · q-prefactor), no hadronic "
            "calibration."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "proton": p,
        "neutron": n_,
        "CODATA_delta_m_MeV": delta_m,
    }
    out = Path(__file__).parent / "kerov-knot-factor.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
