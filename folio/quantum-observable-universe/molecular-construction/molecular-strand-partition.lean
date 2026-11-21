import Mathlib.Data.List.Basic
import Mathlib.Data.Nat.Basic

/-!
# QOU.Molecular.StrandPartition — molecular strand-partition

The per-sub-unit strand counts $(n_1,\dots,n_k)$ of a composite braid
assembled from $k$ sub-units, summing to the total strand count $N$.
This is the combinatorial datum (an ordered composition of $N$) that
indexes the parabolic Young subgroup $S_\lambda \subset S_N$ and its
Hecke subalgebra $H_\lambda(q) \hookrightarrow H_N(q)$.

## References
- [leitner2026] Ch. 12, Definition: Molecular strand-partition
- [kassel1995] Kassel, "Quantum Groups," GTM 155
-/

namespace QOU.Molecular

/-- A molecular strand-partition: the strand count of each sub-unit. -/
-- Ref: [leitner2026] Ch. 12, Definition: Molecular strand-partition
structure StrandPartition where
  /-- Strand count of each sub-unit. -/
  parts : List ℕ
  /-- Every sub-unit carries at least one strand. -/
  parts_pos : ∀ n ∈ parts, 0 < n

namespace StrandPartition

/-- Total strand count `N = Σ nᵢ`. -/
def total (P : StrandPartition) : ℕ := P.parts.sum

/-- Number of sub-units `k = ℓ(λ)`. -/
def numUnits (P : StrandPartition) : ℕ := P.parts.length

/-- The benzene carbon strand-partition `(2,2,2)`: three acetylene units. -/
def benzene : StrandPartition := ⟨[2, 2, 2], by decide⟩

/-- Benzene has total carbon strand count `6`. -/
theorem benzene_total : benzene.total = 6 := by decide

/-- Benzene is assembled from three sub-units. -/
theorem benzene_numUnits : benzene.numUnits = 3 := by decide

end StrandPartition
end QOU.Molecular
