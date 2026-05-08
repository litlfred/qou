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

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath as mp

mp.mp.dps = 40

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL,
)
from hecke_characters import (build_seminormal_matrices, dim_q, qfac,
                                partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
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


def _hbar_sq():
    """ℏ_q² = ((q − 1)/q)²  — jet-tower per-level suppression."""
    hbar = (Q0 - mp.mpf(1)) / Q0
    return hbar * hbar


def hecke_energy_of_op(op_name, shape):
    """Per-operator Hecke energy in block λ, with jet-tower / GB-
    filtration contribution for 1-dim blocks.

    Base (level-0 Plancherel-derived):
        E_0(λ) = |d_q(λ) − 1| / [n]_q!

    For multi-dim blocks (d_q > 1, like std), E_0 is non-zero and
    dominant.  For 1-dim blocks (sym, alt) d_q = 1 so E_0 = 0 —
    these blocks only carry energy through the jet-tower.

    Level-1 jet contribution (from Ω¹(A) prolongation, ℏ_q² weight):
        E_1(λ) = ℏ_q² · |χ_λ(σ) − 1|
    where χ_λ(σ) is the block character on a single generator:
      sym: χ(σ) = q       → |χ−1| = q − 1 = q·ℏ_q
      alt: χ(σ) = −1/q    → |χ−1| = 1 + 1/q
      std: already captured by E_0 (non-trivial matrix)

    Inverse generators pay extra |1 + H_A| for the σ⁻¹ = σ − H_A
    channel decomposition.
    """
    nfac = q_fact(sum(shape))
    dq = mp.mpf(str(float(dim_q(shape))))
    d_cl = classical_dim(shape)
    # Level-0 Plancherel-derived base cost
    E0 = mp.fabs(dq - 1) / nfac
    # Level-1 jet-tower cost: ℏ_q² · |χ_λ(σ) − 1|
    hbar2 = _hbar_sq()
    if d_cl == 1 and len(shape) == 1:                # sym λ = (n,)
        chi_sigma_minus_1 = Q0 - mp.mpf(1)            # q − 1 = q·ℏ_q
    elif d_cl == 1 and shape == tuple([1]*sum(shape)):   # alt λ = (1^n)
        chi_sigma_minus_1 = mp.mpf(1) + mp.mpf(1)/Q0  # 1 + 1/q
    else:
        # multi-dim: E_0 dominates; level-1 correction already
        # implicit in the matrix version.  Skip.
        chi_sigma_minus_1 = mp.mpf(0)
    E1 = hbar2 * mp.fabs(chi_sigma_minus_1)
    base = E0 + E1
    if op_name[0] == '-':
        base = base * (mp.mpf(1) + mp.mpf(HA_NUM))
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

    # Electron: β_e = σ_0·σ_1·σ_0 (trefoil).  Word has 3 factors, all on
    # alternating generators 0, 1, 0.  Provide as (c, d, gen) tuples.
    electron_word_chains = (
        [(1.0, 0.0)],          # g0 chain: σ_0 once
        [(1.0, 0.0)],          # g1 chain: σ_1 once
    )
    # Second σ_0 handled by appending after g1 in process()? No —
    # that's a 2-factor word.  We need the full trefoil σ_0·σ_1·σ_0.
    # build_particle_word stacks g0 then g1; to get σ_0·σ_1·σ_0 we
    # construct the word directly here.
    def build_electron_word():
        return [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)]
    # Wrap in the same process() signature by monkey-patching a new
    # function that skips build_particle_word.  Simpler: just call
    # process() with e chains that concatenate properly.
    # process() builds word = g0_chain as gen 0, then g1_chain as gen 1.
    # That's σ_0 · σ_1 — not σ_0·σ_1·σ_0.  So we need a bespoke call.

    # Inline version for electron:
    def process_electron(m_codata):
        print(f"\n{'=' * 110}")
        print(f"ELECTRON (trefoil β_e = σ_0·σ_1·σ_0) — target {m_codata} MeV")
        print('=' * 110)
        word_target = build_electron_word()
        per_block = {}
        total = mp.mpf(0)
        print(f"  {'λ':<10} {'dim':>4} {'seq_len':>8} {'residual':>14} "
              f"{'total_Eλ':>14}")
        for shape in sorted(partitions_of(3), key=lambda s: -sum(s)):
            M_gg, dim, sigmas = gamma_gamma_matrix(shape)
            if dim == 0:
                continue
            M_target = apply_word_on_block(word_target, sigmas, dim)
            seq, residual = fit_operator_sequence(M_gg, M_target, sigmas,
                                                    dim, max_ops=20)
            E_block = mp.mpf(0)
            for op in seq:
                E_block += hecke_energy_of_op(op, shape)
            total += E_block
            print(f"  {str(shape):<10} {dim:>4} {len(seq):>8} "
                  f"{residual:>14.4e} {float(E_block):>14.6e}")
            per_block[str(list(shape))] = {
                "dim": dim, "sequence": seq, "residual": residual,
                "hecke_energy": mp.nstr(E_block, 20),
            }
        print(f"\n  TOTAL Hecke energy (γγ → e⁻) = {mp.nstr(total, 15)}")
        return {"name": "electron", "m_codata": m_codata,
                "per_block": per_block, "total_hecke_energy": mp.nstr(total, 25)}

    e = process_electron(M_E_MEV)
    p = process("PROTON",  _PROTON_G0,  _PROTON_G1,  M_P_MEV)
    n = process("NEUTRON", _NEUTRON_G0, _NEUTRON_G1, M_N_MEV)

    print(f"\n{'=' * 110}")
    print("CALIBRATED PREFACTOR: m = (E_γγ→target / E_γγ→e⁻) · m_e")
    print('=' * 110)
    e_E = mp.mpf(e["total_hecke_energy"])
    p_E = mp.mpf(p["total_hecke_energy"])
    n_E = mp.mpf(n["total_hecke_energy"])
    print(f"  E_γγ→e⁻ = {mp.nstr(e_E, 15)}")
    print(f"  E_γγ→p  = {mp.nstr(p_E, 15)}")
    print(f"  E_γγ→n  = {mp.nstr(n_E, 15)}")
    print()
    if e_E > 0:
        m_p_fresh = (p_E / e_E) * mp.mpf(str(M_E_MEV))
        m_n_fresh = (n_E / e_E) * mp.mpf(str(M_E_MEV))
        err_p = (float(m_p_fresh) - M_P_MEV) / M_P_MEV * 100
        err_n = (float(m_n_fresh) - M_N_MEV) / M_N_MEV * 100
        print(f"  m_p_fresh = (E_p/E_e) · m_e = {float(m_p_fresh):.6f} MeV  "
              f"err = {err_p:+.2f}%  (CODATA {M_P_MEV})")
        print(f"  m_n_fresh = (E_n/E_e) · m_e = {float(m_n_fresh):.6f} MeV  "
              f"err = {err_n:+.2f}%  (CODATA {M_N_MEV})")
        print()
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
        "electron": e,
        "proton": p,
        "neutron": n,
        "calibrated_masses": {
            "m_p_fresh_MeV": float((p_E / e_E) * mp.mpf(str(M_E_MEV)))
                              if e_E > 0 else None,
            "m_n_fresh_MeV": float((n_E / e_E) * mp.mpf(str(M_E_MEV)))
                              if e_E > 0 else None,
            "err_p_pct": err_p if e_E > 0 else None,
            "err_n_pct": err_n if e_E > 0 else None,
            "ratio_pn_fresh": float(p_E / n_E) if n_E > 0 else None,
            "ratio_pn_codata": M_P_MEV / M_N_MEV,
        },
    }
    out = Path(__file__).parent / "fresh-derivation-gamma-gamma-sdp.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
