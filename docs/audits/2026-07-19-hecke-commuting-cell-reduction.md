# Far commutation at general rank, reduced to the ℤ₂×ℤ₂ cell (2026-07-19)

**Bean:** `qou-farc`. **Lean:** [`QOU/Machinery/HeckeCommutingCellReduction.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeCommutingCellReduction.lean)
— sorry-free, `lean`-direct exit 0, first try (the reduction pattern from the
merged `HeckeDihedralBraidReduction`, applied to the m = 2 pair).

## What landed

- `descentC2σi/σj` — the two descent structures on the 4-element commuting
  cell `[e, sᵢ, sⱼ, sᵢsⱼ]` (lengths `[0,1,1,2]`, `decide`-checked);
- **`cell_far_commute`** — far commutation on the cell (finite check);
- **`CommutingCosetStructure`** — the parabolic factorization datum
  `W ≃ C × Fin 4` with length additivity and cell-wise actions;
- **`far_commute_of_commuting`** — `σᵢσⱼ = σⱼσᵢ` on ANY module carrying
  the datum (fibre localization + cell check);
- `commutingSelf` — the rank-2 self-instance.

## The presentation-law ledger is now complete at the algebra layer

| law | status |
|---|---|
| Hecke quadratic | **proved outright at every rank** (`mulStep_quadratic`, merged #4056) |
| braid (m=3) | **reduced** to the S₃ coset datum (`braid_of_dihedral`, merged #4059) |
| far commutation (m=2) | **reduced** to the ℤ₂×ℤ₂ coset datum (this) |

For all three `HeckeBraidedPresentation` field kinds, the remaining open
content is a single combinatorial statement per pair: the Bourbaki
parabolic coset decomposition of the Coxeter system. No algebraic gap
remains.

Honesty: conditional on the coset data; no general-n class instance
declared; nothing wired; `1/(8π)` stays phase-4. §7c generic `[CommRing R]`.
