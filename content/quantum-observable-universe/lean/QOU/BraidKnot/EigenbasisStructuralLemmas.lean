import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Tactic
import QOU.BraidKnot.ChiralityWritheRibbon

/-!
# QOU.BraidKnot.EigenbasisStructuralLemmas — content/twist eigenbasis lemmas

Lean formalization of the structural lemmas of the **content/twist
eigenbasis**, verified exact-symbolic in
`computations/probes/eigenbasis_structural_lemmas_probe.py` (PR #2502) and
flagged there for Lean follow-up (`lean_followup`).

The eigenbasis is organized by the **ribbon-twist eigenvalue**
`θ_λ = q^{2c(λ)}`: the full twist `Δ² ∈ Z(H_n(q))` acts on the Wedderburn
channel `V_λ` by the scalar `θ_λ`, formalized as the class
[`QOU.BraidKnot.ChiralityWritheRibbon.RibbonTwistEigenvalue`].  This file
proves the lemmas **sorry-free** over `ℝ` importing only Mathlib; the
connection of the abstract framing ratio `θ` to the categorical
`q^{2κ_λ}` is `framing_eigenvalue_pow` below.

## Lemmas

- **L3 — framing generating function** (this file): the framing tower
  `Σ_m t^m χ_λ(β·Δ^{2m})` is the single-pole rational `χ_λ(β)/(1 − t·θ_λ)`.

LaTeX / witness: probe `eigenbasis-structural-lemmas`, lemma L3.

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] braids-and-knots / eigenbasis structural lemmas (PR #2502)
-/

namespace QOU.BraidKnot.EigenbasisStructuralLemmas

open Finset QOU.BraidKnot.ChiralityWritheRibbon

/-! ## L3 — framing generating function -/

/-- **Ribbon power law.**  The eigenvalue of the `m`-fold full twist
`Δ^{2m}` on the channel `V_λ` is the `m`-th power of the single-twist
eigenvalue `θ_λ = q^{2κ_λ}`:

  `q^{2mκ} = (q^{2κ})^m`.

This is the algebraic content linking the `m`-fold framing to the ribbon
eigenvalue; it holds for every real base (the `zpow` identity is valid in a
`GroupWithZero`). -/
theorem framing_eigenvalue_pow (q : ℝ) (κ : ℤ) (m : ℕ) :
    q ^ (2 * (m : ℤ) * κ) = (q ^ (2 * κ)) ^ m := by
  rw [show 2 * (m : ℤ) * κ = (2 * κ) * (m : ℤ) by ring, zpow_mul, zpow_natCast]

/-- **L3 — framing generating function (finite closed form).**

Let `c m = χ_λ(β · Δ^{2m})` be the Hecke character of the braid `β` framed
by `m` full twists, in Wedderburn channel `λ`.  Centrality of the full
twist `Δ² ∈ Z(H_n(q))` together with the ribbon eigenvalue
`Δ²|_{V_λ} = θ` (`θ = q^{2c(λ)}`, `framing_eigenvalue_pow`) gives the
one-step scaling `c (m+1) = θ · c m`.  Then the framing generating function
is the **single-pole rational** `c 0 / (1 − t·θ)`: the partial sums satisfy
the finite geometric closed form

  `(1 − t·θ) · Σ_{m<N} t^m · c m = c 0 · (1 − (t·θ)^N)`,

so the only pole is at `t = θ⁻¹ = q^{−2c(λ)}`.  The result is **not**
vacuous: it pins the framing tower as geometric with ratio `t·θ` and
leading coefficient `c 0`, which is the substance of the eigenbasis
reframing (the framing tower separates orders by content). -/
theorem framing_gf_closed_form
    (θ t : ℝ) (c : ℕ → ℝ)
    (hstep : ∀ m, c (m + 1) = θ * c m) (N : ℕ) :
    (1 - t * θ) * (∑ m ∈ range N, t ^ m * c m) = c 0 * (1 - (t * θ) ^ N) := by
  -- The framed characters form a geometric sequence `c m = θ^m · c 0`.
  have hcm : ∀ m, c m = θ ^ m * c 0 := by
    intro m
    induction m with
    | zero => simp
    | succ k ih => rw [hstep, ih]; ring
  -- Pull `c 0` out and collapse `t^m · θ^m = (t·θ)^m`.
  have hsum : (∑ m ∈ range N, t ^ m * c m) = c 0 * ∑ m ∈ range N, (t * θ) ^ m := by
    rw [mul_sum]
    refine sum_congr rfl (fun m _ => ?_)
    rw [hcm, mul_pow]; ring
  -- Geometric-series closed form `(1 − x)·Σ x^m = 1 − x^N` with `x = t·θ`.
  have hgeom : (1 - t * θ) * (∑ m ∈ range N, (t * θ) ^ m) = 1 - (t * θ) ^ N := by
    linear_combination - geom_sum_mul (t * θ) N
  rw [hsum, ← mul_assoc, mul_comm (1 - t * θ) (c 0), mul_assoc, hgeom]

/-- **L3 discharged at the concrete ribbon eigenvalue `θ_λ = q^{2κ}`.**

Instantiating `framing_gf_closed_form` at the framed character
`c m = q^{2mκ}·χ₀` — the action of the `m`-fold full twist `Δ^{2m}` on `V_λ`
through the ribbon eigenvalue `θ_λ = q^{2κ}`
(`QOU.BraidKnot.ChiralityWritheRibbon.RibbonTwistEigenvalue.framing_formula`,
here via `framing_eigenvalue_pow`).  The hypothesis `hstep` is **discharged**
(not assumed): the one-step scaling `q^{2(m+1)κ} = q^{2κ}·q^{2mκ}` is proved.
The framing tower is then the single-pole rational with pole at `t = q^{−2κ}`:

  `(1 − t·q^{2κ}) · Σ_{m<N} t^m · q^{2mκ} · χ₀ = χ₀ · (1 − (t·q^{2κ})^N)`. -/
theorem framing_gf_ribbon (q t χ₀ : ℝ) (κ : ℤ) (N : ℕ) :
    (1 - t * q ^ (2 * κ)) *
        (∑ m ∈ range N, t ^ m * (q ^ (2 * (m : ℤ) * κ) * χ₀))
      = χ₀ * (1 - (t * q ^ (2 * κ)) ^ N) := by
  have hstep : ∀ m, q ^ (2 * ((m + 1 : ℕ) : ℤ) * κ) * χ₀
      = q ^ (2 * κ) * (q ^ (2 * (m : ℤ) * κ) * χ₀) := by
    intro m
    rw [framing_eigenvalue_pow q κ (m + 1), framing_eigenvalue_pow q κ m, pow_succ]
    ring
  have h := framing_gf_closed_form (q ^ (2 * κ)) t
      (fun m => q ^ (2 * (m : ℤ) * κ) * χ₀) hstep N
  simpa using h

/-- **L3 against the `RibbonTwistEigenvalue` class.**  The fullest discharge:
with an actual ribbon-eigenvalue instance `[RibbonTwistEigenvalue q]`, the
framing tower built from the class's own `framing_eigenvalue` is the single-pole
rational, pole at `t = (θ_λ)⁻¹`.  No new hypothesis — `framing_formula` supplies
the eigenvalue and `framing_gf_ribbon` the geometric closure. -/
theorem framing_gf_ribbon_class {q : ℝ} [RT : RibbonTwistEigenvalue q]
    (t χ₀ : ℝ) (κ : ℤ) (N : ℕ) :
    (1 - t * RT.framing_eigenvalue 1 κ) *
        (∑ m ∈ range N, t ^ m * (RT.framing_eigenvalue (m : ℤ) κ * χ₀))
      = χ₀ * (1 - (t * RT.framing_eigenvalue 1 κ) ^ N) := by
  simp only [RT.framing_formula, show (2 * (1 : ℤ) * κ) = 2 * κ by ring]
  exact framing_gf_ribbon q t χ₀ κ N

/-! ## L1 — order-parity = word-length parity -/

/-- **L1 — order-parity = word-length parity.**

Model the Hecke character of a length-`L` braid word `β` in channel `λ` as a
sum over the index paths of the seminormal matrix product,
`χ_λ(β)(q) = Σ_p Π_{i<L} a(p,i)(q)`, where each factor `a(p,i)` is an entry of
one crossing matrix `σ_j` (or `σ_j − h·I`).  Each such factor is an **odd**
Laurent polynomial: its `q ↦ −q` image is its negation (the seminormal
eigenvalues `q, −q⁻¹` and the off-diagonal entries all have odd Laurent
degree, since `q ↦ −q` sends `q^k ↦ (−1)^k q^k`).  Then

  `χ_λ(β)(−q) = (−1)^L · χ_λ(β)(q)`,

equivalently every exponent of the Laurent character has parity `≡ L (mod 2)`.
This makes the PR #2496 parity obstruction a theorem: a same-type-nucleon /
winding tower flips parity because the nucleon word has odd length `L = 11`,
so `11·k` alternates parity in `k`. -/
theorem character_qneg_parity {L : ℕ} {ι : Type*} (paths : Finset ι)
    (a : ι → Fin L → ℝ → ℝ) (q : ℝ)
    (hodd : ∀ p i, a p i (-q) = - a p i q) :
    (∑ p ∈ paths, ∏ i, a p i (-q)) = (-1) ^ L * ∑ p ∈ paths, ∏ i, a p i q := by
  rw [mul_sum]
  refine sum_congr rfl (fun p _ => ?_)
  have hp : (∏ i, a p i (-q)) = ∏ i : Fin L, (-1 : ℝ) * a p i q := by
    refine prod_congr rfl (fun i _ => ?_)
    rw [hodd p i]; ring
  rw [hp, prod_mul_distrib, prod_const, card_univ, Fintype.card_fin]

/-! ## L2 — bar-involution ↔ conjugation duality -/

/-- **L2 — bar-involution ↔ conjugation duality (conditional on the seminormal
bar–conjugate relation).**

The Hecke **bar involution** `q ↦ q⁻¹` swaps the seminormal eigenvalues
`q ↔ −q⁻¹`, which is exactly the intertwiner `V_λ ≅ V_{λ'}` to the
**conjugate** Wedderburn channel `λ'` (transpose partition; `dim V_λ =
dim V_{λ'}`, so the path index sets are in bijection `φ`).  At the level of
matrix entries this is a uniform sign `s ∈ {±1}` and a path bijection `φ` with

  `a_λ(p,i)(q⁻¹) = s · a_{λ'}(φ p, i)(q)`  (the seminormal bar–conjugate input).

From this **factor-level** categorical input the **character-level** duality
follows by reindexing along `φ` and extracting the `L` signs:

  `χ_λ(β)(q⁻¹) = s^L · χ_{λ'}(β)(q)`.

This is the §3b-cond conditional-class shape: the bar–conjugate relation is the
explicit hypothesis; the duality is **derived**, not assumed. -/
theorem character_bar_conjugate {L : ℕ} {ι ι' : Type*} [Fintype ι] [Fintype ι']
    (a : ι → Fin L → ℝ → ℝ) (a' : ι' → Fin L → ℝ → ℝ)
    (q s : ℝ) (φ : ι ≃ ι')
    (hfac : ∀ p i, a p i q⁻¹ = s * a' (φ p) i q) :
    (∑ p, ∏ i, a p i q⁻¹) = s ^ L * ∑ p', ∏ i, a' p' i q := by
  rw [← Equiv.sum_comp φ (fun p' => ∏ i, a' p' i q), mul_sum]
  refine sum_congr rfl (fun p _ => ?_)
  have hp : (∏ i, a p i q⁻¹) = ∏ i : Fin L, s * a' (φ p) i q :=
    prod_congr rfl (fun i _ => hfac p i)
  rw [hp, prod_mul_distrib, prod_const, card_univ, Fintype.card_fin]

/-- **L2 sign corollary.**  With a unit sign `s ∈ {±1}` the duality constant
`ε_λ = s^L` is itself a sign: the bar image of the channel-`λ` character is
`ε_λ` times the conjugate-channel character, `ε_λ ∈ {±1}` (uniformly `−1` at
`n=3`, `+1` at `n=6`, matching the probe's `(−1)^L`). -/
theorem character_bar_conjugate_sign {L : ℕ} {ι ι' : Type*} [Fintype ι] [Fintype ι']
    (a : ι → Fin L → ℝ → ℝ) (a' : ι' → Fin L → ℝ → ℝ)
    (q s : ℝ) (φ : ι ≃ ι') (hs : s = 1 ∨ s = -1)
    (hfac : ∀ p i, a p i q⁻¹ = s * a' (φ p) i q) :
    ∃ ε : ℝ, (ε = 1 ∨ ε = -1) ∧
      (∑ p, ∏ i, a p i q⁻¹) = ε * ∑ p', ∏ i, a' p' i q := by
  refine ⟨s ^ L, ?_, character_bar_conjugate a a' q s φ hfac⟩
  rcases hs with h | h
  · left; rw [h, one_pow]
  · rw [h]
    rcases Nat.even_or_odd L with he | ho
    · left; exact he.neg_one_pow
    · right; exact ho.neg_one_pow

end QOU.BraidKnot.EigenbasisStructuralLemmas
