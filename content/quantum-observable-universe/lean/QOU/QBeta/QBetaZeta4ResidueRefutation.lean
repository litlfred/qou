/-
Copyright (c) 2026 litlfred. All rights reserved.

# Q_β odd-channel: ζ₄-residue exclusion + R₁₂ trace-cubic reduction (Lean certificate)

Formalize-first certificate for the **scope-(b) structural exclusion** recorded
in `docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md` (bean `0zr0`),
which closed the ζ₄-**residue** route for the Q_β odd channel at the
fibre-Laurent level. The refuted-declaration discipline (AGENTS.md §"Before
declaring refuted/ruled out") requires a scope-(b) exclusion to **cite/prove
the invariant**; until now that invariant lived only in a sympy witness
(`qbeta-zeta4-fibre-cyclotomic.witness.json`). These lemmas are its exact,
kernel-checked certificate.

The object is the bar-odd part of the net decay-width Laurent polynomial
`Δ_net(q) = Δ(neutron) − Δ(proton)`; its numerator (over `4q⁷`) is

  `num(q) = q¹⁴ − 5q¹² + 10q¹⁰ − 16q⁸ + 16q⁶ − 10q⁴ + 5q² − 1`.

**Results (all exact, division-free over any `CommRing`):**

1. `numOdd_factor` — the **cyclotomic content is exactly `q²−1`**:
   `num = (q²−1)·R₁₂`, with `R₁₂` the palindromic degree-12 cofactor.
2. `numOdd_phi4_quot` / `numOdd_at_phi4_root` — **`Φ₄ = q²+1` does NOT divide
   `num`**: exact division `num + 64 = (q²+1)·Q`, so `num ≡ −64 (mod Φ₄)`; at
   any root of `Φ₄` (e.g. `q = i` over `ℂ`) `num = −64 ≠ 0`. This is the
   scope-(b) invariant: the ζ₄=i **residue** (Φ₄ divisibility) is *absent* —
   the odd carrier is not a root-of-unity object.
3. `R12_eq_trace_cubic_shift` (division-free) / `R12_eq_cubic_trace` (`Field`) —
   what **survives**: `R₁₂ = q⁶·C(q²+q⁻²)` with the irreducible cubic
   `C(y) = y³ − 4y² + 3y − 2` in the **bar-even loop-trace variable**
   `y = q²+q⁻² = 2cosh 2λ` (S₃ Galois, disc `−152`). The surviving odd-channel
   content lives in `ℚ[y]`, degree 3 — NOT in a cyclotomic factor.

Derives **no** `c_k` value, wires **nothing**, changes **no** registry tier
(flip-flop guard, registry §8). It hardens an existing refutation and pins the
one surviving open object (`C(y)`). Generic `CommRing` per AGENTS.md §7c; the
one `Field` lemma is the literal `q⁻²` restatement only.

Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.QBeta.Zeta4Residue

variable {R : Type*} [CommRing R]

/-- Numerator of the bar-odd part of the net decay-width carrier
    `Δ_odd(q) = num(q) / (4q⁷)`. -/
def numOdd (q : R) : R :=
  q ^ 14 - 5 * q ^ 12 + 10 * q ^ 10 - 16 * q ^ 8 + 16 * q ^ 6
    - 10 * q ^ 4 + 5 * q ^ 2 - 1

/-- The palindromic degree-12 cofactor `R₁₂` (the non-cyclotomic substance of
    the odd carrier). -/
def R12 (q : R) : R :=
  q ^ 12 - 4 * q ^ 10 + 6 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1

/-- The surviving cubic in the bar-even trace variable: `C(y) = y³−4y²+3y−2`. -/
def cubicC (y : R) : R := y ^ 3 - 4 * y ^ 2 + 3 * y - 2

/-! ## §1. Cyclotomic content of the odd carrier is exactly `q²−1` -/

/-- **The only cyclotomic content of `num` is the trivial `q²−1`.**
    `num = (q²−1)·R₁₂` — the `Φ₁·Φ₂` factor, with the rest carried by the
    non-cyclotomic palindromic `R₁₂`. -/
theorem numOdd_factor (q : R) : numOdd q = (q ^ 2 - 1) * R12 q := by
  unfold numOdd R12; ring

/-! ## §2. `Φ₄ = q²+1` does NOT divide `num` (the ζ₄-residue exclusion) -/

/-- **Exact division of `num` by `Φ₄ = q²+1` leaves the nonzero constant
    remainder `−64`.** `num + 64 = (q²+1)·Q` with `Q` the explicit degree-12
    quotient. Since the remainder is a nonzero constant, `Φ₄ ∤ num`: the
    ζ₄ = i **residue** is absent from the odd carrier. -/
theorem numOdd_phi4_quot (q : R) :
    numOdd q + 64 =
      (q ^ 2 + 1) *
        (q ^ 12 - 6 * q ^ 10 + 16 * q ^ 8 - 32 * q ^ 6 + 48 * q ^ 4
          - 58 * q ^ 2 + 63) := by
  unfold numOdd; ring

/-- **`num` evaluates to the constant `−64` at every root of `Φ₄`** (e.g.
    `q = i` over `ℂ`, where `q²+1 = 0`). Hence `num` has no `Φ₄` factor: the
    scope-(b) exclusion of the ζ₄-residue route, cited invariant. (Over a ring
    where `(64 : R) ≠ 0` — e.g. `ℤ, ℚ, ℝ, ℂ` — this is a genuine non-vanishing;
    the value `−64` itself holds over any `CommRing`.) -/
theorem numOdd_at_phi4_root (q : R) (hq : q ^ 2 + 1 = 0) : numOdd q = -64 := by
  have h := numOdd_phi4_quot q
  rw [hq, zero_mul] at h
  linear_combination h

/-! ## §3. What survives: `R₁₂ = q⁶·C(q²+q⁻²)`, a cubic in the trace variable -/

/-- **Division-free trace-cubic form of `R₁₂`.** `R₁₂ = q⁶·C(q²+q⁻²)` with
    `C(y) = y³−4y²+3y−2`, written without inverses by clearing `q⁶`:
    `R₁₂ = (q⁴+1)³ − 4q²(q⁴+1)² + 3q⁴(q⁴+1) − 2q⁶` (each `q⁶·yᵏ` becomes a
    genuine polynomial via `q²·(q²+q⁻²) = q⁴+1`). The odd carrier's surviving
    content is a **degree-3 object in the bar-even trace variable**, not a
    cyclotomic factor. -/
theorem R12_eq_trace_cubic_shift (q : R) :
    R12 q =
      (q ^ 4 + 1) ^ 3 - 4 * q ^ 2 * (q ^ 4 + 1) ^ 2
        + 3 * q ^ 4 * (q ^ 4 + 1) - 2 * q ^ 6 := by
  unfold R12; ring

/-- **Literal trace-cubic form (`Field`, `q ≠ 0`):** `R₁₂ = q⁶·C(q²+q⁻²)` with
    the trace variable `y = q²+q⁻²` written explicitly. The `Field`/`q ≠ 0`
    hypothesis is only to admit `q⁻²`; the content is the division-free
    `R12_eq_trace_cubic_shift`. -/
theorem R12_eq_cubic_trace {F : Type*} [Field F] (q : F) (hq : q ≠ 0) :
    R12 q = q ^ 6 * cubicC (q ^ 2 + q⁻¹ ^ 2) := by
  unfold R12 cubicC
  field_simp
  ring

end QOU.QBeta.Zeta4Residue
