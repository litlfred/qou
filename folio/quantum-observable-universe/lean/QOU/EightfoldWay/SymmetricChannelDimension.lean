import Mathlib.Tactic
import Mathlib.Data.Sym.Card
import Mathlib.Data.Finsupp.Weight
import Mathlib.Data.Finsupp.Multiset
import Mathlib.RingTheory.MvPolynomial.Basic
import Mathlib.RingTheory.MvPolynomial.Homogeneous
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# The symmetric channel has dimension `C(N + n - 1, n)` — the decuplet at `N = n = 3`

`prop:borromean-decuplet` states that the fully symmetric channel of `V^{⊗3}` at `dim V = 3`
is `10`-dimensional, via `binom(N+n-1, n) = binom(5,3) = 10`, and that this is *conditional on
`N = 3`*: at `N = 2` the same partition yields only a `4`-dimensional quadruplet.

## What is actually being formalised (and what is not)

The temptation is to "formalise" the proposition as `Nat.choose 5 3 = 10`. That is arithmetic
wearing a theorem's clothes — it is a closed numeral computation that says nothing about any
vector space, and it would satisfy a coverage checker while proving nothing. Per the strict Lean
discipline, it is not a theorem.

The genuine content is the **dimension formula itself**, for general `N` and `n`:

    dim_K { degree-n forms in N variables }  =  C(N + n - 1, n)

The space of degree-`n` homogeneous forms in `N` variables *is* the `n`-th symmetric power of the
dual of an `N`-dimensional space, so this is the symmetric channel's dimension, not a stand-in for
it. The proof goes through the object the manuscript's table actually displays — the **weight
diagram**, i.e. the exponent vectors `(n_u, n_d, n_s)` of total degree `n`:

* `wdEquivSym` — the weight diagram is in bijection with **multisets of `n` flavours**. This is
  the "Content" column of the table (`uuu`, `uud`, …, `sss`) made precise: a decuplet state *is*
  a multiset of three quark flavours.
* `card_weightDiagram` — that set has `C(N + n - 1, n)` elements (stars and bars).
* `homogeneousSubmodule_eq_restrictSupport` — the degree-`n` forms are exactly the polynomials
  supported on the weight diagram, so the diagram indexes a **basis**.
* `finrank_homogeneousSubmodule` — the dimension formula, over any commutative semiring
  satisfying the strong rank condition (in particular over any field).

The numerals come last and are *derived*:

* `decuplet_dim` — `N = 3, n = 3` gives `10`;
* `quadruplet_dim` — `N = 2, n = 3` gives `4`;
* `decuplet_ne_quadruplet` — the two differ.

That last one is the point of the exercise. The block's anti-fitting guard is the claim that the
decuplet is *conditional on `N = 3`* and would be a quadruplet at `N = 2`. Deriving both numbers
from one general theorem makes that conditional machine-checked rather than asserted, and it is
what makes the statement falsifiable: were the dimension `N`-independent, `decuplet_ne_quadruplet`
would fail.

## Honest scope

Three things are **not** formalised here, and none of them should be read into the above.

1. **The symmetrizer.** The manuscript realises the symmetric channel as the image of the Hecke
   symmetrizer `e_(3) = Σ_{σ ∈ S₃} T_σ` acting on `V^{⊗3}`. Identifying that image with the
   symmetric power requires `n!` to be invertible — `e_(3)` composed with itself is `n! · e_(3)`,
   hence over a field of characteristic `2` or `3` it is not a projector at all, and the
   identification fails. What is proved here is the dimension of the symmetric power; the
   char-`0` (or char `> n`) hypothesis that ties it to the symmetrizer image is **not** discharged.
2. **The `SU(3)`-structure.** That the `10` basis vectors carry the weights listed in the table,
   and that the space is the irreducible `(3,0)` representation rather than merely a complement
   of the correct dimension, needs representation theory Mathlib does not carry usably. Only
   the *indexing* by quark-count coordinates is proved (`wdEquivSym`).
3. **The physical identification.** That the spin-`3/2` baryon decuplet is *this* channel is a
   spin–flavour–colour selection-rule argument the chapter does not derive; it is already
   recorded as an open item in `sec:eightfold-open-problems`, and nothing here closes it.

-- Ref: [leitner2026] folio/quantum-observable-universe/eightfold-way/borromean-decuplet-derivation.md
-/

namespace QOU.EightfoldWay.SymmetricChannelDimension

open Finset Fintype MvPolynomial

-- No division is ever performed below, so the base ring is deliberately NOT a field: a
-- commutative semiring satisfying the strong rank condition (every field, and every nontrivial
-- commutative ring, is one) carries the whole argument. Cf. the sibling meson-octet module,
-- where the field IS essential — it divides the trace by `n`.
variable {N n : ℕ} {K : Type*} [CommSemiring K] [StrongRankCondition K]

/-- **The weight diagram**: exponent vectors of total degree `n` in `N` flavours.

At `N = n = 3` these are the quark-count coordinates `(n_u, n_d, n_s)` with
`n_u + n_d + n_s = 3` — the triangle whose corners are `Δ⁺⁺ (uuu)`, `Δ⁻ (ddd)` and `Ω⁻ (sss)`. -/
def weightDiagram (N n : ℕ) : Set (Fin N →₀ ℕ) := { d | d.degree = n }

/-- **A weight-diagram point is a multiset of `n` flavours.**

This is the manuscript table's "Content" column as a theorem: the state `uds` *is* the multiset
`{u, d, s}`, and the exponent vector `(1,1,1)` is the same datum written additively. The
bijection is `Finsupp.toMultiset`, and it is what lets stars and bars count the diagram. -/
def wdEquivSym (N n : ℕ) : ↥(weightDiagram N n) ≃ Sym (Fin N) n :=
  Equiv.subtypeEquiv (Finsupp.orderIsoMultiset).toEquiv (by
    intro d
    show d.degree = n ↔ Multiset.card (Finsupp.toMultiset d) = n
    rw [Finsupp.card_toMultiset]
    exact Iff.rfl)

noncomputable instance : Fintype ↥(weightDiagram N n) := Fintype.ofEquiv _ (wdEquivSym N n).symm

/-- **Stars and bars.**  The weight diagram has `C(N + n - 1, n)` points. -/
theorem card_weightDiagram : Fintype.card ↥(weightDiagram N n) = (N + n - 1).choose n := by
  rw [Fintype.card_congr (wdEquivSym N n), Sym.card_sym_eq_choose, Fintype.card_fin]

/-- `Finsupp.degree` is `Finsupp.weight 1`, in the form the homogeneity predicate uses. -/
theorem degree_eq_weight_one' (d : Fin N →₀ ℕ) :
    d.degree = Finsupp.weight (1 : Fin N → ℕ) d :=
  congrFun (Finsupp.degree_eq_weight_one (σ := Fin N) (R := ℕ)) d

omit [StrongRankCondition K] in
/-- **The degree-`n` forms are exactly the polynomials supported on the weight diagram.**

This is the step that turns a counting statement about the diagram into a statement about a
vector space: `restrictSupport` carries a canonical basis indexed by the diagram. -/
theorem homogeneousSubmodule_eq_restrictSupport :
    homogeneousSubmodule (Fin N) K n = restrictSupport K (weightDiagram N n) := by
  ext p
  rw [mem_homogeneousSubmodule, restrictSupport, Finsupp.mem_supported]
  constructor
  · intro h d hd
    show d.degree = n
    rw [degree_eq_weight_one']
    exact h (MvPolynomial.mem_support_iff.mp hd)
  · intro h d hd
    rw [← degree_eq_weight_one']
    exact h (MvPolynomial.mem_support_iff.mpr hd)

/-- **The dimension formula.**  The space of degree-`n` homogeneous forms in `N` variables — the
`n`-th symmetric power of the dual of an `N`-dimensional space — has dimension `C(N + n - 1, n)`.

General in `N`, `n` and the base ring — no division is used anywhere, so no field is needed.
This is the proposition's mathematical core; everything below is instantiation. -/
theorem finrank_homogeneousSubmodule :
    Module.finrank K (homogeneousSubmodule (Fin N) K n) = (N + n - 1).choose n := by
  rw [homogeneousSubmodule_eq_restrictSupport,
    Module.finrank_eq_card_basis (basisRestrictSupport K (weightDiagram N n))]
  exact card_weightDiagram

/-! ### The numerals, as consequences -/

/-- **The decuplet.**  `N = 3` flavours, `n = 3` quarks: dimension `C(5,3) = 10`. -/
theorem decuplet_dim : Module.finrank K (homogeneousSubmodule (Fin 3) K 3) = 10 := by
  rw [finrank_homogeneousSubmodule]
  rfl

/-- **The quadruplet.**  The same partition at `N = 2` gives only `C(4,3) = 4`. -/
theorem quadruplet_dim : Module.finrank K (homogeneousSubmodule (Fin 2) K 3) = 4 := by
  rw [finrank_homogeneousSubmodule]
  rfl

/-- **The anti-fitting guard, machine-checked.**  The decuplet claim is conditional on `N = 3`:
the symmetric channel at `N = 2` is a *different size*. Were the dimension `N`-independent this
would fail, which is what makes the conditional a real hypothesis rather than a hedge. -/
theorem decuplet_ne_quadruplet :
    Module.finrank K (homogeneousSubmodule (Fin 3) K 3)
      ≠ Module.finrank K (homogeneousSubmodule (Fin 2) K 3) := by
  rw [decuplet_dim, quadruplet_dim]
  decide


/-! ### The `N = 2` quartet is the isospin-3/2 ladder

`quadruplet_dim` says the symmetric channel at `N = 2` is *four-dimensional*. That is a
count, and a count does not say the four states are the `Δ(1232)` isospin quartet. This
section supplies the label: the third isospin component, and the four facts that make it
a faithful one.

With index `0 = u` and `1 = d` (the convention `weightDiagram`'s own docstring fixes),
`u` carries `I₃ = +1/2` and `d` carries `I₃ = -1/2`, so a degree-3 monomial carries
`I₃ = (n_u - n_d)/2`. Everything below is stated on the doubled value `2I₃ = n_u - n_d`,
to stay in `ℤ` and keep the statements free of division.

Nothing here is archimedean and nothing needs the base ring, so these are `ℕ`/`ℤ`
statements (§7c).

**The contrast with `N = 3` is deliberate and is NOT proved here.** At three flavours
`I₃` alone is not a faithful label — strangeness is a second independent coordinate, and
`Σ*⁰` and `Λ`-like states share an `I₃`. That is the decuplet's business and is gated on
`N = 3` existing at all. -/

/-- A weight-diagram point at two flavours has quark counts summing to the degree. -/
theorem coordSum_of_mem {w : Fin 2 →₀ ℕ} (hw : w ∈ weightDiagram 2 n) :
    w 0 + w 1 = n := by
  have h : w.degree = n := hw
  rwa [Finsupp.degree_eq_sum, Fin.sum_univ_two] at h

/-- **Twice the third isospin component**, `2I₃ = n_u - n_d`. Doubled so that the
half-integer weights of a fermionic multiplet are integers. -/
def twoI3 (w : Fin 2 →₀ ℕ) : ℤ := (w 0 : ℤ) - (w 1 : ℤ)

/-- The `k`-th point of the degree-3 two-flavour diagram: `u^(3-k) d^k`. -/
noncomputable def quartetPoint (k : Fin 4) : Fin 2 →₀ ℕ :=
  Finsupp.single 0 (3 - (k : ℕ)) + Finsupp.single 1 (k : ℕ)

/-- Each `quartetPoint` really is a point of the diagram. -/
theorem quartetPoint_mem (k : Fin 4) : quartetPoint k ∈ weightDiagram 2 3 := by
  show (quartetPoint k).degree = 3
  rw [Finsupp.degree_eq_sum, Fin.sum_univ_two]
  simp only [quartetPoint, Finsupp.add_apply, Finsupp.single_eq_same,
    Finsupp.single_eq_of_ne, ne_eq, zero_ne_one, not_false_eq_true,
    one_ne_zero]
  omega

/-- **The ladder is attained.** `2I₃` on the four diagram points runs `3, 1, -1, -3`.
Together with `twoI3_mem_ladder` this makes the value set exactly those four. -/
theorem twoI3_quartetPoint (k : Fin 4) : twoI3 (quartetPoint k) = 3 - 2 * (k : ℤ) := by
  unfold twoI3 quartetPoint
  simp only [Finsupp.add_apply, Finsupp.single_eq_same, Finsupp.single_eq_of_ne,
    ne_eq, zero_ne_one, not_false_eq_true, one_ne_zero]
  omega

/-- **The ladder is closed.** Every point of the degree-3 two-flavour diagram carries one
of the four isospin-3/2 weights. -/
theorem twoI3_mem_ladder {w : Fin 2 →₀ ℕ} (hw : w ∈ weightDiagram 2 3) :
    twoI3 w = 3 ∨ twoI3 w = 1 ∨ twoI3 w = -1 ∨ twoI3 w = -3 := by
  have h := coordSum_of_mem hw
  have h1 : w 1 ≤ 3 := by omega
  unfold twoI3
  interval_cases hv : (w 1) <;> omega

/-- **The weights are half-integral**, i.e. `2I₃` is odd at every point. This is the
statement that distinguishes a fermionic multiplet, and it is degree-dependent: at even
degree the same construction gives even `2I₃`. -/
theorem twoI3_odd {w : Fin 2 →₀ ℕ} (hw : w ∈ weightDiagram 2 3) : ¬ (2 ∣ twoI3 w) := by
  have h := coordSum_of_mem hw
  unfold twoI3
  omega

/-- **The label is faithful.** Distinct points of the diagram carry distinct `I₃`, so the
four-dimensionality of `quadruplet_dim` is a count of four *isospin-labelled* states and
not merely of four basis vectors. -/
theorem twoI3_injOn : Set.InjOn twoI3 (weightDiagram 2 3) := by
  intro v hv w hw h
  have hv' := coordSum_of_mem hv
  have hw' := coordSum_of_mem hw
  unfold twoI3 at h
  have h0 : v 0 = w 0 := by omega
  have h1 : v 1 = w 1 := by omega
  ext i
  fin_cases i
  · exact h0
  · exact h1

end QOU.EightfoldWay.SymmetricChannelDimension
