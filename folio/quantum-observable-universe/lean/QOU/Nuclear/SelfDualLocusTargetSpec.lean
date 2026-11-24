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

-- Ref: [leitner2026] docs/audits/2026-07-18-ck-odd-fibre-attack-options.md (shape-leg frontier)
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

/-! ## Simple-zero refinement (the "slope ≠ 0 at q*" shape, algebraically)

The `2026-07-18` frontier fixes the SHAPE of the bar-odd numerator `N_odd` as a
*simple* zero at `q*` (slope `≈ +2.37`). A numeric slope is archimedean; the
algebraic content of "simple zero" — valid over a generic `CommRing` with **no**
`ℝ`, no derivative (§7c) — is that `N` **factors** as `(x − qStar) · cofactor`
with the cofactor a **unit at `qStar`** (nonzero there). That is the typed shape
requirement a fibre derivation must meet. -/

/-- A bar-odd carrier with a **simple** zero at the self-dual locus, encoded
algebraically: `N x = (x − qStar) · cofactor x` with `cofactor qStar ≠ 0`. -/
structure SimpleZeroBarOddCarrier (σ : R →+* R) where
  /-- the bar-odd carrier. -/
  N : R → R
  /-- **content:** bar-odd parity. -/
  barOdd : ∀ x, σ (N x) = -(N x)
  /-- the self-dual locus. -/
  qStar : R
  /-- the cofactor exhibiting the linear factor `(x − qStar)`. -/
  cofactor : R → R
  /-- **content:** the simple-zero factorization. -/
  factor : ∀ x, N x = (x - qStar) * cofactor x
  /-- **content:** the cofactor is a unit at the locus — the zero is *simple*
      (the algebraic "slope ≠ 0"). -/
  cofactorNeZero : cofactor qStar ≠ 0

/-- A simple-zero carrier **vanishes at the locus** — derived from the
factorization, not assumed. -/
theorem simpleZero_vanishAtStar (T : SimpleZeroBarOddCarrier σ) : T.N T.qStar = 0 := by
  rw [T.factor T.qStar, sub_self, zero_mul]

/-- A simple-zero carrier refines the plain `BarOddCarrierTarget`: it forgets the
factorization and keeps the (now-derived) vanishing. -/
def toTarget (T : SimpleZeroBarOddCarrier σ) :
    BarOddCarrierTarget σ where
  N := T.N
  barOdd := T.barOdd
  qStar := T.qStar
  vanishAtStar := simpleZero_vanishAtStar T

/-! ## Capstone connection: `q*` is the pure-bar-even (`ε = 0`) point

The wall-resolution capstone (`2026-07-12`) identifies `q*` as the point where the
full carrier `S` is **pure bar-even** — its bar-odd part vanishes, `ε = 0`. Typed:
decompose `S = even + odd` under the bar-involution; if `odd` vanishes at `qStar`,
then `S` is **bar-fixed** there (`σ (S q*) = S q*`). -/

/-- The full c₃ carrier `S`, bar-decomposed, with a bar-odd part vanishing at the
self-dual locus. -/
structure BarDecomposedCarrier (σ : R →+* R) where
  /-- the full carrier `S = Q_β/E₀`. -/
  S : R → R
  /-- its bar-even part (`Re 𝔙` / meson-cosh channel). -/
  even : R → R
  /-- its bar-odd part (`Im 𝔙` / decay-sinh channel). -/
  odd : R → R
  /-- **content:** the decomposition. -/
  decomp : ∀ x, S x = even x + odd x
  /-- **content:** the even part is bar-fixed. -/
  evenBarFixed : ∀ x, σ (even x) = even x
  /-- **content:** the odd part is bar-odd. -/
  oddBarOdd : ∀ x, σ (odd x) = -(odd x)
  /-- the self-dual locus. -/
  qStar : R
  /-- **content:** the odd part vanishes at the locus. -/
  oddVanishAtStar : odd qStar = 0

/-- **`q*` is the pure-bar-even point (capstone `ε = 0`).** The full carrier is
bar-fixed at the self-dual locus. -/
theorem pure_bar_even_at_star (T : BarDecomposedCarrier σ) :
    σ (T.S T.qStar) = T.S T.qStar := by
  rw [T.decomp, map_add, T.evenBarFixed, T.oddBarOdd, T.oddVanishAtStar, neg_zero,
      add_zero]

end QOU.QBeta.SelfDualLocusTargetSpec
