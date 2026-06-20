import QOU.AppendixSurreals.VacuumEpsilon
import QOU.AppendixSurreals.StandardPart
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# QOU.AppendixSurreals.CasimirEpsilonVacuum — conditional class (§3b-cond)

**§3b-cond class axiomatisation** for content block
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md):
*Casimir force as $\mathrm{st}$-image of $\varepsilon$-vacuum density gradient*.

This is a **conjecture**. Per AGENTS.md §3b-cond, the conjecture is
axiomatised as a Lean `class` whose single field carries the open
content (the surreal coefficient of the plate-constrained unknot
density). A downstream consumer that takes both `VacuumEpsilon` and
this class as `[Instance]` hypotheses derives the textbook Casimir
energy gradient as a *conditional* theorem — fully verified by Lean
modulo the two named conjectural inputs.

The `class` is a parameter, not an asserted fact: it represents the
conjectural existence and scaling of a plate-constrained unknot-
density function. Closing the conjecture means *constructing* such
an instance from QOU primitives, not proving a Lean theorem.

The conditional theorem `energyPerArea_deriv` below is elementary
calculus on a polynomial in `1/d`; the proof is given via
`HasDerivAt` composition (no `sorry`).
-/

namespace QOU.AppendixSurreals

/-- **Plate-mode-count class** — §3b-cond axiomatisation of the
    surreal-coefficient appearing in the parallel-plate Casimir
    conjecture.  See
    [`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md).

    The class carries the *archimedean image* of the surreal
    quantity `(N⊙^in − N⊙^out) · ε`.  The surreal `ε⁻¹` and `ε`
    cancel in the energy density `u(d) = ε·(N⊙^in − N⊙^out)/A`,
    leaving a real-valued function.  This class encodes that
    real-valued energy-density function directly. -/
class CasimirEpsilonVacuum where
  /-- Archimedean energy per unit area between two parallel
      conducting plates separated by `d`, in units where
      `ℏc = 1`.  The conjecture is that this equals
      `-π²/(720 d³)` — the standard-physics Casimir result. -/
  energyPerArea : ℝ → ℝ
  /-- Scaling axiom — the standard-physics result that the QOU
      derivation must reproduce.  Sign: negative (lower energy
      between plates than outside means the force is attractive). -/
  energyPerArea_eq :
    ∀ d : ℝ, 0 < d →
      energyPerArea d = -(Real.pi ^ 2) / (720 * d ^ 3)

/-- **Conditional Casimir-energy gradient** — §3b-cond conditional
    theorem.  Given the plate-mode-count class, the derivative of
    the energy per area is `π²/(240 d⁴)`; the force per area is
    minus this, i.e. `-π² ℏ c / (240 d⁴)` in dimensional units
    (textbook Casimir 1948).

    **Proof strategy.**  Elementary calculus on
    `f(x) = -π²/(720 x³) = -π²/720 · (x³)⁻¹`:

    1. `HasDerivAt (fun x => x^3) (3 d²) d`  via `hasDerivAt_pow 3 d`.
    2. `HasDerivAt (fun x => (x^3)⁻¹) (-(3 d²) / (d³)²) d` via
       `HasDerivAt.inv` on (1).
    3. Multiply by `-π²/720` constant via `HasDerivAt.const_mul`.
    4. Use `EventuallyEq` (via the class axiom on `(0,∞)`) to
       transfer the derivative back to `energyPerArea`.
    5. Simplify `(-π²/720) · (-(3 d²) / (d³)²) = π²/(240 d⁴)` by
       `field_simp; ring`.

    The `VacuumEpsilon` instance is not used by this proof but is
    listed in the hypothesis to advertise the full §3b-cond
    conditional structure: both classes together are required to
    *interpret* this real-valued statement as the standard-part of
    the surreal mechanism in
    [`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md). -/
theorem energyPerArea_deriv
    [VacuumEpsilon] [CasimirEpsilonVacuum]
    (d : ℝ) (hd : 0 < d) :
    deriv CasimirEpsilonVacuum.energyPerArea d = Real.pi ^ 2 / (240 * d ^ 4) := by
  -- Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
  -- Ref: [manuscript] appendix-surreals/casimir-epsilon-vacuum.md
  have hd_ne : d ≠ 0 := ne_of_gt hd
  have hd3_ne : d ^ 3 ≠ 0 := pow_ne_zero 3 hd_ne
  have hd4_pos : (0 : ℝ) < d ^ 4 := pow_pos hd 4
  -- Step 1: locally rewrite the function via the class axiom on (0, ∞).
  have heq : Set.EqOn CasimirEpsilonVacuum.energyPerArea
      (fun x : ℝ => -(Real.pi ^ 2) / (720 * x ^ 3))
      (Set.Ioi (0 : ℝ)) := by
    intro x hx
    exact CasimirEpsilonVacuum.energyPerArea_eq x hx
  -- Step 2: transfer the derivative via EventuallyEq on the
  -- neighborhood (0, ∞).
  have hopen : IsOpen (Set.Ioi (0 : ℝ)) := isOpen_Ioi
  have hd_mem : d ∈ Set.Ioi (0 : ℝ) := hd
  rw [Filter.EventuallyEq.deriv_eq
      (heq.eventuallyEq_of_mem (hopen.mem_nhds hd_mem))]
  -- Step 3: compute deriv of x ↦ -π²/(720 x³) at d > 0.
  -- Build the HasDerivAt for x³ then take inverse.
  have hpow : HasDerivAt (fun x : ℝ => x ^ 3)
      ((3 : ℕ) * d ^ ((3 : ℕ) - 1)) d :=
    hasDerivAt_pow 3 d
  have hpow' : HasDerivAt (fun x : ℝ => x ^ 3) (3 * d ^ 2) d := by
    simpa using hpow
  -- Derivative of 1/x³.
  have hinv : HasDerivAt (fun x : ℝ => (x ^ 3)⁻¹)
      (-(3 * d ^ 2) / (d ^ 3) ^ 2) d :=
    hpow'.inv hd3_ne
  -- Multiply by the constant -π²/720.
  have hfinal : HasDerivAt
      (fun x : ℝ => -(Real.pi ^ 2) / 720 * (x ^ 3)⁻¹)
      (-(Real.pi ^ 2) / 720 * (-(3 * d ^ 2) / (d ^ 3) ^ 2)) d :=
    hinv.const_mul (-(Real.pi ^ 2) / 720)
  -- The function we want is the same as the one in hfinal.
  have hfun_eq : (fun x : ℝ => -(Real.pi ^ 2) / (720 * x ^ 3))
      = fun x : ℝ => -(Real.pi ^ 2) / 720 * (x ^ 3)⁻¹ := by
    funext x; field_simp
  rw [hfun_eq, hfinal.deriv]
  -- Simplify: -π²/720 · -(3 d²) / (d³)² = 3π²/(720 d⁴) = π²/(240 d⁴).
  have hd6_pos : (0 : ℝ) < (d ^ 3) ^ 2 := pow_pos (pow_pos hd 3) 2
  have hd6_ne : (d ^ 3) ^ 2 ≠ 0 := ne_of_gt hd6_pos
  field_simp
  ring

end QOU.AppendixSurreals
