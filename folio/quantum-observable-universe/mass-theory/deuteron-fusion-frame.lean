/-
  Fusion frame of the deuteron 5g law (radical-free algebraic backbone).

  The dimensionless content of the production ²H binding law B = 5g·E_unit
  is canonical Hecke-tower data. This file formalizes the exact algebraic
  identities behind that reading (the numerical/geometric steps — the live
  pyhecke Markov value and the Gauss linking integral — stay in the
  witnessed probes; here is the ring algebra they rest on).

  With v = √q₀ and the symmetric q-integers [2]_v = v + v⁻¹,
  [3]_v = v² + 1 + v⁻²:

    * fusion_identity      [2]_v² = [3]_v + 1        (½⊗½ = 1 ⊕ 0)
    * five_plus_x          1 + [2]_v² = 5 + (v−v⁻¹)²  (the "5" at v = 1)
    * linking_rate_sq      the geometric linking rate² of a slope-z torus
                           pair = z²/(1+z²), independent of scale (the 2π
                           and the torus radii cancel) — the radical-free
                           core of D3
    * criticality_reciprocal   g²(1 + t²) = 1 for g² = (1/t)²/(1+(1/t)²)
                               (marginal-stability = normalized channel
                               projection; take t = [2]_v)
    * deformation_ii_eq_inv   the fully-deformed candidate (1 + [2]_v²)·g
                              equals 1/g — the two deformations 5g and 1/g
                              are the criticality pair

  Generic field, no ℝ, no √ (§7c): every statement is ring/field algebra in
  v and abstract rate/scale variables. The archimedean evaluation at q₀ and
  the MeV unit live downstream.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Tactic

namespace QOU.MassTheory.DeuteronFusion

variable {F : Type*} [Field F]

/-- Symmetric q-integer [2]_v = v + v⁻¹. -/
def twoV (v : F) : F := v + v⁻¹

/-- Symmetric q-integer [3]_v = v² + 1 + v⁻². -/
def threeV (v : F) : F := v ^ 2 + 1 + v⁻¹ ^ 2

/-- **Fusion identity** [2]_v² = [3]_v + 1 — the quantum-dimension form of
    the spin coupling ½ ⊗ ½ = 1 ⊕ 0. -/
theorem fusion_identity (v : F) (hv : v ≠ 0) :
    twoV v ^ 2 = threeV v + 1 := by
  simp only [twoV, threeV]
  field_simp
  ring

/-- **The classical 5.** 1 + [2]_v² = 5 + (v − v⁻¹)², so at v = 1 the
    total quantum dimension of the two-nucleon channel decomposition is 5. -/
theorem five_plus_x (v : F) (hv : v ≠ 0) :
    1 + twoV v ^ 2 = 5 + (v - v⁻¹) ^ 2 := by
  simp only [twoV]
  field_simp
  ring

/-- Sanity: at v = 1 the total quantum dimension is exactly 5. -/
theorem total_dim_at_one : 1 + twoV (1 : F) ^ 2 = 5 := by
  simp only [twoV, inv_one]
  norm_num

/-- **Linking rate², geometry-independent (the radical-free core of D3).**
    For a slope `z = n·r/R` geodesic pair on a torus with cycle
    circumferences `(c·R, c·r)` (`c = 2π`), the squared linking rate
    `(|Lk|·c·r)² / L²`, `L² = (c·R)²(1+z²)`, equals `z²/(1+z²)` — the 2π
    and the individual radii cancel; only the slope survives. -/
theorem linking_rate_sq (R r n c : F) (hR : R ≠ 0) (hc : c ≠ 0)
    (hD : 1 + (n * r / R) ^ 2 ≠ 0) :
    (n * (c * r)) ^ 2 / ((c * R) ^ 2 * (1 + (n * r / R) ^ 2))
      = (n * r / R) ^ 2 / (1 + (n * r / R) ^ 2) := by
  rw [div_eq_div_iff
        (mul_ne_zero (pow_ne_zero 2 (mul_ne_zero hc hR)) hD) hD]
  field_simp

/-- **Criticality = normalized channel projection.** With `t = [2]_v` and
    the squared rate `g²` defined by `g²·(1 + z²) = z²` for `z = 1/t` (i.e.
    `g² = z²/(1+z²)` cleared of its outer division), one has `g²·(1 + t²) = 1`:
    the landed magnitude is exactly the marginal-stability point. -/
theorem criticality_reciprocal (t gsq : F) (ht : t ≠ 0)
    (hg : gsq * (1 + (1 / t) ^ 2) = (1 / t) ^ 2) :
    gsq * (1 + t ^ 2) = 1 := by
  have ht2 : t ^ 2 ≠ 0 := pow_ne_zero 2 ht
  field_simp at hg
  linear_combination hg

/-- **Deformation (ii) = 1/g.** The fully-deformed candidate `s·g` equals
    `g⁻¹` whenever `g²·s = 1` — so the two canonical deformations of the
    classical 5, namely `5g` and `(1 + [2]_v²)·g`, are the criticality pair
    `5g` and `1/g`, split by the exact factor `(1 + [2]_v²)/5 = 1 + x/5`. -/
theorem deformation_ii_eq_inv (g s : F) (hg : g ≠ 0) (h : g ^ 2 * s = 1) :
    s * g = g⁻¹ := by
  field_simp
  linear_combination h

/-- **`5g` in closed form (deformation (i)).** At criticality the exchange
    rate satisfies `g²·(5 + x) = 1` with `x = (v − v⁻¹)²` (compose
    `criticality_reciprocal` with `five_plus_x`). Then the squared binding
    magnitude obeys `(5g)²·(5 + x) = 25` — the radical-free form of
    `5g = 5/√(5 + x)`. The reeb-flow §2e correction ladder
    `√5·(1 − x/10 + 3x²/200 − x³/400 − ⋯)` is exactly the Taylor expansion
    of this closed form (coefficients recorded in the D4 witness). -/
theorem five_g_closed (g x : F) (h : g ^ 2 * (5 + x) = 1) :
    (5 * g) ^ 2 * (5 + x) = 25 := by
  linear_combination 25 * h

/-- **The two deformations split by exactly `1 + x/5`.** Cross-multiplied
    form of `(1/g)² / (5g)² = (5 + x)² / 25`: the fully-deformed `1/g` and
    the classical-count `5g` coincide at `x = 0` (v = 1) and separate at
    first order in the deformation parameter `x`. -/
theorem deformation_split (g x : F) (hg : g ≠ 0) (h : g ^ 2 * (5 + x) = 1) :
    25 * (g⁻¹) ^ 2 = (5 + x) ^ 2 * (5 * g) ^ 2 := by
  have hg2 : g ^ 2 ≠ 0 := pow_ne_zero 2 hg
  rw [inv_pow]
  field_simp
  linear_combination -25 * (g ^ 2 * (5 + x) + 1) * h

/-! ### E_unit parity exclusion (D5)

The bar involution `σ` (the substrate `q ↦ q⁻¹`, an order-2 ring
endomorphism) splits energies into bar-even (`σ x = x`, the binding / cosh
channel) and bar-odd (`σ x = -x`, the 𝔔_β / sinh decay channel). The
deuteron unit `E_unit = B/(5g)` is a quotient of bar-even quantities, hence
bar-even; the β-decay quantum 𝔔_β is bar-odd; a nonzero bar-even quantity is
never a bar-odd one. This is the machine-checked form of the D5 exclusion
of the transition sector as `E_unit`. -/

variable (σ : F →+* F)

/-- Bar-even: fixed by the involution (binding / cosh channel). -/
def BarEven (x : F) : Prop := σ x = x

/-- Bar-odd: negated by the involution (𝔔_β / sinh decay channel). -/
def BarOdd (x : F) : Prop := σ x = -x

/-- **A quotient of bar-even quantities is bar-even.** If `E·s = B` with `B`
    and `s` bar-even and `s ≠ 0`, then `E` is bar-even. Applied to
    `B = 5g·E_unit`: `B` (binding) and `5g` are bar-even, so `E_unit` is. -/
theorem barEven_of_mul {B s E : F} (hs : s ≠ 0) (hB : BarEven σ B)
    (hsdiv : BarEven σ s) (hE : E * s = B) : BarEven σ E := by
  have hmul : σ E * s = E * s := by
    have hcong : σ (E * s) = B := by rw [hE]; exact hB
    rw [map_mul, hsdiv] at hcong
    rw [hcong, hE]
  exact mul_right_cancel₀ hs hmul

/-- **A nonzero bar-even quantity is never bar-odd** (char ≠ 2). Hence the
    bar-even `E_unit` cannot equal the bar-odd `𝔔_β`: the entire bar-odd
    transition sector is excluded as the deuteron unit. -/
theorem barEven_ne_barOdd {E Q : F} (hchar : (2 : F) ≠ 0)
    (hE : BarEven σ E) (hEne : E ≠ 0) (hQ : BarOdd σ Q) : E ≠ Q := by
  intro h
  subst h
  have hEE : E = -E := hE.symm.trans hQ
  have h2 : (2 : F) * E = 0 := by linear_combination hEE
  rcases mul_eq_zero.mp h2 with hc | hz
  · exact hchar hc
  · exact hEne hz

/-- **Parity of a product (bookkeeping).** bar-even × bar-odd is bar-odd.
    So the deuteron law `B = (5g)·E_unit` has `B` bar-odd iff `E_unit` is
    bar-odd (`5g` is bar-even). Which parity `B(²H)` actually carries is an
    *empirical* question, currently open: the reeb-flow §2h data have the
    bar-**even** `2mₑ` closest (+2.6 %) and the bar-**odd** `𝔔_β` worst
    (−21 %), weakly favoring a bar-even unit — so this lemma is neutral
    bookkeeping, not a claim that `B(²H)` is bar-odd. -/
theorem barOdd_of_barEven_mul_barOdd {s U : F}
    (hs : BarEven σ s) (hU : BarOdd σ U) : BarOdd σ (s * U) := by
  show σ (s * U) = -(s * U)
  rw [map_mul, hs, hU, mul_neg]

end QOU.MassTheory.DeuteronFusion
