/-
# Can the photon's colour weights tell the neutron from the proton?

Bean `qou-99qc`. Owner 2026-11-21: build `n` and `p` from the four-term photon
`γ(φ₀, φ₁, φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (`def:photon`) with different colour
weights, as photon-pair products generalising `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`; and test
whether reading 3 forces the colour weights. Pre-registration:
`computations/probes/nucleon_photon_colour_weights/PREREGISTRATION.md`.

Coordinates are those of `QOU.QuarkState.pairNFChiral_eq`: basis
`1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀`.

## Results

* **Characters are linear forms on the normal form.** `chi3`, `chi21`, `chi111` are the
  characters of `H₃(q)` on the three Wedderburn blocks, written on NF coordinates.
  `trace_rho_eq_chi21` identifies `chi21` with the reduced-Burau trace of
  `PhotonPairNormalForm.rho`; `trace_nfP`, `trace_nfN` show that the trace on the proton
  and neutron weight spaces (`NucleonWeightSpaceTraces.A₁, A₂, B₁, B₂`) is
  `chi3 + chi21` on both. So every trace functional of the brief — the one-term quantum
  trace, the D1 = A weight split, label C — is a linear form in `(chi3 X, chi21 X)`.
* **One photon: reading 3 sees only `φ₀ + φ₁`.** `chi3_photon`, `chi21_photon`,
  `chi111_photon`; hence `chi_photon_shift`: moving weight between `σ₀` and `σ₁` changes no
  character. `reading3_line`: every `γ(t, −t, 0)` has `chi3 = 1`, `chi21 = 2`. So reading 3
  cannot fix `φ₀` and `φ₁` separately, for any flavour.
* **Two photons: characters are symmetric in the order** (`chi3_pair_comm`,
  `chi21_pair_comm`, `chi111_pair_comm`), although the elements differ
  (`pair_comm_e`: the `e⁻` coordinates of `γ(a)γ(b)` and `γ(b)γ(a)` differ by
  `a₂(b₀ − b₁) − b₂(a₀ − a₁)`). So under the assignment "the doubly-occurring flavour's
  photon first" (`X_p = γ(w_u)γ(w_d)`, `X_n = γ(w_d)γ(w_u)`) every trace functional is
  the same for `n` and `p`, for every choice of `w_u, w_d` (`majority_rule_traces_agree`).
* **Same element, same everything** (`factorisations_same_functional`): if the proton's
  pair and the neutron's pair both factor one element (for instance `β_Bor`, which every
  point of the PR #8634 solution set factors by definition), no functional of the element
  can tell them apart. This is definitional and is stated only to name it.
* **The scored two-term term is zero for every element, not only for `V³`**
  (`allPairs_connected_zero_P`, `allPairs_connected_zero_N`): `Q₁₂ + Q₂₃ + Q₁₃` is the
  scalar `0` on `W_p` and `−1/3` on `W_n` (`NucleonWeightSpaceTwoTerm.QPairP_eq_sum`,
  `QPairN_eq_sum`), so its connected part vanishes on every matrix.

Base ring (§7c): generic `[CommRing R]` for the NF statements; `[Field R]` where the
weight-space matrices use `q⁻¹`. The ordered-field corollary `reading3_line_nonneg` is the
only place an order is used.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [iwahori1964] https://doi.org/10.15083/00039809
-- Ref: [leitner2026] predicted-spectra, def:photon; prop:borromean-two-photon-factorisation
-/
import QOU.QuarkState.PhotonPairNormalForm
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

namespace QOU.QuarkState.NucleonPhotonColourWeights

open Matrix
open QOU.QuarkState

section NF

variable {R : Type*} [CommRing R]

/-- Trivial character `σᵢ ↦ q` on NF coordinates. -/
def chi3 (q : R) (x : Fin 6 → R) : R :=
  x 0 + q * (x 1 + x 2) + q ^ 2 * (x 3 + x 4) + q ^ 3 * x 5

/-- Sign character `σᵢ ↦ −q⁻¹` on NF coordinates (`q' = q⁻¹`). -/
def chi111 (q' : R) (x : Fin 6 → R) : R :=
  x 0 - q' * (x 1 + x 2) + q' ^ 2 * (x 3 + x 4) - q' ^ 3 * x 5

/-- The `(2,1)` character on NF coordinates: values `2, h, h, −1, −1, 0` on the basis. -/
def chi21 (h : R) (x : Fin 6 → R) : R :=
  2 * x 0 + h * (x 1 + x 2) - (x 3 + x 4)

variable {h q q' : R}

theorem chi3_photon (hh : q - q' = h) (hq : q * q' = 1) (a0 a1 a2 : R) :
    chi3 q (photon h a0 a1 a2) = 1 + q * (a0 + a1) + a2 := by
  rw [photon_eq]; simp [chi3]
  linear_combination (q * a2) * hh + a2 * hq

theorem chi111_photon (hh : q - q' = h) (hq : q * q' = 1) (a0 a1 a2 : R) :
    chi111 q' (photon h a0 a1 a2) = 1 - q' * (a0 + a1) + a2 := by
  rw [photon_eq]; simp [chi111]
  linear_combination (-(q' * a2)) * hh + a2 * hq

theorem chi21_photon (a0 a1 a2 : R) :
    chi21 h (photon h a0 a1 a2) = 2 + h * (a0 + a1) - (1 + h ^ 2) * a2 := by
  rw [photon_eq]; simp [chi21]; ring

/-- **Reading 3 on one photon sees `φ₀ + φ₁` only.** -/
theorem chi_photon_shift (hh : q - q' = h) (hq : q * q' = 1) (a0 a1 a2 t : R) :
    chi3 q (photon h (a0 + t) (a1 - t) a2) = chi3 q (photon h a0 a1 a2) ∧
    chi21 h (photon h (a0 + t) (a1 - t) a2) = chi21 h (photon h a0 a1 a2) ∧
    chi111 q' (photon h (a0 + t) (a1 - t) a2) = chi111 q' (photon h a0 a1 a2) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [chi3_photon hh hq, chi3_photon hh hq]; ring
  · rw [chi21_photon, chi21_photon]; ring
  · rw [chi111_photon hh hq, chi111_photon hh hq]; ring

/-- The line `γ(t, −t, 0)`: both blocks of convention D see the identity values. -/
theorem reading3_line (hh : q - q' = h) (hq : q * q' = 1) (t : R) :
    chi3 q (photon h t (-t) 0) = 1 ∧ chi21 h (photon h t (-t) 0) = 2 := by
  rw [chi3_photon hh hq, chi21_photon]; constructor <;> ring

/-! ### Pair products: order-symmetric characters, order-sensitive element -/

theorem chi3_pair_comm (hh : q - q' = h) (hq : q * q' = 1) (a0 a1 a2 b0 b1 b2 : R) :
    chi3 q (pairNFChiral h a0 a1 a2 b0 b1 b2) = chi3 q (pairNFChiral h b0 b1 b2 a0 a1 a2) := by
  rw [pairNFChiral_eq, pairNFChiral_eq]; simp [chi3]
  linear_combination (-q ^ 2 * (a0 * b2 - a1 * b2 - a2 * b0 + a2 * b1)) * hh
    + (-q * (a0 * b2 - a1 * b2 - a2 * b0 + a2 * b1)) * hq

theorem chi21_pair_comm (a0 a1 a2 b0 b1 b2 : R) :
    chi21 h (pairNFChiral h a0 a1 a2 b0 b1 b2) = chi21 h (pairNFChiral h b0 b1 b2 a0 a1 a2) := by
  rw [pairNFChiral_eq, pairNFChiral_eq]; simp [chi21]; ring

theorem chi111_pair_comm (hh : q - q' = h) (hq : q * q' = 1) (a0 a1 a2 b0 b1 b2 : R) :
    chi111 q' (pairNFChiral h a0 a1 a2 b0 b1 b2) =
      chi111 q' (pairNFChiral h b0 b1 b2 a0 a1 a2) := by
  rw [pairNFChiral_eq, pairNFChiral_eq]; simp [chi111]
  linear_combination (-q' ^ 2 * (a0 * b2 - a1 * b2 - a2 * b0 + a2 * b1)) * hh
    + (q' * (a0 * b2 - a1 * b2 - a2 * b0 + a2 * b1)) * hq

/-- The elements themselves are not symmetric: the `e⁻` coordinates differ. -/
theorem pair_comm_e (a0 a1 a2 b0 b1 b2 : R) :
    pairNFChiral h a0 a1 a2 b0 b1 b2 5 - pairNFChiral h b0 b1 b2 a0 a1 a2 5 =
      a2 * (b0 - b1) - b2 * (a0 - a1) := by
  rw [pairNFChiral_eq, pairNFChiral_eq]; simp; ring

/-- **Majority rule `X_p = γ(w_u)γ(w_d)`, `X_n = γ(w_d)γ(w_u)`: every character agrees.** -/
theorem majority_rule_traces_agree (hh : q - q' = h) (hq : q * q' = 1)
    (u0 u1 u2 d0 d1 d2 : R) :
    chi3 q (pairNFChiral h u0 u1 u2 d0 d1 d2) = chi3 q (pairNFChiral h d0 d1 d2 u0 u1 u2) ∧
    chi21 h (pairNFChiral h u0 u1 u2 d0 d1 d2) = chi21 h (pairNFChiral h d0 d1 d2 u0 u1 u2) ∧
    chi111 q' (pairNFChiral h u0 u1 u2 d0 d1 d2) =
      chi111 q' (pairNFChiral h d0 d1 d2 u0 u1 u2) :=
  ⟨chi3_pair_comm hh hq _ _ _ _ _ _, chi21_pair_comm _ _ _ _ _ _,
    chi111_pair_comm hh hq _ _ _ _ _ _⟩

/-- **Two factorisations of one element are indistinguishable by any functional.** Every
point of PR #8634's solution set factors `β_Bor`, so assigning the proton and the neutron
different points gives the same element. Definitional; stated to name it. -/
theorem factorisations_same_functional {S : Type*} (f : (Fin 6 → R) → S) {T : Fin 6 → R}
    {a0 a1 a2 b0 b1 b2 c0 c1 c2 d0 d1 d2 : R}
    (Hp : pairNFChiral h a0 a1 a2 b0 b1 b2 = T) (Hn : pairNFChiral h c0 c1 c2 d0 d1 d2 = T) :
    f (pairNFChiral h a0 a1 a2 b0 b1 b2) = f (pairNFChiral h c0 c1 c2 d0 d1 d2) := by
  rw [Hp, Hn]

end NF

/-! ## Weight-space traces are `chi3 + chi21`, and the all-pairs term is connected-free -/

section WeightSpace

open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {K : Type*} [Field K]

/-- An NF vector acting on `W_p` (`σ₀ ↦ A₁`, `σ₁ ↦ A₂`; 1-based `σ₁, σ₂` in that file). -/
def nfP (q : K) (v : Fin 6 → K) : Matrix (Fin 3) (Fin 3) K :=
  v 0 • 1 + v 1 • A₁ q + v 2 • A₂ q + v 3 • (A₂ q * A₁ q) + v 4 • (A₁ q * A₂ q)
    + v 5 • (A₁ q * A₂ q * A₁ q)

/-- An NF vector acting on `W_n`. -/
def nfN (q : K) (v : Fin 6 → K) : Matrix (Fin 3) (Fin 3) K :=
  v 0 • 1 + v 1 • B₁ q + v 2 • B₂ q + v 3 • (B₂ q * B₁ q) + v 4 • (B₁ q * B₂ q)
    + v 5 • (B₁ q * B₂ q * B₁ q)

theorem trace_nfP (q : K) (hq : q ≠ 0) (v : Fin 6 → K) :
    trace (nfP q v) = chi3 q v + chi21 (q - q⁻¹) v := by
  simp [nfP, chi3, chi21, A₁, A₂, Matrix.trace_fin_three]
  field_simp
  ring

theorem trace_nfN (q : K) (hq : q ≠ 0) (v : Fin 6 → K) :
    trace (nfN q v) = chi3 q v + chi21 (q - q⁻¹) v := by
  simp [nfN, chi3, chi21, B₁, B₂, Matrix.trace_fin_three]
  field_simp
  ring

/-- `chi21` is the trace of the reduced-Burau representation `rho` of `PhotonPairNormalForm`. -/
theorem trace_rho_eq_chi21 (q : K) (hq : q ≠ 0) (v : Fin 6 → K) :
    trace (rho q v) = chi21 (q - q⁻¹) v := by
  simp [rho, rA, rB, chi21, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]
  field_simp
  ring

/-- **Scored two-term term, proton: zero for every matrix.** -/
theorem allPairs_connected_zero_P (M : Matrix (Fin 3) (Fin 3) K) :
    trace ((Q12p + Q23p + Q13p) * M) = 0 := by
  rw [QPairP_eq_sum]; simp [QPairP]

/-- **Scored two-term term, neutron: the all-pairs insertion is the scalar `−1/3`, so its
connected part `tr(Q_pair M) + tr(M)/3` is zero for every matrix.** -/
theorem allPairs_connected_zero_N (h3 : (3 : K) ≠ 0) (M : Matrix (Fin 3) (Fin 3) K) :
    trace ((Q12n + Q23n + Q13n) * M) + trace M / 3 = 0 := by
  rw [QPairN_eq_sum h3]; simp [QPairN, Matrix.trace_smul]
  field_simp; ring

/-- In particular for every photon-pair element, at any colour weights. -/
theorem allPairs_connected_zero_pair (h3 : (3 : K) ≠ 0) (q a0 a1 a2 b0 b1 b2 : K) :
    trace ((Q12p + Q23p + Q13p) * nfP q (pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2)) = 0 ∧
    trace ((Q12n + Q23n + Q13n) * nfN q (pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2)) +
      trace (nfN q (pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2)) / 3 = 0 :=
  ⟨allPairs_connected_zero_P _, allPairs_connected_zero_N h3 _⟩

end WeightSpace

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Over an ordered field the whole line `γ(t, −t, 0)` passes reading 3 (convention D,
`y_(1³) = 0`): reading 3 does not force `φ₀, φ₁`. -/
theorem reading3_line_nonneg {h q q' : R} (hh : q - q' = h) (hq : q * q' = 1) (t : R) :
    0 ≤ chi3 q (photon h t (-t) 0) ∧ 0 ≤ chi21 h (photon h t (-t) 0) := by
  obtain ⟨h1, h2⟩ := reading3_line hh hq t
  rw [h1, h2]; constructor <;> norm_num

end Ordered

end QOU.QuarkState.NucleonPhotonColourWeights
