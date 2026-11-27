import Mathlib.Tactic
import Mathlib.Data.Matrix.Basic

/-!
# QOU.Information.AntisymmetricInvolutionForcesZero — a unitary involution has no antisymmetric entry

Bean `qou-54tg`. `q-game-of-life.lean`'s `qGameOfLife_reversible` takes
`hT : Function.Involutive T`, justified in its docstring as *"Each q-Toffoli gate
is its own inverse (an involution in `H₃(q)`)"*, while the same content object's
proof states the opposite — *"The generators are **not** involutions at generic
`q`: `σᵢ⁻¹ = σᵢ` holds precisely when `q = q⁻¹`, i.e. in the classical limit
`q → 1`"*. This file settles which is right **at the gate**, not merely at the
generator, and the answer agrees with the proof.

## The argument, and why it needs nothing about the gate's word

`prop:toffoli-transfer-matrix` supplies two facts about the q-Toffoli, both
stated in the block:

* **Unitarity** — `Toff_q† Toff_q = I` (`q-game-of-life.md`, property 4). The
  entries are real functions of `q` for `q > 0`, so this is orthogonality.
* **Antisymmetry** — `P₆₇(q) = −P₇₆(q)` (`prop:toffoli-transfer-matrix`, item 4).

`involutive_orthogonal_transpose_eq` below: an orthogonal involution equals its
own transpose. A symmetric matrix has `M i j = M j i`; an antisymmetric entry has
`M i j = −M j i`. Both at once force `M i j = 0`.

So **`Toff_q² = id` requires `P₇₆(q) = 0`**, i.e. `Φ(q) = 0`.

`Φ` carries the factor `(q − 1)` (`prop:toffoli-transfer-matrix`, items 1 and 5
— *"all target-flip amplitudes vanish as `q → 1`"*), which gives the classical
limit. **It is not the only zero, and saying otherwise would be an over-claim**:
`Φ` also vanishes at `q = u² ≈ 0.4655`, `u` the real root of `u³ + u − 1`, from
its second factor. Both zeros lie **at or below `q = 1`**, and the block's own
stability condition is `q > 1` (*"the physical regime"*, `q-game-of-life.md`).

**So on the regime the block itself declares, `Φ ≠ 0` and the gate is never an
involution** — which is what its proof says about the generators, now
established for the gate. The substrate `q₀ ≈ 1.110` sits there.

This needs no knowledge of which three-crossing word `Toff_q` is, and no
assumption about which entries of its row are supported — the two cited
properties suffice.

## Corroboration, by the route that does need a support assumption

Assuming row 7 is supported on `{6, 7}` (as the classical Toffoli's is, swapping
`|110⟩` and `|111⟩`), `M² = I` forces `P₇₇² − Φ² = 1`. Substituting
`q = u²` and clearing denominators, that is

  `u¹⁶ + 2u¹⁵ + u¹⁴ − 4u¹² − 4u¹¹ − 2u⁹ + 4u⁸ − 6u⁷ + 12u⁶ − 4u⁵ + 20u⁴
     + 8u³ + 13u² + 6u + 1 = 0`,

a polynomial with **zero real roots** — exact Sturm count, not a numeric scan.
At the substrate `P₇₇² − Φ² = 0.3016`, a shortfall of `0.698` from the required
`1`, so the failure is not marginal. Recorded because it is an independent check
that lands in the same place; the theorem below is the one that does not need the
support assumption.

## Consequence for `qGameOfLife_reversible`

Its hypothesis is unsatisfiable by the gate it names, at every `q ≠ 1` and so at
the substrate `q₀ ≈ 1.110`. Per AGENTS.md §"Conditional-proved ≠
premise-established", the theorem is a true implication and must **not** be read
as establishing that the q-GoL tick is reversible. Its sibling
`qGameOfLife_unitary`, keyed on `Function.Bijective`, is the sound one: the
block's proof establishes unitarity and invertibility throughout, never
`T² = id`.

**Scope.** This says the q-Toffoli is not an *involution*. It emphatically does
**not** say the q-GoL tick is irreversible — a unitary gate is invertible, which
is the property the automaton actually needs. The defect is that `_reversible`
asks for the wrong one.
-/

namespace QOU.Information.AntisymmetricInvolutionForcesZero

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]
variable {R : Type*} [CommRing R]

/-- **An orthogonal involution is symmetric.** Both `Mᵀ` and `M` are inverses of
`M`, so they agree. -/
theorem involutive_orthogonal_transpose_eq (M : Matrix n n R)
    (hinv : M * M = 1) (horth : Mᵀ * M = 1) : Mᵀ = M := by
  calc Mᵀ = Mᵀ * 1 := (mul_one _).symm
    _ = Mᵀ * (M * M) := by rw [hinv]
    _ = (Mᵀ * M) * M := (Matrix.mul_assoc _ _ _).symm
    _ = 1 * M := by rw [horth]
    _ = M := one_mul _

/-- **A unitary involution has no antisymmetric entry.** If `M` is an orthogonal
involution and `M i j = −(M j i)`, then `M i j = 0`.

This is the q-Toffoli statement: the gate is unitary and its `(6,7)` entry is
minus its `(7,6)` entry, so if it were also an involution that entry would
vanish — i.e. `Φ(q) = 0`, which happens only in the classical limit `q = 1`. -/
theorem entry_eq_zero_of_antisymm_of_involutive_orthogonal
    [NoZeroDivisors R] (h2 : (2 : R) ≠ 0) (M : Matrix n n R)
    (hinv : M * M = 1) (horth : Mᵀ * M = 1)
    {i j : n} (hanti : M i j = -(M j i)) : M i j = 0 := by
  have hsymm : M j i = M i j := by
    have := involutive_orthogonal_transpose_eq M hinv horth
    calc M j i = Mᵀ i j := rfl
      _ = M i j := by rw [this]
  rw [hsymm] at hanti          -- hanti : M i j = -(M i j)
  have h2m : (2 : R) * M i j = 0 := by linear_combination hanti
  exact (mul_eq_zero.mp h2m).resolve_left h2

/-- **Contrapositive, the form the q-GoL claim needs.** A unitary matrix with a
*nonzero* antisymmetric entry is not an involution. At the substrate
`Φ(q₀) ≠ 0`, so the q-Toffoli is not one. -/
theorem not_involutive_of_antisymm_entry_ne_zero
    [NoZeroDivisors R] (h2 : (2 : R) ≠ 0) (M : Matrix n n R)
    (horth : Mᵀ * M = 1) {i j : n}
    (hanti : M i j = -(M j i)) (hne : M i j ≠ 0) : M * M ≠ 1 := fun hinv =>
  hne (entry_eq_zero_of_antisymm_of_involutive_orthogonal h2 M hinv horth hanti)

end QOU.Information.AntisymmetricInvolutionForcesZero
