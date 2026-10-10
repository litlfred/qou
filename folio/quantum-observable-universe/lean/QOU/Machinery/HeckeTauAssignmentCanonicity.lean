/-
# Pair-canonicity of the τ-assignment — strict independence FAILS (proved)

The general-rank τ-assignment (`tauAssignmentAtRank`) is constructed
from a marked generator pair `(i, j)` with `M i j = 3`: the state is
restricted to the six-element cell of the `{i, j}` parabolic and pushed
through the base-rung `H₃` assignment. The open question left by the
tower work was **canonicity**: does the assignment depend on the marked
pair, or is there a pair-independent functor?

This file settles the *strict* half of that question, negatively and
by proof: at the A₃ rung the assignments for the two braid pairs
`(0,1)` and `(1,2)` are **different functions**. The witness is the
indicator state of the longest `(0,1)`-cell element `σ₀σ₁σ₀`: it lies
in the `(0,1)` cell (so the `(0,1)`-assignment reads it into the
isotypic slot with coefficient `I ≠ 0`) but outside the `⟨σ₁, σ₂⟩`
parabolic (so the `(1,2)`-assignment kills it). Distinctness of the
group elements involved is refuted through the permutation
representation `φA3`, exactly as in the A₃ residue proofs.

Scope discipline (per the repo's refutation calibration): this is a
**scope-limited negative** — *this construction, as marked, is
pair-dependent*. It does NOT exclude:

* a pair-independent assignment obtained by a different construction
  (e.g. summing/averaging over pairs, or a colimit over the Coxeter
  diagram's edges); or
* **coherent** canonicity — transition isomorphisms intertwining the
  `(i,j)`- and `(i',j')`-assignments along diagram automorphisms or
  W-conjugation, making the family a functor on a marked-pair
  groupoid rather than a single map.

Both remain open; the second is the mathematically natural formulation
and is what "canonicity" should mean going forward.

Results:

* **`simple_ne_A3_01` / `simple_ne_A3_12`** — simple-distinctness at
  the two braid pairs, obtained from the FULL geometric representation
  (`simple_ne_full`) — the first consumer of the Chebyshev leg.
* **`tauAssignment_pair_dependent`** — the two A₃ assignments differ
  on an explicit state: strict pair-independence is FALSE.

HONESTY (STRICT): sorry-free, no axioms; `decide` only on finite
`Perm (Fin 4)` / matrix-entry facts. The negative is scope-limited as
documented above; coherent canonicity is NOT settled in either
direction. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterA3Instantiation
import QOU.Machinery.HeckeTauAssignmentGeneralRank
import QOU.Machinery.CoxeterGeometricRepresentationFull

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List CoxeterMatrix Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

local prefix:100 "π" => csA3.wordProd
local prefix:100 "σ" => csA3.simple

/-! ## Simple-distinctness from the full geometric representation -/

/-- `σ₀ ≠ σ₁` in the A₃ group — via the Chebyshev-leg `simple_ne_full`,
no permutation computation needed. -/
theorem simple_ne_A3_01 : σ (0 : Fin 3) ≠ σ 1 :=
  simple_ne_full csA3 (by decide)

/-- `σ₁ ≠ σ₂` in the A₃ group. -/
theorem simple_ne_A3_12 : σ (1 : Fin 3) ≠ σ 2 :=
  simple_ne_full csA3 (by decide)

/-! ## The witness state and the four evaluations -/

/-- The indicator of the longest `(0,1)`-cell element `σ₀σ₁σ₀`. -/
noncomputable def vPairWitness : (Aₙ 3).Group → ℂ :=
  fun w => if w = π [(0 : Fin 3), 1, 0] then 1 else 0

private lemma vPairWitness_self : vPairWitness (π [(0 : Fin 3), 1, 0]) = 1 := by
  unfold vPairWitness
  rw [if_pos rfl]

private lemma vPairWitness_01 : vPairWitness (π [(0 : Fin 3), 1]) = 0 := by
  unfold vPairWitness
  rw [if_neg]
  intro hcontra
  have happ := congrArg φA3 hcontra
  rw [wordProd_ij csA3 0 1, wordProd_iji csA3 0 1] at happ
  simp only [map_mul, φA3_simple] at happ
  exact absurd happ (by decide)

private lemma vPairWitness_12 : vPairWitness (π [(1 : Fin 3), 2]) = 0 := by
  unfold vPairWitness
  rw [if_neg]
  intro hcontra
  have happ := congrArg φA3 hcontra
  rw [wordProd_ij csA3 1 2, wordProd_iji csA3 0 1] at happ
  simp only [map_mul, φA3_simple] at happ
  exact absurd happ (by decide)

private lemma vPairWitness_121 : vPairWitness (π [(1 : Fin 3), 2, 1]) = 0 := by
  unfold vPairWitness
  rw [if_neg]
  intro hcontra
  have happ := congrArg φA3 hcontra
  rw [wordProd_iji csA3 1 2, wordProd_iji csA3 0 1] at happ
  simp only [map_mul, φA3_simple] at happ
  exact absurd happ (by decide)

/-! ## Strict pair-independence fails -/

/-- **The τ-assignment depends on the marked pair**: at the A₃ rung the
`(0,1)`- and `(1,2)`-assignments are different functions. The witness
state is read into the isotypic slot by the first (coefficient `I`)
and killed by the second. Scope-limited negative: refutes *strict*
independence of this construction; coherent canonicity along diagram
automorphisms remains open. -/
theorem tauAssignment_pair_dependent :
    (tauAssignmentAtRank csA3 0 1 (by decide) simple_ne_A3_01).toFun
        vPairWitness
      ≠ (tauAssignmentAtRank csA3 1 2 (by decide) simple_ne_A3_12).toFun
        vPairWitness := by
  intro h
  have h2 := congrFun h 2
  have hL : (tauAssignmentAtRank csA3 0 1 (by decide)
        simple_ne_A3_01).toFun vPairWitness 2
      = vPairWitness (π [(0 : Fin 3), 1])
        + I * vPairWitness (π [(0 : Fin 3), 1, 0]) := rfl
  have hR : (tauAssignmentAtRank csA3 1 2 (by decide)
        simple_ne_A3_12).toFun vPairWitness 2
      = vPairWitness (π [(1 : Fin 3), 2])
        + I * vPairWitness (π [(1 : Fin 3), 2, 1]) := rfl
  rw [hL, hR, vPairWitness_01, vPairWitness_self, vPairWitness_12,
    vPairWitness_121] at h2
  have hI : (I : ℂ) = 0 := by linear_combination h2
  exact Complex.I_ne_zero hI

end QOU.Machinery.CoxeterParabolic
