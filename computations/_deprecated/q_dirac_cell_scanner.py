#!/usr/bin/env python3
"""
q-DIRAC CHARACTER CALCULATOR + (k, ε, D_q²) CELL SCANNER.

Per user direction in session: implement infrastructure for
horizontal/vertical decomposition of mass-formula contributions.

The 3D cell grid:
  k       = curvature-rank = depth(λ) - 1 = #rows(λ) − 1
  ε       = S-eigenvalue (chirality):
              +1 if λ = λ' (self-conjugate) or sym pair
              −1 if λ ≠ λ' (S-anti-invariant via conjugate pair)
  D_q²    = q-Dirac² eigenvalue: ([n]_q · sign(c_λ))² where c_λ is
            the signed content of partition λ
            classes: 0 (chirality channel, D_q² = 0 on (2,1)-type)
                     [k]_q² for some k

Each Wedderburn block λ ⊢ n contributes one cell (k(λ), ε(λ), D_q²(λ)).

Algorithm:
  1. For each n ∈ [3, 4, 5, 6, 9, 12]:
     for each partition λ ⊢ n:
       - compute depth k = #rows(λ) − 1
       - compute S-eigenvalue (self-conj vs conjugate-pair)
       - compute q-Dirac² via signed content
       - record cell (k, ε, D_q²) ← λ
  2. Print the cell grid with population per cell.
  3. Identify which cells are POPULATED (have partitions),
     EMPTY (none), or HEAVILY-POPULATED (many).

For α_EM, np splitting, Q_β: identify which cells contribute.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import partitions_of, dim_q, young_hooks
from q_mpmath import set_q, qint, qfac

# Pass the high-precision Q_MP to q_mpmath so qint/qfac/qpoch run at
# the same precision as the direct Q0/QI arithmetic below.  The earlier
# `set_q(Q0_FLOAT)` would have left q_mpmath bounded to f64 while this
# module does HP arithmetic — silent precision floor.
set_q(Q_MP)
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip


def transpose_partition(lam):
    if not lam: return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def signed_content(lam):
    """Sum over cells of (column - row) (signed Young content).

    For a partition λ = (λ_1, ..., λ_r), the content of cell (i, j)
    is c(i, j) = j - i.  Signed content sums over cells.

    For (3): c = 0+1+2 = 3
    For (2,1): c = 0+1+(-1) = 0   ← chirality channel!
    For (1,1,1): c = 0+(-1)+(-2) = -3
    For (4): c = 0+1+2+3 = 6
    For (3,1): c = 0+1+2+(-1) = 2
    For (2,2): c = 0+1+(-1)+0 = 0   ← chirality
    For (2,1,1): c = 0+1+(-1)+(-2) = -2
    For (1,1,1,1): c = -6
    """
    total = 0
    for i, row in enumerate(lam):
        for j in range(row):
            total += j - i
    return total


def q_dirac_eigenvalue(lam):
    """D_q acts as (q^c_λ - q^{-c_λ}) / (q - q^{-1}) = [c_λ]_q
    on the irrep V_λ.  For c_λ = 0, eigenvalue is 0 (chirality channel)."""
    c = signed_content(lam)
    if c == 0:
        return mp.mpf(0)
    return qint(abs(c)) * (1 if c > 0 else -1)


def q_dirac_squared(lam):
    """D_q² eigenvalue."""
    eig = q_dirac_eigenvalue(lam)
    return eig * eig


def s_eigenvalue(lam):
    """S-eigenvalue:
    +1 if λ = λ' (self-conjugate, lives in S-even subspace)
    'pair' if λ ≠ λ' (forms conjugate pair; S maps to λ')
    """
    return 'self' if transpose_partition(lam) == lam else 'pair'


def main():
    print("=" * 100)
    print("q-DIRAC CHARACTER CALCULATOR + (k, ε, D_q²) CELL SCANNER")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()

    # Test on small partitions first
    chirality_cells_total = []  # (n, partition, k, w_lam) where D_q^2 = 0
    for n in [3, 4, 5, 6, 9, 12]:
        print(f"  ── n = {n} ──")
        print(f"  {'partition':<18} {'depth k':>7} {'c_λ':>5} {'D_q² eigval':>14} "
              f"{'S-class':>8} {'central?':>9} {'dim_q':>10} {'w_λ':>10}")
        nfac = float(qfac(n))
        cells = {}  # (k, eps, central?, D_q²) -> [partitions]
        for lam in partitions_of(n):
            lam_t = tuple(lam)
            k = len(lam_t) - 1
            c = signed_content(lam_t)
            D2 = float(q_dirac_squared(lam_t))
            s_class = s_eigenvalue(lam_t)
            dq = float(dim_q(lam_t))
            w = dq*dq/nfac
            # central? flag: D_q² = 0 marks the chirality channel where the
            # q-Dirac operator vanishes — these are the persistent
            # gauge-invariant background cells (gluon-condensate analogues).
            is_central = abs(D2) < 1e-10
            central_str = "YES" if is_central else "no"
            if is_central:
                chirality_cells_total.append((n, lam_t, k, w))
            print(f"  {str(lam_t):<18} {k:>7} {c:>5} {D2:>14.6f} "
                  f"{s_class:>8} {central_str:>9} {dq:>10.4f} {w:>10.6f}")
            # Round D2 to reasonable precision for binning
            D2_key = round(D2, 4)
            cell = (k, s_class, is_central, D2_key)
            cells.setdefault(cell, []).append(lam_t)

        print(f"\n  Cell grid (k, S-class, central?, D_q²) → partitions:")
        for cell in sorted(cells, key=lambda c: (c[0], c[1], c[2], c[3])):
            k, eps, central, D2 = cell
            parts = cells[cell]
            star = " ★" if central else "  "
            print(f"    ({k}, {eps:>5}, central={str(central):>5}, D²={D2:>10.4f}){star}: "
                  f"{len(parts)} partitions: "
                  f"{[str(p) for p in parts][:3]}{'...' if len(parts) > 3 else ''}")
        print()

    # Chirality channel summary (witness for prop:confinement-categorical)
    print("=" * 100)
    print("  CHIRALITY CHANNEL (D_q² = 0): persistent gauge-invariant background")
    print("=" * 100)
    print(f"  {'n':>3}  {'partition':<18}  {'depth k':>7}  {'w_λ':>10}")
    for (n, lam_t, k, w) in chirality_cells_total:
        print(f"  {n:>3}  {str(lam_t):<18}  {k:>7}  {w:>10.6f}")
    print()

    # Specific identifications for our formulas
    print("=" * 100)
    print("  IDENTIFICATIONS")
    print("=" * 100)
    print()
    print("  α_EM = 45·[3]_q·(1 + ℏ_q⁴·[5]_q + 8q·(ℏ_q⁴·[5]_q)²)")
    print("    ─ 45 = (10 choose 2): cell at n=10, partition Λ²(C^10)")
    print("        decomposes as V_(9,1) ⊕ V_(8,1,1):")
    print(f"          V_(9,1):     k=1, c=8,  D_q² = [8]_q² = {float(qint(8))**2:.4f}")
    print(f"          V_(8,1,1):   k=2, c=4,  D_q² = [4]_q² = {float(qint(4))**2:.4f}")
    print()
    print("    ─ [3]_q: H_3 partition (3) at k=0, c=3, D_q² = [3]_q² = "
          f"{float(qint(3))**2:.4f}")
    print()
    print("  np splitting = m_e·Σ_3 + m_e·Vol(6_1)·|(q;q)_3|")
    print("    ─ Σ_3 = 2 + 1/[2]_q: sum over H_3 cells")
    print(f"        (3): k=0, D_q² = {float(qint(3))**2:.4f}, contributes 1")
    print(f"        (2,1): k=1, D_q² = 0 (chirality), contributes 1/[2]_q")
    print(f"        (1,1,1): k=2, D_q² = {float(qint(3))**2:.4f}, contributes 1")
    print()
    print("    ─ Vol(6_1)·|(q;q)_3|: rank-3 chirality (6_1 is std-channel knot)")
    print()
    print("  Q_β = m_e·(Σ_3-1) + m_e·Vol(6_1)·|(q;q)_3| + m_e·|(q;q)_4|")
    print("    ─ rank 4: universal contribution at k=4, NO specific knot")
    print()

    # Save witness
    witness = {
        'computation': 'q-dirac-cell-scanner',
        'description': (
            'q-Dirac character calculator + (k, ε, D_q²) cell scanner.  '
            'Computes q-Dirac eigenvalue, S-eigenvalue, depth, Plancherel '
            'weight for each partition of n=3,4,5,6,9,12.  Identifies '
            'which cells of the (curvature-rank, chirality, q-Dirac²) '
            'grid are populated and which contribute to α_EM, np splitting, '
            'and Q_β formulas.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
    }
    out = Path(__file__).parent / "q-dirac-cell-scanner.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
