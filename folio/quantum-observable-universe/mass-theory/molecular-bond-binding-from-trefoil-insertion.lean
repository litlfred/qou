import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Molecular bond binding energy from inverse-trefoil insertion

A covalent bond is modelled as an inverse trefoil `T⁻¹` inserted
between two atomic braids. The bond binding energy is the
Wedderburn-channel sum of per-channel volume shifts `ΔΦ_λ` weighted
by the channel weights `W_λ`, times the Hartree scale `E_mol`:

```
E_bond = (W_sym·ΔΦ_sym + W_std·ΔΦ_std + W_alt·ΔΦ_alt) · E_mol.
```

For `n` inserted inverse trefoils (multiple bonds), each per-channel
shift scales linearly, `ΔΦ ∝ n`, so single/double/triple bond
energies scale as `1 : 2 : 3`.

This sibling axiomatises the bond-energy weighted sum and proves the
linear `n`-scaling of the energy in the per-bond shift.

-- Ref: [leitner2026] prop:molecular-bond-binding-from-trefoil-insertion
-- Ref: [adams1985hyperbolic] Adams, "Thrice-punctured spheres in hyperbolic 3-manifolds," Trans. AMS 287 (1985)
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R]

/-- The molecular bond binding energy as the Wedderburn-channel sum
of per-channel volume shifts `ΔΦ` weighted by `W`, times the
Hartree scale `Emol`. -/
def bondEnergy
    (Wsym Wstd Walt ΔΦsym ΔΦstd ΔΦalt Emol : R) : R :=
  (Wsym * ΔΦsym + Wstd * ΔΦstd + Walt * ΔΦalt) * Emol

/-- Multiple-bond `n`-scaling: if every per-channel shift scales by a
common factor `n` (`ΔΦ ↦ n·ΔΦ`), the bond energy scales by `n`. -/
theorem bondEnergy_n_scaling
    (Wsym Wstd Walt ΔΦsym ΔΦstd ΔΦalt Emol n : R) :
    bondEnergy Wsym Wstd Walt (n * ΔΦsym) (n * ΔΦstd) (n * ΔΦalt) Emol
      = n * bondEnergy Wsym Wstd Walt ΔΦsym ΔΦstd ΔΦalt Emol := by
  unfold bondEnergy
  ring

end QOU.BraidKnot
