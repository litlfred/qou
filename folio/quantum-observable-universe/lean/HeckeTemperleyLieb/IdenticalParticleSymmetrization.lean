import Mathlib.Tactic.Ring
import Mathlib.Algebra.Group.Basic

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
* **Z = 4** (⁸Be / first composite Z: the pp-pp, nn-nn double shells).
  `p₁⁴ = s₍₄₎ + 3·s₍₃,₁₎ + 2·s₍₂,₂₎ + 3·s₍₂,₁,₁₎ + s₍₁,₁,₁,₁₎`, multiplicities
  `f^(4)=1, f^(3,1)=3, f^(2,2)=2, f^(2,1,1)=3, f^(1,1,1,1)=1`
  (`Σ (f^λ)² = 1+9+4+9+1 = 24 = 4!`). The `(2,2)` sector (multiplicity 2) and the
  Klein `V₄ ◁ S₄` with `S₄/V₄ ≅ S₃` carry the double-pair (pp × nn) exchange and
  recover the `6 = |S₃| = χ(Bring)` Bring symmetry (Step 4).

General theme (composite Z ≥ 6): `S_Z` has a non-trivial Young-subgroup lattice
(`S_6 ⊃ S₂×S₃`; `S_8 ⊃ S₂≀S₄` …), giving the sub-shell structure whose closures
are the nuclear magic numbers.

Self-contained (`CommRing` identities, `import Mathlib.Tactic.Ring` only) — does
NOT depend on the rest of `QOU.Hecke`, so it builds independently.

## References
- [leitner2026] `docs/audits/2026-06-10-missing-identical-nucleon-symmetrization.md`
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

/-- **Z = 4 Schur–Weyl** (⁸Be / first composite Z: pp-pp, nn-nn double shells).
The naive distinguishable `p₁⁴` decomposes over the five `S₄` irreps with
multiplicities `f^λ = #SYT(λ)`: `f^(4)=1, f^(3,1)=3, f^(2,2)=2, f^(2,1,1)=3,
f^(1,1,1,1)=1`, so `Σ (f^λ)² = 1+9+4+9+1 = 24 = 4! = |S₄|`. The `(2,2)` sector
enters with **multiplicity 2** and the Klein `V₄ ◁ S₄` (`S₄/V₄ ≅ S₃`) carries the
double-pair (pp × nn) exchange — recovering the `6 = |S₃| = χ(Bring)` Bring
symmetry of Step 4. Each `s_λ` is in the monomial-symmetric basis
`s_λ = Σ_μ K_{λμ} m_μ` (Kostka numbers `K`); the five groups below are
`s₍₄₎`, `3·s₍₃,₁₎`, `2·s₍₂,₂₎`, `3·s₍₂,₁,₁₎`, `s₍₁,₁,₁,₁₎`. Sympy- and
bialternant-verified; `ring`-closed. -/
theorem schur_weyl_Z4 (a b c d : R) :
    (a + b + c + d) ^ 4
      = -- s₍₄₎ = h₄ = m₄ + m₃₁ + m₂₂ + m₂₁₁ + m₁₁₁₁   (f^(4) = 1)
        ((a ^ 4 + b ^ 4 + c ^ 4 + d ^ 4)
          + (a ^ 3 * b + a ^ 3 * c + a ^ 3 * d + b ^ 3 * a + b ^ 3 * c + b ^ 3 * d
             + c ^ 3 * a + c ^ 3 * b + c ^ 3 * d + d ^ 3 * a + d ^ 3 * b + d ^ 3 * c)
          + (a ^ 2 * b ^ 2 + a ^ 2 * c ^ 2 + a ^ 2 * d ^ 2 + b ^ 2 * c ^ 2
             + b ^ 2 * d ^ 2 + c ^ 2 * d ^ 2)
          + (a ^ 2 * b * c + a ^ 2 * b * d + a ^ 2 * c * d + b ^ 2 * a * c
             + b ^ 2 * a * d + b ^ 2 * c * d + c ^ 2 * a * b + c ^ 2 * a * d
             + c ^ 2 * b * d + d ^ 2 * a * b + d ^ 2 * a * c + d ^ 2 * b * c)
          + a * b * c * d)
        -- 3 · s₍₃,₁₎ = 3·(m₃₁ + m₂₂ + 2·m₂₁₁ + 3·m₁₁₁₁)   (f^(3,1) = 3)
        + 3 * ((a ^ 3 * b + a ^ 3 * c + a ^ 3 * d + b ^ 3 * a + b ^ 3 * c + b ^ 3 * d
                 + c ^ 3 * a + c ^ 3 * b + c ^ 3 * d + d ^ 3 * a + d ^ 3 * b + d ^ 3 * c)
               + (a ^ 2 * b ^ 2 + a ^ 2 * c ^ 2 + a ^ 2 * d ^ 2 + b ^ 2 * c ^ 2
                  + b ^ 2 * d ^ 2 + c ^ 2 * d ^ 2)
               + 2 * (a ^ 2 * b * c + a ^ 2 * b * d + a ^ 2 * c * d + b ^ 2 * a * c
                      + b ^ 2 * a * d + b ^ 2 * c * d + c ^ 2 * a * b + c ^ 2 * a * d
                      + c ^ 2 * b * d + d ^ 2 * a * b + d ^ 2 * a * c + d ^ 2 * b * c)
               + 3 * (a * b * c * d))
        -- 2 · s₍₂,₂₎ = 2·(m₂₂ + m₂₁₁ + 2·m₁₁₁₁)   (f^(2,2) = 2)
        + 2 * ((a ^ 2 * b ^ 2 + a ^ 2 * c ^ 2 + a ^ 2 * d ^ 2 + b ^ 2 * c ^ 2
                 + b ^ 2 * d ^ 2 + c ^ 2 * d ^ 2)
               + (a ^ 2 * b * c + a ^ 2 * b * d + a ^ 2 * c * d + b ^ 2 * a * c
                  + b ^ 2 * a * d + b ^ 2 * c * d + c ^ 2 * a * b + c ^ 2 * a * d
                  + c ^ 2 * b * d + d ^ 2 * a * b + d ^ 2 * a * c + d ^ 2 * b * c)
               + 2 * (a * b * c * d))
        -- 3 · s₍₂,₁,₁₎ = 3·(m₂₁₁ + 3·m₁₁₁₁)   (f^(2,1,1) = 3)
        + 3 * ((a ^ 2 * b * c + a ^ 2 * b * d + a ^ 2 * c * d + b ^ 2 * a * c
                 + b ^ 2 * a * d + b ^ 2 * c * d + c ^ 2 * a * b + c ^ 2 * a * d
                 + c ^ 2 * b * d + d ^ 2 * a * b + d ^ 2 * a * c + d ^ 2 * b * c)
               + 3 * (a * b * c * d))
        -- s₍₁,₁,₁,₁₎ = e₄ = m₁₁₁₁ = abcd   (f^(1,1,1,1) = 1)
        + a * b * c * d := by ring

/-! ## Newton–Frobenius power-sum form (the bosonic/fermionic constituents)

The symmetrized constituent of `symmetrized_constituent_general.py` is computed
by the Frobenius formula `h_Z = Σ_{μ⊢Z} p_μ/z_μ`, `e_Z = Σ_{μ⊢Z} ε_μ p_μ/z_μ`,
with power sums `p_k = tr_M(B_p^k)` and centralizer orders `z_μ`. The lemmas below
are that formula in closed `ring`-verified form for Z = 2, 3, 4: the complete-
homogeneous `h_Z` (bosonic sector) and elementary `e_Z` (fermionic / Pauli sector)
written against the power sums `p_k = Σ xᵢ^k`. Multiplying through by `Z!` clears
the `1/z_μ` denominators so the statement holds over any `CommRing` (no division).
For Z = 2 this is `two_h2` / `two_e2` above. -/

/-- **Newton–Frobenius Z=3, bosonic.** `6·h₃ = p₁³ + 3p₁p₂ + 2p₃`
(`z₍₁,₁,₁₎=6, z₍₂,₁₎=2, z₍₃₎=3`; coefficients `3! / z_μ = 1,3,2`). `h₃` is the
complete-homogeneous degree-3 symmetric function in `a,b,c`. -/
theorem newton_h3 (a b c : R) :
    6 * (a ^ 3 + a ^ 2 * b + a ^ 2 * c + a * b ^ 2 + a * b * c + a * c ^ 2
         + b ^ 3 + b ^ 2 * c + b * c ^ 2 + c ^ 3)
      = (a + b + c) ^ 3 + 3 * (a + b + c) * (a ^ 2 + b ^ 2 + c ^ 2)
        + 2 * (a ^ 3 + b ^ 3 + c ^ 3) := by ring

/-- **Newton–Frobenius Z=3, fermionic.** `6·e₃ = p₁³ − 3p₁p₂ + 2p₃`, `e₃ = abc`
(signs `ε_μ = (−1)^{3−ℓ(μ)}`). -/
theorem newton_e3 (a b c : R) :
    6 * (a * b * c)
      = (a + b + c) ^ 3 - 3 * (a + b + c) * (a ^ 2 + b ^ 2 + c ^ 2)
        + 2 * (a ^ 3 + b ^ 3 + c ^ 3) := by ring

/-- **Newton–Frobenius Z=4, bosonic.** `24·h₄ = p₁⁴ + 6p₁²p₂ + 3p₂² + 8p₁p₃ + 6p₄`
(`4!/z_μ = 1,6,3,8,6` over `μ = (1⁴),(2,1,1),(2,2),(3,1),(4)`). -/
theorem newton_h4 (a b c d : R) :
    24 * (a ^ 4 + a ^ 3 * b + a ^ 3 * c + a ^ 3 * d + a ^ 2 * b ^ 2 + a ^ 2 * b * c
          + a ^ 2 * b * d + a ^ 2 * c ^ 2 + a ^ 2 * c * d + a ^ 2 * d ^ 2 + a * b ^ 3
          + a * b ^ 2 * c + a * b ^ 2 * d + a * b * c ^ 2 + a * b * c * d + a * b * d ^ 2
          + a * c ^ 3 + a * c ^ 2 * d + a * c * d ^ 2 + a * d ^ 3 + b ^ 4 + b ^ 3 * c
          + b ^ 3 * d + b ^ 2 * c ^ 2 + b ^ 2 * c * d + b ^ 2 * d ^ 2 + b * c ^ 3
          + b * c ^ 2 * d + b * c * d ^ 2 + b * d ^ 3 + c ^ 4 + c ^ 3 * d + c ^ 2 * d ^ 2
          + c * d ^ 3 + d ^ 4)
      = (a + b + c + d) ^ 4
        + 6 * (a + b + c + d) ^ 2 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2)
        + 3 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2) ^ 2
        + 8 * (a + b + c + d) * (a ^ 3 + b ^ 3 + c ^ 3 + d ^ 3)
        + 6 * (a ^ 4 + b ^ 4 + c ^ 4 + d ^ 4) := by ring

/-- **Newton–Frobenius Z=4, fermionic.** `24·e₄ = p₁⁴ − 6p₁²p₂ + 3p₂² + 8p₁p₃ − 6p₄`,
`e₄ = abcd` (signs `ε_μ`). -/
theorem newton_e4 (a b c d : R) :
    24 * (a * b * c * d)
      = (a + b + c + d) ^ 4
        - 6 * (a + b + c + d) ^ 2 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2)
        + 3 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2) ^ 2
        + 8 * (a + b + c + d) * (a ^ 3 + b ^ 3 + c ^ 3 + d ^ 3)
        - 6 * (a ^ 4 + b ^ 4 + c ^ 4 + d ^ 4) := by ring

/-! ## Orbit identity ≠ Young symmetrizer (relabeling vs. composition)

A recurring confusion (`block_swap_binding.py`, `symmetrized_binding_probe.py`):
the **orbit identity** `tr_M(β_{Z,N}) = tr_M(rep)` (`atom_orbit_reduction.py`)
is **relabeling** — a same-species permutation leaves the canonical word
`p…pn…n` fixed, so it acts by CONJUGATION `β_σ W β_σ⁻¹`, and any cyclic trace is
conjugation-invariant (Markov M1). The identical-particle **Young symmetrizer** is
a DIFFERENT object: the COMPOSITION average `|G|⁻¹ Σ_σ tr_M(W·β_σ)` (not
conjugation), which the inter-nucleon bonds make `≠ tr_M(W)` — measured as
`S_atom ≠ S_free` in `block_swap_binding.py`. The lemma isolates exactly the part
the orbit identity proves (conjugation), so the gap to the symmetrizer is explicit. -/

/-- **Relabeling = conjugation is trace-invariant (the orbit identity).** For any
cyclic trace `τ` (`τ(xy)=τ(yx)`) on a group, conjugation by `g` preserves it:
`τ(g a g⁻¹) = τ a`. This is `atom_orbit_reduction`'s `tr_M(β_σ W β_σ⁻¹)=tr_M(W)`.
It does **not** give `τ(a g) = τ(a)` — the Young symmetrizer composes `β_σ` rather
than conjugating, so that (generally false) equality is exactly the binding signal
`log(S_free/S_atom)`. -/
theorem orbit_relabel_invariant {G : Type*} [Group G] (τ : G → R)
    (hcyc : ∀ x y : G, τ (x * y) = τ (y * x)) (g a : G) :
    τ (g * a * g⁻¹) = τ a := by
  rw [hcyc (g * a) g⁻¹, inv_mul_cancel_left]

end QOU.Hecke.IdenticalParticle
