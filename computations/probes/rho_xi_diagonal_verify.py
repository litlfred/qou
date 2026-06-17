#!/usr/bin/env python3
"""Verify the sparse / diagonal-only `ρ_ξ` against the direct build (A=4).

Checks, on the A=4 (`λ⊢12`, `n_inner=9`) `_self_test` words:

  1. EXACTNESS — `rho_word_full_sparse` == dense `prod`, and `rho_word_diag` ==
     the diagonal of the dense build, for every ξ⊢9 (to ~1e-40).
  2. COMBINER IDENTITY — the A=4 combiner assembled with the **diagonal-only**
     contraction reproduces `young_seminormal.chi_young` to `<1e-25`.
  3. BLOCK-DIAGONAL-IN-V_ξ — the diagonal-only trace equals the full
     `trace_A_kron` (which sums over the off-diagonal inner index), confirming
     `A^λ_{ξν}` is block-diagonal in `V_ξ` so only `diag(ρ_ξ)` is needed.
  4. SPEEDUP — wall time of dense vs sparse vs diagonal `ρ_ξ` builds.

Run: `python3 rho_xi_diagonal_verify.py`  (minutes; no 24-min full build). No fit.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parents[1]               # computations/
AOP = HERE / "a_operator"
for p in (str(HERE), str(AOP), str(HERE / "substrate")):
    sys.path.insert(0, p)

import a_operator_categorical as aoa            # noqa: E402
import a_operator_recursive as rec              # noqa: E402
import rho_xi_diagonal as rxd                   # noqa: E402
from young_seminormal import chi_young, seminormal_sigma  # noqa: E402
from lr_coefficients import partitions_of       # noqa: E402

DPS = 50
mp.mp.dps = 60


def _seminormal_mats_shim(lam, q_str, dps):
    """Pure-Python `exact_seminormal_matrices` (no native wheel) for verifying."""
    qq = mp.mpf(q_str)
    n = sum(lam)
    mats = [seminormal_sigma(tuple(lam), i, qq) for i in range(1, n)]
    return mats, (mats[0].rows if mats else 1)


# The native pyhecke wheel is absent in this container; route the seminormal
# builder used by interface_blocks' ν-alignment + the dense reference through the
# pure-Python young_seminormal rule (same convention as chi_young).
aoa.exact_seminormal_matrices = _seminormal_mats_shim


def dense_prod(mats, word):
    """Reference dense `ρ_ξ(word) = ∏ (c·σ_g + d·I)` (the crosscheck's `prod`)."""
    M = mp.eye(mats[0].rows)
    eye = mp.eye(mats[0].rows)
    for (c, d, g) in word:
        M = M * (c * mats[g] + d * eye)
    return M


def trace_full(A, RWx, RBn, d_mu, d_nu):
    """The crosscheck's `trace_A_kron` (sums over the off-diagonal inner index)."""
    s = mp.mpf(0)
    for a in range(d_mu):
        for ap in range(d_mu):
            rwa = RWx[ap, a]
            if rwa == 0:
                continue
            for b in range(d_nu):
                for bp in range(d_nu):
                    rbb = RBn[bp, b]
                    if rbb != 0:
                        s += A[a * d_nu + b, ap * d_nu + bp] * rwa * rbb
    return s


def trace_diag(A, diag_RW, RBn, d_mu, d_nu):
    """Diagonal-only contraction — uses only `diag(ρ_ξ)`."""
    s = mp.mpf(0)
    for a in range(d_mu):
        ra = diag_RW[a]
        if ra == 0:
            continue
        for b in range(d_nu):
            for bp in range(d_nu):
                rbb = RBn[bp, b]
                if rbb != 0:
                    s += A[a * d_nu + b, a * d_nu + bp] * ra * rbb
    return s


def main() -> int:
    q = aoa.q0_mp(DPS)
    q_str = mp.nstr(q, DPS)
    h = q - 1 / q

    def fac(br):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, g) for (s, g) in br]

    inner = [(1, 0), (1, 3), (-1, 5), (1, 7), (1, 1)]    # generic H_9 inner word
    block = [(1, 0), (-1, 1)]                            # H_3 block word
    finner = fac(inner)
    fblock = fac(block)

    print("=" * 74)
    print(" Verify sparse / diagonal-only ρ_ξ vs direct build (A=4, ξ⊢9)")
    print("=" * 74)

    # (1) exactness + timing, per ξ⊢9
    worst_full = mp.mpf(0)
    worst_diag = mp.mpf(0)
    t_dense = t_sparse = t_diag = 0.0
    RW_diag = {}
    RW_full = {}
    d_max = 0
    for xi in partitions_of(9):
        mats, d = aoa.exact_seminormal_matrices(xi, q_str, DPS)
        d_max = max(d_max, d)
        t = time.time(); Md = dense_prod(mats, finner); t_dense += time.time() - t
        t = time.time(); Ms, _ = rxd.rho_word_full_sparse(xi, q_str, DPS, finner); t_sparse += time.time() - t
        t = time.time(); dg, _ = rxd.rho_word_diag(xi, q_str, DPS, finner); t_diag += time.time() - t
        RW_diag[xi] = dg
        RW_full[xi] = Ms
        worst_full = max(worst_full, max(abs(Ms[i, j] - Md[i, j])
                         for i in range(d) for j in range(d)))
        worst_diag = max(worst_diag, max(abs(dg[i] - Md[i, i]) for i in range(d)))

    print(f" 1. EXACTNESS (ξ⊢9, d_ξ≤{d_max}):")
    print(f"      max|full_sparse − dense|     = {mp.nstr(worst_full, 4)}")
    print(f"      max|diag − dense.diagonal|   = {mp.nstr(worst_diag, 4)}")
    print(f" 4. SPEEDUP (all ξ⊢9, {len(inner)}-crossing inner word):")
    print(f"      dense  prod  = {t_dense:7.2f}s")
    print(f"      sparse full  = {t_sparse:7.2f}s   ({t_dense / max(t_sparse,1e-9):.1f}× vs dense)")
    print(f"      diagonal     = {t_diag:7.2f}s   ({t_dense / max(t_diag,1e-9):.1f}× vs dense)")

    # (2)+(3) combiner identity (diag-only) vs chi_young; diag-only vs full trace
    RB = {nu: dense_prod(aoa.exact_seminormal_matrices(nu, q_str, DPS)[0], fblock)
          for nu in partitions_of(3)}
    worst_id = mp.mpf(0)
    worst_df = mp.mpf(0)
    for lam in [(10, 2), (11, 1), (7, 5)]:
        full = finner + [(mp.mpf(1), -h / 2, 8)] + [(c, d, g + 9) for (c, d, g) in fblock]
        lhs = chi_young(lam, full, q)
        blocks = rec.interface_blocks(lam, 9, 3, q_str, -h / 2, DPS)
        rhs_diag = mp.mpf(0)
        rhs_full = mp.mpf(0)
        for (xi, nu), info in blocks.items():
            A, d_mu, d_nu = info["A"], info["d_mu"], info["d_nu"]
            rhs_diag += trace_diag(A, RW_diag[xi], RB[nu], d_mu, d_nu)
            rhs_full += trace_full(A, RW_full[xi], RB[nu], d_mu, d_nu)
        worst_id = max(worst_id, abs(lhs - rhs_diag))
        worst_df = max(worst_df, abs(rhs_diag - rhs_full))

    print(" 2. COMBINER IDENTITY (diag-only vs chi_young, λ∈{(10,2),(11,1),(7,5)}):")
    print(f"      max|chi_young − rhs_diag|    = {mp.nstr(worst_id, 4)}"
          f"   {'OK' if worst_id < mp.mpf(10) ** -25 else 'FAIL'}")
    print(" 3. BLOCK-DIAGONAL-IN-V_ξ (diag-only trace vs full trace):")
    print(f"      max|rhs_diag − rhs_full|     = {mp.nstr(worst_df, 4)}"
          f"   {'OK (only diag needed)' if worst_df < mp.mpf(10) ** -25 else 'FAIL'}")

    ok = worst_full < mp.mpf(10) ** -30 and worst_diag < mp.mpf(10) ** -30 \
        and worst_id < mp.mpf(10) ** -25 and worst_df < mp.mpf(10) ** -25
    print("\n VERDICT:", "PASS — diagonal-only ρ_ξ is exact; only diag(ρ_ξ) is"
          " needed; sparse/diag are faster." if ok else "FAIL — see above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
