import Mathlib.Tactic

/-!
# QOU.Nuclear.PretzelLevelTwoBlockFactorization — the algebra that splits the `(−2,3,7)` index into six blocks

## Where this sits (Route C, M3, beans `qou-x3iv` Part 18, `qou-m3ad`, `qou-gz37`)

The `(−2,3,7)` pretzel's state integral is one-dimensional with factor vector
`(1,1,2)` (`qou-x3iv` Parts 10–12a; Garoufalidis–Kashaev 1411.6062 eq (56)). Read
as a `U(1)` theory with tetrahedron chirals of gauge charge `(1,1,2)` at
Chern–Simons level `2`, its 3D index is

`I(m,ζ) = Σₙ q⁻ⁿ CT_z [ z²ⁿ I_Δ(n+m, zζ) I_Δ(n−m, z/ζ) I_Δ(2n, z²) ]`.

The probe `aomega_m3_pretzel_index_factorisation_blocks_probe.py` checks this
against the triangulation index of SnapPy's `m016` on every cell `m ∈ [−2,2]`,
`e ∈ [−6,6]` to `q³`, and against Garoufalidis–Zagier's printed total index to
`q⁷`. Closing the contour on the poles of the three denominators gives **six**
families, and each one is a product of a `q`-series in `x = q^{m/2}ζ` and the same
series at `q⁻¹` in `x̃ = q^{m/2}/ζ` (GGM eq (19)).

This file proves the **exponent and sign bookkeeping** behind that split. It is
exact integer and field algebra. The infinite products and the contour argument
are analytic and are not formalised here. If they are, they belong in
`QOU/Transcendental/`.

* `theta_exponent_splits`: the unit-family Gaussian `q^{−n} z^{2n}` splits into
  a `q`-side `B(B+1)` and a `q⁻¹`-side `−A(A+1)`.
* `doubled_exponent_splits`: the doubled-family exponent splits into
  `j(j+2)/4` and `−i(i+2)/4`, once `i − j = 2n`.
* `doubled_pole_sign_and_parity`: on a doubled pole the `q`-side sign `σ` equals
  the `q⁻¹`-side sign `σ'`, and `i ≡ j (mod 2)`. This is the level-2 pairing rule
  that Parts 12b–17 searched for: **same sign, same parity** on both sides.
* `odd_parity_quarter_offset`: the odd-parity doubled blocks start at `q^{3/4}`.
* `fundamental_sq_eq_adjoint_add_one`: with `σ = m + m⁻¹` and `s = m² + 1 + m⁻²`,
  `σ² = s + 1`. The doubled blocks see the meridian only through `±σ`.
* `family_count`: `2 + 2·2 = 6`, the pretzel's rank.

-- Ref: [leitner2026] computations/probes/aomega_m3_pretzel_index_factorisation_blocks_probe.py
-- Ref: [ggm-2021] library/arxiv-2012.00062v3 eq (19) (block form of the rotated index)
-- Ref: [garoufalidis-zagier-2024] library/arxiv-2111.06645 Obs 3.9 (printed total index)
-/

namespace QOU.Nuclear.PretzelLevelTwoBlockFactorization

/-- **The unit-family Gaussian splits.** On the pole `x̃₁ = qⁱ`, `x₁ = q⁻ʲ` the flux
is `n = i − j − m`, and with `x = qᵃ`, `x̃ = qᵇ`, `A = i − b`, `B = j + a`, the
exponent of `q^{−n} z^{2n}` is `(A − B)(−1 − A − B)`. It equals
`B(B+1) − A(A+1)`: a `q`-side term in `j` and a `q⁻¹`-side term in `i`, with no
cross term. -/
theorem theta_exponent_splits {R : Type*} [CommRing R] (A B : R) :
    (A - B) * (-1 - A - B) = B * (B + 1) - A * (A + 1) := by
  ring

/-- **The doubled-family exponent splits.** On a doubled pole `s = σ q^{−j/2}`,
`s̃ = σ q^{i/2}` with `i − j = 2n`, four times the exponent of
`q^{−n} (s/s̃)ⁿ` is `−4n − 2(i+j)n`. It equals `j(j+2) − i(i+2)`. -/
theorem doubled_exponent_splits (i j n : ℤ) (h : i - j = 2 * n) :
    -4 * n - 2 * (i + j) * n = j * (j + 2) - i * (i + 2) := by
  have : i = j + 2 * n := by omega
  subst this
  ring

/-- **Same sign, same parity.** A doubled pole needs `σ σ' q^{(i−j)/2} = qⁿ`. Over
signs `σ, σ' ∈ {±1}` and integers this forces `σ = σ'` and `i ≡ j (mod 2)`. -/
theorem doubled_pole_sign_and_parity (σ σ' : ℤ) (hσ : σ = 1 ∨ σ = -1)
    (hσ' : σ' = 1 ∨ σ' = -1) (i j n : ℤ)
    (hsign : σ * σ' = 1) (hexp : i - j = 2 * n) :
    σ = σ' ∧ i % 2 = j % 2 := by
  refine ⟨?_, by omega⟩
  rcases hσ with h | h <;> rcases hσ' with h' | h' <;> subst h <;> subst h' <;> simp_all

/-- **Odd parity starts at `q^{3/4}`.** For odd `j`, `j(j+2) ≡ 3 (mod 4)`, so the
exponent `j(j+2)/4` has fractional part `3/4`. For even `j = 2k` it is the integer
`k(k+1)`. -/
theorem odd_parity_quarter_offset (k : ℤ) :
    (2 * k + 1) * (2 * k + 3) = 4 * (k * k + 2 * k) + 3 ∧
      (2 * k) * (2 * k + 2) = 4 * (k * (k + 1)) := by
  constructor <;> ring

/-- **The fundamental character squares to the adjoint plus one.** The doubled
blocks depend on the meridian eigenvalue `m` only through `σ = m + m⁻¹`. With
`s = m² + 1 + m⁻²` (the adjoint character `s(x)`, `x = m²`), `σ² = s + 1` over any
commutative ring for `m : Rˣ`. So a `σ`-even expression lies in `ℤ[s]` and a
`σ`-odd one does not. -/
theorem fundamental_sq_eq_adjoint_add_one {R : Type*} [CommRing R] (m : Rˣ) :
    ((m : R) + (↑m⁻¹ : R)) ^ 2 = ((m : R) ^ 2 + 1 + (↑m⁻¹ : R) ^ 2) + 1 := by
  have hm : (m : R) * (↑m⁻¹ : R) = 1 := Units.mul_inv m
  linear_combination 2 * hm

/-- **Six families.** Two unit families (chirals 1 and 2) and `2 × 2` doubled
families (sign `σ`, parity `ε`). The count matches the pretzel's rank `6`
(GZ weight dimensions `1 + 4 + 1`). -/
theorem family_count : 2 + 2 * 2 = 6 ∧ 1 + 4 + 1 = 6 := by decide

end QOU.Nuclear.PretzelLevelTwoBlockFactorization
