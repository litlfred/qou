/-
Copyright (c) 2026 litlfred. All rights reserved.

# The archimedean q₀-continuation of the W_λ value map is polynomial evaluation

Companion to [`KeystoneLRModulusFold.lean`](KeystoneLRModulusFold.lean) and
[`KeystoneLRAmplitudeReal.lean`](KeystoneLRAmplitudeReal.lean).  The W_λ keystone's
value map `d_q(λ) = [mark λ]_q` (`KeystoneMcKayValueMap`) is a **global Laurent
polynomial** in `q` — equivalently a polynomial in the fold parameter
`t = q + q⁻¹` via the Chebyshev quantum integer `qi` — so the passage from the
root-of-unity fibre value (`t = φ = 2cos(π/5)`) to the real substrate value
(`t = q₀ + q₀⁻¹ ≈ 2.01090`) is **evaluation of one fixed polynomial at two
points**, not an analytic continuation of transcendental data.

This file makes that precise for the four physical `n = 5` blocks and exhibits the
one structurally interesting feature — the **fold/unfold** of the muon block:

* the block quantum dimensions are the `qi` polynomials
  `d((5)) = [1]`, `d((4,1)) = [4]`, `d((3,2)) = [5]`, `d((3,1,1)) = [5] + 1`
  (the `+1` is the A₅-split signature);
* `muon_folds_at_root` : `d((3,2))(φ) = [5]_φ = 0` — at the root the muon block is
  degenerate (the `D = 2` collapse, #3820);
* `muon_unfolds_generic` : `d((3,2))(t) = t⁴ − 3t² + 1` — the same polynomial is
  non-trivial off the fold, so the archimedean continuation **unfolds** the
  degeneracy into the growing 4-class `(1, [4], [5], [5]+1)` the mass ratios need;
* `wlambda_ratio_is_qi` : every W_λ ratio (where the `D²` normaliser cancels) is a
  ratio of `qi` polynomials, hence continues by evaluation — the honest content of
  "the continuation is not the wall."

The numeric continuation at the substrate `q₀` is recorded in the witness
`computations/probes/wlambda-q0-continuation.witness.json`.

Base ring: generic `{R : Type*} [CommRing R]` — the value map and its continuation
are pre-archimedean algebra (§7c; the real evaluation `t = q₀+q₀⁻¹` is a numerical
instance, not part of the structural statement).  **Honest scope:** this certifies
that the *value-map* continuation is polynomial evaluation; it does **not** derive
`loc_matches` (the gauge = categorical identification) and wires nothing.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneLRModulusFold

namespace QOU.BraidKnot.KeystoneWLambdaContinuation

open QOU.BraidKnot.KeystoneLRModulusFold

variable {R : Type*} [CommRing R]

/-- Quantum dimension of the vacuum block `(5)`: `d = [1] = 1`. -/
def dqVac (t : R) : R := qi t 1

/-- Quantum dimension of the block `(4,1)`: `d = [4]`. -/
def dq41 (t : R) : R := qi t 4

/-- Quantum dimension of the muon block `(3,2)`: `d = [5]`. -/
def dq32 (t : R) : R := qi t 5

/-- Quantum dimension of the electron block `(3,1,1)`: `d = [5] + 1` (the A₅-split
`3 ⊕ 3′` signature; equivalently `[3][4]/[2]`, `KeystoneMcKayValueMap`). -/
def dq311 (t : R) : R := qi t 5 + 1

/-- **The muon block folds to zero at the fibre root** `t = φ` (`φ² = φ + 1`,
`φ = 2cos(π/5)`): `d((3,2))(φ) = [5]_φ = 0`.  This is the `D = 2` degeneracy of the
root-of-unity fibre. -/
theorem muon_folds_at_root {φ : R} (hφ : φ ^ 2 = φ + 1) : dq32 φ = 0 :=
  qi_phi_five hφ

/-- **The muon block unfolds off the fold**: the *same* quantum-dimension is the
polynomial `d((3,2))(t) = t⁴ − 3t² + 1`, non-trivial for generic `t`.  Evaluated at
the substrate `t = q₀ + q₀⁻¹` this is the physical `[5]_{q₀} ≈ 5.22`, not `0` — the
archimedean continuation unfolds the root degeneracy. -/
theorem muon_unfolds_generic (t : R) : dq32 t = t ^ 4 - 3 * t ^ 2 + 1 := by
  show qi t 5 = _; rw [qi_five]; ring

/-- **The electron/muon split**: `d((3,1,1)) = d((3,2)) + 1` — the archimedean
continuation carries the `+1` split signature at every `t`, so the electron block
never coincides with the muon block off the trivial locus. -/
theorem electron_muon_split (t : R) : dq311 t = dq32 t + 1 := rfl

/-- **The continuation is evaluation.** The four block quantum dimensions are fixed
`qi` polynomials in `t`; therefore any W_λ ratio (in which the `D²` normaliser
cancels) is a ratio of `qi` polynomials — the root value and the archimedean `q₀`
value are that one rational function at `t = φ` versus `t = q₀ + q₀⁻¹`.  Stated for
the electron/muon ratio numerator: `d((3,1,1)) − d((3,2)) = 1` for all `t`, an
identity of polynomials, hence continuation-stable. -/
theorem wlambda_ratio_is_qi (t : R) : dq311 t - dq32 t = 1 := by
  rw [electron_muon_split]; ring

/-- The four block dimensions as an explicit Chebyshev tuple in `t` — the
continuation object: evaluate at `t = φ` for the (folded) root data, at
`t = q₀+q₀⁻¹` for the physical q₀ data. -/
theorem block_dims_explicit (t : R) :
    dqVac t = 1 ∧ dq41 t = t ^ 3 - 2 * t ∧ dq32 t = t ^ 4 - 3 * t ^ 2 + 1
      ∧ dq311 t = t ^ 4 - 3 * t ^ 2 + 2 := by
  refine ⟨rfl, ?_, muon_unfolds_generic t, ?_⟩
  · show qi t 4 = _; rw [qi_four]; ring
  · show qi t 5 + 1 = _; rw [qi_five]; ring

end QOU.BraidKnot.KeystoneWLambdaContinuation
