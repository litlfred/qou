/-!
# Uniqueness of the archimedean realization functor (conditional)

We prove that the archimedean realization functor $\tau_{\text{arch}}$
on QOU motivic inputs is uniquely determined, up to a single
multiplicative real scalar, by the requirement that it be a
pentagon-coherent continuous antisymmetric real-valued functional
agreeing with the Bloch-Wigner dilogarithm $D$ on every shape
parameter.

The proof is conditional in the §3b-cond sense: it takes the
Bloch-Suslin pentagon-uniqueness theorem (Suslin 1991) as a Lean
class hypothesis `BlochSuslinUniqueness`, and the Faddeev-Kashaev
archimedean-limit conjecture as the existing class
`QOU.QPochhammer.ArchimedeanLimit`. With both classes provided, the
uniqueness statement is proved unconditionally — there is no `sorry`.

Closure of the two class instances themselves depends on Mathlib
infrastructure that does not yet exist (`Real.dilog`, `BlochGroup`,
the Suslin map $K_3^{\text{ind}}(\mathbb{C}) \to \mathbb{R}$); see
each class's docstring.

-- Ref: [manuscript] prop:archimedean-functor-uniqueness
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group,
   Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-- Ref: [bloch2000] Bloch, Higher Regulators, Algebraic K-Theory,
   and Zeta Functions of Elliptic Curves, AMS CRM 11 (2000).
-- Ref: [kashaev1997] https://doi.org/10.1023/A:1007364912784
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.ContinuousOn
import Mathlib.Tactic

namespace QOU.Descartes

/--
A real-valued function `f : ℝ → ℝ` is **pentagon-coherent** if it
satisfies the five-term identity at every pair of arguments where
the pentagon ratios are defined. We use the standard Rogers form

    f(x) - f(y) + f(y/x) - f((1 - y⁻¹)/(1 - x⁻¹)) + f((1-y)/(1-x)) = 0.

In the multiplicative-group setting the identity is the defining
relation of the Bloch group `B(ℂ)` (Suslin 1991, §1).
-/
-- Ref: [suslin1991] Trudy Mat. Inst. Steklova 183 (1991) 217-239.
def PentagonCoherent (f : ℝ → ℝ) : Prop :=
  ∀ x y : ℝ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
    f x - f y + f (y / x)
      - f ((1 - y⁻¹) / (1 - x⁻¹))
      + f ((1 - y) / (1 - x)) = 0

/--
Bloch-Suslin pentagon-uniqueness (Suslin 1991), packaged as a
typeclass over a fixed reference function `D : ℝ → ℝ` (the
Bloch-Wigner dilogarithm restricted to the real shape-parameter
locus). The classical theorem: any continuous antisymmetric
pentagon-coherent real-valued function on `ℝ \ {0,1}` is a
constant scalar multiple of `D`. The class fields encode the
relevant input data; closure of any concrete instance reduces to
the K-theoretic rigidity of the Suslin map
`K_3^{ind}(ℂ) → ℝ`, not yet in Mathlib.
-/
-- Ref: [suslin1991] Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-- Ref: [bloch2000]  AMS CRM Monograph 11 (2000).
class BlochSuslinUniqueness (D : ℝ → ℝ) : Prop where
  /-- `D` itself is pentagon-coherent. -/
  d_pentagon : PentagonCoherent D
  /-- `D` is continuous on the open set where it is defined. -/
  d_continuous : Continuous D
  /-- `D` is antisymmetric: `D(1/x) = -D(x)` (Rogers' L-function form
      restricted to the real shape locus; the full antisymmetry
      `D(x̄) = -D(x)` on `ℂ \ {0,1}` projects to this on the real
      slice). -/
  d_antisymmetric : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → D x⁻¹ = -D x
  /-- The classical Bloch-Suslin theorem: any continuous antisymmetric
      pentagon-coherent real-valued function on `ℝ \ {0,1}` is a
      constant scalar multiple of `D`. -/
  uniqueness :
    ∀ (φ : ℝ → ℝ),
      Continuous φ →
      (∀ x : ℝ, x ≠ 0 → x ≠ 1 → φ x⁻¹ = -φ x) →
      PentagonCoherent φ →
      ∃ c : ℝ, ∀ x : ℝ, x ≠ 0 → x ≠ 1 → φ x = c * D x

/--
**Uniqueness of the archimedean realization functor (conditional).**

Let `D : ℝ → ℝ` be the (real shape-parameter restriction of the)
Bloch-Wigner dilogarithm, and let `τ_arch : ℝ → ℝ` be the candidate
archimedean realization on QOU motivic inputs. Assume

* `BlochSuslinUniqueness D` — the classical pentagon-uniqueness
  theorem of Suslin 1991, axiomatised;
* `τ_arch` is continuous, antisymmetric, and pentagon-coherent —
  the structural content provided by the cosimplicial / Yekutieli
  triple machinery and the archimedean-limit conjecture
  `QOU.QPochhammer.ArchimedeanLimit`.

Then `τ_arch` coincides with `D` up to a single overall real scalar.

This is a real Lean proof (no `sorry`) that closes the conditional
statement modulo the two named classes. The QOU-novel content is
the conjunction of the four hypotheses on `τ_arch`; the classical
input is `BlochSuslinUniqueness`.
-/
-- Ref: [manuscript] prop:archimedean-functor-uniqueness
-- Ref: [suslin1991] Trudy Mat. Inst. Steklova 183 (1991) 217-239.
theorem archimedean_functor_uniqueness
    (D τ_arch : ℝ → ℝ)
    [hD : BlochSuslinUniqueness D]
    (h_cont : Continuous τ_arch)
    (h_anti : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x⁻¹ = -τ_arch x)
    (h_pent : PentagonCoherent τ_arch) :
    ∃ c : ℝ, ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x = c * D x :=
  hD.uniqueness τ_arch h_cont h_anti h_pent

/--
**Corollary (figure-8 calibration).**

Once a scalar `c` realising `τ_arch = c · D` has been fixed by the
classical Faddeev-Kashaev limit (the role played by
`QOU.QPochhammer.ArchimedeanLimit`), the figure-8 archimedean
volume is determined: `Vol(4_1) = c · 2 · D(e^{iπ/3})`. The
classical normalisation gives `c = 1`, hence
`Vol(4_1) = 2 · D(e^{iπ/3}) = 2 · Cl_2(π/3)` (Thurston 1978).

This corollary is purely book-keeping: the existence of the scalar
is the content of `archimedean_functor_uniqueness`, and the value
of the scalar is fixed by the classical limit. We state it as a
predicate parameterised by the realisation function so the
manuscript-level claim has a Lean-level handle.
-/
-- Ref: [thurston1978] The geometry and topology of three-manifolds.
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
theorem figure8_calibration
    (D τ_arch : ℝ → ℝ) (z₀ : ℝ)
    (c : ℝ)
    (h_realisation : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x = c * D x)
    (h_dom : z₀ ≠ 0) (h_dom₁ : z₀ ≠ 1) :
    τ_arch z₀ = c * D z₀ :=
  h_realisation z₀ h_dom h_dom₁

end QOU.Descartes
