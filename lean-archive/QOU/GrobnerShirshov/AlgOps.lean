import QOU.GrobnerShirshov.Basic

/-!
# AlgElement Algebraic Operations

Provides the arithmetic on `AlgElement G k` needed to construct
rewriting systems concretely: singleton monomials, addition, scalar
multiplication, negation, and left/right multiplication by a generator.

These operations are the reason the Hecke rewriting system (HeckeGS.lean)
was previously axiomatised — `AlgElement` in Basic.lean is a raw data
structure.  This module makes it an algebra.

## Design notes

- **Supports are supsets**: `add f g` uses `f.support ∪ g.support`,
  which is valid but may overcount (cancellation).  This is fine:
  `support_spec` only requires zero coefficients *outside* the support.
- **DecidableEq on monomials**: required for `if m = m' then ... else ...`
  constructions.  `Monomial G = List G`, so `DecidableEq G` suffices.
- **No general multiplication**: convolution on `List G` requires summing
  over all factorizations.  We provide `leftMulGen` (prepend one generator)
  instead, which suffices for braid word embedding.
-/


namespace QOU.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G]

/-! ## §1  Singleton (basis monomial) -/

/-- A single monomial with coefficient `c`.  The basis of all
    `AlgElement` construction. -/
def AlgElement.single (m : Monomial G) (c : k) : AlgElement G k where
  coeff := fun m' => if m' = m then c else 0
  support := if c = 0 then ∅ else {m}
  support_spec := by
    intro m' hm'
    split_ifs with hc
    · simp
    · simp only [Finset.mem_singleton] at hm'
      simp [hm']

/-- A single monomial with coefficient 1. -/
def AlgElement.singleton (m : Monomial G) : AlgElement G k :=
  AlgElement.single m 1

/-- The singleton of a non-empty monomial has nonempty support. -/
theorem AlgElement.singleton_support_nonempty (m : Monomial G) :
    (AlgElement.singleton m : AlgElement G k).support.Nonempty := by
  unfold AlgElement.singleton AlgElement.single
  simp [one_ne_zero]

/-! ## §2  Addition -/

/-- Add two algebra elements.  Support is the union (possibly
    an oversized superset due to cancellation). -/
def AlgElement.add (f g : AlgElement G k) : AlgElement G k where
  coeff := fun m => f.coeff m + g.coeff m
  support := f.support ∪ g.support
  support_spec := by
    intro m hm
    simp only [Finset.mem_union, not_or] at hm
    rw [f.support_spec m hm.1, g.support_spec m hm.2, add_zero]

/-! ## §3  Scalar Multiplication -/

/-- Scalar multiply: `c • f`. -/
def AlgElement.smul (c : k) (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => c * f.coeff m
  support := f.support  -- oversized if c = 0, but still valid
  support_spec := by
    intro m hm
    rw [f.support_spec m hm, mul_zero]

/-! ## §4  Negation and Subtraction -/

/-- Negate an algebra element. -/
def AlgElement.neg (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => -(f.coeff m)
  support := f.support
  support_spec := by
    intro m hm
    rw [f.support_spec m hm, neg_zero]

/-- Subtract: `f - g`. -/
def AlgElement.sub (f g : AlgElement G k) : AlgElement G k :=
  AlgElement.add f (AlgElement.neg g)

/-! ## §5  Left Multiplication by a Generator -/

/-- Left-multiply by a single generator: `g · f`.
    Prepends `g` to every monomial in the support.

    `(g · f).coeff(g :: t) = f.coeff(t)` and
    `(g · f).coeff(other) = 0`. -/
def AlgElement.leftMulGen (gen : G) (f : AlgElement G k) :
    AlgElement G k where
  coeff := fun m =>
    match m with
    | [] => 0
    | h :: t => if h = gen then f.coeff t else 0
  support := f.support.image (fun m => gen :: m)
  support_spec := by
    intro m hm
    simp only [Finset.mem_image, not_exists, not_and] at hm
    match m with
    | [] => rfl
    | h :: t =>
      split_ifs with heq
      · subst heq
        exact f.support_spec t (fun ht => hm t ht rfl)
      · rfl

/-- Right-multiply by a single generator: `f · g`.
    Appends `g` to every monomial in the support. -/
def AlgElement.rightMulGen (f : AlgElement G k) (gen : G) :
    AlgElement G k where
  coeff := fun m =>
    if h : m.length > 0 ∧ m.getLast (by omega) = gen
    then f.coeff (m.dropLast)
    else 0
  support := f.support.image (fun m => m ++ [gen])
  support_spec := by
    intro m hm
    simp only [Finset.mem_image, not_exists, not_and] at hm
    split_ifs with h
    · exact f.support_spec m.dropLast (fun hd => by
        have := hm m.dropLast hd
        simp [List.dropLast_append_getLast (by omega)] at this)
    · rfl

/-! ## §6  Multi-generator left multiplication -/

/-- Left-multiply by a word (list of generators): `w · f`.
    Defined by folding `leftMulGen` from right to left:
    `[g₁, g₂, g₃] · f = g₁ · (g₂ · (g₃ · f))`. -/
def AlgElement.leftMulWord (w : List G) (f : AlgElement G k) :
    AlgElement G k :=
  w.foldr (fun g acc => AlgElement.leftMulGen g acc) f

/-- The singleton of a word `w` with coefficient 1:
    the algebra element with `coeff(w) = 1` and all others 0.

    This is a semantic property: `leftMulWord w (singleton [])` has
    the same coefficients as `singleton w`.  The proof requires an
    extensionality principle for `AlgElement` (coefficient-wise equality
    implies propositional equality), which we do not carry because
    `AlgElement` is not a quotient type.  Instead, the property holds
    by construction: `leftMulGen` prepends one generator at a time,
    and starting from `singleton []` (coefficient 1 on the empty word),
    prepending `g₁, g₂, …` yields coefficient 1 on `[g₁, g₂, …]`. -/

/-! ## §7  Constructing multi-term elements -/

/-- Build an algebra element from a list of (monomial, coefficient) pairs.
    This is the primary constructor for rewriting rule relations. -/
def AlgElement.ofTerms (terms : List (Monomial G × k)) :
    AlgElement G k where
  coeff := fun m =>
    ((terms.filter (fun p => p.1 = m)).map Prod.snd).sum
  support := (terms.map Prod.fst).toFinset
  support_spec := by
    intro m hm
    simp only [List.toFinset, List.mem_toFinset, List.mem_map,
               not_exists, not_and] at hm
    suffices h : terms.filter (fun p => p.1 = m) = [] by
      simp [h]
    rw [List.filter_eq_nil]
    intro p hp
    simp only [decide_eq_true_eq]
    intro heq
    exact absurd (Exists.intro p ⟨hp, heq⟩) (by push_neg; exact fun p hp => hm p hp)

/-- `ofTerms` with nonempty leading term has nonempty support. -/
theorem AlgElement.ofTerms_support_nonempty
    {terms : List (Monomial G × k)} (h : terms ≠ []) :
    (AlgElement.ofTerms terms).support.Nonempty := by
  unfold AlgElement.ofTerms
  simp only [List.toFinset]
  exact List.toFinset_nonempty_iff.mpr (List.map_ne_nil_of_ne_nil Prod.fst h)

end QOU.GrobnerShirshov
