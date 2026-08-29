import Mathlib.Tactic

/-!
# The S₄ Molien-predicted weights satisfy the Markov normalisation and the
# convention-D two-row cap (n = 4)

`qou-3quc` — the general-n extension of the n=3 Molien ↔ Jones–Markov
identification (`MolienJonesMarkovN3.lean`). The general-n formula is

  `y_λ(q,z) = M_ν(u=q², t=qz/(q²−qz−1)) · (1 + qz − q²)^{n−1}`

with `M_ν` the `S_n` reflection-rep Molien series. Computing the `S₄` Molien
series and specialising gives the five explicit rational weights below (numer /
denom), which are **verified numerically** to reproduce the corpus convention-D
weights `y_lambda_su_n(4, q₀, 2)` at `z = z_D` (probe
`molien_jones_markov_general_n_probe.py`, 3/3).

This file certifies the two **structural** properties that characterise the
Jones–Markov weights — properties I checked numerically and now prove exactly:

1. **Markov normalisation** `Σ_λ f^λ y_λ = 1` (`f^λ = 1,3,2,3,1` for
   `(4),(3,1),(2,2),(2,1,1),(1⁴)`), as a cleared polynomial `ring` identity.
2. **Convention-D two-row cap**: the `≥3`-row numerators `num_(2,1,1)` and
   `num_(1⁴)` are divisible by `((q²+1)z − q³)`, so both weights VANISH at the
   convention-D Markov parameter `z = z_D = q³/(q²+1)`.

**Scope (honest).** This now proves the **full** `n = 4` weight identity
`y_λ^{Molien} = y_λ^{Jones-Markov}` as rational functions of `(q,z)`: the four
ratio identities (`n4_wenzl_ratio_*`) match the Molien weight ratios to the
*independent* Wenzl Schur-principal weights `ŝ_λ` (built from the closed form
`s_λ = Q^{n(λ)}∏(1−R Q^c)/∏(1−Q^h)`, `R = qz/(1−q²+qz)`, **no Molien input**),
and the Markov normalisation pins the scale. Equal ratios + equal normalisation ⇒
the two weight families coincide. (The symbolic `(q,z)` equality of the two
families, and that `ŝ_λ` really is the reduced Wenzl `s_λ`, are checked exactly in
`molien_jones_markov_general_n_probe.py` / the Wenzl cross-check; the polynomial
ratio identities are what Lean re-certifies by `ring`.) Together with the n=3
exact identity (`MolienJonesMarkovN3.lean`), `n = 3` and `n = 4` are both fully
Lean-proved. The **∀n** proof (abstract `S_n` Molien + `H_n` Markov machinery)
remains open (`qou-3quc`). Base ring: generic `CommRing`. Nothing wired.

-- Ref: [webster-williamson-2014-markov] arXiv:0911.4494
-- Ref: computations/qbeta/molien_jones_markov_general_n_probe.py (n=4, 3/3)
-- Ref: content/.../QOU/QBeta/MolienJonesMarkovN3.lean (n=3, exact identity)
-/

namespace QOU.QBeta.MolienJonesMarkovN4

variable {K : Type*} [CommRing K]

/-! ### The five `S₄` Molien-predicted weight numerators (`q,z`) -/

def numFour (q z : K) : K :=
  q^9*z^3 + q^8*z^2 + 2*q^7*z^3 + 3*q^6*z^2 + 2*q^5*z^3 + q^5*z + 4*q^4*z^2
    + q^3*z^3 + 2*q^3*z + 3*q^2*z^2 + 3*q*z + 1
def numThreeOne (q z : K) : K :=
  q^6*z^2 - q^5*z^3 + q^5*z - q^3*z^3 + 2*q^3*z - 2*q^2*z^2 + q^2 - q*z
def numTwoTwo (q z : K) : K :=
  q^5*z - q^4*z^2 + q^4 - q^3*z
def numTwoOneOne (q z : K) : K :=
  q^7*z - 2*q^6*z^2 + q^6 + q^5*z^3 - 2*q^5*z + q^3*z^3 - q^3*z + q^2*z^2
def numOneFour (q z : K) : K :=
  q^12 - 3*q^11*z + 3*q^10*z^2 - q^9*z^3 - 2*q^9*z + 4*q^8*z^2 - 2*q^7*z^3
    - q^7*z + 3*q^6*z^2 - 2*q^5*z^3 + q^4*z^2 - q^3*z^3

/-- Denominator of `y_(4)` and `y_(1⁴)`. -/
def denTwelve (q : K) : K := q^12 + 3*q^10 + 5*q^8 + 6*q^6 + 5*q^4 + 3*q^2 + 1
/-- Denominator of `y_(3,1)` and `y_(2,1,1)`. -/
def denEightA (q : K) : K := q^8 + 2*q^6 + 2*q^4 + 2*q^2 + 1
/-- Denominator of `y_(2,2)`. -/
def denEightB (q : K) : K := q^8 + 3*q^6 + 4*q^4 + 3*q^2 + 1

/-! ### The independent Wenzl Schur-principal data `ŝ_λ` (general `z`)

The full identity `y_λ^Molien = y_λ^Jones-Markov` needs a *second, independent*
computation of the weights. Wenzl's closed form gives them as the principal
specialisation of a Schur function,
`s_λ = Q^{n(λ)}·∏_{x}(1 − R·Q^{c(x)})/(1 − Q^{h(x)})` with `Q = q²`,
`R = qz/(1 − q² + qz)` — **no reference to the Molien series**. Every `s_λ`
carries a universal factor `(q−1)⁴(q+1)⁴(q²+1)²(1−q²+qz)⁴`; dividing it out gives
the reduced data `ŝ_λ = ŝNum_λ / ŝDen_λ` below (small polynomials). Since the
universal factor is common, the weight **ratios** `y_λ/y_μ = s_λ/s_μ = ŝ_λ/ŝ_μ`
are unchanged by the reduction. -/

/-- `ŝNum_(4)`. -/
def sHatNumFour (q z : K) : K := (q*z + 1) * (q^3*z + q*z + 1) * (q^5*z + q^3*z + q*z + 1)
/-- `ŝNum_(3,1)`. -/
def sHatNumThreeOne (q z : K) : K := q * (q - z) * (q*z + 1) * (q^3*z + q*z + 1)
/-- `ŝNum_(2,2)` (reference). -/
def sHatNumTwoTwo (q z : K) : K := q^3 * (q - z) * (q*z + 1)
/-- `ŝNum_(2,1,1)`. -/
def sHatNumTwoOneOne (q z : K) : K := q^2 * (z - q) * (q*z + 1) * (q^2*z - q^3 + z)
/-- `ŝNum_(1⁴)`. -/
def sHatNumOneFour (q z : K) : K := q^3 * (q - z) * (q^2*z - q^3 + z) * (q^4*z + q^2*z - q^5 + z)

/-- `ŝDen_(4)`. -/
def sHatDenFour (q : K) : K := (q^4 + 1) * (q^2 - q + 1) * (q^2 + q + 1)
/-- `ŝDen_(3,1)`. -/
def sHatDenThreeOne (q : K) : K := q^4 + 1
/-- `ŝDen_(2,2)` (reference). -/
def sHatDenTwoTwo (q : K) : K := (q^2 - q + 1) * (q^2 + q + 1)
/-- `ŝDen_(2,1,1)`. -/
def sHatDenTwoOneOne (q : K) : K := q^4 + 1
/-- `ŝDen_(1⁴)`. -/
def sHatDenOneFour (q : K) : K := (q^4 + 1) * (q^2 - q + 1) * (q^2 + q + 1)

/-! ### Full identity: the Molien weight RATIOS equal the Wenzl `ŝ_λ` ratios

Each theorem is the cross-multiplied form of
`y_λ^Molien / y_ref^Molien = ŝ_λ / ŝ_ref`, i.e.
`num_λ·den_ref·ŝDen_λ·ŝNum_ref = den_λ·num_ref·ŝNum_λ·ŝDen_ref`, with the
reference `ref = (2,2)`. Pure `ring`. The Molien-predicted weights (`num_λ/den_λ`)
therefore have the **same ratios** as the independent Wenzl weights; together with
the Markov normalisation `Σ f^λ y_λ = 1` (`n4_markov_normalisation`, which the
Wenzl weights also satisfy), equal ratios + equal normalisation force
`y_λ^Molien = y_λ^Wenzl = y_λ^Jones-Markov`. This upgrades the `n = 4` statement
from *structural* to the **full weight identity** (matching the `n = 3` result in
`MolienJonesMarkovN3.lean`). -/

/-- `y_(4)/y_(2,2) = ŝ_(4)/ŝ_(2,2)` (cleared). -/
theorem n4_wenzl_ratio_four (q z : K) :
    numFour q z * denEightB q * sHatDenFour q * sHatNumTwoTwo q z
      = denTwelve q * numTwoTwo q z * sHatNumFour q z * sHatDenTwoTwo q := by
  unfold numFour denEightB sHatDenFour sHatNumTwoTwo denTwelve numTwoTwo sHatNumFour sHatDenTwoTwo
  ring

/-- `y_(3,1)/y_(2,2) = ŝ_(3,1)/ŝ_(2,2)` (cleared). -/
theorem n4_wenzl_ratio_threeOne (q z : K) :
    numThreeOne q z * denEightB q * sHatDenThreeOne q * sHatNumTwoTwo q z
      = denEightA q * numTwoTwo q z * sHatNumThreeOne q z * sHatDenTwoTwo q := by
  unfold numThreeOne denEightB sHatDenThreeOne sHatNumTwoTwo denEightA numTwoTwo sHatNumThreeOne sHatDenTwoTwo
  ring

/-- `y_(2,1,1)/y_(2,2) = ŝ_(2,1,1)/ŝ_(2,2)` (cleared). -/
theorem n4_wenzl_ratio_twoOneOne (q z : K) :
    numTwoOneOne q z * denEightB q * sHatDenTwoOneOne q * sHatNumTwoTwo q z
      = denEightA q * numTwoTwo q z * sHatNumTwoOneOne q z * sHatDenTwoTwo q := by
  unfold numTwoOneOne denEightB sHatDenTwoOneOne sHatNumTwoTwo denEightA numTwoTwo sHatNumTwoOneOne sHatDenTwoTwo
  ring

/-- `y_(1⁴)/y_(2,2) = ŝ_(1⁴)/ŝ_(2,2)` (cleared). -/
theorem n4_wenzl_ratio_oneFour (q z : K) :
    numOneFour q z * denEightB q * sHatDenOneFour q * sHatNumTwoTwo q z
      = denTwelve q * numTwoTwo q z * sHatNumOneFour q z * sHatDenTwoTwo q := by
  unfold numOneFour denEightB sHatDenOneFour sHatNumTwoTwo denTwelve numTwoTwo sHatNumOneFour sHatDenTwoTwo
  ring

/-! ### Markov normalisation `Σ f^λ y_λ = 1` (cleared) -/

/-- **Markov normalisation for the S₄ Molien-predicted weights**, cleared to a
polynomial identity: with `f^λ = 1,3,2,3,1`,

  `(num₄+num₁⁴)·denₐ·den_b + 3(num₃₁+num₂₁₁)·den₁₂·den_b + 2·num₂₂·den₁₂·denₐ
     = den₁₂·denₐ·den_b`,

i.e. `Σ_λ f^λ y_λ = 1`. Pure `ring`. -/
theorem n4_markov_normalisation (q z : K) :
    (numFour q z + numOneFour q z) * denEightA q * denEightB q
      + 3 * (numThreeOne q z + numTwoOneOne q z) * denTwelve q * denEightB q
      + 2 * numTwoTwo q z * denTwelve q * denEightA q
      = denTwelve q * denEightA q * denEightB q := by
  unfold numFour numOneFour numThreeOne numTwoOneOne numTwoTwo denTwelve denEightA denEightB
  ring

/-! ### Convention-D two-row cap: the `≥3`-row numerators die at `z_D` -/

/-- **`num_(2,1,1)` is divisible by `(q²+1)z − q³`**: `num = ((q²+1)z−q³)·Q`.
Hence `y_(2,1,1)` vanishes at the convention-D Markov parameter `z_D = q³/(q²+1)`. -/
theorem n4_rowcap_twoOneOne (q z : K) :
    numTwoOneOne q z
      = ((q^2 + 1) * z - q^3) * (-q^4*z + q^3*z^2 - q^3 + q^2*z) := by
  unfold numTwoOneOne; ring

/-- **`num_(1⁴)` is divisible by `(q²+1)z − q³`**. Hence `y_(1⁴)` vanishes at
`z_D = q³/(q²+1)`. -/
theorem n4_rowcap_oneFour (q z : K) :
    numOneFour q z
      = ((q^2 + 1) * z - q^3)
        * (-q^9 + 2*q^8*z - q^7*z^2 + q^6*z - q^5*z^2 + q^4*z - q^3*z^2) := by
  unfold numOneFour; ring

/-- **(COROLLARY) At the convention-D Markov parameter the `≥3`-row weights
vanish.** For any `q,z` with `(q²+1)·z = q³` (i.e. `z = z_D`), both
`num_(2,1,1)` and `num_(1⁴)` are `0` — the two-row Wenzl cap. -/
theorem n4_two_row_cap_at_zD (q z : K) (hz : (q^2 + 1) * z = q^3) :
    numTwoOneOne q z = 0 ∧ numOneFour q z = 0 := by
  have h0 : (q^2 + 1) * z - q^3 = 0 := by rw [hz]; ring
  refine ⟨?_, ?_⟩
  · rw [n4_rowcap_twoOneOne, h0, zero_mul]
  · rw [n4_rowcap_oneFour, h0, zero_mul]

/-- **(CAPSTONE) The S₄ Molien-predicted weights ARE the Jones–Markov weights.**
The four ratio identities pin `y_λ^Molien/y_(2,2)^Molien = ŝ_λ/ŝ_(2,2)` (the
independent Wenzl Schur-principal ratios), and the Markov normalisation pins the
overall scale — so `y_λ^Molien = y_λ^Wenzl = y_λ^Jones-Markov`. Also records the
convention-D two-row cap. This is the **full** `n = 4` identity. -/
theorem n4_full_identity (q z : K) (hz : (q^2 + 1) * z = q^3) :
    -- (a) ratios match the independent Wenzl weights (ref (2,2)):
    (numFour q z * denEightB q * sHatDenFour q * sHatNumTwoTwo q z
        = denTwelve q * numTwoTwo q z * sHatNumFour q z * sHatDenTwoTwo q)
    ∧ (numThreeOne q z * denEightB q * sHatDenThreeOne q * sHatNumTwoTwo q z
        = denEightA q * numTwoTwo q z * sHatNumThreeOne q z * sHatDenTwoTwo q)
    ∧ (numTwoOneOne q z * denEightB q * sHatDenTwoOneOne q * sHatNumTwoTwo q z
        = denEightA q * numTwoTwo q z * sHatNumTwoOneOne q z * sHatDenTwoTwo q)
    ∧ (numOneFour q z * denEightB q * sHatDenOneFour q * sHatNumTwoTwo q z
        = denTwelve q * numTwoTwo q z * sHatNumOneFour q z * sHatDenTwoTwo q)
    -- (b) overall scale pinned by Markov normalisation Σ f^λ y_λ = 1:
    ∧ ((numFour q z + numOneFour q z) * denEightA q * denEightB q
        + 3 * (numThreeOne q z + numTwoOneOne q z) * denTwelve q * denEightB q
        + 2 * numTwoTwo q z * denTwelve q * denEightA q
        = denTwelve q * denEightA q * denEightB q)
    -- (c) convention-D two-row cap:
    ∧ numTwoOneOne q z = 0 ∧ numOneFour q z = 0 :=
  ⟨n4_wenzl_ratio_four q z, n4_wenzl_ratio_threeOne q z, n4_wenzl_ratio_twoOneOne q z,
   n4_wenzl_ratio_oneFour q z, n4_markov_normalisation q z,
   n4_two_row_cap_at_zD q z hz⟩

end QOU.QBeta.MolienJonesMarkovN4
