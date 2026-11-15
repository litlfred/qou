import Mathlib.Tactic
import QOU.StandardModel.PolarizationRealStructure

/-!
# R1: can Bring's real structure fix the polarization phase `λ`?

Bean `qou-r1bn` (epic `qou-qs0e`). Audit:
`docs/audits/2026-11-15-r1-braden-northover-real-structure-on-sp.md`.

`PolarizationRealStructure.lean` (PR #7825) showed that the model cone carries a `U(1)`
of real structures `p ↦ u p ū`, `u = c j + d k`, and selects none. The remaining
candidate was the real structure of Bring's curve `B` (Braden–Northover). The corpus
has **no map** from `B` or `Jac(B)` to the polarization line `𝒮_p`, so the transport
itself is not derivable now (scope (a)). This file proves the structural facts that
constrain any such transport. Every statement is about the model sphere or about the
permutation group; none asserts that a transport exists.

## The model sphere

On `S²` (pure quaternions) the reflection with unit normal `n` is
`x ↦ −n x n̄` (`refl`). The real structure `realStr u` of PR #7825 acts on `S²` as
`refl u` (`hopf_realStr`), so the `U(1)` family is the reflections whose normal lies in
the `j`–`k` plane. They all fix the chart centres `±i` (`refl_orthW_unitI`).

## Proved here (generic `[CommRing R]`, §7c)

1. `hopf_realStr`: the family acts on `S²` by the reflections `refl u`.
2. `conjBy_refl_conjBy`: a rotation carries `refl n` to `refl (g n ḡ)` (covariance).
3. **Dichotomy for the chart centres `±i`.**
   * `refl_orthW_unitI`: every member of the PR #7825 family fixes `i`.
   * `refl_unitI_unitI`: the reflection with normal `i` swaps `i ↔ −i`.
   * `refl_unitI_comm_cplx`: the reflection with normal `i` commutes with **every**
     `λ`-rotation `conjBy (a + b i)`. So it is `λ`-invariant and cannot fix `λ`.
   * `rot90_normal_axial`: if the `90°` `λ`-rotation fixes a normal up to sign, the
     normal is along `i`. So the only `λ`-invariant reflection is the one with normal
     `i`, which swaps the chart centres.
4. `no_omega_invariant_orthW`: the 3-fold element `ω = 1 + i + j + k` of the binary
   icosahedral group (standard embedding) fixes no member of the family, even up to
   scale. **The corpus does not establish that `A₅` acts on the cone**
   (`BringConeIcosahedral.lean`); this is the hypothetical case.
5. `perm_comm_swaps_eq_one`, `bring_central_real_structure_unique`: a permutation of a
   set of at least three points that commutes with every transposition is the identity.
   With `Aut(B) = S₅` and coordinate conjugation `c` commuting with `S₅` (Riera–Rodríguez;
   cited, not formalized), the real structures of `B` are `c ∘ g` with `g² = 1`, and
   `c` is the only one commuting with all of `Aut(B)`.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [riera-rodriguez-1992] Riera, Rodríguez, The period matrix of Bring's curve, Pacific J. Math. 154 (1992)
-- Ref: [braden-northover-2012] Braden, Northover, Bring's curve: its period matrix, boundary evaluation, and the Riemann period problem
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-! ## 1. The PR #7825 family on the sphere -/

/-- Reflection of the sphere with normal `n`: `x ↦ −n x n̄`. -/
def refl (n x : BringCone R) : BringCone R := -(conjBy n x)

/-- For `u = c j + d k` a unit, `ū i u = −i`. -/
theorem star_orthW_unitI_orthW {c d : R} (h : c * c + d * d = 1) :
    star (orthW c d) * unitI * orthW c d = -unitI := by
  ext <;> simp [orthW, unitI] <;> first | ring1 | linear_combination h | linear_combination -h

/-- **The real structures of PR #7825 act on `S²` as reflections**:
`hopf (u p ū) = −u (hopf p) ū`. -/
theorem hopf_realStr {c d : R} (h : c * c + d * d = 1) (p : BringCone R) :
    hopf (realStr (orthW c d) p) = refl (orthW c d) (hopf p) := by
  have key := star_orthW_unitI_orthW h
  have e : hopf (realStr (orthW c d) p)
      = orthW c d * p * (star (orthW c d) * unitI * orthW c d) * star p
          * star (orthW c d) := by
    simp only [hopf, realStr, star_mul, star_star, mul_assoc]
  rw [e, key]
  simp only [refl, conjBy, hopf, mul_neg, neg_mul, mul_assoc]

/-! ## 2. Covariance -/

/-- **Rotating a reflection rotates its normal**: `g ∘ refl n ∘ ḡ = refl (g n ḡ)` (as
conjugations; for `normSq g = 1` the outer maps are mutually inverse rotations). -/
theorem conjBy_refl_conjBy (g n x : BringCone R) :
    conjBy g (refl n (conjBy (star g) x)) = refl (conjBy g n) x := by
  simp only [refl, conjBy, star_mul, star_star, mul_neg, neg_mul, mul_assoc]

/-- The sign of the normal does not matter. -/
theorem refl_neg (n x : BringCone R) : refl (-n) x = refl n x := by
  simp [refl, conjBy]

/-! ## 3. The chart-centre dichotomy -/

/-- **Every member of the PR #7825 family fixes the chart centre `i`.** -/
theorem refl_orthW_unitI {c d : R} (h : c * c + d * d = 1) :
    refl (orthW c d) unitI = unitI := by
  ext <;> simp [refl, conjBy, orthW, unitI] <;>
    first | ring1 | linear_combination h | linear_combination -h

/-- **The reflection with normal `i` swaps the chart centres** `i ↦ −i`. -/
theorem refl_unitI_unitI : refl (unitI : BringCone R) unitI = -unitI := by
  ext <;> simp [refl, conjBy, unitI]

/-- The reflection with normal `i` negates the `i`-component: its mirror is the
`j`–`k` great circle, which contains neither chart centre. -/
theorem refl_unitI_apply (x : BringCone R) :
    refl unitI x = ⟨-x.re, -x.imI, x.imJ, x.imK⟩ := by
  ext <;> simp [refl, conjBy, unitI]

/-- **The reflection with normal `i` is `λ`-invariant**: it commutes with every rotation
`conjBy (a + b i)` about the `i`-axis, which are exactly the `λ`-rotations of
`hopf_dict_rotate`. So it cannot single out a value of `λ`. -/
theorem refl_unitI_comm_cplx (a b : R) (x : BringCone R) :
    conjBy (cplx a b) (refl unitI x) = refl unitI (conjBy (cplx a b) x) := by
  ext <;> simp [refl, conjBy, cplx, unitI] <;> ring

/-- **Only the axial normal is `λ`-invariant.** If the `90°` rotation about `i`
(`g = 1 + i`, scale `normSq g = 2`) fixes the normal `n` up to sign, `g n ḡ = ±2 n`,
then `n` has no `j`- or `k`-component. -/
theorem rot90_normal_axial (h2 : ∀ x : R, 2 * x = 0 → x = 0) {n : BringCone R} {r : R}
    (hr : r = 2 ∨ r = -2) (h : conjBy (cplx 1 1) n = r • n) :
    n.imJ = 0 ∧ n.imK = 0 := by
  have hJ := congrArg (fun x : BringCone R => x.imJ) h
  have hK := congrArg (fun x : BringCone R => x.imK) h
  simp [conjBy, cplx] at hJ hK
  rcases hr with rfl | rfl
  · have hk : n.imK = 0 := h2 _ (by linear_combination hJ + hK)
    refine ⟨h2 _ (by linear_combination hK - 2 * hk), hk⟩
  · have hk : n.imK = 0 := h2 _ (by linear_combination hK - hJ)
    refine ⟨h2 _ (by linear_combination -hK + 2 * hk), hk⟩

/-! ## 4. The icosahedral 3-fold element fixes no member of the family -/

/-- `ω = 1 + i + j + k`, twice the order-6 element `(1 + i + j + k)/2` of the binary
icosahedral group in its standard embedding. -/
def omegaQ : BringCone R := ⟨1, 1, 1, 1⟩

/-- `ω` rotates `j ↦ k ↦ i` (scaled by `normSq ω = 4`): `ω (c j + d k) ω̄ = 4 d i + 4 c k`. -/
theorem conjBy_omegaQ_orthW (c d : R) :
    conjBy omegaQ (orthW c d) = ⟨0, 4 * d, 0, 4 * c⟩ := by
  ext <;> simp [conjBy, omegaQ, orthW] <;> ring

/-- **`ω` fixes no member of the family, even up to scale**, when `4` is cancellable. -/
theorem no_omega_invariant_orthW (h4 : ∀ x : R, 4 * x = 0 → x = 0) {c d r : R}
    (h : conjBy omegaQ (orthW c d) = r • orthW c d) : c = 0 ∧ d = 0 := by
  rw [conjBy_omegaQ_orthW] at h
  have hI := congrArg (fun x : BringCone R => x.imI) h
  have hK := congrArg (fun x : BringCone R => x.imK) h
  simp [orthW] at hI hK
  have hd : d = 0 := h4 _ hI
  refine ⟨h4 _ ?_, hd⟩
  rw [hK, hd, mul_zero]

/-- With a unit normal, the hypothetical icosahedral action leaves no member invariant. -/
theorem no_omega_invariant_unit [Nontrivial R] (h4 : ∀ x : R, 4 * x = 0 → x = 0)
    {c d r : R} (hu : c * c + d * d = 1) :
    conjBy omegaQ (orthW c d) ≠ r • orthW c d := by
  intro h
  obtain ⟨rfl, rfl⟩ := no_omega_invariant_orthW h4 h
  simp at hu

end QOU.Tetraplectic

namespace QOU.Brings

/-! ## 5. Bring side: the `Aut(B)`-central real structure is unique -/

/-- If `g` commutes with the transposition `(a b)`, then `g a ∈ {a, b}`. -/
theorem apply_mem_of_comm_swap {α : Type*} [DecidableEq α] {g : Equiv.Perm α} {a b : α}
    (hab : a ≠ b) (hc : g * Equiv.swap a b = Equiv.swap a b * g) :
    g a = a ∨ g a = b := by
  by_contra hne
  push_neg at hne
  have e := congrArg (fun f : Equiv.Perm α => f b) hc
  simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_right] at e
  rw [Equiv.swap_apply_of_ne_of_ne hne.1 hne.2] at e
  exact hab (g.injective e)

/-- **A permutation commuting with every transposition is the identity**, on any set in
which every point has two further distinct points (so on `Fin 5`). -/
theorem perm_comm_swaps_eq_one {α : Type*} [DecidableEq α]
    (hthree : ∀ a : α, ∃ b c : α, a ≠ b ∧ a ≠ c ∧ b ≠ c) {g : Equiv.Perm α}
    (hc : ∀ a b : α, g * Equiv.swap a b = Equiv.swap a b * g) : g = 1 := by
  ext a
  obtain ⟨b, c, hab, hac, hbc⟩ := hthree a
  rcases apply_mem_of_comm_swap hab (hc a b) with h1 | h1
  · simpa using h1
  · rcases apply_mem_of_comm_swap hac (hc a c) with h2 | h2
    · simpa using h2
    · exact absurd (h1.symm.trans h2) hbc

/-- **Bring's curve: `c` is the only real structure commuting with `Aut(B) = S₅`.**
The real structures of `B` are `c ∘ g` with `g ∈ S₅`, `g² = 1` (coordinate conjugation
`c` commutes with the permutation action). `c ∘ g` commutes with every `h ∈ S₅` iff `g`
does, and then `g = 1`. -/
theorem bring_central_real_structure_unique {g : Equiv.Perm (Fin 5)}
    (hc : ∀ h : Equiv.Perm (Fin 5), g * h = h * g) : g = 1 :=
  perm_comm_swaps_eq_one (by decide) (fun a b => hc _)

end QOU.Brings
