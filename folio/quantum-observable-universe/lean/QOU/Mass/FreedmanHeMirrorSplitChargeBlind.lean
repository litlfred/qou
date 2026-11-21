/-
QOU.Mass.FreedmanHeMirrorSplitChargeBlind — the Freedman–He link bound cannot
produce an A-dependent mirror split from a charge-only flux.

Arc context (em-linking; beans `qou-o6ml`, `qou-0hdx`). The Freedman–He energy
bound for a divergence-free field on an invariant domain modelled on an
`n`-component link `L`, as stated by Komendarczyk (arXiv:0808.1533v1, eq. (43),
p. 26; verified in this repo at
`library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216`), is

  `E_{3/2}(X) ≥ (π/16)^{1/4} · (Σ_{k=1..n} ac(L_k, L)|Flux(X_k)|) · min_k |Flux(X_k)|`

Every factor on the right is either link topology (`ac`) or flux. **Nothing in it
distinguishes a proton from a neutron.** But the observable the em-linking arc
scores against — `κ(A)`, built from the mirror-pair binding split — is pure
charge. So charge can enter the bound at exactly one place: the flux must differ
between proton and neutron components.

This file asks what that buys, and the answer is: not enough. Take a carrier link
that is **vertex-transitive**, so `ac(L_k, L) = a` for every component `k` — true
of the Borromean rings (whose complement carries an `S₃` symmetry) and of every
carrier this arc has used. Assign each component a flux by its charge: `φp` for
the `Z` protons, `φn` for the `N` neutrons. Mirror partners `(Z, N)` and `(N, Z)`
share `A`, share the link, and share `min_k |Flux|` — the swap only relabels
which components carry which flux. Then the mirror split is

  `Δ = C·a·m·(Z − N)·(φp − φn)`,

which for the `d = |Z − N| = 1` ladder is **one constant, independent of the
nucleus** (`mirrorSplit_succ_const`, `mirrorSplit_succ_eq_of_ne`).

The measured ladder is not constant: the AME mirror split grows by a factor of
13.63 from `A = 3` to `A = 63`
(`computations/em-linking-fh-mirror-split-charge-blindness.witness.json`). So
constant charge-fluxes are refuted, and the required `φp − φn` must **grow** by
that factor — where the corpus had recorded the obligation as a flux *decline* of
1.449. That 1.449 is `√(κ(3)/κ(41))`, read off `κ`; but `κ := split/((Z−1)·u)`
with `u` constant to 5.0e-8, so the pair count is already divided out and `κ` is
not the energy eq. (43) bounds.

SCOPE — this is a **scope-(a)** exclusion of a model class, not of eq. (43).
What is excluded is `{vertex-transitive carrier} × {flux depending only on
charge} × {saturation}`. Three escapes survive and are *not* refuted here: a
carrier that is not vertex-transitive; an `ac` depending on the charge
assignment; an unsaturated bound (eq. (43) is an inequality, and using it as an
equality is an assumption this corpus nowhere establishes). Each is a further
thing that would have to be derived.

Base ring: generic `CommRing R` per AGENTS.md §7c. Nothing here needs an
ordering, a square root, or any archimedean construct — the content is the
cancellation in the swap, which is ring algebra.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Cast.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Push

namespace QOU.Mass.FreedmanHeMirrorSplitChargeBlind

variable {R : Type*} [CommRing R]

/-- The right-hand side of the Freedman–He link bound (Komendarczyk eq. (43))
specialised to a **vertex-transitive** carrier and a **charge-only** flux.

`C` is the pure constant `(π/16)^{1/4}`, `a` the common component value
`ac(L_k, L)`, `m` the factor `min_k |Flux(X_k)|`, and the `Z` proton components
carry flux `φp` while the `N` neutron components carry `φn`. The sum
`Σ_k ac(L_k,L)|Flux(X_k)|` collapses to `a · (Z·φp + N·φn)`. -/
def fhBound (C a φp φn m : R) (Z N : ℕ) : R :=
  C * a * ((Z : R) * φp + (N : R) * φn) * m

/-- The mirror split: the bound's value on `(Z, N)` minus its value on the
mirror partner `(N, Z)`. Mirror partners share `A = Z + N`, share the carrier
link, and share `m` — the swap only relabels which components are charged, so
every ingredient except the charge assignment is held fixed. -/
def mirrorSplit (C a φp φn m : R) (Z N : ℕ) : R :=
  fhBound C a φp φn m Z N - fhBound C a φp φn m N Z

/-- **The split factorises**: all dependence on the nucleus enters through the
single integer `Z − N`, multiplying the flux *difference*.

This is the charge-blindness of eq. (43) made explicit: the topology (`a`), the
constant (`C`) and the minimum (`m`) survive the subtraction untouched, and the
component counts survive only in the combination `Z − N`. -/
theorem mirrorSplit_eq (C a φp φn m : R) (Z N : ℕ) :
    mirrorSplit C a φp φn m Z N
      = C * a * m * (((Z : R) - (N : R)) * (φp - φn)) := by
  unfold mirrorSplit fhBound
  ring

/-- **The refutation, for the `d = 1` ladder.** Every mirror pair with
`Z = N + 1` — which is the whole `A = 2Z − 1` series the arc scores against —
gets the *same* split `C·a·m·(φp − φn)`, with no dependence on `N` whatsoever. -/
theorem mirrorSplit_succ_const (C a φp φn m : R) (N : ℕ) :
    mirrorSplit C a φp φn m (N + 1) N = C * a * m * (φp - φn) := by
  rw [mirrorSplit_eq]
  push_cast
  ring

/-- Stated as the falsifiable claim: **two different nuclei on the `d = 1` ladder
have equal splits.** The AME ladder disagrees by a factor of 13.63 across
`A = 3…63`, so the hypotheses of this theorem — a vertex-transitive carrier, a
flux depending only on charge, and a saturated bound — cannot all hold. -/
theorem mirrorSplit_succ_eq_of_ne (C a φp φn m : R) (N₁ N₂ : ℕ) :
    mirrorSplit C a φp φn m (N₁ + 1) N₁ = mirrorSplit C a φp φn m (N₂ + 1) N₂ := by
  rw [mirrorSplit_succ_const, mirrorSplit_succ_const]

/-- The split vanishes identically when the two fluxes agree. So a charge-blind
flux assignment predicts **no** mirror splitting at all — the bound cannot even
produce the effect, let alone its `A`-dependence. This is the degenerate case
that forces `φp ≠ φn` before any fitting begins. -/
theorem mirrorSplit_eq_zero_of_flux_eq (C a φ m : R) (Z N : ℕ) :
    mirrorSplit C a φ φ m Z N = 0 := by
  rw [mirrorSplit_eq, sub_self, mul_zero, mul_zero]

/-- A `d`-fold generalisation: for `Z = N + d` the split scales *linearly* in the
charge asymmetry `d` and in nothing else. So even off the `d = 1` ladder the
bound offers only one free integer, and it is not `A`. -/
theorem mirrorSplit_add_eq (C a φp φn m : R) (N d : ℕ) :
    mirrorSplit C a φp φn m (N + d) N = C * a * m * ((d : R) * (φp - φn)) := by
  rw [mirrorSplit_eq]
  push_cast
  ring

end QOU.Mass.FreedmanHeMirrorSplitChargeBlind
