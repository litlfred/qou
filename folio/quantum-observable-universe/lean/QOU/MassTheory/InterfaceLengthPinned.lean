/-
InterfaceLengthPinned.lean — why the normal-form machinery pins the
interface word, and what that pinning actually rests on.

CONTEXT.  `conj:confinement-nf-structure-forcing` decomposes the normal-form
shift of a compound braid `β = β₁ ⋆ I ⋆ β₂` as

    shift_NF(β) = α_shift(I) + Δ(β₁, β₂; A),

where `α_shift(K) := max_{λ ⊢ p} ord_{q=0}^{(−)} χ_λ(β_K)` is a POLE ORDER —
a Laurent valuation, not a magnitude (`prop:alpha-shift-torus-knot`).

THE MECHANISM.  On the all-anti-symmetric channel `V_{(1^p)}` every standard
Young tableau of a single column is unique, so the channel is 1-dimensional
and each Hecke generator acts by a scalar.  For a column the content
difference across adjacent cells is `ρ = −1`, so that scalar is

    a = h / (1 − q^{−2ρ}) = (q − q⁻¹)/(1 − q²) = −q⁻¹,

of q-valuation exactly −1.  A POSITIVE braid word of length `L` therefore has
column character `(−q⁻¹)^L`, of valuation `−L`: each letter contributes
exactly one to the pole order.  Since the column channel is also the observed
maximizer, `α_shift` of a positive word is its LENGTH.

WHAT IS PROVED HERE.  The valuation bookkeeping, and — the point — that a
unit step per letter is exactly what makes the pole order a FAITHFUL reader
of word length.  `colPole_faithful` is the pinning: two interface words of
different lengths cannot share an α_shift, so the interface slot in the shift
decomposition is not free.  `colPole_not_faithful_of_zero_step` shows the
hypothesis is load-bearing: at step 0 every length collapses to the same pole
order and nothing is pinned.

This is deliberately generic Nat arithmetic (AGENTS.md §7c): no ordering on
`q`, no `Real`, nothing archimedean.  The archimedean input — that the scalar
is `−q⁻¹` and not something else — is measured in
`computations/meson/interface_alpha_shift_is_pinned_probe.py`, whose controls
reproduce the committed `alpha-shift-torus.witness.json` values.

@module QOU.MassTheory.InterfaceLengthPinned
-/

set_option autoImplicit false

namespace QOU.MassTheory

/-- Pole order at `q = 0` of the all-column character of a positive braid
word, accumulated one letter at a time.  `step` is the pole order contributed
by a single generator; the column channel has `step = 1`. -/
def colPole (step : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => step + colPole step n

/-- The pole order is linear in the word length. -/
theorem colPole_eq_mul (step n : Nat) : colPole step n = step * n := by
  induction n with
  | zero => rfl
  | succ k ih =>
      show step + colPole step k = step * (k + 1)
      rw [ih, Nat.mul_succ]
      exact Nat.add_comm step (step * k)

/-- On the all-column channel each generator has valuation `−1`, i.e.
contributes one to the pole order, so `α_shift` of a positive word IS its
length. -/
theorem colPole_one (n : Nat) : colPole 1 n = n := by
  rw [colPole_eq_mul, Nat.one_mul]

/-- **The pinning.**  Pole order recovers word length exactly, so two
interface words of different lengths carry different `α_shift`.  The
interface slot in the shift decomposition is therefore not free: a substitute
word is admissible only if it has the same length as the one it replaces. -/
theorem colPole_faithful {m n : Nat} (h : colPole 1 m = colPole 1 n) : m = n := by
  rw [colPole_one, colPole_one] at h; exact h

/-- The unit step is load-bearing.  If a generator contributed nothing to the
pole order, every word length would collapse to the same `α_shift` and the
interface would be entirely unconstrained. -/
theorem colPole_not_faithful_of_zero_step :
    ∃ m n : Nat, m ≠ n ∧ colPole 0 m = colPole 0 n := by
  refine ⟨0, 1, by decide, ?_⟩
  rw [colPole_eq_mul, colPole_eq_mul]

/-- Substituting a longer interface strictly raises the normal-form shift,
where `base` is the `Δ(β₁, β₂; A)` contribution of the two components.  This
is what moves the `D(u)` exponent off its verified value. -/
theorem shift_strict_mono (base : Nat) {m n : Nat} (h : m < n) :
    base + colPole 1 m < base + colPole 1 n := by
  rw [colPole_one, colPole_one]; omega

/-- Contrapositive, in the form the `D(u)` check uses: if the compound shift
matches the recorded exponent for two interfaces, those interfaces have equal
length. -/
theorem interface_length_of_shift_eq (base : Nat) {m n : Nat}
    (h : base + colPole 1 m = base + colPole 1 n) : m = n := by
  rw [colPole_one, colPole_one] at h; omega

end QOU.MassTheory
