# GAP 6a + 18a — scoping audit

**Date:** 2026-05-04
**Branch:** `claude/gap-6a-18a-scoping`
**Status:** scoping only — neither GAP closed.

## Purpose

Document the precise mathematical work remaining to close
[GAP 6a (motivic Galois character instance)](2026-05-02-forward-derivation-pre-archimedean.md#step-6--substrate-motivic-galois-character)
and
[GAP 18a (closed-form mass endomorphism)](2026-05-02-forward-derivation-pre-archimedean.md#step-18--mass-endomorphism-tower).
Both are listed in the workplan as research-grade
([P3.5](2026-05-01-math-framework-workplan.md#p35--family-4-motivic-substrate-instance-at-q_0)
open-ended; P18a multi-week).

## Class architecture is in place

Both GAPs already have the conditional-class scaffolding required by
CLAUDE.md §3b:

| Class | File | Status |
|-------|------|--------|
| `MotivicSubstrate` | [`lean/QOU/AlgebraicSubstrate/MotivicSubstrate.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/MotivicSubstrate.lean) | axiomatised |
| `MotivicGaloisCharacter` | [`lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean) | axiomatised |
| `MassEndomorphism` | [`braids-and-knots/mass-endomorphism-conjecture.lean`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-conjecture.lean) | axiomatised |
| `MassEvaluation` (Arch) | [`braids-and-knots/mass-endomorphism-tower.lean`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean) | axiomatised |

`motivic_perpetual_obstruction` is **proved** conditionally on the class
([`MotivicPerpetualObstruction.lean:49`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean));
multiple `MassEndomorphism` corollaries (`fullMass_eq_volume`,
`transient_unique`, `descended_eq_vol_minus_transient`,
`fullMass_pos_of_vol_pos`) are proved conditionally on the class.

**What's missing:** a concrete `instance` for the QOU substrate at q₀
(GAP 6a) and a deterministic recipe `Braid → MassEndomorphism`
(GAP 18a). The classes themselves are non-contradictory — see the
trivial witness instances landed alongside this doc.

## GAP 6a — motivic Galois character instance

### What "closed" means precisely

A concrete `instance : MotivicGaloisCharacter K0 Mhat motiveA` for
the QOU substrate, where:

1. `K0` is the Grothendieck ring of varieties over ℚ (or the appropriate
   subring containing `[A]`),
2. `Mhat` is the dimension-completed localisation `K₀[𝕃⁻¹]^∧`,
3. `motiveA = [A]` is the motivic class of the QOU Frobenius–Hopf
   algebra,
4. **`frobenius_at p : Mhat`** is the actual local Frobenius
   eigenvalue at finite prime `p`, derived from the brane-tower
   p-adic realisation,
5. `almost_everywhere_nontrivial` is established (the bad set
   `S = {primes dividing χ(A)}` is finite and non-trivially backed).

### The substantive mathematical work

- **Identify the substrate variety.** The QOU substrate parameter
  `q₀ ≈ 1.1097` is pinned by `q⁴(q-1) = 1` (see
  [`q-pinning-50-digit.witness.json`](../../computations/q-pinning-50-digit.witness.json)).
  This makes `q₀` a root of `T⁵ − T⁴ − 1 ∈ ℤ[T]` — a degree-5
  algebraic number. The minimal polynomial defines an algebraic
  variety `Spec(ℤ[T]/(T⁵−T⁴−1))` whose generic fibre carries the
  substrate.
- **Construct the brane-tower realisation at p.** For each finite
  prime `p ∤ disc(T⁵−T⁴−1)`, the substrate variety has a smooth
  reduction mod p. The local Frobenius `Frob_p` acts on the étale
  cohomology of this reduction; its eigenvalues are the local
  Frobenius eigenvalues on `[A]`.
- **Compute eigenvalues.** For small primes `p ∈ {3, 5, 7, 11, …}`,
  the eigenvalues can be computed numerically by reducing
  `T⁵−T⁴−1 mod p`, factoring, and reading off the Frobenius traces.
  This is a concrete-enough computation to script (see proposed
  compute below).
- **Show non-units.** For `p` not dividing the algebraic discriminant
  `disc(T⁵−T⁴−1) = 2869`, the eigenvalues are `p`-Weil numbers and
  hence not units in `Mhat` (their absolute values are integral
  multiples of √p, not 1).

### Tractable next step

Land a Python compute that, for `p ∈ {3, 5, 7, 11, 13, 17, 19, 23}`:

1. Reduces `T⁵ − T⁴ − 1` mod `p` and factors over `𝔽_p`.
2. Computes the Frobenius trace `a_p = Tr(Frob_p | H¹_ét)` from
   the factorisation.
3. Records `frobenius_at p ↦ a_p` as a witness, with a JSON manifest
   matching the LP/SDP-witness convention.

This is **not** a closed-form derivation but provides the
empirical evidence that the conjectural instance is consistent.

### Why not closeable in one session

- Requires choosing `K0` precisely (which Grothendieck ring; with
  what coefficients).
- Requires `Mhat` to carry the dimension completion structure
  (Mathlib does not have this off the shelf).
- The Lean encoding of "Frobenius at p" requires either (a)
  importing Mathlib's `EllipticCurve.Frobenius` or analogous
  machinery, or (b) defining a bespoke Frobenius on the
  substrate variety, which is itself ~weeks of work.

## GAP 18a — closed-form mass endomorphism

### What "closed" means precisely

A deterministic Lean function

```lean
def closedFormInstance {R : Type*} [CommRing R] (β : Braid n) :
    MassEndomorphism R β
```

producing the instance fields from `β` algorithmically. Specifically:

- `q : R` — supplied by caller (the substrate parameter).
- `N : ℕ` — `2n − 1` (`n` single-generator centres + `n−1`
  adjacent-pair centres).
- `z : Fin N → R` — the algebraic-volume coordinates, computed
  from `β` via the Wedderburn decomposition + GS-filtration
  partial-fraction split (the
  [`term6_residues_at_roots.py`](../../computations/term6_residues_at_roots.py)
  pipeline produces these numerically; the closed form requires
  the symbolic chain).
- `tr_transient : R` — `Σᵢ Φ_q(z i)`.
- `tr_descended : R` — `tr_M(ρ(β))` (Markov trace of the Hecke
  image; computable via the existing `MarkovTrace` class).
- `vol_identity : R` — `Vol(K_β)/ℏ_q²` (Thurston volume of the
  braid closure divided by `ℏ_q²`); this is the *conjectural*
  field — the mass-endomorphism conjecture **is** the equality
  `tr_transient = vol_identity − tr_descended`.

### The substantive mathematical work

- **The volume identity** (`vol_eq` field) is precisely the
  open conjecture. Closing it is equivalent to proving the
  Volume Conjecture for the braid closure `K_β` in the QOU
  framework. A concrete recipe that produces `vol_identity` from
  `β` can either:
  - **(a) Compute `Vol(K_β)/ℏ_q²` independently** (e.g. via
    SnapPy for the closure), in which case the recipe gives a
    *fitting* statement, not a derivation. Per CLAUDE.md, fits
    are recorded as conjectures; no Lean closure.
  - **(b) Define `vol_identity := tr_descended + tr_transient`**
    by fiat, in which case `vol_eq` becomes `rfl` — but this
    elides the Volume Conjecture and is not what's wanted.
- **The transient component** `tr_transient = Σᵢ Φ_q(z i)` requires
  the Habiro-ring evaluation of `Φ_q` at the formal coordinates
  `z i`. These are the residues at primitive roots of unity computed
  by [`term6_residues_at_roots.py`](../../computations/term6_residues_at_roots.py)
  — the pipeline is real, but the symbolic closed form for the
  full sum (Mittag-Leffler decomposition of `tr_M(q)` into
  pole-residue contributions) is what's open.

### Tractable next step

The most tractable partial closure is a **Hecke-side recipe** that
produces every field except `vol_identity`. Specifically:

1. Take `β` as a list of generator indices.
2. Compute `tr_descended` via the existing
   [`Hecke/MarkovTrace.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/MarkovTrace.lean)
   (`trace_decomposition` is now proved per PR #492).
3. Compute the `z i` values via the GS-filtration partial-fraction
   split (Term 6 pipeline).
4. Define `tr_transient := Σᵢ Φ_q (z i)`.
5. Leave `vol_identity` as a *parameter* — accept it from the
   caller. The recipe then produces a `MassEndomorphism` instance
   *parameterised by* the conjectural `vol_identity`.

This is the shape of "closed-form modulo the Volume Conjecture":
every mechanical computation is automated; the only input is the
single conjectural scalar.

### Why not closeable in one session

- Requires bridging the Term 6 numerical pipeline (Python + sympy)
  with the Lean symbolic side. The witness JSON has the data; the
  Lean closed form needs it as polynomial-time-computable
  expressions.
- The Volume Conjecture for braid closures over the QOU substrate
  is open; no formalisation in any prover.

## Trivial witness instances landed in this branch

Both classes are confirmed inhabitable:

- [`lean/QOU/LiftingDescent/MotivicGaloisCharacterTrivial.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicGaloisCharacterTrivial.lean) —
  trivial substrate over `K0 = Mhat = ℤ`,
  `Target = const ℤ`, `frobenius_at p := (p : ℤ)`. Witnesses
  `motivic_perpetual_obstruction` non-vacuously.
- [`lean/QOU/MassEndomorphism/MassEndomorphismTrivial.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/MassEndomorphismTrivial.lean) —
  zero-mass instance over `R = ℤ` (`tr_descended = tr_transient =
  vol_identity = 0`). Witnesses `fullMass_eq_volume` non-vacuously.

These guard against accidental class over-constraint. They do
**not** close GAP 6a or 18a.

## Summary

| GAP | Class scaffold | Trivial instance | Concrete instance | Closed |
|-----|----------------|------------------|-------------------|--------|
| 6a  | ✓ | ✓ (this branch) | open | open |
| 18a | ✓ | ✓ (this branch) | open | open |

Both GAPs are well-defined and structurally ready; neither is
closeable without dedicated mathematical research.
