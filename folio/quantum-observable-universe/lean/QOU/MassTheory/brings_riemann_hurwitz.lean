import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.ArchimedeanUniverse.brings_riemann_hurwitz

Content block
[`lem:brings-riemann-hurwitz`](../../../quantum-observable-universe/brings-surface/brings-riemann-hurwitz.md):
*Let `π : Σ₄ → ℙ¹` be a branched covering of degree `4` from a genus-`4` curve
onto the projective line. Its total ramification is fixed by the
Riemann–Hurwitz formula: `R_tot = 2g(Σ₄) − 2 − 4(2g(ℙ¹) − 2) = 14`.*

## Lean structure & Round-Trip Pass-3 Alignment

1. **Pass-3 canonical entrypoint (`BringsRiemannHurwitzContext`, `brings_riemann_hurwitz`):**
   Preserved verbatim per Round-Trip Pass 3 (`c3d2cab80a9`): `BringsRiemannHurwitzContext`
   carries the genera (`g_Sigma = 4`, `g_P1 = 0`), covering degree (`deg = 4`), and
   branch-point count (`n_branch = 6`) as explicit inputs (with **no** global typeclass
   instance), and `brings_riemann_hurwitz` derives `R_tot = 14` by arithmetic.

2. **Branched-cover ramification divisor model (`FiberProfile`, `BranchedCoverData`):**
   - `brings_adjunction_genus_eq_four`: complete-intersection `[1, 2, 3]` in `ℙ⁴` gives
     `deg K_{Σ₄} = 6` and `g(Σ₄) = 4`.
   - `localRamification_eq_deg_sub_length`: for any partition `e₁ + ⋯ + e_m = d` (`eᵢ ≥ 1`),
     `∑ᵢ (eᵢ − 1) = d − m`.
   - `brings_cover_ramification_forced`: **every** degree-`4` branched cover from genus `4`
     to genus `0` satisfies `totalRamification = 14` and `5 ≤ numBranchPoints ≤ 14`.
   - `six_branch_ramification_classification`: classifies all `6`-branch-point degree-`4`
     ramification count triples `(n₁, n₂, n₃) ∈ {(0, 4, 2), (1, 2, 3), (2, 0, 4)}`.
   - `bringsCanonicalCover` & `bringsCanonicalCoverContext`: explicit `def` witnesses
     (not instances) realising `deg = 4`, `R_tot = 14`, `numBranchPoints = 6`.

## References

- [leitner2026] brings-surface/brings-riemann-hurwitz.md.
-/

namespace QOU.ArchimedeanUniverse

/-- Geometric context for the Riemann–Hurwitz lemma.

    The data are the genuine geometric inputs (the two genera, the
    covering degree, and the branch-point count). The total ramification
    is *defined* from them via Riemann–Hurwitz (see `R_tot` below), so
    its value is derived rather than assumed. -/
class BringsRiemannHurwitzContext where
  /-- Genus of Bring's surface `Σ₄` — geometric input `g(Σ₄) = 4`. -/
  g_Sigma : ℕ
  /-- The classical genus fact for Bring's surface. -/
  genus_Sigma : g_Sigma = 4
  /-- Genus of the target `ℙ¹` — geometric input `g(ℙ¹) = 0`. -/
  g_P1 : ℕ
  /-- The genus of the projective line. -/
  genus_P1 : g_P1 = 0
  /-- Degree of the covering `π : Σ₄ → ℙ¹` — geometric input. -/
  deg : ℕ
  /-- The covering degree. -/
  deg_is_four : deg = 4
  /-- Number of branch points. -/
  n_branch : ℕ
  /-- The branch-point count hypothesis. -/
  branch_is_six : n_branch = 6

namespace BringsRiemannHurwitzContext

variable [ctx : BringsRiemannHurwitzContext]

/-- Total ramification, **defined** by the Riemann–Hurwitz formula
    `R_tot = (2 g_Σ − 2) − deg·(2 g_{ℙ¹} − 2)`. -/
def R_tot : ℤ :=
  (2 * (ctx.g_Sigma : ℤ) - 2) - (ctx.deg : ℤ) * (2 * (ctx.g_P1 : ℤ) - 2)

end BringsRiemannHurwitzContext

/-- **Lemma** ([`lem:brings-riemann-hurwitz`]):
    under `BringsRiemannHurwitzContext`, the covering has degree `4`, total
    ramification `R_tot = 14` (derived from Riemann–Hurwitz with `g_Σ = 4`,
    `g_{ℙ¹} = 0`, `deg = 4`), and `6` branch points. -/
-- Ref: [leitner2026] brings-surface/brings-riemann-hurwitz.md
theorem brings_riemann_hurwitz [ctx : BringsRiemannHurwitzContext] :
    ctx.deg = 4 ∧ BringsRiemannHurwitzContext.R_tot = 14 ∧ ctx.n_branch = 6 := by
  refine ⟨ctx.deg_is_four, ?_, ctx.branch_is_six⟩
  unfold BringsRiemannHurwitzContext.R_tot
  rw [ctx.genus_Sigma, ctx.genus_P1, ctx.deg_is_four]
  norm_num

/-! ## Complete-intersection adjunction & branched-cover ramification profiles -/

/-- Canonical degree `deg K_C = (∑ dᵢ − (N + 1)) · (∏ dᵢ)` of a smooth complete-intersection
    curve in `ℙ^N`. -/
def completeIntersectionCanonicalDeg (ambientDim : ℕ) (degrees : List ℕ) : ℤ :=
  ((degrees.sum : ℤ) - ((ambientDim : ℤ) + 1)) * (degrees.prod : ℤ)

/-- Genus `g(Σ₄)` of Bring's surface derived from its `(1, 2, 3)` complete
    intersection in `ℙ⁴` via `2g − 2 = deg K_{Σ₄}`. -/
def bringsAdjunctionGenus : ℕ :=
  ((completeIntersectionCanonicalDeg 4 [1, 2, 3] + 2) / 2).toNat

/-- Adjunction evaluation: `deg K_{Σ₄} = 6` and `g(Σ₄) = 4`. -/
-- Ref: [leitner2026] brings-surface/brings-riemann-hurwitz-proof.md
theorem brings_adjunction_genus_eq_four :
    completeIntersectionCanonicalDeg 4 [1, 2, 3] = 6 ∧
    bringsAdjunctionGenus = 4 := by
  simp [bringsAdjunctionGenus, completeIntersectionCanonicalDeg]

/-- Ramification multiplicity partition `[e₁, …, e_m]` of a fiber of a degree-`d`
    branched cover (`eᵢ ≥ 1`, `∑ eᵢ = d`). -/
structure FiberProfile (deg : ℕ) where
  /-- Ramification indices at the preimages in the fiber. -/
  mults : List ℕ
  /-- Every preimage has multiplicity at least `1`. -/
  pos_mults : ∀ e ∈ mults, 1 ≤ e
  /-- Sum of multiplicities equals the sheet degree `deg`. -/
  sum_eq_deg : mults.sum = deg

namespace FiberProfile

/-- Tame local ramification `R_y = ∑ᵢ (eᵢ − 1)` of a fiber. -/
def localRamification {deg : ℕ} (F : FiberProfile deg) : ℕ :=
  (F.mults.map (fun e => e - 1)).sum

private theorem sum_sub_one_add_length :
    ∀ (l : List ℕ), (∀ e ∈ l, 1 ≤ e) →
      (l.map (fun e => e - 1)).sum + l.length = l.sum
  | [], _ => rfl
  | e :: es, hpos => by
    have he : 1 ≤ e := hpos e (by simp)
    have hes : ∀ x ∈ es, 1 ≤ x := fun x hx => hpos x (by simp [hx])
    have ih := sum_sub_one_add_length es hes
    simp only [List.map_cons, List.sum_cons, List.length_cons]
    omega

/-- **Fiber Hurwitz identity**: for any partition `e₁ + ⋯ + e_m = d` with `eᵢ ≥ 1`,
    the local ramification `∑ᵢ (eᵢ − 1)` equals `d − m`. -/
-- Ref: [leitner2026] brings-surface/brings-riemann-hurwitz-proof.md
theorem localRamification_eq_deg_sub_length {deg : ℕ} (F : FiberProfile deg) :
    F.localRamification = deg - F.mults.length ∧
    F.localRamification + F.mults.length = deg := by
  unfold localRamification
  have h := sum_sub_one_add_length F.mults F.pos_mults
  rw [F.sum_eq_deg] at h
  exact ⟨by omega, h⟩

/-- Every fiber of a positive-degree cover has at least one preimage (`m ≥ 1`),
    and if `m < d` (branched fiber) then `1 ≤ R_y ≤ d − 1`. -/
theorem localRamification_bounds_of_branched {deg : ℕ} (hdeg : 0 < deg)
    (F : FiberProfile deg) (hbr : F.mults.length < deg) :
    1 ≤ F.localRamification ∧ F.localRamification ≤ deg - 1 := by
  have hne : F.mults ≠ [] := by
    intro hemp
    have hs := F.sum_eq_deg
    rw [hemp] at hs
    simp at hs
    omega
  have hlen_pos : 1 ≤ F.mults.length := List.length_pos_iff.mpr hne
  have hsum := (F.localRamification_eq_deg_sub_length).2
  omega

end FiberProfile

/-- Finite tamely branched cover data `π : X → Y` satisfying Riemann–Hurwitz
    `2g_X − 2 = deg · (2g_Y − 2) + ∑_{k} R_k`. -/
structure BranchedCoverData where
  /-- Genus `g_X` of the source curve `X`. -/
  g_source : ℕ
  /-- Genus `g_Y` of the target curve `Y`. -/
  g_target : ℕ
  /-- Sheet degree `d > 0` of `π : X → Y`. -/
  deg : ℕ
  /-- Degree is positive. -/
  deg_pos : 0 < deg
  /-- Multiplicity profiles over the branch points in `Y`. -/
  branchFibers : List (FiberProfile deg)
  /-- Every listed branch fiber has strictly fewer than `deg` preimages (`R_k ≥ 1`). -/
  all_branched : ∀ F ∈ branchFibers, F.mults.length < deg
  /-- Riemann–Hurwitz formula relating Euler characteristics and total ramification. -/
  riemann_hurwitz :
    2 * (g_source : ℤ) - 2 =
      (deg : ℤ) * (2 * (g_target : ℤ) - 2) +
        ((branchFibers.map FiberProfile.localRamification).sum : ℤ)

namespace BranchedCoverData

/-- Total ramification degree `R_tot = ∑_k R_k`. -/
def totalRamification (C : BranchedCoverData) : ℕ :=
  (C.branchFibers.map FiberProfile.localRamification).sum

/-- Number of branch points `b = |branchFibers|`. -/
def numBranchPoints (C : BranchedCoverData) : ℕ :=
  C.branchFibers.length

end BranchedCoverData

private theorem sum_ramification_bounds_deg_four :
    ∀ (fs : List (FiberProfile 4)), (∀ F ∈ fs, F.mults.length < 4) →
      fs.length ≤ (fs.map FiberProfile.localRamification).sum ∧
      (fs.map FiberProfile.localRamification).sum ≤ 3 * fs.length
  | [], _ => by simp
  | F :: rest, hbr => by
    have hF := F.localRamification_bounds_of_branched (by omega) (hbr F (by simp))
    have ih := sum_ramification_bounds_deg_four rest (fun G hG => hbr G (by simp [hG]))
    simp only [List.map_cons, List.sum_cons, List.length_cons]
    omega

/-- **Universal Riemann–Hurwitz forcing for `Σ₄ → ℙ¹`**:
    for **any** degree-`4` branched cover from Bring's genus-`4` curve (`g_X = bringsAdjunctionGenus`)
    to `ℙ¹` (`g_Y = 0`), Riemann–Hurwitz forces `R_tot = 14` and `5 ≤ b ≤ 14`. -/
-- Ref: [leitner2026] brings-surface/brings-riemann-hurwitz.md
theorem brings_cover_ramification_forced (C : BranchedCoverData)
    (hgX : C.g_source = bringsAdjunctionGenus)
    (hgY : C.g_target = 0)
    (hdeg : C.deg = 4) :
    C.totalRamification = 14 ∧
    5 ≤ C.numBranchPoints ∧
    C.numBranchPoints ≤ 14 := by
  have hg4 : C.g_source = 4 := hgX.trans brings_adjunction_genus_eq_four.2
  rcases C with ⟨gX, gY, d, hdpos, fs, hbr, hrh⟩
  dsimp only at hg4 hgY hdeg
  subst hg4 hgY hdeg
  have hbds := sum_ramification_bounds_deg_four fs hbr
  unfold BranchedCoverData.totalRamification BranchedCoverData.numBranchPoints
  dsimp only
  omega

/-- **Classification of 6-branch-point degree-4 ramification profiles**:
    if `n₁, n₂, n₃` count fibers of local ramification `1, 2, 3` (`[2,1,1]`,
    `[3,1]`/`[2,2]`, `[4]`) over `6` branch points with total ramification `14`,
    then `(n₁, n₂, n₃) ∈ {(0, 4, 2), (1, 2, 3), (2, 0, 4)}`. -/
-- Ref: [leitner2026] brings-surface/brings-riemann-hurwitz-proof.md
theorem six_branch_ramification_classification (n₁ n₂ n₃ : ℕ) :
    (n₁ + n₂ + n₃ = 6 ∧ n₁ + 2 * n₂ + 3 * n₃ = 14) ↔
    (n₁, n₂, n₃) ∈ ({(0, 4, 2), (1, 2, 3), (2, 0, 4)} : Finset (ℕ × ℕ × ℕ)) := by
  constructor
  · rintro ⟨h6, h14⟩
    have hn1 : n₁ ≤ 6 := by omega
    have hn2 : n₂ ≤ 6 := by omega
    have hn3 : n₃ ≤ 6 := by omega
    interval_cases n₁ <;> interval_cases n₂ <;> simp_all <;> omega
  · intro hmem
    simp only [Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq] at hmem
    rcases hmem with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ <;> omega

/-- Total-ramification fiber `[4]` (`m = 1`, `R = 3`) for degree `4`. -/
def fiberRamThree : FiberProfile 4 where
  mults := [4]
  pos_mults := by simp
  sum_eq_deg := rfl

/-- Triple-point fiber `[3, 1]` (`m = 2`, `R = 2`) for degree `4`. -/
def fiberRamTwo : FiberProfile 4 where
  mults := [3, 1]
  pos_mults := by simp
  sum_eq_deg := rfl

/-- Explicit `6`-branch-point degree-`4` Riemann–Hurwitz cover profile
    `Σ₄ → ℙ¹` (`(n₁, n₂, n₃) = (0, 4, 2)`, `2 · 3 + 4 · 2 = 14`). -/
def bringsCanonicalCover : BranchedCoverData where
  g_source := bringsAdjunctionGenus
  g_target := 0
  deg := 4
  deg_pos := by norm_num
  branchFibers :=
    [fiberRamThree, fiberRamThree, fiberRamTwo, fiberRamTwo, fiberRamTwo, fiberRamTwo]
  all_branched := by
    simp [fiberRamThree, fiberRamTwo]
  riemann_hurwitz := by
    rw [brings_adjunction_genus_eq_four.2]
    simp [fiberRamThree, fiberRamTwo, FiberProfile.localRamification]

/-- Explicit `def` witness (deliberately not an `instance`) for `BringsRiemannHurwitzContext`. -/
def bringsCanonicalCoverContext : BringsRiemannHurwitzContext where
  g_Sigma := bringsCanonicalCover.g_source
  genus_Sigma := brings_adjunction_genus_eq_four.2
  g_P1 := bringsCanonicalCover.g_target
  genus_P1 := rfl
  deg := bringsCanonicalCover.deg
  deg_is_four := rfl
  n_branch := bringsCanonicalCover.numBranchPoints
  branch_is_six := rfl

/-- Full branched-cover ramification summary for `Σ₄ → ℙ¹`. -/
theorem brings_riemann_hurwitz_branched_cover :
    bringsAdjunctionGenus = 4 ∧
    (∀ C : BranchedCoverData,
      C.g_source = bringsAdjunctionGenus → C.g_target = 0 → C.deg = 4 →
        C.totalRamification = 14 ∧
        (∀ F ∈ C.branchFibers, F.localRamification = 4 - F.mults.length)) ∧
    bringsCanonicalCover.deg = 4 ∧
    bringsCanonicalCover.totalRamification = 14 ∧
    bringsCanonicalCover.numBranchPoints = 6 := by
  refine ⟨brings_adjunction_genus_eq_four.2, ?_, rfl, ?_, rfl⟩
  · intro C hgX hgY hdeg
    refine ⟨(brings_cover_ramification_forced C hgX hgY hdeg).1, ?_⟩
    intro F _
    exact (F.localRamification_eq_deg_sub_length).1.trans
      (congr_arg (· - F.mults.length) hdeg)
  · exact (brings_cover_ramification_forced bringsCanonicalCover rfl rfl rfl).1

end QOU.ArchimedeanUniverse
