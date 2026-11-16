import QOU.Mathlib.FaddeevRatioPeriodic
import QOU.MathlibExt.DoublyPeriodicLiouville

/-!
# Faddeev–Volkov rigidity against a compact-curve function class

Categorify audit 2026-11-15, item 3. Uniqueness of the Faddeev quantum dilogarithm has the
same shape as Bloch–Wigner rigidity (PR #7946) with `ℙ¹` replaced by the elliptic curve
`E = ℂ/⟨ib, i/b⟩`: the solution set is a torsor under the doubly periodic functions, and the
one analytic axiom is that such functions in the class are constant (`H⁰(E, O) = ℂ`).

* `CompactCurveClass bas`: members are continuous, and lattice-periodic members are constant.
* `ratio_const`: if the ratio of two `FaddeevPhi` solutions lies in the class, it is constant.
  Both periods are **derived** (`periodic_b_of_continuous`, `periodic_binv_of_continuous`).
* `entireClass`: the holomorphic instance (Liouville, `const_of_doublyPeriodic`).
  `ratio_const_of_entire` needs neither the nowhere-zero hypothesis nor the separate `i/b`
  period that `FaddeevRigidityReduction.uniqueUpToScalar_of_entire` takes.

**What this does not do.** It does not prove that the ratio for the concrete `Φ_b` lies in any
class (for `entireClass` that is `hratio`, bean `qou-cons`, which `RigidityReductionScope`
shows is equivalent to the conclusion there). It moves the analysis to that one membership
statement. A bounded-meromorphic instance (`BoundedMeromorphicLiouville`) and the algebraic
function field of `E` are natural further instances, not built here.

-- Ref: [leitner2026] /mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md item 3
-/
open Complex Module
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.Mathlib.FaddeevRatioPeriodic

namespace QOU.QBeta.FaddeevCompactCurve

/-- **A function class with the compact-curve axiom** for the lattice spanned by `bas`:
its members are continuous, and a member periodic under the lattice is constant — the
statement `H⁰(E, O) = ℂ` for `E = ℂ / (ℤ·bas 0 + ℤ·bas 1)`. This is the elliptic analogue of
the `H⁰(ℙ¹, O(−1)) = 0` axiom of the Bloch–Wigner rigidity class (PR #7946). -/
structure CompactCurveClass (bas : Basis (Fin 2) ℝ ℂ) where
  mem : (ℂ → ℂ) → Prop
  continuous_of_mem : ∀ f, mem f → Continuous f
  const_of_periodic : ∀ f, mem f → (∀ i, ∀ z, f (z + bas i) = f z) → ∃ c, ∀ z, f z = c

/-- **Faddeev–Volkov rigidity in any compact-curve class.**  If the ratio of two `FaddeevPhi`
solutions lies in the class, it is constant. Both periods of the ratio are derived from the
shift equations plus continuity (`periodic_b_of_continuous`, `periodic_binv_of_continuous`);
no nowhere-zero hypothesis and no separate `i/b`-periodicity input is needed. The only
analytic content is the class's own axiom. -/
theorem ratio_const {b : ℂ} {Φ Ψ : ℂ → ℂ} (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ)
    {bas : Basis (Fin 2) ℝ ℂ} (hb0 : bas 0 = I * b) (hb1 : bas 1 = I / b)
    (C : CompactCurveClass bas) (hmem : C.mem (fun z => Ψ z / Φ z)) :
    ∃ c, ∀ z, Ψ z / Φ z = c := by
  have hcont := C.continuous_of_mem _ hmem
  refine C.const_of_periodic _ hmem ?_
  rw [Fin.forall_fin_two]
  refine ⟨fun z => ?_, fun z => ?_⟩
  · have h := periodic_b_of_continuous hΦ hΨ hcont (z + I * b)
    rw [hb0]
    simpa using h.symm
  · have h := periodic_binv_of_continuous hΦ hΨ hcont (z + I / b)
    rw [hb1]
    simpa using h.symm

/-- **The holomorphic instance** (Liouville): entire functions. -/
def entireClass (bas : Basis (Fin 2) ℝ ℂ) : CompactCurveClass bas where
  mem f := Differentiable ℂ f
  continuous_of_mem _ hf := hf.continuous
  const_of_periodic _ hf hper :=
    QOU.MathlibExt.DoublyPeriodicLiouville.const_of_doublyPeriodic hf hper

/-- The entire instance recovers the reduction: an entire ratio of two solutions is constant,
with **both** periods derived (compare `FaddeevRigidityReduction.uniqueUpToScalar_of_entire`,
which takes the `i/b`-period as a hypothesis and needs `Φ` nowhere zero). -/
theorem ratio_const_of_entire {b : ℂ} {Φ Ψ : ℂ → ℂ} (hΦ : FaddeevPhi b Φ)
    (hΨ : FaddeevPhi b Ψ) {bas : Basis (Fin 2) ℝ ℂ} (hb0 : bas 0 = I * b) (hb1 : bas 1 = I / b)
    (hr : Differentiable ℂ (fun z => Ψ z / Φ z)) :
    ∃ c, ∀ z, Ψ z / Φ z = c :=
  ratio_const hΦ hΨ hb0 hb1 (entireClass bas) hr

end QOU.QBeta.FaddeevCompactCurve
