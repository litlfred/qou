import QOU.BraidKnot.CompositionCosetReduceMirror

/-!
# Mathas' Lemma 3.9 at the level of spans: the double-coset terms are everything

Putting the two coset reductions together:

    `H · x_μ · H = span { T_d · x_μ · T_e : d ∈ D_μ, e⁻¹ ∈ D_μ }`

Every product with `x_μ` in the middle, however the two outer factors are chosen, is an
`R`-combination of the **double-coset-indexed** terms — and, because both reductions
produce only powers of `q`, the coefficients are `q`-powers times the basis coefficients
of the outer factors.  That is Mathas' Lemma 3.9 in span form.

## The `T_d⁻¹` expansion turns out not to be needed

The plan recorded on the previous branch was to expand `T_d⁻¹` over the Bruhat interval
`[e, d⁻¹]` (`TwInverseBruhat.TwInv_mem_spanBruhatLe`) and control the surviving terms.
That is **not necessary for this statement**: expanding the outer factors in the `T`-basis
is already enough, since each `T_h · x_μ` and `x_μ · T_k` reduces on its own.

The interval bound is still the sharp fact and remains worth having — it is what would
bound *which* `d` occur, rather than merely that some do — but it is a refinement of this
result, not an input to it.  Recording that because the reverse impression would send the
next agent to build machinery it does not need.

## Scope: this is the span statement, not the basis statement

What is **not** proved here is that the `T_d · x_μ · T_e` are linearly *independent*, nor
that the index set matches pairs of row-standard tableaux under
`CompositionTableau.existsUnique_rowStandard`.  The first is a genuine further claim; the
second is the tableau-vocabulary step.  Mathas' 3.9 asks only for the combination, which is
what is proved — but a reader should not take "3.9 is done" to mean the Murphy basis is.
-/

namespace QOU.BraidKnot.CompositionDoubleCoset

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy
open QOU.BraidKnot.CompositionCosetSum QOU.BraidKnot.CompositionCosetReduce
open QOU.BraidKnot.CompositionCosetReduceMirror
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.TwBasis Equiv

variable {n : ℕ} (K : Type*) [Field K] (q : K)

/-- **The double-coset span**: everything of the form `T_d · x_μ · T_e` with `d`
distinguished on the right and `e` on the left. -/
noncomputable def spanDoubleCoset (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] : Submodule K (QOU.Hecke.IwahoriHecke K q n) :=
  Submodule.span K
    {x | ∃ d e : Perm (Fin (n + 1)), IsDistinguished c d ∧ IsDistinguishedL c e ∧
      x = Tw K q n d * xComp K q c * Tw K q n e}

/-- The `T_w` span the algebra — `basisTwOfField` restated as a spanning statement. -/
theorem span_range_Tw_eq_top :
    Submodule.span K (Set.range (Tw K q n)) = (⊤ : Submodule K (QOU.Hecke.IwahoriHecke K q n)) := by
  have h := (basisTwOfField K q n).span_eq
  rwa [coe_basisTwOfField] at h

/-- **Base case**: a product of two basis elements around `x_μ`. -/
theorem Tw_mul_xComp_mul_Tw_mem (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] (h k : Perm (Fin (n + 1))) :
    Tw K q n h * xComp K q c * Tw K q n k ∈ spanDoubleCoset K q c := by
  obtain ⟨d, v, hd, -, -, hred⟩ := Tw_mul_xComp_reduce K q c h
  obtain ⟨e, w, he, -, -, hred'⟩ := xComp_mul_Tw_reduce K q c k
  have hstep : Tw K q n h * xComp K q c * Tw K q n k
      = (q ^ ((permCoxeterSystem n).length v) * q ^ ((permCoxeterSystem n).length w))
        • (Tw K q n d * xComp K q c * Tw K q n e) := by
    rw [hred, smul_mul_assoc, mul_assoc, hred', mul_smul_comm, smul_smul, mul_assoc]
  rw [hstep]
  exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨d, e, hd, he, rfl⟩)

/-- **Linear in the right factor.** -/
theorem Tw_mul_xComp_mul_mem (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] (h : Perm (Fin (n + 1)))
    (Y : QOU.Hecke.IwahoriHecke K q n) :
    Tw K q n h * xComp K q c * Y ∈ spanDoubleCoset K q c := by
  have hY : Y ∈ Submodule.span K (Set.range (Tw K q n)) := by
    rw [span_range_Tw_eq_top]; trivial
  induction hY using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨k, rfl⟩ := hy
      exact Tw_mul_xComp_mul_Tw_mem K q c h k
  | zero => simp only [mul_zero]; exact Submodule.zero_mem _
  | add a b _ _ ha hb => rw [mul_add]; exact add_mem ha hb
  | smul t a _ ha => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ ha

/-- **Mathas' Lemma 3.9, span form.**  Every `X · x_μ · Y` is an `R`-combination of the
double-coset terms, with `q`-power coefficients. -/
theorem mul_xComp_mul_mem (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] (X Y : QOU.Hecke.IwahoriHecke K q n) :
    X * xComp K q c * Y ∈ spanDoubleCoset K q c := by
  have hX : X ∈ Submodule.span K (Set.range (Tw K q n)) := by
    rw [span_range_Tw_eq_top]; trivial
  induction hX using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨h, rfl⟩ := hx
      exact Tw_mul_xComp_mul_mem K q c h Y
  | zero => simp only [zero_mul]; exact Submodule.zero_mem _
  | add a b _ _ ha hb => rw [add_mul, add_mul]; exact add_mem ha hb
  | smul t a _ ha => rw [smul_mul_assoc, smul_mul_assoc]; exact Submodule.smul_mem _ _ ha

end QOU.BraidKnot.CompositionDoubleCoset
