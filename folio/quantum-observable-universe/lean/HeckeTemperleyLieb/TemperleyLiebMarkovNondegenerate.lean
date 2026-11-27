/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import HeckeTemperleyLieb.TemperleyLiebAlgebra
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring

/-!
# Nondegeneracy of a Markov trace on the Temperley–Lieb tower

Let `K` be a field, `δ, ε ∈ K` with `δ ε = 1`, and let `τ_n` be a Markov trace on the tower
`TL_1(δ) ⊂ TL_2(δ) ⊂ ⋯` (`TLFin K δ n`, `n` generators, `n + 1` strands): `τ_0(1) = 1`,
`τ_{n+1}(ι x) = τ_n(x)`, `τ_n(xy) = τ_n(yx)`, `τ_{n+1}(ι(x) e_n) = ε τ_n(x)`.
Write `[k]` for the Chebyshev numbers `[0] = 0`, `[1] = 1`, `[k+2] = δ[k+1] − [k]`
(`qint`; at `δ = q + q⁻¹` these are the balanced quantum integers).

**Theorem** (`nondegenerate_iff`).  The trace form `(x, y) ↦ τ_n(xy)` on `TLFin K δ n` is
nondegenerate **iff `[k] ≠ 0` for every `3 ≤ k ≤ n + 2`.**

This is the classical criterion (Jones 1983; Goodman–de la Harpe–Jones 1989, §2.8; Wenzl
1988).  The proof here is self-contained and purely algebraic.

## Route

* **Jones' lemma** (`sup_eq_top`, `last_mul_eq`): `TL_{n+2} = ι TL_{n+1} + span(ι a · e · ι b)`,
  and `e A e ⊆ ι(A) e` with the coefficient commuting with `e`; hence
  `e_{last} y = e_{last} ι(z)` for every `y` (`exists_last_mul_eq`).
* **Jones–Wenzl projectors** (`jw`): `p_0 = 1`,
  `p_{n+1} = ι p_n − ([n+1]/[n+2]) ι p_n · e_n · ι p_n`.  When `[k] ≠ 0` for `k ≤ n + 1`,
  `p_n` kills every generator on both sides, is idempotent, `1 − p_n` lies in the ideal
  spanned by the generators, and `τ_n(p_n) = [n+2] ε^{n+1}` (`jw_spec`, `tau_jw`).
* **Sufficiency** (`nondegenerate_succ`): if `x` is in the radical at level `n + 1`, then
  `e_{last} x = e_{last} ι z` with `z` in the radical at level `n`, so `e_{last} x = 0`;
  the relations `e_i = e_i e_{i+1} e_i` push this down to every generator; so the ideal
  spanned by generators kills `x`, and `p_{n+1} x = aug(x) p_{n+1}` with
  `τ(p_{n+1}) = [n+3] ε^{n+2} ≠ 0` gives `aug(x) = 0`.  Then `x = (1 − p) x + p x = 0`.
* **Necessity** (`not_nondegenerate`): at the least `k ≥ 3` with `[k] = 0`, the projector
  `p_{k−2}` has trace `0` and kills every generator, so (included into any higher level)
  it lies in the radical (`tau_inclIter_mul`); its augmentation is `1`, so it is nonzero.

No empirical input: everything is over an arbitrary field.

-- Ref: [jones1983]; [wenzl1988]
-/

namespace QOU.MathlibExt.TemperleyLiebMarkov

open QOU.MathlibExt.TemperleyLieb

/-! ## Generic facts about a presented Temperley–Lieb algebra -/

section Generic

variable {R : Type*} [CommRing R] {δ : R} {B : Type*} {Adj : B → B → Prop}

theorem adjoin_e_eq_top : Algebra.adjoin R (Set.range (e R δ Adj)) = ⊤ := by
  have h := congrArg (Subalgebra.map (RingQuot.mkAlgHom R (Rel R δ Adj)))
    (FreeAlgebra.adjoin_range_ι R B)
  rw [AlgHom.map_adjoin, ← Set.range_comp, Algebra.map_top] at h
  rw [show e R δ Adj = (RingQuot.mkAlgHom R (Rel R δ Adj)) ∘ FreeAlgebra.ι R from rfl, h,
    AlgHom.range_eq_top]
  exact RingQuot.mkAlgHom_surjective R _

theorem mem_adjoin_e (t : TemperleyLiebAlgebra R δ Adj) :
    t ∈ Algebra.adjoin R (Set.range (e R δ Adj)) := by
  rw [adjoin_e_eq_top]; exact Algebra.mem_top

/-- A submodule containing `1` and closed under right multiplication by every generator is
everything. -/
theorem submodule_eq_top {S : Submodule R (TemperleyLiebAlgebra R δ Adj)} (h1 : 1 ∈ S)
    (hS : ∀ s ∈ S, ∀ i, s * e R δ Adj i ∈ S) : S = ⊤ := by
  rw [eq_top_iff]
  intro t ht
  clear ht
  have key : ∀ M ∈ S, M * t ∈ S := by
    induction mem_adjoin_e t using Algebra.adjoin_induction with
    | mem y hy => obtain ⟨j, rfl⟩ := hy; exact fun M hM => hS M hM j
    | algebraMap r =>
      intro M hM
      rw [Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]
      exact S.smul_mem _ hM
    | add y z _ _ hy hz => intro M hM; rw [mul_add]; exact S.add_mem (hy M hM) (hz M hM)
    | mul y z _ _ hy hz => intro M hM; rw [← mul_assoc]; exact hz _ (hy M hM)
  simpa using key 1 h1

/-- If `p e_i = 0` for every generator then `p y = aug(y) • p`. -/
theorem mul_eq_aug_smul {p : TemperleyLiebAlgebra R δ Adj} (hp : ∀ i, p * e R δ Adj i = 0)
    (y : TemperleyLiebAlgebra R δ Adj) : p * y = augmentation R δ Adj y • p := by
  induction mem_adjoin_e y using Algebra.adjoin_induction with
  | mem y hy => obtain ⟨j, rfl⟩ := hy; rw [hp, augmentation_e, zero_smul]
  | algebraMap r =>
    rw [AlgHom.commutes, Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]; rfl
  | add y z _ _ hy hz => rw [mul_add, hy, hz, map_add, add_smul]
  | mul y z _ _ hy hz => rw [← mul_assoc, hy, smul_mul_assoc, hz, smul_smul, map_mul]

/-- An algebra map whose values on generators commute with `c` has all values commuting
with `c`. -/
theorem commute_of_gens {A : Type*} [Ring A] [Algebra R A]
    (f : TemperleyLiebAlgebra R δ Adj →ₐ[R] A) (c : A) (h : ∀ i, Commute (f (e R δ Adj i)) c)
    (x : TemperleyLiebAlgebra R δ Adj) : Commute (f x) c := by
  induction mem_adjoin_e x using Algebra.adjoin_induction with
  | mem y hy => obtain ⟨j, rfl⟩ := hy; exact h j
  | algebraMap r => rw [AlgHom.commutes]; exact Algebra.commutes r c
  | add y z _ _ hy hz => rw [map_add]; exact hy.add_left hz
  | mul y z _ _ hy hz => rw [map_mul]; exact hy.mul_left hz

/-- The span of all `a e_i b`. -/
noncomputable def genIdeal (R : Type*) [CommRing R] (δ : R) {B : Type*} (Adj : B → B → Prop) :
    Submodule R (TemperleyLiebAlgebra R δ Adj) :=
  Submodule.span R {y | ∃ a b i, y = a * e R δ Adj i * b}

theorem aug_eq_zero_of_mem_genIdeal {u : TemperleyLiebAlgebra R δ Adj}
    (hu : u ∈ genIdeal R δ Adj) : augmentation R δ Adj u = 0 := by
  induction hu using Submodule.span_induction with
  | mem z hz => obtain ⟨a, b, i, rfl⟩ := hz; simp
  | zero => simp
  | add a b _ _ ha hb => rw [map_add, ha, hb, add_zero]
  | smul r a _ ha => rw [map_smul, ha, smul_zero]

end Generic

/-! ## The tower -/

section Tower

variable {K : Type*} [Field K] (δ : K)

/-- The inclusion `TL_{n+1} → TL_{n+2}`, `e_i ↦ e_i`. -/
noncomputable def incl (n : ℕ) : TLFin K δ n →ₐ[K] TLFin K δ (n + 1) :=
  lift K δ adjFin (fun i => e K δ adjFin (Fin.castSucc i)) (fun _ => e_sq _)
    (fun i j h => e_adjacent (by simpa only [adjFin, Fin.coe_castSucc] using h))
    (fun i j h => e_farCommute (by simpa only [adjFin, Fin.coe_castSucc] using h))

@[simp] theorem incl_e (n : ℕ) (i : Fin n) :
    incl δ n (e K δ adjFin i) = e K δ adjFin (Fin.castSucc i) :=
  lift_e _ _ _ _ _ _ _ i

@[simp] theorem aug_incl (n : ℕ) (x : TLFin K δ n) :
    augmentation K δ adjFin (incl δ n x) = augmentation K δ adjFin x := by
  have : (augmentation K δ (adjFin (n := n + 1))).comp (incl δ n)
      = augmentation K δ adjFin := hom_ext _ _ _ _ _ (fun i => by simp)
  exact AlgHom.congr_fun this x

theorem incl_genIdeal (n : ℕ) {u : TLFin K δ n} (hu : u ∈ genIdeal K δ adjFin) :
    incl δ n u ∈ genIdeal K δ adjFin := by
  induction hu using Submodule.span_induction with
  | mem z hz =>
    obtain ⟨a, b, i, rfl⟩ := hz
    exact Submodule.subset_span ⟨incl δ n a, incl δ n b, Fin.castSucc i, by simp⟩
  | zero => simp
  | add a b _ _ ha hb => rw [map_add]; exact Submodule.add_mem _ ha hb
  | smul r a _ ha => rw [map_smul]; exact Submodule.smul_mem _ _ ha

/-- Everything two levels down commutes with the top generator. -/
theorem incl_incl_commute (n : ℕ) (x : TLFin K δ n) :
    Commute (incl δ (n + 1) (incl δ n x)) (e K δ adjFin (Fin.last (n + 1))) := by
  refine commute_of_gens ((incl δ (n + 1)).comp (incl δ n)) _ (fun i => ?_) x
  rw [AlgHom.comp_apply, incl_e, incl_e]
  refine e_commute_fin ?_
  simp only [Fin.coe_castSucc, Fin.val_last]
  have := i.isLt
  omega

/-- On level `0` everything is a scalar, so it commutes with `e_0`. -/
theorem incl_zero_commute (x : TLFin K δ 0) :
    Commute (incl δ 0 x) (e K δ adjFin (Fin.last 0)) :=
  commute_of_gens (incl δ 0) _ (fun i => i.elim0) x

theorem last_adj (n : ℕ) :
    e K δ adjFin (Fin.last (n + 1)) * e K δ adjFin (Fin.castSucc (Fin.last n))
      * e K δ adjFin (Fin.last (n + 1)) = e K δ adjFin (Fin.last (n + 1)) :=
  e_adjacent_fin (by simp)

theorem e_sq' {n : ℕ} (i : Fin n) :
    e K δ adjFin i * e K δ adjFin i = δ • e K δ adjFin i := by
  rw [e_sq_fin, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]

/-! ### Jones' lemma -/

/-- `span(ι a · e_n · ι b)` inside `TL_{n+2}`. -/
noncomputable def JJ (n : ℕ) : Submodule K (TLFin K δ (n + 1)) :=
  Submodule.span K {y | ∃ a b : TLFin K δ n, y = incl δ n a * e K δ adjFin (Fin.last n) * incl δ n b}

/-- `e ι(b) e = ι(b') e` with `ι b'` commuting with `e`. -/
def HProp (n : ℕ) : Prop :=
  ∀ b : TLFin K δ n, ∃ b' : TLFin K δ n, Commute (incl δ n b') (e K δ adjFin (Fin.last n)) ∧
    e K δ adjFin (Fin.last n) * incl δ n b * e K δ adjFin (Fin.last n)
      = incl δ n b' * e K δ adjFin (Fin.last n)

theorem hProp_zero : HProp δ 0 := by
  intro b
  refine ⟨δ • b, incl_zero_commute δ _, ?_⟩
  rw [(incl_zero_commute δ b).eq.symm, mul_assoc, e_sq', mul_smul_comm, map_smul, smul_mul_assoc]

theorem sup_eq_top (n : ℕ) (hH : HProp δ n) :
    LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n = ⊤ := by
  apply submodule_eq_top
  · exact Submodule.mem_sup_left ⟨1, by simp⟩
  intro s hs i
  obtain ⟨y, hy, z, hz, rfl⟩ := Submodule.mem_sup.mp hs
  obtain ⟨c, rfl⟩ := hy
  clear hs
  rw [add_mul]
  refine Submodule.add_mem _ ?_ ?_
  · -- `ι c · e_i`
    induction i using Fin.lastCases with
    | last => exact Submodule.mem_sup_right (Submodule.subset_span ⟨c, 1, by simp⟩)
    | cast j =>
      exact Submodule.mem_sup_left ⟨c * e K δ adjFin j, by simp⟩
  · induction hz using Submodule.span_induction with
    | mem w hw =>
      obtain ⟨a, b, rfl⟩ := hw
      induction i using Fin.lastCases with
      | last =>
        obtain ⟨b', _, hb'⟩ := hH b
        refine Submodule.mem_sup_right (Submodule.subset_span ⟨a * b', 1, ?_⟩)
        rw [map_mul, map_one, mul_one, mul_assoc, mul_assoc, ← mul_assoc _ (incl δ n b), hb',
          ← mul_assoc]
      | cast j =>
        refine Submodule.mem_sup_right (Submodule.subset_span ⟨a, b * e K δ adjFin j, ?_⟩)
        simp [mul_assoc]
    | zero => rw [zero_mul]; exact Submodule.zero_mem _
    | add a b _ _ ha hb => rw [add_mul]; exact Submodule.add_mem _ ha hb
    | smul r a _ ha => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ ha

theorem hProp_succ (n : ℕ) (hH : HProp δ n) : HProp δ (n + 1) := by
  intro b
  have hb : b ∈ LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n := by
    rw [sup_eq_top δ n hH]; exact Submodule.mem_top
  obtain ⟨y, hy, z, hz, rfl⟩ := Submodule.mem_sup.mp hb
  obtain ⟨c, rfl⟩ := hy
  clear hb
  set g := e K δ adjFin (Fin.last (n + 1))
  -- the property, for elements of `JJ`
  have hJ : ∀ w ∈ JJ δ n, ∃ w' : TLFin K δ n,
      g * incl δ (n + 1) w * g = incl δ (n + 1) (incl δ n w') * g := by
    intro w hw
    induction hw using Submodule.span_induction with
    | mem w hw =>
      obtain ⟨a, b, rfl⟩ := hw
      refine ⟨a * b, ?_⟩
      have ha := (incl_incl_commute δ n a).eq
      have hb := (incl_incl_commute δ n b).eq
      simp only [map_mul, incl_e]
      calc g * (incl δ (n + 1) (incl δ n a) * e K δ adjFin (Fin.castSucc (Fin.last n))
              * incl δ (n + 1) (incl δ n b)) * g
          = incl δ (n + 1) (incl δ n a) * (g * e K δ adjFin (Fin.castSucc (Fin.last n)) * g)
              * incl δ (n + 1) (incl δ n b) := by
            simp only [mul_assoc]; rw [← mul_assoc g, ← ha, mul_assoc, hb]
        _ = incl δ (n + 1) (incl δ n a) * incl δ (n + 1) (incl δ n b) * g := by
            rw [last_adj, mul_assoc, ← hb, ← mul_assoc]
    | zero => exact ⟨0, by simp⟩
    | add a b _ _ ha hb =>
      obtain ⟨a', ha'⟩ := ha; obtain ⟨b', hb'⟩ := hb
      exact ⟨a' + b', by rw [map_add, mul_add, add_mul, ha', hb', map_add, map_add, add_mul]⟩
    | smul r a _ ha =>
      obtain ⟨a', ha'⟩ := ha
      exact ⟨r • a', by rw [map_smul, mul_smul_comm, smul_mul_assoc, ha', map_smul, map_smul,
        smul_mul_assoc]⟩
  obtain ⟨w', hw'⟩ := hJ z hz
  refine ⟨incl δ n (δ • c + w'), incl_incl_commute δ n _, ?_⟩
  simp only [AlgHom.toLinearMap_apply]
  rw [map_add, mul_add, add_mul, hw', ← (incl_incl_commute δ n c).eq, mul_assoc, e_sq',
    mul_smul_comm, map_add, map_add, add_mul, map_smul, map_smul, smul_mul_assoc]

theorem hProp (n : ℕ) : HProp δ n := by
  induction n with
  | zero => exact hProp_zero δ
  | succ n ih => exact hProp_succ δ n ih

/-- **`e_{last} y = e_{last} ι(z)`** for every `y ∈ TL_{n+2}`. -/
theorem exists_last_mul_eq (n : ℕ) (y : TLFin K δ (n + 1)) :
    ∃ z : TLFin K δ n, e K δ adjFin (Fin.last n) * y = e K δ adjFin (Fin.last n) * incl δ n z := by
  have hy : y ∈ LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n := by
    rw [sup_eq_top δ n (hProp δ n)]; exact Submodule.mem_top
  obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hy
  obtain ⟨c, rfl⟩ := hy'
  clear hy
  set g := e K δ adjFin (Fin.last n)
  have hJ : ∀ w ∈ JJ δ n, ∃ w' : TLFin K δ n, g * w = g * incl δ n w' := by
    intro w hw
    induction hw using Submodule.span_induction with
    | mem w hw =>
      obtain ⟨a, b, rfl⟩ := hw
      obtain ⟨a', ha'c, ha'⟩ := hProp δ n a
      refine ⟨a' * b, ?_⟩
      rw [← mul_assoc, ← mul_assoc, ha', ha'c.eq, map_mul, mul_assoc]
    | zero => exact ⟨0, by simp⟩
    | add a b _ _ ha hb =>
      obtain ⟨a', ha'⟩ := ha; obtain ⟨b', hb'⟩ := hb
      exact ⟨a' + b', by rw [mul_add, ha', hb', map_add, mul_add]⟩
    | smul r a _ ha =>
      obtain ⟨a', ha'⟩ := ha
      exact ⟨r • a', by rw [mul_smul_comm, ha', map_smul, mul_smul_comm]⟩
  obtain ⟨w', hw'⟩ := hJ z hz
  exact ⟨c + w', by rw [mul_add, hw', map_add, mul_add]; rfl⟩

/-! ## Chebyshev numbers and Jones–Wenzl projectors -/

/-- The Chebyshev numbers `[0] = 0`, `[1] = 1`, `[k+2] = δ[k+1] − [k]`. -/
def qint : ℕ → K
  | 0 => 0
  | 1 => 1
  | (k + 2) => δ * qint (k + 1) - qint k

@[simp] theorem qint_zero : qint δ 0 = 0 := rfl
@[simp] theorem qint_one : qint δ 1 = 1 := rfl
theorem qint_two : qint δ 2 = δ := by simp [qint]
theorem qint_add_two (k : ℕ) : qint δ (k + 2) = δ * qint δ (k + 1) - qint δ k := rfl

/-- **The Jones–Wenzl projectors** `p_0 = 1`,
`p_{n+1} = ι p_n − ([n+1]/[n+2]) · ι p_n · e_n · ι p_n`. -/
noncomputable def jw : ∀ n : ℕ, TLFin K δ n
  | 0 => 1
  | (n + 1) => incl δ n (jw n) - (qint δ (n + 1) / qint δ (n + 2)) •
      (incl δ n (jw n) * e K δ adjFin (Fin.last n) * incl δ n (jw n))

theorem jw_succ (n : ℕ) : jw δ (n + 1) = incl δ n (jw δ n) - (qint δ (n + 1) / qint δ (n + 2)) •
      (incl δ n (jw δ n) * e K δ adjFin (Fin.last n) * incl δ n (jw δ n)) := rfl

/-- The algebraic properties of `p_n`, together with the recursion identity
`e_n · ι p_n · e_n = ([n+2]/[n+1]) · ι(Q) · e_n` (with `Q = ι p_{n−1}`, or `1` at `n = 0`)
that drives the next step. -/
def JWSpec (n : ℕ) : Prop :=
  (∀ i, jw δ n * e K δ adjFin i = 0) ∧ (∀ i, e K δ adjFin i * jw δ n = 0) ∧
    jw δ n * jw δ n = jw δ n ∧ 1 - jw δ n ∈ genIdeal K δ adjFin ∧
    ∃ Q : TLFin K δ n, Commute (incl δ n Q) (e K δ adjFin (Fin.last n)) ∧ jw δ n * Q = jw δ n ∧
      Q * jw δ n = jw δ n ∧
      e K δ adjFin (Fin.last n) * (incl δ n (jw δ n) * e K δ adjFin (Fin.last n))
        = (qint δ (n + 2) / qint δ (n + 1)) • (incl δ n Q * e K δ adjFin (Fin.last n))

theorem jwSpec_zero : JWSpec δ 0 := by
  refine ⟨fun i => i.elim0, fun i => i.elim0, mul_one _, by simp [jw], 1, by simp, mul_one _,
    one_mul _, ?_⟩
  rw [qint_two, qint_one, div_one, map_one, one_mul, jw, map_one, one_mul, e_sq']

theorem jwSpec_succ (n : ℕ) (h1 : qint δ (n + 1) ≠ 0) (h2 : qint δ (n + 2) ≠ 0)
    (hS : JWSpec δ n) : JWSpec δ (n + 1) := by
  obtain ⟨hr, hl, hidem, hJ, Q, hQc, hPQ, hQP, hkey⟩ := hS
  set P := jw δ n
  set c := qint δ (n + 1) / qint δ (n + 2)
  set μ := qint δ (n + 2) / qint δ (n + 1)
  set g := e K δ adjFin (Fin.last n)
  set ιP := incl δ n P
  have hcμ : c * μ = 1 := by simp only [c, μ]; field_simp
  have hιPP : ιP * ιP = ιP := by rw [← map_mul, hidem]
  have hjw : jw δ (n + 1) = ιP - c • (ιP * g * ιP) := rfl
  -- right action of `g`
  have hjg : jw δ (n + 1) * g = 0 := by
    have : ιP * (g * (ιP * g)) = μ • (ιP * g) := by
      rw [hkey, mul_smul_comm, ← mul_assoc, ← map_mul, hPQ]
    rw [hjw, sub_mul, smul_mul_assoc]
    simp only [mul_assoc]
    rw [this, smul_smul, hcμ, one_smul, sub_self]
  have hgj : g * jw δ (n + 1) = 0 := by
    have : g * (ιP * (g * ιP)) = μ • (g * ιP) := by
      rw [← mul_assoc ιP, ← mul_assoc g, ← mul_assoc g, mul_assoc g ιP g, hkey, smul_mul_assoc,
        hQc.eq, mul_assoc, ← map_mul, hQP]
    rw [hjw, mul_sub, mul_smul_comm]
    simp only [mul_assoc]
    rw [this, smul_smul, hcμ, one_smul, sub_self]
  have hjιP : jw δ (n + 1) * ιP = jw δ (n + 1) := by
    rw [hjw, sub_mul, smul_mul_assoc, hιPP, mul_assoc (ιP * g), hιPP]
  have hιPj : ιP * jw δ (n + 1) = jw δ (n + 1) := by
    rw [hjw, mul_sub, mul_smul_comm, hιPP, ← mul_assoc, ← mul_assoc, hιPP]
  refine ⟨fun i => ?_, fun i => ?_, ?_, ?_, ιP, incl_incl_commute δ n P, hjιP, hιPj, ?_⟩
  · induction i using Fin.lastCases with
    | last => exact hjg
    | cast j =>
      rw [← incl_e, hjw, sub_mul, smul_mul_assoc, ← map_mul, hr, map_zero, mul_assoc,
        ← map_mul, hr, map_zero, mul_zero, smul_zero, sub_zero]
  · induction i using Fin.lastCases with
    | last => exact hgj
    | cast j =>
      rw [← incl_e, hjw, mul_sub, mul_smul_comm, ← map_mul, hl, map_zero, ← mul_assoc,
        ← mul_assoc, ← map_mul, hl, map_zero, zero_mul, zero_mul, smul_zero, sub_zero]
  · nth_rewrite 2 [hjw]
    rw [mul_sub, mul_smul_comm, hjιP, ← mul_assoc, ← mul_assoc, hjιP, hjg, zero_mul, smul_zero,
      sub_zero]
  · have : 1 - jw δ (n + 1) = incl δ n (1 - P) + c • (ιP * g * ιP) := by
      rw [hjw, map_sub, map_one]; abel
    rw [this]
    refine Submodule.add_mem _ (incl_genIdeal δ n hJ) (Submodule.smul_mem _ _ ?_)
    exact Submodule.subset_span ⟨ιP, ιP, Fin.last n, rfl⟩
  · -- the recursion identity one level up
    set g' := e K δ adjFin (Fin.last (n + 1))
    have hc : incl δ (n + 1) ιP * g' = g' * incl δ (n + 1) ιP := (incl_incl_commute δ n P).eq
    have hg : incl δ (n + 1) g = e K δ adjFin (Fin.castSucc (Fin.last n)) := incl_e _ _ _
    have hA : g' * (incl δ (n + 1) ιP * g') = δ • (incl δ (n + 1) ιP * g') := by
      rw [hc, ← mul_assoc, e_sq', smul_mul_assoc]
    have hB : g' * (incl δ (n + 1) (ιP * g * ιP) * g') = incl δ (n + 1) ιP * g' := by
      rw [map_mul, map_mul, hg]
      calc g' * (incl δ (n + 1) ιP * e K δ adjFin (Fin.castSucc (Fin.last n))
              * incl δ (n + 1) ιP * g')
          = incl δ (n + 1) ιP * (g' * e K δ adjFin (Fin.castSucc (Fin.last n)) * g')
              * incl δ (n + 1) ιP := by
            simp only [mul_assoc]; rw [← mul_assoc g', ← hc, mul_assoc, hc]
        _ = incl δ (n + 1) ιP * g' := by
            rw [last_adj, mul_assoc, ← hc, ← mul_assoc, ← map_mul, hιPP]
    have hδc : δ - c = qint δ (n + 3) / qint δ (n + 2) := by
      rw [eq_div_iff h2, sub_mul, show qint δ (n + 3) = δ * qint δ (n + 2) - qint δ (n + 1) from rfl]
      simp only [c]
      rw [div_mul_cancel₀ _ h2]
    simp only [show n + 1 + 2 = n + 3 from rfl, show n + 1 + 1 = n + 2 from rfl]
    rw [jw_succ, map_sub, map_smul, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, hA, hB, ← hδc,
      sub_smul]

/-- Every `jw n` satisfies its specification when `[k] ≠ 0` for `k ≤ n + 1`. -/
theorem jw_spec (n : ℕ) (hg : ∀ k ≤ n, qint δ (k + 1) ≠ 0) : JWSpec δ n := by
  induction n with
  | zero => exact jwSpec_zero δ
  | succ n ih =>
    exact jwSpec_succ δ n (hg n (by omega)) (hg (n + 1) le_rfl) (ih fun k hk => hg k (by omega))

end Tower

/-! ## Markov traces on the tower -/

section Markov

variable {K : Type*} [Field K] (δ ε : K)

/-- **A Markov trace on the Temperley–Lieb tower** with parameter `ε`. -/
structure MarkovTower where
  /-- The trace on each level. -/
  τ : ∀ n, TLFin K δ n →ₗ[K] K
  tr_one : τ 0 1 = 1
  tr_incl : ∀ n x, τ (n + 1) (incl δ n x) = τ n x
  tr_comm : ∀ n x y, τ n (x * y) = τ n (y * x)
  tr_markov : ∀ n x, τ (n + 1) (incl δ n x * e K δ adjFin (Fin.last n)) = ε * τ n x

variable {δ ε} (T : MarkovTower δ ε)

/-- The trace form on level `n` is nondegenerate. -/
def Nondegenerate (n : ℕ) : Prop :=
  ∀ x : TLFin K δ n, (∀ y, T.τ n (x * y) = 0) → x = 0

theorem rad_mul_left {n : ℕ} {x : TLFin K δ n} (hx : ∀ y, T.τ n (x * y) = 0)
    (a : TLFin K δ n) : ∀ y, T.τ n (a * x * y) = 0 := by
  intro y; rw [mul_assoc, T.tr_comm, mul_assoc]; exact hx _

theorem tau_jw (hε : δ * ε = 1) (n : ℕ) (hg : ∀ k ≤ n, qint δ (k + 1) ≠ 0)
    (hS : ∀ m ≤ n, JWSpec δ m) : T.τ n (jw δ n) = qint δ (n + 2) * ε ^ (n + 1) := by
  induction n with
  | zero => rw [jw, T.tr_one, qint_two, zero_add, pow_one, hε]
  | succ n ih =>
    have ih := ih (fun k hk => hg k (by omega)) (fun m hm => hS m (by omega))
    obtain ⟨-, -, hidem, -⟩ := hS n (by omega)
    have h2 : qint δ (n + 2) ≠ 0 := hg (n + 1) le_rfl
    have hc : qint δ (n + 1) / qint δ (n + 2) * qint δ (n + 2) = qint δ (n + 1) :=
      div_mul_cancel₀ _ h2
    simp only [show n + 1 + 2 = n + 3 from rfl, show n + 1 + 1 = n + 2 from rfl]
    rw [jw_succ, map_sub, map_smul, T.tr_incl, T.tr_comm, ← mul_assoc, ← map_mul, hidem,
      T.tr_markov, ih, smul_eq_mul, show qint δ (n + 3) = δ * qint δ (n + 2) - qint δ (n + 1) from rfl]
    linear_combination (-(ε * ε ^ (n + 1))) * hc + (-(qint δ (n + 2) * ε ^ (n + 1))) * hε

theorem nondegenerate_zero : Nondegenerate T 0 := by
  intro x hx
  have h := mul_eq_aug_smul (p := (1 : TLFin K δ 0)) (fun i => i.elim0) x
  rw [one_mul] at h
  have h1 := hx 1
  rw [mul_one, h, map_smul, T.tr_one, smul_eq_mul, mul_one] at h1
  rw [h, h1, zero_smul]

/-- **The inductive step.** -/
theorem nondegenerate_succ (hε : δ * ε = 1) (n : ℕ) (hn : Nondegenerate T n)
    (hg : ∀ k ≤ n + 2, qint δ (k + 1) ≠ 0) : Nondegenerate T (n + 1) := by
  have hε0 : ε ≠ 0 := right_ne_zero_of_mul_eq_one hε
  set g := e K δ adjFin (Fin.last n)
  -- R1: the top generator kills the radical
  have R1 : ∀ x : TLFin K δ (n + 1), (∀ y, T.τ (n + 1) (x * y) = 0) → g * x = 0 := by
    intro x hx
    obtain ⟨z, hz⟩ := exists_last_mul_eq δ n x
    have hzrad : ∀ c, T.τ n (z * c) = 0 := by
      intro c
      have h : ε * T.τ n (z * c) = 0 := by
        rw [← T.tr_markov, map_mul (incl δ n), T.tr_comm, ← mul_assoc, ← hz, mul_assoc,
          T.tr_comm, mul_assoc]
        exact hx _
      exact (mul_eq_zero.mp h).resolve_left hε0
    rw [hz, hn z hzrad, map_zero, mul_zero]
  -- R2: every generator kills the radical
  have R2 : ∀ d, ∀ i : Fin (n + 1), i.val + d = n → ∀ x : TLFin K δ (n + 1),
      (∀ y, T.τ (n + 1) (x * y) = 0) → e K δ adjFin i * x = 0 := by
    intro d
    induction d with
    | zero =>
      intro i hi x hx
      have : i = Fin.last n := Fin.ext (by simp; omega)
      subst this; exact R1 x hx
    | succ d ih =>
      intro i hi x hx
      let j : Fin (n + 1) := ⟨i.val + 1, by omega⟩
      have hadj : e K δ adjFin i * e K δ adjFin j * e K δ adjFin i = e K δ adjFin i :=
        e_adjacent_fin (Or.inl rfl)
      rw [← hadj, mul_assoc, mul_assoc,
        ih j (by simp [j]; omega) _ (rad_mul_left T hx _), mul_zero]
  have R2' : ∀ i : Fin (n + 1), ∀ x : TLFin K δ (n + 1),
      (∀ y, T.τ (n + 1) (x * y) = 0) → e K δ adjFin i * x = 0 :=
    fun i => R2 (n - i.val) i (by omega)
  -- the projector
  have hS := jw_spec δ (n + 1) (fun k hk => hg k (by omega))
  obtain ⟨hr, -, -, hJ, -⟩ := hS
  have htau : T.τ (n + 1) (jw δ (n + 1)) ≠ 0 := by
    rw [tau_jw T hε (n + 1) (fun k hk => hg k (by omega))
      (fun m hm => jw_spec δ m (fun k hk => hg k (by omega)))]
    exact mul_ne_zero (hg (n + 2) le_rfl) (pow_ne_zero _ hε0)
  intro x hx
  -- R3: the generator ideal kills `x`
  have R3 : ∀ u ∈ genIdeal K δ adjFin, u * x = 0 := by
    intro u hu
    induction hu using Submodule.span_induction with
    | mem z hz =>
      obtain ⟨a, b, i, rfl⟩ := hz
      rw [mul_assoc, mul_assoc, R2' i _ (rad_mul_left T hx b), mul_zero]
    | zero => rw [zero_mul]
    | add a b _ _ ha hb => rw [add_mul, ha, hb, add_zero]
    | smul r a _ ha => rw [smul_mul_assoc, ha, smul_zero]
  -- R4: the projector kills `x`
  have R4 : jw δ (n + 1) * x = 0 := by
    have hpx := mul_eq_aug_smul hr x
    have h0 : T.τ (n + 1) (jw δ (n + 1) * x) = 0 := by rw [T.tr_comm]; exact hx _
    rw [hpx, map_smul, smul_eq_mul] at h0
    rw [hpx, (mul_eq_zero.mp h0).resolve_right htau, zero_smul]
  calc x = (1 - jw δ (n + 1)) * x + jw δ (n + 1) * x := by rw [sub_mul, one_mul, sub_add_cancel]
    _ = 0 := by rw [R3 _ hJ, R4, add_zero]

/-- Iterated inclusion `TL_{r+1} → TL_{r+m+1}`. -/
noncomputable def inclIter (r : ℕ) : ∀ m : ℕ, TLFin K δ r →ₐ[K] TLFin K δ (r + m)
  | 0 => AlgHom.id K _
  | (m + 1) => (incl δ (r + m)).comp (inclIter r m)

theorem aug_inclIter (r m : ℕ) (x : TLFin K δ r) :
    augmentation K δ adjFin (inclIter (δ := δ) r m x) = augmentation K δ adjFin x := by
  induction m with
  | zero => rfl
  | succ m ih => exact (aug_incl δ (r + m) _).trans ih

/-- **An element killing every generator, of trace `0`, stays in the radical at every
higher level.** -/
theorem tau_inclIter_mul {r : ℕ} {p : TLFin K δ r} (hp : ∀ i, p * e K δ adjFin i = 0)
    (hτ : T.τ r p = 0) (m : ℕ) (y : TLFin K δ (r + m)) :
    T.τ (r + m) (inclIter (δ := δ) r m p * y) = 0 := by
  induction m with
  | zero =>
    show T.τ r (p * y) = 0
    rw [mul_eq_aug_smul hp, map_smul, hτ, smul_zero]
  | succ m ih =>
    set X := inclIter (δ := δ) r m p
    show T.τ (r + m + 1) (incl δ (r + m) X * y) = 0
    have hy : y ∈ LinearMap.range (incl δ (r + m)).toLinearMap ⊔ JJ δ (r + m) := by
      rw [sup_eq_top δ _ (hProp δ _)]; exact Submodule.mem_top
    obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hy
    obtain ⟨c, rfl⟩ := hy'
    clear hy
    rw [mul_add, map_add]
    have h1 : T.τ (r + m + 1) (incl δ (r + m) X * incl δ (r + m) c) = 0 := by
      rw [← map_mul, T.tr_incl]; exact ih c
    simp only [AlgHom.toLinearMap_apply]
    rw [h1, zero_add]
    induction hz using Submodule.span_induction with
    | mem w hw =>
      obtain ⟨a, b, rfl⟩ := hw
      rw [← mul_assoc, ← mul_assoc, ← map_mul, T.tr_comm, ← mul_assoc, ← map_mul,
        T.tr_markov, T.tr_comm, mul_assoc, ih, mul_zero]
    | zero => rw [mul_zero, map_zero]
    | add a b _ _ ha hb => rw [mul_add, map_add, ha, hb, add_zero]
    | smul r' a _ ha => rw [mul_smul_comm, map_smul, ha, smul_zero]

/-- **Necessity.** -/
theorem not_nondegenerate (hε : δ * ε = 1) (n : ℕ)
    (h : ∃ k, 3 ≤ k ∧ k ≤ n + 2 ∧ qint δ k = 0) : ¬ Nondegenerate T n := by
  classical
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  let k₀ := Nat.find h
  obtain ⟨hk3, hkn, hk0⟩ := Nat.find_spec h
  have hmin : ∀ k < k₀, ¬ (3 ≤ k ∧ k ≤ n + 2 ∧ qint δ k = 0) := fun k hk => Nat.find_min h hk
  obtain ⟨r, hr⟩ : ∃ r, k₀ = r + 2 := ⟨k₀ - 2, by omega⟩
  have hg : ∀ k ≤ r, qint δ (k + 1) ≠ 0 := by
    intro k hk
    rcases Nat.lt_or_ge k 2 with h2 | h2
    · interval_cases k
      · simp
      · rw [qint_two]; exact hδ
    · intro h0
      exact hmin (k + 1) (by omega) ⟨by omega, by omega, h0⟩
  obtain ⟨hr0, -, -, hJ, -⟩ := jw_spec δ r hg
  have hτ : T.τ r (jw δ r) = 0 := by
    rw [tau_jw T hε r hg (fun m hm => jw_spec δ m fun k hk => hg k (by omega)), ← hr, hk0,
      zero_mul]
  obtain ⟨m, rfl⟩ : ∃ m, n = r + m := ⟨n - r, by omega⟩
  intro hnd
  have hX := hnd _ (tau_inclIter_mul T hr0 hτ m)
  have haug := congrArg (augmentation K δ adjFin) hX
  rw [aug_inclIter, map_zero] at haug
  have h1 := aug_eq_zero_of_mem_genIdeal hJ
  rw [map_sub, map_one, haug, sub_zero] at h1
  exact one_ne_zero h1

/-- **The nondegeneracy criterion.**  For a Markov trace with `δ ε = 1`, the trace form on
`TL_{n+1}(δ)` is nondegenerate iff `[k] ≠ 0` for `3 ≤ k ≤ n + 2`. -/
theorem nondegenerate_iff (hε : δ * ε = 1) (n : ℕ) :
    Nondegenerate T n ↔ ∀ k, 3 ≤ k → k ≤ n + 2 → qint δ k ≠ 0 := by
  constructor
  · intro hnd k hk3 hkn hk0
    exact not_nondegenerate T hε n ⟨k, hk3, hkn, hk0⟩ hnd
  · intro hq
    have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
    induction n with
    | zero => exact nondegenerate_zero T
    | succ n ih =>
      refine nondegenerate_succ T hε n (ih fun k h3 hk => hq k h3 (by omega)) fun k hk => ?_
      rcases Nat.lt_or_ge k 2 with h2 | h2
      · interval_cases k
        · simp
        · rw [qint_two]; exact hδ
      · exact hq (k + 1) (by omega) (by omega)

end Markov

end QOU.MathlibExt.TemperleyLiebMarkov

