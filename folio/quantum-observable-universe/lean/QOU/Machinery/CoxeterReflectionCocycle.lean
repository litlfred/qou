/-
# The reflection cocycle and the strong exchange property — `RightExchangeProp` proved

This file closes the audited Mathlib gap recorded in
`QOU.Machinery.CoxeterParabolicCoset`: the exchange property of Coxeter
systems (Bjorner–Brenti Thm 1.4.3; Bourbaki Lie IV §1) is PROVED here,
sorry-free, at every rank, by the classical reflection-cocycle
construction:

* **`cocyclePerm`** — for each generator `i`, the involution of
  `W × ℤ/2` given by `(w, ε) ↦ (σᵢ w σᵢ, ε + [w = σᵢ])`.
* **`cocycleWord_apply`** — the master formula: the composite over a word
  `ω` sends `(t, ε)` to `(π ω · t · (π ω)⁻¹, ε + parity of the number of
  occurrences of `t` in the right inversion sequence of `ω`)`.
* **`cocyclePerm_liftable`** — the braid-relation check
  `(fᵢ fⱼ)^{M i j} = 1`: the word is `alternatingWord i j (2m)`, its
  inversion-sequence entries are `π (alternatingWord _ _ (2k+1))`
  (Mathlib's `getElem_leftInvSeq_alternatingWord`), and the entries have
  period `m` by `simple_mul_simple_pow'` — so the inversion sequence is
  `T ++ T` and every ℤ/2 parity count vanishes. No parity case split.
* **`eta`** — the cocycle `η(w, t)`, well-defined on `W` via
  `CoxeterSystem.lift` (the presentation universal property); the cocycle
  law `η(uv, t) = η(v, t) + η(u, v t v⁻¹)` and `η(t, t) = 1` for every
  reflection `t` (three-line cocycle algebra, no induction).
* **`eta_eq_one_of_isRightInversion`** — `ℓ(w t) < ℓ(w) → η(w, t) = 1`,
  by the self-inverse trick: `η(wt, t) = 1 + η(w, t)`, so `η(w, t) = 0`
  would delete a letter from a reduced word of `w t` and force
  `ℓ(w) < ℓ(w t)`, a contradiction.
* **`strong_exchange`** — for ANY word `ω` and any right inversion `t` of
  `π ω`: some single letter of `ω` can be deleted, `π ω · t = π (ω − 1
  letter)`. (Strong: `t` ranges over all reflections, `ω` need not be
  reduced.)
* **`rightExchange : RightExchangeProp cs`** — the parabolic-coset file's
  exchange hypothesis, discharged. **`length_minRep_mul_wordProd'`** —
  the Bourbaki lifting lemma, now UNCONDITIONAL at every rank.

Consequence: the length-additivity obligations of the merged
`DihedralCosetStructure` / `CommutingCosetStructure` reductions rest on a
proved theorem, not a hypothesis; what remains for the general-rank
braid/far-commutation instantiation is only the cell-equivalence
assembly (the parabolic transversal construction).

HONESTY (STRICT): sorry-free; no axiom, no class instance, no `True`.
Everything below is proved from Mathlib's Coxeter primitives. Nothing
wired; `1/(8π)` stays phase-4. Base ring: none — pure Coxeter
combinatorics with ℤ/2 bookkeeping (§7c not applicable).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterParabolicCoset
import Mathlib.GroupTheory.Coxeter.Inversion
import Mathlib.Data.ZMod.Basic

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open scoped Classical

/-! ## ℤ/2 parity counts -/

section ParityCount

variable {α : Type*}

/-- The ℤ/2 parity of the number of occurrences of `t` in `l`. -/
noncomputable def parityCount (l : List α) (t : α) : ZMod 2 :=
  (l.map (fun x => if x = t then (1 : ZMod 2) else 0)).sum

@[simp] lemma parityCount_nil (t : α) : parityCount ([] : List α) t = 0 := rfl

lemma parityCount_cons (x : α) (l : List α) (t : α) :
    parityCount (x :: l) t = (if x = t then 1 else 0) + parityCount l t := by
  simp [parityCount]

lemma parityCount_append (l₁ l₂ : List α) (t : α) :
    parityCount (l₁ ++ l₂) t = parityCount l₁ t + parityCount l₂ t := by
  simp [parityCount]

lemma parityCount_reverse (l : List α) (t : α) :
    parityCount l.reverse t = parityCount l t := by
  simp [parityCount, List.map_reverse, List.sum_reverse]

lemma mem_of_parityCount_ne_zero {l : List α} {t : α}
    (h : parityCount l t ≠ 0) : t ∈ l := by
  induction l with
  | nil => simp at h
  | cons x l ih =>
    rw [parityCount_cons] at h
    by_cases hx : x = t
    · rw [← hx]
      exact List.mem_cons_self
    · rw [if_neg hx, zero_add] at h
      exact List.mem_cons_of_mem x (ih h)

/-- A list of length `2m` whose entries repeat with period `m` has every
parity count zero: the list is two equal halves. -/
lemma parityCount_eq_zero_of_period {l : List α} {m : ℕ}
    (hlen : l.length = 2 * m)
    (hper : ∀ k, (hk : k < m) → l[m + k]'(by omega) = l[k]'(by omega))
    (t : α) : parityCount l t = 0 := by
  have hdt : l.drop m = l.take m := by
    apply List.ext_getElem
    · simp [hlen]
      omega
    · intro k h1 h2
      have hk : k < m := by
        rw [List.length_drop, hlen] at h1
        omega
      rw [List.getElem_drop, List.getElem_take]
      exact hper k hk
  have hxx : ∀ x : ZMod 2, x + x = 0 := by decide
  calc parityCount l t = parityCount (l.take m ++ l.drop m) t := by
        rw [List.take_append_drop]
    _ = parityCount (l.take m) t + parityCount (l.drop m) t :=
        parityCount_append _ _ _
    _ = parityCount (l.take m) t + parityCount (l.take m) t := by rw [hdt]
    _ = 0 := hxx _

end ParityCount

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-! ## The cocycle permutations -/

/-- The reflection-cocycle step at generator `i`:
`(w, ε) ↦ (σᵢ w σᵢ, ε + [w = σᵢ])`. -/
noncomputable def cocycleFun (i : B) : W × ZMod 2 → W × ZMod 2 :=
  fun p => (σ i * p.1 * σ i, p.2 + if p.1 = σ i then 1 else 0)

lemma cocycleFun_involutive (i : B) : Function.Involutive (cocycleFun cs i) := by
  rintro ⟨w, ε⟩
  have hss := cs.simple_mul_simple_self i
  unfold cocycleFun
  dsimp only
  by_cases hw : w = σ i
  · subst hw
    have h3 : σ i * σ i * σ i = σ i := by rw [hss, one_mul]
    have hx : ∀ x : ZMod 2, x + 1 + 1 = x := by decide
    rw [if_pos rfl, if_pos h3, Prod.mk.injEq]
    exact ⟨by rw [h3, h3], hx ε⟩
  · have hns : ¬(σ i * w * σ i = σ i) := by
      intro hcontra
      apply hw
      calc w = (σ i * σ i) * w * (σ i * σ i) := by rw [hss, one_mul, mul_one]
        _ = σ i * (σ i * w * σ i) * σ i := by group
        _ = σ i * σ i * σ i := by rw [hcontra]
        _ = σ i := by rw [hss, one_mul]
    have h1 : σ i * (σ i * w * σ i) * σ i = w := by
      calc σ i * (σ i * w * σ i) * σ i = (σ i * σ i) * w * (σ i * σ i) := by group
        _ = w := by rw [hss, one_mul, mul_one]
    rw [if_neg hw, if_neg hns, Prod.mk.injEq]
    exact ⟨h1, by rw [add_zero, add_zero]⟩

/-- The cocycle step as a permutation of `W × ℤ/2`. -/
noncomputable def cocyclePerm (i : B) : Equiv.Perm (W × ZMod 2) :=
  (cocycleFun_involutive cs i).toPerm

@[simp] lemma cocyclePerm_apply (i : B) (p : W × ZMod 2) :
    cocyclePerm cs i p = cocycleFun cs i p := rfl

/-- The composite cocycle permutation of a word. -/
noncomputable def cocycleWord (ω : List B) : Equiv.Perm (W × ZMod 2) :=
  (ω.map (cocyclePerm cs)).prod

@[simp] lemma cocycleWord_nil : cocycleWord cs ([] : List B) = 1 := rfl

lemma cocycleWord_cons (c : B) (ω : List B) :
    cocycleWord cs (c :: ω) = cocyclePerm cs c * cocycleWord cs ω := by
  simp [cocycleWord]

/-- **The master formula**: the composite cocycle permutation of a word
`ω` conjugates by `π ω` and adds the ℤ/2 count of `t` in the right
inversion sequence of `ω`. -/
theorem cocycleWord_apply (ω : List B) (t : W) (ε : ZMod 2) :
    cocycleWord cs ω (t, ε)
      = (π ω * t * (π ω)⁻¹, ε + parityCount (cs.rightInvSeq ω) t) := by
  induction ω with
  | nil => simp
  | cons c ω ih =>
    rw [cocycleWord_cons, Equiv.Perm.mul_apply, ih, cocyclePerm_apply]
    unfold cocycleFun
    have hcond : (π ω * t * (π ω)⁻¹ = σ c) ↔ ((π ω)⁻¹ * σ c * π ω = t) := by
      constructor
      · intro h
        rw [← h]
        group
      · intro h
        rw [← h]
        group
    have hris : cs.rightInvSeq (c :: ω) = ((π ω)⁻¹ * σ c * π ω) :: cs.rightInvSeq ω := by
      simp [rightInvSeq]
    rw [hris, parityCount_cons]
    have hfst : σ c * (π ω * t * (π ω)⁻¹) * σ c
        = π (c :: ω) * t * (π (c :: ω))⁻¹ := by
      rw [cs.wordProd_cons, mul_inv_rev, cs.inv_simple]
      group
    have hsnd : ε + parityCount (cs.rightInvSeq ω) t
          + (if π ω * t * (π ω)⁻¹ = σ c then (1 : ZMod 2) else 0)
        = ε + ((if (π ω)⁻¹ * σ c * π ω = t then 1 else 0)
          + parityCount (cs.rightInvSeq ω) t) := by
      rw [if_congr hcond rfl rfl]
      ring
    rw [Prod.mk.injEq]
    exact ⟨hfst, hsnd⟩

/-! ## Alternating-word bookkeeping for the braid check -/

lemma alternatingWord_two_mul_succ (i j : B) (m : ℕ) :
    alternatingWord i j (2 * (m + 1)) = i :: j :: alternatingWord i j (2 * m) := by
  have h1 : ¬ Even (2 * m + 1) := by rw [Nat.even_iff]; omega
  have h2 : Even (2 * m) := by rw [Nat.even_iff]; omega
  rw [show 2 * (m + 1) = (2 * m + 1) + 1 from by ring]
  rw [alternatingWord_succ', if_neg h1, alternatingWord_succ', if_pos h2]

lemma alternatingWord_odd_succ_succ (i j : B) (n : ℕ) :
    alternatingWord i j (2 * n + 1 + 2) = j :: i :: alternatingWord i j (2 * n + 1) := by
  have h1 : Even (2 * n + 1 + 1) := by rw [Nat.even_iff]; omega
  have h2 : ¬ Even (2 * n + 1) := by rw [Nat.even_iff]; omega
  rw [show 2 * n + 1 + 2 = (2 * n + 1 + 1) + 1 from by ring]
  rw [alternatingWord_succ', if_pos h1, alternatingWord_succ', if_neg h2]

lemma alternatingWord_two_mul_reverse (i j : B) (m : ℕ) :
    (alternatingWord i j (2 * m)).reverse = alternatingWord j i (2 * m) := by
  induction m with
  | zero => simp [alternatingWord]
  | succ m ih =>
    rw [alternatingWord_two_mul_succ]
    rw [show 2 * (m + 1) = (2 * m + 1) + 1 from by ring, alternatingWord_succ,
      alternatingWord_succ]
    simp [ih, List.concat_eq_append]

lemma wordProd_alternatingWord_two_mul (i j : B) (m : ℕ) :
    π (alternatingWord i j (2 * m)) = (σ i * σ j) ^ m := by
  induction m with
  | zero => simp [alternatingWord]
  | succ m ih =>
    rw [alternatingWord_two_mul_succ, cs.wordProd_cons, cs.wordProd_cons, ih,
      pow_succ', mul_assoc]

lemma wordProd_alternatingWord_odd_add (i j : B) (n m : ℕ) :
    π (alternatingWord i j (2 * n + 1 + 2 * m))
      = (σ j * σ i) ^ m * π (alternatingWord i j (2 * n + 1)) := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [show 2 * n + 1 + 2 * (m + 1) = 2 * (n + m) + 1 + 2 from by ring,
      alternatingWord_odd_succ_succ, cs.wordProd_cons, cs.wordProd_cons,
      show 2 * (n + m) + 1 = 2 * n + 1 + 2 * m from by ring, ih, pow_succ']
    group

/-- **Period-`m` structure of the inversion sequence of the braid word**:
entry `k + m` equals entry `k`, by `(σⱼ σᵢ)^{M i j} = 1`. -/
lemma getElem_leftInvSeq_alternatingWord_period (i j : B) (k : ℕ)
    (hk : k < M i j) :
    (cs.leftInvSeq (alternatingWord j i (2 * M i j)))[M i j + k]'(by
        simp [cs.length_leftInvSeq, length_alternatingWord]; omega)
      = (cs.leftInvSeq (alternatingWord j i (2 * M i j)))[k]'(by
        simp [cs.length_leftInvSeq, length_alternatingWord]; omega) := by
  rw [cs.getElem_leftInvSeq_alternatingWord j i (M i j) (M i j + k) (by omega),
    cs.getElem_leftInvSeq_alternatingWord j i (M i j) k (by omega)]
  rw [show 2 * (M i j + k) + 1 = 2 * k + 1 + 2 * M i j from by ring,
    wordProd_alternatingWord_odd_add cs, cs.simple_mul_simple_pow', one_mul]

/-! ## Liftability: the Coxeter relations hold in the cocycle representation -/

lemma cocyclePerm_mul_pow (i j : B) (m : ℕ) :
    (cocyclePerm cs i * cocyclePerm cs j) ^ m
      = cocycleWord cs (alternatingWord i j (2 * m)) := by
  induction m with
  | zero => simp [alternatingWord]
  | succ m ih =>
    rw [alternatingWord_two_mul_succ, cocycleWord_cons, cocycleWord_cons, ← ih,
      pow_succ', mul_assoc]

/-- **The cocycle permutations satisfy the Coxeter relations.** The parity
count over the inversion sequence of the doubled braid word vanishes
because the sequence is two identical halves. -/
theorem cocyclePerm_liftable : M.IsLiftable (cocyclePerm cs) := by
  intro i j
  rw [cocyclePerm_mul_pow]
  apply Equiv.ext
  rintro ⟨t, ε⟩
  rw [cocycleWord_apply]
  have hprod : π (alternatingWord i j (2 * M i j)) = 1 := by
    rw [wordProd_alternatingWord_two_mul cs, cs.simple_mul_simple_pow]
  have hcount : parityCount (cs.rightInvSeq (alternatingWord i j (2 * M i j))) t = 0 := by
    have hrev : cs.rightInvSeq (alternatingWord i j (2 * M i j))
        = (cs.leftInvSeq (alternatingWord j i (2 * M i j))).reverse := by
      have := cs.leftInvSeq_reverse (alternatingWord i j (2 * M i j))
      rw [alternatingWord_two_mul_reverse] at this
      rw [this, List.reverse_reverse]
    rw [hrev, parityCount_reverse]
    apply parityCount_eq_zero_of_period
      (m := M i j)
      (hlen := by simp [cs.length_leftInvSeq, length_alternatingWord])
    intro k hk
    exact getElem_leftInvSeq_alternatingWord_period cs i j k hk
  rw [hprod, hcount, add_zero, one_mul, inv_one, mul_one, Equiv.Perm.one_apply]

/-! ## The cocycle `η`, well-defined on `W` via the presentation lift -/

/-- The cocycle representation `W →* Perm (W × ℤ/2)`, via the universal
property of the Coxeter presentation. -/
noncomputable def etaHom : W →* Equiv.Perm (W × ZMod 2) :=
  cs.lift ⟨cocyclePerm cs, cocyclePerm_liftable cs⟩

@[simp] lemma etaHom_simple (i : B) : etaHom cs (σ i) = cocyclePerm cs i :=
  cs.lift_apply_simple (cocyclePerm_liftable cs) i

lemma etaHom_wordProd (ω : List B) : etaHom cs (π ω) = cocycleWord cs ω := by
  induction ω with
  | nil => simp [cs.wordProd_nil]
  | cons c ω ih =>
    rw [cs.wordProd_cons, map_mul, etaHom_simple, ih, cocycleWord_cons]

/-- The reflection cocycle `η(w, t) ∈ ℤ/2` — for `w = π ω`, the parity of
the number of occurrences of `t` in the right inversion sequence of `ω`,
well-defined on `W` (word-independent) because it is computed through the
homomorphism `etaHom`. -/
noncomputable def eta (w t : W) : ZMod 2 := (etaHom cs w (t, 0)).2

lemma eta_wordProd (ω : List B) (t : W) :
    eta cs (π ω) t = parityCount (cs.rightInvSeq ω) t := by
  unfold eta
  rw [etaHom_wordProd, cocycleWord_apply, zero_add]

lemma etaHom_apply (w t : W) (ε : ZMod 2) :
    etaHom cs w (t, ε) = (w * t * w⁻¹, ε + eta cs w t) := by
  obtain ⟨ω, -, rfl⟩ := cs.exists_reduced_word w
  rw [etaHom_wordProd, cocycleWord_apply, eta_wordProd]

/-- **The cocycle law**: `η(uv, t) = η(v, t) + η(u, v t v⁻¹)`. -/
lemma eta_mul (u v t : W) :
    eta cs (u * v) t = eta cs v t + eta cs u (v * t * v⁻¹) := by
  have key : etaHom cs (u * v) (t, 0)
      = ((u * v) * t * (u * v)⁻¹, eta cs v t + eta cs u (v * t * v⁻¹)) := by
    rw [map_mul, Equiv.Perm.mul_apply, etaHom_apply cs v, zero_add, etaHom_apply cs u]
    rw [Prod.mk.injEq]
    constructor
    · group
    · rfl
  have hdef : eta cs (u * v) t = (etaHom cs (u * v) (t, 0)).2 := rfl
  rw [hdef, key]

@[simp] lemma eta_one (t : W) : eta cs 1 t = 0 := by
  unfold eta
  rw [map_one, Equiv.Perm.one_apply]

lemma eta_simple_self (c : B) : eta cs (σ c) (σ c) = 1 := by
  unfold eta
  rw [etaHom_simple, cocyclePerm_apply]
  unfold cocycleFun
  simp

lemma eta_inv_add (r t : W) : eta cs r⁻¹ t + eta cs r (r⁻¹ * t * r) = 0 := by
  have := eta_mul cs r r⁻¹ t
  rw [mul_inv_cancel, eta_one, inv_inv] at this
  exact this.symm

/-- **`η(t, t) = 1` for every reflection `t`** — the three-line cocycle
algebra (no induction): decompose `t = w σ_c w⁻¹` and expand `η(t, t)`
with the cocycle law. -/
theorem eta_isReflection_self {t : W} (ht : cs.IsReflection t) :
    eta cs t t = 1 := by
  obtain ⟨w, c, rfl⟩ := ht
  set t := w * σ c * w⁻¹ with hT
  -- η(t,t) = η(σc·w⁻¹, t) + η(w, σc)
  have step1 : eta cs t t = eta cs (σ c * w⁻¹) t + eta cs w (σ c) := by
    have hsplit : t = w * (σ c * w⁻¹) := by rw [hT]; group
    have harg : (σ c * w⁻¹) * t * (σ c * w⁻¹)⁻¹ = σ c := by
      rw [hT]
      group
    calc eta cs t t = eta cs (w * (σ c * w⁻¹)) t := by rw [← hsplit]
      _ = eta cs (σ c * w⁻¹) t + eta cs w ((σ c * w⁻¹) * t * (σ c * w⁻¹)⁻¹) :=
          eta_mul cs w (σ c * w⁻¹) t
      _ = eta cs (σ c * w⁻¹) t + eta cs w (σ c) := by rw [harg]
  -- η(σc·w⁻¹, t) = η(w⁻¹, t) + 1
  have step2 : eta cs (σ c * w⁻¹) t = eta cs w⁻¹ t + 1 := by
    have harg : w⁻¹ * t * (w⁻¹)⁻¹ = σ c := by
      rw [hT]
      group
    calc eta cs (σ c * w⁻¹) t
        = eta cs w⁻¹ t + eta cs (σ c) (w⁻¹ * t * (w⁻¹)⁻¹) :=
          eta_mul cs (σ c) w⁻¹ t
      _ = eta cs w⁻¹ t + 1 := by rw [harg, eta_simple_self]
  -- η(w⁻¹, t) + η(w, σc) = 0
  have step3 : eta cs w⁻¹ t + eta cs w (σ c) = 0 := by
    have harg : w⁻¹ * t * w = σ c := by
      rw [hT]
      group
    have := eta_inv_add cs w t
    rwa [harg] at this
  have hswap : ∀ a b : ZMod 2, a + b = 0 → a + 1 + b = 1 := by decide
  rw [step1, step2]
  exact hswap _ _ step3

/-! ## From `η = 1` to letter deletion, and the exchange theorems -/

lemma mem_rightInvSeq_of_eta_eq_one {ω : List B} {t : W}
    (h : eta cs (π ω) t = 1) : t ∈ cs.rightInvSeq ω := by
  apply mem_of_parityCount_ne_zero
  rw [← eta_wordProd, h]
  exact one_ne_zero

lemma exists_eraseIdx_of_eta_eq_one {ω : List B} {t : W}
    (h : eta cs (π ω) t = 1) :
    ∃ j < ω.length, π ω * t = π (ω.eraseIdx j) := by
  obtain ⟨j, hj, hjt⟩ := List.mem_iff_getElem.mp (mem_rightInvSeq_of_eta_eq_one cs h)
  have hlen : j < ω.length := by
    rwa [cs.length_rightInvSeq] at hj
  refine ⟨j, hlen, ?_⟩
  have := cs.wordProd_mul_getD_rightInvSeq ω j
  rwa [List.getD_eq_getElem _ _ hj, hjt] at this

lemma length_mul_lt_of_eta_eq_one {ω : List B} (hred : cs.IsReduced ω)
    {t : W} (h : eta cs (π ω) t = 1) : ℓ (π ω * t) < ℓ (π ω) := by
  obtain ⟨j, hj, heq⟩ := exists_eraseIdx_of_eta_eq_one cs h
  rw [heq]
  calc ℓ (π (ω.eraseIdx j)) ≤ (ω.eraseIdx j).length := cs.length_wordProd_le _
    _ < ω.length := by
        have := List.length_eraseIdx_add_one hj
        omega
    _ = ℓ (π ω) := hred.symm

/-- **The key equivalence direction**: a right inversion has `η = 1` —
by the self-inverse trick `η(wt, t) = η(t, t) + η(w, t) = 1 + η(w, t)`:
were `η(w, t) = 0`, a reduced word for `w t` would delete a letter and
give `ℓ(w) < ℓ(w t)`, contradicting `ℓ(w t) < ℓ(w)`. -/
theorem eta_eq_one_of_isRightInversion {w t : W}
    (h : cs.IsRightInversion w t) : eta cs w t = 1 := by
  by_contra hne
  have h0 : eta cs w t = 0 := by
    have hcase : ∀ x : ZMod 2, x ≠ 1 → x = 0 := by decide
    exact hcase _ hne
  have hmul : eta cs (w * t) t = 1 := by
    have := eta_mul cs w t t
    have harg : t * t * t⁻¹ = t := by group
    rw [harg, h0, add_zero, eta_isReflection_self cs h.1] at this
    exact this
  obtain ⟨ω, hlen, hw⟩ := cs.exists_reduced_word (w * t)
  have hred : cs.IsReduced ω := by
    unfold CoxeterSystem.IsReduced
    rw [← hw, hlen]
  have hlt : ℓ (π ω * t) < ℓ (π ω) := by
    apply length_mul_lt_of_eta_eq_one cs hred
    rw [← hw]
    exact hmul
  rw [← hw, mul_assoc, h.1.mul_self, mul_one] at hlt
  exact absurd h.2 (not_lt_of_gt hlt)

/-- **STRONG EXCHANGE** (Bjorner–Brenti Thm 1.4.3): if `t` is a right
inversion of `π ω` — any reflection, any word, reducedness NOT required —
then `π ω · t` is obtained by deleting a single letter of `ω`. -/
theorem strong_exchange (ω : List B) {t : W}
    (h : cs.IsRightInversion (π ω) t) :
    ∃ j < ω.length, π ω * t = π (ω.eraseIdx j) :=
  exists_eraseIdx_of_eta_eq_one cs (eta_eq_one_of_isRightInversion cs h)

/-- **The right exchange property holds in every Coxeter system** — the
hypothesis of the parabolic-coset lifting lemma, discharged
unconditionally. This closes the audited Mathlib gap: the braid and
far-commutation coset reductions no longer rest on an unproved
hypothesis. -/
theorem rightExchange : RightExchangeProp cs := by
  intro ω hred c hdesc
  obtain ⟨j, -, hj⟩ := strong_exchange cs ω
    ((cs.isRightInversion_simple_iff_isRightDescent (π ω) c).mpr hdesc)
  exact ⟨j, hj⟩
-- Note: `strong_exchange` returns a bounded existential `∃ j < ω.length, …`
-- while `RightExchangeProp` asks the unbounded `∃ r, …`, so the destructure
-- re-packages the witness; a direct `exact` does not typecheck.

/-- **The Bourbaki lifting lemma, UNCONDITIONAL**: a minimal coset
representative `u` and a reduced `J`-word `p` satisfy
`ℓ(u · π p) = ℓ(u) + |p|` — at every rank, from Mathlib's primitives
alone. -/
theorem length_minRep_mul_wordProd' (J : Set B) {u : W}
    (hu : IsMinRep cs J u) {p : List B} (hp : ∀ l ∈ p, l ∈ J)
    (hred : cs.IsReduced p) :
    ℓ (u * π p) = ℓ u + p.length :=
  length_minRep_mul_wordProd cs J (rightExchange cs) hu hp hred

end QOU.Machinery.CoxeterParabolic
