#!/usr/bin/env python3
"""
Fresh p/n from γγ + SDP, EXACT via BFS (not greedy).

H_3(q) has 6 basis elements at most, but the operators σ_0, σ_1, σ_0⁻¹,
σ_1⁻¹ generate the full algebra.  In the 2-dim standard block, the
Hoefsmit matrices are 2×2, and a BFS over "reachable states" from
M_γγ using these four operators explores the orbit exactly.

Exact shortest-path metric: minimum number of operators needed to
transform M_γγ_block → M_target_block (to within Frobenius tolerance).

Total Hecke energy = Σ_blocks  min_cost_path_in_block · E(λ) per-op.

Since HeckeElements are infinite in scope but the PARTICLE-target
matrices are fixed (finite), we BFS over continuous matrices up to
a tolerance.  For convergence within reasonable time, cap BFS depth.
If no path found at the cap, fall back to greedy.
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from collections import deque
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
from hecke_characters import (build_seminormal_matrices, dim_q,
                                partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
HA = float(H_A_VAL)


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


def apply_word(word, sigmas, dim):
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for c, d, g in word:
        if g >= len(sigmas):
            return I
        F = c * sigmas[g] + d * I
        M = M @ F
    return M


def gamma_gamma_matrix(shape):
    sigmas, dim = hecke_rep_at_q0(shape)
    I = np.eye(dim, dtype=complex)
    M = I.copy() + (sigmas[0] if len(sigmas) > 0 else 0)
    if len(sigmas) > 1:
        M = M + sigmas[1] + sigmas[0] @ sigmas[1]
    return M, dim, sigmas


def build_particle_word(g0, g1):
    word = []
    for c, d in g0:
        word.append((c, d, 0))
    for c, d in g1:
        word.append((c, d, 1))
    return word


def bfs_shortest_op_path(M_source, M_target, sigmas, dim,
                            max_depth: int = 16,
                            tol: float = 1e-8):
    """BFS over operator sequences in {+0, +1, -0, -1} to find the
    shortest path from M_source to M_target (up to Frobenius tol).

    Since the state space is continuous, two states are considered
    equal if ||M_1 − M_2|| < tol.  Caches visited states by hashing
    rounded matrix entries to avoid exponential blow-up.
    """
    I = np.eye(dim, dtype=complex)
    ops = {}
    if len(sigmas) >= 1:
        ops["+0"] = sigmas[0]
        ops["-0"] = sigmas[0] - HA * I
    if len(sigmas) >= 2:
        ops["+1"] = sigmas[1]
        ops["-1"] = sigmas[1] - HA * I

    def key(M):
        # Round to tol precision for hashing
        R = np.round(M / tol).astype(np.int64)
        return R.tobytes()

    start_key = key(M_source)
    target_key = key(M_target)

    # Early exit
    if np.linalg.norm(M_source - M_target) < tol:
        return [], 0.0

    visited = {start_key}
    queue = deque([(M_source, [])])

    best = None
    while queue:
        M, seq = queue.popleft()
        if len(seq) >= max_depth:
            continue
        for op_name, F in ops.items():
            M_new = M @ F
            new_seq = seq + [op_name]
            res = np.linalg.norm(M_new - M_target)
            if res < tol:
                return new_seq, res
            k = key(M_new)
            if k in visited:
                continue
            visited.add(k)
            queue.append((M_new, new_seq))
        if len(visited) > 50000:
            # Guard against blow-up
            break
    # No exact path: return greedy-style nearest state at depth limit
    # (signal failure with None sequence)
    return None, float('inf')


def greedy_fallback(M_source, M_target, sigmas, dim, max_ops=30):
    I = np.eye(dim, dtype=complex)
    ops = {"+0": sigmas[0] if sigmas else I,
            "+1": sigmas[1] if len(sigmas) > 1 else I,
            "-0": (sigmas[0] - HA * I) if sigmas else I,
            "-1": (sigmas[1] - HA * I) if len(sigmas) > 1 else I}
    M = M_source.copy()
    seq = []
    for _ in range(max_ops):
        best = None
        for k, F in ops.items():
            d = np.linalg.norm(M @ F - M_target)
            if best is None or d < best[0]:
                best = (d, k, M @ F)
        seq.append(best[1])
        M = best[2]
        if best[0] < 1e-10:
            break
    return seq, np.linalg.norm(M - M_target)


def _hbar_sq():
    hbar = (Q0 - mp.mpf(1)) / Q0
    return hbar * hbar


def hecke_energy_of_op(op_name, shape):
    """Level-0 Plancherel + level-1 jet-tower cost per operator."""
    nfac = q_fact(sum(shape))
    dq = mp.mpf(str(float(dim_q(shape))))
    d_cl = classical_dim(shape)
    E0 = mp.fabs(dq - 1) / nfac
    hbar2 = _hbar_sq()
    if d_cl == 1 and len(shape) == 1:
        chi_m1 = Q0 - mp.mpf(1)
    elif d_cl == 1 and shape == tuple([1] * sum(shape)):
        chi_m1 = mp.mpf(1) + mp.mpf(1) / Q0
    else:
        chi_m1 = mp.mpf(0)
    E1 = hbar2 * mp.fabs(chi_m1)
    base = E0 + E1
    if op_name[0] == '-':
        base = base * (mp.mpf(1) + mp.mpf(HA))
    return base


def process_target(name, word_target, m_codata):
    print(f"\n{'=' * 100}")
    print(f"{name} — target m_codata = {m_codata} MeV")
    print('=' * 100)
    print(f"  {'λ':<10} {'dim':>4} {'bfs_depth':>10} {'residual':>14} "
          f"{'method':<8} {'total_Eλ':>14}")
    per_block = {}
    total = mp.mpf(0)
    for shape in sorted(partitions_of(3), key=lambda s: -sum(s)):
        M_gg, dim, sigmas = gamma_gamma_matrix(shape)
        if dim == 0:
            continue
        M_target = apply_word(word_target, sigmas, dim)
        seq, res = bfs_shortest_op_path(M_gg, M_target, sigmas, dim,
                                          max_depth=12, tol=1e-6)
        method = "BFS"
        if seq is None:
            method = "greedy"
            seq, res = greedy_fallback(M_gg, M_target, sigmas, dim,
                                         max_ops=30)
        E_block = mp.mpf(0)
        for op in seq:
            E_block += hecke_energy_of_op(op, shape)
        total += E_block
        print(f"  {str(shape):<10} {dim:>4} {len(seq):>10} "
              f"{res:>14.4e} {method:<8} {float(E_block):>14.6e}")
        per_block[str(list(shape))] = {
            "dim": dim, "sequence": seq, "residual": res,
            "method": method, "hecke_energy": mp.nstr(E_block, 20),
        }
    print(f"\n  TOTAL E (γγ → {name}) = {mp.nstr(total, 15)}")
    return {"name": name, "m_codata": m_codata, "per_block": per_block,
            "total_hecke_energy": mp.nstr(total, 25)}


def main() -> int:
    print("=" * 100)
    print("FRESH DERIVATION γγ + SDP via BFS (exact shortest path)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")

    # Target words
    w_e = [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)]       # trefoil
    w_p = build_particle_word(_PROTON_G0,  _PROTON_G1)
    w_n = build_particle_word(_NEUTRON_G0, _NEUTRON_G1)

    e = process_target("ELECTRON", w_e, M_E_MEV)
    p = process_target("PROTON",   w_p, M_P_MEV)
    n = process_target("NEUTRON",  w_n, M_N_MEV)

    print(f"\n{'=' * 100}")
    print("CALIBRATED via m = (E_target / E_electron) · m_e")
    print('=' * 100)
    e_E = mp.mpf(e["total_hecke_energy"])
    p_E = mp.mpf(p["total_hecke_energy"])
    n_E = mp.mpf(n["total_hecke_energy"])
    print(f"  E_γγ→e⁻ = {mp.nstr(e_E, 15)}")
    print(f"  E_γγ→p  = {mp.nstr(p_E, 15)}")
    print(f"  E_γγ→n  = {mp.nstr(n_E, 15)}")
    if e_E > 0:
        m_p_fresh = (p_E / e_E) * mp.mpf(str(M_E_MEV))
        m_n_fresh = (n_E / e_E) * mp.mpf(str(M_E_MEV))
        print(f"  m_p = (E_p/E_e)·m_e = {float(m_p_fresh):.6f} MeV "
              f"(CODATA {M_P_MEV},  err {(float(m_p_fresh)-M_P_MEV)/M_P_MEV*100:+.3f}%)")
        print(f"  m_n = (E_n/E_e)·m_e = {float(m_n_fresh):.6f} MeV "
              f"(CODATA {M_N_MEV},  err {(float(m_n_fresh)-M_N_MEV)/M_N_MEV*100:+.3f}%)")
    if n_E > 0:
        ratio = p_E / n_E
        print(f"  ratio p/n          = {float(ratio):.6f}  "
              f"(CODATA {M_P_MEV/M_N_MEV:.6f})")

    witness = {
        "computation": "fresh-derivation-gamma-gamma-bfs",
        "description": (
            "Fresh γγ → target Hecke-energy via BFS exact shortest-path "
            "over {σ_0±, σ_1±} operators on Wedderburn blocks, with "
            "greedy fallback when BFS exceeds depth/state budget.  "
            "Level-0 Plancherel + level-1 jet-tower cost per operator.  "
            "Calibrated via m = (E_target/E_electron)·m_e."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "electron": e,
        "proton": p,
        "neutron": n,
    }
    out = Path(__file__).parent / "fresh-derivation-gamma-gamma-bfs.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
