# Mass-gap three-step program — substrate gap → ε³ lemma → obstruction theorem

**Date:** 2026-06-11 · **Owner direction:** session discussion (two routes
assessed; converged on the program below) · **Status:** workplan (no step
started)

## 0. Context and the resolved dichotomy

Two candidate routes were proposed for making the
[`conj:yang-mills-mass-gap`](../../content/quantum-observable-universe/models-of-qous/yang-mills-mass-gap.md)
claim rigorous:

- **Route 1** — prove the gap at |q| ≠ 1, then transfer it through q → 1
  (crystal-basis / surreal limit techniques).
- **Route 2** — show the q → 1 limit hits the same H²(𝒮, 𝔾ₘ) Kummer
  obstruction class (χ(A) = −6) that the NS and P≠NP formulations use.

These are **opposite branches of one dichotomy**, not two implementations:
a successful gap transfer would falsify the obstruction. The framework is
committed to the obstruction branch three ways: the gap function vanishes
on μ₂ ⊂ 𝔾ₘ (stated in the conjecture block); the classical-limit
obstruction persists at all primes > 3; and the substrate sits at
q₀ ≈ 1.11, never at 1. Route 1 executed honestly at the limit point
*computes* the obstruction rather than evading it — hence the unified
program below.

**Direct computation (2026-06-11).** The exploratory probe
[`q1_mass_gap_probe.py`](../../folio-assistant/computations/q1_mass_gap_probe.py)
(witness `q1-mass-gap-probe.witness.json`) evaluated the tower at
q ∈ {q₀, …, 1.000001, 1}:

| quantity | q → 1 behaviour |
|---|---|
| Plancherel weight tower w_λ(q) = [n]_q!/H_q(λ)², n = 3..6 | **survives** — all weights positive at q = 1, level structure intact |
| accidental degeneracies | n = 6 has 6 distinct levels at q₀ but **5 at q = 1** — the deformation resolves the classical (5,1)/(3,3) same-dimension coincidence; resolution is lost at the classical point |
| crossing energy E_×(q) = (q − q⁻¹)/2 | **dies** — exactly 0 |
| categorical gap bound Δ_q = ½(q − q⁻¹)(q − 1)² | **dies** — ~ h³, h = q − 1 |
| physical-units gap Δ_q/ℏ_q² | **dies** — exact identity **½·q·(q−1)·(q+1)**, ~ h (the 1/ℏ_q² normalization buys back two powers of h, not three) |

Verdict: at q = 1 the mass tower End(Aₙ) is structurally intact but
**massless**. The gap is deformation-induced and does not survive the
limit in either normalization. This is the computational shadow of the
μ₂-vanishing statement and pins the program to the obstruction branch.

## 1. Step 1 — substrate gap theorem (the shared keystone)

> **Target.** At fixed q > 1 (later |q| ≠ 1), every non-vacuum excitation
> of the categorical transfer matrix on End(Aₙ) has mass ≥ Δ_q > 0,
> **uniformly in n**.

Sub-tasks, in order:

1. **S1a (fixed n, formal anchor).** Lean statements for positivity of the
   crossing-energy bound and the exact physical-units identity — skeleton
   in §4 below. Effort: small; lands when an LSP-capable session is
   available (sandbox elan is currently network-blocked).
2. **S1b (identify the right operator).** The probe shows the *Plancherel
   weight* minimal level separation shrinks with n (0.5 → 0.125 → 0.075 →
   0.0264 for n = 3..6): raw weight separations do NOT give a uniform
   bound. The gap statement must be about the **transfer matrix** 𝒯_q
   (excitation energies), not weight separations. Deliverable: a
   definition block pinning 𝒯_q's spectrum to the crossing-energy
   filtration, so "gap" has one meaning across the corpus.
3. **S1c (uniformity in n).** Candidate strategies, in preference order:
   (i) Wenzl/Jones-tower positivity — the inclusion H_n ⊂ H_{n+1} with
   conditional expectation transports the spectral bound up the tower;
   (ii) Perron–Frobenius structure of 𝒯_q on the positive cone;
   (iii) min-energy-per-crossing counting: every non-trivial excitation
   carries ≥ 1 crossing, and crossings contribute additively ≥ E_×(q).
   Semisimplicity for q not a root of unity (substrate axiom) is the
   standing hypothesis. This is the hard step; treat as research-grade.

## 2. Step 2 — the ε³ lemma (surreal formalization; small)

> **Target.** In `SurrealRateCalculus`, at q = 1 + ε (ε a positive
> infinitesimal): Δ_q = ε³(1 + O(ε)) and Δ_q/ℏ_q² = ε + 3⁄2·ε² + O(ε³).
> Standard parts are 0: **no standard positive gap arises from this
> mechanism at the classical point.**

This formalizes "the gap dies at third order (categorical) / first order
(physical)" and is the bridge lemma: route 1's machinery proving route 2's
content. The exact identity Δ_q/ℏ_q² = ½q(q−1)(q+1) (probe-verified,
assert-checked) makes the physical-units half a polynomial computation.

## 3. Step 3 — the obstruction theorem (route 2 proper)

> **Target.** Make rigorous the reduction asserted in the conjecture
> block: the mass-gap classical limit and the classical-limit obstruction
> both reduce to divisibility of χ(A) = −6 in the Kummer tower of
> H²(𝒮, 𝔾ₘ); corollaries instantiate the same class for the NS and
> P≠NP formulations (`fluid-dynamics/`, `information-theory/`).

**Universality caveat (must accompany every artifact of step 3).** The
obstruction proves *the QOU framework's* classical limit fails — NOT that
standard q = 1 Yang–Mills (Wightman-axiomatized, on ℝ⁴) does not exist.
Promotion to a Millennium-relevant counterexample would additionally
require a universality theorem ("any axiomatized YM with a gap yields a
QOU-type structure"), which does not exist. Until then every statement is
framework-conditional. Publication, if any, is per-problem and
conditional — never as a unified multi-problem claim.

## 4. Lean keystone skeleton (S1a)

Lands under `qou:QOU.BraidKnot.*` once an LSP session is available; kept
here (not as a `.lean` file) so CI stays green meanwhile. Generic-R per
CLAUDE.md §7c is not available — ordering (`1 < q`) forces ℝ.

```lean
namespace QOU.BraidKnot

/-- Crossing energy `E_×(q) = (q − q⁻¹)/2`. -/
noncomputable def crossingEnergy (q : ℝ) : ℝ := (q - q⁻¹) / 2

/-- Categorical mass-gap lower bound `Δ_q = E_×(q) · (q − 1)²`. -/
noncomputable def gapBound (q : ℝ) : ℝ := crossingEnergy q * (q - 1) ^ 2

/-- Keystone, fixed n: the bound is strictly positive for `1 < q`. -/
theorem gapBound_pos {q : ℝ} (hq : 1 < q) : 0 < gapBound q := by
  -- Ref: [manuscript] models-of-qous/yang-mills-mass-gap.md
  sorry

/-- Exact physical-units identity `Δ_q/ℏ_q² = ½·q·(q−1)·(q+1)`,
    `ℏ_q = (q−1)/q` (probe-verified, q1_mass_gap_probe.py). -/
theorem gapBound_div_hbarSq {q : ℝ} (h0 : q ≠ 0) (h1 : q ≠ 1) :
    gapBound q / ((q - 1) / q) ^ 2 = q * (q - 1) * (q + 1) / 2 := by
  -- Ref: [manuscript] q1-mass-gap-probe.witness.json exact_identities
  sorry

/-- Vanishing at the classical point (μ₂-vanishing, computational shadow). -/
theorem gapBound_at_one : gapBound 1 = 0 := by
  -- Ref: [manuscript] models-of-qous/yang-mills-mass-gap.md §G_m-torsion
  sorry

/-- Uniform-in-n gap, conditional form (§3b-cond conditional-class
    pattern), parametrized by the level-n excitation spectrum; S1b pins
    `spectrum` to the transfer-matrix `𝒯_q` excitation energies. -/
class SubstrateGap (q : ℝ) (spectrum : ℕ → Set ℝ) : Prop where
  one_lt : 1 < q
  gap_uniform : ∀ n : ℕ, ∀ E ∈ spectrum n, E ≠ 0 → gapBound q ≤ E

end QOU.BraidKnot
```

## 5. Priorities and coordination

| # | item | size | depends on | priority |
|---|---|---|---|---|
| 1 | S1a Lean skeleton lands + compiles | S | LSP session | **P1** |
| 2 | Step 2 ε³ lemma in SurrealRateCalculus | S | S1a | **P1** |
| 3 | S1b transfer-matrix definition block | M | — | **P2** |
| 4 | Step 3 obstruction-reduction theorem | L | S1b | **P2** |
| 5 | S1c uniformity in n | XL (research) | S1b | **P3** |

Coordination: Lean modules overlap the active HeckeAlgebra/lean-repair
branches (#2094, #2095, #2108) — post intent before S1a lands; the
n = 6 degeneracy-resolution observation may interest the metallic-regime
and qbeta threads (informational only).
