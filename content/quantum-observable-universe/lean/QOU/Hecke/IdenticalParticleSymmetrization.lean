import Mathlib.Tactic.Ring

/-!
# QOU.Hecke.IdenticalParticleSymmetrization — Schur–Weyl decomposition of the
  identical-nucleon constituent power

The canonical mass-tower constituent factorization (Step 5l,
`closed_form_tau_M.py:302`) is
`tr_M(𝓑_K) = tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏ fᵢ`, where the `^Z`/`^N` are
**plain powers** — Wenzl disjoint multiplicativity, i.e. the trace of the
*distinguishable* tensor power `V^{⊗Z}` (the power sum `p₁^Z = (tr V)^Z`).

For **identical** nucleons that is the wrong object: the physical trace must
project onto a definite symmetry sector under the block-permutation group `S_Z`.
By Schur–Weyl duality the distinguishable power decomposes as

  `p₁^Z  =  Σ_{λ ⊢ Z}  f^λ · s_λ`        (`f^λ = #SYT(λ) = dim` of the `S_Z` irrep)

so the naive `tr_M³(𝓑_p)^Z` is the FULL sum over symmetry sectors; an
identical-particle (e.g. doubly-magic, Pauli-closed) state lives in ONE sector
`s_λ`. The missing-symmetrization gap (`docs/audits/2026-06-10-missing-
identical-nucleon-symmetrization.md`) is precisely that the tower keeps the full
power instead of the physical sector.

This module proves the decomposition for the two smallest occupations,
machine-checked (axioms `propext`/`Classical.choice`/`Quot.sound` only — no
`sorry`):

* **Z = 2** (⁴He: the proton pair, the neutron pair). `p₁² = s₍₂₎ + s₍₁,₁₎ =
  h₂ + e₂`, multiplicities `f^(2)=1, f^(1,1)=1`. The square splits into
  symmetric (`h₂`) + antisymmetric (`e₂`); the doubly-magic pp/nn pairing is the
  `S₂`-sector projection the plain power omits.
* **Z = 3** (Li: ppp / nnn). `p₁³ = s₍₃₎ + 2·s₍₂,₁₎ + s₍₁,₁,₁₎`, multiplicities
  `f^(3)=1, f^(2,1)=2, f^(1,1,1)=1` — the standard rep enters with multiplicity 2.

General theme (Z ≥ 4, composite Z): `S_Z` then has a non-trivial Young-subgroup
lattice (`S_4 ⊃ S₂≀S₂ ⊃ V₄`; `S_6 ⊃ S₂×S₃` …), giving the sub-shell structure
whose closures are the nuclear magic numbers. The `Z=2` Klein `V₄ ◁ S₄` with
`S₄/V ≅ S₃` recovers the `6 = |S₃| = χ(Bring)` Bring symmetry (Step 4).

Self-contained (`CommRing` identities, `import Mathlib.Tactic.Ring` only) — does
NOT depend on the rest of `QOU.Hecke`, so it builds independently.

## References
- [manuscript] `docs/audits/2026-06-10-missing-identical-nucleon-symmetrization.md`
- Schur–Weyl duality; symmetric functions (Macdonald, *Symmetric Functions and
  Hall Polynomials*).
-/

namespace QOU.Hecke.IdenticalParticle

variable {R : Type*} [CommRing R]

/-- **Z = 2 Schur–Weyl** (⁴He pp / nn). The naive distinguishable square
`p₁² = (a+b)²` splits into the `S₂` symmetric sector `s₍₂₎ = h₂ = a²+ab+b²`
(multiplicity `f^(2)=1`) and the antisymmetric sector `s₍₁,₁₎ = e₂ = ab`
(`f^(1,1)=1`). An identical proton/neutron pair occupies one sector — the
doubly-magic projection the plain `^Z` power discards. -/
theorem schur_weyl_Z2 (a b : R) :
    (a + b) ^ 2 = (a ^ 2 + a * b + b ^ 2) + a * b := by ring

/-- The two `S₂` sectors via the power sums `p₁ = a+b`, `p₂ = a²+b²`
(no division): `2·h₂ = p₁² + p₂`. -/
theorem two_h2 (a b : R) :
    2 * (a ^ 2 + a * b + b ^ 2) = (a + b) ^ 2 + (a ^ 2 + b ^ 2) := by ring

/-- `2·e₂ = p₁² − p₂` — the antisymmetric (Pauli) sector. -/
theorem two_e2 (a b : R) :
    2 * (a * b) = (a + b) ^ 2 - (a ^ 2 + b ^ 2) := by ring

/-- **Z = 3 Schur–Weyl** (Li ppp / nnn). `p₁³` decomposes into the symmetric
`s₍₃₎ = h₃` (`f^(3)=1`), the standard rep `s₍₂,₁₎` with **multiplicity 2**
(`f^(2,1)=2`), and the antisymmetric `s₍₁,₁,₁₎ = e₃ = abc` (`f^(1,1,1)=1`). The
`1,2,1` are the `#SYT` of `S₃`; `Σ (f^λ)² = 1+4+1 = 6 = 3! = |S₃|`. -/
theorem schur_weyl_Z3 (a b c : R) :
    (a + b + c) ^ 3
      = (a ^ 3 + b ^ 3 + c ^ 3
          + a ^ 2 * b + a ^ 2 * c + b ^ 2 * a + b ^ 2 * c + c ^ 2 * a + c ^ 2 * b
          + a * b * c)
        + 2 * ((a ^ 2 * b + a ^ 2 * c + b ^ 2 * a + b ^ 2 * c + c ^ 2 * a
                + c ^ 2 * b) + 2 * (a * b * c))
        + a * b * c := by ring

end QOU.Hecke.IdenticalParticle
