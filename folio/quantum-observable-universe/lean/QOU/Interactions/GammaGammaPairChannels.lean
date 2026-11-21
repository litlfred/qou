import Mathlib.Tactic
import QOU.QuarkState.PhotonPairNormalForm

/-!
# The six channels of the γγ product, and the confinement reference point

Bean `qou-qs2u`, owner D2 item 2 (2026-11-15). The γγ product
`γ(φ) · γ(ψ)` in `H₃(q)`, with `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (`def:photon`; the last
term is the chiral vertex by owner ruling 2026-11-18, bean `qou-99qc`) and `h = q − q⁻¹`, has
six channel coefficients. They are recorded in
`brings-surface/trivial-knot-photon-interpretation-table5-data.md`, and were recomputed
exactly from the Hecke relation `T_s T_w = h T_w + T_{sw}` (`s` a left descent of `w`) in
`computations/probes/gamma_gamma_pair_nf_h3_probe.py` (sympy, `h` symbolic, all six
agree).

The coefficients were re-derived for the chiral vertex on 2026-11-20; the same six
polynomials are proved from the H₃ multiplication in
`QOU.QuarkState.pairNFChiral_eq` (`QuarkState/PhotonPairNormalForm.lean`). Their agreement with that
normal form is `channels_eq_pairNFChiral`. The definitions below transcribe
the probe-verified table, and the theorems are about those polynomials.

## What this settles

1. **The coefficients are integer polynomials in `φ, ψ, h`**, so they are defined over
   any commutative ring. The reality of `φ` in `prop:confinement-universality` is not
   used by this stage.
2. **At the conjecture's reference point `φ = ψ = 0` the product is the vacuum**
   (`pair_vacuum_at_zero`). Every crossing channel vanishes, so at that point the chain
   `γγ → q q̄ → B₃ · crossings` produces **no quark**. The reference value `N(0,0,0)` of
   the conjecture is therefore not the output of the derivation chain at `0`; it is
   `NF(B₃ · crossings)` with the quark flavours supplied from outside.
3. **The up-quark channel `σ₀` depends on the photon** (`sigma0_channel_nonconstant`).
   So if quark types are read from which channels are nonzero, the flavour assignment
   depends on `φ`, and universality can hold only on the set of `φ` that yield the
   nucleon's flavours. The proof block's own text says "the photon initial conditions
   determine which quark type is produced at each vertex", which is this dependence.

No `sorry`, no axiom, no class.
-/

namespace QOU.Interactions.GammaGamma

variable {R : Type*} [CommRing R]

/-- A photon's colour content `(φ₀, φ₁, φ₀₁)`. -/
structure Photon (R : Type*) where
  c0 : R
  c1 : R
  c01 : R

/-- Coefficient of `1` in `γ(φ)γ(ψ)`. -/
def chId (h : R) (φ ψ : Photon R) : R :=
  1 + φ.c0 * ψ.c0 + φ.c1 * ψ.c1 - h * (φ.c0 * ψ.c01 + φ.c01 * ψ.c0) + h ^ 2 * (φ.c01 * ψ.c01)
/-- Coefficient of `σ₀` (the up-quark channel). -/
def chS0 (h : R) (φ ψ : Photon R) : R :=
  φ.c0 + ψ.c0 + φ.c0 * ψ.c0 * h + φ.c01 * ψ.c1 - h * (φ.c01 + ψ.c01)
    - h ^ 2 * (φ.c0 * ψ.c01 + φ.c01 * ψ.c0) + h ^ 3 * (φ.c01 * ψ.c01)
/-- Coefficient of `σ₁`. -/
def chS1 (h : R) (φ ψ : Photon R) : R :=
  φ.c1 + ψ.c1 + φ.c1 * ψ.c1 * h + φ.c0 * ψ.c01 - h * (φ.c01 * ψ.c01)
/-- Coefficient of `L₊ = σ₀σ₁`. -/
def chLp (h : R) (φ ψ : Photon R) : R :=
  φ.c01 + ψ.c01 + φ.c0 * ψ.c1 + h * (φ.c0 * ψ.c01) - h ^ 2 * (φ.c01 * ψ.c01)
/-- Coefficient of `L₋ = σ₁σ₀`. -/
def chLm (h : R) (φ ψ : Photon R) : R := φ.c1 * ψ.c0 + φ.c01 * ψ.c01 - h * (φ.c1 * ψ.c01)
/-- Coefficient of `e⁻ = σ₀σ₁σ₀`. -/
def chE (_h : R) (φ ψ : Photon R) : R := φ.c01 * ψ.c0 + φ.c1 * ψ.c01

/-- **The six channels are the H₃ normal form**, not a transcription: in the NF basis
`[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` they are `pairNFChiral`. -/
theorem channels_eq_pairNFChiral (h : R) (φ ψ : Photon R) :
    QOU.QuarkState.pairNFChiral h φ.c0 φ.c1 φ.c01 ψ.c0 ψ.c1 ψ.c01 =
      ![chId h φ ψ, chS0 h φ ψ, chS1 h φ ψ, chLm h φ ψ, chLp h φ ψ, chE h φ ψ] := by
  rw [QOU.QuarkState.pairNFChiral_eq]
  funext i; fin_cases i <;> simp [chId, chS0, chS1, chLm, chLp, chE] <;> ring

/-- The bare photon, `φ = 0`. -/
def bare : Photon R := ⟨0, 0, 0⟩

/-- **At the reference point the γγ product is the vacuum**: identity channel `1`,
every crossing channel `0`, for every `h`. -/
theorem pair_vacuum_at_zero (h : R) :
    chId h bare bare = 1 ∧ chS0 h bare bare = 0 ∧ chS1 h bare bare = 0 ∧
      chLp h bare bare = 0 ∧ chLm h bare bare = 0 ∧ chE h bare bare = 0 := by
  simp [chId, chS0, chS1, chLp, chLm, chE, bare]

/-- **The up-quark channel depends on the photon**: a single horizontal unit
polarisation on one photon opens it. -/
theorem sigma0_channel_nonconstant [Nontrivial R] (h : R) :
    chS0 h ⟨1, 0, 0⟩ bare ≠ chS0 h bare bare := by
  simp [chS0, bare]

end QOU.Interactions.GammaGamma
