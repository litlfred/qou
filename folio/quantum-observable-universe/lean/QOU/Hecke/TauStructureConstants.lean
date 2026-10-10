import QOU.Hecke.TauSymmetrizing

/-!
# QOU.Hecke.TauStructureConstants — `τ(T_v T_w) = δ_{w,v⁻¹} q^{ℓ(v)}`

The hypothesis that `QOU.Hecke.TauSymmetrizing` carried, discharged.  With it
the Gram determinant of the canonical trace becomes unconditional, and `H_n(q)`
is a symmetric Frobenius algebra at every `q ≠ 0`.

`Ref: [geckpfeiffer2000]` §8.1.  The citation is attribution — Geck and Pfeiffer
proved this; what follows is a Lean proof of their statement.

## The induction is on `ℓ(v)` alone, and that matters

8.1.1 is usually run on `ℓ(v) + ℓ(w)`, choosing a simple reflection that is a
descent of *both* factors.  Producing such a common descent needs the exchange
condition, and **Mathlib has no exchange condition** — measured, there is no
occurrence of `xchange` anywhere in `Mathlib/GroupTheory/Coxeter/`.

It is not needed.  Induct on `ℓ(v)`, take *any* left descent `i` of `v`
(`CoxeterSystem.exists_leftDescent_of_ne_one`), and split on whether `i` happens
to be a right descent of `w`.  Both branches close because of one observation:

> a left descent of `v` and a right descent of `w` at the **same** `i` are
> contradictory once `w` is pinned to `v⁻¹` or to `v⁻¹ s_i`, since
> `ℓ(s_i v) = ℓ(v⁻¹ s_i)` (`CoxeterSystem.length_inv`).

In the ascent branch that kills the only surviving delta, so both sides vanish;
in the descent branch it kills the `(q-1)` term, leaving exactly `q` times the
inductive value.  The `(q-1)` term never contributes at all — which is precisely
why no common descent is required.

## Handedness

This corpus's `T_a · T_b = T_{ba}` (see `QOU.Hecke.TwMul`; it is a fact about
the orbit representation, not a typo), so the decompositions read
`T_v = T_{s v} · T_s` at a left descent and `T_w = T_s · T_{w s}` at a right
one.  Both are `Tw_mul_Tw` under the length hypothesis the descent supplies.

## What is proved

* `permCoxeterSystem_simple` / `Tw_simple` — the bridges to `σ` and to the
  concrete transposition.
* `Tw_simple_mul_self` — `T_s² = (q-1) T_s + q`, the `v = s` case of `σ_mul_Tw`.
* three decomposition lemmas at a descent / an ascent.
* `tau_Tw_mul_Tw` — **the identity**.
* `tauGram_det` / `tauGram_det_ne_zero` — the conditional results of
  `TauSymmetrizing`, now unconditional.

## What this still does NOT give

`det(τ-Gram) ≠ 0` for every `q ≠ 0` is **not** semisimplicity, which fails at
roots of unity.  It is Frobenius-ness.  The Schur-element criterion needs, in
addition, that `τ`'s Wedderburn weights are `1/s_λ`; that identification is
where `q` enters and is not here.  `SchurElementCriterion` remains a cited class
with no instance.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.SymmetricCoxeter
open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-! ### Bridges -/

/-- Mathlib's abstract simple reflection is this corpus's adjacent
    transposition. -/
theorem permCoxeterSystem_simple (i : Fin n) :
    (permCoxeterSystem n).simple i = s n i := by
  rw [CoxeterSystem.simple]
  exact toPerm_simple n i

/-- `T_{s_i} = σ_i`: the basis element at a simple reflection is the generator. -/
theorem Tw_simple (i : Fin n) : Tw K q n (s n i) = σ K q n i := by
  refine orbitMap_injective K q n ?_
  rw [orbitMap_Tw, orbitMap_apply, toEnd_σ, Rs_single_perm]
  simp [s]

/-- **The quadratic relation on the basis**: `T_s² = (q-1) T_s + q`.

    This is `σ_mul_Tw` at `v = s_i`, which lands in the *down* case because
    `s_i` inverts the pair `(i, i+1)` by construction. -/
theorem Tw_simple_mul_self (i : Fin n) :
    Tw K q n (s n i) * Tw K q n (s n i)
      = (q - 1) • Tw K q n (s n i) + q • (1 : QOU.Hecke.IwahoriHecke K q n) := by
  have hnot : ¬ (s n i) i.castSucc < (s n i) i.succ := by
    simp only [s, Equiv.swap_apply_left, Equiv.swap_apply_right]
    exact not_lt.mpr (le_of_lt (Fin.castSucc_lt_succ i))
  have hcancel : s n i * Equiv.swap i.castSucc i.succ = 1 := s_mul_self n i
  nth_rewrite 1 [Tw_simple K q n i]
  rw [σ_mul_Tw, if_neg hnot, hcancel, Tw_one]

/-! ### Descent decompositions -/

/-- **At a left descent, `T_v = T_{s v} · T_s`.** -/
theorem Tw_mul_simple_of_isLeftDescent (v : Equiv.Perm (Fin (n + 1))) (i : Fin n)
    (h : (permCoxeterSystem n).IsLeftDescent v i) :
    Tw K q n ((permCoxeterSystem n).simple i * v)
        * Tw K q n ((permCoxeterSystem n).simple i)
      = Tw K q n v := by
  have hlen : (permCoxeterSystem n).length v
      = (permCoxeterSystem n).length ((permCoxeterSystem n).simple i)
        + (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v) := by
    have hd := ((permCoxeterSystem n).isLeftDescent_iff).mp h
    rw [(permCoxeterSystem n).length_simple]
    omega
  have hmul : (permCoxeterSystem n).simple i
      * ((permCoxeterSystem n).simple i * v) = v := by
    rw [← mul_assoc, CoxeterSystem.simple_mul_simple_self, one_mul]
  have := Tw_mul_Tw K q n ((permCoxeterSystem n).simple i * v)
    ((permCoxeterSystem n).simple i) (by rw [hmul]; exact hlen)
  rwa [hmul] at this

/-- **At an ascent, `T_s · T_w = T_{w s}`.** -/
theorem Tw_simple_mul_of_not_isRightDescent (w : Equiv.Perm (Fin (n + 1))) (i : Fin n)
    (h : ¬ (permCoxeterSystem n).IsRightDescent w i) :
    Tw K q n ((permCoxeterSystem n).simple i) * Tw K q n w
      = Tw K q n (w * (permCoxeterSystem n).simple i) :=
  Tw_mul_Tw K q n ((permCoxeterSystem n).simple i) w
    (by rw [(permCoxeterSystem n).length_simple,
      ((permCoxeterSystem n).not_isRightDescent_iff).mp h])

/-- **At a right descent, `T_w = T_s · T_{w s}`.** -/
theorem Tw_simple_mul_of_isRightDescent (w : Equiv.Perm (Fin (n + 1))) (i : Fin n)
    (h : (permCoxeterSystem n).IsRightDescent w i) :
    Tw K q n ((permCoxeterSystem n).simple i) * Tw K q n (w * (permCoxeterSystem n).simple i)
      = Tw K q n w := by
  have hmul : w * (permCoxeterSystem n).simple i * (permCoxeterSystem n).simple i = w := by
    rw [mul_assoc, CoxeterSystem.simple_mul_simple_self, mul_one]
  have hlen : (permCoxeterSystem n).length
        (w * (permCoxeterSystem n).simple i * (permCoxeterSystem n).simple i)
      = (permCoxeterSystem n).length (w * (permCoxeterSystem n).simple i)
        + (permCoxeterSystem n).length ((permCoxeterSystem n).simple i) := by
    rw [hmul, (permCoxeterSystem n).length_simple,
      ← ((permCoxeterSystem n).isRightDescent_iff).mp h]
  have := Tw_mul_Tw K q n ((permCoxeterSystem n).simple i)
    (w * (permCoxeterSystem n).simple i) hlen
  rwa [hmul] at this

/-- `T_s² = (q-1) T_s + q`, phrased at Mathlib's simple reflection. -/
theorem Tw_simple'_mul_self (i : Fin n) :
    Tw K q n ((permCoxeterSystem n).simple i) * Tw K q n ((permCoxeterSystem n).simple i)
      = (q - 1) • Tw K q n ((permCoxeterSystem n).simple i)
          + q • (1 : QOU.Hecke.IwahoriHecke K q n) := by
  rw [permCoxeterSystem_simple]; exact Tw_simple_mul_self K q n i

/-! ### The identity -/

private theorem tau_Tw_mul_Tw_aux :
    ∀ (k : ℕ) (v w : Equiv.Perm (Fin (n + 1))),
      (permCoxeterSystem n).length v = k →
      tau K q n (Tw K q n v * Tw K q n w)
        = if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0 := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    intro v w hk
    by_cases hv : v = 1
    · subst hv
      rw [Tw_one, one_mul, tau_Tw]
      simp
    · obtain ⟨i, hi⟩ := (permCoxeterSystem n).exists_leftDescent_of_ne_one hv
      have hss : (permCoxeterSystem n).simple i * (permCoxeterSystem n).simple i = 1 :=
        CoxeterSystem.simple_mul_simple_self _ _
      have hsinv : ((permCoxeterSystem n).simple i)⁻¹ = (permCoxeterSystem n).simple i :=
        inv_eq_of_mul_eq_one_right hss
      have hlen' : (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v) + 1
          = (permCoxeterSystem n).length v :=
        ((permCoxeterSystem n).isLeftDescent_iff).mp hi
      have hdecomp : Tw K q n ((permCoxeterSystem n).simple i * v)
          * Tw K q n ((permCoxeterSystem n).simple i) = Tw K q n v :=
        Tw_mul_simple_of_isLeftDescent K q n v i hi
      have hinv : ((permCoxeterSystem n).simple i * v)⁻¹
          = v⁻¹ * (permCoxeterSystem n).simple i := by
        rw [mul_inv_rev, hsinv]
      by_cases hd : (permCoxeterSystem n).IsRightDescent w i
      · -- descent branch: the (q-1) term drops, q times the inductive value survives
        have hdesc := Tw_simple_mul_of_isRightDescent K q n w i hd
        have hsw : Tw K q n ((permCoxeterSystem n).simple i) * Tw K q n w
            = (q - 1) • Tw K q n w
                + q • Tw K q n (w * (permCoxeterSystem n).simple i) := by
          conv_lhs => rw [← hdesc]
          rw [← mul_assoc, Tw_simple'_mul_self, add_mul, smul_mul_assoc, smul_mul_assoc,
            one_mul, hdesc]
        have hexp : Tw K q n v * Tw K q n w
            = (q - 1) • (Tw K q n ((permCoxeterSystem n).simple i * v) * Tw K q n w)
                + q • (Tw K q n ((permCoxeterSystem n).simple i * v)
                        * Tw K q n (w * (permCoxeterSystem n).simple i)) := by
          conv_lhs => rw [← hdecomp]
          rw [mul_assoc, hsw, mul_add, mul_smul_comm, mul_smul_comm]
        have hlt : (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v) < k := by
          omega
        rw [hexp, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul,
          ih _ hlt _ w rfl, ih _ hlt _ (w * (permCoxeterSystem n).simple i) rfl]
        have hfalse : w ≠ ((permCoxeterSystem n).simple i * v)⁻¹ := by
          intro he
          have h1 : (permCoxeterSystem n).length w
              = (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v) := by
            rw [he, CoxeterSystem.length_inv]
          have h3 : w * (permCoxeterSystem n).simple i = v⁻¹ := by
            rw [he, hinv, mul_assoc, hss, mul_one]
          have h2 : (permCoxeterSystem n).length (w * (permCoxeterSystem n).simple i)
              < (permCoxeterSystem n).length w := hd
          rw [h3, CoxeterSystem.length_inv] at h2
          omega
        have hiff : (w * (permCoxeterSystem n).simple i
            = ((permCoxeterSystem n).simple i * v)⁻¹) ↔ (w = v⁻¹) := by
          rw [hinv]; exact mul_left_inj _
        rw [if_neg hfalse, mul_zero, zero_add]
        by_cases hc : w = v⁻¹
        · rw [if_pos (hiff.mpr hc), if_pos hc, ← hlen', pow_succ]
          ring
        · rw [if_neg (fun hx => hc (hiff.mp hx)), if_neg hc, mul_zero]
      · -- ascent branch: the surviving delta is impossible, so both sides vanish
        have hasc := Tw_simple_mul_of_not_isRightDescent K q n w i hd
        have hexp : Tw K q n v * Tw K q n w
            = Tw K q n ((permCoxeterSystem n).simple i * v)
                * Tw K q n (w * (permCoxeterSystem n).simple i) := by
          conv_lhs => rw [← hdecomp]
          rw [mul_assoc, hasc]
        have hlt : (permCoxeterSystem n).length ((permCoxeterSystem n).simple i * v) < k := by
          omega
        rw [hexp, ih _ hlt _ (w * (permCoxeterSystem n).simple i) rfl]
        have hne : w ≠ v⁻¹ := by
          intro he
          exact hd (he ▸ ((permCoxeterSystem n).isRightDescent_inv_iff).mpr hi)
        have hiff : (w * (permCoxeterSystem n).simple i
            = ((permCoxeterSystem n).simple i * v)⁻¹) ↔ (w = v⁻¹) := by
          rw [hinv]; exact mul_left_inj _
        rw [if_neg (fun hx => hne (hiff.mp hx)), if_neg hne]

/-- **`τ(T_v · T_w) = δ_{w, v⁻¹} · q^{ℓ(v)}`** — Geck–Pfeiffer §8.1.

    `Ref: [geckpfeiffer2000]`.  Proved by induction on `ℓ(v)` with an arbitrary
    left descent; no exchange condition is used.  See the module docstring. -/
theorem tau_Tw_mul_Tw (v w : Equiv.Perm (Fin (n + 1))) :
    tau K q n (Tw K q n v * Tw K q n w)
      = if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0 :=
  tau_Tw_mul_Tw_aux K q n _ v w rfl

/-! ### The Gram determinant, now unconditional -/

/-- **`det` of the `τ`-Gram matrix**, with no hypothesis. -/
theorem tauGram_det :
    (tauGram K q n).det
      = (Equiv.Perm.sign (Equiv.inv (Equiv.Perm (Fin (n + 1)))) : K)
          * ∏ v : Equiv.Perm (Fin (n + 1)), q ^ (permCoxeterSystem n).length v :=
  tauGram_det_of_structure_constants K q n (tau_Tw_mul_Tw K q n)

/-- **`H_n(q)` is a symmetric Frobenius algebra for every `q ≠ 0`.**

    Not semisimplicity — that fails at roots of unity.  See the module
    docstring. -/
theorem tauGram_det_ne_zero (hq : q ≠ 0) : (tauGram K q n).det ≠ 0 :=
  tauGram_det_ne_zero_of_structure_constants K q n hq (tau_Tw_mul_Tw K q n)

/-! ### `τ` is a trace

Immediate from the identity, and not available before it: swapping `v` and `w`
in `δ_{w,v⁻¹} q^{ℓ(v)}` gives `δ_{v,w⁻¹} q^{ℓ(w)}`, and those agree because
`w = v⁻¹ ↔ v = w⁻¹` and `ℓ(v⁻¹) = ℓ(v)`.  This is what makes `τ` a *symmetrizing*
trace rather than merely a linear functional, and it is what makes the block
weights of a Wedderburn decomposition well defined. -/

/-- **`τ(x y) = τ(y x)`.** -/
theorem tau_mul_comm (x y : QOU.Hecke.IwahoriHecke K q n) :
    tau K q n (x * y) = tau K q n (y * x) := by
  have key : (LinearMap.compr₂ (LinearMap.mul K (QOU.Hecke.IwahoriHecke K q n)) (tau K q n))
      = (LinearMap.compr₂ (LinearMap.mul K (QOU.Hecke.IwahoriHecke K q n))
          (tau K q n)).flip := by
    refine LinearMap.ext_basis (basisTwOfField K q n) (basisTwOfField K q n) ?_
    intro v w
    simp only [coe_basisTwOfField, LinearMap.compr₂_apply, LinearMap.mul_apply',
      LinearMap.flip_apply]
    rw [tau_Tw_mul_Tw, tau_Tw_mul_Tw]
    by_cases h : w = v⁻¹
    · subst h
      simp [CoxeterSystem.length_inv]
    · rw [if_neg h, if_neg (fun hc => h (by rw [hc, inv_inv]))]
  have := congrFun (congrArg DFunLike.coe (congrArg (fun B => B x) key)) y
  simpa using this

/-- The Gram matrix of `τ` is symmetric — the matrix form of `tau_mul_comm`. -/
theorem tauGram_symm (v w : Equiv.Perm (Fin (n + 1))) :
    tauGram K q n v w = tauGram K q n w v := by
  rw [tauGram_apply, tauGram_apply, tau_mul_comm]

end QOU.Hecke.TwBasis
