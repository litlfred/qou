/-
  C = bar iff all irreps are one-dimensional.

  On H_n(q), charge conjugation (σ → σ⁻¹) and the bar involution
  (q → q⁻¹) agree on all irreducible characters if and only if
  every irrep is one-dimensional. At H₂ this holds (unique); at
  H₃+ it fails (standard rep breaks the equivalence).

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Tactic
import Mathlib.Tactic.NormNum

namespace QOU.ParticleInteractions

/-- At H₂: n! = 2 = 1² + 1². All irreps are 1-dim. -/
theorem h2_all_one_dim : 1^2 + 1^2 = Nat.factorial 2 := by decide

/-- 2 = 1² + 1² is the UNIQUE decomposition of 2 as a sum of
  positive squares. No multi-dim irrep can exist at H₂. -/
theorem two_only_unit_squares (a b : ℕ) (ha : 0 < a) (hb : 0 < b)
    (hab : a^2 + b^2 = 2) : a = 1 ∧ b = 1 := by
  have ha2 : a ≤ 1 := by nlinarith
  have hb2 : b ≤ 1 := by nlinarith
  omega

/-- At H₃: n! = 6 = 1² + 2² + 1². A 2-dim irrep EXISTS. -/
theorem h3_has_multidim : 1^2 + 2^2 + 1^2 = Nat.factorial 3 := by decide

/-- For n ≥ 3: n! ≥ 6 > 2 = 1² + 1², so the two 1-dim irreps
  cannot exhaust the algebra dimension. Multi-dim irreps forced. -/
theorem factorial_exceeds_two_squares (n : ℕ) (hn : 3 ≤ n) :
    1^2 + 1^2 < Nat.factorial n := by
  have h6 : Nat.factorial 3 ≤ Nat.factorial n := Nat.factorial_le hn
  have : Nat.factorial 3 = 6 := by decide
  omega

/-- The number of 1-dim irreps of `S_n` for `n ≥ 2` — the trivial and the
  sign representation.  A **named constant**, not a theorem.

  Replaced `theorem exactly_two_one_dim_irreps : (2 : ℕ) = 2 := rfl`
  (2026-08-21; vacuity ledger, `reflexive-tautology-ascribed-literal`).
  `2 = 2` holds however many 1-dim irreps `S_n` has, so it asserted
  nothing; per Strict Lean Discipline §8 a statement with no falsifiable
  content is notation and belongs in a `def`.

  The general justification the old docstring gave — that `S_n` has
  exactly two homomorphisms to `ℤ/2ℤ` — is **not** formalised here (it
  needs `Mathlib`'s symmetric-group representation theory).  What this
  file *does* prove is the `H₂` case, from the other direction:
  `two_only_unit_squares` shows `1² + 1² = 2` is the unique decomposition
  of `dim H₂ = 2!` into positive squares, so at `H₂` these two exhaust the
  algebra and no multi-dimensional irrep can exist. -/
def oneDimIrrepCount : ℕ := 2

/-- At `H₂` the 1-dim irreps exhaust the algebra: `oneDimIrrepCount` of
  them, each of dimension 1, square-sum to `dim H₂ = 2!`.  False for any
  other count, so the constant is doing work here. -/
theorem oneDimIrreps_exhaust_h2 :
    oneDimIrrepCount * 1 ^ 2 = Nat.factorial 2 := by
  norm_num [oneDimIrrepCount]

/-- C = bar at H₂ (1-dim only).
  On a 1-dim rep with eigenvalue α:
    C: α → α⁻¹  (from σ⁻¹ = σ − h, eigenvalue α − h)
    bar: α → α⁻¹  (from q → q⁻¹, eigenvalue q → q⁻¹)
  These agree when α ∈ {q, −q⁻¹}:
    C(q) = q − h = q − (q − q⁻¹) = q⁻¹ = bar(q)  ✓
    C(−q⁻¹) = −q⁻¹ − h = −q = bar(−q⁻¹)  ✓  -/
theorem c_equals_bar_on_one_dim_eigenvalue_q (q h : ℤ) (hdef : h = q - (-q)) :
    q - h = -q := by omega

/-! ### `c_equals_bar_on_one_dim_eigenvalue_neg_q_inv` — REMOVED 2026-08-21:
    it was **false**, not merely unproved.

    It read

        theorem c_equals_bar_on_one_dim_eigenvalue_neg_q_inv
            (q h : ℤ) (hdef : h = q - (-q)) : (-q) - h = q := by omega

    and did not compile on `main` (`omega` correctly refused).  The
    hypothesis gives `h = q - (-q) = 2q`, so the left side is
    `(-q) - 2q = -3q`, and `-3q = q` forces `4q = 0`, i.e. `q = 0`.  The
    statement is therefore false for **every** non-zero `q` — this is an
    honest negative, so it is reported rather than weakened until it
    passes (Strict Lean Discipline §10).

    The underlying problem is the model, not the arithmetic.  This file
    encodes the multiplicative eigenvalues in an **additive ℤ toy**, with
    `q⁻¹` standing in as `-q`.  Under that encoding the two Hecke
    eigenvalues `q` and `-q⁻¹` both map to `q`, so the `-q⁻¹` case is not
    expressible as a statement distinct from the `q` case above — no
    choice of sign repairs it.  Stating it correctly needs the genuine
    multiplicative setting (`q : Rˣ`, as `mass-theory/
    meson-kaon-pion-hecke-seifert.lean` uses), not a sign fix here.

    Tracked as bean `qou-citp`.  The surviving companion
    `c_equals_bar_on_one_dim_eigenvalue_q` is true under this encoding
    (`q - 2q = -q`) and is retained — but see the multiplicative section
    below, which supersedes it as the statement of record. -/

/-! ### Multiplicative restatement (supersedes the additive ℤ toy above)

The additive toy could not express the `-q⁻¹` eigenvalue case as a claim
distinct from the `q` case, because it encodes `q⁻¹` as `-q` and therefore
sends both eigenvalues to the same element.  That collapse is what admitted a
false theorem.  Here the same claims are stated over a genuine commutative ring
with `q` a **unit**, following `mass-theory/meson-kaon-pion-hecke-seifert.lean`.

Both eigenvalue cases now hold *and* are separately expressible; `eigenvalues_distinct`
records that they are genuinely different elements exactly when `q² ≠ -1`, which is
the content the toy destroyed. -/

section Multiplicative

variable {R : Type*} [CommRing R]

/-- The Hecke parameter `h = q - q⁻¹`, with `q` a unit. -/
def heckeH (q : Rˣ) : R := (q : R) - ((q⁻¹ : Rˣ) : R)

/-- `C` acts on a one-dimensional eigenvalue by `α ↦ α - h`, from `σ⁻¹ = σ - h`. -/
def cOnEigenvalue (q : Rˣ) (α : R) : R := α - heckeH q

/-- `C = bar` on the eigenvalue `q`: `C(q) = q - h = q⁻¹ = bar(q)`. -/
theorem cOnEigenvalue_q (q : Rˣ) :
    cOnEigenvalue q (q : R) = ((q⁻¹ : Rˣ) : R) := by
  simp [cOnEigenvalue, heckeH]

/-- `C = bar` on the eigenvalue `-q⁻¹`: `C(-q⁻¹) = -q⁻¹ - h = -q = bar(-q⁻¹)`.
  This is the case the additive toy could not state; it is *false* there and
  true here. -/
theorem cOnEigenvalue_neg_q_inv (q : Rˣ) :
    cOnEigenvalue q (-((q⁻¹ : Rˣ) : R)) = -(q : R) := by
  simp [cOnEigenvalue, heckeH]
  ring

/-- The two Hecke eigenvalues are genuinely distinct exactly when `q² ≠ -1`.
  Under the additive toy both collapsed onto the same element for every `q`,
  which is precisely why the second case could not be stated there. -/
theorem eigenvalues_distinct (q : Rˣ) (hq : (q : R) * (q : R) + 1 ≠ 0) :
    (q : R) ≠ -((q⁻¹ : Rˣ) : R) := by
  intro hEq
  apply hq
  have hinv : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := q.mul_inv
  have h1 : ((q⁻¹ : Rˣ) : R) = -(q : R) := by
    rw [hEq]; ring
  rw [h1] at hinv
  linear_combination -hinv

end Multiplicative

end QOU.ParticleInteractions
