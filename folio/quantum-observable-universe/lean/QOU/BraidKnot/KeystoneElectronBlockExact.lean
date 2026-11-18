import QOU.BraidKnot.BWVacuumRowConcrete

/-!
# Keystone gate is EXACT on the self-conjugate sector — no archimedean continuation

`BWVacuumRowConcrete.lean` de-opaques the keystone gate `bwS0_eq_hecke` into the concrete RT/Seifert
vacuum row `bwS0Concrete = S₀·θ^f` and shows (`bwS0Concrete_eq_S0_forces_trivial_twist`) that the
gate `bwS0Concrete = S₀` holds **iff** the framing twist is trivial, `θ_λ^f = 1`.  At real `q₀ > 1`
that is **false** off the self-conjugate blocks (`θ_λ = q₀^{c(λ)}` is not a root of unity for
`c(λ) ≠ 0`), leaving the residue as a fibre root-of-unity continuation problem — the standing open
piece of `bwS0_eq_hecke` (ledger `docs/coordination/s5-so3-keystone.md`; the 2026-07-11 general
Subgoal-2 reversal makes it open-for-all, no owner gate).

This file closes that residue **on the self-conjugate sector**, exactly and without any continuation.

## The observation

`KeystoneModularTwist.contentSum_conjugate` proves the content sum is transpose-**antisymmetric**,
`c(λ′) = − c(λ)`.  On a **self-conjugate** block (`λ′ = λ`) this forces `c(λ) = − c(λ)`, i.e.
`c(λ) = 0` over `ℤ`.  Hence the twist `θ_λ = q^{c(λ)} = q^0 = 1` for **every** `q` (no `q₀ > 1`,
no root-of-unity fibre needed), so `θ_λ^f = 1` for **every** framing `f`, and
`bwS0Concrete_of_twist_pow_one` gives the gate **exactly**:

  `bwS0Concrete (heckeVerlindeData …) (theta q) f λ = S₀_λ`   for all `f`, all `q`, self-conjugate `λ`.

The framing obstruction that refutes the gate off-diagonal is **structurally absent** on the
self-conjugate sector — there is nothing to continue.  The physical **electron block** `λ = [3,1,1]`
(`c = 0+1+2−1−2 = 0`, self-conjugate) is the flagship instance: its keystone value `bwS0 = S₀ = d_q/D`
is exact at real `q₀` with no archimedean continuation, `d_q([3,1,1]) = [3]_q[4]_q/[2]_q`
(`KeystoneMcKayValueMap.qFactorial_shape_311`).

**Scope.** This is a genuine, no-fit advance on the *remaining open* archimedean piece of
`bwS0_eq_hecke` — it Lean-izes the "self-conjugate continuation is exact" ledger observation (#3701,
previously only a Python probe).  It does **not** close the gate on the **non**-self-conjugate blocks
(where `c(λ) ≠ 0`, `θ^f ≠ 1` at `q₀ > 1`): that fibre root-of-unity continuation stays open.

Base ring `ℝ` (§7c): `bwS0Concrete`/`S₀` live over `ℝ` (`D = √(Σ d_q²)`); the content-sum algebra is
over `ℤ` exponents.

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (content, conjugate).
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators
open QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-- **Self-conjugate ⇒ zero content sum.**  The content sum is transpose-antisymmetric
(`contentSum_conjugate`, `c(λ′) = − c(λ)`); on a self-conjugate block `λ′ = λ` this gives
`c(λ) = − c(λ)`, so `c(λ) = 0`. -/
theorem selfConj_contentSum_zero (l : List ℕ) (hl : l.Sorted (· ≥ ·))
    (hself : Partition.conjugate l = l) : contentSum l = 0 := by
  have h := contentSum_conjugate l hl
  rw [hself] at h
  omega

/-- **The twist is trivial on a self-conjugate block: `θ_λ = 1` for every `q`.**  Immediate from
`c(λ) = 0` (`selfConj_contentSum_zero`) and `q^0 = 1` — no `q₀ > 1`, no root-of-unity fibre. -/
theorem theta_selfConj_eq_one {R : Type*} [GroupWithZero R] (q : R) (l : List ℕ)
    (hl : l.Sorted (· ≥ ·)) (hself : Partition.conjugate l = l) : theta q l = 1 := by
  unfold theta
  rw [selfConj_contentSum_zero l hl hself]
  exact zpow_zero q

/-- **The de-opaqued keystone gate is EXACT on the self-conjugate sector, for every framing.**
On a self-conjugate block the twist is trivial (`theta_selfConj_eq_one`), so `θ_λ^f = 1^f = 1` for
all `f`, and `bwS0Concrete_of_twist_pow_one` gives `bwS0Concrete = S₀` with **no archimedean
continuation** — the framing obstruction that refutes the gate off-diagonal is absent here. -/
theorem bwS0Concrete_selfConj_exact
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) (l : List ℕ) (hl : l ∈ P)
    (hself : Partition.conjugate l = l) (f : ℤ) :
    bwS0Concrete (heckeVerlindeData q hq P hsorted hconj hP) (theta q) f l
      = (heckeVerlindeData q hq P hsorted hconj hP).S0 l := by
  apply bwS0Concrete_of_twist_pow_one
  rw [theta_selfConj_eq_one q l (hsorted l hl) hself, one_zpow]

/-- **The electron block `[3,1,1]` — keystone gate exact at real `q₀`, framing-free.**
`[3,1,1]` is self-conjugate (`c = 0+1+2−1−2 = 0`), so its keystone vacuum-row value equals the Hecke
modular datum `S₀ = d_q/D` **exactly** — no continuation from the root-of-unity fibre.  (Its closed
value is `d_q([3,1,1]) = [3]_q[4]_q/[2]_q`, `KeystoneMcKayValueMap.qFactorial_shape_311`.) -/
theorem bwS0Concrete_electron_block_exact
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) (hmem : [3, 1, 1] ∈ P) (f : ℤ) :
    bwS0Concrete (heckeVerlindeData q hq P hsorted hconj hP) (theta q) f [3, 1, 1]
      = (heckeVerlindeData q hq P hsorted hconj hP).S0 [3, 1, 1] :=
  bwS0Concrete_selfConj_exact q hq P hsorted hconj hP [3, 1, 1] hmem (by decide) f

/-- Subtracting one from the twist value on a self-conjugate partition yields zero. -/
theorem theta_selfConj_sub_one_eq_zero {R : Type*} [CommRing R] [Nontrivial R] [NoZeroDivisors R]
    [GroupWithZero R] (q : R) (l : List ℕ)
    (hl : l.Sorted (· ≥ ·)) (hself : Partition.conjugate l = l) :
    theta q l - 1 = 0 := by
  rw [theta_selfConj_eq_one q l hl hself, sub_self]

end QOU.BraidKnot.Keystone
