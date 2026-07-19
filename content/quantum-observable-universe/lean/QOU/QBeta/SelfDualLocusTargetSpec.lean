/-
# The c₃⟺q₀ self-dual-locus target specification — what a fibre derivation must produce

The stalled-agent c₃⟺q₀ synthesis (PR #4085 consolidation) established that every
*real*-magnitude route to the c₃ bar-odd carrier `S` is closed by a proved
invariant, and that one *fibre-level complex* object survives — the same object
for the swing, the Δ_λ closure, and the q₀ zero `q*`. This file states the
**typed target** of that surviving object, in the honest `TargetSpec` style of
`QOU.Archimedean.TauFunctorTargetSpec`: the interface a fibre derivation must
supply, machine-checked to be content-free *by itself* so the real wall is named
exactly.

The target has two legs, and it is important to keep them apart:

* **SHAPE leg (open, actively worked).** A fibre derivation must produce a
  *bar-odd* carrier `N` (under the substrate bar-involution `σ`, `σ (N x) = −N x`)
  whose zero is the self-dual locus `qStar` — the `ε = 0` / Chern–Simons-vanishing
  point where `S` is pure bar-even (capstone `2026-07-12-c3-wall-resolution-capstone.md`).
  This is `BarOddCarrierTarget` below. The shape is the object of the 5₂-chiral
  fibre program (`docs/audits/2026-07-18-ck-odd-fibre-attack-options.md`).

* **VALUE leg (proved-closed, measurement-limited).** The *numeric position* of
  `qStar` — hence the swing value — is **not** derivable below the experimental
  `Q_β` floor. This is already proved (fully machine-checked) in
  `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing` (no anchor-invariant
  fibre datum equals the swinging `S`) and the gate arithmetic in
  `QOU.QBeta.MeasurementLimitedFloor`. The TargetSpec does **not** re-open this
  leg; a fibre derivation supplies the *shape*, never the sub-floor *value*.

Per §"Axiomatization is NOT a Proof": nothing here asserts the fibre derivation
exists; the trivial inhabitant is labeled as demonstrating NON-sufficiency of the
interface (the `N ≡ 0` carrier satisfies every field), never as progress; the
carrier `N` remains an abstract datum, no `c_k` is wired, and `q*`'s value stays
measurement-limited.

Base ring is a generic `CommRing R` with an abstract involution `σ : R →+* R`
(the `q ↦ q⁻¹` bar map); no `ℝ`, no ordering — the substrate→archimedean wall is
not crossed (AGENTS.md §7c). Companion: `QOU.QBeta.CrossingWeightAffine` (the
concrete affine bar-odd carrier `−h·w`, the shape's simplest realization).

-- Ref: [manuscript] docs/audits/2026-07-18-ck-odd-fibre-attack-options.md (shape-leg frontier)
-/
import Mathlib.Algebra.Field.Basic

namespace QOU.QBeta.SelfDualLocusTargetSpec

variable {R : Type*} [CommRing R]

/-- **The SHAPE target a fibre derivation of the c₃ bar-odd channel must supply.**
A carrier `N : R → R` that is bar-odd under the substrate involution `σ`, together
with a self-dual locus `qStar` at which it vanishes (the `ε = 0` / CS-vanishing
point). The *functorial/fibre provenance* of `N`, and the sub-`Q_β`-floor *value*
of `qStar`, live OUTSIDE this type — see the module docstring's two-leg split. -/
structure BarOddCarrierTarget (σ : R →+* R) where
  /-- the bar-odd carrier (the categorical image of the c₃ odd channel). -/
  N : R → R
  /-- **content:** `N` is bar-odd — `σ (N x) = −N x` for every `x`. -/
  barOdd : ∀ x, σ (N x) = -(N x)
  /-- the self-dual locus (the `ε = 0` / CS→0 point). -/
  qStar : R
  /-- **content:** the carrier vanishes at the self-dual locus. -/
  vanishAtStar : N qStar = 0

variable {σ : R →+* R}

/-- **Self-consistency at the locus.** The bar image of the carrier also vanishes
at `qStar` — the zero is bar-fixed, matching "pure bar-even at `q*`" (capstone). -/
theorem bar_vanishes_at_star (T : BarOddCarrierTarget σ) : σ (T.N T.qStar) = 0 := by
  rw [T.vanishAtStar]; exact map_zero σ

/-- **A bar-odd carrier is antisymmetric about any bar-fixed point in value.**
If `T.N x = 0` then `σ (T.N x) = 0` too; more usefully, at the locus the odd
carrier contributes nothing to the bar-even (`Re 𝔙`) channel — the value there is
carried entirely by the even part. Stated as the vanishing of the symmetrized
combination `N + σ∘N` at `qStar`. -/
theorem even_symmetrization_at_star (T : BarOddCarrierTarget σ) :
    T.N T.qStar + σ (T.N T.qStar) = 0 := by
  rw [T.vanishAtStar, map_zero, add_zero]

/-- **Honesty check — the interface is trivially inhabitable.** The `N ≡ 0`
carrier satisfies every field (bar-odd vacuously, vanishing everywhere), so
`BarOddCarrierTarget` *alone* carries no content: the wall is NOT the interface,
the parity, or the vanishing condition (all free). It is EXCLUSIVELY (a) the
fibre/functorial provenance that produces the *specific* non-zero `N` of the c₃
odd channel, and (b) the sub-`Q_β`-floor *value* of `qStar`, which
`no_anchor_invariant_realizes_swing` + `MeasurementLimitedFloor` prove is not
derivable. Mirrors `TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable`. -/
def trivial (σ : R →+* R) : BarOddCarrierTarget σ where
  N := fun _ => 0
  barOdd := fun _ => by rw [map_zero, neg_zero]
  qStar := 0
  vanishAtStar := rfl

/-- The trivial inhabitant is genuinely content-free: its carrier is identically
zero. This is the machine-checked witness that the interface does not constrain
the physics. -/
theorem trivial_carrier_zero (σ : R →+* R) (x : R) : (trivial σ).N x = 0 := rfl

end QOU.QBeta.SelfDualLocusTargetSpec
