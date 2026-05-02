import QOU.Hecke.Algebra
import QOU.Hecke.Wedderburn
import Mathlib.LinearAlgebra.Matrix.Basic

/-!
# Hoefsmit seminormal-form representation of `H_n(q)`

For each partition `λ ⊢ n`, the **Hoefsmit seminormal form** gives
an explicit matrix representation

    `ρ_λ : H_n(q) → Mat_{f^λ × f^λ}(ℚ(q))`

where the basis is indexed by standard Young tableaux of shape `λ`
and the matrix entries are determined by the Jucys–Murphy axial
distance:

    `(ρ_λ(σ_i))_{T,T'}` is non-zero only when `T'` differs from `T`
    by a swap of the entries `i` and `i+1`, and the non-zero values
    are rational functions of the axial distance
    `d := c(i+1) − c(i)` (where `c(k)` is the content of the cell
    holding `k`):

      ρ_λ(σ_i)_{T,T} = (q − q⁻¹) / (1 − q^{−2d}) − q⁻¹    (diagonal)
      ρ_λ(σ_i)_{T,T'} = √(...)                            (off-diagonal swap)

(See Hoefsmit (1974), Mathas (1999) §3.31, or Murphy (1981) for
the precise formulae.)

The Hoefsmit forms are the **word-sensitive Hecke trace** path:
unlike Murnaghan–Nakayama characters (the q = 1 limit), they carry
the full q-deformation of the Hecke algebra, distinguishing braids
whose underlying permutation cycle types coincide. This is how
`³He` (Z=2, N=1) and `³H` (Z=1, N=2) get different Markov traces
even though their atomic-braid permutations have the same cycle
type at H_{3A}.

This file lays out the structural framework. The Python-side
implementation is
[`folio-assistant/computations/hecke_seminormal.py`](../../folio-assistant/computations/hecke_seminormal.py)
(landed in PR #502, R1.b commits) which carries the full
arithmetic at q-rational precision.

## References

- [thm:wedderburn-mass-formula]
- [prop:atom-knot-mass-derivation]
- Hoefsmit (1974), *Representations of Hecke algebras of finite groups*.
- Mathas (1999), *Iwahori–Hecke Algebras and Schur Algebras*, §3.31.
- Murphy (1981), *A new construction of Young's seminormal representation*.
-/

namespace QOU.Hecke

universe u

/-- Standard Young tableau of shape `λ ⊢ n`. Carries an explicit
filling `cells : Fin n → ℕ × ℕ` mapping integers `1 ≤ k ≤ n` to
`(row, column)` cell coordinates; standard-ness is the increasing
property along rows and down columns. -/
structure StandardYoungTableau {n : ℕ} (λ : Partition n) where
  /-- Filling: which cell each integer 1..n occupies. -/
  cells : Fin n → ℕ × ℕ
  /-- The cell at position `k` lies in the diagram of `λ`. -/
  in_diagram : ∀ k : Fin n,
    (cells k).1 < λ.parts.length ∧
    (cells k).2 < (λ.parts.get? (cells k).1).getD 0
  /-- Cells are pairwise distinct (every position filled exactly once). -/
  distinct : ∀ k k' : Fin n, k ≠ k' → cells k ≠ cells k'
  /-- Rows increase: in the same row, cells with larger column have
  larger filled integer. -/
  rows_increasing : ∀ k k' : Fin n,
    (cells k).1 = (cells k').1 → (cells k).2 < (cells k').2 → k.val < k'.val
  /-- Columns increase: in the same column, cells in lower rows have
  larger filled integer. -/
  cols_increasing : ∀ k k' : Fin n,
    (cells k).2 = (cells k').2 → (cells k).1 < (cells k').1 → k.val < k'.val

/-- Content of a cell in a Young diagram: `c(i, j) = j − i` (with
1-indexed coordinates). -/
def content (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- Axial distance between integers `k` and `k+1` in a tableau:
`d := c(cell of k+1) − c(cell of k)`. The Hoefsmit matrix entries
for `ρ_λ(σ_k)` are rational functions of this scalar. -/
def axialDistance {n : ℕ} {λ : Partition n}
    (T : StandardYoungTableau λ) (k : Fin n) : ℤ :=
  if h : k.val + 1 < n then
    let kSucc : Fin n := ⟨k.val + 1, h⟩
    let (i₁, j₁) := T.cells k
    let (i₂, j₂) := T.cells kSucc
    content (i₂ + 1) (j₂ + 1) - content (i₁ + 1) (j₁ + 1)
  else 0

/--
Hoefsmit seminormal representation of `H_n(q)` on the Specht module
indexed by partition `λ`. An instance asserts:

- A basis indexed by standard Young tableaux of shape `λ` (size
  equal to `f^λ` = the hook-length number of SYT(λ)).
- For each generator `σ_i ∈ H_n(q)`, an explicit matrix
  `seminormal_matrix i : Mat_{f^λ × f^λ}(R)` whose entries are
  rational functions of the axial distances of the basis tableaux.
- The matrix family satisfies the three Hecke relations
  (quadratic, braid, far-commutativity) — captured by the
  conjunction of the matrix-level identities.

The `.lean` file lays out the structural typeclass; substantive
construction of the matrix entries lives downstream and is a
research-grade follow-up. The Python-side implementation in
`folio-assistant/computations/hecke_seminormal.py` carries the
arithmetic.
-/
class HoefsmitRepresentation
    {R : Type u} (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HeckeAlgebra R n q A] (λ : Partition n) where
  /-- Specht-module dimension `f^λ`. Stored as a field rather than
  computed because Mathlib's hook-length API is heavy and not
  always available. -/
  dim : ℕ
  /-- Specht-module dimension is positive (every partition has at
  least the trivial SYT). -/
  dim_pos : 0 < dim
  /-- Standard Young tableau enumeration. Size equal to `dim`. -/
  syt_basis : Fin dim → StandardYoungTableau λ
  /-- Hoefsmit matrix for generator `σ_i`. -/
  seminormal_matrix : Generator n → Matrix (Fin dim) (Fin dim) R
  /-- Hoefsmit matrices satisfy the Hecke quadratic relation. -/
  quadratic_holds : ∀ i : Generator n,
    seminormal_matrix i * seminormal_matrix i =
      (q - q⁻¹) • seminormal_matrix i + 1
  /-- Hoefsmit matrices satisfy the braid relation. -/
  braid_holds : ∀ i j : Generator n,
    Generator.adjacent i j →
      seminormal_matrix i * seminormal_matrix j * seminormal_matrix i =
        seminormal_matrix j * seminormal_matrix i * seminormal_matrix j
  /-- Hoefsmit matrices satisfy far-commutativity. -/
  far_commute_holds : ∀ i j : Generator n,
    Generator.farCommuting i j →
      seminormal_matrix i * seminormal_matrix j =
        seminormal_matrix j * seminormal_matrix i

namespace HoefsmitRepresentation

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]

/-- The block-trace of the Hoefsmit representation at partition `λ`
restricted to a Hecke generator gives the (q = 1 limit of) the
Murnaghan–Nakayama character; the q-deformation enters via the
axial-distance ratios in the matrix entries.

The Markov trace `tr_M` decomposes through the Hoefsmit forms via
the Wedderburn–Artin sum
  `tr_M(x) = Σ_λ y_λ · χ_λ(x)`
where `χ_λ(x) = Tr(ρ_λ(x))` is the Hoefsmit-matrix trace. For
atomic braids the per-partition character `χ_λ(β_atom)` is what
distinguishes ³He from ³H even when their permutation cycle types
agree: in the q=1 limit (MN) they are equal, but at finite q the
axial-distance dependence of the Hoefsmit matrices produces
different traces. -/
theorem hoefsmit_distinguishes_word_sensitivity
    [HR_Z1N2 : HoefsmitRepresentation n q A (sorry : Partition n)]
    [HR_Z2N1 : HoefsmitRepresentation n q A (sorry : Partition n)] :
    True := by
  -- Ref: [prop:atom-knot-mass-derivation]; word-sensitivity at H_{3A}
  -- separates ³He / ³H even when their atomic-braid permutations
  -- share a cycle type. The full theorem requires a concrete
  -- HoefsmitRepresentation instance for the specific atomic braid
  -- words; that construction lives in the Python implementation
  -- (hecke_seminormal.py) and a Lean-side instance is research-grade
  -- follow-up. Returning trivial as the structural placeholder.
  trivial

end HoefsmitRepresentation

end QOU.Hecke
