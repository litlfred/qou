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

**Scope (honest).** This proves the Molien-predicted `S₄` weights are
Markov-normalised and satisfy the D-cap — necessary properties of the true
Jones–Markov weights. It does **not** prove `y_λ^{Molien} = y_λ^{Jones-Markov}`
as rational functions of `(q,z)`: that additionally needs the *independent*
general-`z` `H₄` weights (e.g. via Wenzl's closed form), which are not formalised
here. Together with the n=3 exact identity (`MolienJonesMarkovN3.lean`) and the
n=4 numeric per-weight match, this is the formalised evidence for general n.
The **∀n** proof (abstract `S_n` Molien + `H_n` Markov machinery) remains open
(`qou-3quc`). Base ring: generic `CommRing`. Nothing wired.

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

/-- **(CAPSTONE) The S₄ Molien-predicted weights are Markov-normalised and satisfy
the convention-D two-row cap.** -/
theorem n4_structural (q z : K) (hz : (q^2 + 1) * z = q^3) :
    ((numFour q z + numOneFour q z) * denEightA q * denEightB q
      + 3 * (numThreeOne q z + numTwoOneOne q z) * denTwelve q * denEightB q
      + 2 * numTwoTwo q z * denTwelve q * denEightA q
      = denTwelve q * denEightA q * denEightB q)
    ∧ numTwoOneOne q z = 0 ∧ numOneFour q z = 0 :=
  ⟨n4_markov_normalisation q z, n4_two_row_cap_at_zD q z hz⟩

end QOU.QBeta.MolienJonesMarkovN4
