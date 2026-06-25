import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic
import QOU.Archimedean.DilogarithmArchimedeanLimit


/-!
# Archimedean limit of Φ_n(x; q): conjecture statement

The conjecture: under the joint Faddeev scaling q → 1, n → ∞,
n(1-q) → ∞, the rescaled logarithm (1-q) · log Φ_n(x; q) converges
to the classical dilogarithm Li₂(x).

This file provides:
* a concrete Mathlib-backed definition of `LiTwo : ℝ → ℝ` as the
  series Σ_{k≥1} x^k / k², replacing the previous `opaque`
  placeholder. The series converges absolutely on the closed unit
  disc, divergently outside it; at `|x| ≤ 1` the value coincides
  with the principal-branch real dilogarithm.
* unconditional boundary lemmas (`LiTwo_zero`, `partialProduct_zero`)
  that anchor the conjecture's class instances at the only points
  where the Faddeev limit is trivial.
* the conjecture, packaged as the typeclass `ArchimedeanLimit`, with
  one field stating the convergence of `(1-q) log Φ_n(x;q)` to
  `LiTwo x` along Faddeev's joint scaling. The class is the §3b-cond
  hook used by `prop:archimedean-functor-uniqueness`.

Difficulty split (see audit
`docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md`):
* **Part A** — fixed `x ∈ (0,1)`, convergence side `q → 1⁻` — is
  mathematically ELEMENTARY (a monotone left-Riemann-sum limit, an
  exponential tail bound, and the factor `(1-q)/ℏ → 1`; no Tauberian
  theorem, no branch cut, since `1 - x q^k ≥ 1 - x > 0`). A sorry-free
  Lean proof of Part A is gated only on Mathlib Riemann-sum-to-integral
  convergence plus the identity `∫₀ˣ -log(1-t)/t = Σ_{k≥1} xᵏ/k²` — the
  infrastructure bottleneck noted in the 2026-05-30 closure audit.
* **Part B** — the substrate continuation `q → 1⁺` (to `q₀ ≈ 1.11`) and
  uniformity as `x → 1⁻` — is the genuine open content: there the factors
  `1 - x q^k` change sign (the poles of `Φ_n` approach the `Li₂` branch
  cut) and the Frobenius-pairing pole cancellation must do real work.

The class formulation isolates these gaps; the unconditional `x = 0`
instance below is the boundary anchor.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-/

namespace QOU.QPochhammer

/-! The concrete primitives `denomPolyLocal`, `partialProductLocal`,
    `LiTwo`, and the boundary lemmas `LiTwo_zero`, `denomPoly_zero`,
    `partialProduct_zero`, `faddeev_limit_at_zero` now live in the
    importable lib module `QOU.Archimedean.DilogarithmArchimedeanLimit`
    (imported above) — their single source of truth — so downstream
    content blocks (e.g. `cl2-pentagon-and-faddeev-partial`) can reuse
    them.  The open conjecture class and its boundary instance below
    consume those imported primitives. -/

/-- The Archimedean-limit conjecture, packaged as a typeclass.
    A concrete instance asserts the convergence
    `(1 - q) · log Φ_n(x; q) → Li₂(x)` along Faddeev's scaling. -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
class ArchimedeanLimit (x : ℝ) : Prop where
  /-- The Faddeev limit of the rescaled log partial product equals
      the classical dilogarithm. The hypotheses on `(q, n)` capture
      the joint scaling `q → 1`, `n → ∞`, `n(1-q) → ∞`. -/
  -- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
  faddeev_limit :
    ∀ ε > (0 : ℝ),
      ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
        (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
          ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε

/-- Stated form of the conjecture (sorry-free at the level of Lean,
    inhabited only via a `[ArchimedeanLimit x]` typeclass instance). -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem partialProduct_to_LiTwo (x : ℝ) [h : ArchimedeanLimit x]
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
      (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
        ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε :=
  h.faddeev_limit ε hε

/-- **Unconditional instance at `x = 0`.** The Faddeev limit holds
    trivially at the boundary point `x = 0` because both sides of
    the asserted convergence are identically zero, so the limit is
    the constant zero sequence. This is the only point at which the
    `ArchimedeanLimit` class can be inhabited without further
    Mathlib infrastructure; for every `x ∈ (0, 1)` the instance
    requires the full Tauberian argument from Faddeev 1994 /
    Kashaev 1997. -/
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
instance archimedeanLimit_zero : ArchimedeanLimit 0 where
  faddeev_limit := by
    intro ε hε
    refine ⟨1, by norm_num, ?_⟩
    intro q n _
    rw [faddeev_limit_at_zero]
    simpa using hε

end QOU.QPochhammer
