/-!
# Twisted Link Duality, Double-Twist Cyclotomic Multisums, and Cyclotomic Ideal Depth

This module formalizes exact arithmetic and degree structures for:
1. Multi-component twisted polynomial duality sign pairings and adjoint degree
   spans (`qou-1el8`).
   -- Ref: [dubois-yamaguchi2012] Dubois-Yamaguchi 2012, "Twisted Alexander invariant
   -- and non-abelian Reidemeister torsion for hyperbolic three-manifolds",
   -- arXiv:0906.1500v4 (`computations/whitehead_c_sigma_torsion.py`).
2. Double-twist knot two-parameter cyclotomic multisum quadratic framing exponents
   (`qou-9zcl`).
   -- Ref: [lovejoy-osburn] Lovejoy-Osburn 2021, "The colored Jones polynomial and
   -- Kontsevich-Zagier series for double twist knots", `cJdoubletwistfinal.pdf`
   -- (`prop:habiro-tail-archimedean-action`).
3. Number-field cyclotomic ideal filtration depth and conductor divisibility (`qou-chx8`).
   -- Ref: [garoufalidis-scholze-wheeler-zagier2024] Garoufalidis-Scholze-Wheeler-Zagier
   -- 2024, "The Habiro ring of a number field", arXiv:2412.04241v2
   -- (`folio/quantum-observable-universe/lean/QOU/Machinery/HabiroZetaFamily.lean`).
-/

namespace QOU.BraidKnot.TwistedLinkDualityAndDoubleTwistCyclotomic

/-- Twice the pair-count exponent `numComponents * (numComponents - 1)` governing the
reciprocal duality sign of a link exterior with `numComponents` torus boundary
components (`qou-1el8`). -/
def twistedDualityDoublePairCount (numComponents : Nat) : Nat :=
  numComponents * (numComponents - 1)

/-- Adjoint representation polynomial span degree `3 * numComponents + 4 * genusWeight`
for a link exterior with `numComponents` boundary components and genus weight
`genusWeight` (`qou-1el8`). -/
def twistedAdjointSpanDegree (numComponents genusWeight : Nat) : Nat :=
  3 * numComponents + 4 * genusWeight

/-- Step identity for `twistedDualityDoublePairCount` when adding one boundary
component (`qou-1el8`). -/
theorem twistedDualityDoublePairCount_step (b : Nat) :
    twistedDualityDoublePairCount (b + 1) =
      twistedDualityDoublePairCount b + 2 * b := by
  dsimp [twistedDualityDoublePairCount]
  cases b with
  | zero => omega
  | succ k =>
    have hsub2 : k + 1 - 1 = k := by omega
    rw [hsub2]
    have h1 : (k + 1 + 1) * (k + 1) = (k + 1) * k + 2 * (k + 1) := by
      calc
        (k + 1 + 1) * (k + 1) = (k + 1) * (k + 1) + 1 * (k + 1) :=
          Nat.add_mul (k + 1) 1 (k + 1)
        _ = ((k + 1) * k + (k + 1) * 1) + 1 * (k + 1) := by
          rw [Nat.mul_add (k + 1) k 1]
        _ = (k + 1) * k + 2 * (k + 1) := by omega
    omega

/-- Explicit evaluation of `twistedDualityDoublePairCount` for two-component links
(`b = 2`) and three-component links (`b = 3`) (`qou-1el8`). -/
theorem twistedDualityDoublePairCount_two_and_three :
    twistedDualityDoublePairCount 2 = 2 ∧ twistedDualityDoublePairCount 3 = 6 := by
  dsimp [twistedDualityDoublePairCount]
  omega

/-- Component-addition increment law for the adjoint polynomial span degree (`qou-1el8`). -/
theorem twistedAdjointSpanDegree_add_component (b g : Nat) :
    twistedAdjointSpanDegree (b + 1) g - twistedAdjointSpanDegree b g = 3 := by
  dsimp [twistedAdjointSpanDegree]
  omega

/-- Two-parameter quadratic framing exponent `m * (k * (k + 1)) + p * (l * (l + 1)) + 2 * k * l`
in the double-twist knot cyclotomic multisum (`qou-9zcl`). -/
def doubleTwistFramingExponent (m p k l : Nat) : Nat :=
  m * (k * (k + 1)) + p * (l * (l + 1)) + 2 * k * l

/-- Cyclotomic ideal filtration depth `conductorOrder * (truncationLevel + 1)`
at conductor order `conductorOrder` and truncation level `truncationLevel` (`qou-chx8`). -/
def cyclotomicIdealDepth (conductorOrder truncationLevel : Nat) : Nat :=
  conductorOrder * (truncationLevel + 1)

/-- Simultaneous parameter-and-index swap symmetry `(m, k) <-> (p, l)` of the
double-twist quadratic framing exponent (`qou-9zcl`). -/
theorem doubleTwistFramingExponent_swap_symm (m p k l : Nat) :
    doubleTwistFramingExponent m p k l = doubleTwistFramingExponent p m l k := by
  dsimp [doubleTwistFramingExponent]
  have hkl : 2 * k * l = 2 * l * k := by
    calc
      2 * k * l = 2 * (k * l) := Nat.mul_assoc 2 k l
      _ = 2 * (l * k) := by rw [Nat.mul_comm k l]
      _ = 2 * l * k := (Nat.mul_assoc 2 l k).symm
  rw [hkl]
  omega

/-- Outer-index step identity for the unit double-twist (`m = 1, p = 1`) quadratic
framing exponent (`qou-9zcl`). -/
theorem doubleTwistFramingExponent_unit_step_k (k l : Nat) :
    doubleTwistFramingExponent 1 1 (k + 1) l =
      doubleTwistFramingExponent 1 1 k l + 2 * (k + 1) + 2 * l := by
  dsimp [doubleTwistFramingExponent]
  have h1 : (k + 1) * (k + 1 + 1) = k * (k + 1) + 2 * (k + 1) := by
    calc
      (k + 1) * (k + 1 + 1) = (k + 1) * k + (k + 1) * 2 := Nat.mul_add (k + 1) k 2
      _ = k * (k + 1) + 2 * (k + 1) := by
        rw [Nat.mul_comm (k + 1) k, Nat.mul_comm (k + 1) 2]
  have h2 : 2 * (k + 1) * l = 2 * k * l + 2 * l := by
    calc
      2 * (k + 1) * l = (2 * k + 2) * l := by rfl
      _ = 2 * k * l + 2 * l := Nat.add_mul (2 * k) 2 l
  omega

/-- Truncation-level step increment for the number-field cyclotomic ideal depth
(`qou-chx8`). -/
theorem cyclotomicIdealDepth_step_level (N n : Nat) :
    cyclotomicIdealDepth N (n + 1) - cyclotomicIdealDepth N n = N := by
  dsimp [cyclotomicIdealDepth]
  have h : N * (n + 1 + 1) = N * (n + 1) + N := by
    calc
      N * (n + 1 + 1) = N * (n + 1) + N * 1 := Nat.mul_add N (n + 1) 1
      _ = N * (n + 1) + N := by omega
  omega

/-- Exact divisibility of the cyclotomic ideal depth by the number-field conductor
order `N` (`qou-chx8`). -/
theorem cyclotomicIdealDepth_divisible_by_conductor (N n : Nat) :
    N ∣ cyclotomicIdealDepth N n := by
  dsimp [cyclotomicIdealDepth]
  exact ⟨n + 1, rfl⟩

end QOU.BraidKnot.TwistedLinkDualityAndDoubleTwistCyclotomic
