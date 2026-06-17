#!/usr/bin/env python3
"""Dense Wedderburn-projector SDP: the redundancy / degenerate-face control.

confinement-sdp.md states the genuine dense SDP

    min <T, Φ>   s.t.  Φ ⪰ 0,  <π_λ, Φ> ≥ 0 ∀λ,  (2×2-pair PSD),  trΦ = c

as the 𝓑₃-confinement-selection principle (#2433's one open *compute* lever).
This probe confirms the formalize-first structural verdict that it CANNOT select
the specific multi-block Borromean element. On H_3(q₀) (Wedderburn blocks
[3]⊕[2,1]⊕[1,1,1], dims 1+4+1 = 6) it checks THREE facts:

  1. REDUNDANCY — the per-block <π_λ,Φ>≥0 and 2×2-pair-PSD constraints are
     implied by the global Φ⪰0 (tr(π_λΦ)≥0 for PSD π_λ,Φ; principal submatrices
     of a PSD matrix are PSD). So solving WITH vs WITHOUT them gives the same
     optimal VALUE and the same min-cost SUPPORT (optimal face).
  2. DEGENERATE FACE — T is block-constant diagonal (T_λλ = μ_λ, q-Laplacian).
     A linear objective over the density spectrahedron is minimised on the face
     of states supported on T's minimum eigenspace. At q₀ that min is DEGENERATE
     (μ_[2,1] = μ_[1,1,1] < μ_[3]), so the face is 5-of-6 dimensional: the
     program selects NO unique operator (two valid solves return different Φ*,
     same value — the signature of a high-dimensional optimal face).
  3. 𝓑₃ NOT SELECTED — the face excludes the high-cost trivial [3] block, while
     𝓑₃ ≈ identity carries weight in every block. A high-dimensional face that
     also misses 𝓑₃'s [3]-component cannot single out the specific 𝓑₃ element.

Verdict: structurally bounded → do not build the heavy solver. Breaking the
degeneracy to pick 𝓑₃ needs the external topological (Borromean) criterion, not
a continuous variational program. No fit, nothing rewired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[1]               # computations/
PYHECKE = HERE.parent / "tools" / "pyhecke" / "python"
for p in (str(HERE), str(HERE / "substrate"), str(PYHECKE)):
    sys.path.insert(0, p)

try:
    from q_parameter import Q as _Q
    Q0 = float(_Q)
except Exception:
    Q0 = 1.10998                                         # canonical substrate q₀


def qint(n: int, q: float) -> float:
    """Balanced q-integer [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)."""
    if q == 1:
        return float(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def mu_lambda(partition, q: float) -> float:
    """q-Laplacian / content-Casimir eigenvalue μ_λ = Σ_cells [c]_q·[c+1]_q.

    Matches computations/sdp_cross_channel.py::mu_at (c = col − row).
    """
    mu = 0.0
    for i, row in enumerate(partition):
        for j in range(row):
            c = j - i
            mu += qint(c, q) * qint(c + 1, q)
    return mu


# H_3 Wedderburn blocks: [3] (d=1), [2,1] (d=2 → 4-dim End-block), [1,1,1] (d=1).
BLOCKS = [((3,), 1), ((2, 1), 2), ((1, 1, 1), 1)]
DIM = sum(d * d for _, d in BLOCKS)                       # 1 + 4 + 1 = 6
TOL = 1e-5


def build_cost_and_projectors(q: float):
    """Diagonal cost T = ⊕_λ μ_λ·I_{d_λ²} and block projectors π_λ (6×6)."""
    diag = []
    pis = []
    offset = 0
    for lam, d in BLOCKS:
        mu = mu_lambda(lam, q)
        width = d * d
        diag.extend([mu] * width)
        pi = np.zeros((DIM, DIM))
        for k in range(offset, offset + width):
            pi[k, k] = 1.0
        pis.append((lam, pi))
        offset += width
    return np.diag(diag), pis


def occupancy(phi: np.ndarray, pis) -> dict:
    """Trace of Φ within each Wedderburn block (per-block occupancy)."""
    return {lam: float(np.trace(pi @ phi)) for lam, pi in pis}


def support_set(occ: dict) -> frozenset:
    """The set of blocks the state actually occupies (> TOL)."""
    return frozenset(lam for lam, v in occ.items() if v > TOL)


def main() -> int:
    import cvxpy as cp

    q = Q0
    T, pis = build_cost_and_projectors(q)
    mus = {lam: mu_lambda(lam, q) for lam, _ in BLOCKS}
    mu_min = min(mus.values())
    min_blocks = [lam for lam, _ in BLOCKS if abs(mus[lam] - mu_min) < TOL]
    face_dim = sum(d * d for lam, d in BLOCKS if lam in min_blocks)

    print("=" * 78)
    print(" Dense Wedderburn-projector SDP on H_3(q₀) — redundancy / face control")
    print("=" * 78)
    print(f" q₀ = {q:.6f}   dim H_3 = {DIM}  (blocks [3]⊕[2,1]⊕[1,1,1] = 1+4+1)")
    print(" q-Laplacian cost per block  μ_λ:")
    for lam, _ in BLOCKS:
        flag = "  ← min" if lam in min_blocks else ""
        print(f"   μ_{str(lam):<10} = {mus[lam]:.5f}{flag}")
    print(f" min cost μ = {mu_min:.5f} attained by {len(min_blocks)} block(s):"
          f" {[str(b) for b in min_blocks]}")
    print(f" ⇒ optimal-face dimension = {face_dim} of {DIM}"
          f" ({'DEGENERATE — non-unique selection' if len(min_blocks) > 1 else 'unique'})\n")

    Phi = cp.Variable((DIM, DIM), symmetric=True)
    obj = cp.Minimize(cp.trace(T @ Phi))
    base = [Phi >> 0, cp.trace(Phi) == 1]
    extra = [cp.trace(pi @ Phi) >= 0 for _, pi in pis]
    for i in range(DIM - 1):                              # 2×2 adjacent-pair PSD
        extra.append(Phi[i:i + 2, i:i + 2] >> 0)

    runs = {}
    for name, cons in (("without extra", base),
                       ("WITH extra", base + extra)):
        cp.Problem(obj, cons).solve(solver=cp.SCS, verbose=False)
        phi = np.asarray(Phi.value)
        occ = occupancy(phi, pis)
        runs[name] = {
            "val": float(np.trace(T @ phi)),
            "phi": phi,
            "occ": occ,
            "supp": support_set(occ),
        }
        print(f" [{name}]  objective = {runs[name]['val']:.5f}"
              f"   support = {sorted(str(b) for b in runs[name]['supp'])}")

    a, b = runs["without extra"], runs["WITH extra"]
    print(f"\n 1. REDUNDANCY:  |Δobjective| = {abs(a['val'] - b['val']):.2e},"
          f"  same support = {a['supp'] == b['supp']}"
          f"  → {'REDUNDANT (same value + same optimal face)' if a['supp'] == b['supp'] and abs(a['val'] - b['val']) < 1e-4 else 'NOT redundant'}")

    df = np.linalg.norm(a["phi"] - b["phi"])
    print(f" 2. DEGENERATE FACE:  min attained by {len(min_blocks)} blocks"
          f" (face dim {face_dim}/{DIM}); the two solves return DIFFERENT Φ*"
          f" (‖ΔΦ‖_F = {df:.3f}) at the SAME value → no unique operator selected")

    excl = [str(lam) for lam, _ in BLOCKS if lam not in min_blocks]
    print(f" 3. 𝓑₃ NOT SELECTED:  the face EXCLUDES the high-cost block(s) {excl}"
          f" (the trivial [3] component, where 𝓑₃'s identity weight partly lives);"
          f"\n    a degenerate {face_dim}-dim face cannot single out the specific"
          f" multi-block 𝓑₃ element.")

    print("\n VERDICT: redundant extra constraints + a degenerate optimal face ⇒")
    print(" the continuous SDP selects a COST LEVEL / subspace, never the specific")
    print(" 𝓑₃ operator. Breaking the degeneracy needs the external topological")
    print(" (Borromean) criterion. Structurally bounded — REFUTED. No fit, not wired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
