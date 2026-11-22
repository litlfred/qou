import QOU.MassTheory.PhotonPairReachability

/-!
# The last 19 non-factorising cells of the six-strand photon-pair test

`PhotonPairNoFactor` proves, by a single blocked matrix entry, that 1370 (word, i, j) cells of the
pair test are not two-photon products. Of the 25 cells it leaves out, 6 ARE two-photon products
(`PhotonPairIdleFactor`). This file proves the other 19 are not, on the one-marked-strand sector.

Each proof takes the sector equations `γᵢγⱼ eₛ = μ·w eₛ` at the entries listed, together with
`q·qi = 1`, `tt·μ = 1` and `uu·(q − qi) = 1`, and derives `1 = 0` by `linear_combination` with an
explicit polynomial certificate (a Nullstellensatz certificate). So the statement holds for every
`q` with `q·qi = 1` and `q ≠ ±1`, and every `μ ≠ 0`, over any field.

The certificates were found with Singular's `lift` and checked exactly in sympy before emission;
Lean re-checks each one with `ring`.

-- Ref: [leitner2026] computations/probes/six_strand_photon_pair/six_strand_pair_probe.py
-/

namespace QOU.MassTheory.PhotonPairNoFactorSector

open QOU.MassTheory.PhotonPairReachability

variable {K : Type*} [Field K]

/-- The γγ word `V1V0V1`. -/
def u0 : List (ℕ × Bool) := [(1, true), (2, false), (0, true), (1, false), (1, true), (2, false)]

/-- The γγ word `V2V1V2`. -/
def u1 : List (ℕ × Bool) := [(2, true), (3, false), (1, true), (2, false), (2, true), (3, false)]

/-- The γγ word `V3V2V3`. -/
def u2 : List (ℕ × Bool) := [(3, true), (4, false), (2, true), (3, false), (3, true), (4, false)]

/-- The γγ word `V0V1V2V1V2`. -/
def u3 : List (ℕ × Bool) := [(0, true), (1, false), (1, true), (2, false), (2, true), (3, false), (1, true), (2, false), (2, true), (3, false)]

/-- The γγ word `V0V3V1V2V3`. -/
def u4 : List (ℕ × Bool) := [(0, true), (1, false), (3, true), (4, false), (1, true), (2, false), (2, true), (3, false), (3, true), (4, false)]

/-- The γγ word `V1V2V3V2V3`. -/
def u5 : List (ℕ × Bool) := [(1, true), (2, false), (2, true), (3, false), (3, true), (4, false), (2, true), (3, false), (3, true), (4, false)]

/-- The γγ word `V3V0V1V2V3`. -/
def u6 : List (ℕ × Bool) := [(3, true), (4, false), (0, true), (1, false), (1, true), (2, false), (2, true), (3, false), (3, true), (4, false)]

/-- The γγ word `V3V2V0V3V1`. -/
def u7 : List (ℕ × Bool) := [(3, true), (4, false), (2, true), (3, false), (0, true), (1, false), (3, true), (4, false), (1, true), (2, false)]

/-- The γγ word `V3V2V3V0V1`. -/
def u8 : List (ℕ × Bool) := [(3, true), (4, false), (2, true), (3, false), (3, true), (4, false), (0, true), (1, false), (1, true), (2, false)]

/-- `V1V0V1` at photon positions `(1, 0)` is not a two-photon product. -/
theorem noPair_V1V0V1_1_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 1 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u0 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_0 := congrFun (H (basisVec 1)) 0
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e1_2 := congrFun (H (basisVec 1)) 2
  have e1_3 := congrFun (H (basisVec 1)) 3
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e3_1 := congrFun (H (basisVec 3)) 1
  have e3_2 := congrFun (H (basisVec 3)) 2
  simp only [photon, wordAct, u0, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_0 e1_1 e1_2 e1_3 e2_0 e2_1 e2_2 e3_1 e3_2
  exact one_ne_zero (by linear_combination (a2*q*tt*uu + b2*q*tt*uu - c2*a^2*q*tt^2 - c2*a^2*tt^2*uu - c2*a*c*q*tt^2*uu - c2*a*q*tt^2*uu + c2*b^2*q*tt^2 + c2*b*tt^2 - c2*c*tt^2*uu + c2*μ*q^2*tt^2*uu + c2*μ*q*tt^2*uu^2 + c2*q*tt*uu^2 - c2*qi*tt*uu^2 - c2*tt*uu - 2*a*q*tt*uu + a*qi*tt*uu + a*tt + c*q*tt + c*tt*uu + q*qi*tt*uu + q*tt*uu^2) * e1_0 + (c2*tt*uu^2 - 2*a*tt*uu + c*tt + tt*uu^2) * e1_1 + (-a2*q^2*qi*tt*uu + a2*q*tt*uu + c2*qi*tt*uu^2 - a*qi*tt*uu + a*tt + b*q*qi*tt + b*qi*tt*uu - c*q*qi*tt*uu + c*qi*tt + 2*c*tt*uu + qi*tt*uu^2 + tt*uu) * e1_2 + (a2*q*qi*tt*uu - a2*qi*tt*uu^2 - b2*qi*tt*uu^2 + c2*tt*uu^2 + a*qi*tt - 2*a*tt*uu - b*qi*tt + 2*c*qi*tt*uu + c*tt + tt*uu^2) * e1_3 + (a2*a^2*q*tt^2 + a2*a^2*tt^2*uu + a2*a*c*q*tt^2*uu + a2*a*q*tt^2*uu - a2*b^2*q*tt^2 - a2*b*tt^2 + a2*c*tt^2*uu - a2*μ*q^2*tt^2*uu - a2*μ*q*tt^2*uu^2 - a2*q^2*tt*uu + a2*q*qi*tt*uu + a2*qi*tt*uu^2 + a2*tt*uu - c2*q^2*tt*uu^2 + 2*a*q^2*tt*uu - a*q*qi*tt*uu - a*q*tt + b*qi*tt - c*q^2*tt - c*q*tt*uu - q^2*tt*uu^2 - q*tt*uu) * e2_0 + (-a2*q*tt*uu - c2*q*tt*uu^2 + 2*a*q*tt*uu - a*qi*tt*uu - a*tt - c*q*tt - c*tt*uu - q*tt*uu^2 - tt*uu) * e2_1 + (-a2*q*qi*tt*uu - c2*tt*uu^2 + 2*a*tt*uu + b*qi*tt - c*qi*tt*uu - c*tt - tt*uu^2) * e2_2 + (-a2*q*qi*tt*uu + b2*qi*tt*uu^2 + a*tt*uu - c*qi*tt*uu - c*tt - tt*uu^2) * e3_1 + (a2*q^2*qi*tt*uu - a2*q*qi^2*tt*uu - a2*q*tt*uu - b2*qi*tt*uu + b2*tt*uu^2 + a*qi*tt*uu - a*tt - b*q*qi*tt + b*qi^2*tt + c*q*qi*tt*uu - c*qi^2*tt*uu - c*qi*tt - c*tt*uu - qi*tt*uu^2 - qi*tt) * e3_2 + (a2^2*q*tt*uu + a2*b2*a*q^2*tt*uu - a2*b2*a*q*qi*tt*uu + a2*b2*b*tt*uu + a2*b2*c*q^2*qi*tt*uu - a2*b2*c*q*qi^2*tt*uu + a2*b2*q*tt*uu + a2*c2*q*qi*tt*uu + 2*a2*a*c*q*tt*uu - a2*a*c*qi*tt*uu - a2*a*c*tt - a2*b*q*tt*uu - a2*c^2*q*tt - a2*c*q*tt*uu^2 + a2*c*tt*uu + a2*μ*q^3*qi*tt*uu - a2*μ*q^2*qi^2*tt*uu + b2^2*b*tt*uu + b2*c2*b*qi*tt*uu + b2*c2*b*tt*uu^2 + b2*c2*c*q*tt*uu^2 - b2*c2*c*qi*tt*uu^2 - b2*a*b*q*tt + b2*a*b*qi*tt - 2*b2*a*b*tt*uu + b2*a*c*q*tt*uu - b2*a*c*qi*tt*uu - b2*a*c*tt - b2*b*c*q*qi*tt + b2*b*c*qi^2*tt + b2*b*c*tt + 2*b2*b*tt*uu^2 + b2*c^2*q*qi*tt*uu - b2*c^2*qi^2*tt*uu + b2*c*tt*uu - b2*μ*q^2*qi*tt*uu^2 + b2*μ*q*qi^2*tt*uu^2 + b2*μ*q*qi*tt*uu - b2*μ*q*tt*uu^2 + b2*μ*qi*tt*uu^2 + b2*μ*tt*uu + c2^2*a*q*tt*uu^2 + c2^2*b*q*tt*uu^2 + c2^2*c*q^2*tt*uu^2 - c2*a^2*μ*q*qi*tt^2 - c2*a^2*μ*qi*tt^2*uu - 2*c2*a^2*q*tt*uu + c2*a^2*qi*tt*uu - 2*c2*a*b*q*tt*uu - c2*a*c*μ*q*qi*tt^2*uu - 2*c2*a*c*q^2*tt*uu + c2*a*c*q*qi*tt*uu + c2*a*c*q*tt - c2*a*μ*q*qi*tt^2*uu + c2*a*q*tt*uu^2 + c2*b^2*μ*q*qi*tt^2 + 2*c2*b*c*q*tt + c2*b*μ*qi*tt^2 + c2*b*q*tt*uu^2 + c2*b*qi*tt*uu^2 + c2*c^2*q^2*tt - c2*c^2*q*tt*uu + c2*c^2*qi*tt*uu + c2*c^2*tt - c2*c*μ*qi*tt^2*uu + c2*c*q^2*tt*uu^2 + c2*c*q*tt*uu + c2*c*qi*tt*uu + c2*μ^2*q^2*qi*tt^2*uu + c2*μ^2*q*qi*tt^2*uu^2 - c2*μ*q^2*tt*uu^2 + c2*μ*q*qi*tt*uu^2 + c2*μ*q*tt*uu - c2*μ*qi^2*tt*uu^2 - c2*μ*qi*tt*uu - a*b*tt + 2*a*c*tt*uu + a*μ*q^2*tt*uu - 2*a*μ*q*qi*tt*uu - a*μ*q*tt + a*μ*qi^2*tt*uu + a*μ*qi*tt - b*c*qi*tt - b*c*tt*uu + c^2*qi*tt*uu - c^2*tt + c*μ*q^2*qi*tt*uu - c*μ*q*qi^2*tt*uu - c*tt*uu^2 + μ*q*qi^2*tt*uu - μ*q*tt*uu + μ*qi*tt*uu) * hqi + (-c2*a^2*q*qi*tt - c2*a^2*qi*tt*uu - c2*a*c*q*qi*tt*uu - c2*a*q*qi*tt*uu + c2*b^2*q*qi*tt + c2*b*qi*tt - c2*c*qi*tt*uu + c2*μ*q^2*qi*tt*uu + c2*μ*q*qi*tt*uu^2 - 1) * ht + (-a2*b2*b*tt*uu + a2*a*c*tt + a2*a*tt - b2^2*b*tt*uu - b2*c2*b*qi*tt*uu + b2*a*c*tt - b2*b^2*qi*tt - b2*b*c*qi^2*tt - b2*b*qi*tt*uu - b2*c^2*qi*tt - b2*μ*tt*uu - c2*b^2*q*qi*tt - c2*b*c*q*tt - c2*c^2*tt - c2*μ*q*tt*uu + c2*μ*qi*tt*uu + a*c*qi*tt + a*μ*q*tt - a*μ*qi*tt + b*c*qi*tt - μ*tt) * hu : (1 : K) = 0)

/-- `V2V1V2` at photon positions `(2, 0)` is not a two-photon product. -/
theorem noPair_V2V1V2_2_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 2 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u1 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e4_3 := congrFun (H (basisVec 4)) 3
  simp only [photon, wordAct, u1, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_2 e3_3 e4_3
  exact one_ne_zero (by linear_combination (-qi*tt) * e3_2 + (a*qi*tt) * e3_3 + (-a*q*qi*tt + a*qi^2*tt) * e4_3 + (-μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V2V1V2` at photon positions `(2, 1)` is not a two-photon product. -/
theorem noPair_V2V1V2_2_1 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 2 (photon q qi a2 b2 c2 1 v) = fun p => μ * wordAct q qi u1 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e2_3 := congrFun (H (basisVec 2)) 3
  have e2_4 := congrFun (H (basisVec 2)) 4
  have e3_1 := congrFun (H (basisVec 3)) 1
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e4_2 := congrFun (H (basisVec 4)) 2
  have e4_3 := congrFun (H (basisVec 4)) 3
  simp only [photon, wordAct, u1, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e2_1 e2_2 e2_3 e2_4 e3_1 e3_2 e3_3 e4_2 e4_3
  exact one_ne_zero (by linear_combination (a2*q*tt*uu + b2*q*tt*uu - c2*a^2*q*tt^2 - c2*a^2*tt^2*uu - c2*a*c*q*tt^2*uu - c2*a*q*tt^2*uu + c2*b^2*q*tt^2 + c2*b*tt^2 - c2*c*tt^2*uu + c2*μ*q^2*tt^2*uu + c2*μ*q*tt^2*uu^2 + c2*q*tt*uu^2 - c2*qi*tt*uu^2 - c2*tt*uu - 2*a*q*tt*uu + a*qi*tt*uu + a*tt + c*q*tt + c*tt*uu + q*qi*tt*uu + q*tt*uu^2) * e2_1 + (c2*tt*uu^2 - 2*a*tt*uu + c*tt + tt*uu^2) * e2_2 + (-a2*q^2*qi*tt*uu + a2*q*tt*uu + c2*qi*tt*uu^2 - a*qi*tt*uu + a*tt + b*q*qi*tt + b*qi*tt*uu - c*q*qi*tt*uu + c*qi*tt + 2*c*tt*uu + qi*tt*uu^2 + tt*uu) * e2_3 + (a2*q*qi*tt*uu - a2*qi*tt*uu^2 - b2*qi*tt*uu^2 + c2*tt*uu^2 + a*qi*tt - 2*a*tt*uu - b*qi*tt + 2*c*qi*tt*uu + c*tt + tt*uu^2) * e2_4 + (a2*a^2*q*tt^2 + a2*a^2*tt^2*uu + a2*a*c*q*tt^2*uu + a2*a*q*tt^2*uu - a2*b^2*q*tt^2 - a2*b*tt^2 + a2*c*tt^2*uu - a2*μ*q^2*tt^2*uu - a2*μ*q*tt^2*uu^2 - a2*q^2*tt*uu + a2*q*qi*tt*uu + a2*qi*tt*uu^2 + a2*tt*uu - c2*q^2*tt*uu^2 + 2*a*q^2*tt*uu - a*q*qi*tt*uu - a*q*tt + b*qi*tt - c*q^2*tt - c*q*tt*uu - q^2*tt*uu^2 - q*tt*uu) * e3_1 + (-a2*q*tt*uu - c2*q*tt*uu^2 + 2*a*q*tt*uu - a*qi*tt*uu - a*tt - c*q*tt - c*tt*uu - q*tt*uu^2 - tt*uu) * e3_2 + (-a2*q*qi*tt*uu - c2*tt*uu^2 + 2*a*tt*uu + b*qi*tt - c*qi*tt*uu - c*tt - tt*uu^2) * e3_3 + (-a2*q*qi*tt*uu + b2*qi*tt*uu^2 + a*tt*uu - c*qi*tt*uu - c*tt - tt*uu^2) * e4_2 + (a2*q^2*qi*tt*uu - a2*q*qi^2*tt*uu - a2*q*tt*uu - b2*qi*tt*uu + b2*tt*uu^2 + a*qi*tt*uu - a*tt - b*q*qi*tt + b*qi^2*tt + c*q*qi*tt*uu - c*qi^2*tt*uu - c*qi*tt - c*tt*uu - qi*tt*uu^2 - qi*tt) * e4_3 + (a2^2*q*tt*uu + a2*b2*a*q^2*tt*uu - a2*b2*a*q*qi*tt*uu + a2*b2*b*tt*uu + a2*b2*c*q^2*qi*tt*uu - a2*b2*c*q*qi^2*tt*uu + a2*b2*q*tt*uu + a2*c2*q*qi*tt*uu + 2*a2*a*c*q*tt*uu - a2*a*c*qi*tt*uu - a2*a*c*tt - a2*b*q*tt*uu - a2*c^2*q*tt - a2*c*q*tt*uu^2 + a2*c*tt*uu + a2*μ*q^3*qi*tt*uu - a2*μ*q^2*qi^2*tt*uu + b2^2*b*tt*uu + b2*c2*b*qi*tt*uu + b2*c2*b*tt*uu^2 + b2*c2*c*q*tt*uu^2 - b2*c2*c*qi*tt*uu^2 - b2*a*b*q*tt + b2*a*b*qi*tt - 2*b2*a*b*tt*uu + b2*a*c*q*tt*uu - b2*a*c*qi*tt*uu - b2*a*c*tt - b2*b*c*q*qi*tt + b2*b*c*qi^2*tt + b2*b*c*tt + 2*b2*b*tt*uu^2 + b2*c^2*q*qi*tt*uu - b2*c^2*qi^2*tt*uu + b2*c*tt*uu - b2*μ*q^2*qi*tt*uu^2 + b2*μ*q*qi^2*tt*uu^2 + b2*μ*q*qi*tt*uu - b2*μ*q*tt*uu^2 + b2*μ*qi*tt*uu^2 + b2*μ*tt*uu + c2^2*a*q*tt*uu^2 + c2^2*b*q*tt*uu^2 + c2^2*c*q^2*tt*uu^2 - c2*a^2*μ*q*qi*tt^2 - c2*a^2*μ*qi*tt^2*uu - 2*c2*a^2*q*tt*uu + c2*a^2*qi*tt*uu - 2*c2*a*b*q*tt*uu - c2*a*c*μ*q*qi*tt^2*uu - 2*c2*a*c*q^2*tt*uu + c2*a*c*q*qi*tt*uu + c2*a*c*q*tt - c2*a*μ*q*qi*tt^2*uu + c2*a*q*tt*uu^2 + c2*b^2*μ*q*qi*tt^2 + 2*c2*b*c*q*tt + c2*b*μ*qi*tt^2 + c2*b*q*tt*uu^2 + c2*b*qi*tt*uu^2 + c2*c^2*q^2*tt - c2*c^2*q*tt*uu + c2*c^2*qi*tt*uu + c2*c^2*tt - c2*c*μ*qi*tt^2*uu + c2*c*q^2*tt*uu^2 + c2*c*q*tt*uu + c2*c*qi*tt*uu + c2*μ^2*q^2*qi*tt^2*uu + c2*μ^2*q*qi*tt^2*uu^2 - c2*μ*q^2*tt*uu^2 + c2*μ*q*qi*tt*uu^2 + c2*μ*q*tt*uu - c2*μ*qi^2*tt*uu^2 - c2*μ*qi*tt*uu - a*b*tt + 2*a*c*tt*uu + a*μ*q^2*tt*uu - 2*a*μ*q*qi*tt*uu - a*μ*q*tt + a*μ*qi^2*tt*uu + a*μ*qi*tt - b*c*qi*tt - b*c*tt*uu + c^2*qi*tt*uu - c^2*tt + c*μ*q^2*qi*tt*uu - c*μ*q*qi^2*tt*uu - c*tt*uu^2 + μ*q*qi^2*tt*uu - μ*q*tt*uu + μ*qi*tt*uu) * hqi + (-c2*a^2*q*qi*tt - c2*a^2*qi*tt*uu - c2*a*c*q*qi*tt*uu - c2*a*q*qi*tt*uu + c2*b^2*q*qi*tt + c2*b*qi*tt - c2*c*qi*tt*uu + c2*μ*q^2*qi*tt*uu + c2*μ*q*qi*tt*uu^2 - 1) * ht + (-a2*b2*b*tt*uu + a2*a*c*tt + a2*a*tt - b2^2*b*tt*uu - b2*c2*b*qi*tt*uu + b2*a*c*tt - b2*b^2*qi*tt - b2*b*c*qi^2*tt - b2*b*qi*tt*uu - b2*c^2*qi*tt - b2*μ*tt*uu - c2*b^2*q*qi*tt - c2*b*c*q*tt - c2*c^2*tt - c2*μ*q*tt*uu + c2*μ*qi*tt*uu + a*c*qi*tt + a*μ*q*tt - a*μ*qi*tt + b*c*qi*tt - μ*tt) * hu : (1 : K) = 0)

/-- `V3V2V3` at photon positions `(3, 1)` is not a two-photon product. -/
theorem noPair_V3V2V3_3_1 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 1 v) = fun p => μ * wordAct q qi u2 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e4_3 := congrFun (H (basisVec 4)) 3
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u2, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e4_3 e4_4 e5_4
  exact one_ne_zero (by linear_combination (-qi*tt) * e4_3 + (a*qi*tt) * e4_4 + (-a*q*qi*tt + a*qi^2*tt) * e5_4 + (-μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V2V3` at photon positions `(3, 2)` is not a two-photon product. -/
theorem noPair_V3V2V3_3_2 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 2 v) = fun p => μ * wordAct q qi u2 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  have e3_5 := congrFun (H (basisVec 3)) 5
  have e4_2 := congrFun (H (basisVec 4)) 2
  have e4_3 := congrFun (H (basisVec 4)) 3
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_3 := congrFun (H (basisVec 5)) 3
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u2, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_2 e3_3 e3_4 e3_5 e4_2 e4_3 e4_4 e5_3 e5_4
  exact one_ne_zero (by linear_combination (a2*q*tt*uu + b2*q*tt*uu - c2*a^2*q*tt^2 - c2*a^2*tt^2*uu - c2*a*c*q*tt^2*uu - c2*a*q*tt^2*uu + c2*b^2*q*tt^2 + c2*b*tt^2 - c2*c*tt^2*uu + c2*μ*q^2*tt^2*uu + c2*μ*q*tt^2*uu^2 + c2*q*tt*uu^2 - c2*qi*tt*uu^2 - c2*tt*uu - 2*a*q*tt*uu + a*qi*tt*uu + a*tt + c*q*tt + c*tt*uu + q*qi*tt*uu + q*tt*uu^2) * e3_2 + (c2*tt*uu^2 - 2*a*tt*uu + c*tt + tt*uu^2) * e3_3 + (-a2*q^2*qi*tt*uu + a2*q*tt*uu + c2*qi*tt*uu^2 - a*qi*tt*uu + a*tt + b*q*qi*tt + b*qi*tt*uu - c*q*qi*tt*uu + c*qi*tt + 2*c*tt*uu + qi*tt*uu^2 + tt*uu) * e3_4 + (a2*q*qi*tt*uu - a2*qi*tt*uu^2 - b2*qi*tt*uu^2 + c2*tt*uu^2 + a*qi*tt - 2*a*tt*uu - b*qi*tt + 2*c*qi*tt*uu + c*tt + tt*uu^2) * e3_5 + (a2*a^2*q*tt^2 + a2*a^2*tt^2*uu + a2*a*c*q*tt^2*uu + a2*a*q*tt^2*uu - a2*b^2*q*tt^2 - a2*b*tt^2 + a2*c*tt^2*uu - a2*μ*q^2*tt^2*uu - a2*μ*q*tt^2*uu^2 - a2*q^2*tt*uu + a2*q*qi*tt*uu + a2*qi*tt*uu^2 + a2*tt*uu - c2*q^2*tt*uu^2 + 2*a*q^2*tt*uu - a*q*qi*tt*uu - a*q*tt + b*qi*tt - c*q^2*tt - c*q*tt*uu - q^2*tt*uu^2 - q*tt*uu) * e4_2 + (-a2*q*tt*uu - c2*q*tt*uu^2 + 2*a*q*tt*uu - a*qi*tt*uu - a*tt - c*q*tt - c*tt*uu - q*tt*uu^2 - tt*uu) * e4_3 + (-a2*q*qi*tt*uu - c2*tt*uu^2 + 2*a*tt*uu + b*qi*tt - c*qi*tt*uu - c*tt - tt*uu^2) * e4_4 + (-a2*q*qi*tt*uu + b2*qi*tt*uu^2 + a*tt*uu - c*qi*tt*uu - c*tt - tt*uu^2) * e5_3 + (a2*q^2*qi*tt*uu - a2*q*qi^2*tt*uu - a2*q*tt*uu - b2*qi*tt*uu + b2*tt*uu^2 + a*qi*tt*uu - a*tt - b*q*qi*tt + b*qi^2*tt + c*q*qi*tt*uu - c*qi^2*tt*uu - c*qi*tt - c*tt*uu - qi*tt*uu^2 - qi*tt) * e5_4 + (a2^2*q*tt*uu + a2*b2*a*q^2*tt*uu - a2*b2*a*q*qi*tt*uu + a2*b2*b*tt*uu + a2*b2*c*q^2*qi*tt*uu - a2*b2*c*q*qi^2*tt*uu + a2*b2*q*tt*uu + a2*c2*q*qi*tt*uu + 2*a2*a*c*q*tt*uu - a2*a*c*qi*tt*uu - a2*a*c*tt - a2*b*q*tt*uu - a2*c^2*q*tt - a2*c*q*tt*uu^2 + a2*c*tt*uu + a2*μ*q^3*qi*tt*uu - a2*μ*q^2*qi^2*tt*uu + b2^2*b*tt*uu + b2*c2*b*qi*tt*uu + b2*c2*b*tt*uu^2 + b2*c2*c*q*tt*uu^2 - b2*c2*c*qi*tt*uu^2 - b2*a*b*q*tt + b2*a*b*qi*tt - 2*b2*a*b*tt*uu + b2*a*c*q*tt*uu - b2*a*c*qi*tt*uu - b2*a*c*tt - b2*b*c*q*qi*tt + b2*b*c*qi^2*tt + b2*b*c*tt + 2*b2*b*tt*uu^2 + b2*c^2*q*qi*tt*uu - b2*c^2*qi^2*tt*uu + b2*c*tt*uu - b2*μ*q^2*qi*tt*uu^2 + b2*μ*q*qi^2*tt*uu^2 + b2*μ*q*qi*tt*uu - b2*μ*q*tt*uu^2 + b2*μ*qi*tt*uu^2 + b2*μ*tt*uu + c2^2*a*q*tt*uu^2 + c2^2*b*q*tt*uu^2 + c2^2*c*q^2*tt*uu^2 - c2*a^2*μ*q*qi*tt^2 - c2*a^2*μ*qi*tt^2*uu - 2*c2*a^2*q*tt*uu + c2*a^2*qi*tt*uu - 2*c2*a*b*q*tt*uu - c2*a*c*μ*q*qi*tt^2*uu - 2*c2*a*c*q^2*tt*uu + c2*a*c*q*qi*tt*uu + c2*a*c*q*tt - c2*a*μ*q*qi*tt^2*uu + c2*a*q*tt*uu^2 + c2*b^2*μ*q*qi*tt^2 + 2*c2*b*c*q*tt + c2*b*μ*qi*tt^2 + c2*b*q*tt*uu^2 + c2*b*qi*tt*uu^2 + c2*c^2*q^2*tt - c2*c^2*q*tt*uu + c2*c^2*qi*tt*uu + c2*c^2*tt - c2*c*μ*qi*tt^2*uu + c2*c*q^2*tt*uu^2 + c2*c*q*tt*uu + c2*c*qi*tt*uu + c2*μ^2*q^2*qi*tt^2*uu + c2*μ^2*q*qi*tt^2*uu^2 - c2*μ*q^2*tt*uu^2 + c2*μ*q*qi*tt*uu^2 + c2*μ*q*tt*uu - c2*μ*qi^2*tt*uu^2 - c2*μ*qi*tt*uu - a*b*tt + 2*a*c*tt*uu + a*μ*q^2*tt*uu - 2*a*μ*q*qi*tt*uu - a*μ*q*tt + a*μ*qi^2*tt*uu + a*μ*qi*tt - b*c*qi*tt - b*c*tt*uu + c^2*qi*tt*uu - c^2*tt + c*μ*q^2*qi*tt*uu - c*μ*q*qi^2*tt*uu - c*tt*uu^2 + μ*q*qi^2*tt*uu - μ*q*tt*uu + μ*qi*tt*uu) * hqi + (-c2*a^2*q*qi*tt - c2*a^2*qi*tt*uu - c2*a*c*q*qi*tt*uu - c2*a*q*qi*tt*uu + c2*b^2*q*qi*tt + c2*b*qi*tt - c2*c*qi*tt*uu + c2*μ*q^2*qi*tt*uu + c2*μ*q*qi*tt*uu^2 - 1) * ht + (-a2*b2*b*tt*uu + a2*a*c*tt + a2*a*tt - b2^2*b*tt*uu - b2*c2*b*qi*tt*uu + b2*a*c*tt - b2*b^2*qi*tt - b2*b*c*qi^2*tt - b2*b*qi*tt*uu - b2*c^2*qi*tt - b2*μ*tt*uu - c2*b^2*q*qi*tt - c2*b*c*q*tt - c2*c^2*tt - c2*μ*q*tt*uu + c2*μ*qi*tt*uu + a*c*qi*tt + a*μ*q*tt - a*μ*qi*tt + b*c*qi*tt - μ*tt) * hu : (1 : K) = 0)

/-- `V0V1V2V1V2` at photon positions `(0, 2)` is not a two-photon product. -/
theorem noPair_V0V1V2V1V2_0_2 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 2 v) = fun p => μ * wordAct q qi u3 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e3_0 := congrFun (H (basisVec 3)) 0
  have e3_1 := congrFun (H (basisVec 3)) 1
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e4_0 := congrFun (H (basisVec 4)) 0
  have e4_1 := congrFun (H (basisVec 4)) 1
  have e4_2 := congrFun (H (basisVec 4)) 2
  simp only [photon, wordAct, u3, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e2_2 e3_0 e3_1 e3_2 e4_0 e4_1 e4_2
  exact one_ne_zero (by linear_combination (a*q*tt + c*tt + q*qi*tt) * e1_1 + (-q^2*tt) * e2_0 + (-a*q^2*tt + a*q*qi*tt - c*q*tt + c*qi*tt - q^2*qi*tt + q*qi^2*tt) * e2_1 + (-tt) * e2_2 + (-q^4*qi*tt + q^3*qi^2*tt + q^3*tt - q^2*qi*tt - q*tt) * e3_0 + (-a*q^2*qi*tt + a*q*qi^2*tt - c*q*qi*tt + c*qi^2*tt - q^2*qi^2*tt + q*qi^3*tt) * e3_1 + (-q^2*qi*tt + q*tt - qi*tt) * e3_2 + (-q^3*qi*tt + q^2*qi^2*tt + q^2*tt - q*qi*tt - tt) * e4_0 + (-a*q^2*qi^2*tt + a*q*qi^3*tt - c*q*qi^2*tt + c*qi^3*tt - q^2*qi^3*tt + q*qi^4*tt) * e4_1 + (-q*qi*tt - qi^2*tt + tt) * e4_2 + (a2*a*q^2*tt + b2*c*q*tt - b2*q*tt + c2*a*q*tt - c2*c*tt - c2*q*qi*tt + c2*tt + c*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt - tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V0V1V2V1V2` at photon positions `(0, 3)` is not a two-photon product. -/
theorem noPair_V0V1V2V1V2_0_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u3 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  simp only [photon, wordAct, u3, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e2_2
  exact one_ne_zero (by linear_combination (a*q*tt + c*tt + tt) * e1_1 + (-q^2*tt) * e2_0 + (-a*q^2*tt + a*q*qi*tt - c*q*tt + c*qi*tt - q*tt + qi*tt) * e2_1 + (-tt) * e2_2 + (a2*c*q*tt + b2*c*q*tt + c2*c*q*qi*tt + c*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V0V1V2V1V2` at photon positions `(2, 0)` is not a two-photon product. -/
theorem noPair_V0V1V2V1V2_2_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 2 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u3 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e1_3 := congrFun (H (basisVec 1)) 3
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e4_2 := congrFun (H (basisVec 4)) 2
  simp only [photon, wordAct, u3, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e1_3 e2_0 e2_1 e2_2 e3_2 e4_2
  exact one_ne_zero (by linear_combination (a2*q*tt + c2*tt + tt) * e1_1 + (tt) * e1_3 + (-q^2*tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt - q^2*qi*tt + qi*tt) * e2_1 + (-tt) * e2_2 + (-qi*tt) * e3_2 + (-qi^2*tt) * e4_2 + (b2*a*q^2*tt + b2*a*tt + b2*b*q^2*tt + b2*c*q^2*qi*tt + b2*c*qi*tt + b2*q*tt + 2*c2*a*q*tt + c2*b*q*tt + 2*c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V0V1V2V1V2` at photon positions `(3, 0)` is not a two-photon product. -/
theorem noPair_V0V1V2V1V2_3_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u3 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e2_2 := congrFun (H (basisVec 2)) 2
  simp only [photon, wordAct, u3, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e2_2
  exact one_ne_zero (by linear_combination (a2*q*tt + c2*tt + tt) * e1_1 + (-q^2*tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt - q*tt + qi*tt) * e2_1 + (-tt) * e2_2 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V0V3V1V2V3` at photon positions `(0, 3)` is not a two-photon product. -/
theorem noPair_V0V3V1V2V3_0_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u4 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u4, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_3 e3_4 e4_4 e5_4
  exact one_ne_zero (by linear_combination (-tt) * e3_3 + (-qi*tt) * e3_4 + (a2*q*tt + c2*tt + tt) * e4_4 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt + qi*tt) * e5_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V0V3V1V2V3` at photon positions `(3, 0)` is not a two-photon product. -/
theorem noPair_V0V3V1V2V3_3_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u4 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  simp only [photon, wordAct, u4, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e3_3 e3_4
  exact one_ne_zero (by linear_combination (a2*q*tt + tt) * e1_1 + (tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt + qi*tt) * e2_1 + (-tt) * e3_3 + (-qi*tt) * e3_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V1V2V3V2V3` at photon positions `(1, 3)` is not a two-photon product. -/
theorem noPair_V1V2V3V2V3_1_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 1 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u5 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e3_1 := congrFun (H (basisVec 3)) 1
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e4_1 := congrFun (H (basisVec 4)) 1
  have e4_2 := congrFun (H (basisVec 4)) 2
  have e4_3 := congrFun (H (basisVec 4)) 3
  have e5_1 := congrFun (H (basisVec 5)) 1
  have e5_2 := congrFun (H (basisVec 5)) 2
  have e5_3 := congrFun (H (basisVec 5)) 3
  simp only [photon, wordAct, u5, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e2_2 e3_1 e3_2 e3_3 e4_1 e4_2 e4_3 e5_1 e5_2 e5_3
  exact one_ne_zero (by linear_combination (a*q*tt + c*tt + q*qi*tt) * e2_2 + (-q^2*tt) * e3_1 + (-a*q^2*tt + a*q*qi*tt - c*q*tt + c*qi*tt - q^2*qi*tt + q*qi^2*tt) * e3_2 + (-tt) * e3_3 + (-q^4*qi*tt + q^3*qi^2*tt + q^3*tt - q^2*qi*tt - q*tt) * e4_1 + (-a*q^2*qi*tt + a*q*qi^2*tt - c*q*qi*tt + c*qi^2*tt - q^2*qi^2*tt + q*qi^3*tt) * e4_2 + (-q^2*qi*tt + q*tt - qi*tt) * e4_3 + (-q^3*qi*tt + q^2*qi^2*tt + q^2*tt - q*qi*tt - tt) * e5_1 + (-a*q^2*qi^2*tt + a*q*qi^3*tt - c*q*qi^2*tt + c*qi^3*tt - q^2*qi^3*tt + q*qi^4*tt) * e5_2 + (-q*qi*tt - qi^2*tt + tt) * e5_3 + (a2*a*q^2*tt + b2*c*q*tt - b2*q*tt + c2*a*q*tt - c2*c*tt - c2*q*qi*tt + c2*tt + c*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt - tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V1V2V3V2V3` at photon positions `(3, 1)` is not a two-photon product. -/
theorem noPair_V1V2V3V2V3_3_1 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 1 v) = fun p => μ * wordAct q qi u5 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e2_2 := congrFun (H (basisVec 2)) 2
  have e2_4 := congrFun (H (basisVec 2)) 4
  have e3_1 := congrFun (H (basisVec 3)) 1
  have e3_2 := congrFun (H (basisVec 3)) 2
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e4_3 := congrFun (H (basisVec 4)) 3
  have e5_3 := congrFun (H (basisVec 5)) 3
  simp only [photon, wordAct, u5, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e2_2 e2_4 e3_1 e3_2 e3_3 e4_3 e5_3
  exact one_ne_zero (by linear_combination (a2*q*tt + c2*tt + tt) * e2_2 + (tt) * e2_4 + (-q^2*tt) * e3_1 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt - q^2*qi*tt + qi*tt) * e3_2 + (-tt) * e3_3 + (-qi*tt) * e4_3 + (-qi^2*tt) * e5_3 + (b2*a*q^2*tt + b2*a*tt + b2*b*q^2*tt + b2*c*q^2*qi*tt + b2*c*qi*tt + b2*q*tt + 2*c2*a*q*tt + c2*b*q*tt + 2*c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V0V1V2V3` at photon positions `(0, 3)` is not a two-photon product. -/
theorem noPair_V3V0V1V2V3_0_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u6 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u6, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_3 e3_4 e4_4 e5_4
  exact one_ne_zero (by linear_combination (-tt) * e3_3 + (-qi*tt) * e3_4 + (a2*q*tt + c2*tt + tt) * e4_4 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt + qi*tt) * e5_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V0V1V2V3` at photon positions `(3, 0)` is not a two-photon product. -/
theorem noPair_V3V0V1V2V3_3_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u6 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  simp only [photon, wordAct, u6, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e3_3 e3_4
  exact one_ne_zero (by linear_combination (a2*q*tt + tt) * e1_1 + (tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt + qi*tt) * e2_1 + (-tt) * e3_3 + (-qi*tt) * e3_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V2V0V3V1` at photon positions `(0, 3)` is not a two-photon product. -/
theorem noPair_V3V2V0V3V1_0_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u7 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u7, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_3 e3_4 e4_4 e5_4
  exact one_ne_zero (by linear_combination (-tt) * e3_3 + (-qi*tt) * e3_4 + (a2*q*tt + c2*tt + tt) * e4_4 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt + qi*tt) * e5_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V2V0V3V1` at photon positions `(3, 0)` is not a two-photon product. -/
theorem noPair_V3V2V0V3V1_3_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u7 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  simp only [photon, wordAct, u7, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e3_3 e3_4
  exact one_ne_zero (by linear_combination (a2*q*tt + tt) * e1_1 + (tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt + qi*tt) * e2_1 + (-tt) * e3_3 + (-qi*tt) * e3_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V2V3V0V1` at photon positions `(0, 3)` is not a two-photon product. -/
theorem noPair_V3V2V3V0V1_0_3 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 0 (photon q qi a2 b2 c2 3 v) = fun p => μ * wordAct q qi u8 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  have e4_4 := congrFun (H (basisVec 4)) 4
  have e5_4 := congrFun (H (basisVec 5)) 4
  simp only [photon, wordAct, u8, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e3_3 e3_4 e4_4 e5_4
  exact one_ne_zero (by linear_combination (-tt) * e3_3 + (-qi*tt) * e3_4 + (a2*q*tt + c2*tt + tt) * e4_4 + (-a2*q^2*tt + a2*q*qi*tt - c2*q*tt + c2*qi*tt + qi*tt) * e5_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

/-- `V3V2V3V0V1` at photon positions `(3, 0)` is not a two-photon product. -/
theorem noPair_V3V2V3V0V1_3_0 (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c 3 (photon q qi a2 b2 c2 0 v) = fun p => μ * wordAct q qi u8 v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
  have e1_1 := congrFun (H (basisVec 1)) 1
  have e2_0 := congrFun (H (basisVec 2)) 0
  have e2_1 := congrFun (H (basisVec 2)) 1
  have e3_3 := congrFun (H (basisVec 3)) 3
  have e3_4 := congrFun (H (basisVec 3)) 4
  simp only [photon, wordAct, u8, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at e1_1 e2_0 e2_1 e3_3 e3_4
  exact one_ne_zero (by linear_combination (a2*q*tt + tt) * e1_1 + (tt) * e2_0 + (-a2*q^2*tt + a2*q*qi*tt + qi*tt) * e2_1 + (-tt) * e3_3 + (-qi*tt) * e3_4 + (c2*a*q*tt + c2*b*q*tt + c2*c*q*qi*tt + c2*tt - μ*q^2*qi^2*tt - μ*q*qi*tt - μ*tt) * hqi + (-1) * ht : (1 : K) = 0)

end QOU.MassTheory.PhotonPairNoFactorSector
