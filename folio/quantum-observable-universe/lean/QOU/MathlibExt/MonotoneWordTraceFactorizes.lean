import QOU.MathlibExt.MarkovTraceInterleavedCrossTerm
import Mathlib.Tactic

/-!
# Monotone Hecke words factorize under the Markov trace — the converse of the `n = 4` cross term

`MarkovTraceInterleavedCrossTerm` shows that the Markov trace is **not** bond-multiplicative in
general: the interleaved word `g₀ g₁ g₀ g₂ g₁` and the sequential word `g₀² g₁² g₂` have the same
per-generator content and traces differing by the exact cross term `z (z² − h z − 1)`.

This file proves the converse direction, which is what the production atom word actually relies
on. Call a word **monotone** if it is an ascending product `s n · s (n+1) · ⋯ · s (n+k−1)` in which
the letter at level `m` lies in `H (m+1)` and stabilises the trace on `H m` with some constant
`c m` — every letter of the form `a • 1 + b • g m` (the production superposition letter
`c·σ_g + d·1`), every power `g m ^ e` (a run of one generator), and every `R`-linear combination
of these qualifies. Then

    tr (a · s n ⋯ s (n+k−1)) = (∏ᵢ c (n+i)) · tr a         for `a ∈ H n`,

and in particular the trace of the bare word is the **product of the letter traces**
(`tr_stabWord_eq_prod_tr`). Ordering is the whole content: the same letters in a non-ascending
order can carry a cross term (`content_reorder_defect`), the ascending order never does.

## Why this matters for the derivation chain

`computations/mass_at_3A_proper.py::atom_braid_word_3A` writes each nucleon on generators
`3k, 3k+1` and the inter-nucleon bond as a **single** letter at `3k+2`, walking the chain once
in ascending order.

🛑 **CORRECTION (2026-09-14, bean `qou-u5qs`). This passage used to continue "so the
production word is monotone in the sense above", and that is no longer true of the live
word.** Since the 2026-09-05 owner ruling (bean `qou-hu1f`) each nucleon's confinement core
is the **alternating** `(σ₀σ₁⁻¹)³`, not a run of one generator — and `σ₀`, `σ₁` are adjacent
and do not commute, so the core is not a `stabWord` in the sense this file defines.
`mass_at_3A_proper.py` records the same thing from the topological side (measured
2026-09-07, bean `qou-m6gp`): *"The 2026-09-05 alternating core `(σ₀σ₁⁻¹)³` is NOT monotone,
so the monotone ⇒ #T(2,k) ⇒ Vol = 0 argument no longer applies."*

**What survives, and it is the whole per-bond product form — only the reason changed.** The
grounding is now **connected-sum multiplicativity**: each interface is a *single* letter, so
every atom branch closure is the connected sum of its `A` nucleon pieces (measured, 800/800
branches over ²H/³H/³He/⁴He decompose into exactly `A` summands), and the Markov trace is
blind to letter order *inside* a summand. So `tr_M(W_atom)/tr_M(W_free)` is identical under
the grouped and alternating intra-orderings to `~1e-60` at `A = 2, 3, 4`, and the
bond-additivity of the binding, `qou-ls86`'s `n = 3` identity and the absence of the `n = 4`
cross term all stand — as theorems about the **interface being one letter**, not about the
ordering.

The theorems in this file are untouched: they are stated for an arbitrary `stabWord` and
prove exactly what they say. It is only the claim that the *production* word is one of them
that was stale. It is also the algebraic face of the topological fact
recorded on 2026-08-25 (`docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`): a
monotone word closes to a connected sum of `(2, k)` torus links, with hyperbolic volume `0`.
Both statements have the same single hypothesis. See
`docs/audits/2026-09-04-monotone-word-trace-factorizes-derived-link-map.md`.

## Base ring (§7c)

Generic `CommRing R` acting on a generic `Ring A`, through the `MarkovTrace` structure of
`QOU.MathlibExt.OcneanuTrace` (T1–T3). The Hecke quadratic is a hypothesis where a run
`g m ^ e` is collapsed. The one convention-D evaluation is over a generic `Field`.

-- Ref: [leitner2026] computations/mass_at_3A_proper.py (atom_braid_word_3A)
-- Ref: [leitner2026] docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md
-- Ref: [jones1987] https://doi.org/10.2307/1971403 — the Markov trace on the Hecke tower.
-/

namespace QOU.MathlibExt.MonotoneWordFactorizes

open QOU.MathlibExt.OcneanuTrace
open QOU.MathlibExt.InterleavedCrossTerm

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-! ## Stabilising letters: the general factorization -/

/-- **Iterated Markov stabilisation with a level-dependent constant.** If every letter `s m` lies
in `H (m+1)` and stabilises the trace on `H m` by `c m`, then appending the ascending word
`s n ⋯ s (n+k−1)` to `a ∈ H n` multiplies the trace by `∏ᵢ<ₖ c (n+i)`. This generalises
`MarkovTrace.tr_mul_stabWord` (constant `c`) to letters with different traces at each level. -/
theorem tr_mul_stabWord_prod (s : ℕ → A) (c : ℕ → R) (hs : ∀ m, s m ∈ T.H (m + 1))
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c m * T.tr a) (n : ℕ) :
    ∀ (k : ℕ) (a : A), a ∈ T.H n →
      T.tr (a * stabWord s n k) = (∏ i ∈ Finset.range k, c (n + i)) * T.tr a := by
  intro k
  induction k with
  | zero => intro a _; simp
  | succ k ih =>
    intro a ha
    have hmem : a * stabWord s n k ∈ T.H (n + k) :=
      (T.H (n + k)).mul_mem (T.H_mono (Nat.le_add_right n k) ha) (T.stabWord_mem s hs n k)
    rw [stabWord_succ, ← mul_assoc, hstab (n + k) _ hmem, ih a ha, Finset.prod_range_succ]
    ring

/-- The trace of a bare monotone word is the product of the stabilising constants. -/
theorem tr_stabWord_prod (s : ℕ → A) (c : ℕ → R) (hs : ∀ m, s m ∈ T.H (m + 1))
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c m * T.tr a) (n k : ℕ) :
    T.tr (stabWord s n k) = ∏ i ∈ Finset.range k, c (n + i) := by
  have h := tr_mul_stabWord_prod T s c hs hstab n k 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-- A stabilising letter's constant is its own trace: `c m = tr (s m)`. -/
theorem stab_const_eq_tr (s : ℕ → A) (c : ℕ → R)
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c m * T.tr a) (m : ℕ) :
    c m = T.tr (s m) := by
  have h := hstab m 1 (T.H m).one_mem
  rw [one_mul, T.tr_one, mul_one] at h
  exact h.symm

/-- **MONOTONE ⇒ FACTORIZES.** The Markov trace of an ascending word of stabilising letters is
the product of the traces of its letters. This is the per-bond product form that the production
atom word's trace implementation assumes, proved from the ordering alone. -/
theorem tr_stabWord_eq_prod_tr (s : ℕ → A) (c : ℕ → R) (hs : ∀ m, s m ∈ T.H (m + 1))
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c m * T.tr a) (n k : ℕ) :
    T.tr (stabWord s n k) = ∏ i ∈ Finset.range k, T.tr (s (n + i)) := by
  rw [tr_stabWord_prod T s c hs hstab n k]
  exact Finset.prod_congr rfl fun i _ => stab_const_eq_tr T s c hstab (n + i)

/-! ## Which letters stabilise -/

/-- The affine letter `a • 1 + b • g m` — the production superposition letter `c·σ + d·1` —
lies one level up. -/
theorem affine_mem (m : ℕ) (a b : R) : a • (1 : A) + b • T.g m ∈ T.H (m + 1) :=
  (T.H (m + 1)).add_mem ((T.H (m + 1)).smul_mem (T.H (m + 1)).one_mem a)
    ((T.H (m + 1)).smul_mem (T.g_mem m) b)

/-- The affine letter stabilises with constant `a + b z`: linearity plus one Markov move. -/
theorem tr_mul_affine (m : ℕ) (a b : R) (x : A) (hx : x ∈ T.H m) :
    T.tr (x * (a • (1 : A) + b • T.g m)) = (a + b * T.z) * T.tr x := by
  rw [mul_add, mul_smul_comm, mul_smul_comm, mul_one, map_add, map_smul, map_smul,
    T.markov m x hx, smul_eq_mul, smul_eq_mul]
  ring

/-- The trace of a single affine letter. -/
theorem tr_affine (m : ℕ) (a b : R) : T.tr (a • (1 : A) + b • T.g m) = a + b * T.z := by
  have h := tr_mul_affine T m a b 1 (T.H m).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-- **The production word class.** An ascending word whose letter at level `m` is
`a m • 1 + b m • g m` has trace `∏ᵢ (a (n+i) + b (n+i) z)`: one factor per letter, each the trace
of that letter alone. -/
theorem tr_affineWord (a b : ℕ → R) (n k : ℕ) :
    T.tr (stabWord (fun m => a m • (1 : A) + b m • T.g m) n k)
      = ∏ i ∈ Finset.range k, (a (n + i) + b (n + i) * T.z) :=
  tr_stabWord_prod T _ (fun m => a m + b m * T.z) (fun m => affine_mem T m (a m) (b m))
    (fun m x hx => tr_mul_affine T m (a m) (b m) x hx) n k

/-- **The affine letters at one level form a 2-dimensional algebra.** Under the Hecke quadratic,
the product of two affine letters at level `m` is again affine — so a *run* of production
superposition letters on one generator (the 7 letters `atom_braid_word_3A` writes at `g₀` for
²H, say) collapses to a single affine letter and is covered by `tr_affineWord`. -/
theorem affine_mul_affine (m : ℕ) (h : R) (hq : T.g m * T.g m = h • T.g m + 1) (a b a' b' : R) :
    (a • (1 : A) + b • T.g m) * (a' • (1 : A) + b' • T.g m)
      = (a * a' + b * b') • (1 : A) + (a * b' + a' * b + h * (b * b')) • T.g m := by
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, hq,
    smul_add, add_smul]
  module

/-- The Chebyshev-type run coefficient: `tr (x · g^e) = runCoeff h z e · tr x` for `x ∈ H m`,
under the Hecke quadratic `g² = h g + 1`. `runCoeff 0 = 1`, `runCoeff 1 = z`,
`runCoeff (e+2) = h · runCoeff (e+1) + runCoeff e`. -/
def runCoeff (h z : R) : ℕ → R
  | 0 => 1
  | 1 => z
  | e + 2 => h * runCoeff h z (e + 1) + runCoeff h z e

@[simp] theorem runCoeff_zero (h z : R) : runCoeff h z 0 = 1 := rfl
@[simp] theorem runCoeff_one (h z : R) : runCoeff h z 1 = z := rfl
theorem runCoeff_two (h z : R) : runCoeff h z 2 = h * z + 1 := by
  simp [runCoeff]

/-- **A run of one generator stabilises.** Under the Hecke quadratic at level `m`,
`tr (x · g m ^ e) = runCoeff h z e · tr x` for every `x ∈ H m`. -/
theorem tr_mul_gpow (m : ℕ) (h : R) (hq : T.g m * T.g m = h • T.g m + 1) :
    ∀ (e : ℕ) (x : A), x ∈ T.H m → T.tr (x * T.g m ^ e) = runCoeff h T.z e * T.tr x := by
  have key : ∀ e, (∀ x ∈ T.H m, T.tr (x * T.g m ^ e) = runCoeff h T.z e * T.tr x) ∧
      (∀ x ∈ T.H m, T.tr (x * T.g m ^ (e + 1)) = runCoeff h T.z (e + 1) * T.tr x) := by
    intro e
    induction e with
    | zero =>
      refine ⟨fun x _ => by simp, fun x hx => ?_⟩
      simp only [Nat.zero_add, runCoeff_one, pow_one]
      exact T.markov m x hx
    | succ e ih =>
      refine ⟨ih.2, fun x hx => ?_⟩
      have hsplit : x * T.g m ^ (e + 2) = h • (x * T.g m ^ (e + 1)) + x * T.g m ^ e := by
        have h1 : T.g m ^ (e + 2) = T.g m ^ e * (T.g m * T.g m) := by
          rw [pow_succ, pow_succ, mul_assoc]
        rw [h1, hq, mul_add, mul_one, mul_smul_comm, pow_succ, ← mul_assoc, mul_add,
          mul_smul_comm, ← mul_assoc]
      rw [hsplit, map_add, map_smul, smul_eq_mul, ih.2 x hx, ih.1 x hx]
      simp only [runCoeff]
      ring
  exact fun e => (key e).1

/-- A run `g m ^ e` lies one level up. -/
theorem gpow_mem (m e : ℕ) : T.g m ^ e ∈ T.H (m + 1) := (T.H (m + 1)).pow_mem (T.g_mem m) e

/-- **Runs factorize.** If every generator satisfies the Hecke quadratic, the ascending word
with run length `e m` at level `m` has trace `∏ᵢ runCoeff h z (e (n+i))` — one factor per run. -/
theorem tr_runWord (h : R) (hq : ∀ m, T.g m * T.g m = h • T.g m + 1) (e : ℕ → ℕ) (n k : ℕ) :
    T.tr (stabWord (fun m => T.g m ^ e m) n k)
      = ∏ i ∈ Finset.range k, runCoeff h T.z (e (n + i)) :=
  tr_stabWord_prod T _ (fun m => runCoeff h T.z (e m)) (fun m => gpow_mem T m (e m))
    (fun m x hx => tr_mul_gpow T m h (hq m) (e m) x hx) n k

/-! ## Contrast with the interleaved word -/

/-- The sequential word `g₀² g₁² g₂` of `MarkovTraceInterleavedCrossTerm` *is* the monotone
run-word with run lengths `(2, 2, 1)`. -/
theorem sequential_eq_runWord :
    T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2
      = stabWord (fun m => T.g m ^ (if m = 2 then 1 else 2)) 0 3 := by
  simp [stabWord, pow_two]

/-- The sequential trace, re-derived from the general factorization: `(hz+1)·(hz+1)·z`. -/
theorem tr_sequential_via_factorization (h : R) (hq : ∀ m, T.g m * T.g m = h • T.g m + 1) :
    T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2) = (h * T.z + 1) * (h * T.z + 1) * T.z := by
  rw [sequential_eq_runWord T, tr_runWord T h hq]
  simp [Finset.prod_range_succ, runCoeff_two]

/-- **Same content, different order.** The interleaved word `g₀ g₁ g₀ g₂ g₁` has exactly the
per-generator content of the monotone run-word `(2, 2, 1)`; its trace is that word's factorized
trace **plus** the cross term `z (z² − h z − 1)`. Monotone ordering is the hypothesis under
which the product formula holds, and dropping it is what lets the cross term appear. -/
theorem content_reorder_defect (h : R) (hq : ∀ m, T.g m * T.g m = h • T.g m + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1)
      = (∏ i ∈ Finset.range 3, runCoeff h T.z (if i = 2 then 1 else 2))
        + T.z * (T.z ^ 2 - h * T.z - 1) := by
  have hd := interleaved_sub_sequential T h (hq 0) (hq 1) hbraid
  rw [sequential_eq_runWord T, tr_runWord T h hq] at hd
  have : ∀ i ∈ Finset.range 3, runCoeff h T.z (if 0 + i = 2 then 1 else 2)
      = runCoeff h T.z (if i = 2 then 1 else 2) := fun i _ => by simp
  rw [Finset.prod_congr rfl this] at hd
  linear_combination hd

/-! ## The production pn letter at convention D -/

/-- The deuteron bond letter of `atom_braid_word_3A` is `σ − (h/2)·1` (`c = 1`, `d = −h/2`). Its
letter trace `z − h/2` at convention D is `(q⁴ + 1) / (2 q (q² + 1))`. -/
theorem pnLetterTrace_convD {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h2' : (2 : K) ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) / 2 = (q ^ 4 + 1) / (2 * q * (q ^ 2 + 1)) := by
  field_simp
  ring

end QOU.MathlibExt.MonotoneWordFactorizes
