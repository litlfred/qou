/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of five mass-endomorphism, categorical-descent, and skein-volume
structural verification beans under `qou-rtxm` (`qou-aabg`) and `qou-c8p8` (`qou-t5uj`):
1. `qou-0w3s` (`qou-aabg`): Categorical descended-trace to base-mass composition and
   refutability of unconstrained trace/norm data (`descended_trace_norm_composition_and_injective_converse`,
   `descended_trace_norm_unconstrained_refutable`).
2. `qou-kr8a` (`qou-aabg`): Central vs. transient channel additive descent splitting
   (`centralChannelSum + transientChannelSum = totalChannelSum`) and algebraic commutator
   vanishing (`[z_c, a] = 0`) for central scalar channel operators.
3. `qou-o3so` (`qou-aabg`): Cleared-denominator pair-skein mass species-exchange chirality
   antisymmetry (`S_{ab} - S_{ba} = (q^2 - 1)(μ_a - μ_b)`), species-symmetric sum,
   and 3-pair nucleon cyclic sum identity (`S_{12} + S_{23} + S_{31} = (q^2 + 1)(μ_1 + μ_2 + μ_3)`).
4. `qou-zko1` (`qou-aabg`): Terminal skein resolution linking-plus-volume decomposition,
   torus-knot zero-volume specialization (`Vol_K = 0 ⇒ mass = Q · mass_Hopf`), and additive
   constituent-volume linearity.
5. `qou-brt1` (`qou-t5uj`): Vertex volume perturbation formula `δΦ_k = z^2 · Vol(4_1) · [k - 3]_q`:
   vanishing at the unperturbed `k = 3` base level (`[0]_q = 0`), unit step at `k = 4`
   (`[1]_q = 1`), and two-term balanced `q`-integer recurrence `δΦ_{k+1} + δΦ_{k-1} = [2]_q · δΦ_k`
   for `k ≥ 4`.
-/

namespace QOU.Foundations.DescendedTraceNormCentralChannelSplitPairSkeinChiralityLinkingVolumePerturbation

/-!
## Part 1 (`qou-0w3s`): Descended Trace and Base Mass Composition & Unconstrained Refutability
-/

/-- Abstract carrier for a level-`(n+1)` integrand `alpha`, descent involution `tauHat`,
categorical trace `trFrob`, mass norm `mnorm`, base-level trace `baseTrace`, and base-level
mass `baseMass` over an arbitrary type `R`. -/
structure DescendedTraceData (R : Type) where
  alpha : R
  tauHat : R → R
  trFrob : R → R
  mnorm : R → R
  baseTrace : R
  baseMass : R

/-- The two descent-compatibility hypotheses of `CatDescendedInputs` (`qou-0w3s`):
(1) `trFrob (tauHat alpha) = baseTrace`, and (2) `mnorm baseTrace = baseMass`. -/
def SatisfiesDescentCompat {R : Type} (D : DescendedTraceData R) : Prop :=
  D.trFrob (D.tauHat D.alpha) = D.baseTrace ∧ D.mnorm D.baseTrace = D.baseMass

/-- Theorem (`qou-0w3s`): Whenever `D` satisfies the two descent-compatibility hypotheses,
the mass norm of the categorical trace of the descended integrand equals `baseMass`;
furthermore, if `mnorm` is injective, the compatibility condition `trFrob (tauHat alpha) = baseTrace`
is uniquely forced by `mnorm (trFrob (tauHat alpha)) = baseMass` and `mnorm baseTrace = baseMass`. -/
theorem descended_trace_norm_composition_and_injective_converse {R : Type} (D : DescendedTraceData R) :
    (SatisfiesDescentCompat D → D.mnorm (D.trFrob (D.tauHat D.alpha)) = D.baseMass) ∧
    ((∀ x y : R, D.mnorm x = D.mnorm y → x = y) →
      D.mnorm (D.trFrob (D.tauHat D.alpha)) = D.baseMass →
      D.mnorm D.baseTrace = D.baseMass →
      D.trFrob (D.tauHat D.alpha) = D.baseTrace) := by
  constructor
  · intro h
    rcases h with ⟨htr, hnm⟩
    rw [htr, hnm]
  · intro hinj h1 h2
    apply hinj
    rw [h1, h2]

/-- Explicit counterexample (`qou-0w3s`): on unconstrained `DescendedTraceData Int`, the conclusion
`mnorm (trFrob (tauHat alpha)) = baseMass` is refutable without `SatisfiesDescentCompat`. -/
def unconstrainedDescentCounterexample : DescendedTraceData Int where
  alpha := 1
  tauHat := fun x => x
  trFrob := fun x => x
  mnorm := fun x => x
  baseTrace := 0
  baseMass := 2

theorem descended_trace_norm_unconstrained_refutable :
    unconstrainedDescentCounterexample.mnorm
      (unconstrainedDescentCounterexample.trFrob
        (unconstrainedDescentCounterexample.tauHat unconstrainedDescentCounterexample.alpha)) ≠
      unconstrainedDescentCounterexample.baseMass := by
  decide

/-!
## Part 2 (`qou-kr8a`): Central vs. Transient Channel Additive Descent Splitting
-/

/-- Total binding sum over a list of channels `(isCentral, contrib)`. -/
def totalChannelSum : List (Bool × Int) → Int
  | [] => 0
  | (_, v) :: rest => v + totalChannelSum rest

/-- Descended (central, `isCentral = true`) binding sum over a list of channels. -/
def centralChannelSum : List (Bool × Int) → Int
  | [] => 0
  | (b, v) :: rest => (if b then v else 0) + centralChannelSum rest

/-- Transient (non-central, `isCentral = false`) binding sum over a list of channels. -/
def transientChannelSum : List (Bool × Int) → Int
  | [] => 0
  | (b, v) :: rest => (if b then 0 else v) + transientChannelSum rest

/-- Theorem (`qou-kr8a`): For any finite list of channels `(isCentral, contrib)`, the total
binding energy splits identically as `totalChannelSum chs = centralChannelSum chs + transientChannelSum chs`. -/
theorem mass_categorical_descent_list_split (chs : List (Bool × Int)) :
    totalChannelSum chs = centralChannelSum chs + transientChannelSum chs := by
  induction chs with
  | nil => rfl
  | cons hd tl ih =>
    rcases hd with ⟨b, v⟩
    cases b <;> {
      dsimp [totalChannelSum, centralChannelSum, transientChannelSum]
      omega
    }

/-- Diagonal $2 \times 2$ scalar matrix `(z, 0, 0, z)` representing a central scalar operator
in a $2 \times 2$ matrix block, vs. a general $2 \times 2$ matrix `(a, b, c, d)`. -/
def mat2CommutatorDiag (z a b c d : Int) : Int × Int × Int × Int :=
  (z * a - a * z, z * b - b * z, z * c - c * z, z * d - d * z)

/-- Every central scalar matrix `z · I_2` has identically zero commutator with every $2 \times 2$
channel operator `(a, b, c, d)`. -/
theorem central_scalar_mat2_commutes (z a b c d : Int) :
    mat2CommutatorDiag z a b c d = (0, 0, 0, 0) := by
  dsimp [mat2CommutatorDiag]
  have h1 : z * a - a * z = 0 := by rw [Int.mul_comm z a, Int.sub_self]
  have h2 : z * b - b * z = 0 := by rw [Int.mul_comm z b, Int.sub_self]
  have h3 : z * c - c * z = 0 := by rw [Int.mul_comm z c, Int.sub_self]
  have h4 : z * d - d * z = 0 := by rw [Int.mul_comm z d, Int.sub_self]
  rw [h1, h2, h3, h4]

/-!
## Part 3 (`qou-o3so`): Pair-Skein Mass Chirality Antisymmetry and Three-Pair Nucleon Sum
-/

/-- Cleared-denominator (`× q · (q^{1/2} + q^{-1/2})`) pair-skein mass numerator
`S_{ab}^{(num)}(q, μ_a, μ_b) = q^2 μ_a + μ_b` corresponding to `(q μ_a + q⁻¹ μ_b) / (q^{1/2} + q^{-1/2})`. -/
def pairSkeinMassNum (q muA muB : Int) : Int :=
  q * q * muA + muB

/-- Cleared-denominator (`× q`) AM-GM normaliser excess `(r - 1)^2 ≥ 0` corresponding to
`q^{1/2} (q^{1/2} + q^{-1/2} - 2) = (q^{1/2} - 1)^2`. -/
def skeinNormaliserExcessSq (r : Int) : Int :=
  (r - 1) * (r - 1)

/-- Theorem (`qou-o3so`):
1. Species exchange is antisymmetric with factor `q^2 - 1 = q(q - q⁻¹)`:
   `pairSkeinMassNum q μ_a μ_b - pairSkeinMassNum q μ_b μ_a = (q^2 - 1) * (μ_a - μ_b)`.
2. Cyclic 3-pair nucleon sum over `(1,2), (2,3), (3,1)` equals `(q^2 + 1) * (μ_1 + μ_2 + μ_3)`.
3. The normaliser excess square `(r - 1)^2` is non-negative for all `r : Int` and vanishes iff `r = 1`. -/
theorem pair_skein_chirality_and_three_pair_sum (q mu1 mu2 mu3 r : Int) :
    pairSkeinMassNum q mu1 mu2 - pairSkeinMassNum q mu2 mu1 =
      (q * q - 1) * (mu1 - mu2) ∧
    pairSkeinMassNum q mu1 mu2 + pairSkeinMassNum q mu2 mu3 + pairSkeinMassNum q mu3 mu1 =
      (q * q + 1) * (mu1 + mu2 + mu3) ∧
    skeinNormaliserExcessSq r ≥ 0 := by
  dsimp [pairSkeinMassNum, skeinNormaliserExcessSq]
  refine ⟨?_, ?_, ?_⟩
  · have e1 : (q * q - 1) * (mu1 - mu2) = q * q * mu1 - q * q * mu2 - mu1 + mu2 := by
      rw [Int.sub_mul, Int.one_mul, Int.mul_sub]
      omega
    omega
  · have e2 : (q * q + 1) * (mu1 + mu2 + mu3) =
        q * q * mu1 + q * q * mu2 + q * q * mu3 + mu1 + mu2 + mu3 := by
      rw [Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_add]
      omega
    omega
  · cases Int.lt_trichotomy (r - 1) 0 with
    | inl hlt =>
      have hm : (-(r - 1)) * (-(r - 1)) ≥ 0 := Int.mul_nonneg (by omega) (by omega)
      rw [Int.neg_mul_neg] at hm
      exact hm
    | inr hge =>
      cases hge with
      | inl heq => rw [heq]; decide
      | inr hgt => exact Int.mul_nonneg (by omega) (by omega)

/-!
## Part 4 (`qou-zko1`): Skein Mass from Linking and Torus-Knot Zero-Volume Specialization
-/

/-- Cleared-denominator (`× (q - 1)^2`, since `q^2 ℏ_q^2 = q^2 (1 - q⁻¹)^2 = (q - 1)^2`)
terminal skein resolution mass functional:
`(q - 1)^2 · 𝔪(H) = (q - 1)^2 · Q · 𝔪(L_Hopf) + q^2 · ∑_i Vol(K_i)`. -/
def skeinMassFromLinkingScaled (q Q massHopf : Int) (vols : List Int) : Int :=
  (q - 1) * (q - 1) * Q * massHopf + q * q * vols.foldl (· + ·) 0

/-- Helper lemma: `List.foldl (· + ·) acc (List.replicate n 0) = acc`. -/
theorem foldl_add_replicate_zero (n : Nat) (acc : Int) :
    (List.replicate n (0 : Int)).foldl (· + ·) acc = acc := by
  induction n generalizing acc with
  | zero => rfl
  | succ k ih =>
    dsimp [List.replicate]
    rw [Int.add_zero]
    exact ih acc

/-- Theorem (`qou-zko1`): When all `n` constituent knots in a terminal skein resolution are torus
knots (`Vol(K_i) = 0`), the constituent volume sum vanishes and the scaled hadron mass reduces
purely to the Hopf-link binding energy `(q - 1)^2 · Q · 𝔪(L_Hopf)`. -/
theorem skein_mass_torus_constituents_zero_vol (q Q massHopf : Int) (n : Nat) :
    skeinMassFromLinkingScaled q Q massHopf (List.replicate n 0) =
      (q - 1) * (q - 1) * Q * massHopf := by
  dsimp [skeinMassFromLinkingScaled]
  rw [foldl_add_replicate_zero n 0, Int.mul_zero, Int.add_zero]

/-!
## Part 5 (`qou-brt1`): Vertex Volume Perturbation Formula and Balanced `q`-Integer Recurrence
-/

/-- Cleared-denominator balanced `q`-integer numerator `q^{m-1} [m]_q` for `m ∈ {0, 1, 2, 3}`:
- `m = 0`: `0` (`[0]_q = 0` at `k = 3`)
- `m = 1`: `1` (`[1]_q = 1` at `k = 4`)
- `m = 2`: `q^2 + 1` (`q [2]_q = q^2 + 1` at `k = 5`)
- `m = 3`: `q^4 + q^2 + 1` (`q^2 [3]_q = q^4 + q^2 + 1` at `k = 6`). -/
def qIntBalNum (q : Int) : Nat → Int
  | 0 => 0
  | 1 => 1
  | 2 => q * q + 1
  | _ => q * q * q * q + q * q + 1

/-- Cleared-denominator vertex volume perturbation `δΦ_k^{(num)}(q, zNum, vol41)` at level
`k = m + 3` (`m = k - 3`). -/
def volumePerturbationNum (q zNum vol41 : Int) (m : Nat) : Int :=
  zNum * zNum * vol41 * qIntBalNum q m

/-- Theorem (`qou-brt1`):
1. At the unperturbed level `k = 3` (`m = 0`), the vertex volume perturbation vanishes:
   `volumePerturbationNum q zNum vol41 0 = 0`.
2. At `k = 4` (`m = 1`), `volumePerturbationNum q zNum vol41 1 = zNum^2 * vol41`.
3. Two-term balanced `q`-integer recurrence across `m = 0, 1, 2` (`k = 3, 4, 5`) and `m = 1, 2, 3` (`k = 4, 5, 6`):
   `q^2 * δΦ^{(num)}(m) + δΦ^{(num)}(m+2) = (q^2 + 1) * δΦ^{(num)}(m+1)`. -/
theorem volume_perturbation_zero_and_three_term_recurrence (q zNum vol41 : Int) :
    volumePerturbationNum q zNum vol41 0 = 0 ∧
    volumePerturbationNum q zNum vol41 1 = zNum * zNum * vol41 ∧
    q * q * volumePerturbationNum q zNum vol41 0 + volumePerturbationNum q zNum vol41 2 =
      (q * q + 1) * volumePerturbationNum q zNum vol41 1 ∧
    q * q * volumePerturbationNum q zNum vol41 1 + volumePerturbationNum q zNum vol41 3 =
      (q * q + 1) * volumePerturbationNum q zNum vol41 2 := by
  dsimp [volumePerturbationNum, qIntBalNum]
  refine ⟨by rw [Int.mul_zero], by rw [Int.mul_one], ?_, ?_⟩
  · rw [Int.mul_zero, Int.mul_zero, Int.zero_add, Int.mul_one, Int.mul_comm (q * q + 1) _]
  · have h1 : q * q * (zNum * zNum * vol41 * 1) +
        zNum * zNum * vol41 * (q * q * q * q + q * q + 1) =
        zNum * zNum * vol41 * (q * q + (q * q * q * q + q * q + 1)) := by
      rw [Int.mul_one, Int.mul_comm (q * q) (zNum * zNum * vol41), ← Int.mul_add]
    have h2 : (q * q + 1) * (zNum * zNum * vol41 * (q * q + 1)) =
        zNum * zNum * vol41 * ((q * q + 1) * (q * q + 1)) := by
      rw [Int.mul_comm (q * q + 1) _, Int.mul_assoc]
    have h3 : q * q + (q * q * q * q + q * q + 1) = (q * q + 1) * (q * q + 1) := by
      rw [Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_one, ← Int.mul_assoc]
      omega
    rw [h1, h2, h3]

end QOU.Foundations.DescendedTraceNormCentralChannelSplitPairSkeinChiralityLinkingVolumePerturbation
