import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic

/-!
# Faddeev modular-double quantum dilogarithm — structural axiomatisation

The Faddeev *non-compact* quantum dilogarithm `Φ_b` — the correct decay-face
object (bar-odd / root-of-unity / Chern–Simons), **not** the compact
q-Pochhammer `∏(1−q^{-k}z)^{-1}` used in the mass tower — is a transcendental
function not available in Mathlib. This file provides:

1. the **bar-parity decomposition** (the sinh/cosh = bar-odd/bar-even split)
   over any commutative ring with a ring involution `σ` — the algebraic core
   of "modular double `b ↔ b^{-1}` = bar involution `q ↔ q^{-1}`; symmetric
   part = cosh (mass/Rogers face), antisymmetric part = sinh (decay/CS face)";
2. a **class** axiomatising `Φ_b`'s defining relations (modular invariance
   `Φ_b = Φ_{b^{-1}}`; Faddeev inversion `Φ(x)Φ(-x) = c`) with a derived
   consequence — the §3b pattern (the transcendental function is the open
   object; its structural identities are formalised).

Scope: this does **not** construct `Φ_b`, and does **not** claim `Φ_b` is the
canonical archimedean functor of the decay step — that is the open f-map (a
§3b-cond conditional). See
`docs/scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md` and
`docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`.
-/

namespace QOU.QBeta

/-- **Bar-parity decomposition** (the sinh/cosh split under the modular
    involution). Over any commutative ring, for a ring involution `σ` (the
    bar `q ↦ q^{-1}` / modular double `b ↦ b^{-1}`), the doubled element
    `2·f` splits as a **bar-even** (cosh; mass/Rogers face) part `f + σ f`,
    fixed by `σ`, plus a **bar-odd** (sinh; decay/CS face) part `f − σ f`,
    negated by `σ`. -/
theorem bar_parity_decomposition {R : Type*} [CommRing R]
    (σ : R →+* R) (hσ : Function.Involutive σ) (f : R) :
    2 * f = (f + σ f) + (f - σ f)
      ∧ σ (f + σ f) = f + σ f
      ∧ σ (f - σ f) = -(f - σ f) := by
  refine ⟨by ring, ?_, ?_⟩
  · rw [map_add, hσ f]; ring
  · rw [map_sub, hσ f]; ring

/-- Structural axiomatisation of the Faddeev modular-double quantum
    dilogarithm `Φ_b`. The transcendental function is not constructed
    (open); its defining identities are recorded so downstream results
    depend on them explicitly. `bar` is the modular involution `b ↦ b^{-1}`
    (`= q ↦ q^{-1}`). -/
structure FaddeevModularDouble (R : Type*) [CommRing R] where
  Phi : R → R
  bar : R →+* R
  bar_invol : Function.Involutive bar
  /-- Modular invariance `Φ_b = Φ_{b^{-1}}`. -/
  modular_invariance : ∀ x, Phi (bar x) = Phi x
  /-- The Faddeev inversion constant (the archimedean instance is
      `Φ_b(0)^2 · e^{πix²}`; here the constant `c`). -/
  c : R
  /-- Faddeev inversion relation `Φ(x)·Φ(-x) = c`. -/
  inversion : ∀ x, Phi x * Phi (-x) = c

/-- Derived: the Faddeev inversion constant is `Φ_b(0)^2`. -/
theorem FaddeevModularDouble.c_eq_phi_zero_sq {R : Type*} [CommRing R]
    (F : FaddeevModularDouble R) : F.c = F.Phi 0 * F.Phi 0 := by
  have h := F.inversion 0
  simpa using h.symm

/-! ## σ-unitarity — the algebraic form of `|u| = 1` (the fibre-saddle phase)

Numerically witnessed on the validated evaluator
(`computations/qbeta/qbeta_fmap_phi_b_root_of_unity_reference.py`): at real
`b` (root-of-unity `q = e^{2πib²}`, the fibre/decay saddle) and real `z`,
`|Φ_b(z)| = 1` — `Φ_b` is a pure phase. The analytic reason is the reflection
`w ↦ −w̄` of the Faddeev contour integral (Hikami math/0604094 eq (2.1)),
which sends `log Φ_b` to `−(log Φ_b)‾` for real `b, z`.

The lemmas below isolate the **algebraic core** over any commutative ring
with a ring involution `σ` (archimedean instance: complex conjugation):
σ-unitaries form a multiplicative monoid, and — the arc-closing rigidity —
**a bar-even σ-unitary is an involution (`u² = 1`)**, so any genuine phase
(`u² ≠ 1`) necessarily carries bar-odd content. This is the algebraic reason
the unimodular fibre-saddle `Φ_b` is a bar-ODD (decay/sinh) carrier and the
`Q_β/Q_A = cos Φ(u)` phase reframe is the natural bar-odd form. -/

/-- σ-unitary: `σ(u)·u = 1` — the ring-involution form of `|u| = 1`. -/
def IsSigmaUnitary {R : Type*} [CommRing R] (σ : R →+* R) (u : R) : Prop :=
  σ u * u = 1

theorem isSigmaUnitary_one {R : Type*} [CommRing R] (σ : R →+* R) :
    IsSigmaUnitary σ 1 := by
  simp [IsSigmaUnitary]

/-- σ-unitaries are closed under multiplication. -/
theorem IsSigmaUnitary.mul {R : Type*} [CommRing R] {σ : R →+* R} {u v : R}
    (hu : IsSigmaUnitary σ u) (hv : IsSigmaUnitary σ v) :
    IsSigmaUnitary σ (u * v) := by
  unfold IsSigmaUnitary at hu hv ⊢
  have h : σ (u * v) * (u * v) = (σ u * u) * (σ v * v) := by
    rw [map_mul]; ring
  rw [h, hu, hv, one_mul]

/-- **Bar-even unitaries are involutions.** If `u` is σ-unitary and σ-fixed
    (bar-even), then `u² = 1`. -/
theorem IsSigmaUnitary.sq_eq_one_of_bar_even {R : Type*} [CommRing R]
    {σ : R →+* R} {u : R} (hu : IsSigmaUnitary σ u) (heven : σ u = u) :
    u * u = 1 := by
  have h : σ u * u = 1 := hu
  rwa [heven] at h

/-- **Phases are bar-odd (mod involutions).** A σ-unitary with `u² ≠ 1`
    cannot be bar-even: it carries a nontrivial bar-odd part. The algebraic
    reason the fibre-saddle pure-phase `Φ_b` lives on the bar-odd (decay)
    face. -/
theorem IsSigmaUnitary.not_bar_even_of_sq_ne_one {R : Type*} [CommRing R]
    {σ : R →+* R} {u : R} (hu : IsSigmaUnitary σ u) (h : u * u ≠ 1) :
    σ u ≠ u :=
  fun heven => h (hu.sq_eq_one_of_bar_even heven)

/-! ## Channel separation — cross-anchor variation is pure phase

The fibre-side spec for the `c_k` evaluation map (handed to the z→c_k f-map
keystone, PR #3458). The observed cross-anchor `c_3` swing
(`c_3(q_p) = −2.0693` proton vs `−2.0097` muon; `Δq = 1.28×10⁻⁸`) demands a
slope `dc_3/dq ≈ 4.66×10⁶`, which for a **smooth real function of `q`** requires
a singularity within `≈ 4.4×10⁻⁷` of `q_0` (the real-`q` impossibility, PR
#1821 — no categorical object supplies such a pole). The lemmas below record
the algebraic reason the impossibility is a **magnitude-channel** bound only:
between two σ-unitaries (the fibre-saddle `|Φ_b| = 1`), the entire connecting
factor is again σ-unitary — a *pure phase*. The magnitude channel is flat, so
the swing lives in the phase (bar-odd / `Im 𝔙` / decay) channel, on which the
smooth-real magnitude bound is silent. -/

/-- The σ-conjugate `σ u` is the two-sided inverse of a σ-unitary `u`
    (commutative form of `u·ū = 1`). -/
theorem IsSigmaUnitary.mul_bar_self {R : Type*} [CommRing R] {σ : R →+* R}
    {u : R} (hu : IsSigmaUnitary σ u) : u * σ u = 1 := by
  rw [mul_comm]; exact hu

/-- The σ-inverse of a σ-unitary is σ-unitary. -/
theorem IsSigmaUnitary.inv {R : Type*} [CommRing R] {σ : R →+* R} {u : R}
    (hu : IsSigmaUnitary σ u) (hσ : Function.Involutive σ) :
    IsSigmaUnitary σ (σ u) := by
  unfold IsSigmaUnitary
  rw [hσ u, mul_comm]; exact hu

/-- **Cross-anchor connecting factor is a pure phase.** For two σ-unitaries
    `u₁, u₂` (the fibre-saddle `Φ_b` at the proton and muon anchors), the
    connecting factor `w = σ(u₁)·u₂` is itself σ-unitary and satisfies
    `u₁·w = u₂`. Hence *all* cross-anchor variation between σ-unitaries is
    carried by a σ-unitary (pure-phase) factor — the magnitude channel is
    flat, and the `Δc_3` swing is a phase-channel (bar-odd) quantity. -/
theorem IsSigmaUnitary.crossFactor {R : Type*} [CommRing R] {σ : R →+* R}
    {u₁ u₂ : R} (h₁ : IsSigmaUnitary σ u₁) (h₂ : IsSigmaUnitary σ u₂)
    (hσ : Function.Involutive σ) :
    IsSigmaUnitary σ (σ u₁ * u₂) ∧ u₁ * (σ u₁ * u₂) = u₂ := by
  refine ⟨(h₁.inv hσ).mul h₂, ?_⟩
  rw [← mul_assoc, h₁.mul_bar_self, one_mul]

end QOU.QBeta
