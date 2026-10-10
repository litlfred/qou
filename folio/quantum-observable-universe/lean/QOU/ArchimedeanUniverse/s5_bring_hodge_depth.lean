import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
# S₅-Hodge depth of Bring's curve — representation-theory core

Formalizes the character-theoretic assertions computed by
`computations/substrate/s5_bring_hodge_depth.py` (keystone / strand-b1).

**Cited geometric input (NOT proved here).** Riera–Rodríguez 1992,
*The period matrix of Bring's curve*: the space of holomorphic
differentials `H⁰(Ω)` of Bring's genus-4 curve is the irreducible
4-dimensional `S₅` standard representation `W` (the partition `(4,1)`,
or equivalently its sign-twist `(2,1,1,1)`). The numerical period matrix
`τ` itself lives in that reference; it is **not** reconstructed here.

**What this file proves (unconditional finite ℚ arithmetic).** The
`S₅` class-function inner products over the 7 conjugacy classes:

* `W` is irreducible: `⟨χ_(4,1), χ_(4,1)⟩ = 1`;
* the sign-twist `(2,1,1,1)` is also irreducible and **distinct** from
  `(4,1)`: `⟨χ_(2,1,1,1), χ_(2,1,1,1)⟩ = 1`, `⟨χ_(4,1), χ_(2,1,1,1)⟩ = 0`;
* `W` occurs in `H¹ = H^{1,0} ⊕ H^{0,1} = W ⊕ conj W = 2·W` with
  **multiplicity 2**: `⟨χ_{H¹}, χ_(4,1)⟩ = 2`.

**Consequence (interpretation, modulo the cited input).** Because the
Gauss–Manin operator `M` on the prolonged periods is `S₅`-equivariant,
Schur's lemma forces `M = id_W ⊗ B` with `B` a `2×2` matrix on the
multiplicity space, so the period recurrence has **depth ≤ 2**.

**Explicitly NOT proved.** *Depth = 2* (not merely `≤ 2`) needs Griffiths
transversality (`∇F^p ⊂ F^{p-1} ⊗ Ω` ⇒ `B` non-scalar) — a further
geometric input, stated in the workplan, not formalized. And the
identification `H⁰(Ω) ≅ W` is the Riera–Rodríguez input above, not a
theorem of this file.
-/

set_option autoImplicit false

namespace QOU.ArchimedeanUniverse.S5BringHodgeDepth

/-- Conjugacy-class sizes of `S₅` on its 7 classes
`e, (12), (12)(34), (123), (123)(45), (1234), (12345)` (sum `= 120 = |S₅|`). -/
def classSizes : List ℚ := [1, 10, 15, 20, 20, 30, 24]

/-- The sign character of `S₅` on the 7 classes (parity of a representative). -/
def sgn : List ℚ := [1, -1, 1, 1, -1, -1, 1]

/-- Character of the standard representation `W = (4,1)`:
`χ(g) = (# fixed points of g) − 1`. -/
def chiW41 : List ℚ := [4, 2, 0, 1, -1, 0, -1]

/-- Character of the sign-twist `(2,1,1,1) = (4,1) ⊗ sgn`
(`= [4, -2, 0, 1, 1, 0, -1]`, i.e. `chiW41` times `sgn` entrywise). -/
def chiW2111 : List ℚ := [4, -2, 0, 1, 1, 0, -1]

/-- Character of `H¹ = W ⊕ conj W = 2·W` (`W` is real, so `conj W ≅ W`). -/
def chiH1 : List ℚ := [8, 4, 0, 2, -2, 0, -2]

/-- The `S₅` class-function inner product
`⟨a, b⟩ = (1/|S₅|) Σ_classes |C|·a(C)·b(C)` (real characters). -/
def inner (a b : List ℚ) : ℚ :=
  (classSizes.zipWith (· * ·) (a.zipWith (· * ·) b)).sum / 120

/-- `sgn` twists `chiW41` into `chiW2111` entrywise (bookkeeping check). -/
theorem chiW2111_eq_twist : chiW41.zipWith (· * ·) sgn = chiW2111 := by
  norm_num [chiW41, sgn, chiW2111, List.zipWith]

/-- `chiH1` is `2 · chiW41` entrywise (`H¹ = 2·W`). -/
theorem chiH1_eq_two_chiW41 : chiW41.zipWith (· + ·) chiW41 = chiH1 := by
  norm_num [chiW41, chiH1, List.zipWith]

/-- **The standard rep `W = (4,1)` is irreducible:** `⟨χ_W, χ_W⟩ = 1`. -/
theorem W41_irreducible : inner chiW41 chiW41 = 1 := by norm_num [inner, classSizes, sgn, chiW41, chiW2111, chiH1, List.zipWith, List.sum]

/-- **The sign-twist `(2,1,1,1)` is irreducible:** `⟨χ, χ⟩ = 1`. -/
theorem W2111_irreducible : inner chiW2111 chiW2111 = 1 := by norm_num [inner, classSizes, sgn, chiW41, chiW2111, chiH1, List.zipWith, List.sum]

/-- **`(4,1)` and `(2,1,1,1)` are distinct irreducibles:** `⟨χ_(4,1), χ_(2,1,1,1)⟩ = 0`. -/
theorem W41_W2111_distinct : inner chiW41 chiW2111 = 0 := by norm_num [inner, classSizes, sgn, chiW41, chiW2111, chiH1, List.zipWith, List.sum]

/-- **`W` occurs in `H¹ = 2·W` with multiplicity 2:** `⟨χ_{H¹}, χ_W⟩ = 2`.
This is the Schur bound `depth ≤ 2` on the `S₅`-equivariant Gauss–Manin
recurrence (modulo the cited Riera–Rodríguez identification `H⁰(Ω) ≅ W`). -/
theorem multiplicity_W_in_H1 : inner chiH1 chiW41 = 2 := by norm_num [inner, classSizes, sgn, chiW41, chiW2111, chiH1, List.zipWith, List.sum]

end QOU.ArchimedeanUniverse.S5BringHodgeDepth
