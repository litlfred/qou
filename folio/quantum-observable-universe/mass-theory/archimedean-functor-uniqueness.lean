import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.ContinuousOn
import Mathlib.Tactic


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

-- Ref: [leitner2026] prop:archimedean-functor-uniqueness
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group,
   Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-- Ref: [bloch2000] Bloch, Higher Regulators, Algebraic K-Theory,
   and Zeta Functions of Elliptic Curves, AMS CRM 11 (2000).
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-/

namespace QOU.Archimedean

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
-- Ref: [leitner2026] prop:archimedean-functor-uniqueness
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
-- Ref: [murakami-murakami2001] Murakami & Murakami, "The colored Jones polynomials and the simplicial volume of a knot," Acta Math. 186 (2001), arXiv:math/9905075
theorem figure8_calibration
    (D τ_arch : ℝ → ℝ) (z₀ : ℝ)
    (c : ℝ)
    (h_realisation : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x = c * D x)
    (h_dom : z₀ ≠ 0) (h_dom₁ : z₀ ≠ 1) :
    τ_arch z₀ = c * D z₀ :=
  h_realisation z₀ h_dom h_dom₁

/-! ## The real-slice pentagon forces vanishing (2026-11-15, issue #7942)

`PentagonCoherent` above is **not** the Bloch–Suslin five-term relation: the
last two arguments are the *inverses* of Suslin's
`(1 - x⁻¹)/(1 - y⁻¹)` and `(1 - x)/(1 - y)`.  Together with the antisymmetry
`f x⁻¹ = -f x` this is strong enough to kill every solution on `ℝ \ {0,1}`,
with no continuity and no K-theory.  Specialise the relation at `y = x⁻¹`:

  `2 f x - f (x²) - 2 f (-x) = 0`   (`x ∉ {0, 1, -1}`).

The same identity at `-x` gives `f (x²) = 2 f (-x) - 2 f x`, so `f (x²) = 0`,
hence `f` vanishes on `(0,∞) \ {1}` and then on `(-∞,0)`.

Consequences, all proved below:

* `pentagonCoherent_antisymm_eq_zero` — any antisymmetric `PentagonCoherent`
  function is `0` off `{0,1}`;
* `blochSuslinUniqueness_iff` — `BlochSuslinUniqueness D ↔ D = 0`;
* `instBlochSuslinUniquenessZero` — the instance at `D = 0` (which *is* the
  Bloch–Wigner function on the real line, since `D(x) = 0` for real `x`);
* `archimedean_functor_hyps_force_zero` — the hypotheses of
  `archimedean_functor_uniqueness` already force `τ_arch = 0` off `{0,1}`, so
  that theorem cannot carry `Vol(4₁)`: its figure-8 point `e^{iπ/3}` is not on
  the real slice.

The class therefore has an instance, but only the trivial one.  The intended
statement needs complex arguments and Suslin's orientation of the five-term
relation; that corrected statement is
`QOU/Archimedean/BlochSuslinComplex.lean` (`BlochWignerFiveTerm`,
`BlochSuslinRigidity`, `figure8_from_rigidity`).  See issue #7942. -/

/-- Real-slice pentagon at `y = x⁻¹`: `f (x²) = 2 f x - 2 f (-x)`. -/
theorem pentagon_at_inv (f : ℝ → ℝ)
    (h_anti : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → f x⁻¹ = -f x)
    (h_pent : PentagonCoherent f) (x : ℝ)
    (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hxm : x ≠ -1) :
    f (x ^ 2) = 2 * f x - 2 * f (-x) := by
  have hxi0 : x⁻¹ ≠ 0 := inv_ne_zero hx0
  have hxi1 : x⁻¹ ≠ 1 := by
    intro h; exact hx1 (by simpa using congrArg (·⁻¹) h)
  have hxx : x ≠ x⁻¹ := by
    intro h
    have h2 : x * x = 1 := by
      calc x * x = x * x⁻¹ := by rw [← h]
        _ = 1 := mul_inv_cancel₀ hx0
    have : (x - 1) * (x + 1) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h | h
    · exact hx1 (by linarith)
    · exact hxm (by linarith)
  have hP := h_pent x x⁻¹ hx0 hx1 hxi0 hxi1 hxx
  have hsq0 : x ^ 2 ≠ 0 := pow_ne_zero 2 hx0
  have hsq1 : x ^ 2 ≠ 1 := by
    intro h
    have : (x - 1) * (x + 1) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h | h
    · exact hx1 (by linarith)
    · exact hxm (by linarith)
  have hn0 : -x ≠ 0 := neg_ne_zero.mpr hx0
  have hn1 : -x ≠ 1 := fun h => hxm (by linarith)
  have e1 : x⁻¹ / x = (x ^ 2)⁻¹ := by field_simp
  have e2 : (1 - x⁻¹⁻¹) / (1 - x⁻¹) = -x := by
    rw [inv_inv]
    have : (1 : ℝ) - x⁻¹ ≠ 0 := sub_ne_zero.mpr (Ne.symm hxi1)
    field_simp
    have : x - 1 ≠ 0 := sub_ne_zero.mpr hx1
    field_simp
    ring
  have e3 : (1 - x⁻¹) / (1 - x) = (-x)⁻¹ := by
    have : (1 : ℝ) - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hx1)
    field_simp
    ring
  rw [e1, e2, e3, h_anti x hx0 hx1, h_anti _ hsq0 hsq1, h_anti _ hn0 hn1] at hP
  linarith

/-- **Every antisymmetric `PentagonCoherent` function vanishes off `{0,1}`.**
    No continuity is used. -/
theorem pentagonCoherent_antisymm_eq_zero (f : ℝ → ℝ)
    (h_anti : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → f x⁻¹ = -f x)
    (h_pent : PentagonCoherent f) :
    ∀ x : ℝ, x ≠ 0 → x ≠ 1 → f x = 0 := by
  -- vanishing on the positive half-line minus `1`
  have hpos : ∀ t : ℝ, 0 < t → t ≠ 1 → f t = 0 := by
    intro t ht ht1
    set s := Real.sqrt t with hs
    have hs0 : 0 < s := Real.sqrt_pos.mpr ht
    have hsq : s ^ 2 = t := Real.sq_sqrt ht.le
    have hs1 : s ≠ 1 := by
      intro h; apply ht1; rw [← hsq, h]; norm_num
    have hsm : s ≠ -1 := by intro h; linarith
    have a := pentagon_at_inv f h_anti h_pent s hs0.ne' hs1 hsm
    have b := pentagon_at_inv f h_anti h_pent (-s) (neg_ne_zero.mpr hs0.ne')
      (by intro h; linarith) (by intro h; exact hs1 (by linarith))
    rw [neg_sq, neg_neg] at b
    rw [← hsq]; linarith
  intro x hx0 hx1
  rcases lt_or_gt_of_ne hx0 with hneg | hposx
  · by_cases hxm : x = -1
    · subst hxm
      have := h_anti (-1) (by norm_num) (by norm_num)
      norm_num at this; linarith
    · have a := pentagon_at_inv f h_anti h_pent x hx0 hx1 hxm
      have h2 : f (x ^ 2) = 0 :=
        hpos _ (by positivity) (by
          intro h
          have : (x - 1) * (x + 1) = 0 := by ring_nf; linarith
          rcases mul_eq_zero.mp this with h | h
          · exact hx1 (by linarith)
          · exact hxm (by linarith))
      have h3 : f (-x) = 0 := hpos _ (by linarith) (by intro h; exact hxm (by linarith))
      linarith
  · exact hpos x hposx hx1

/-- **The hypotheses of `archimedean_functor_uniqueness` force `τ_arch = 0`**
    off `{0,1}`, whatever `D` is. -/
theorem archimedean_functor_hyps_force_zero (τ_arch : ℝ → ℝ)
    (h_anti : ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x⁻¹ = -τ_arch x)
    (h_pent : PentagonCoherent τ_arch) :
    ∀ x : ℝ, x ≠ 0 → x ≠ 1 → τ_arch x = 0 :=
  pentagonCoherent_antisymm_eq_zero τ_arch h_anti h_pent

/-- **`BlochSuslinUniqueness D` holds exactly when `D = 0`.** -/
theorem blochSuslinUniqueness_iff (D : ℝ → ℝ) :
    BlochSuslinUniqueness D ↔ D = 0 := by
  constructor
  · intro h
    have hz := pentagonCoherent_antisymm_eq_zero D h.d_antisymmetric h.d_pentagon
    have hdense : Dense ({(0 : ℝ), 1}ᶜ : Set ℝ) := by
      simpa [Set.compl_eq_univ_diff] using dense_univ.diff_finite (Set.toFinite ({(0 : ℝ), 1} : Set ℝ))
    exact Continuous.ext_on hdense h.d_continuous continuous_const
      (fun x hx => by
        simp only [Set.mem_compl_iff, Set.mem_insert_iff, Set.mem_singleton_iff,
          not_or] at hx
        simpa using hz x hx.1 hx.2)
  · rintro rfl
    refine ⟨?_, continuous_const, ?_, ?_⟩
    · intro x y _ _ _ _ _; simp
    · intro x _ _; simp
    · intro φ _ h_anti h_pent
      exact ⟨0, fun x hx0 hx1 => by
        simpa using pentagonCoherent_antisymm_eq_zero φ h_anti h_pent x hx0 hx1⟩

/-- **The instance.**  `D = 0`, which is the Bloch–Wigner dilogarithm on the
    real line (`D(x) = Im Li₂(x) + arg(1-x) log|x| = 0` for real `x`). -/
instance instBlochSuslinUniquenessZero : BlochSuslinUniqueness (0 : ℝ → ℝ) :=
  (blochSuslinUniqueness_iff 0).mpr rfl

end QOU.Archimedean
