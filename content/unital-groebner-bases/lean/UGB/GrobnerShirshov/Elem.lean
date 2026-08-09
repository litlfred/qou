import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Image

/-!
# Elements of the free associative algebra, and their arithmetic

`AlgElement G k` is the raw carrier used throughout `UGB.GrobnerShirshov`:
a coefficient function `Monomial G → k` together with a finite `support`
that is only required to be a *superset* of the monomials carrying a
non-zero coefficient.

This module holds the type and **all** of its algebraic operations, so that
`Basic.lean` — which needs subtraction, scalar multiplication and two-sided
multiplication by monomials in order to state a reduction step — can use them
without a cyclic import. (`AlgOps.lean` previously held them, but `AlgOps`
imports `Basic`; the operations were moved here and `Basic` now imports this
file. Nothing was renamed, and everything stays in the `UGB.GrobnerShirshov`
namespace, so downstream references are unaffected.)

## The support field is not canonical

Because `support` may be strictly larger than `{m | coeff m ≠ 0}`, *no*
mathematical statement about an element should be phrased in terms of it.
Two `AlgElement`s with the same coefficients but different supports denote
the same element of `k⟨G⟩`. Hence:

- `AlgElement.isZero f` means `∀ m, f.coeff m = 0`, **not** `f.support = ∅`;
- `AlgElement.CoeffEq f g` is the equality of elements that matters.

`support` is retained only to keep sums over an element finite.

## Design notes

- **Supports are supersets**: `add f g` uses `f.support ∪ g.support`, which is
  valid but may overcount (cancellation). `support_spec` only requires zero
  coefficients *outside* the support.
- **DecidableEq on monomials**: required for `Finset.image` and for the
  shape test in `contextMul`. `Monomial G = List G`, so `DecidableEq G`
  suffices.
- **No general multiplication**: convolution on `List G` requires summing over
  all factorizations. What the rewriting theory actually needs is
  multiplication by a *monomial* on each side — `contextMul a f b = a · f · b`
  — and that is exact and cheap.

## References

- Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), 178–218.
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Monomials -/

/-- A **monomial** in a free associative algebra on generators of type `G`.
    Represented as a list (word) of generators, with `[]` as the empty
    monomial (unit `1`). -/
abbrev Monomial (G : Type u) := List G

/-- `excise a m b` is the candidate middle factor of `m` between the contexts
    `a` and `b`: drop `|a|` letters from the front and `|b|` from the back.
    It is the *only* possible `w` with `m = a ++ w ++ b`, which is what makes
    the shape test in `contextMul` a decidable equation rather than an
    existential. -/
def excise {G : Type u} (a m b : Monomial G) : Monomial G :=
  (m.drop a.length).take (m.length - a.length - b.length)

@[simp] theorem excise_middle {G : Type u} (a w b : Monomial G) :
    excise a (a ++ w ++ b) b = w := by
  have hlen : (a ++ w ++ b).length - a.length - b.length = w.length := by
    simp only [List.length_append]; omega
  rw [excise, hlen, List.append_assoc, List.drop_left' rfl, List.take_left' rfl]

/-- The middle factor is uniquely determined: if `m = a ++ w ++ b` then
    `w = excise a m b`. -/
theorem excise_eq_of_eq {G : Type u} {a m b w : Monomial G}
    (h : m = a ++ w ++ b) : excise a m b = w := by
  subst h; exact excise_middle a w b

/-! ## §2  Algebra elements -/

/-- An element of the free associative algebra `k⟨G⟩` over a ring `k`,
    represented as a finitely-supported linear combination of monomials.

    For the formalization we work abstractly: an element is a function
    from monomials to coefficients with finite support. -/
structure AlgElement (G : Type u) (k : Type v) [Ring k] where
  /-- Coefficient of each monomial. -/
  coeff : Monomial G → k
  /-- The support is finite. -/
  support : Finset (Monomial G)
  /-- Coefficients outside the support are zero. -/
  support_spec : ∀ m, m ∉ support → coeff m = 0

namespace AlgElement

variable {G : Type u} {k : Type v} [Ring k]

/-- The zero element of the free algebra. -/
def zero : AlgElement G k where
  coeff := fun _ => 0
  support := ∅
  support_spec := fun _ _ => rfl

/-- **Equality of elements.** `AlgElement` is a representation, not a
    quotient: the `support` field is a superset of the true support, so two
    structurally different values can denote the same element of `k⟨G⟩`.
    `CoeffEq` is the equality that means anything mathematically. -/
def CoeffEq (f g : AlgElement G k) : Prop := ∀ m, f.coeff m = g.coeff m

/-- An element **is zero** when every coefficient vanishes.

    Note this is *not* `f.support = ∅`: the support field is an arbitrary
    superset of `{m | coeff m ≠ 0}`, so `support = ∅` is a statement about the
    chosen representation and not about the element. (It was the earlier
    definition; with a representation-independent notion of reduction it would
    make `IsGrobnerShirshovBasis` unsatisfiable rather than merely wrong,
    since the difference `f - f` carries the support `f.support ∪ f.support`.)
    -/
def isZero (f : AlgElement G k) : Prop := ∀ m, f.coeff m = 0

theorem isZero_zero : (zero : AlgElement G k).isZero := fun _ => rfl

/-- A representation with empty support is zero. -/
theorem isZero_of_support_eq_empty {f : AlgElement G k} (h : f.support = ∅) :
    f.isZero := fun m => f.support_spec m (by rw [h]; exact Finset.notMem_empty m)

/-- A monomial carrying a non-zero coefficient lies in the support. -/
theorem mem_support_of_coeff_ne_zero {f : AlgElement G k} {m : Monomial G}
    (h : f.coeff m ≠ 0) : m ∈ f.support := by
  by_contra hm
  exact h (f.support_spec m hm)

/-! ### §2.1  Singletons -/

/-- A single monomial with coefficient `c`.  The basis of all
    `AlgElement` construction. -/
def single [DecidableEq G] [DecidableEq k] (m : Monomial G) (c : k) :
    AlgElement G k where
  coeff := fun m' => if m' = m then c else 0
  support := if c = 0 then ∅ else {m}
  support_spec := by
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m' hm'
    by_cases hc : c = 0
    · -- c = 0: coefficient function is identically zero
      subst hc
      split_ifs <;> rfl
    · -- c ≠ 0: support is {m}, so m' ≠ m, hence coeff m' = 0
      simp [hc] at hm'
      exact if_neg hm'

@[simp] theorem single_coeff_self [DecidableEq G] [DecidableEq k]
    (m : Monomial G) (c : k) : (single m c : AlgElement G k).coeff m = c := by
  show (if m = m then c else 0) = c
  exact if_pos rfl

@[simp] theorem single_coeff_of_ne [DecidableEq G] [DecidableEq k]
    {m m' : Monomial G} (c : k) (h : m' ≠ m) :
    (single m c : AlgElement G k).coeff m' = 0 := by
  show (if m' = m then c else 0) = 0
  exact if_neg h

/-- A single monomial with coefficient 1. -/
def singleton [DecidableEq G] [DecidableEq k] (m : Monomial G) :
    AlgElement G k :=
  single m 1

/-- The singleton of a monomial has nonempty support. -/
theorem singleton_support_nonempty [DecidableEq G] [DecidableEq k] [Nontrivial k]
    (m : Monomial G) :
    (singleton m : AlgElement G k).support.Nonempty := by
  unfold singleton single
  simp

@[simp] theorem singleton_coeff_self [DecidableEq G] [DecidableEq k]
    (m : Monomial G) : (singleton m : AlgElement G k).coeff m = 1 :=
  single_coeff_self m 1

@[simp] theorem singleton_coeff_of_ne [DecidableEq G] [DecidableEq k]
    {m m' : Monomial G} (h : m' ≠ m) :
    (singleton m : AlgElement G k).coeff m' = 0 :=
  single_coeff_of_ne 1 h

/-! ### §2.2  Addition, scalar multiplication, negation, subtraction -/

/-- Add two algebra elements.  Support is the union (possibly
    an oversized superset due to cancellation). -/
def add [DecidableEq G] (f g : AlgElement G k) : AlgElement G k where
  coeff := fun m => f.coeff m + g.coeff m
  support := f.support ∪ g.support
  support_spec := by
    intro m hm
    simp only [Finset.mem_union, not_or] at hm
    rw [f.support_spec m hm.1, g.support_spec m hm.2, add_zero]

@[simp] theorem add_coeff [DecidableEq G] (f g : AlgElement G k) (m : Monomial G) :
    (add f g).coeff m = f.coeff m + g.coeff m := rfl

/-- Scalar multiply: `c • f`. -/
def smul (c : k) (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => c * f.coeff m
  support := f.support  -- oversized if c = 0, but still valid
  support_spec := by
    intro m hm
    rw [f.support_spec m hm, mul_zero]

@[simp] theorem smul_coeff (c : k) (f : AlgElement G k) (m : Monomial G) :
    (smul c f).coeff m = c * f.coeff m := rfl

/-- Negate an algebra element. -/
def neg (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => -(f.coeff m)
  support := f.support
  support_spec := by
    intro m hm
    rw [f.support_spec m hm, neg_zero]

@[simp] theorem neg_coeff (f : AlgElement G k) (m : Monomial G) :
    (neg f).coeff m = -(f.coeff m) := rfl

/-- Subtract: `f - g`. -/
def sub [DecidableEq G] (f g : AlgElement G k) : AlgElement G k := add f (neg g)

@[simp] theorem sub_coeff [DecidableEq G] (f g : AlgElement G k) (m : Monomial G) :
    (sub f g).coeff m = f.coeff m - g.coeff m := (sub_eq_add_neg _ _).symm

/-! ### §2.3  Two-sided multiplication by monomials -/

/-- **Context multiplication** `a · f · b`: multiply `f` on the left by the
    monomial `a` and on the right by the monomial `b`.

    This is the operation a rewriting step is built from — replacing an
    occurrence of a rule's leading monomial *inside* a larger word means
    subtracting `c • (a · relation · b)`. It is exact (no convolution needed)
    because `a` and `b` are monomials: the coefficient of `a ++ w ++ b` is the
    coefficient of `w`, and every other monomial gets `0`. -/
def contextMul [DecidableEq G] (a : Monomial G) (f : AlgElement G k)
    (b : Monomial G) : AlgElement G k where
  coeff := fun m => if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0
  support := f.support.image (fun w => a ++ w ++ b)
  support_spec := by
    intro m hm
    by_cases h : a ++ excise a m b ++ b = m
    · rw [if_pos h]
      refine f.support_spec _ (fun hmem => hm ?_)
      exact Finset.mem_image.mpr ⟨excise a m b, hmem, h⟩
    · exact if_neg h

@[simp] theorem contextMul_coeff_middle [DecidableEq G] (a b w : Monomial G)
    (f : AlgElement G k) : (contextMul a f b).coeff (a ++ w ++ b) = f.coeff w := by
  show (if a ++ excise a (a ++ w ++ b) b ++ b = a ++ w ++ b then
          f.coeff (excise a (a ++ w ++ b) b) else 0) = f.coeff w
  rw [excise_middle, if_pos rfl]

/-- Off the shape `a ++ _ ++ b` the coefficient is zero. -/
theorem contextMul_coeff_of_not_shape [DecidableEq G] {a b m : Monomial G}
    (f : AlgElement G k) (h : ∀ w : Monomial G, m ≠ a ++ w ++ b) :
    (contextMul a f b).coeff m = 0 := by
  show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0) = 0
  exact if_neg (fun hc => h (excise a m b) hc.symm)

/-- Every monomial carrying a non-zero coefficient in `a · f · b` has the
    shape `a ++ w ++ b` with `w` carrying a non-zero coefficient in `f`. -/
theorem contextMul_shape [DecidableEq G] {a b m : Monomial G}
    {f : AlgElement G k} (h : (contextMul a f b).coeff m ≠ 0) :
    ∃ w : Monomial G, m = a ++ w ++ b ∧ f.coeff w ≠ 0 := by
  by_cases hs : a ++ excise a m b ++ b = m
  · refine ⟨excise a m b, hs.symm, fun hz => h ?_⟩
    show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0) = 0
    rw [if_pos hs]; exact hz
  · refine absurd ?_ h
    show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0) = 0
    exact if_neg hs

@[simp] theorem contextMul_nil_nil_coeff [DecidableEq G] (f : AlgElement G k)
    (m : Monomial G) : (contextMul [] f []).coeff m = f.coeff m := by
  have := contextMul_coeff_middle ([] : Monomial G) ([] : Monomial G) m f
  simpa using this

/-! ### §2.4  Multiplication by a single generator (legacy helpers) -/

/-- Left-multiply by a single generator: `g · f`.
    Prepends `g` to every monomial in the support.

    `(g · f).coeff (g :: t) = f.coeff t` and `(g · f).coeff other = 0`. -/
def leftMulGen [DecidableEq G] (gen : G) (f : AlgElement G k) :
    AlgElement G k where
  coeff := fun m =>
    match m with
    | [] => 0
    | h :: t => if h = gen then f.coeff t else 0
  support := f.support.image (fun m => gen :: m)
  support_spec := by
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m hm
    cases m with
    | nil => rfl
    | cons h t =>
      by_cases hhg : h = gen
      · subst hhg
        have h_t_zero : f.coeff t = 0 := by
          apply f.support_spec
          intro ht
          apply hm
          exact Finset.mem_image.mpr ⟨t, ht, rfl⟩
        simp [h_t_zero]
      · exact if_neg hhg

/-- Right-multiply by a single generator: `f · g`.
    Appends `g` to every monomial in the support. -/
def rightMulGen [DecidableEq G] (f : AlgElement G k) (gen : G) :
    AlgElement G k where
  coeff := fun m =>
    if hne : m ≠ [] then
      if m.getLast hne = gen then f.coeff m.dropLast else 0
    else 0
  support := f.support.image (fun m => m ++ [gen])
  support_spec := by
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m hm
    by_cases hne0 : m = []
    · subst hne0; rfl
    · have hne : m ≠ [] := hne0
      simp only [hne, ne_eq, not_false_eq_true, dif_pos]
      by_cases hlast : m.getLast hne = gen
      · rw [if_pos hlast]
        apply f.support_spec
        intro hsupp
        apply hm
        refine Finset.mem_image.mpr ⟨m.dropLast, hsupp, ?_⟩
        conv_rhs => rw [← List.dropLast_append_getLast hne]
        rw [hlast]
      · exact if_neg hlast

/-- Left-multiply by a word (list of generators): `w · f`.
    Defined by folding `leftMulGen` from right to left:
    `[g₁, g₂, g₃] · f = g₁ · (g₂ · (g₃ · f))`. -/
def leftMulWord [DecidableEq G] (w : List G) (f : AlgElement G k) :
    AlgElement G k :=
  w.foldr (fun g acc => leftMulGen g acc) f

/-! ### §2.5  Building elements from term lists -/

/-- Build an algebra element from a list of (monomial, coefficient) pairs.
    This is the primary constructor for rewriting rule relations. -/
def ofTerms [DecidableEq G] (terms : List (Monomial G × k)) :
    AlgElement G k where
  coeff := fun m => ((terms.filter (fun p => p.1 = m)).map Prod.snd).sum
  support := (terms.map Prod.fst).toFinset
  support_spec := by
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    -- Per Gemini review on PR #467: m ∉ supports of `terms` ⇒
    -- the filter is empty ⇒ the coefficient sum is zero.
    intro m hm
    rw [List.mem_toFinset, List.mem_map, not_exists] at hm
    push_neg at hm
    have h_empty : terms.filter (fun p => p.1 = m) = [] := by
      rw [List.filter_eq_nil_iff]
      intro x hx heq
      exact hm x hx (decide_eq_true_eq.mp heq)
    rw [h_empty, List.map_nil, List.sum_nil]

/-- `ofTerms` with a nonempty term list has nonempty support. -/
theorem ofTerms_support_nonempty [DecidableEq G]
    {terms : List (Monomial G × k)} (h : terms ≠ []) :
    (ofTerms terms).support.Nonempty := by
  -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
  cases terms with
  | nil => exact absurd rfl h
  | cons head tail =>
    refine ⟨head.1, ?_⟩
    show head.1 ∈ ((head :: tail).map Prod.fst).toFinset
    simp

theorem ofTerms_coeff [DecidableEq G] (terms : List (Monomial G × k))
    (m : Monomial G) :
    (ofTerms terms).coeff m = ((terms.filter (fun p => p.1 = m)).map Prod.snd).sum :=
  rfl

end AlgElement

end UGB.GrobnerShirshov
