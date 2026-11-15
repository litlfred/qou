import QOU.MassTheory.UrsellPartitionFunctionB3
import Mathlib.Tactic

/-!
# The body-number expansion has a classical floor: no power counting in `ε = q − 1`

Bean `qou-olxi`, attack option 1 (owner: "do as suggested", 2026-09-15). The
question was whether the many-body (body-number) expansion of the binding is
*ordered* in the deformation parameter `ε = q − 1` — the ingredient a Weinberg-style
power counting over body number would need. The answer is no, and the reason is an
identity rather than a measurement.

The interface (bond) factors of the multiplicative assembly are `z + d_kind`
(`bond_factors_are_z_plus_d_probe`), with `z = z_D = q³/(q² + 1)` the convention-D
Markov parameter and `d_kind` the kind-dependent correction, which is `O(ε)` for all
three interface kinds:

    kind                z + d at q = 1 + ε          d
    pp   (σ)            1/2 +  ε   + ε²/4           0
    pn   (averaged)     1/2 +  0   + 3ε²/4         −ε   + ε²/2
    nn   (σ⁻¹)          1/2 −  ε   + 5ε²/4         −2ε  + ε²

So at the classical point every bond factor is `z_D(1) = 1/2` (`zD_one`,
`bondFactor_classical`), its Mayer variable is `−1/2`, and the connected three-body
cumulant of the assembly — `b₃ = −φᵀ₃` by `b3corpus_eq_neg_phi3` — is

    b₃(1/2, 1/2, 1/2) = −(1 − 1/2)²·(1/2 + 2) = −5/8 ≠ 0     (`b3corpus_classical`).

Its `ε`-valuation is therefore `0`: the three-body term is not suppressed relative
to the two-body term by any power of `ε`, and the same holds for `b₄`. **What is
ordered in the corpus is the jet tower**, `T(ρ) = Σ_{n ≥ 1} ℏ_q^{2n} Δ^{(n)}(ρ)` with
remainder ratio `q⁻²` (`rem:brane-tower-q-laplacian-decay-interpretation`): the
expansion parameter of the framework counts *jet level*, not body number. The
body-number expansion at fixed `q` is a lattice-gas cluster expansion with `O(1)`
weights, and its convergence is a Mayer–Ursell question, not a power-counting one.

Scope: this is a scope-(b) exclusion — the invariant is the identity
`z_D(1) = 1/2` — of the *ordering in ε*; it says nothing against orderings in
another parameter. The `d_kind` series are the probe's measured coefficients, carried
here as truncations at second order and used only through their vanishing at
`ε = 0`. Generic field of characteristic zero (§7c); no numerics; no `sorry`.

-- Ref: [leitner2026] bean qou-olxi; computations/probes/bond_factors_are_z_plus_d_probe.py
-/

namespace QOU.MassTheory

open QOU.MassTheory.UrsellPartitionFunctionB3

variable {K : Type*} [Field K]

/-- The convention-D Markov parameter `z_D = q³/(q² + 1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- **At the classical point the Markov parameter is `1/2`.** -/
theorem zD_one : zD (1 : K) = 1 / 2 := by
  norm_num [zD]

/-- The three interface kinds of the canonical atom word. -/
inductive InterfaceKind
  | pp
  | pn
  | nn

/-- The kind-dependent correction `d_kind(ε)`, the probe's measured series truncated
at second order: `0`, `−ε + ε²/2`, `−2ε + ε²`. -/
def dKind : InterfaceKind → K → K
  | .pp, _ => 0
  | .pn, ε => -ε + ε ^ 2 / 2
  | .nn, ε => -2 * ε + ε ^ 2

/-- The bond factor `z_D(1 + ε) + d_kind(ε)`. -/
def bondFactor (k : InterfaceKind) (ε : K) : K := zD (1 + ε) + dKind k ε

/-- **Every bond factor is `1/2` at the classical point**, whatever its kind. -/
theorem bondFactor_classical (k : InterfaceKind) : bondFactor k (0 : K) = 1 / 2 := by
  cases k <;> simp [bondFactor, dKind, zD] <;> norm_num

/-- The Mayer variable of a classical bond is `−1/2`. -/
theorem mayer_classical [CharZero K] : mayer (1 / 2 : K) = -(1 / 2) := by
  norm_num [mayer]

/-- **The connected three-body cumulant does not vanish at `q = 1`:** `b₃ = −5/8`.
Hence its `ε`-valuation is `0`, and the body-number expansion carries no power
counting in `ε`. -/
theorem b3corpus_classical [CharZero K] : b3corpus (1 / 2 : K) (1 / 2) (1 / 2) = -(5 / 8) := by
  rw [b3corpus_uniform_closed_form]
  norm_num

/-- The same statement through the Ursell function: `φᵀ₃(−1/2, −1/2, −1/2) = 5/8`. -/
theorem phi3_classical [CharZero K] : phi3 (-(1 / 2) : K) (-(1 / 2)) (-(1 / 2)) = 5 / 8 := by
  norm_num [phi3]

/-- Assembled: the classical three-body cumulant of the bond model, with every
bond factor evaluated at the classical point. -/
theorem b3_bondModel_classical [CharZero K] (k₁ k₂ k₃ : InterfaceKind) :
    b3corpus (bondFactor k₁ (0 : K)) (bondFactor k₂ 0) (bondFactor k₃ 0) = -(5 / 8) := by
  rw [bondFactor_classical, bondFactor_classical, bondFactor_classical]
  exact b3corpus_classical

end QOU.MassTheory
