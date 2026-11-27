/-
# The H₂ gluon vertex is PSD exactly at an even crossing count

The selection rule for the nucleon's gluon self-coupling term, stated and
proved as the algebraic fact it is.

## The setting

`sdp_gamma_gamma_to_qqbar.py` poses the gluon vertex as an `H₂(q)` semidefinite
program. `H₂(q)` has normal-form basis `{1, σ₀}`, so a candidate vertex is
`T_w = c₁·1 + c_σ·σ₀`, and its two Wedderburn blocks are one-dimensional:

* symmetric `(2)`   — `σ₀ ↦ q`,     projection `c₁ + q·c_σ`
* alternating `(1,1)` — `σ₀ ↦ -q⁻¹`, projection `c₁ - q⁻¹·c_σ`

`T_w` is PSD exactly when both projections are non-negative.

## What is proved

For the vertex `σ₀^k` — `k` gluon crossings — the projections are the `k`-th
powers of the generator's two eigenvalues, because each projection is a ring
homomorphism. So

* `symEigen`: the symmetric projection is `q^k`, positive for every `k` when
  `0 < q`, hence never the binding constraint;
* `altEigen`: the alternating projection is `(-q⁻¹)^k`, and
  **`0 ≤ (-q⁻¹)^k ↔ Even k`**.

PSD at the vertex is therefore a **parity condition on the crossing count**,
and nothing else.

## Why this is the durable form of the rule

The rule it replaces was a Frobenius-positivity test evaluated numerically
against a Gram matrix (`fsh-guts/deprecated/computations/integer-lp-gluon.py`). That
test went stale twice over — it was built at convention C's Markov parameter
and on the superseded `tr_M(e⁻) = z³` rule — and under the production
convention D its premise no longer holds at all, so it selects nothing
(`computations/qbeta/integer_lp_gluon_convention_d.py`).

The statement below has no such exposure. It mentions no Markov parameter, no
Gram matrix, no trace rule and no anchor; it is a fact about the two
one-dimensional representations of `H₂(q)`. A convention change cannot
invalidate it.

## What it does and does not settle

It **excludes** an odd crossing count — including the single `σ₀` that the
convention-D re-run of the integer LP returns as its optimum — and it makes
`σ₀²`, the shipped construction, the minimal non-zero admissible vertex. The
convention-C answer for the neutron (`L₊ → L₋`, four crossings) is likewise
even and admissible.

It does **not** force `k > 0`: `k = 0` is PSD, since the empty vertex is the
identity. Whether the gluon vertex is present at all is a separate question and
is not answered here.

The normalisation `tr_M(T_w) = 1` is deliberately **not** used as the selector.
Imposed as a constraint it admits only the identity — `σ₀²` is PSD but has
`tr_M = 1.128…` at the substrate — so it excludes every non-trivial vertex and
cannot distinguish among them. It is a normalisation of the trace, not a
selection principle. Bean `qou-1qsw`.

## Base ring

`symEigenPow` is stated over a generic `DivisionRing` — it is pure algebra. The
parity statement needs an ordering to say `0 ≤ ·`, so it is stated over an
ordered field — `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`, this
Mathlib's decomposition of the former `LinearOrderedField` (AGENTS.md §7c:
archimedean only where genuinely needed; the ordering is genuinely needed and
nothing stronger is).
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Group.Even

namespace QOU.QBeta.GluonVertexPsdParity

variable {R : Type*}

section Algebra
variable [DivisionRing R]

/-- The symmetric `(2)` block sends `σ₀ ↦ q`, so it sends `σ₀^k ↦ q^k`. -/
def symEigenPow (q : R) (k : ℕ) : R := q ^ k

/-- The alternating `(1,1)` block sends `σ₀ ↦ -q⁻¹`, so it sends
`σ₀^k ↦ (-q⁻¹)^k`. Both projections are ring homomorphisms `H₂(q) → R`, which
is why a power of the generator maps to the power of its eigenvalue. -/
def altEigenPow (q : R) (k : ℕ) : R := (-q⁻¹) ^ k

/-- The alternating projection splits into a sign and a magnitude. This is the
whole content of the parity rule: the magnitude `(q⁻¹)^k` is positive for
`0 < q`, so the sign of the projection is the sign of `(-1)^k`. -/
theorem altEigenPow_eq (q : R) (k : ℕ) :
    altEigenPow q k = (-1 : R) ^ k * (q⁻¹) ^ k := by
  unfold altEigenPow
  exact neg_pow q⁻¹ k

end Algebra

section Ordered
variable [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The symmetric block is never the binding constraint: it is positive at
every crossing count. -/
theorem symEigenPow_pos {q : R} (hq : 0 < q) (k : ℕ) : 0 < symEigenPow q k :=
  pow_pos hq k

/-- **The gluon-vertex parity rule.** For `0 < q`, the alternating projection of
`σ₀^k` is non-negative exactly when `k` is even — so the `H₂` vertex is PSD
exactly at an even number of gluon crossings. -/
theorem altEigenPow_nonneg_iff_even {q : R} (hq : 0 < q) (k : ℕ) :
    0 ≤ altEigenPow q k ↔ Even k := by
  have hinv : 0 < (q⁻¹) ^ k := pow_pos (inv_pos.mpr hq) k
  rw [altEigenPow_eq]
  constructor
  · intro h
    by_contra hodd
    rw [(Nat.not_even_iff_odd.mp hodd).neg_one_pow, neg_one_mul] at h
    exact absurd hinv (not_lt.mpr (neg_nonneg.mp h))
  · intro hk
    rw [hk.neg_one_pow, one_mul]
    exact le_of_lt hinv

/-- An odd crossing count is excluded. Stated separately because it is the
operative direction: it is what rules out the single `σ₀` that the
convention-D integer-LP re-run returns as its optimum. -/
theorem altEigenPow_neg_of_odd {q : R} (hq : 0 < q) {k : ℕ} (hk : Odd k) :
    altEigenPow q k < 0 := by
  have hinv : 0 < (q⁻¹) ^ k := pow_pos (inv_pos.mpr hq) k
  rw [altEigenPow_eq, hk.neg_one_pow, neg_one_mul]
  exact neg_lt_zero.mpr hinv

/-- The vertex `σ₀^k` is PSD (both blocks non-negative) iff `k` is even. -/
theorem vertex_psd_iff_even {q : R} (hq : 0 < q) (k : ℕ) :
    (0 ≤ symEigenPow q k ∧ 0 ≤ altEigenPow q k) ↔ Even k := by
  constructor
  · rintro ⟨_, h⟩
    exact (altEigenPow_nonneg_iff_even hq k).mp h
  · intro hk
    exact ⟨le_of_lt (symEigenPow_pos hq k),
           (altEigenPow_nonneg_iff_even hq k).mpr hk⟩

/-- `σ₀²` — the shipped two-crossing gluon term — is admissible. -/
theorem two_crossings_psd {q : R} (hq : 0 < q) :
    0 ≤ symEigenPow q 2 ∧ 0 ≤ altEigenPow q 2 :=
  (vertex_psd_iff_even hq 2).mpr ⟨1, rfl⟩

/-- A single `σ₀` is **not** admissible — the convention-D LP's optimum is
excluded by the vertex condition. -/
theorem one_crossing_not_psd {q : R} (hq : 0 < q) :
    ¬ (0 ≤ symEigenPow q 1 ∧ 0 ≤ altEigenPow q 1) := by
  intro h
  have : Even 1 := (vertex_psd_iff_even hq 1).mp h
  exact (Nat.not_even_iff_odd.mpr ⟨0, rfl⟩) this

/-- **Four-crossing neutron gluon vertex is PSD and two-crossing product is unity (`qou-1qsw`).**
For `0 < q`, `k = 4` is PSD (`0 ≤ symEigenPow q 4 ∧ 0 ≤ altEigenPow q 4`), and at `k = 2`
the product of the symmetric and alternating eigenvalues `q² · (-q⁻¹)²` equals `1`. -/
theorem four_crossings_psd_and_two_prod_one {q : R} (hq : 0 < q) :
    (0 ≤ symEigenPow q 4 ∧ 0 ≤ altEigenPow q 4) ∧
    symEigenPow q 2 * altEigenPow q 2 = 1 := by
  refine ⟨(vertex_psd_iff_even hq 4).mpr ⟨2, rfl⟩, ?_⟩
  unfold symEigenPow altEigenPow
  have hq0 : q ≠ 0 := hq.ne'
  rw [neg_sq, inv_pow, mul_inv_cancel₀ (pow_ne_zero 2 hq0)]

end Ordered

end QOU.QBeta.GluonVertexPsdParity
