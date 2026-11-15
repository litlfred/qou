import QOU.QBeta.RatioEntireOfSameDivisor
import QOU.QBeta.FaddeevPhiUniquenessAssembly

/-!
# A_ω uniqueness leg — the conditional capstone (same divisor ⇒ proportional)

Composes the three proved pieces of the Faddeev–Volkov uniqueness leg into one
statement, discharging the `hr_entire` input via brick (c):

* brick (c) `RatioEntire.entire_toMeromorphicNFOn_div_of_same_order` — **same
  divisor ⇒ the normal-form ratio `r = toMeromorphicNFOn (Φ₁/Φ₂)` is entire**;
* the concrete-`Φ_b` reduction
  `FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire` —
  **entire ratio + the two `FaddeevPhi` quasi-period periodicities ⇒ proportional**.

The result: two `FaddeevPhi` solutions with the **same divisor** are proportional
on `Φ₂`'s nonvanishing locus. The `hr_entire` wall is gone (brick (c)); what
remains are the **honestly-named residual analytic inputs**, carried as explicit
hypotheses, *none axiomatised*:

1. `hsame` — the same-divisor premise. **Not derivable from the `FaddeevPhi`
   class** (`FaddeevPhiEllipticFreedom.faddeevPhi_mul_elliptic`: an elliptic
   factor gives a solution with a different divisor); it needs a strip-growth
   strengthening or the `PhiBProd` divisor.
2. `hr_ratio` — the normal-form representative agrees with `Φ₁/Φ₂` pointwise on
   `Φ₂`'s nonvanishing locus. This needs the solutions to be in meromorphic
   **normal form** (no `0/0` junk at removable points) — a second property the
   total-function class does not encode.
3. `hS₀/hS₁ + hmem₀/hmem₁` — the periodicity loci are dense and lie off `Φ₂`'s
   zeros (the `Φ_b` zero-lattice discreteness, `PhiBProd`-gated).

So the leg is reduced to exactly these three named analytic facts about the
concrete `Φ_b` — the maximal reduction achievable at the class level. Verified
`lean`-direct against the Meromorphic cone (exit 0).
-/

open Complex MeromorphicOn
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.FaddeevUniquenessCapstone

/-- **Conditional capstone: same divisor ⇒ proportional.** Two `FaddeevPhi`
solutions at `b` (nondegenerate lattice `(b²).im ≠ 0`), meromorphic on `ℂ` with
`Φ₂` nowhere locally zero and **the same divisor** (`hsame`), are proportional on
`Φ₂`'s nonvanishing locus — provided the normal-form ratio agrees with `Φ₁/Φ₂`
there (`hr_ratio`) and the two `FaddeevPhi` periodicity loci are dense off `Φ₂`'s
zeros (`hmem₀/hmem₁`). The `hr_entire` input is discharged internally by brick (c);
the remaining hypotheses are the honest, non-axiomatised residual analytic inputs. -/
theorem faddeevPhi_proportional_of_same_divisor
    {b : ℂ} (hb2 : (b ^ 2).im ≠ 0)
    {Φ₁ Φ₂ : ℂ → ℂ} [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂]
    (hΦ₁ : MeromorphicOn Φ₁ Set.univ) (hΦ₂ : MeromorphicOn Φ₂ Set.univ)
    (hΦ₂0 : ∀ z, meromorphicOrderAt Φ₂ z ≠ ⊤)
    (hsame : ∀ z, meromorphicOrderAt Φ₁ z = meromorphicOrderAt Φ₂ z)
    (hr_ratio : ∀ z, Φ₂ z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z = Φ₁ z / Φ₂ z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I * b) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I / b) ≠ 0) :
    ∃ c, ∀ z, Φ₂ z ≠ 0 → Φ₁ z = c * Φ₂ z := by
  have hbrick := RatioEntire.entire_toMeromorphicNFOn_div_of_same_order hΦ₂ hΦ₁ hΦ₂0 hsame
  exact FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire
    hb2 hbrick.1 hr_ratio hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.FaddeevUniquenessCapstone
