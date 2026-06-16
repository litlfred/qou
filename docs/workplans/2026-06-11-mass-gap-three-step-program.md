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
[`q1_mass_gap_probe.py`](../../computations/q1_mass_gap_probe.py)
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

**ε-stratification (probe extension, 2026-06-11).** At q = 1 + ε the
surviving structure is stratified by infinitesimal order — this is the
refined target for Step 2 (which is thereby an ε-stratification lemma,
not just the ε³ rate):

| order | what lives there |
|---|---|
| ε⁰ (standard) | semisimple tower; classical Plancherel weights; vacuum level (standard part 1/720 at n = 6) |
| ε¹ | physical-units mass gap ½q(q−1)(q+1); also the categorical Dirac operator's Reeb coupling coefficient (1 − q⁻¹) |
| ε² | degeneracy resolution: w₍₃,₃₎ − w₍₅,₁₎ = (5/18)ε² + O(ε³), linear term excluded by bar-invariance — the n = 6 two-nucleon (color-tube) channel becoming spectrally real |
| ε³ | categorical gap bound ½(q − q⁻¹)(q − 1)² |

The ε² row carries a physical hypothesis worth its own probe: if
inter-nucleon channel resolution enters at h² while mass enters at h,
binding-to-mass ratios should be O(h²)-suppressed (h² ≈ 0.0121 at q₀ vs
empirical nuclear binding fractions ~0.009 — same order). Whether the
framework's binding formula realizes this is checkable against the
Δ_λ / closed-form-τ_M machinery.

**Probe result (2026-06-11,
`b-over-m-order-probe.witness.json`):** empirical B/m for d / ³He /
⁴He = 0.00119 / 0.00275 / 0.00759 — ratios to h² of 0.098 / 0.227 /
0.628, one to two decades below the h-stratum. Order check passes; the
A-dependence rising toward h²-saturation at ⁴He is exactly the
structure Δ_λ must supply.

**Lean-provability of the B/m hypothesis (owner question,
2026-06-11).** Three-quarters of it is formalizable; one quarter is
witness-territory by nature:

1. **Unconditional, provable now-ish:** the splitting lemma
   `w₍₃,₃₎(1+ε) − w₍₅,₁₎(1+ε) = (5/18)ε² + O(ε³)` — the weights are
   explicit rational functions of q (products of balanced q-integers),
   so the statement is finite polynomial arithmetic over ℚ(q); the
   zero-linear-term half follows elegantly from bar-invariance
   `w(q) = w(q⁻¹)`. Medium effort, one focused LSP session.
2. **Unconditional, easy:** the gap-order identities (already
   skeletoned: `physical_units_gap_linear`, `gap_bound_vanishes_at_one`).
3. **Conditional-class theorem (§3b-cond pattern):** define the class
   of "binding functionals supported on the inter-family splitting
   stratum"; THEOREM: every functional in the class is O(h²). The Δ_λ
   closure, when it lands, instantiates the class — at which point
   B/m = O(h²) becomes a corollary rather than a hypothesis.
4. **Not a theorem, ever:** the empirical comparison itself (AME
   values are measurements) — that stays a witness, which is the
   correct epistemic type for it.

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

## 4. Lean keystone skeleton (S1a) — **LANDED 2026-06-12, sorry-free**

Landed as
[`QOU.BraidKnot.MassGapKeystone`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MassGapKeystone.lean)
(all three skeleton `sorry`s discharged; `lake build
QOU.BraidKnot.MassGapKeystone` green on v4.24.0 via the lake-cache
restore). The same module also delivers **Step 2** (the ε³ lemma) in
exact form: `Δ_{1+ε} = ε³(2+ε)/(2(1+ε))` (categorical),
`Δ/ℏ_q² = ε + (3/2)ε² + (1/2)ε³` (physical-units, exact cubic — the
workplan's `O(ε³)` tail pinned to exactly `ε³/2`), plus the two-sided
pinch `ε³/2 ≤ Δ_{1+ε} ≤ ε³` for `ε > 0`. Generic-R per CLAUDE.md §7c is
not available — ordering (`1 < q`) forces ℝ. The original skeleton is
retained below for provenance.

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
| 1 | S1a Lean skeleton lands + compiles | S | LSP session | **DONE 2026-06-12** (`QOU.BraidKnot.MassGapKeystone`, sorry-free) |
| 2 | Step 2 ε³ lemma in SurrealRateCalculus | S | S1a | **DONE 2026-06-12** (exact forms in `MassGapKeystone`; the abstract `SurrealRateCalculus.massGap_order` rate is realised concretely with the `(2+ε)/(2(1+ε))` scalar displayed) |
| 3 | S1b transfer-matrix definition block | M | — | **DONE 2026-06-12**: `def:categorical-transfer-matrix` already carried the spectral interface (`QOU.Torsion.CategoricalTransferMatrix` — corpus-grep find); S1b landed as the *bridge* in `MassGapKeystone`: `towerSpectrum` pins `SubstrateGap`'s spectrum to that interface, `substrateGap_of_uniform_gapValue` instantiates it from per-level `gapValue` bounds, and `CrossingFiltration` + `substrateGap_of_crossingFiltration` reduce S1c strategy (iii) to a single named hypothesis (valid on the substrate window `1 < q ≤ 2`). Dedup note: the first MassGapKeystone revision duplicated `minCrossingEnergy`/`massGapBound` + 2 theorems from `QOU.Torsion.MassGap`; the S1b revision deletes the duplicates and states everything over the `QOU.Torsion` originals. |
| 4 | Step 3 obstruction-reduction theorem | L | S1b | **mass-gap arm DONE 2026-06-13** (`QOU.BraidKnot.MassGapObstruction`, sorry-free): `kummer_vanishes_at_two` (μ₂ shadow, `2 ∣ 6`), `kummer_persists_above_three` (the "persists at all primes > 3" claim as a theorem), and the combined `massgap_classical_limit_obstruction` — gap death at q = 1 (unconditional) + Kummer persistence (conditional on `QouObstructionReductionContext` with χ(A) = −6). The never-compiled `qou_obstruction_reduction.lean` stub was repaired in passing (missing imports). **Universality theorem remains the open research piece** (mandatory caveat carried in the module docstring). |
| 5 | S1c uniformity in n | XL (research) | S1b | **constructive half DONE 2026-06-13** (`QOU.BraidKnot.CrossingGradedModel`, sorry-free): the crossing-graded model tower (strategy (iii)'s additive energy accounting as spectrum definition `eigenvalues k = k·E_×(q)`) satisfies `CrossingFiltration` by construction; the full pipeline composes to per-level `YangMillsMassGap` witnesses and the **first in-framework `HasYangMillsMassGap` instance** (model-caveated, window `1 < q ≤ 2`). **Open residue of S1c = ONE spectral hypothesis**: every non-vacuum excitation of the *physical* `𝒯_q` on `End(Aₙ)` carries ≥ one crossing's energy (the `per_crossing` field for the physical tower). Strategies (i) Wenzl-tower transport / (ii) Perron–Frobenius are the candidate routes; research-grade. |
| 6 | Typed frontier — narrow both remaining research hypotheses to machine-checkable interfaces | M | rows 1–5 | **DONE 2026-06-13** (`QOU.BraidKnot.MassGapFrontier`, sorry-free). **Gap 1 (S1c physical spectral hypothesis) narrowed three ways**: (a) spectral anchor — `crossingEnergy_eq_eigenvalue_mean` proves `E_×(q) = (q + (−q⁻¹))/2` is the *mean of the two Hecke crossing eigenvalues* `{q, −q⁻¹}` on `S²V ⊕ Λ²V`, with separation `[2]_q = q + q⁻¹` (`crossing_eigenvalue_separation`); (b) induction decomposition — `crossingFiltration_of_base_and_transport` proves `FiltrationBase q tms` + `TowerTransport q tms` ⟹ full `CrossingFiltration` (strategy (i)'s base + Wenzl/Jones-tower transport, two strictly smaller named hypotheses replacing the universally-quantified one); (c) what remains is constructing the base + the transport step (Wenzl conditional-expectation positivity). **Honest scope note (formalize-first finding 2026-06-13): the base case is NOT a near-term `native_decide` win.** The per-crossing Hecke spectrum is the *signed* pair `{q, −q⁻¹}`, and for `1 < q` the antisymmetric eigenvalue is negative — `−q⁻¹ ∈ (−1,0) < 0 < E_×(q)`. But `CategoricalTransferMatrix.eigenvalues` is a *non-negative, monotone, vacuum-0 energy* spectrum (its axioms), so the physical energy spectrum is **not** the raw signed Hecke spectrum: an energy functional `E : (signed Hecke / vertex-volume) → ℝ≥0` sits in between, and `FiltrationBase` is a claim about *that* spectrum. The finite-rank check (H₂/H₃) is well-posed only after the functional is fixed, and fixing it is itself open content (the crossing-graded model postulates `energy = k·E_×` to sidestep it). A numerical probe now would either re-derive the model or smuggle a weights-as-energies identification — declined per the formalize-first + critical-distance disciplines. **Gap 2 (Step-3 universality) narrowed to an interface class**: `AxiomatizedYMWithGap` (minimal abstract data — excitation spectrum + uniform positive gap, deliberately QOU-free), `YMUniversality` class (the gate `AxiomatizedYMWithGap → QouObstructionReductionContext` with `chi_A = −6`), and `universality_transfers_obstruction` (proved sorry-free against the interface — Kummer persistence at all primes > 3 transfers from QOU to every axiomatized gapped YM, conditional on the *existence* of a `YMUniversality` instance). No instance of `YMUniversality` is provided or claimed; constructing one is precisely the open research, and per the workplan's mandatory caveat every obstruction statement remains framework-conditional until it exists. Net effect: discharging either remaining research gap now reduces to constructing **one Lean instance** with a precisely pinned field signature, rather than carrying a prose hypothesis. |

Coordination: Lean modules overlap the active HeckeAlgebra/lean-repair
branches (#2094, #2095, #2108) — post intent before S1a lands; the
n = 6 degeneracy-resolution observation may interest the metallic-regime
and qbeta threads (informational only).
