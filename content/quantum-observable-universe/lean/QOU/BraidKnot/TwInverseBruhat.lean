import QOU.BraidKnot.TwInverseLength
import QOU.Machinery.CoxeterBruhat

/-!
# `T_w⁻¹` lives in the Bruhat interval `[e, w⁻¹]`

`TwInverseLength.TwInv_mem_spanLe` bounds `T_w⁻¹` in *length*.  The sharper fact —
measured exactly over `S_2`, `S_3`, `S_4` in
[`tw_inverse_support_probe.py`](../../../../../computations/hecke/tw_inverse_support_probe.py)
at 32/32 — is that its support is the **Bruhat interval `[e, w⁻¹]`**.  This file proves it.

## Note the `w⁻¹`, because the naive statement is false

Against `w` rather than `w⁻¹` the claim holds on **16 of the 32** elements measured, which
are exactly the 16 involutions — the elements where the two agree.  `Tw_mul_Tw`'s flipped
handedness is the cause, the same flip that forced `sortPerm`'s orientation and
`IsDistinguishedL`.  Stating this against `w` would be a false lemma.

## What the induction needs, and what it does not

Only the two ascending-extension steps of `CoxeterBruhat` — `u ≤ t ⇒ u ≤ t·sᵢ` and
`u ≤ t ⇒ u·sᵢ ≤ t·sᵢ` — together with the corpus's own `σ_mul_Tw`, which puts
`σᵢ · T_u` in the span of `T_u` and `T_{u·sᵢ}` in both branches.

It needs **neither transitivity, nor antisymmetry, nor the subword property**, all of
which `CoxeterBruhat` leaves open pending the exchange condition.  That is worth stating
plainly: this theorem does not silently depend on `BruhatLe` being a partial order, which
is not yet known here.

The length hypothesis comes free from reducedness: `wordProd (i :: ω) = sᵢ · v`, so
reducedness of `i :: ω` gives `ℓ(sᵢv) = ℓ(v) + 1`, and inverting — `ℓ` is
inverse-invariant — gives exactly `ℓ(v⁻¹·sᵢ) = ℓ(v⁻¹) + 1`, which is the hypothesis both
extension lemmas want.
-/

namespace QOU.BraidKnot.TwInverseBruhat

open QOU.Hecke.TwBasis QOU.Hecke.IwahoriHecke QOU.Hecke.SymmetricCoxeter Equiv
open QOU.BraidKnot.HeckeMurphy QOU.BraidKnot.TwInverseLength
open QOU.Machinery.CoxeterBruhat

variable (K : Type*) [Field K] (q : K) {n : ℕ}

/-- **`span {T_v : v ≤ w}`** — the Bruhat filtration. -/
noncomputable def spanBruhatLe (w : Perm (Fin (n + 1))) :
    Submodule K (QOU.Hecke.IwahoriHecke K q n) :=
  Submodule.span K
    {x | ∃ v : Perm (Fin (n + 1)), BruhatLe (permCoxeterSystem n) v w ∧ x = Tw K q n v}

theorem Tw_mem_spanBruhatLe {v w : Perm (Fin (n + 1))}
    (h : BruhatLe (permCoxeterSystem n) v w) : Tw K q n v ∈ spanBruhatLe K q w :=
  Submodule.subset_span ⟨v, h, rfl⟩

theorem one_mem_spanBruhatLe (w : Perm (Fin (n + 1))) :
    (1 : QOU.Hecke.IwahoriHecke K q n) ∈ spanBruhatLe K q w := by
  have := Tw_mem_spanBruhatLe K q (one_bruhatLe (permCoxeterSystem n) w)
  rwa [Tw_one] at this

/-- Ascending one simple reflection only widens the interval. -/
theorem spanBruhatLe_mono_simple {t : Perm (Fin (n + 1))} (i : Fin n)
    (hlen : (permCoxeterSystem n).length (t * (permCoxeterSystem n).simple i)
              = (permCoxeterSystem n).length t + 1) :
    spanBruhatLe K q t ≤ spanBruhatLe K q (t * (permCoxeterSystem n).simple i) := by
  refine Submodule.span_mono ?_
  rintro x ⟨v, hv, rfl⟩
  exact ⟨v, bruhatLe_mul_simple (permCoxeterSystem n) i hv hlen, rfl⟩

/-- **The filtration step.**  `σᵢ` moves `[e, t]` into `[e, t·sᵢ]`, using both extension
lemmas — one per branch of `σ_mul_Tw`. -/
theorem σ_mul_mem_spanBruhatLe {t : Perm (Fin (n + 1))}
    {x : QOU.Hecke.IwahoriHecke K q n} (i : Fin n)
    (hlen : (permCoxeterSystem n).length (t * (permCoxeterSystem n).simple i)
              = (permCoxeterSystem n).length t + 1)
    (hx : x ∈ spanBruhatLe K q t) :
    σ K q n i * x ∈ spanBruhatLe K q (t * (permCoxeterSystem n).simple i) := by
  induction hx using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨v, hv, rfl⟩ := hy
      have hup : BruhatLe (permCoxeterSystem n) v (t * (permCoxeterSystem n).simple i) :=
        bruhatLe_mul_simple (permCoxeterSystem n) i hv hlen
      have hside : BruhatLe (permCoxeterSystem n) (v * sw i)
          (t * (permCoxeterSystem n).simple i) := by
        have := bruhatLe_mul_simple_mul_simple (permCoxeterSystem n) i hv hlen
        rwa [simple_eq_sw] at this
      rw [σ_mul_Tw]
      by_cases h : v i.castSucc < v i.succ
      · rw [if_pos h]; exact Tw_mem_spanBruhatLe K q hside
      · rw [if_neg h]
        exact add_mem
          (Submodule.smul_mem _ _ (Tw_mem_spanBruhatLe K q hup))
          (Submodule.smul_mem _ _ (Tw_mem_spanBruhatLe K q hside))
  | zero => simp only [mul_zero]; exact Submodule.zero_mem _
  | add a b _ _ ha hb => rw [mul_add]; exact add_mem ha hb
  | smul c a _ ha => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ ha

variable [Invertible q]

theorem σInv_mul_mem_spanBruhatLe {t : Perm (Fin (n + 1))}
    {x : QOU.Hecke.IwahoriHecke K q n} (i : Fin n)
    (hlen : (permCoxeterSystem n).length (t * (permCoxeterSystem n).simple i)
              = (permCoxeterSystem n).length t + 1)
    (hx : x ∈ spanBruhatLe K q t) :
    σInv K q n i * x ∈ spanBruhatLe K q (t * (permCoxeterSystem n).simple i) := by
  have hstep : σInv K q n i * x = ⅟q • (σ K q n i * x) - (⅟q * (q - 1)) • x := by
    rw [σInv, smul_mul_assoc, sub_mul, smul_mul_assoc, one_mul, smul_sub, smul_smul]
  rw [hstep]
  exact sub_mem
    (Submodule.smul_mem _ _ (σ_mul_mem_spanBruhatLe K q i hlen hx))
    (Submodule.smul_mem _ _ (spanBruhatLe_mono_simple K q i hlen hx))

/-- **The interval bound, along a reduced word.** -/
theorem TwInvOf_mem_spanBruhatLe (ω : List (Fin n))
    (hred : (permCoxeterSystem n).IsReduced ω) :
    TwInvOf K q ω ∈ spanBruhatLe K q ((permCoxeterSystem n).wordProd ω)⁻¹ := by
  induction ω with
  | nil =>
      rw [TwInvOf_nil]
      exact one_mem_spanBruhatLe K q _
  | cons i ω ih =>
      have hredω : (permCoxeterSystem n).IsReduced ω := by
        simpa using hred.drop 1
      set v := (permCoxeterSystem n).wordProd ω with hv
      -- `wordProd (i :: ω) = sᵢ · v`, so its inverse is `v⁻¹ · sᵢ`
      have hprod : (permCoxeterSystem n).wordProd (i :: ω)
          = (permCoxeterSystem n).simple i * v := by
        rw [hv, (permCoxeterSystem n).wordProd_cons]
      have hsimp : ((permCoxeterSystem n).simple i)⁻¹ = (permCoxeterSystem n).simple i :=
        inv_eq_of_mul_eq_one_right ((permCoxeterSystem n).simple_mul_simple_self i)
      have hinv : ((permCoxeterSystem n).wordProd (i :: ω))⁻¹
          = v⁻¹ * (permCoxeterSystem n).simple i := by
        rw [hprod, mul_inv_rev, hsimp]
      -- reducedness of `i :: ω` is exactly the ascending hypothesis, after inverting
      have hlenC : (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v)
          = (permCoxeterSystem n).length v + 1 := by
        have h1 : (permCoxeterSystem n).length
            ((permCoxeterSystem n).wordProd (i :: ω)) = (i :: ω).length := hred
        have h2 : (permCoxeterSystem n).length v = ω.length := hredω
        rw [← hprod, h1, List.length_cons, h2]
      have hlen : (permCoxeterSystem n).length (v⁻¹ * (permCoxeterSystem n).simple i)
          = (permCoxeterSystem n).length v⁻¹ + 1 := by
        have e1 := (permCoxeterSystem n).length_inv (v⁻¹ * (permCoxeterSystem n).simple i)
        have e2 := (permCoxeterSystem n).length_inv v
        rw [mul_inv_rev, hsimp, inv_inv] at e1
        omega
      rw [TwInvOf_cons, hinv]
      exact σInv_mul_mem_spanBruhatLe K q i hlen (ih hredω)

/-- **`T_w⁻¹ ∈ span {T_v : v ≤ w⁻¹}`** — the interval bound the probe measured at 32/32,
and the sharp form of the triangularity Mathas' Lemma 3.9 needs.

Note `w⁻¹`: against `w` the statement is **false**, holding only on involutions. -/
theorem TwInv_mem_spanBruhatLe (w : Perm (Fin (n + 1))) :
    TwInv K q w ∈ spanBruhatLe K q w⁻¹ := by
  have h := TwInvOf_mem_spanBruhatLe K q (reducedWord n w) (reducedWord_isReduced n w)
  rwa [wordProd_reducedWord] at h

end QOU.BraidKnot.TwInverseBruhat
