import Mathlib.Tactic

/-!
# QOU.Observations.SDPRegimeSwitch — SDP dual block is positive semidefinite

**Proposition** ([`prop:sdp-regime-switch`](../../../quantum-observable-universe/observations/sdp-regime-switch.md)).

The SDP extension of the LP-dual operator-selection framework introduces
matrix-valued cross-block couplings `c_{λλ'}` between conjugate-partition
pairs in the Wedderburn decomposition of `H_n(q)`. The SDP dual carries a
`2×2` PSD block per conjugate pair `(λ, λ')`:

```
  ⎛ μ_λ − y₀ − y_λ        c_{λλ'}      ⎞
  ⎝ c_{λλ'}          μ_{λ'} − y₀ − y_{λ'} ⎠  ⪰  0
```

## Disposition (derived, not projected)

The previous encoding carried a `holds`-style restatement: the class
fields `diag_nonneg` / `det_cond` already *are* the scalar Sylvester
conditions, and the "theorem" merely re-emitted them. Here those two
conditions are the genuine **dual-feasibility inputs** (the SDP solution's
slack), and the theorem **derives** the actual positive-semidefiniteness
of the block — its quadratic form is non-negative for *every* test vector
`(x₀, x₁)`:

  `(μ_λ − y₀ − y_λ)·x₀² + 2·c_{λλ'}·x₀x₁ + (μ_{λ'} − y₀ − y_{λ'})·x₁² ≥ 0`.

This is Sylvester's criterion for a symmetric `2×2` matrix
(`d ≥ 0`, `d' ≥ 0`, `dd' ≥ c²` ⇒ PSD), proved over any linearly ordered
commutative ring (§7c: nothing archimedean is used) via the identity
`d·Q = (d·x₀ + c·x₁)² + (dd' − c²)·x₁²` (case `d > 0`) and the degenerate
`d = 0 ⇒ c = 0` collapse. The "regime switch" of the manuscript — the
isolated `(Z, N)` values where `c_{λλ'} = 0` — is exactly where the block
diagonalises; the PSD feasibility derived here holds throughout.

-- Ref: [leitner2026] quantum-observable-universe/observations/sdp-regime-switch.md
-/

namespace QOU.Observations

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Dual-feasibility data for the SDP regime-switch block. All fields are
    *inputs* (the SDP solution and its slack); the block's
    positive-semidefiniteness is **derived** in `SDPRegimeSwitch`. -/
class SDPRegimeSwitchContext (R : Type*) [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  /-- The substrate parameter `q`. -/
  q : R
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Per-partition q-Laplacian eigenvalue `μ_λ`. -/
  μ : ℕ → R
  /-- LP-dual variable `y_0`. -/
  y_0 : R
  /-- Per-partition LP-dual variables `y_λ`. -/
  y : ℕ → R
  /-- Per-conjugate-pair coupling `c_{λλ'}`. -/
  c_couple : ℕ → ℕ → R
  /-- Dual feasibility (diagonal slack ≥ 0): the `2×2` block diagonal
      entries `μ − y₀ − y` are non-negative. -/
  diag_nonneg : ∀ l l' : ℕ,
    0 ≤ μ l - y_0 - y l ∧
    0 ≤ μ l' - y_0 - y l'
  /-- Dual feasibility (determinant slack ≥ 0): the product of diagonals
      dominates the squared coupling. -/
  det_cond : ∀ l l' : ℕ,
    (c_couple l l') ^ 2 ≤ (μ l - y_0 - y l) * (μ l' - y_0 - y l')

/-- **SDP dual block is positive semidefinite** ([`prop:sdp-regime-switch`]).

    For every conjugate pair `(l, l')` the `2×2` dual block is PSD: its
    quadratic form is non-negative for every test vector `(x₀, x₁)`,

      `d·x₀² + 2c·x₀x₁ + d'·x₁² ≥ 0`,   `d := μ_l − y₀ − y_l`, etc.

    **Derived** (Sylvester) from the dual-feasibility inputs `diag_nonneg`
    (`d, d' ≥ 0`) and `det_cond` (`c² ≤ dd'`) — the genuine
    semidefiniteness of the block, not a restatement of the scalar slacks.
    Proof: for `d > 0`, `d·Q = (d·x₀ + c·x₁)² + (dd' − c²)·x₁² ≥ 0`; for
    `d = 0`, `c² ≤ 0` forces `c = 0` and `Q = d'·x₁² ≥ 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/sdp-regime-switch.md
theorem SDPRegimeSwitch [ctx : SDPRegimeSwitchContext R] (l l' : ℕ) (x0 x1 : R) :
    0 ≤ (ctx.μ l - ctx.y_0 - ctx.y l) * x0 ^ 2
      + 2 * ctx.c_couple l l' * x0 * x1
      + (ctx.μ l' - ctx.y_0 - ctx.y l') * x1 ^ 2 := by
  obtain ⟨hd, hd'⟩ := ctx.diag_nonneg l l'
  have hdet := ctx.det_cond l l'
  set d := ctx.μ l - ctx.y_0 - ctx.y l with hd_def
  set d' := ctx.μ l' - ctx.y_0 - ctx.y l' with hd'_def
  set c := ctx.c_couple l l' with hc_def
  rcases lt_or_eq_of_le hd with hdpos | hd0
  · -- d > 0:  d·Q = (d·x₀ + c·x₁)² + (dd' − c²)·x₁² ≥ 0,  d > 0 ⇒ Q ≥ 0.
    nlinarith [sq_nonneg (d * x0 + c * x1),
      mul_nonneg (sub_nonneg.mpr hdet) (sq_nonneg x1), hdpos]
  · -- d = 0:  c² ≤ d·d' = 0 ⇒ c = 0,  Q = d'·x₁² ≥ 0.
    have hc0 : c = 0 := by
      have hc2 : c ^ 2 ≤ 0 := by rw [← hd0] at hdet; simpa using hdet
      have : c ^ 2 = 0 := le_antisymm hc2 (sq_nonneg c)
      exact pow_eq_zero_iff (by norm_num : (2 : ℕ) ≠ 0) |>.mp this
    rw [hc0, ← hd0]
    nlinarith [mul_nonneg hd' (sq_nonneg x1)]

end QOU.Observations
