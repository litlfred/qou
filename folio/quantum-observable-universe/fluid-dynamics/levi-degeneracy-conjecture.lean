import Mathlib.LinearAlgebra.CrossProduct
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.FluidDynamics.LeviDegeneracy — `conj:levi-degeneracy`, re-scoped

**Re-scoped 2026-10-13** onto the vorticity plane field, per the owner decision
"Q1 Θ = f·ξ♭".  The setting is the 3D flow domain (`ℝ³`, or `T³` read
periodically), not the state bundle `𝒮`.  There `ξ = ω/|ω|` where `ω ≠ 0`, the
plane field is `ker Θ = ξ^⊥`, and its Levi datum is the single scalar
`ξ·curl ξ` (`prop:core-levi-form`).

## What this file contains

1. **Branch (A) is withdrawn, with a machine-checked counterexample.**  Branch (A)
   read "non-degenerate (bounded) Levi data ⇒ blow-up".  Under `Θ = f·ξ♭` the
   Beltrami flow `u = e^{-νt}(sin z, cos z, 0)` on `T³` has `ξ·curl ξ = 1`
   everywhere and `|ω|² = e^{-2νt} ≤ 1`.  `beltrami_*` below check the curl, the
   Levi scalar, the heat equation and the bound.  Scope (b) **for that
   implication under that reading**: the counterexample is the invariant.  It
   refutes no reading the corpus has not stated.

   The reduction of NS to the heat equation for this field is standard and is
   stated, not formalised: the field depends on `z` only and has zero third
   component, so `div u = 0` and `(u·∇)u = u₃ ∂_z u = 0`, and `p ≡ 0`.

2. **The true conditional statement** (standard-cited, not derived here): the
   contrapositive of Beirão da Veiga–Berselli.  `BeiraoDaVeigaBerselliCriterion`
   carries the **cited theorem** as its one field — the hypothesis — and
   `blowup_forces_direction_incoherence` **derives** its contrapositive.  The class
   is a cited result, not a conjecture; no instance is given here, because the
   PDE theorem is not formalisable in Mathlib today.

3. **Branch (B), restated as an open carrier.**  `LeviDegeneracy` asserts
   "Levi scalar vanishes on the high-vorticity set ⇒ no blow-up".  No standard
   result implies it: the Constantin–Fefferman / Beirão da Veiga–Berselli
   hypothesis bounds all of `∇ξ` from above, and vanishing of one component does
   not supply it.  It is a primary conjecture: content-bearing, **no instance**.

## What was removed

The previous `LeviDegeneracy` class identified the degeneracy set of an abstract
`leviForm : ℝ → ℝ → ℝ` with the angular reciprocals `{1/κ : κ ≥ 2}` of the
root-of-unity ladder `q_κ = e^{iπ/κ}`.  Under `Θ = f·ξ♭` the Levi datum is a
function on the flow domain, not on the `q`-ladder, so that encoding has no
referent.  Nothing else in the tree named the class (measured 2026-10-13).

The growth-rate trichotomy (`QOU/FluidDynamics/levi_growth_trichotomy.lean`)
is stated for a Levi *condition number*, which is undefined in dimension 3; it is
untouched here and recorded as out of scope in the content block.

No `sorry`, no `axiom`, no instance of either class.

Ref: [leitner2026] fluid-dynamics/levi-degeneracy-conjecture, `conj:levi-degeneracy`
-/

namespace QOU.FluidDynamics

namespace LeviDegeneracyQ1

open Matrix

/-! ### 1. The Beltrami counterexample to branch (A) -/

/-- The Beltrami direction field `ξ(z) = (sin z, cos z, 0)`. -/
noncomputable def beltramiDir (z : ℝ) : Fin 3 → ℝ := ![Real.sin z, Real.cos z, 0]

/-- `curl` of a field `(a(z), b(z), 0)` depending on `z` only:
`(-b'(z), a'(z), 0)`. -/
noncomputable def curlZ (a b : ℝ → ℝ) (z : ℝ) : Fin 3 → ℝ :=
  ![-(deriv b z), deriv a z, 0]

/-- **`curl ξ = ξ`** for the Beltrami direction field. -/
theorem beltrami_curl (z : ℝ) : curlZ Real.sin Real.cos z = beltramiDir z := by
  simp [curlZ, beltramiDir, Real.deriv_sin, Real.deriv_cos]

/-- **The Levi scalar is identically `1`**: `ξ·curl ξ = sin² z + cos² z = 1`.
So `ker ξ♭` is a contact structure on all of `T³`, with a constant,
non-degenerate Levi datum. -/
theorem beltrami_levi_scalar (z : ℝ) :
    beltramiDir z ⬝ᵥ curlZ Real.sin Real.cos z = 1 := by
  rw [beltrami_curl]
  simp [beltramiDir, dotProduct, Fin.sum_univ_three]
  nlinarith [Real.sin_sq_add_cos_sq z]

/-- `ξ` is a unit field. -/
theorem beltrami_unit (z : ℝ) : beltramiDir z ⬝ᵥ beltramiDir z = 1 := by
  simp [beltramiDir, dotProduct, Fin.sum_univ_three]
  nlinarith [Real.sin_sq_add_cos_sq z]

/-- Temporal factor `e^{-νt}` solves `g' = -ν g`. -/
theorem decay_deriv (ν t : ℝ) :
    deriv (fun s => Real.exp (-ν * s)) t = -ν * Real.exp (-ν * t) := by
  have h : HasDerivAt (fun s => -ν * s) (-ν) t := by
    simpa using (hasDerivAt_id t).const_mul (-ν)
  rw [(h.exp).deriv]; ring

/-- Spatial factor: `∂_z² sin = -sin` and `∂_z² cos = -cos`. -/
theorem beltrami_second_deriv (z : ℝ) :
    deriv (deriv Real.sin) z = -Real.sin z ∧
      deriv (deriv Real.cos) z = -Real.cos z := by
  refine ⟨?_, ?_⟩
  · rw [Real.deriv_sin, Real.deriv_cos]
  · rw [Real.deriv_cos']
    exact ((Real.hasDerivAt_sin z).neg).deriv

/-- **Heat equation, componentwise.**  For `u = e^{-νt}(sin z, cos z, 0)`:
`∂_t u_i = ν ∂_z² u_i` for `i = 1, 2` (the third component is `0`).  With
`div u = 0`, `(u·∇)u = 0` and `p ≡ 0` (file docstring) this is the unforced
Navier–Stokes system. -/
theorem beltrami_heat (ν t z : ℝ) :
    -ν * Real.exp (-ν * t) * Real.sin z
        = ν * (Real.exp (-ν * t) * deriv (deriv Real.sin) z) ∧
      -ν * Real.exp (-ν * t) * Real.cos z
        = ν * (Real.exp (-ν * t) * deriv (deriv Real.cos) z) := by
  obtain ⟨h1, h2⟩ := beltrami_second_deriv z
  rw [h1, h2]; constructor <;> ring

/-- **Bounded vorticity for all time**: `|ω|² = e^{-2νt}·|ξ|² ≤ 1` for `ν, t ≥ 0`
(here `ω = curl u = u`). -/
theorem beltrami_vorticity_bounded (ν t z : ℝ) (hν : 0 ≤ ν) (ht : 0 ≤ t) :
    (Real.exp (-ν * t) • beltramiDir z) ⬝ᵥ (Real.exp (-ν * t) • beltramiDir z)
      ≤ 1 := by
  rw [smul_dotProduct, dotProduct_smul, beltrami_unit, smul_eq_mul, smul_eq_mul,
    mul_one]
  have h0 : 0 < Real.exp (-ν * t) := Real.exp_pos _
  have h1 : Real.exp (-ν * t) ≤ 1 := Real.exp_le_one_iff.mpr (by nlinarith)
  nlinarith

/-- **Branch (A) fails for this flow** ([`conj:levi-degeneracy`], scope (b) for
the implication under `Θ = f·ξ♭`): the Levi scalar is `1` everywhere — never
degenerate — and the vorticity stays bounded for all `t ≥ 0`. -/
-- Ref: [constantin1993] (the flow trivially satisfies the Lipschitz hypothesis)
theorem beltrami_refutes_branchA (ν : ℝ) (hν : 0 ≤ ν) :
    (∀ z, beltramiDir z ⬝ᵥ curlZ Real.sin Real.cos z = 1) ∧
      ∀ t, 0 ≤ t → ∀ z,
        (Real.exp (-ν * t) • beltramiDir z) ⬝ᵥ (Real.exp (-ν * t) • beltramiDir z)
          ≤ 1 :=
  ⟨beltrami_levi_scalar, fun t ht z => beltrami_vorticity_bounded ν t z hν ht⟩

/-! ### 2. Flow data and the Beirão da Veiga–Berselli contrapositive -/

/-- Data of a flow on `[0, T*)` in `ℝ³` coordinates: the vorticity `ω(t, x)`,
the direction field `ξ(t, x)` and the value `curl ξ (t, x)`.  **Data only**: the
relations between the fields are named propositions below, and solution-hood is a
predicate the caller supplies. -/
structure FlowData where
  /-- Blow-up time candidate `T*`. -/
  Tstar : ℝ
  /-- Vorticity `ω(t, x)`. -/
  vort : ℝ → (Fin 3 → ℝ) → (Fin 3 → ℝ)
  /-- Direction field `ξ(t, x)`. -/
  dir : ℝ → (Fin 3 → ℝ) → (Fin 3 → ℝ)
  /-- The value of `curl ξ` at `(t, x)`. -/
  curlDir : ℝ → (Fin 3 → ℝ) → (Fin 3 → ℝ)

namespace FlowData

/-- `ξ = ω/|ω|` wherever `ω ≠ 0`. -/
def IsVorticityDirection (s : FlowData) : Prop :=
  ∀ t x, s.vort t x ≠ 0 →
    s.dir t x = (Real.sqrt (s.vort t x ⬝ᵥ s.vort t x))⁻¹ • s.vort t x

/-- `(t, x)` lies in the high-vorticity set `|ω| > Ω`. -/
def HighVort (s : FlowData) (Ω t : ℝ) (x : Fin 3 → ℝ) : Prop :=
  Ω ^ 2 < s.vort t x ⬝ᵥ s.vort t x

/-- **The Beirão da Veiga–Berselli hypothesis**: `|sin φ| ≤ C |x − y|^{1/2}` on
the high-vorticity set, written squared: `|ξ(x) × ξ(y)|² ≤ C²·|x − y|`. -/
def DirectionHalfHolder (s : FlowData) : Prop :=
  ∃ Ω : ℝ, 0 < Ω ∧ ∃ C : ℝ, 0 ≤ C ∧
    ∀ t, 0 ≤ t → t < s.Tstar → ∀ x y, s.HighVort Ω t x → s.HighVort Ω t y →
      (s.dir t x ⨯₃ s.dir t y) ⬝ᵥ (s.dir t x ⨯₃ s.dir t y)
        ≤ C ^ 2 * Real.sqrt ((x - y) ⬝ᵥ (x - y))

/-- **No blow-up at `T*`**, in Beale–Kato–Majda form: `|ω|` bounded on
`[0, T*) × ℝ³`. -/
def VorticityBounded (s : FlowData) : Prop :=
  ∃ M : ℝ, ∀ t, 0 ≤ t → t < s.Tstar → ∀ x, s.vort t x ⬝ᵥ s.vort t x ≤ M

/-- **Levi degeneracy on the high-vorticity set**: `ξ·curl ξ = 0` wherever
`|ω| > Ω`, for some `Ω > 0`. -/
def LeviDegenerateOnHighVort (s : FlowData) : Prop :=
  ∃ Ω : ℝ, 0 < Ω ∧ ∀ t, 0 ≤ t → t < s.Tstar → ∀ x, s.HighVort Ω t x →
    s.dir t x ⬝ᵥ s.curlDir t x = 0

end FlowData

/-- **The Beirão da Veiga–Berselli criterion, as a cited hypothesis.**

`IsSolution s` is the caller's predicate "`s` is a smooth solution of unforced
Navier–Stokes on `[0, T*)`, in the class of the theorem, with `curlDir` the curl
of `dir`".  The single field is the published theorem: on such a solution, the
½-Hölder direction condition on the high-vorticity set prevents blow-up.  It is a
**hypothesis**, never discharged here.  The class carries the theorem, not the
conclusion derived from it below.

Bibliographic data confirmed via secondary sources; the primary text is not held
(`docs/audits/2026-10-12-ns-v1-geometric-depletion.md` §1). -/
class BeiraoDaVeigaBerselliCriterion (IsSolution : FlowData → Prop) : Prop where
  -- Ref: [beiraodaveiga2002] Differential Integral Equations 15(3) (2002) 345–356
  -- Ref: [constantin1993] Indiana Univ. Math. J. 42 (1993) 775–789 (Lipschitz form)
  criterion : ∀ s, IsSolution s → s.IsVorticityDirection →
    s.DirectionHalfHolder → s.VorticityBounded

/-- **Blow-up forces direction incoherence** (the true conditional statement;
contrapositive of Beirão da Veiga–Berselli).  If a solution blows up at `T*`,
then for every threshold `Ω > 0` and constant `C ≥ 0` there is a time `t < T*` and
two high-vorticity points at which the line field violates the ½-Hölder bound. -/
-- Ref: [beiraodaveiga2002]
theorem blowup_forces_direction_incoherence {IsSolution : FlowData → Prop}
    [h : BeiraoDaVeigaBerselliCriterion IsSolution] (s : FlowData)
    (hs : IsSolution s) (hd : s.IsVorticityDirection) (hblow : ¬ s.VorticityBounded) :
    ∀ Ω : ℝ, 0 < Ω → ∀ C : ℝ, 0 ≤ C →
      ∃ t, 0 ≤ t ∧ t < s.Tstar ∧ ∃ x y, s.HighVort Ω t x ∧ s.HighVort Ω t y ∧
        C ^ 2 * Real.sqrt ((x - y) ⬝ᵥ (x - y))
          < (s.dir t x ⨯₃ s.dir t y) ⬝ᵥ (s.dir t x ⨯₃ s.dir t y) := by
  intro Ω hΩ C hC
  by_contra hno
  apply hblow
  refine h.criterion s hs hd ⟨Ω, hΩ, C, hC, ?_⟩
  intro t ht0 htT x y hx hy
  by_contra hlt
  exact hno ⟨t, ht0, htT, x, y, hx, hy, lt_of_not_ge hlt⟩

/-! ### 3. Branch (B): the open carrier -/

/-- **`conj:levi-degeneracy`, branch (B), re-scoped (open; no instance).**

On every solution in the caller's class, if the Levi scalar `ξ·curl ξ` vanishes
on the high-vorticity set then the vorticity stays bounded up to `T*`.

No standard result supplies this.  The Beirão da Veiga–Berselli hypothesis
bounds all of `∇ξ` from above on the high-vorticity set, and the vanishing of
the one component `ξ·curl ξ` does not imply it — nor does its non-vanishing
(`beltrami_refutes_branchA` is the other side of that).  This is a primary
conjecture; assuming it is assuming the open content. -/
class LeviDegeneracy (IsSolution : FlowData → Prop) : Prop where
  -- Ref: [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (branch B)
  degenerate_implies_regular : ∀ s, IsSolution s → s.IsVorticityDirection →
    s.LeviDegenerateOnHighVort → s.VorticityBounded

/-- What branch (B) gives, stated as a derivation: under the carrier, a blowing-up
solution has a non-zero Levi scalar somewhere in every high-vorticity set.  This
is the contrapositive of the carrier's field and adds nothing to it; it is here
so that the shape of the claim is visible. -/
theorem levi_nondegenerate_somewhere_of_blowup {IsSolution : FlowData → Prop}
    [h : LeviDegeneracy IsSolution] (s : FlowData) (hs : IsSolution s)
    (hd : s.IsVorticityDirection) (hblow : ¬ s.VorticityBounded) :
    ∀ Ω : ℝ, 0 < Ω → ∃ t, 0 ≤ t ∧ t < s.Tstar ∧ ∃ x, s.HighVort Ω t x ∧
      s.dir t x ⬝ᵥ s.curlDir t x ≠ 0 := by
  intro Ω hΩ
  by_contra hno
  apply hblow
  refine h.degenerate_implies_regular s hs hd ⟨Ω, hΩ, ?_⟩
  intro t ht0 htT x hx
  by_contra hne
  exact hno ⟨t, ht0, htT, x, hx, hne⟩

end LeviDegeneracyQ1

end QOU.FluidDynamics
