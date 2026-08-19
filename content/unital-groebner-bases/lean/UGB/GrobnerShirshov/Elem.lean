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

/-- Zero out the coefficient at one monomial.  Used to peel an element apart
    one term at a time. -/
def eraseCoeff [DecidableEq G] (f : AlgElement G k) (m₀ : Monomial G) :
    AlgElement G k where
  coeff := fun m => if m = m₀ then 0 else f.coeff m
  support := f.support
  support_spec := by
    intro m hm
    by_cases h : m = m₀
    · exact if_pos h
    · rw [if_neg h]; exact f.support_spec m hm

@[simp] theorem eraseCoeff_self [DecidableEq G] (f : AlgElement G k)
    (m₀ : Monomial G) : (f.eraseCoeff m₀).coeff m₀ = 0 := by
  show (if m₀ = m₀ then (0 : k) else f.coeff m₀) = 0
  exact if_pos rfl

theorem eraseCoeff_of_ne [DecidableEq G] {f : AlgElement G k} {m m₀ : Monomial G}
    (h : m ≠ m₀) : (f.eraseCoeff m₀).coeff m = f.coeff m := by
  show (if m = m₀ then (0 : k) else f.coeff m) = f.coeff m
  exact if_neg h

@[simp] theorem eraseCoeff_support [DecidableEq G] (f : AlgElement G k)
    (m₀ : Monomial G) : (f.eraseCoeff m₀).support = f.support := rfl

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

/-- `contextMul` sends a coefficientwise negation to a coefficientwise negation.

The transfer lemma of §6 runs on this: a rule and its negative give
S-polynomials that are negatives of each other, and the two halves of an
S-polynomial are context-multiplications. -/
theorem contextMul_coeff_neg [DecidableEq G] (a b : Monomial G)
    {f g : AlgElement G k} (h : ∀ w, f.coeff w = -(g.coeff w)) (m : Monomial G) :
    (contextMul a f b).coeff m = -((contextMul a g b).coeff m) := by
  show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0)
     = -(if a ++ excise a m b ++ b = m then g.coeff (excise a m b) else 0)
  split_ifs
  · exact h _
  · rw [neg_zero]

/-- **Sliding a single generator across an element that commutes with it.**

If every monomial of `f` commutes with `x` *as a word* — `w ++ [x] = [x] ++ w` —
then multiplying on the right by `x` and multiplying on the left by `x` give the
same element.

This is the shape of a rule composed with itself over `xxx` when its relation is
a polynomial in the one generator `x`: the two halves of the S-polynomial are
this element slid past the same letter, so the S-polynomial vanishes outright
rather than merely reducing to zero. -/
theorem contextMul_gen_comm [DecidableEq G] (x : G) (f : AlgElement G k)
    (hf : ∀ w : Monomial G, f.coeff w ≠ 0 → w ++ [x] = [x] ++ w) (m : Monomial G) :
    (contextMul [] f [x]).coeff m = (contextMul [x] f []).coeff m := by
  by_cases hL : (contextMul [] f [x]).coeff m = 0
  · by_cases hR : (contextMul [x] f []).coeff m = 0
    · rw [hL, hR]
    · exfalso
      obtain ⟨w, hm, hw⟩ := contextMul_shape hR
      have hcomm := hf w hw
      rw [show m = [] ++ w ++ [x] by rw [hm]; simp [hcomm], contextMul_coeff_middle] at hL
      exact hw hL
  · obtain ⟨w, hm, hw⟩ := contextMul_shape hL
    have hcomm := hf w hw
    rw [hm, contextMul_coeff_middle,
      show ([] ++ w ++ [x] : Monomial G) = [x] ++ w ++ [] by simp [hcomm],
      contextMul_coeff_middle]

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

/-- `contextMul` sees only the coefficient function, so it respects `CoeffEq`.

Needed because `ofTerms` is a *representation*: the same element written with its
terms in a different order is a different value of `AlgElement` (different
`support`, different `coeff` term), so a rule can only be matched against a
normal form up to coefficients. -/
theorem contextMul_coeff_congr [DecidableEq G] (a b : Monomial G)
    {f g : AlgElement G k} (h : ∀ w, f.coeff w = g.coeff w) (m : Monomial G) :
    (contextMul a f b).coeff m = (contextMul a g b).coeff m := by
  show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0)
     = (if a ++ excise a m b ++ b = m then g.coeff (excise a m b) else 0)
  rw [h]

/-- **A relation in context is the same terms, in context.**

`contextMul` is defined through `excise`, so reading a coefficient off it is a
case split on whether the monomial has the shape `a ++ _ ++ b`. That split is the
same every time; this does it once, for a relation given by an explicit term
list. Every rule in a finite presentation is such a list, and every S-polynomial
is two context-multiplications of them, so this is the lemma that keeps a
composition's proof to word identities plus `split_ifs`.

The shape case split is the outer `by_cases`; the induction on `L` inside it only
has to push `List.filter` through `List.map`, because `w ↦ a ++ w ++ b` is
injective and append-cancellation is `simp`. -/
theorem contextMul_ofTerms_coeff [DecidableEq G] (a b : Monomial G)
    (L : List (Monomial G × k)) (m : Monomial G) :
    (contextMul a (ofTerms L) b).coeff m
      = (ofTerms (L.map (fun p => (a ++ p.1 ++ b, p.2)))).coeff m := by
  by_cases hs : ∃ w : Monomial G, m = a ++ w ++ b
  · obtain ⟨w, rfl⟩ := hs
    rw [contextMul_coeff_middle, ofTerms_coeff, ofTerms_coeff]
    induction L with
    | nil => rfl
    | cons p t ih =>
      simp only [List.map_cons, List.filter_cons, decide_eq_true_eq,
        List.append_cancel_left_eq, List.append_cancel_right_eq]
      split_ifs
      · simp only [List.map_cons, List.sum_cons, ih]
      · exact ih
  · rw [contextMul_coeff_of_not_shape _ (fun w hw => hs ⟨w, hw⟩), ofTerms_coeff]
    induction L with
    | nil => rfl
    | cons p t ih =>
      rw [List.map_cons, List.filter_cons,
        if_neg (by simpa using (fun h => hs ⟨p.1, h.symm⟩ : ¬ (a ++ p.1 ++ b = m)))]
      exact ih

/-- **A two-term relation in context is the same two terms, in context.**

Every rule in a two-term presentation — braid, far-commutation, Bokut–Shiao —
has this shape, and an S-polynomial is built out of exactly two such
context-multiplications. Computing one from the `excise` definition each time is
the same case split every time; this does it once.

The proof is the only place the shape condition has to be reasoned about: on the
shape `a ++ w ++ b` both sides reduce to append-cancellation, and off it both
sides are zero because a matching term would exhibit the missing `w`. -/
theorem contextMul_ofTerms_pair_coeff [DecidableEq G] (a b w₁ w₂ : Monomial G)
    (c₁ c₂ : k) (m : Monomial G) :
    (contextMul a (ofTerms [(w₁, c₁), (w₂, c₂)]) b).coeff m
      = (ofTerms [(a ++ w₁ ++ b, c₁), (a ++ w₂ ++ b, c₂)]).coeff m := by
  by_cases hs : ∃ w : Monomial G, m = a ++ w ++ b
  · obtain ⟨w, rfl⟩ := hs
    rw [contextMul_coeff_middle, ofTerms_coeff, ofTerms_coeff]
    simp only [List.filter_cons, List.filter_nil, decide_eq_true_eq,
      List.append_assoc, List.append_cancel_left_eq, List.append_cancel_right_eq]
    split_ifs <;> rfl
  · rw [contextMul_coeff_of_not_shape _ (fun w hw => hs ⟨w, hw⟩), ofTerms_coeff]
    have h₁ : ¬ (a ++ w₁ ++ b = m) := fun h => hs ⟨w₁, h.symm⟩
    have h₂ : ¬ (a ++ w₂ ++ b = m) := fun h => hs ⟨w₂, h.symm⟩
    rw [List.filter_cons, if_neg (by simpa using h₁), List.filter_cons,
      if_neg (by simpa using h₂), List.filter_nil]
    rfl

end AlgElement

end UGB.GrobnerShirshov
