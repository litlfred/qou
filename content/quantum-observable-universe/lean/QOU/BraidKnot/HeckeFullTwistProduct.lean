import QOU.BraidKnot.HeckeTranspositionExpansion

/-!
# `∏Lᵢ = Δ²` for every `n`

`HeckeJucysMurphyElements` proved the twist identity at `n = 2` and `n = 3` by writing both sides
out and applying one braid move.  That does not generalise: at `n = 4` the word has 12 letters and
the number of braid moves grows.  This file proves it for all `n`.

## What is being proved, and what commutativity does *not* give

`jmRaw_comm` makes the product `L₀L₁⋯Lₙ` **order-independent**.  That is a different statement from
identifying it with the full twist, and it is not used here — this file is pure braid-group
combinatorics and touches the Hecke relation nowhere.  (Contrast `sigma_comm_transp_pair`, where the
Hecke relation was essential.)

## The shape of the argument

Two words, both built only from the generators:

* `delta k = σ₀σ₁⋯σ_{k−1}` — the ascending run.  `Δ² = (delta n)^{n+1}` is the full twist of `B_{n+1}`.
* `run b k = σ_{b+k−1}⋯σ_b` — a descending run with bottom `b`.

The JM element factors as `Lₖ = run 0 k · delta k` (`jmRaw_eq_run_mul_delta`), which is just its own
recursion read as a word.  Everything then rests on one identity:

    (delta (b+k) · σ_{b+k})^{k+1} = (delta (b+k))^{k+1} · run b (k+1)          `delta_pow_run`

At `b = 0` this reads `(delta (n+1))^{n+1} = (delta n)^{n+1} · run 0 (n+1)`, and multiplying on the
right by `delta (n+1)` turns the right-hand side into `(delta n)^{n+1} · L_{n+1}` and the left into
`(delta (n+1))^{n+2}` — which is the induction step for the twist identity.

The free bottom index `b` is what makes the induction go through: the step consumes the inductive
hypothesis at `b+1`, not at `b`, so a version stated only at `b = 0` would not close.

## The one place a braid move happens

`run_push` — the statement that a descending run can be pushed through `delta`, at the cost of
turning the trailing `σ_{b+j}` into a `σ_b`.  Its inductive step reduces to

    σ_{m+1} σ_m σ_{m+1} = σ_m σ_{m+1} σ_m

with everything else moved aside by far-commutation.  Every other lemma here is bookkeeping.

Refs:
- [wenzl1988] Hecke algebra representations.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-- **Ascending run** `delta k = σ₀ σ₁ ⋯ σ_{k−1}`.  The full twist of `B_{n+1}` is
`(delta n)^{n+1}`. -/
def delta (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | (k + 1) => delta H k * H.σ k

/-- **Descending run** `run b k = σ_{b+k−1} σ_{b+k−2} ⋯ σ_b`, peeled from the top so that the
bottom index `b` stays fixed under the recursion. -/
def run (H : HeckeGenerators R A q) (b : ℕ) : ℕ → A
  | 0 => 1
  | (k + 1) => H.σ (b + k) * run H b k

@[simp] theorem delta_zero (H : HeckeGenerators R A q) : delta H 0 = 1 := rfl

theorem delta_succ (H : HeckeGenerators R A q) (k : ℕ) :
    delta H (k + 1) = delta H k * H.σ k := rfl

@[simp] theorem run_zero (H : HeckeGenerators R A q) (b : ℕ) : run H b 0 = 1 := rfl

theorem run_succ (H : HeckeGenerators R A q) (b k : ℕ) :
    run H b (k + 1) = H.σ (b + k) * run H b k := rfl

/-- The same run peeled from the **bottom** instead: `run b (k+1) = run (b+1) k · σ_b`. -/
theorem run_peel_bot (H : HeckeGenerators R A q) (b : ℕ) :
    ∀ k : ℕ, run H b (k + 1) = run H (b + 1) k * H.σ b := by
  intro k
  induction k generalizing b with
  | zero => simp [run]
  | succ i ih =>
      rw [run_succ, ih, run_succ]
      have e : b + 1 + i = b + (i + 1) := by omega
      rw [e, mul_assoc]

/-- `σ_j` commutes with a whole descending run whose letters all sit at distance `≥ 2` below `j`. -/
theorem sigma_comm_run (H : HeckeGenerators R A q) (b j : ℕ) :
    ∀ k : ℕ, b + k < j → H.σ j * run H b k = run H b k * H.σ j := by
  intro k
  induction k with
  | zero => simp
  | succ i ih =>
      intro h
      have hfar : H.σ (b + i) * H.σ j = H.σ j * H.σ (b + i) := H.far (b + i) j (by omega)
      have hih := ih (by omega)
      rw [run_succ]
      calc H.σ j * (H.σ (b + i) * run H b i)
          = (H.σ j * H.σ (b + i)) * run H b i := by noncomm_ring
        _ = (H.σ (b + i) * H.σ j) * run H b i := by rw [hfar]
        _ = H.σ (b + i) * (H.σ j * run H b i) := by noncomm_ring
        _ = H.σ (b + i) * (run H b i * H.σ j) := by rw [hih]
        _ = _ := by noncomm_ring

/-- `σ_j` commutes with `delta m` whenever `m < j` — every letter of `delta m` has index `≤ m−1`. -/
theorem sigma_comm_delta (H : HeckeGenerators R A q) (j : ℕ) :
    ∀ m : ℕ, m < j → H.σ j * delta H m = delta H m * H.σ j := by
  intro m
  induction m with
  | zero => simp
  | succ i ih =>
      intro h
      have hfar : H.σ i * H.σ j = H.σ j * H.σ i := H.far i j (by omega)
      have hih := ih (by omega)
      rw [delta_succ]
      calc H.σ j * (delta H i * H.σ i)
          = (H.σ j * delta H i) * H.σ i := by noncomm_ring
        _ = (delta H i * H.σ j) * H.σ i := by rw [hih]
        _ = delta H i * (H.σ j * H.σ i) := by noncomm_ring
        _ = delta H i * (H.σ i * H.σ j) := by rw [← hfar]
        _ = _ := by noncomm_ring

/-- **The push law's core braid step**, isolated.

For any `r` commuting with `σ_{m+1}`, and any `b < m`:

    σ_{m+1} · (σ_m r) · σ_b · σ_{m+1}  =  σ_m · (σ_{m+1} · (σ_m r)) · σ_b

`σ_b` slides past `σ_{m+1}` (they are `≥ 2` apart because `b < m`), `σ_{m+1}` slides past `r` by
hypothesis, and what is left is the braid relation on `σ_m, σ_{m+1}`. -/
theorem core_braid_push (H : HeckeGenerators R A q) (b m : ℕ) (hbm : b < m) (r : A)
    (hr : H.σ (m + 1) * r = r * H.σ (m + 1)) :
    H.σ (m + 1) * (H.σ m * r) * H.σ b * H.σ (m + 1)
      = H.σ m * (H.σ (m + 1) * (H.σ m * r)) * H.σ b := by
  have hbf : H.σ b * H.σ (m + 1) = H.σ (m + 1) * H.σ b := H.far b (m + 1) (by omega)
  have hbr : H.σ m * H.σ (m + 1) * H.σ m = H.σ (m + 1) * H.σ m * H.σ (m + 1) := H.braid m
  calc H.σ (m + 1) * (H.σ m * r) * H.σ b * H.σ (m + 1)
      = H.σ (m + 1) * H.σ m * r * (H.σ b * H.σ (m + 1)) := by noncomm_ring
    _ = H.σ (m + 1) * H.σ m * r * (H.σ (m + 1) * H.σ b) := by rw [hbf]
    _ = H.σ (m + 1) * H.σ m * (r * H.σ (m + 1)) * H.σ b := by noncomm_ring
    _ = H.σ (m + 1) * H.σ m * (H.σ (m + 1) * r) * H.σ b := by rw [← hr]
    _ = (H.σ (m + 1) * H.σ m * H.σ (m + 1)) * r * H.σ b := by noncomm_ring
    _ = (H.σ m * H.σ (m + 1) * H.σ m) * r * H.σ b := by rw [← hbr]
    _ = _ := by noncomm_ring

/-- **The push law** — the only place a braid move happens in this file.

    run (b+1) j · delta m · σ_m  =  delta m · run (b+1) j · σ_b        (m = b + j)

A descending run can be carried through `delta`; the price is that the trailing generator drops from
`σ_m` all the way to `σ_b`.  That drop is exactly what turns the ascending-run power into a JM
element in `delta_pow_run`.

The index `m` is carried as a variable with `m = b + j` as a hypothesis rather than written as
`b + j` inline: the induction re-associates the sum at every step, and a syntactic `b + j` would
force a rewrite before each use. -/
theorem run_push (H : HeckeGenerators R A q) : ∀ (j b m : ℕ), m = b + j →
    run H (b + 1) j * delta H m * H.σ m
      = delta H m * run H (b + 1) j * H.σ b := by
  intro j
  induction j with
  | zero => intro b m hm; subst hm; simp
  | succ i ih =>
      intro b m hm
      obtain ⟨p, hp, hpb⟩ : ∃ p, m = p + 1 ∧ p = b + i := ⟨b + i, by omega, rfl⟩
      subst hp
      have hrun : run H (b + 1) (i + 1) = H.σ (p + 1) * run H (b + 1) i := by
        rw [run_succ]; congr 2; omega
      have hd : delta H (p + 1) = delta H p * H.σ p := delta_succ H p
      have hdc : H.σ (p + 1) * delta H p = delta H p * H.σ (p + 1) :=
        sigma_comm_delta H (p + 1) p (by omega)
      have hih : run H (b + 1) i * delta H p * H.σ p
          = delta H p * run H (b + 1) i * H.σ b := ih b p hpb
      have hcore : H.σ (p + 1) * run H (b + 1) i * H.σ b * H.σ (p + 1)
          = H.σ p * (H.σ (p + 1) * run H (b + 1) i) * H.σ b := by
        cases i with
        | zero =>
            have hbp : b = p := by omega
            subst hbp
            have hb : H.σ b * H.σ (b + 1) * H.σ b
                = H.σ (b + 1) * H.σ b * H.σ (b + 1) := H.braid b
            simp only [run_zero, mul_one]
            rw [← hb]
        | succ l =>
            have hp2 : run H (b + 1) (l + 1) = H.σ p * run H (b + 1) l := by
              rw [run_succ]; congr 2; omega
            have hr : H.σ (p + 1) * run H (b + 1) l = run H (b + 1) l * H.σ (p + 1) :=
              sigma_comm_run H (b + 1) (p + 1) l (by omega)
            rw [hp2]
            exact core_braid_push H b p (by omega) (run H (b + 1) l) hr
      rw [hrun, hd]
      calc H.σ (p + 1) * run H (b + 1) i * (delta H p * H.σ p) * H.σ (p + 1)
          = H.σ (p + 1) * (run H (b + 1) i * delta H p * H.σ p) * H.σ (p + 1) := by noncomm_ring
        _ = H.σ (p + 1) * (delta H p * run H (b + 1) i * H.σ b) * H.σ (p + 1) := by rw [hih]
        _ = (H.σ (p + 1) * delta H p) * (run H (b + 1) i * H.σ b * H.σ (p + 1)) := by noncomm_ring
        _ = (delta H p * H.σ (p + 1)) * (run H (b + 1) i * H.σ b * H.σ (p + 1)) := by rw [hdc]
        _ = delta H p
              * (H.σ (p + 1) * run H (b + 1) i * H.σ b * H.σ (p + 1)) := by noncomm_ring
        _ = delta H p
              * (H.σ p * (H.σ (p + 1) * run H (b + 1) i) * H.σ b) := by rw [hcore]
        _ = _ := by noncomm_ring

/-! ## The power identity, and the twist -/

/-- **The engine**: `(delta m · σ_m)^{k+1} = (delta m)^{k+1} · run b (k+1)` for `m = b + k`.

The free bottom index `b` is load-bearing — the inductive step consumes the hypothesis at `b+1`, so
a version stated only at `b = 0` does not close. -/
theorem delta_pow_run (H : HeckeGenerators R A q) : ∀ (k b m : ℕ), m = b + k →
    (delta H m * H.σ m) ^ (k + 1) = (delta H m) ^ (k + 1) * run H b (k + 1) := by
  intro k
  induction k with
  | zero => intro b m hm; subst hm; simp [run_succ]
  | succ l ih =>
      intro b m hm
      have hih := ih (b + 1) m (by omega)
      have hpush := run_push H (l + 1) b m hm
      have hpeel : run H b (l + 1 + 1) = run H (b + 1) (l + 1) * H.σ b := run_peel_bot H b (l + 1)
      calc (delta H m * H.σ m) ^ (l + 1 + 1)
          = (delta H m * H.σ m) ^ (l + 1) * (delta H m * H.σ m) := by rw [pow_succ]
        _ = delta H m ^ (l + 1) * run H (b + 1) (l + 1) * (delta H m * H.σ m) := by rw [hih]
        _ = delta H m ^ (l + 1) * (run H (b + 1) (l + 1) * delta H m * H.σ m) := by noncomm_ring
        _ = delta H m ^ (l + 1) * (delta H m * run H (b + 1) (l + 1) * H.σ b) := by rw [hpush]
        _ = (delta H m ^ (l + 1) * delta H m) * (run H (b + 1) (l + 1) * H.σ b) := by noncomm_ring
        _ = delta H m ^ (l + 1 + 1) * run H b (l + 1 + 1) := by rw [← pow_succ, ← hpeel]

/-- **The twist step**: `(delta (n+1))^{n+1} = (delta n)^{n+1} · run 0 (n+1)`. -/
theorem delta_twist_step (H : HeckeGenerators R A q) (n : ℕ) :
    delta H (n + 1) ^ (n + 1) = delta H n ^ (n + 1) * run H 0 (n + 1) := by
  have h := delta_pow_run H n 0 n (by omega)
  rw [← delta_succ] at h
  exact h

/-- **The JM element as a word**: `Lₖ = run 0 k · delta k`, i.e. `σ_{k−1}⋯σ₀ · σ₀⋯σ_{k−1}`.  This is
just its own recursion read as a word. -/
theorem jmRaw_eq_run_mul_delta (H : HeckeGenerators R A q) (k : ℕ) :
    jmRaw H k = run H 0 k * delta H k := by
  induction k with
  | zero => simp
  | succ i ih =>
      rw [jmRaw_succ, ih, run_succ, delta_succ]
      simp only [Nat.zero_add]
      noncomm_ring

/-- The ordered product `L₀ L₁ ⋯ L_{n−1}`.  A `Finset.prod` is unavailable here — `A` is not
commutative — so the product is defined by its own recursion. -/
def jmProd (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | (n + 1) => jmProd H n * jmRaw H n

theorem jmProd_succ (H : HeckeGenerators R A q) (n : ℕ) :
    jmProd H (n + 1) = jmProd H n * jmRaw H n := rfl

/-- **`∏Lᵢ = Δ²`, for every `n`.**  `L₀L₁⋯Lₙ = (delta n)^{n+1}`, the full twist of `B_{n+1}`.

Proved from the braid relations alone — the Hecke relation is not used anywhere in this file, and
neither is `jmRaw_comm` (which makes the product order-independent, a different statement). -/
theorem jmProd_eq_delta_pow (H : HeckeGenerators R A q) (n : ℕ) :
    jmProd H (n + 1) = delta H n ^ (n + 1) := by
  induction n with
  | zero => simp [jmProd]
  | succ m ih =>
      rw [jmProd_succ, ih, jmRaw_eq_run_mul_delta]
      calc delta H m ^ (m + 1) * (run H 0 (m + 1) * delta H (m + 1))
          = (delta H m ^ (m + 1) * run H 0 (m + 1)) * delta H (m + 1) := by noncomm_ring
        _ = delta H (m + 1) ^ (m + 1) * delta H (m + 1) := by rw [← delta_twist_step]
        _ = delta H (m + 1) ^ (m + 1 + 1) := (pow_succ _ _).symm

/-! ## Consistency with the hand-proved small cases -/

theorem delta_two (H : HeckeGenerators R A q) : delta H 2 = H.σ 0 * H.σ 1 := by
  simp [delta_succ]

/-- The `n = 2` case of `HeckeJucysMurphyElements.jmRaw_prod_two`, recovered from the general
theorem. -/
theorem jmProd_two_eq_fullTwist2 (H : HeckeGenerators R A q) :
    jmProd H 2 = fullTwist2 H := by
  rw [jmProd_eq_delta_pow H 1]
  simp [delta_succ, fullTwist2, pow_succ]

/-- The `n = 3` case of `HeckeJucysMurphyElements.jmRaw_prod_three`, recovered from the general
theorem — the hand proof there used one explicit braid move on a six-letter word; this one is the
`n = 2` instance of an induction. -/
theorem jmProd_three_eq_fullTwist3 (H : HeckeGenerators R A q) :
    jmProd H 3 = fullTwist3 H := by
  rw [jmProd_eq_delta_pow H 2, delta_two]
  rfl

end QOU.BraidKnot.Hecke
