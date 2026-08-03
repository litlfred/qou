import Mathlib.Algebra.GeomSum
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.QIntegerAlexanderTorus — q-integer differences are torus-knot Alexander polynomials

Bean `qou-rftd` (T8), epic `qou-8lxd`.

The **symmetric** quantum integer difference `[n]_q − [n−1]_q` equals the
Alexander polynomial of the `(2, 2n−1)` torus knot. This is the cheapest
genuine bridge between the framework's `q`-side (quantum integers, which
appear throughout the Hecke machinery — quantum dimensions, `[3]_q!` in the
Borromean factor, Wenzl genericity) and its **knot** side.

Observed phenomenologically by Gavrilik in the `U_q(su_n)` hadron
mass-sum-rule programme, where it is used to *label hadron flavours by knot
invariants*
-- Ref: [gavrilik2001] https://arxiv.org/abs/hep-ph/0103325

The identity itself is pure algebra over `ℤ[q^{±1}]` and is proved here
**sorry-free and unconditionally**, independent of any phenomenological use.
Nothing about hadron masses, flavour labelling, or the Cabibbo angle is
asserted or assumed; those claims carry their own (separately assessed)
epistemic status and are *not* imported by this file.

## Statement

Write everything in **framed** (Laurent-free) form so the file lives over a
generic `CommRing R` with no inverses and no archimedean input (§7c).
The symmetric quantum integer

  `[n]_q = q^{n−1} + q^{n−3} + ⋯ + q^{−(n−1)}`

satisfies `q^{n−1} · [n]_q = ∑_{i<n} q^{2i} =: framedQInt q n`, and

  `q^{n−1} · ([n]_q − [n−1]_q) = framedQInt q (n+1) − q · framedQInt q n`
                              *(with the index shift `n ↦ n+1`)*.

The two results are:

* `framedQInt_sub_eq_alexanderTorus2` — the difference **is** the normalized
  Alexander polynomial `Δ_{T(2,2n+1)}(q) = ∑_{j < 2n+1} (−q)^j`;
* `one_add_mul_alexanderTorus2_odd` — the division-free closed form
  `(1 + q) · Δ_{T(2,2n+1)}(q) = 1 + q^{2n+1}`,
  i.e. `Δ_{T(2,m)}(q) = (1 + q^m)/(1 + q)`, the classical Alexander
  polynomial of the `(2,m)` torus knot for odd `m`.

## Why this matters to the framework

`n = 1` gives `T(2,3)` — the **trefoil**, which is the framework's electron
knot — with `Δ = 1 − q + q²`. So the very first instance of the identity
lands on the knot the framework already uses, with no tuning. Note this is a
*structural* observation, not a derivation of anything: the identity holds
over any commutative ring and says nothing on its own about masses.

Two adjacent facts are recorded as separate results rather than folded in,
because each is a genuinely different claim:

* `framedQInt_sub_eq_zero_iff_alexander_root` — the vanishing locus
  `[n]_q = [n−1]_q` is exactly the root set of `Δ_{T(2,2n+1)}`.
* `alexanderTorus2_bar_symm` — `Δ` is bar-symmetric, `Δ(q) = q^{m−1} Δ(q⁻¹)`
  in framed form, matching the `bar`-involution the framework uses elsewhere.
-/

namespace QOU.BraidsAndKnots.QIntegerAlexanderTorus

open Finset

variable {R : Type*} [CommRing R]

/-- **Framed symmetric quantum integer**: `framedQInt q n = ∑_{i<n} q^{2i}`,
which is `q^{n−1} · [n]_q` for the symmetric quantum integer
`[n]_q = q^{n−1} + ⋯ + q^{−(n−1)}`. Framing clears the negative powers, so
the whole file works over a generic `CommRing` (§7c). -/
def framedQInt (q : R) (n : ℕ) : R := ∑ i ∈ range n, q ^ (2 * i)

/-- **Normalized Alexander polynomial of the `(2, m)` torus knot**:
`Δ_{T(2,m)}(q) = ∑_{j<m} (−q)^j`. For odd `m` this is the classical
`(1 + q^m)/(1 + q)`; see `one_add_mul_alexanderTorus2_odd`. -/
def alexanderTorus2 (q : R) (m : ℕ) : R := ∑ j ∈ range m, (-q) ^ j

@[simp] theorem framedQInt_zero (q : R) : framedQInt q 0 = 0 := by
  simp [framedQInt]

@[simp] theorem framedQInt_one (q : R) : framedQInt q 1 = 1 := by
  simp [framedQInt]

theorem framedQInt_succ (q : R) (n : ℕ) :
    framedQInt q (n + 1) = framedQInt q n + q ^ (2 * n) := by
  simp [framedQInt, Finset.sum_range_succ]

@[simp] theorem alexanderTorus2_zero (q : R) : alexanderTorus2 q 0 = 0 := by
  simp [alexanderTorus2]

@[simp] theorem alexanderTorus2_one (q : R) : alexanderTorus2 q 1 = 1 := by
  simp [alexanderTorus2]

theorem alexanderTorus2_succ (q : R) (m : ℕ) :
    alexanderTorus2 q (m + 1) = alexanderTorus2 q m + (-q) ^ m := by
  simp [alexanderTorus2, Finset.sum_range_succ]

/-- **The identity.** The framed symmetric quantum-integer difference is the
normalized Alexander polynomial of the `(2, 2n+1)` torus knot:

  `q^n · ([n+1]_q − [n]_q) = Δ_{T(2,2n+1)}(q)`.

Proved by induction; holds over any commutative ring, for every `q`. -/
theorem framedQInt_sub_eq_alexanderTorus2 (q : R) (n : ℕ) :
    framedQInt q (n + 1) - q * framedQInt q n = alexanderTorus2 q (2 * n + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
      have h2 : 2 * (n + 1) + 1 = (2 * n + 1) + 1 + 1 := by ring
      rw [framedQInt_succ q (n + 1), framedQInt_succ q n, h2,
        alexanderTorus2_succ, alexanderTorus2_succ, ← ih]
      have hodd : (-q : R) ^ (2 * n + 1) = -(q ^ (2 * n + 1)) := by
        rw [neg_pow]
        simp [Odd.neg_one_pow ⟨n, by ring⟩]
      have heven : (-q : R) ^ (2 * n + 1 + 1) = q ^ (2 * n + 1 + 1) := by
        rw [neg_pow]
        simp [Even.neg_one_pow ⟨n + 1, by ring⟩]
      rw [hodd, heven]
      ring

/-- **Division-free closed form.** `(1 + q) · Δ_{T(2,m)}(q) = 1 − (−1)^m q^m`.
For odd `m` this is `1 + q^m`, recovering the classical Alexander polynomial
`Δ_{T(2,m)}(q) = (1 + q^m)/(1 + q)` of the `(2,m)` torus knot without
requiring `1 + q` to be invertible. -/
theorem one_add_mul_alexanderTorus2 (q : R) (m : ℕ) :
    (1 + q) * alexanderTorus2 q m = 1 - (-q) ^ m := by
  have h : alexanderTorus2 q m * ((-q) - 1) = (-q) ^ m - 1 := geom_sum_mul (-q) m
  have h' : alexanderTorus2 q m * (1 + q) = 1 - (-q) ^ m := by
    have : ((-q : R) - 1) = -(1 + q) := by ring
    rw [this, mul_neg] at h
    linear_combination -h
  linear_combination h'

/-- The odd specialisation: `(1 + q) · Δ_{T(2,2n+1)}(q) = 1 + q^{2n+1}`. -/
theorem one_add_mul_alexanderTorus2_odd (q : R) (n : ℕ) :
    (1 + q) * alexanderTorus2 q (2 * n + 1) = 1 + q ^ (2 * n + 1) := by
  rw [one_add_mul_alexanderTorus2]
  have hodd : (-q : R) ^ (2 * n + 1) = -(q ^ (2 * n + 1)) := by
    rw [neg_pow]
    simp [Odd.neg_one_pow ⟨n, by ring⟩]
  rw [hodd]
  ring

/-- Combining the two: the framed quantum-integer difference satisfies the
same division-free relation. -/
theorem one_add_mul_framedQInt_sub (q : R) (n : ℕ) :
    (1 + q) * (framedQInt q (n + 1) - q * framedQInt q n) = 1 + q ^ (2 * n + 1) := by
  rw [framedQInt_sub_eq_alexanderTorus2, one_add_mul_alexanderTorus2_odd]

/-- **The trefoil instance** (`n = 1`, knot `T(2,3) = 3₁`), the framework's
electron knot: `Δ_{3₁}(q) = 1 − q + q²`, and it is the framed difference
`[2]_q − [1]_q` in framed form. -/
theorem alexanderTorus2_trefoil (q : R) :
    framedQInt q 2 - q * framedQInt q 1 = 1 - q + q ^ 2 := by
  simp [framedQInt, Finset.sum_range_succ]
  ring

/-- The `T(2,5) = 5₁` instance: `Δ_{5₁}(q) = 1 − q + q² − q³ + q⁴`. -/
theorem alexanderTorus2_five_one (q : R) :
    framedQInt q 3 - q * framedQInt q 2 = 1 - q + q ^ 2 - q ^ 3 + q ^ 4 := by
  simp [framedQInt, Finset.sum_range_succ]
  ring

/-- **The vanishing locus is the Alexander root set.** `[n+1]_q = [n]_q`
(in framed form) exactly when `q` is a root of `Δ_{T(2,2n+1)}`. This is the
statement that makes the "discrete choice instead of fitting" phrasing in the
`U_q(su_n)` mass-sum-rule literature a *root-finding* problem rather than a
parameter fit — an observation about the shape of that programme, not an
endorsement of its numerics. -/
theorem framedQInt_sub_eq_zero_iff_alexander_root (q : R) (n : ℕ) :
    framedQInt q (n + 1) - q * framedQInt q n = 0 ↔ alexanderTorus2 q (2 * n + 1) = 0 := by
  rw [framedQInt_sub_eq_alexanderTorus2]

/-- **Bar symmetry in framed form.** `Δ_{T(2,m)}` is palindromic up to sign:
`q^{m−1} · Δ(q⁻¹) = Δ(q)` unframes to the bar-involution symmetry
`Δ(q) = Δ(q⁻¹)` for odd `m`. Stated here framed, as
`∑_{j<m} (−1)^j q^{m−1−j} = ∑_{j<m} (−1)^j q^j` for odd `m`. -/
theorem alexanderTorus2_bar_symm (q : R) (n : ℕ) :
    ∑ j ∈ range (2 * n + 1), (-1 : R) ^ j * q ^ (2 * n - j)
      = alexanderTorus2 q (2 * n + 1) := by
  unfold alexanderTorus2
  rw [← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl ?_
  intro j hj
  simp only [Finset.mem_range] at hj
  have hj' : j ≤ 2 * n := by omega
  have hsub : 2 * n + 1 - 1 - j = 2 * n - j := by omega
  rw [hsub, neg_pow]
  have : (-1 : R) ^ (2 * n - j) * q ^ (2 * n - j) = (-1 : R) ^ j * q ^ (2 * n - j) := by
    have hpar : ((2 * n - j) % 2) = (j % 2) := by omega
    rcases Nat.even_or_odd j with he | ho
    · have h1 : Even (2 * n - j) := by
        rcases he with ⟨k, hk⟩; exact ⟨n - k, by omega⟩
      rw [h1.neg_one_pow, he.neg_one_pow]
    · have h1 : Odd (2 * n - j) := by
        rcases ho with ⟨k, hk⟩; exact ⟨n - k - 1, by omega⟩
      rw [h1.neg_one_pow, ho.neg_one_pow]
  rw [this]

end QOU.BraidsAndKnots.QIntegerAlexanderTorus
