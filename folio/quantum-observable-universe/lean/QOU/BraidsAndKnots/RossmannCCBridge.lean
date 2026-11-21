import Mathlib.Algebra.Order.Group.Int
import Mathlib.Tactic.Linarith

/-!
# Rossmann characteristic-cycle bridge — a CONDITIONAL candidate for the
  `Δ_λ` single-degree concentration (`DeltaLambdaDTRealization`)

**This is a conditional conjecture carrier, NOT a derived result.**  See
`docs/audits/2026-08-02-rossmann-cc-bridge-deltalambda-realization.md`.

The arc proved (PR #4581) that no *algebraic* substrate grading forces the
single-degree concentration of `Δ_λ`: every genuine graded multiplicity tower
spreads `V_λ` over both grade-parities and CANCELS to `|χ| < dim`, never `Δ_λ`.
The one candidate that is *not* an algebraic grading is the **characteristic
cycle of the archimedean character**:

* `tr_M = Σ_λ y_λ χ_λ` is a character (proved in corpus);
* IF its archimedean evaluation is a Harish-Chandra invariant eigendistribution
  `θ` on `𝔤𝔩_n` — **(IDENT), the open substrate identification** — then by
  Rossmann II its characteristic cycle `CC(θ)` is a Springer conormal cycle, and
  by Springer 1976 / Shoji the component at `λ` is `V_λ` concentrated in the
  single top degree `2n(λ)` — a **single grade-parity** object;
* a single grade-parity object **saturates** `|χ| = dim` (no cancellation), and
  hence realizes `Δ_λ`.

**(IDENT) is genuinely open** and sits under the standing microlocal-is-analogy
guard (`docs/audits/2026-06-09-aqa-dmodule-analogy-not-mechanism.md`): the corpus
does not establish that the archimedean functor lands in the invariant-
eigendistribution setting.  So the class below has **NO instance** (open); it
encodes (IDENT) as its content field, and the theorem *derives* the `Δ_λ`
realization from it — a non-degenerate §3b-cond conditional, not a self-assuming
projection.

## References
Springer, Invent. Math. 36 (1976) 173–207; Invent. Math. 44 (1978) 279–293.
Shoji, arXiv:1909.06744.  Rossmann, *Invariant eigendistributions … II*.
-- Ref: [leitner2026] docs/audits/2026-08-02-rossmann-cc-bridge-deltalambda-realization.md
-/

namespace QOU.BraidsAndKnots

/-- **Conditional conjecture class (§3b-cond, OPEN — no instance).**

For each partition datum `l : Λ`, the archimedean character's Springer
characteristic cycle is summarised by its **even-degree mass** `e l ≥ 0` and
**odd-degree mass** `o l ≥ 0` (of cohomological degree); its ungraded total
`e + o` is the Wedderburn dimension `dim l` (a proved-in-corpus prerequisite);
its signed Euler characteristic is `e - o`; and `target l = Δ_λ` is the signed
dimension (`|target| = dim`), sign-matched to the cycle.

The **content field is `single_parity` — this is (IDENT)**: the claim that the
characteristic cycle of the archimedean character is *single grade-parity*
(concentrated / cancellation-free), the microlocal concentration Rossmann +
Springer predict for a genuine invariant eigendistribution.  It is the OPEN
substrate identification; there is deliberately **no instance** of this class. -/
class RossmannCCConcentration (Λ : Type*) where
  /-- Wedderburn dimension `dim V_λ` (as a `ℤ`). -/
  dim : Λ → ℤ
  /-- The signed binding factor `Δ_λ` (`= ±dim`). -/
  target : Λ → ℤ
  /-- Even-cohomological-degree mass of the characteristic cycle. -/
  e : Λ → ℤ
  /-- Odd-cohomological-degree mass of the characteristic cycle. -/
  o : Λ → ℤ
  e_nonneg : ∀ l, 0 ≤ e l
  o_nonneg : ∀ l, 0 ≤ o l
  /-- Proved-in-corpus prerequisite: `f_λ(1) = dim V_λ` (ungraded total). -/
  total : ∀ l, e l + o l = dim l
  /-- `Δ_λ` is the signed dimension. -/
  target_abs : ∀ l, |target l| = dim l
  /-- **(IDENT) — the open substrate identification.**  The characteristic cycle
  of the archimedean character is single grade-parity (cancellation-free). -/
  single_parity : ∀ l, e l = 0 ∨ o l = 0
  /-- The cycle's signed Euler characteristic has the sign of `Δ_λ`. -/
  sign_match : ∀ l, (0 ≤ target l → 0 ≤ e l - o l) ∧ (target l ≤ 0 → e l - o l ≤ 0)

variable {Λ : Type*}

/-- **Conditional consequence (DERIVED, non-degenerate).**  Given (IDENT) — the
archimedean character's characteristic cycle is single grade-parity — its signed
Euler characteristic `e - o` equals `Δ_λ`.  I.e. the characteristic cycle
**realizes** `Δ_λ`: the single-degree concentration (`DeltaLambdaDTRealization`)
holds *conditionally on (IDENT)*.

The derivation is genuine (not a projection of the hypothesis): single-parity
gives the saturation `|e - o| = e + o = dim = |Δ_λ|`, and `sign_match` upgrades
equal-magnitude to equal-signed. The open input is `single_parity` (IDENT); the
conclusion `e - o = Δ_λ` is composed from it with the proved corpus prerequisites
`total`/`target_abs` (the #4581 single-parity-saturation mechanism, over `ℤ`). -/
theorem rossmann_cc_realizes_deltaLambda [C : RossmannCCConcentration Λ] (l : Λ) :
    C.e l - C.o l = C.target l := by
  have he := C.e_nonneg l
  have ho := C.o_nonneg l
  have htot := C.total l
  have hdimnn : 0 ≤ C.dim l := by linarith
  have hcases : C.target l = C.dim l ∨ C.target l = -C.dim l :=
    (abs_eq hdimnn).mp (C.target_abs l)
  have hsm := C.sign_match l
  rcases C.single_parity l with he0 | ho0
  · rcases hcases with h | h
    · have := hsm.1 (by linarith); linarith
    · linarith
  · rcases hcases with h | h
    · linarith
    · have := hsm.2 (by linarith); linarith

/-- The concentration is **not vacuous as an implication**: the same hypotheses
without single-parity do NOT force `e - o = Δ_λ`.  A two-parity witness
(`e = o = 1`, `dim = 2`, `target = 2`) satisfies every field EXCEPT
`single_parity`, yet `e - o = 0 ≠ 2 = target` — mirroring #4581's cancellation.
So `single_parity` (IDENT) is genuinely load-bearing in the derivation above. -/
theorem rossmann_cc_two_parity_fails :
    ∃ (e o dim target : ℤ),
      0 ≤ e ∧ 0 ≤ o ∧ e + o = dim ∧ |target| = dim ∧
      (0 ≤ target → 0 ≤ e - o) ∧ (target ≤ 0 → e - o ≤ 0) ∧
      e - o ≠ target := by
  refine ⟨1, 1, 2, 2, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **Double even-degree mass decomposition from concentration (`qou-zcjg`).**
Combining `C.total l` (`e + o = dim`) with `rossmann_cc_realizes_deltaLambda l`
(`e - o = target`) yields `2 * e = dim + target`. -/
theorem rossmann_cc_double_even_eq_dim_add_target [C : RossmannCCConcentration Λ] (l : Λ) :
    2 * C.e l = C.dim l + C.target l := by
  have htot := C.total l
  have hdiff := rossmann_cc_realizes_deltaLambda (C := C) l
  linarith

end QOU.BraidsAndKnots
