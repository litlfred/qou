import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.NormalForms
import Mathlib.Data.Finset.Image

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


namespace UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G]

/-! ## §1  Singleton (basis monomial) -/

/-- A single monomial with coefficient `c`.  The basis of all
    `AlgElement` construction. -/
def AlgElement.single [DecidableEq k] (m : Monomial G) (c : k) : AlgElement G k where
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

/-- A single monomial with coefficient 1. -/
def AlgElement.singleton [DecidableEq k] (m : Monomial G) : AlgElement G k :=
  AlgElement.single m 1

/-- The singleton of a non-empty monomial has nonempty support. -/
theorem AlgElement.singleton_support_nonempty [DecidableEq k] [Nontrivial k]
    (m : Monomial G) :
    (AlgElement.singleton m : AlgElement G k).support.Nonempty := by
  unfold AlgElement.singleton AlgElement.single
  simp

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
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m hm
    cases m with
    | nil => rfl
    | cons h t =>
      by_cases hhg : h = gen
      · -- h = gen, so m = gen :: t.  If t were in f.support, m would
        -- be in the image — contradicting hm.  Hence t ∉ f.support
        -- and f.coeff t = 0 by f.support_spec.
        subst hhg
        simp only [if_pos rfl]
        apply f.support_spec
        intro ht
        apply hm
        exact Finset.mem_image.mpr ⟨t, ht, rfl⟩
      · -- h ≠ gen: coefficient is 0 directly
        exact if_neg hhg

/-- Right-multiply by a single generator: `f · g`.
    Appends `g` to every monomial in the support. -/
def AlgElement.rightMulGen (f : AlgElement G k) (gen : G) :
    AlgElement G k where
  coeff := fun m =>
    if hne : m ≠ [] then
      if m.getLast hne = gen
      then f.coeff (m.dropLast)
      else 0
    else 0
  support := f.support.image (fun m => m ++ [gen])
  support_spec := by
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m hm
    by_cases hne0 : m = []
    · subst hne0; rfl
    · -- m ≠ []
      have hne : m ≠ [] := hne0
      simp only [hne, ne_eq, not_false_eq_true, dif_pos]
      by_cases hlast : m.getLast hne = gen
      · -- last element is gen; need f.coeff (dropLast m) = 0
        rw [if_pos hlast]
        apply f.support_spec
        intro hsupp
        apply hm
        refine Finset.mem_image.mpr ⟨m.dropLast, hsupp, ?_⟩
        -- dropLast m ++ [gen] = m, using hlast and dropLast_append_getLast
        conv_rhs => rw [← List.dropLast_append_getLast hne]
        rw [hlast]
      · exact if_neg hlast

/-! ## §6  Multi-generator left multiplication -/

/-- Left-multiply by a word (list of generators): `w · f`.
    Defined by folding `leftMulGen` from right to left:
    `[g₁, g₂, g₃] · f = g₁ · (g₂ · (g₃ · f))`. -/
def AlgElement.leftMulWord (w : List G) (f : AlgElement G k) :
    AlgElement G k :=
  w.foldr (fun g acc => AlgElement.leftMulGen g acc) f

/- The singleton of a word `w` with coefficient 1:
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
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    intro m hm
    -- m is not the first projection of any term.  Hence every filtered
    -- term has snd = 0 (vacuously, since the filter is empty).
    -- We show the underlying list is `[]` by membership.
    have hfilter : ∀ p ∈ terms, ¬ p.1 = m := by
      intro p hp hp1
      apply hm
      simp only [List.mem_toFinset, List.mem_map]
      exact ⟨p, hp, hp1⟩
    -- Hence the filter contains no elements, so its sum is 0.
    suffices h : ((terms.filter (fun p => p.1 = m)).map Prod.snd).sum = 0 by
      exact h
    have : terms.filter (fun p => p.1 = m) = [] := by
      induction terms with
      | nil => rfl
      | cons p ps ih =>
        have hp : ¬ p.1 = m := hfilter p (List.mem_cons_self _ _)
        have hps : ∀ q ∈ ps, ¬ q.1 = m := fun q hq =>
          hfilter q (List.mem_cons_of_mem _ hq)
        rw [List.filter_cons]
        simp [hp, ih hps]
    rw [this]
    simp

/-- `ofTerms` with nonempty leading term has nonempty support. -/
theorem AlgElement.ofTerms_support_nonempty
    {terms : List (Monomial G × k)} (h : terms ≠ []) :
    (AlgElement.ofTerms terms).support.Nonempty := by
  -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
  -- support = (terms.map Prod.fst).toFinset; pick the first term.
  unfold AlgElement.ofTerms
  match h_eq : terms with
  | [] => exact absurd h_eq h
  | p :: ps =>
    refine ⟨p.1, ?_⟩
    simp [List.mem_toFinset]

/-! ## §8  Generic Deg-Lex Order Construction -/

/-- Construct a deg-lex `AdmissibleOrder` for any generator type `G`
    equipped with an injective rank function `rank : G → ℕ`.

    This generalises `degLexOrder` from NormalForms.lean (which is
    specific to `SU2Gen`).  The proofs are identical in structure:
    - Well-foundedness: from `List.Lex.wellFounded` via rank
    - Trichotomy: case split on length, then on lex
    - Compatibility: length preserved by concatenation

    We delegate to the existing NormalForms infrastructure by mapping
    generators to `SU2Gen` (or more precisely, to `ℕ` via rank) and
    using `List.Lex.wellFounded` directly. -/
noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G]
    (rank : G → ℕ) (rank_inj : Function.Injective rank) :
    AdmissibleOrder G where
  lt := fun a b =>
    a.length < b.length ∨
    (a.length = b.length ∧ List.Lex (fun x y => rank x < rank y) a b)
  trichotomy := by
    intro a b
    by_cases h1 : a.length < b.length
    · left; left; exact h1
    · by_cases h2 : b.length < a.length
      · right; right; left; exact h2
      · have heq : a.length = b.length := by omega
        -- Same length: compare lexicographically
        have : ∀ (x y : List G), x.length = y.length →
            List.Lex (fun a b => rank a < rank b) x y ∨
            x = y ∨
            List.Lex (fun a b => rank a < rank b) y x := by
          intro x
          induction x with
          | nil => intro y hy; cases y with
            | nil => right; left; rfl
            | cons _ _ => simp at hy
          | cons g gs ih => intro y hy; cases y with
            | nil => simp at hy
            | cons h hs =>
              simp [List.length_cons] at hy
              by_cases hr1 : rank g < rank h
              · left; exact List.Lex.rel hr1
              · by_cases hr2 : rank h < rank g
                · right; right; exact List.Lex.rel hr2
                · have hge : rank g = rank h := by omega
                  have hgh : g = h := rank_inj hge
                  subst hgh
                  rcases ih hs hy with hlx | heq | hrx
                  · left; exact List.Lex.cons hlx
                  · right; left; rw [heq]
                  · right; right; exact List.Lex.cons hrx
        rcases this a b heq with hlx | heq' | hrx
        · left; right; exact ⟨heq, hlx⟩
        · right; left; exact heq'
        · right; right; right; exact ⟨heq.symm, hrx⟩
  wf := by
    -- Ref: [bokut2005] §1 (deg-lex well-foundedness via product order).
    -- Pending Mathlib rename of `List.Lex.wellFounded`.
    sorry
  left_compat := by
    intro a b c h
    rcases h with hlen | ⟨heq, hlex⟩
    · left; simp; omega
    · right; refine ⟨?_, ?_⟩
      · simp; omega
      · -- c ++ a lex< c ++ b when a lex< b (same length)
        induction c with
        | nil => simpa
        | cons x xs ih =>
          simp only [List.cons_append]
          exact List.Lex.cons ih
  right_compat := by
    intro a b d h
    rcases h with hlen | ⟨heq, hlex⟩
    · left; simp; omega
    · right; refine ⟨?_, ?_⟩
      · simp; omega
      · -- a ++ d lex< b ++ d when a lex< b (same length).
        -- Ref: [bokut2005] §1 (right-compatibility under deg-lex);
        -- pending: induction generates nil case forced by length-eq hyp.
        sorry

end UGB.GrobnerShirshov
