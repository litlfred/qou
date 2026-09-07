import Mathlib.Tactic
import Mathlib.Algebra.Algebra.Defs

/-!
# The infinitesimal braid relations are homogeneous — KZ flatness is level-independent

Bean `qou-d0qq`, prune P3 of
`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §B.

Kohno's theorem: the Knizhnik–Zamolodchikov connection `∇ = d − ħ Σ_{i<j} t_ij d log(z_i − z_j)`
on the configuration space `Conf_n(ℂ)` is flat **iff** the coefficients `t_ij` satisfy the
infinitesimal braid relations — symmetry `t_ij = t_ji`, the commutator relation
`[t_ij, t_ik + t_jk] = 0` for distinct `i, j, k`, and `[t_ij, t_kl] = 0` for disjoint pairs.
Those relations are *homogeneous* in `t`: if `t` satisfies them, so does `c • t` for every
scalar `c`. Since the level enters the connection only through the overall scalar `ħ`
(`ħ = 1/(k+2)` up to normalisation), **flatness cannot depend on the level** — real,
imaginary, or otherwise. What *does* depend on the level is the monodromy's target: the
Hecke algebra `H_n(q)` with `q = e^{iπħ}` is semisimple iff `q` is not a root of unity.

This file proves the homogeneity (the only step with content); the equivalence
"flat ⟺ infinitesimal braid relations" is Kohno's theorem and is cited, not formalised.
Consequence for the corpus: two content blocks (`mass-theory/lifted-crossing-locality`,
`nuclear-interactions/q-holonomy-locality-derivation`) said the KZ connection is "flat at
`q₀`" as though flatness singled out `q₀`; it does not. What singles out `q₀` there is
semisimplicity, and the blocks are reworded to say so.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — flatness ⟺ infinitesimal braid relations.

Base ring: `A` any (non-commutative) `R`-algebra over a commutative ring `R`; no `ℝ`.
-/

namespace QOU.Mass.KZFlatnessLevelIndependent

open scoped BigOperators

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A] {n : ℕ}

/-- The infinitesimal braid (Kohno–Drinfeld) relations on a family `t : Fin n → Fin n → A`. -/
structure InfinitesimalBraidRelations (t : Fin n → Fin n → A) : Prop where
  symm : ∀ i j, t i j = t j i
  /-- `[t_ij, t_ik + t_jk] = 0` for pairwise distinct `i, j, k`. -/
  comm_three : ∀ i j k, i ≠ j → i ≠ k → j ≠ k → Commute (t i j) (t i k + t j k)
  /-- `[t_ij, t_kl] = 0` for disjoint pairs. -/
  comm_disjoint : ∀ i j k l, i ≠ k → i ≠ l → j ≠ k → j ≠ l → Commute (t i j) (t k l)

/-- Homogeneity: the relations survive scaling by any scalar `c` — the level. -/
theorem InfinitesimalBraidRelations.smul {t : Fin n → Fin n → A}
    (ht : InfinitesimalBraidRelations t) (c : R) :
    InfinitesimalBraidRelations (fun i j => c • t i j) where
  symm := fun i j => by simp [ht.symm i j]
  comm_three := fun i j k hij hik hjk => by
    have h := ht.comm_three i j k hij hik hjk
    show Commute (c • t i j) (c • t i k + c • t j k)
    rw [← smul_add]
    unfold Commute SemiconjBy at h ⊢
    rw [smul_mul_assoc, mul_smul_comm, smul_mul_assoc, mul_smul_comm, h]
  comm_disjoint := fun i j k l hik hil hjk hjl => by
    have h := ht.comm_disjoint i j k l hik hil hjk hjl
    show Commute (c • t i j) (c • t k l)
    unfold Commute SemiconjBy at h ⊢
    rw [smul_mul_assoc, mul_smul_comm, smul_mul_assoc, mul_smul_comm, h]

/-- The zero family satisfies the relations — so the relations alone say nothing about
which `c` is "the" level; that is the point. -/
theorem InfinitesimalBraidRelations.zero :
    InfinitesimalBraidRelations (fun _ _ : Fin n => (0 : A)) where
  symm := fun _ _ => rfl
  comm_three := fun _ _ _ _ _ _ => by simp
  comm_disjoint := fun _ _ _ _ _ _ _ _ => by simp

end QOU.Mass.KZFlatnessLevelIndependent
