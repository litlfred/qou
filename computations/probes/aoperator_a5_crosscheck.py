#!/usr/bin/env python3
"""A=5 (⁵He) end-to-end combiner cross-check via the contraction-only diagonal.

Extends the A=4 ⁴He cross-check (`a_operator_recursive_he4_crosscheck.py`,
#2405) to A=5 using the diagonal-only / contraction-only `ρ_ξ` (#2449 / #2456):
only `diag(ρ_ξ(W_inner))` is needed (A^λ_{ξν} block-diagonal in V_ξ), and at A=5
the inner factor is ξ⊢12 (`d_ξ ≤ 7700`) — too large for the 50-dps dense build
(~8 h) but feasible in **float64** (~minutes), the realistic A=5 backend per the
cost wall (`docs/audits/2026-06-17-aoperator-a6-cost-wall-contraction-only.md`).

Validation ladder:
  (A4) float64 combiner vs the EXACT `young_seminormal.chi_young` on the real
       ⁴He word (small-d λ⊢12) — confirms the float64 path itself (≈1e-10).
  (A5) float64 combiner vs the canonical fine-Bratteli transfer
       (`reduced_block_kernel.chi_all_lambda_reduced_block`) on the real ⁵He
       word, per-λ and assembled `tr_M = Σ_λ y_λ χ^λ`.

Coarse by design (float64 ≈ 1e-8 after the long word product); the point is that
the combiner KERNEL reproduces the production transfer at A=5. No production
value changes (tr_M already validated by the transfer); no fit, nothing rewired.

Run: `python3 -u aoperator_a5_crosscheck.py 2>&1 | tee /tmp/a5.log`  (minutes).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.sparse as sp

HERE = Path(__file__).resolve().parents[1]               # computations/
AOP = HERE / "a_operator"
for p in (str(HERE), str(AOP), str(HERE / "substrate")):
    sys.path.insert(0, p)

import a_operator_categorical as aoa            # noqa: E402
import a_operator_recursive as rec              # noqa: E402
import rho_xi_diagonal as rxd                   # noqa: E402
from young_seminormal import chi_young, seminormal_sigma, standard_tableaux  # noqa: E402
from lr_coefficients import partitions_of       # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0                 # noqa: E402

DPS = 50
mp.mp.dps = 60
BATCH = 256


def _shim(lam, q_str, dps):
    """Pure-Python `exact_seminormal_matrices` (no native wheel) for ν⊢3."""
    qq = mp.mpf(q_str)
    n = sum(lam)
    mats = [seminormal_sigma(tuple(lam), i, qq) for i in range(1, n)]
    return mats, (mats[0].rows if mats else 1)


aoa.exact_seminormal_matrices = _shim            # interface_blocks' ν-alignment


def peel(word, A):
    """Split the 3A word at the last-nucleon bridge (gen 3A−4); n_inner = 3A−3.

    Returns `(W_inner, I_d, block, n_inner)` with `block` shifted to 0-based
    H_3 generators, matching the A=4 cross-check convention generalised."""
    n_inner = 3 * A - 3
    bridge = 3 * A - 4
    idx = next(i for i, (c, d, g) in enumerate(word) if g == bridge)
    W_inner = word[:idx]
    I_d = word[idx][1]
    block = [(c, d, g - n_inner) for (c, d, g) in word[idx + 1:]]
    return W_inner, I_d, block, n_inner


def diag_rho_float(xi, q_str, word, batch=BATCH):
    """`diag(ρ_ξ(word))` in float64, batched sparse mat-vec. `O(d·batch)` memory."""
    nz, d = rxd.sparse_generators(xi, q_str, DPS)
    gens = []
    for e in nz:
        if e:
            rows = [i for (i, _, _) in e]
            cols = [j for (_, j, _) in e]
            vals = [float(v) for (_, _, v) in e]
            gens.append(sp.csr_matrix((vals, (rows, cols)), shape=(d, d)))
        else:
            gens.append(sp.csr_matrix((d, d)))
    rev = [(float(c), float(dc), g) for (c, dc, g) in reversed(word)]
    diag = np.zeros(d)
    for a0 in range(0, d, batch):
        cols = list(range(a0, min(a0 + batch, d)))
        V = np.zeros((d, len(cols)))
        for k, a in enumerate(cols):
            V[a, k] = 1.0
        for (c, dc, g) in rev:
            V = c * (gens[g] @ V) + dc * V
        for k, a in enumerate(cols):
            diag[a] = V[a, k]
    return diag, d


def rho_full_float(nu, q_str, word):
    """Small full float64 ρ_ν(word) for ν⊢3 (d_ν ≤ 2)."""
    qq = mp.mpf(q_str)
    n = sum(nu)
    mats = [np.array([[float(x) for x in row]
                      for row in seminormal_sigma(tuple(nu), i, qq).tolist()])
            for i in range(1, n)]
    d = mats[0].shape[0] if mats else 1
    M = np.eye(d)
    for (c, dc, g) in word:
        M = float(c) * (M @ mats[g]) + float(dc) * M
    return M


def combiner_chi_float(lam, n_inner, I_d, diags, RB, q_str):
    """χ^λ via the float64 contraction-only combiner (only diag(ρ_ξ) used)."""
    blocks = rec.interface_blocks(lam, n_inner, 3, q_str, mp.mpf(I_d), DPS)
    total = 0.0
    for (xi, nu), info in blocks.items():
        A = info["A"]
        d_mu, d_nu = info["d_mu"], info["d_nu"]
        dg = diags[xi]
        rb = RB[nu]
        for a in range(d_mu):
            da = dg[a]
            if da == 0.0:
                continue
            s = 0.0
            for b in range(d_nu):
                for bp in range(d_nu):
                    s += float(A[a * d_nu + b, a * d_nu + bp]) * rb[bp, b]
            total += da * s
    return total


def main() -> int:
    q = aoa.q0_mp(DPS)
    q_str = mp.nstr(q, DPS)
    print(f"q₀={q_str[:12]}  dps={DPS} (transfer ref) / float64 (combiner)\n", flush=True)

    # ---- (A4) float64 path self-check vs exact chi_young on the real ⁴He word ----
    w4 = atom_braid_word_3A(2, 2)
    Wi4, Id4, bl4, ni4 = peel(w4, 4)
    print(f"[A4 self-check] n_inner={ni4} |W_inner|={len(Wi4)} bridge_d={Id4:.4f}", flush=True)
    diags4 = {}
    for xi in partitions_of(ni4):
        diags4[xi], _ = diag_rho_float(xi, q_str, Wi4)
    RB4 = {nu: rho_full_float(nu, q_str, bl4) for nu in partitions_of(3)}
    worst4 = 0.0
    for lam in partitions_of(12):
        if len(standard_tableaux(lam)) > 60:
            continue
        ref = float(chi_young(lam, w4, q))
        got = combiner_chi_float(lam, ni4, Id4, diags4, RB4, q_str)
        worst4 = max(worst4, abs(got - ref))
    print(f"[A4 self-check] max|combiner_float − chi_young| (small-d λ⊢12) = {worst4:.2e}"
          f"   {'OK' if worst4 < 1e-6 else 'FAIL'}\n", flush=True)

    # ---- (A5) float64 combiner vs the fine-Bratteli transfer on the real ⁵He word ----
    w5 = atom_braid_word_3A(2, 3)
    Wi5, Id5, bl5, ni5 = peel(w5, 5)
    print(f"[A5] ⁵He n_inner={ni5} |W_inner|={len(Wi5)} bridge_d={Id5:.4f}"
          f"  #ξ⊢{ni5}={len(partitions_of(ni5))}", flush=True)
    t0 = time.time()
    diags5 = {}
    for i, xi in enumerate(partitions_of(ni5)):
        td = time.time()
        diags5[xi], d = diag_rho_float(xi, q_str, Wi5)
        if d >= 500:
            print(f"   ρ_ξ {xi} d={d}: {time.time()-td:.1f}s "
                  f"(cum {time.time()-t0:.0f}s)", flush=True)
    print(f"[A5] all ρ_ξ diagonals (float64): {time.time()-t0:.0f}s", flush=True)
    RB5 = {nu: rho_full_float(nu, q_str, bl5) for nu in partitions_of(3)}

    # transfer reference (canonical, 50 dps)
    t0 = time.time()
    chi_ref = chi_all_lambda_reduced_block(w5, 15, q=None)
    chi_ref = {tuple(k): float(v) for k, v in chi_ref.items()}
    print(f"[A5] transfer reference (all λ⊢15): {time.time()-t0:.0f}s", flush=True)

    t0 = time.time()
    chi_comb = {}
    for lam in partitions_of(15):
        chi_comb[tuple(lam)] = combiner_chi_float(lam, ni5, Id5, diags5, RB5, q_str)
    print(f"[A5] combiner all-λ χ (float64): {time.time()-t0:.0f}s", flush=True)

    worst = max(abs(chi_comb[k] - chi_ref[k]) for k in chi_comb)
    denom = max(abs(chi_ref[k]) for k in chi_ref) or 1.0
    y = {tuple(k): float(v) for k, v in y_lambda_at(15, Q0).items()}
    trM_comb = sum(y[k] * chi_comb[k] for k in chi_comb)
    trM_ref = sum(y[k] * chi_ref[k] for k in chi_ref)
    print(f"\n[A5] per-λ max|χ_comb − χ_transfer| (all {len(chi_comb)}) = {worst:.2e}"
          f"   (rel to max|χ| {worst/denom:.2e})", flush=True)
    print(f"[A5] tr_M_combiner = {trM_comb:.10g}", flush=True)
    print(f"[A5] tr_M_transfer = {trM_ref:.10g}", flush=True)
    rel = abs(trM_comb - trM_ref) / (abs(trM_ref) or 1.0)
    print(f"[A5] |Δtr_M|={abs(trM_comb-trM_ref):.2e}  rel={rel:.2e}"
          f"   {'OK — combiner reproduces transfer at A=5 (float64)' if rel < 1e-5 else 'CHECK'}",
          flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
