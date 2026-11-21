/-
# Pin-robustness of ratio observables — the generalized Habiro finding, as lemmas

**Sibling to the `BWVacuumRow*` keystone carriers — this file does NOT edit them.** Formal core of
the μ–p pin-sensitivity map (`computations/mu_p_pin_sensitivity_map.py`, PR #3847).

## Context

The μ–p substrate tension is an 11.5 ppb disagreement between the **proton** and **muon** pins of the
substrate modulus `q₀`. The relative pin-sensitivity `S(O) = d(log O)/d(log q₀)` of the canonical
mass chain (`m_μ = m_e·Vol(4₁)/ℏ_q²`, `m_p = 2(m_μ·F_Bor − 6m_e)`, …) **concentrates in the absolute
muon anchor** `ℏ_q⁻² = ((q−1)/q)⁻²`:

* `S(m_μ) = −2/(q−1) ≈ −18.2`  (exact; anchor amplification `1/(q−1) ≈ 9.1`),
* `S(m_p) ≈ −21`, `S(m_n) ≈ −21`  (inherit the anchor),
* but every dimensionless **ratio** that shares that anchor factor has it **cancel**:
  `S(m_p/m_μ) ≈ −2.8`, `S(m_n/m_p) ≈ +0.03`, and the McKay `W_λ` q-Verlinde measure `S ≈ 0.19`.

So the McKay / `W_λ` keystone route (#3830) is **blind** to the μ–p tension: no ratio observable can
adjudicate an 11.5 ppb split that lives entirely in the absolute anchor. This is the generalized,
quantified form of the #3830 Habiro pin-robustness finding.

## What this file proves (sorry-free)

The logarithmic derivative (`logDeriv`, the pin-sensitivity up to the ubiquitous `q` factor) of a
ratio `(h·a)/(h·b)` is **independent of the shared factor `h`** — the anchor cancels. In particular a
ratio of two pure multiples of the anchor is **pin-constant** (`logDeriv = 0`). These are the exact
structural extremes; the *approximate* real case (`m_p` carries a small `−12 m_e` term that breaks
exact anchor-homogeneity, leaving the `−2.8` residual) is quantified numerically in the witness.

The abstract hypothesis `∀ x, h x ≠ 0` (resp. `anchor x ≠ 0`) is exactly satisfied by the physical
anchor `ℏ_q⁻² = (q/(q−1))²` on the substrate ray `q > 1` (where `q₀ ≈ 1.11` lives): there it is a
strictly positive unit, so the ratio identity holds throughout the physical domain.

## What this file does NOT do

It does **not** resolve the μ–p tension (scope-(a) per AGENTS.md refute-honestly: the tension lives in
the absolute anchor, which no ratio sees) and wires nothing to production. It formalizes **why** the
`W_λ` route is pin-blind — a structural fact, not a closure of Subgoal-2.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-17-mu-p-pin-sensitivity-map.md
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Tactic

namespace QOU.BraidKnot.Keystone

/-- **Shared-factor cancellation (pure function identity).** A ratio `(h·a)/(h·b)` equals `a/b`
wherever the shared factor `h` is nonzero — the anchor cancels. Stated over any field, pointwise. -/
theorem ratio_shared_factor_eq {𝕜 : Type*} [Field 𝕜]
    (h a b : 𝕜 → 𝕜) (hh : ∀ x, h x ≠ 0) :
    (fun x => (h x * a x) / (h x * b x)) = (fun x => a x / b x) := by
  funext x
  exact mul_div_mul_left (a x) (b x) (hh x)

/-- **Pin-sensitivity of a ratio is anchor-independent.** The logarithmic derivative of the ratio
`(h·a)/(h·b)` equals that of `a/b`: the shared factor `h` — e.g. the absolute anchor `ℏ_q⁻²` — makes
**zero** contribution to the ratio's pin-sensitivity. This is the generalized Habiro pin-robustness:
`W_λ` and every mass ratio, sharing the anchor, are blind to it. -/
theorem logDeriv_ratio_indep_of_shared_factor
    (h a b : ℝ → ℝ) (hh : ∀ x, h x ≠ 0) :
    logDeriv (fun x => (h x * a x) / (h x * b x)) = logDeriv (fun x => a x / b x) := by
  rw [ratio_shared_factor_eq h a b hh]

/-- **A ratio of two pure-anchor observables is pin-CONSTANT.** If `f = c₁·anchor` and
`g = c₂·anchor` (both proportional to the same anchor — e.g. two `ℏ_q⁻²`-masses), the ratio has zero
logarithmic derivative everywhere the anchor is a unit: perfect pin-robustness. The μ–p tension, which
lives in `anchor` itself, is invisible in any such ratio. -/
theorem logDeriv_pure_anchor_ratio_eq_zero
    (anchor : ℝ → ℝ) (c₁ c₂ : ℝ) (hanchor : ∀ x, anchor x ≠ 0) :
    logDeriv (fun x => (c₁ * anchor x) / (c₂ * anchor x)) = 0 := by
  have hfun : (fun x => (c₁ * anchor x) / (c₂ * anchor x)) = (fun _ => c₁ / c₂) := by
    funext x
    exact mul_div_mul_right c₁ c₂ (hanchor x)
  rw [hfun]
  funext x
  simp [logDeriv]

/-- The absolute muon anchor's `ℏ_q⁻²` factor, `(q/(q−1))²` (`= 1/ℏ_q²`, `ℏ_q = (q−1)/q`). It is the
sole carrier of the large pin-sensitivity `S = 2/(q−1)`. On the substrate ray `q > 1` it is a
strictly positive unit — the hypothesis the pin-robustness lemmas require. -/
noncomputable def hbarInvSq (q : ℝ) : ℝ := (q / (q - 1)) ^ 2

theorem hbarInvSq_pos {q : ℝ} (hq : 1 < q) : 0 < hbarInvSq q := by
  have h1 : (0 : ℝ) < q - 1 := by linarith
  have hq0 : (0 : ℝ) < q := by linarith
  simp only [hbarInvSq]
  positivity

end QOU.BraidKnot.Keystone
