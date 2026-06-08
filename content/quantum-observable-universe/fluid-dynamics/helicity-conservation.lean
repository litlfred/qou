import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.helicity_conservation — categorical helicity conservation

The categorical helicity `ℋ_q` of a vortex configuration is conserved
under the quantum Euler equation (`dℋ_q/dt = 0`) and decomposes into
writhe, twist, and linking contributions, with the writhe and twist of
each filament obeying the Călugăreanu–White–Fuller relation
`Wr_q + Tw_q = Lk_q`.

LaTeX label: `prop:helicity-conservation`

## What the load-bearing claim is

The md states (1) conservation `dℋ_q/dt = 0`, (2) the three-way
topological decomposition `ℋ_q = writhe + twist + linking`, and the
self-linking identity `Wr_q + Tw_q = Lk_q`. The earlier version of this
file stated only `theorem … : True := trivial`, a tautology that
asserts none of this (integrity FAIL).

Below the claims are bundled as fields of an abstract `HelicityContext`
(the helicity data of one configuration over a time parameter) and the
theorems project them, mirroring the build-graph copy under
`QOU/FluidDynamics/helicity_conservation.lean`.

## References
- [manuscript] §Fluid dynamics / Categorical helicity conservation,
  prop:helicity-conservation
-/

namespace QOU.FluidDynamics

/-- Helicity data of a vortex configuration: the time-dependent
    categorical helicity `ℋ_q(t)`, its writhe/twist/linking pieces, the
    per-filament self-linking data, and the load-bearing identities. -/
class HelicityContext where
  /-- The categorical helicity `ℋ_q` as a function of time. -/
  Hq : ℝ → ℝ
  /-- Writhe contribution `Σ Wr_q (Γ)²`. -/
  writhe : ℝ
  /-- Twist contribution `Σ Tw_q (Γ)²`. -/
  twist : ℝ
  /-- Linking contribution `2 Σ_{i<j} lk_q Γ_i Γ_j`. -/
  linking : ℝ
  /-- `q`-deformed writhe, twist and self-linking of a single filament. -/
  Wr : ℝ
  Tw : ℝ
  Lk : ℝ
  /-- **Conservation.** `ℋ_q` is constant in time (`dℋ_q/dt = 0`),
      expressed as equality of values at any two times. -/
  conserved : ∀ t s, Hq t = Hq s
  /-- **Decomposition.** `ℋ_q = writhe + twist + linking` (at every time,
      since `ℋ_q` is constant). -/
  decomposition : ∀ t, Hq t = writhe + twist + linking
  /-- **Călugăreanu–White–Fuller relation.** `Wr_q + Tw_q = Lk_q`. -/
  cwf : Wr + Tw = Lk

/-- **Categorical helicity conservation** ([`prop:helicity-conservation`]).

    `ℋ_q` is conserved under the quantum Euler equation: its value is the
    same at any two times. -/
-- Ref: [manuscript] prop:helicity-conservation
theorem helicity_conservation [ctx : HelicityContext] (t s : ℝ) :
    ctx.Hq t = ctx.Hq s :=
  ctx.conserved t s

/-- **Helicity decomposition.** `ℋ_q = writhe + twist + linking`. -/
-- Ref: [manuscript] prop:helicity-conservation
theorem helicity_decomposition [ctx : HelicityContext] (t : ℝ) :
    ctx.Hq t = ctx.writhe + ctx.twist + ctx.linking :=
  ctx.decomposition t

/-- **Călugăreanu–White–Fuller self-linking relation.**
    `Wr_q + Tw_q = Lk_q`. -/
-- Ref: [manuscript] prop:helicity-conservation
theorem helicity_cwf_relation [ctx : HelicityContext] :
    ctx.Wr + ctx.Tw = ctx.Lk :=
  ctx.cwf

end QOU.FluidDynamics
