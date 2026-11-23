import Mathlib.Algebra.Polynomial.Laurent
import QOU.Archimedean.GroundRing

/-!
# QOU.Archimedean.ParticleKnots

Canonical declarations of the elementary-particle knot structures, shared by
the `predicted-spectra` and `knots-particles-confinement` content blocks.

## Why these live here (bean `qou-lsib`, owner-authorised 2026-08-23)

They previously lived in the content-block `.lean` siblings that document
them — `electron-knot.lean`, `neutrino-knot.lean`, and so on. Those files sit
at `content/{paper}/{chapter}/{block}.lean`, **outside** the `qou` package's
`["QOU", "QOU.+"]` globs, so they are not modules and cannot import one
another. A block needing another block's structure therefore had two options,
and the corpus contained both:

* **re-declare it locally** — `down-quark.lean` carried its own `Neutrino` and
  `UpQuark`, each a *stripped-down* copy with fewer fields than the original,
  so the two declarations were not even in agreement; or
* **reference it and fail to compile** — `positron-knot.lean` referencing
  `Electron`, `spectral-half-line.lean` and `hasse-weil-bound.lean`
  referencing `LocalQZetaFunction`.

Both are now unnecessary: a content-block sibling can `import
QOU.Archimedean.ParticleKnots` and get one canonical declaration.

**Where a duplicate disagreed, the fuller declaration is canonical here.**
Every field carries a default, so a structure with more fields still admits
`({} : T).field` for each field the narrower version had; `down-quark.lean`
was checked against this file's `Neutrino` and `UpQuark` and uses only fields
present in both.

## Constructing a particle

Every field has a default, so the canonical instance is `({} : Electron)` and
a field is read as `({} : Electron).charge`. Note that `Electron.mk` is the
*constructor* — a function — so `Electron.mk.charge` does not elaborate; five
blocks carried that form before it was corrected.
-/

namespace QOU.Archimedean

/-! `R_q = ℤ[q, q⁻¹]` is **not** redeclared here. It is `QOU.Archimedean.GroundRing`'s,
and this file imports it.

Until 2026-08-30 both modules declared `abbrev R_q := LaurentPolynomial ℤ` — same name,
same namespace, same body, and neither importing the other. Each compiled alone; they
collided only where something imported both, which is the root aggregator `QOU.lean`:
`import QOU.Archimedean.ParticleKnots failed, environment already contains
'QOU.Archimedean.R_q' from QOU.Archimedean.GroundRing`. Bean `qou-lksc`. -/

/-- The formal parameter `q` of the ground ring. -/
noncomputable def q_param : R_q := LaurentPolynomial.T 1

/-- The formal parameter `q⁻¹` of the ground ring. -/
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The electron: the braid word `σ₀σ₁σ₀ ∈ B₃` (owner ruling 2026-11-21), whose
closure is the positive Hopf link `T_{2,2}`. Until 2026-11-21 this structure
recorded the trefoil `T_{2,3}`; the trefoil braid `σ₀³ ∈ B₂` is the documented
backup (`docs/audits/2026-11-21-electron-word-options-downstream.md`). -/
structure Electron where
  /-- Letters of the braid word `σ₀σ₁σ₀`, all positive. -/
  braidLetters : List (Fin 2) := [0, 1, 0]
  /-- Torus link parameter p: the Hopf link is `T_{2,2}`. -/
  torusP : ℕ := 2
  /-- Torus link parameter n: the Hopf link is `T_{2,2}`. -/
  torusN : ℕ := 2
  /-- Crossing number of the Hopf link (the word has 3 letters; it is not minimal). -/
  crossing_number : ℕ := 2
  /-- Seifert genus of the Hopf link (its minimal Seifert surface is an annulus). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (torus link → non-hyperbolic). -/
  volume : R_q := 0
  /-- Coulomb charge: −1 (from crossing chirality). -/
  charge : ℤ := -1
  /-- Orientation: +1 for particle (forward time). -/
  orientation : ℤ := 1

/-- The positron: the conjugate word `σ₀⁻¹σ₁⁻¹σ₀⁻¹ ∈ B₃` with reversed crossings,
whose closure is the negative Hopf link. Until 2026-11-21 this structure recorded the
mirror trefoil. -/
structure Positron where
  /-- Letters of the braid word `σ₀⁻¹σ₁⁻¹σ₀⁻¹` (every letter inverted). -/
  braidLetters : List (Fin 2) := [0, 1, 0]
  /-- Torus link parameter p (same as the electron's Hopf link). -/
  torusP : ℕ := 2
  /-- Torus link parameter n (same as the electron's Hopf link). -/
  torusN : ℕ := 2
  /-- Crossing number (same as the Hopf link). -/
  crossing_number : ℕ := 2
  /-- Seifert genus (same as the Hopf link). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (torus link → non-hyperbolic). -/
  volume : R_q := 0
  /-- Coulomb charge: +1 (reversed crossing chirality). -/
  charge : ℤ := 1
  /-- Orientation: −1 for antiparticle (reversed time direction). -/
  orientation : ℤ := -1

/-- The neutrino: unknot `K_{0₁}` with trivial knot invariants. -/
structure Neutrino where
  /-- Crossing number of the unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus of the unknot. -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : R_q := 0
  /-- Jones polynomial `J_ν(q) = 1` for all `q`. -/
  jones_trivial : ∀ q : R_q, (1 : R_q) = 1 := fun _ => rfl
  /-- Coulomb charge contribution: zero (no crossings). -/
  charge : ℤ := 0
  /-- Orientation: +1 for particle (vs. −1 for antiparticle). -/
  orientation : ℤ := 1

/-- The antineutrino: mirror unknot with reversed orientation. -/
structure Antineutrino where
  /-- Crossing number (trivial knot). -/
  crossing_number : ℕ := 0
  /-- Seifert genus. -/
  genus : ℕ := 0
  /-- Hyperbolic volume. -/
  volume : R_q := 0
  /-- Jones polynomial evaluated at any `q` is 1. -/
  jones_trivial : ∀ q : R_q, (1 : R_q) = 1 := fun _ => rfl
  /-- Orientation: −1 for antiparticle. -/
  orientation : ℤ := -1

/-- The up quark: unknot `K_{0₁}` with positive crossing orientation,
    threaded through a color tube in the Borromean link `B₃`. -/
structure UpQuark where
  /-- Crossing number of the underlying unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus (trivial knot). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : R_q := 0
  /-- Crossing orientation: +1 for positive (contributes `+q` to Skein). -/
  crossing_orientation : ℤ := 1
  /-- Number of Borromean components this quark links with. -/
  borromean_links : ℕ := 2
  /-- Coulomb charge numerator (charge = numerator / 3). -/
  charge_numerator : ℤ := 2
  /-- Coulomb charge denominator. -/
  charge_denominator : ℕ := 3
  /-- Color-confined: cannot be isolated from `B₃`. -/
  confined : Bool := true

/-- The down quark: unknot `K_{0₁}` with negative crossing orientation. -/
structure DownQuark where
  /-- Crossing number of the underlying unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus (trivial knot). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : R_q := 0
  /-- Crossing orientation: −1 for negative (contributes `−q⁻¹` to Skein). -/
  crossing_orientation : ℤ := -1
  /-- Number of Borromean components this quark links with. -/
  borromean_links : ℕ := 2
  /-- Coulomb charge numerator (charge = numerator / 3). -/
  charge_numerator : ℤ := -1
  /-- Coulomb charge denominator. -/
  charge_denominator : ℕ := 3
  /-- Color-confined: cannot be isolated from `B₃`. -/
  confined : Bool := true

end QOU.Archimedean
