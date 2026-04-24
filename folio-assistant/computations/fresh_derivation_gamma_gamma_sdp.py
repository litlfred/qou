#!/usr/bin/env python3
"""
Fresh p/n derivation from γγ pair production with SDP selection.

User's Q4: "rederive construction from γγ with SDP".

Setup:
  Initial state: two photons γ₁γ₂ produce a specific Hecke element
  ε_γγ in H_3(q) whose NF was computed in
  breit-wheeler-nucleon-nf.witness.json:
      γ = 𝟙 + φ·σ_0 + φ·σ_1   (symmetric polarization)
      γγ = (𝟙 + φ·σ_0)(𝟙 + φ·σ_1) NF

  Target state: proton β_p (uud) or neutron β_n (udd) at NF.

  SDP selection: identify the set of Hecke-generator operations
  {σ_0, σ_1, σ_0⁻¹, σ_1⁻¹} that, when applied to γγ with minimum
  Hecke energy, produces the proton/neutron NF.

This script implements a FIRST-ORDER version:

  1. Compute γγ NF at q₀ (using breit-wheeler machinery).
  2. Compute β_p, β_n NFs at q₀.
  3. For each target, solve the LP:
        min  Σ_i |a_i| · c_i      (Hecke-energy-weighted operator count)
        s.t. γγ · (σ_0)^{a_0} · (σ_0⁻¹)^{b_0}
                · (σ_1)^{a_1} · (σ_1⁻¹)^{b_1} = β_target
                a_i, b_i ≥ 0 integers
     Relax to LP over reals, extract optimal cost as mass proxy.

  4. Construct m_fresh = (overall_prefactor) · (LP_optimal_cost).

LIMITATIONS:
  - The equality γγ · op_sequence = β_target is a SYMBOLIC constraint
    in H_3(q); we cannot directly solve it via LP on just 4 integer
    counts.  Instead we solve for the LEAST-SQUARES operator mixture
    that approximates the transition — a proxy for the SDP.
  - For a proper SDP, we would need matrix-valued operator variables
    on each partition block (sym, std, alt) subject to PSD.  This is
    deferred (requires cvxpy + careful formulation).
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
import mpmath as mp

mp.mp.dps = 40

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL,
)
from hecke_characters import (build_seminormal_matrices, dim_q, qfac,
                                partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


Q0 = mp.mpf(str(Q0_FLOAT))
QI = mp.mpf(1) / Q0
HA_NUM = float(H_A_VAL)


def q_int(k):
    return (Q0**k - QI**k) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def classical_dim(shape):
    n = sum(shape)
    hooks = young_hooks(shape)
    fact_n = mp.mpf(1)
    for k in range(1, n + 1):
        fact_n *= k
    hp = mp.mpf(1)
    for h in hooks:
        hp *= h
    return fact_n / hp


def hecke_rep_at_q0(shape):
    """Build Hoefsmit σ_i matrices at q=q₀ as numpy complex arrays."""
    sigmas_sym, dim, _ = build_seminormal_matrices(shape)
    q_sym = sp.Symbol('q')
    out = []
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
        out.append(M)
    return out, dim


def apply_word_on_block(word, sigmas, dim):
    """Apply a Hecke word (list of (c, d, gen)) to identity in block."""
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for c, d, g in word:
        if g >= len(sigmas):
            return I  # trivial
        F = c * sigmas[g] + d * I
        M = M @ F
    return M


def apply_operator_sequence(word, seq, sigmas, dim):
    """Apply Hecke generator sequence like ['+0','+1','-0','-1'] to M."""
    I = np.eye(dim, dtype=complex)
    M = apply_word_on_block(word, sigmas, dim)
    for op in seq:
        sign = +1 if op[0] == '+' else -1
        gen = int(op[1:])
        if gen >= len(sigmas):
            continue
        if sign == +1:
            F = sigmas[gen]
        else:
            # σ_i⁻¹ = σ_i − (q − q⁻¹) · I
            F = sigmas[gen] - HA_NUM * I
        M = M @ F
    return M


def gamma_gamma_ops_symmetric():
    """γγ in H_3(q) with symmetric polarization:
       γ = 𝟙 + φ·σ_0 + φ·σ_1
       γγ = (𝟙 + φ·σ_0)(𝟙 + φ·σ_1)
       Truncate to φ=1 for simplicity (pure combinatorial content):
       γγ = 𝟙 + σ_0 + σ_1 + σ_0·σ_1
    """
    # As a Hecke word list: we have 4 basis contributions
    # For the LP we want the NF matrix in each block.
    return [
        ("𝟙",         []),
        ("σ_0",       [(1.0, 0.0, 0)]),
        ("σ_1",       [(1.0, 0.0, 1)]),
        ("σ_0·σ_1",   [(1.0, 0.0, 0), (1.0, 0.0, 1)]),
    ]


def gamma_gamma_matrix(shape):
    """γγ matrix in λ-Wedderburn block: sum of the 4 basis ops."""
    sigmas, dim = hecke_rep_at_q0(shape)
    I = np.eye(dim, dtype=complex)
    M = I.copy() + sigmas[0] + (sigmas[1] if len(sigmas) > 1 else I)
    if len(sigmas) > 1:
        M += sigmas[0] @ sigmas[1]
    return M, dim, sigmas


def build_particle_word(g0, g1):
    word = []
    for c, d in g0:
        word.append((c, d, 0))
    for c, d in g1:
        word.append((c, d, 1))
    return word


def fit_operator_sequence(M_source, M_target, sigmas, dim, max_ops=12):
    """Find operator sequence σ_0^±1, σ_1^±1 that transforms M_source → M_target.

    Uses a greedy basin-search: at each step pick operator minimising
    Frobenius distance to target.  Not an SDP proper, but a cheap
    sandbox for the LP idea.

    Returns (sequence, final_residual).
    """
    I = np.eye(dim, dtype=complex)
    ops = {
        "+0": sigmas[0] if len(sigmas) > 0 else I,
        "+1": sigmas[1] if len(sigmas) > 1 else I,
        "-0": (sigmas[0] - HA_NUM * I) if len(sigmas) > 0 else I,
        "-1": (sigmas[1] - HA_NUM * I) if len(sigmas) > 1 else I,
    }
    M = M_source.copy()
    seq = []
    for step in range(max_ops):
        best = None
        best_op = None
        for k, F in ops.items():
            M_try = M @ F
            d = np.linalg.norm(M_try - M_target)
            if best is None or d < best:
                best = d
                best_op = k
                best_M = M_try
        seq.append(best_op)
        M = best_M
        residual = np.linalg.norm(M - M_target)
        if residual < 1e-10:
            break
    return seq, np.linalg.norm(M - M_target)


def hecke_energy_of_op(op_name, shape):
    """Per-operator Hecke energy in block λ.

    Use |y_λ(q)| = |d_q(λ)/[n]_q! − 1/[n]_q!| (Plancherel-derived
    shadow price).  Operators σ_0, σ_1 at a single block pay the same
    cost (block-uniform).  σ^-1 costs more (by factor |1 + H_A|).
    """
    nfac = q_fact(sum(shape))
    dq = mp.mpf(str(float(dim_q(shape))))
    base = mp.fabs(dq - 1) / nfac
    if op_name[0] == '-':
        return base * (mp.mpf(1) + mp.mpf(HA_NUM))
    return base


def process(name, g0, g1, m_codata, n=3):
    print(f"\n{'=' * 110}")
    print(f"{name} — target m_codata = {m_codata} MeV")
    print('=' * 110)
    word_target = build_particle_word(g0, g1)

    print(f"  LP-on-Hecke-blocks: γγ → {name} sequence fitting")
    print(f"  {'λ':<10} {'dim':>4} {'seq_len':>8} {'residual':>14} "
          f"{'total_Eλ':>14}")

    per_block = {}
    total_E_LP = mp.mpf(0)
    for shape in sorted(partitions_of(n), key=lambda s: -sum(s)):
        M_gg, dim, sigmas = gamma_gamma_matrix(shape)
        if dim == 0:
            continue
        M_target = apply_word_on_block(word_target, sigmas, dim)
        seq, residual = fit_operator_sequence(M_gg, M_target, sigmas,
                                                dim, max_ops=20)
        E_block = mp.mpf(0)
        for op in seq:
            E_block += hecke_energy_of_op(op, shape)
        total_E_LP += E_block
        print(f"  {str(shape):<10} {dim:>4} {len(seq):>8} "
              f"{residual:>14.4e} {float(E_block):>14.6e}")
        per_block[str(list(shape))] = {
            "dim": dim,
            "sequence": seq,
            "residual": residual,
            "hecke_energy": mp.nstr(E_block, 20),
        }

    print(f"\n  TOTAL Hecke energy (γγ → {name}): {mp.nstr(total_E_LP, 15)}")
    print(f"\n  Prefactor candidates:")
    for pname, pv in [
        ("m_e",             mp.mpf(str(M_E_MEV))),
        ("m_e · 8G",        mp.mpf(str(M_E_MEV)) * 8 *
                              mp.mpf("0.915965594177")),
        ("m_e · 2π",        mp.mpf(str(M_E_MEV)) * 2 * mp.pi),
        ("E₀ (β-decay)",    mp.mpf("417.0")),  # rough; overridden below
    ]:
        m_fresh = pv * total_E_LP
        err = (float(m_fresh) - m_codata) / m_codata * 100
        print(f"    {pname:<14} m_fresh = {float(m_fresh):+12.4f} MeV  "
              f"err = {err:+.2f}%")

    return {
        "name": name,
        "m_codata": m_codata,
        "per_block": per_block,
        "total_hecke_energy": mp.nstr(total_E_LP, 25),
    }


def main() -> int:
    print("=" * 110)
    print("FRESH DERIVATION from γγ + SDP (first-order: greedy LP proxy)")
    print("=" * 110)
    print(f"  q_0 = {Q0_FLOAT}")
    print()
    print("  γγ initial state (symmetric polarization, φ=1):")
    print("     γ = 𝟙 + σ_0 + σ_1")
    print("     γγ = 𝟙 + σ_0 + σ_1 + σ_0·σ_1")
    print()
    p = process("PROTON",  _PROTON_G0,  _PROTON_G1,  M_P_MEV)
    n = process("NEUTRON", _NEUTRON_G0, _NEUTRON_G1, M_N_MEV)

    print(f"\n{'=' * 110}")
    print("COMPARISON: proton/neutron via γγ → target Hecke-energy cost")
    print('=' * 110)
    p_E = mp.mpf(p["total_hecke_energy"])
    n_E = mp.mpf(n["total_hecke_energy"])
    print(f"  total_E_LP(γγ → p) = {mp.nstr(p_E, 15)}")
    print(f"  total_E_LP(γγ → n) = {mp.nstr(n_E, 15)}")
    if n_E > 0:
        ratio = p_E / n_E
        print(f"  ratio p/n          = {float(ratio):.6f}")
        print(f"  CODATA m_p/m_n     = {M_P_MEV/M_N_MEV:.6f}")

    witness = {
        "computation": "fresh-derivation-gamma-gamma-sdp",
        "description": (
            "Fresh p/n construction from γγ pair-production initial "
            "state using greedy LP proxy for SDP operator selection.  "
            "γγ = 𝟙 + σ_0 + σ_1 + σ_0·σ_1 in H_3(q); fit per-block "
            "Hecke-generator sequence to reach proton/neutron NF; "
            "sum Hecke energies as mass proxy.  Symmetric polarization, "
            "φ = 1.  Proper SDP deferred (requires cvxpy + matrix-"
            "valued dual variables)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "proton": p,
        "neutron": n,
    }
    out = Path(__file__).parent / "fresh-derivation-gamma-gamma-sdp.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
