#!/usr/bin/env python3
"""Colored Jones via the U_q(sl₂) universal R-matrix on a braid word —
derivable, self-checked machinery, then applied to the Whitehead link.

Route 3 of the Whitehead reconstruction (branch
claude/whitehead-habiro-kashaev-lupmgo).  NO R-matrix closed form is
transcribed from memory: the braiding is assembled from the explicit
generators E, F, K of U_q(sl₂) in the N-dimensional irrep, each of whose
entries is checked against the defining relations

    K E K⁻¹ = q²E,   K F K⁻¹ = q⁻²F,   [E,F] = (K − K⁻¹)/(q − q⁻¹).

The universal R-matrix (finite sum, E/F nilpotent in a finite irrep)

    R = q^{H⊗H/2} · Σ_{n≥0} q^{n(n−1)/2} (q−q⁻¹)ⁿ/[n]! · (Eⁿ ⊗ Fⁿ)

gives the braiding Ř = P∘R.  The pipeline is then VALIDATED, not assumed:

  V1  Ř obeys the braid relation (Ř⊗1)(1⊗Ř)(Ř⊗1) = (1⊗Ř)(Ř⊗1)(1⊗Ř).
  V2  the closure invariant of the figure-eight braid (σ₁σ₂⁻¹)² reproduces
      the in-repo Habiro–Le colored Jones J_N(4₁) (numeric, generic q),
      which fixes the enhancement μ and framing normalization against a
      KNOWN object (calibration, not a fudge).
  V3  at q = e^{2πi/N} the figure-eight closure grows at rate Vol(4₁).

Only after V1–V3 pass is the same machinery applied to Whitehead-link
braid candidates, selected by the formula-free volume test → 4G.

Audit-only; no wiring.
"""
from __future__ import annotations

import cmath
import math

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402


# ────────────────────────── q-integers ──────────────────────────
def qint(n: int, q: mp.mpc) -> mp.mpc:
    """[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)."""
    if q == 1:
        return mp.mpc(n)
    return (q**n - q**(-n)) / (q - q**(-1))


def qfact(n: int, q: mp.mpc) -> mp.mpc:
    r = mp.mpc(1)
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


# ─────────────── U_q(sl₂) generators in the N-dim irrep ───────────────
def uqsl2_generators(N: int, q: mp.mpc):
    """E, F, K (as N×N mpmath matrices) on the weight basis v_0..v_{N-1}.

    Conventions (highest weight N-1):
        K v_i = q^{N-1-2i} v_i
        E v_i = [N-i]_q v_{i-1}     (E v_0 = 0)
        F v_i = [i+1]_q v_{i+1}     (F v_{N-1} = 0)
    These satisfy [E,F] = (K−K⁻¹)/(q−q⁻¹); verified in _check_relations.
    """
    E = mp.zeros(N, N)
    F = mp.zeros(N, N)
    K = mp.zeros(N, N)
    for i in range(N):
        K[i, i] = q**(N - 1 - 2 * i)
        if i - 1 >= 0:
            E[i - 1, i] = qint(N - i, q)      # E v_i = [N-i] v_{i-1}
        if i + 1 <= N - 1:
            F[i + 1, i] = qint(i + 1, q)      # F v_i = [i+1] v_{i+1}
    return E, F, K


def _check_relations(N: int, q: mp.mpc, tol=1e-30) -> bool:
    E, F, K = uqsl2_generators(N, q)
    Kinv = mp.zeros(N, N)
    for i in range(N):
        Kinv[i, i] = 1 / K[i, i]
    comm = E * F - F * E
    rhs = (K - Kinv) / (q - q**(-1))
    ok_ef = mp.mnorm(comm - rhs) < tol
    # K E K⁻¹ = q² E
    ok_ke = mp.mnorm(K * E * Kinv - q**2 * E) < tol
    ok_kf = mp.mnorm(K * F * Kinv - q**(-2) * F) < tol
    return bool(ok_ef and ok_ke and ok_kf)


# ─────────────────── universal R-matrix on V⊗V ───────────────────
def _kron(A, B):
    """Kronecker product of two mpmath matrices."""
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    out = mp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            aij = A[i, j]
            if aij == 0:
                continue
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k, j * cb + l] = aij * B[k, l]
    return out


def r_check_braiding(N: int, q: mp.mpc):
    """Return (Rcheck, Rcheck_inv) as N²×N² mpmath matrices: Ř = P∘R."""
    E, F, K = uqsl2_generators(N, q)
    Id = mp.eye(N)
    # weights w_i = N-1-2i
    w = [N - 1 - 2 * i for i in range(N)]
    # diagonal q^{H⊗H/2} on basis v_i⊗v_j
    D = mp.zeros(N * N, N * N)
    for i in range(N):
        for j in range(N):
            D[i * N + j, i * N + j] = q ** (mp.mpf(w[i] * w[j]) / 2)
    # Σ_n q^{n(n-1)/2} (q-q⁻¹)^n/[n]! E^n ⊗ F^n
    S = mp.zeros(N * N, N * N)
    En = mp.eye(N)
    Fn = mp.eye(N)
    for n in range(0, N):          # E,F nilpotent: E^N = F^N = 0
        coeff = q ** (mp.mpf(n * (n - 1)) / 2) * (q - q**(-1))**n / qfact(n, q)
        S += coeff * _kron(En, Fn)
        En = En * E
        Fn = Fn * F
    R = D * S
    # permutation P: v_i⊗v_j -> v_j⊗v_i
    P = mp.zeros(N * N, N * N)
    for i in range(N):
        for j in range(N):
            P[j * N + i, i * N + j] = 1
    Rcheck = P * R
    Rinv = _inv(Rcheck)
    return Rcheck, Rinv


def _inv(M):
    return M ** (-1)


# ─────────────── braid-group rep + closure invariant ───────────────
def braid_rep(word, m: int, N: int, Rc, Rci):
    """Represent a braid word (list of ±i, 1-based generator index) on V^{⊗m}.

    Returns the N^m × N^m mpmath matrix ρ(word).
    """
    dim = N ** m
    rho = mp.eye(dim)
    for g in word:
        i = abs(g)                      # acts on strands i, i+1 (1-based)
        block = Rc if g > 0 else Rci
        # embed block on strands (i, i+1): Id^{i-1} ⊗ block ⊗ Id^{m-i-1}
        left = mp.eye(N ** (i - 1))
        right = mp.eye(N ** (m - i - 1))
        op = _kron(_kron(left, block), right)
        rho = op * rho
    return rho


def _apply_gate_local(rho, Rc, Rci, g, N):
    """Left-multiply the N³×N³ operator `rho` by the 2-local gate for
    generator g (±1 → strands 0,1; ±2 → strands 1,2), via strided block
    matmul — O(N⁸) instead of the O(N⁹) full np.kron matmul.

    3-strand basis index x = a·N² + b·N + c (a,b,c ∈ [0,N)).
    """
    block = Rc if g > 0 else Rci               # N²×N²
    i = abs(g)                                  # 1 → (a,b), 2 → (b,c)
    dim = N ** 3
    new = mp.zeros(dim, dim)
    if i == 1:
        # gate on (a,b): group rows by fixed c
        for c in range(N):
            rows = [a * N * N + b * N + c for a in range(N) for b in range(N)]
            sub = mp.matrix(N * N, dim)
            for r, x in enumerate(rows):
                for col in range(dim):
                    sub[r, col] = rho[x, col]
            out = block * sub                   # (N²×N²)·(N²×dim)
            for r, x in enumerate(rows):
                for col in range(dim):
                    new[x, col] = out[r, col]
    else:
        # gate on (b,c): group rows by fixed a
        for a in range(N):
            rows = [a * N * N + b * N + c for b in range(N) for c in range(N)]
            sub = mp.matrix(N * N, dim)
            for r, x in enumerate(rows):
                for col in range(dim):
                    sub[r, col] = rho[x, col]
            out = block * sub
            for r, x in enumerate(rows):
                for col in range(dim):
                    new[x, col] = out[r, col]
    return new


def closure_invariant_fast(word, N, q, Rc, Rci, mu_power=1):
    """Same as closure_invariant for a 3-strand braid, but O(N⁸) per gate."""
    dim = N ** 3
    rho = mp.eye(dim)
    for g in word:
        rho = _apply_gate_local(rho, Rc, Rci, g, N)
    mu_diag = [q ** (mp.mpf(N - 1 - 2 * i) * mu_power) for i in range(N)]
    total = mp.mpc(0)
    for x in range(dim):
        weight = mp.mpc(1)
        y = x
        for _ in range(3):
            weight *= mu_diag[y % N]
            y //= N
        total += weight * rho[x, x]
    return total


def closure_invariant(word, m: int, N: int, q: mp.mpc, Rc, Rci,
                      mu_power: mp.mpf = 1):
    """Quantum-trace closure invariant tr( μ^{⊗m} ρ(word) ), μ = K^{mu_power}.

    The overall framing/normalization is fixed later by calibration (V2);
    this returns the raw quantum trace.
    """
    rho = braid_rep(word, m, N, Rc, Rci)
    # μ = diag(q^{(N-1-2i)·mu_power})
    mu_diag = [q ** (mp.mpf(N - 1 - 2 * i) * mu_power) for i in range(N)]
    dim = N ** m
    total = mp.mpc(0)
    # trace of (μ^{⊗m}) ρ : Σ_x (∏ μ over digits of x) ρ[x,x]
    for x in range(dim):
        # base-N digits of x (m of them)
        weight = mp.mpc(1)
        y = x
        for _ in range(m):
            weight *= mu_diag[y % N]
            y //= N
        total += weight * rho[x, x]
    return total


# ─────────────────────────── validation ───────────────────────────
FIG8_BRAID = [1, -2, 1, -2]      # (σ₁σ₂⁻¹)² in B₃, closure = 4₁


def colored_jones_4_1_exact(N: int, q: mp.mpc) -> mp.mpc:
    """In-repo Habiro–Le form J_N(4₁;q) = Σ_k q^{Nk}(q^{-N-1};q^{-1})_k(q^{-N+1};q)_k."""
    def qpoch(a, base, k):
        p = mp.mpc(1)
        for j in range(k):
            p *= (1 - a * base**j)
        return p
    total = mp.mpc(0)
    for k in range(0, N):
        total += q**(N * k) * qpoch(q**(-N - 1), q**(-1), k) * qpoch(q**(-N + 1), q, k)
    return total


if __name__ == "__main__":
    set_compute_dps()
    q = mp.exp(mp.mpc(0, 1) * mp.mpf("0.37"))     # generic q on unit circle, not a root
    print("U_q(sl₂) colored-Jones machinery — self-checks\n")
    print("  V1  generator relations + braid relation:")
    for N in (2, 3, 4):
        rel = _check_relations(N, q)
        Rc, Rci = r_check_braiding(N, q)
        # braid relation on V^{⊗3}
        I = mp.eye(N)
        b1 = _kron(Rc, I)
        b2 = _kron(I, Rc)
        lhs = b1 * b2 * b1
        rhs = b2 * b1 * b2
        braid_ok = mp.mnorm(lhs - rhs) < mp.mpf("1e-20")
        inv_ok = mp.mnorm(Rc * Rci - mp.eye(N * N)) < mp.mpf("1e-20")
        print(f"    N={N}: sl₂ relations {rel}, Ř·Ř⁻¹=I {bool(inv_ok)}, braid relation {bool(braid_ok)}")

    print("\n  V2  figure-eight normalized closure raw/[N] (balanced q) vs in-repo")
    print("      Habiro–Le J_N(4₁) at q²  [identity: norm(q) = J_HL(q²)]:")
    v2_ok = True
    for N in (2, 3, 4):
        Rc, Rci = r_check_braiding(N, q)
        raw = closure_invariant(FIG8_BRAID, 3, N, q, Rc, Rci, mu_power=1)
        norm = raw / qint(N, q)
        exact = colored_jones_4_1_exact(N, q**2)   # convention q_HL = q_mine²
        err = abs(norm - exact)
        v2_ok = v2_ok and (err < mp.mpf("1e-20"))
        print(f"    N={N}: norm={complex(norm):.8f}  J_HL(q²)={complex(exact):.8f}  err={float(err):.1e}")
    print(f"    V2 {'PASSED — machinery reproduces the known figure-eight colored Jones' if v2_ok else 'FAILED'}")
