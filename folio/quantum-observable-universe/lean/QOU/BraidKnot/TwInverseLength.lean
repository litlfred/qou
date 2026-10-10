import QOU.BraidKnot.CompositionIdeal

/-!
# `T_w⁻¹` lives in length `≤ ℓ(w)` — the Bruhat-free half of triangularity

Reaching Mathas' Lemma 3.9 at the level of `m_{st}` (rather than of `x_μ`, which
`CompositionIdeal.exists_xComp_swap` settles) means expanding `T_d⁻¹` in the `T`-basis and
controlling where it lands.  Measured exactly over `S_2`, `S_3`, `S_4` in
[`tw_inverse_support_probe.py`](../../../../../computations/hecke/tw_inverse_support_probe.py),
the support is the **Bruhat interval `[e, w⁻¹]`** — note the inverse, which is the
`Tw_mul_Tw` handedness flip again — with leading coefficient `q^{-ℓ(w)}`.

The full statement needs a Bruhat order, and **there is none to hand**: Mathlib's
`GroupTheory/Coxeter/` carries no `Bruhat` at all, and the corpus's
`QOU/Mathlib/KazhdanLusztigBasis.lean` is an abstract `BarInvolution`/`KLBasis`
axiomatisation with no concrete construction.  Building that order is a separate piece of
work.

**This file proves the half that needs none of it**: the *length* bound, measured 32/32 by
the same probe.  It is the "no escape upward" half of triangularity, and unlike the Bruhat
half it requires nothing beyond the corpus's own multiplication rule — `σ_mul_Tw` already
says `σ_i · T_v` lies in the span of `T_v` and `T_{v·sᵢ}`, in *both* of its branches.

## Why the inverse is built rather than taken

`CompositionIdeal.isUnit_Tw` gives `T_w` a unit, but a unit's inverse is opaque: nothing
about `↑u⁻¹` can be induced over.  So `TwInvOf` builds the inverse explicitly as the
product of the `σᵢ⁻¹` along the reversed word — `Tw_mul_TwInv` and `TwInv_mul_Tw` check
that it *is* the inverse — and the span bound is then a list induction on that word.

Note the ordering: `TwOf` folds as `ω.foldl (fun h i => σ i * h) 1`, i.e.
`σ_{i_k} ⋯ σ_{i_1}`, so the inverse is `σ_{i_1}⁻¹ ⋯ σ_{i_k}⁻¹` — a `foldr`, not a
`foldl`.  Getting that backwards produces something that is not an inverse at all.
-/

namespace QOU.BraidKnot.TwInverseLength

open QOU.Hecke.TwBasis QOU.Hecke.IwahoriHecke QOU.Hecke.SymmetricCoxeter Equiv
open QOU.BraidKnot.HeckeMurphy

variable (K : Type*) [Field K] (q : K) {n : ℕ}

/-! ### The filtration by length -/

/-- **`span {T_v : ℓ(v) ≤ k}`** — the length filtration of `H_n(q)`. -/
noncomputable def spanLe (k : ℕ) : Submodule K (QOU.Hecke.IwahoriHecke K q n) :=
  Submodule.span K
    {x | ∃ v : Perm (Fin (n + 1)), (permCoxeterSystem n).length v ≤ k ∧ x = Tw K q n v}

theorem Tw_mem_spanLe {v : Perm (Fin (n + 1))} {k : ℕ}
    (h : (permCoxeterSystem n).length v ≤ k) : Tw K q n v ∈ spanLe K q k :=
  Submodule.subset_span ⟨v, h, rfl⟩

theorem one_mem_spanLe (k : ℕ) : (1 : QOU.Hecke.IwahoriHecke K q n) ∈ spanLe K q (n := n) k := by
  have := Tw_mem_spanLe K q (v := (1 : Perm (Fin (n + 1)))) (k := k) (by simp)
  rwa [Tw_one] at this

theorem spanLe_mono {k m : ℕ} (h : k ≤ m) :
    spanLe K q (n := n) k ≤ spanLe K q (n := n) m := by
  refine Submodule.span_mono ?_
  rintro x ⟨v, hv, rfl⟩
  exact ⟨v, hv.trans h, rfl⟩

/-- `ℓ(v · sᵢ) ≤ ℓ(v) + 1` — either branch of `length_mul_simple`. -/
theorem length_mul_sw_le (v : Perm (Fin (n + 1))) (i : Fin n) :
    (permCoxeterSystem n).length (v * sw i) ≤ (permCoxeterSystem n).length v + 1 := by
  rw [← simple_eq_sw]
  rcases (permCoxeterSystem n).length_mul_simple v i with h | h <;> omega

/-- **The filtration step.**  Multiplying by a generator raises length by at most one,
because `σ_mul_Tw` lands in the span of `T_v` and `T_{v·sᵢ}` in both of its branches. -/
theorem σ_mul_mem_spanLe {k : ℕ} {x : QOU.Hecke.IwahoriHecke K q n}
    (hx : x ∈ spanLe K q k) (i : Fin n) :
    σ K q n i * x ∈ spanLe K q (k + 1) := by
  induction hx using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨v, hv, rfl⟩ := hy
      have hlen : (permCoxeterSystem n).length (v * sw i) ≤ k + 1 :=
        le_trans (length_mul_sw_le v i) (by omega)
      have hv' : (permCoxeterSystem n).length v ≤ k + 1 := by omega
      rw [σ_mul_Tw]
      by_cases h : v i.castSucc < v i.succ
      · rw [if_pos h]
        exact Tw_mem_spanLe K q (v := v * sw i) hlen
      · rw [if_neg h]
        exact add_mem
          (Submodule.smul_mem _ _ (Tw_mem_spanLe K q hv'))
          (Submodule.smul_mem _ _ (Tw_mem_spanLe K q (v := v * sw i) hlen))
  | zero => simp only [mul_zero]; exact Submodule.zero_mem _
  | add a b _ _ ha hb => rw [mul_add]; exact add_mem ha hb
  | smul c a _ ha => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ ha

variable [Invertible q]

/-- The same for `σᵢ⁻¹`, which is `⅟q · (σᵢ − (q−1))` and so adds no new support. -/
theorem σInv_mul_mem_spanLe {k : ℕ} {x : QOU.Hecke.IwahoriHecke K q n}
    (hx : x ∈ spanLe K q k) (i : Fin n) :
    σInv K q n i * x ∈ spanLe K q (k + 1) := by
  have hstep : σInv K q n i * x = ⅟q • (σ K q n i * x) - (⅟q * (q - 1)) • x := by
    rw [σInv, smul_mul_assoc, sub_mul, smul_mul_assoc, one_mul, smul_sub, smul_smul]
  rw [hstep]
  exact sub_mem
    (Submodule.smul_mem _ _ (σ_mul_mem_spanLe K q hx i))
    (Submodule.smul_mem _ _ (spanLe_mono K q (Nat.le_succ k) hx))

/-! ### The inverse, built explicitly -/

/-- `T_ω⁻¹` along a word: `σ_{i_1}⁻¹ ⋯ σ_{i_k}⁻¹`, the reverse order of `TwOf`. -/
noncomputable def TwInvOf (ω : List (Fin n)) : QOU.Hecke.IwahoriHecke K q n :=
  ω.foldr (fun i h => σInv K q n i * h) 1

@[simp] theorem TwInvOf_nil : TwInvOf K q ([] : List (Fin n)) = 1 := rfl

@[simp] theorem TwInvOf_cons (i : Fin n) (ω : List (Fin n)) :
    TwInvOf K q (i :: ω) = σInv K q n i * TwInvOf K q ω := rfl

omit [Invertible q] in
theorem foldl_sigma (ω : List (Fin n)) (a : QOU.Hecke.IwahoriHecke K q n) :
    ω.foldl (fun h i => σ K q n i * h) a
      = (ω.foldl (fun h i => σ K q n i * h) 1) * a := by
  induction ω generalizing a with
  | nil => simp
  | cons i ω ih =>
      rw [List.foldl_cons, List.foldl_cons, ih (σ K q n i * a),
        ih (σ K q n i * 1), mul_one, mul_assoc]

omit [Invertible q] in
theorem TwOf_cons (i : Fin n) (ω : List (Fin n)) :
    TwOf K q n (i :: ω) = TwOf K q n ω * σ K q n i := by
  show (i :: ω).foldl (fun h i => σ K q n i * h) 1 = _
  rw [List.foldl_cons, mul_one, foldl_sigma]
  rfl

/-- **`TwInvOf` is the inverse of `TwOf`** — the check that the `foldr` ordering is the
right one.  A `foldl` here would not be an inverse. -/
theorem TwOf_mul_TwInvOf (ω : List (Fin n)) :
    TwOf K q n ω * TwInvOf K q ω = 1 := by
  induction ω with
  | nil => simp [TwOf]
  | cons i ω ih =>
      rw [TwOf_cons, TwInvOf_cons, mul_assoc, ← mul_assoc (σ K q n i),
        σ_mul_σInv, one_mul, ih]

theorem TwInvOf_mul_TwOf (ω : List (Fin n)) :
    TwInvOf K q ω * TwOf K q n ω = 1 := by
  induction ω with
  | nil => simp [TwOf]
  | cons i ω ih =>
      rw [TwOf_cons, TwInvOf_cons, mul_assoc, ← mul_assoc (TwInvOf K q ω),
        ih, one_mul, σInv_mul_σ]

/-- **The length bound, along a word.** -/
theorem TwInvOf_mem_spanLe (ω : List (Fin n)) :
    TwInvOf K q ω ∈ spanLe K q (n := n) ω.length := by
  induction ω with
  | nil => simpa using one_mem_spanLe K q 0
  | cons i ω ih =>
      rw [TwInvOf_cons, List.length_cons]
      exact σInv_mul_mem_spanLe K q ih i

/-! ### The headline -/

/-- **`T_w⁻¹`**, built from the chosen reduced word for `w`. -/
noncomputable def TwInv (w : Perm (Fin (n + 1))) : QOU.Hecke.IwahoriHecke K q n :=
  TwInvOf K q (reducedWord n w)

theorem Tw_mul_TwInv (w : Perm (Fin (n + 1))) :
    Tw K q n w * TwInv K q w = 1 := TwOf_mul_TwInvOf K q _

theorem TwInv_mul_Tw (w : Perm (Fin (n + 1))) :
    TwInv K q w * Tw K q n w = 1 := TwInvOf_mul_TwOf K q _

/-- **`T_w⁻¹` lies in length `≤ ℓ(w)`** — the Bruhat-free half of the triangularity that
Mathas' 3.9 needs, and the half that the probe measured at 32/32.

What this does **not** say is the Bruhat half: that the support sits inside `[e, w⁻¹]`.
That is measured, not proved, and proving it needs a subword order the corpus does not
have. -/
theorem TwInv_mem_spanLe (w : Perm (Fin (n + 1))) :
    TwInv K q w ∈ spanLe K q (n := n) ((permCoxeterSystem n).length w) := by
  have hlen : (reducedWord n w).length = (permCoxeterSystem n).length w := by
    have hred := reducedWord_isReduced n w
    rw [CoxeterSystem.IsReduced, wordProd_reducedWord] at hred
    exact hred.symm
  have := TwInvOf_mem_spanLe K q (reducedWord n w)
  rwa [hlen] at this

end QOU.BraidKnot.TwInverseLength
