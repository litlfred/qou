import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# The cube-moment lower bound — step (C) of the tower growth bound, unconditionally

`QOU/Mass/LevelSelectionLogarithmic.lean` proves the level-selection consequences
**conditional on** the class `TowerGeometricLowerBound`, and states the blocker:

> "The combinatorial core — a super-exponential lower bound on `w_std(k)` — is
> **not** proved here: a faithful proof needs SYT + skew-tableau +
> Plancherel-measure Mathlib infrastructure that does not yet exist (a
> multi-session build)."

That is true of the *whole* chain, but not of every link in it. The chain in
`computations/deltalambda/wlambda_wstd_superexp_lower_bound.py` is (A) a branching
identity, (B) an exact Plancherel identity, (C) a cube-moment lower bound, (D) a
transfer inequality. **Step (C) needs no tableau theory at all** — it is the
elementary "max dominates the root-mean-square" argument:

    Σ_λ (f^λ)³  ≥  (max_λ f^λ)³  ≥  (k!/p(k))^{3/2},

using only that the `f^λ` are non-negative, that there are `p(k)` of them, and
that `Σ_λ (f^λ)² = k!`. The tableau content sits entirely in that *input identity*
(RSK/Burnside), not in the inequality.

This file proves (C) abstractly, so the open premise shrinks from "a
super-exponential lower bound on `w_std`" to "the RSK/Burnside identity
`Σ_λ (f^λ)² = k!`, plus step (D)". It does **not** close
`TowerGeometricLowerBound` and supplies no instance.

## Statement, and why it is polynomial

Radicals are avoided by squaring: with `M = Σ f²` and `P = card`,

    M³  ≤  (Σ f³)² · P³        (`sum_sq_pow_three_le`)

is equivalent to the corpus's `Σ f³ ≥ (M/P)^{3/2}` but stays inside `ring`/`nlinarith`
reach — no `Real.rpow`, no `Real.sqrt`, no side conditions about branch cuts.
Instantiated at `M = k!`, `P = p(k)` it gives `(Σ (f^λ)³)² ≥ (k!)³/p(k)³`, i.e.
exactly `Σ (f^λ)³ / k! ≥ √(k!)/p(k)^{3/2}`, the corpus's form.

## What remains open (unchanged by this file)

* the input identity `Σ_λ (f^λ)² = k!` — the RSK/Burnside target
  (`QOU/Mathlib/RSKBurnsideTarget.lean`);
* step (D), the transfer `w_std(k) ≥ 𝔼_Planch[f^{λ/(3)}]`, which the source
  script calls "the one remaining clean Lean sub-goal";
* hence `TowerGeometricLowerBound` itself, which still has **no instance**.

Per AGENTS.md §"Axiomatization is NOT a Proof": proving one link does not
establish the chain, and this file claims only the link.

## Base ring (§7c)

`ℝ`: an inequality between real sums, archimedean by nature.

-- Ref: [leitner2026] computations/deltalambda/wlambda_wstd_superexp_lower_bound.py
-- Ref: [stanley1999] https://doi.org/10.1017/CBO9780511609589
-/

namespace QOU.Mass

open Finset

/-- **Step (C), abstractly.** For non-negative `f` on a finite nonempty index type,

    (Σ f²)³ ≤ (Σ f³)² · (card)³.

Equivalently `Σ f³ ≥ ((Σ f²)/card)^{3/2}` — the "max dominates the
root-mean-square" bound, stated polynomially so no radicals appear.

The proof is two elementary facts: the sum of squares is at most `card` times the
largest square, and the sum of cubes is at least the largest cube. -/
theorem sum_sq_pow_three_le {ι : Type*} [Fintype ι] [Nonempty ι]
    (f : ι → ℝ) (hf : ∀ i, 0 ≤ f i) :
    (∑ i, f i ^ 2) ^ 3 ≤ (∑ i, f i ^ 3) ^ 2 * (Fintype.card ι : ℝ) ^ 3 := by
  obtain ⟨i₀, -, hmax⟩ := Finset.exists_max_image (univ : Finset ι) f univ_nonempty
  set m : ℝ := f i₀ with hm
  have hm0 : 0 ≤ m := hf i₀
  -- every square is at most the largest square
  have hsq : ∑ i, f i ^ 2 ≤ (Fintype.card ι : ℝ) * m ^ 2 := by
    calc ∑ i, f i ^ 2 ≤ ∑ _i : ι, m ^ 2 :=
          Finset.sum_le_sum (fun i _ => pow_le_pow_left₀ (hf i) (hmax i (mem_univ i)) 2)
      _ = (Fintype.card ι : ℝ) * m ^ 2 := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  -- the sum of cubes dominates the largest cube
  have hcube : m ^ 3 ≤ ∑ i, f i ^ 3 :=
    Finset.single_le_sum (f := fun i => f i ^ 3)
      (fun i _ => pow_nonneg (hf i) 3) (mem_univ i₀)
  have hS2 : (0 : ℝ) ≤ ∑ i, f i ^ 2 :=
    Finset.sum_nonneg (fun i _ => pow_nonneg (hf i) 2)
  have hc0 : (0 : ℝ) ≤ (Fintype.card ι : ℝ) := Nat.cast_nonneg _
  -- cube the square bound
  have h1 : (∑ i, f i ^ 2) ^ 3 ≤ ((Fintype.card ι : ℝ) * m ^ 2) ^ 3 :=
    pow_le_pow_left₀ hS2 hsq 3
  -- and square the cube bound
  have h2 : (m ^ 3) ^ 2 ≤ (∑ i, f i ^ 3) ^ 2 :=
    pow_le_pow_left₀ (pow_nonneg hm0 3) hcube 2
  have hexp : ((Fintype.card ι : ℝ) * m ^ 2) ^ 3
      = (Fintype.card ι : ℝ) ^ 3 * (m ^ 3) ^ 2 := by ring
  calc (∑ i, f i ^ 2) ^ 3
      ≤ ((Fintype.card ι : ℝ) * m ^ 2) ^ 3 := h1
    _ = (Fintype.card ι : ℝ) ^ 3 * (m ^ 3) ^ 2 := hexp
    _ ≤ (Fintype.card ι : ℝ) ^ 3 * (∑ i, f i ^ 3) ^ 2 :=
        mul_le_mul_of_nonneg_left h2 (pow_nonneg hc0 3)
    _ = (∑ i, f i ^ 3) ^ 2 * (Fintype.card ι : ℝ) ^ 3 := by ring

/-- **The corpus's instantiation.** With the sum of squares pinned to `M` (for the
tower: `M = k!`, the RSK/Burnside identity) and `P = card` the number of index
values (`P = p(k)`, the partition count), the cube moment obeys
`M³ ≤ (Σ f³)² · P³`.

`M` and `P` enter as hypotheses; supplying them for the Plancherel tower is the
open RSK/Burnside work, not done here. -/
theorem cube_moment_lower_bound {ι : Type*} [Fintype ι] [Nonempty ι]
    (f : ι → ℝ) (hf : ∀ i, 0 ≤ f i) {M P : ℝ}
    (hM : ∑ i, f i ^ 2 = M) (hP : (Fintype.card ι : ℝ) = P) :
    M ^ 3 ≤ (∑ i, f i ^ 3) ^ 2 * P ^ 3 := by
  subst hM; subst hP; exact sum_sq_pow_three_le f hf

/-- **Step (D) does not need to be sharp.** The source script uses the transfer
inequality in its sharp form `w_std ≥ 𝔼[f^{λ/(3)}]` (i.e. `ε = 1`) to reach
`w_std ≥ T/4`, where `T = Σ (f^λ)³/k!` is the cube moment and `T = 2·w_std + 2·b`
is the exact Plancherel identity (B).

But **any** positive ratio bound suffices. If `ε·b ≤ a` for some `ε > 0` then
`a ≥ (ε / (2(1+ε)))·T`, and since `T` is super-exponential by
`sum_sq_pow_three_le`, so is `a` — the constant is irrelevant to the growth
conclusion.

This matters for what has to be proved. Sharp (D) is a genuinely
measure-theoretic statement: it is **false pointwise** (at a single-row `λ = (k)`,
`f^{λ/(3)} = 1` while `f^{λ/(2,1)} = 0`), so it cannot be obtained by a
tableau-by-tableau argument. Establishing it only up to *some explicit constant*
is a strictly weaker target, and the measured ratio `a/b` runs `4.00 → 2.04` over
`k = 3..12` — so there is better than a factor-2 margin to spend. -/
theorem cube_moment_le_of_ratio_bound {a b T ε : ℝ}
    (hε : 0 < ε) (hT : T = 2 * a + 2 * b) (hab : ε * b ≤ a) :
    (ε / (2 * (1 + ε))) * T ≤ a := by
  have h1 : (0 : ℝ) < 1 + ε := by linarith
  rw [hT, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [hab, hε.le]

/-- **The character form of the weakening — `Cov ≤ 0` is far more than is needed.**

`docs/audits/2026-07-18-deltalambda-D-reduction-content-covariance.md` reduces (D)
rigorously, via `S_k` character identities and the Jucys–Murphy content formula, to

    a = (T₁ − T₃)/3 ,   b = (T₁ + 2·T₃)/6      (using `T₂ = 0` exactly),

with `T₁ = Σ (f^λ)³`, `T₃ = Σ (f^λ)²·χ^λ(3-cycle)`, and concludes

    (D)  ⟺  4·T₃ ≤ T₁  ⟸  T₃ ≤ 0  ⟺  Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0.

Combined with `cube_moment_le_of_ratio_bound`, **the covariance inequality is not
what has to be proved.** Any `c < 1` with `T₃ ≤ c·T₁` yields a positive ratio
bound with `ε = 2(1−c)/(1+2c)`, which is all the growth conclusion consumes.

The slack is large. Measured `T₃/T₁` runs `−0.200 → −0.007` over `k = 3..12`,
against a requirement of merely `< 1` — roughly two orders of magnitude of room at
`k = 12`. And the trivial character bound `|χ^λ(3-cycle)| ≤ f^λ` already gives
`T₃ ≤ T₁`; what is missing is only a *quantitative* gap below `1`, which the
extremal shapes cannot obstruct since `λ = (k)` and `λ = (1ᵏ)` — the only shapes
attaining the ratio `1` — have `f^λ = 1` and so contribute `±1` against a `T₁`
that is super-exponential.

The identity below is the bridge; the `c < 1` bound itself is **not** proved here. -/
theorem ratio_bound_of_T3_le {T₁ T₃ a b c : ℝ}
    (hc2 : -(1:ℝ)/2 < c) (h3 : T₃ ≤ c * T₁)
    (ha : a = (T₁ - T₃) / 3) (hb : b = (T₁ + 2 * T₃) / 6) :
    (2 * (1 - c) / (1 + 2 * c)) * b ≤ a := by
  have hden : (0:ℝ) < 1 + 2 * c := by linarith
  subst ha; subst hb
  rw [div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [h3, hden]

/-- **The extremal split — where the explicit `c < 1` comes from.**

Write `T₃ = Σ_λ (f^λ)³·r(λ)` with `r(λ) = χ^λ(3-cycle)/f^λ`, so `|r| ≤ 1`. Only
two shapes attain `r = 1`: the single row `λ = (k)` and the single column
`λ = (1ᵏ)` (the Jucys–Murphy content formula gives exactly `1` there). Both have
`f^λ = 1`, so together they carry mass `M = 2` — while `T₁` is super-exponential.

Splitting them off, `T₃ ≤ M + ρ·(T₁ − M)` where `ρ = max r` over the remaining
shapes. This lemma is the consequence: **any** `ρ < 1` and `M < T₁` force
`T₃ < T₁`, with the explicit constant `c = (M + ρ(T₁ − M))/T₁`.

Crucially `ρ` may depend on `k`. The second-largest content spread sits at
`λ = (k−1, 1)` (and its conjugate), where the gap in `Σ_□ c(□)²` against the
single row is exactly `(k−1)² − 1`, giving

    ρ = 1 − 3/(k−1)

— verified against direct enumeration for `k = 4..14`. That decays only
polynomially, and `T₁` grows super-exponentially, so the resulting
`ε ≍ 4/(3(k−1))` is absorbed without loss: `a ≳ T₁/k` is still
super-exponential. A *uniform* `c < 1` is not needed.

**`hρ` is supplied by the literature (bean `qou-mcgt`).** The hypothesis — that
every non-extremal shape has `r(λ) ≤ ρ < 1` — is the statement that the normal
Cayley graph on `S_k` generated by the full **3-cycle conjugacy class** has the
**Aldous property**: its strictly second-largest eigenvalue is attained by the
standard representation `(k−1,1)`. That equivalence is forced by the
Jucys–Murphy identity, which makes `C₂(λ) = C(k,2) +` (eigenvalue of the 3-cycle
class sum), so maximising `C₂` *is* maximising `χ^λ(3-cycle)/f^λ`.

Two independent citations give it:

* **Li–Xia–Zhou**: for a **single conjugacy class** `S`, `Cay(S_k, S)` has the
  Aldous property **iff** `2 ≤ |supp(σ)| ≤ k−2`. The 3-cycles are a single class
  with `|supp| = 3`, so this applies for `k ≥ 5`.
* **Lv–Zhou, Thm 1.3(a)** (arXiv:2607.29018): if `O(S) = ∅` then `Cay(S_k, S)`
  has the Aldous property. Every 3-cycle is **even**, so `O(S) = ∅`.

Their Corollary 1.5 gives the eigenvalue in closed form for `S ⊆ A_k` with
`2 ≤ |supp| ≤ k−2`, namely `λ₂ = (Σ_σ|fix σ| − |S|)/(k−1)`. For the 3-cycle class
(`|S| = k(k−1)(k−2)/3`, `fix = k−3`) this is `λ₂/λ₁ = (k−4)/(k−1) = 1 − 3/(k−1)`
— exactly `ρ`, confirmed against direct enumeration for `k = 5..24`.

**Residual caveat, and it is real.** Both results are stated for *sufficiently
large* `k`; neither gives `N` explicitly in the statements read. Direct
enumeration covers `k ≤ 24` and the closed formula matches at every one, so any
gap is confined to a window above 24 — but the constant is not pinned here, and
`hρ` is therefore left as an explicit hypothesis rather than discharged. -/
theorem T3_lt_of_extremal_split {T₁ T₃ ρ M : ℝ}
    (hMT : M < T₁) (hρ : ρ < 1)
    (hsplit : T₃ ≤ M + ρ * (T₁ - M)) :
    T₃ < T₁ := by
  have hpos : 0 < T₁ - M := by linarith
  nlinarith [hsplit, hpos, hρ]

/-- The explicit constant produced by the split, packaged for
`ratio_bound_of_T3_le`: `T₃ ≤ c·T₁` with `c < 1`. -/
theorem T3_le_explicit_c {T₁ T₃ ρ M : ℝ}
    (hT1 : 0 < T₁) (hMT : M < T₁) (hρ : ρ < 1)
    (hsplit : T₃ ≤ M + ρ * (T₁ - M)) :
    ∃ c : ℝ, c < 1 ∧ T₃ ≤ c * T₁ := by
  refine ⟨T₃ / T₁, ?_, ?_⟩
  · rw [div_lt_one hT1]
    exact T3_lt_of_extremal_split hMT hρ hsplit
  · rw [div_mul_cancel₀ _ hT1.ne']

/-- **Non-vacuity, and sharpness.** The bound is attained when the mass sits on a
single index: `f = 1` at one point of a one-element type gives `1 ≤ 1`. -/
example : (∑ _i : Fin 1, (1 : ℝ) ^ 2) ^ 3
    ≤ (∑ _i : Fin 1, (1 : ℝ) ^ 3) ^ 2 * (Fintype.card (Fin 1) : ℝ) ^ 3 := by
  simp

end QOU.Mass
