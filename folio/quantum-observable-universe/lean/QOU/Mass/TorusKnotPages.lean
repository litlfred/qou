import QOU.BringsSurface.EulerCharacteristicSix
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.Tactic

/-!
# Torus-knot pages: the algebra behind `total_curvature_is_the_computable_half_probe`

`computations/probes/total_curvature_is_the_computable_half_probe.py` (bean `qou-m3sh`)
found that every multi-strand component of the canonical atom closure is a `(2, odd)`-torus
knot — `T(2,7)` on the `sigma` branch, `T(2,5)` / `T(2,3)` on the `sigma^-1` branch — and
read three algebraic facts off that by exact integer arithmetic. This file proves the ones
that are algebra, so the probe's role on them is reduced to a consistency check.

* **The Seifert form of `T(2, n)` is unimodular.** From the 2-strand positive braid the
  Seifert matrix is `(n-1) × (n-1)`, `-1` on the diagonal and `+1` on the superdiagonal.
  It is upper triangular, so its determinant is `(-1)^(n-1)`, which is `1` for odd `n`
  (`seifertT2_det`, `seifertT2_det_eq_one_of_even`). That is the self-duality of
  `H_1(page)` under the Seifert form — the sense in which the vanishing cycles are a frame
  with a dual frame — and it holds for every `n`, not only the three the probe checked.

* **The curvature floor is bookkeeping once Milnor is granted.** Milnor: the infimum of
  total curvature over an isotopy class is `2π · b(L)`, and `b(L) ≥ μ + #knotted`. With
  `μ = A + 1` (`QOU/Mass/SLq2LabelParity.lean`) and `#knotted = A` (the probe, both
  branches, `A = 2, 3, 4, 6`) the floor is `2π(2A + 1)` (`curvature_floor`). The geometry —
  Milnor's theorem, and the identification of the components as torus knots — is NOT
  formalised here; this records only that the arithmetic chain is what it says.

* **The pages embed on Bring's surface by the corpus's own criterion.** The corpus derives
  Bring's genus from torus-knot embeddability (`EulerCharacteristicSix`: `T(2,9)` must
  embed, `T(2,11)` must not, so `g = 4`). The pages found by the probe are `T(2,3)`,
  `T(2,5)`, `T(2,7)`, of Seifert rank `1, 2, 3`, and they embed at the forced genus
  (`pages_embed_on_bring`); `T(2,9)` is the last that does.

* **Bennequin arithmetic.** Both sub-braid shapes that occur, `2` strands with `7`
  crossings and `3` strands with `8`, give `χ = k - c = -5` and Bennequin genus `3`
  (`bennequin_chi`, `bennequin_genus`). On the `sigma` branch that equals `g(T(2,7))`, so
  the braid's own surface has minimal genus and — fibered knots having a unique
  minimal-genus Seifert surface — is the page. The uniqueness theorem is not formalised.

What is checked by the probe but NOT proved here: the Alexander polynomial
`det(V - t Vᵀ) = (tⁿ + 1)/(t + 1)` and the monodromy order `2n`, both verified in exact
integer arithmetic at `n = 3, 5, 7` and left as that.

Ground ring `ℤ` for the Seifert form; `ℕ` bookkeeping elsewhere. Bean `qou-m3sh`.
-/

namespace QOU.Mass.TorusKnotPages

open Matrix

/-- Seifert matrix of `T(2, m + 1)` from its 2-strand positive braid: `m × m`, `-1` on
the diagonal, `+1` on the superdiagonal, `0` elsewhere. -/
def seifertT2 (m : ℕ) : Matrix (Fin m) (Fin m) ℤ :=
  Matrix.of fun i j => if i = j then -1 else if (j : ℕ) = (i : ℕ) + 1 then 1 else 0

theorem seifertT2_blockTriangular (m : ℕ) : (seifertT2 m).BlockTriangular id := by
  intro i j hij
  have hlt : (j : ℕ) < (i : ℕ) := Fin.lt_iff_val_lt_val.mp hij
  have h1 : i ≠ j := fun h => by subst h; exact lt_irrefl _ hlt
  have h2 : (j : ℕ) ≠ (i : ℕ) + 1 := by omega
  simp [seifertT2, h1, h2]

/-- The Seifert matrix is upper triangular with `-1` down the diagonal. -/
theorem seifertT2_det (m : ℕ) : (seifertT2 m).det = (-1) ^ m := by
  rw [Matrix.det_of_upperTriangular (seifertT2_blockTriangular m)]
  simp [seifertT2, Finset.prod_const]

/-- For `T(2, n)` with `n` odd, `m = n - 1` is even and the Seifert form is unimodular
with determinant `1`: `H_1(page)` is self-dual under it. -/
theorem seifertT2_det_eq_one_of_even {m : ℕ} (hm : Even m) : (seifertT2 m).det = 1 := by
  rw [seifertT2_det, hm.neg_one_pow]

/-- The three cases the probe checked, as instances. -/
theorem seifertT2_det_three_five_seven :
    (seifertT2 2).det = 1 ∧ (seifertT2 4).det = 1 ∧ (seifertT2 6).det = 1 :=
  ⟨seifertT2_det_eq_one_of_even ⟨1, rfl⟩, seifertT2_det_eq_one_of_even ⟨2, rfl⟩,
    seifertT2_det_eq_one_of_even ⟨3, rfl⟩⟩

/-- **The curvature floor, as bookkeeping.** Granting Milnor (`inf ∫κ = 2π b`) and the
component-wise bridge bound `b ≥ μ + #knotted`, with `μ = A + 1` and `#knotted = A`, the
floor is `2π (2A + 1)`. Stated with the `2π` factored out. -/
theorem curvature_floor (A mu knotted b : ℕ) (hmu : mu = A + 1) (hk : knotted = A)
    (hb : mu + knotted ≤ b) : 2 * A + 1 ≤ b := by
  omega

/-- The braid presentation on `3A` strands gives `b ≤ 3A`, so the floor and the ceiling
bracket `b` in `[2A + 1, 3A]`, which is non-empty exactly when `A ≥ 1`. -/
theorem bridge_bracket_nonempty (A : ℕ) (hA : 1 ≤ A) : 2 * A + 1 ≤ 3 * A := by
  omega

open QOU.BringsSurface.EulerCharacteristicSix in
/-- The pages the probe found — `T(2,3)`, `T(2,5)`, `T(2,7)` — embed on Bring's surface at
the corpus's forced genus `4`, and `T(2,9)` is the last torus knot of this family that does. -/
theorem pages_embed_on_bring :
    Embeds 2 3 4 ∧ Embeds 2 5 4 ∧ Embeds 2 7 4 ∧ Embeds 2 9 4 ∧ ¬ Embeds 2 11 4 := by
  decide

/-- Bennequin Euler characteristic `χ = k - c` for the two sub-braid shapes that occur. -/
theorem bennequin_chi : (2 : ℤ) - 7 = -5 ∧ (3 : ℤ) - 8 = -5 := by norm_num

/-- Bennequin genus `(c - k + 1) / 2` is `3` for both shapes — equal to `g(T(2,7))`. -/
theorem bennequin_genus : (7 - 2 + 1) / 2 = 3 ∧ (8 - 3 + 1) / 2 = 3 := by decide

/-! ### The Alexander polynomial, as far as the algebra goes

`det(V - X·Vᵀ)` for the bidiagonal Seifert matrix above is a tridiagonal determinant,
diagonal `X - 1`, superdiagonal `1`, subdiagonal `-X`. Expanding along the last row gives
the continuant recurrence `D_m = (X - 1) D_{m-1} + X D_{m-2}` with `D_0 = 1`,
`D_1 = X - 1`. That expansion is the one step NOT carried out in Lean here; what is proved
is the closed form the recurrence forces, `(X + 1) D_m = X^(m+1) + (-1)^m`, so that for
`T(2, n)` with `n = 2g + 1` the Alexander polynomial is `(X^n + 1)/(X + 1)`. The probe
checks the determinant itself, in exact integer arithmetic, at `n = 3, 5, 7`. -/

open Polynomial in
/-- The continuant of `V - X·Vᵀ`: `D_0 = 1`, `D_1 = X - 1`,
`D_{m+2} = (X - 1) D_{m+1} + X D_m`. -/
noncomputable def alexContinuant : ℕ → Polynomial ℤ
  | 0 => 1
  | 1 => X - 1
  | (m + 2) => (X - 1) * alexContinuant (m + 1) + X * alexContinuant m

open Polynomial in
/-- `(X + 1) D_m = X^(m+1) + (-1)^m` for every `m`. -/
theorem alexContinuant_mul_X_add_one (m : ℕ) :
    alexContinuant m * (X + 1) = X ^ (m + 1) + (-1) ^ m := by
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    match m with
    | 0 => simp [alexContinuant]
    | 1 => simp only [alexContinuant]; ring
    | m + 2 =>
      have h1 := ih (m + 1) (by omega)
      have h0 := ih m (by omega)
      calc alexContinuant (m + 2) * (X + 1)
          = (X - 1) * (alexContinuant (m + 1) * (X + 1))
              + X * (alexContinuant m * (X + 1)) := by
            simp only [alexContinuant]; ring
        _ = (X - 1) * (X ^ (m + 2) + (-1) ^ (m + 1)) + X * (X ^ (m + 1) + (-1) ^ m) := by
            rw [h1, h0]
        _ = X ^ (m + 3) + (-1) ^ (m + 2) := by ring

open Polynomial in
/-- For `T(2, 2g + 1)`: `(X + 1) · D_{2g} = X^(2g+1) + 1`, i.e. the Alexander polynomial
is `(X^n + 1)/(X + 1)` with `n = 2g + 1` — degree `2g`, monic, as a fibered knot's must be. -/
theorem alexContinuant_torus (g : ℕ) :
    alexContinuant (2 * g) * (X + 1) = X ^ (2 * g + 1) + 1 := by
  rw [alexContinuant_mul_X_add_one, (even_two_mul g).neg_one_pow]

open Polynomial in
/-- `D_{2g}` divides `X^(2n) - 1` with `n = 2g + 1`. This is the algebraic core of "the
monodromy of `T(2, n)` has order dividing `2n`": Cayley–Hamilton turns it into `h^(2n) = 1`
once the characteristic polynomial of the monodromy is identified with `D_{2g}`, which is
the same determinant step left to the probe (it checks the order is exactly `2n` at
`n = 3, 5, 7`). -/
theorem alexContinuant_dvd_X_pow_sub_one (g : ℕ) :
    alexContinuant (2 * g) ∣ X ^ (2 * (2 * g + 1)) - 1 := by
  refine ⟨(X + 1) * (X ^ (2 * g + 1) - 1), ?_⟩
  have h := alexContinuant_torus g
  calc X ^ (2 * (2 * g + 1)) - 1
      = (X ^ (2 * g + 1) + 1) * (X ^ (2 * g + 1) - 1) := by ring
    _ = (alexContinuant (2 * g) * (X + 1)) * (X ^ (2 * g + 1) - 1) := by rw [h]
    _ = alexContinuant (2 * g) * ((X + 1) * (X ^ (2 * g + 1) - 1)) := by ring

end QOU.Mass.TorusKnotPages
