import QOU.Eightfold.FureyMinimalLeftIdeal
import Mathlib.LinearAlgebra.Basis.Bilinear

set_option maxHeartbeats 8000000

/-!
# QOU.Eightfold.FureyIdealTowerTest — the ideal `S_u`, its `su(3)` structure, and the
# forced-embedding test against the tower's chirality / flavour data

Bean `qou-s4xb` (epic `qou-8lxd`), stream 15. Continues `FureyMinimalLeftIdeal`.

## Part A — the minimal left ideal (Furey thesis §6.6)

Over a generic `[Field K] [CharZero K]` with `i * i = −1`:

* `vacProj` — the operator `ωω† = α₁α₂α₃α₃†α₂†α₁†` (`αⱼ = βⱼ/2`), with
  `vacProj x = φ(x) • Ω`, `φ(x) = (x₀ − i x₁)/2`, `φ(Ω) = 1` (`vacProj_apply`,
  `vacProj_idem`): a rank-one idempotent.
* `Su` — the left ideal `{X ∈ End_K(𝕆_K) : X ∘ ωω† = X} = End_K(𝕆_K) · ωω†` (a left ideal:
  `Su_left_ideal`); `Su ≃ₗ 𝕆_K` by `X ↦ X Ω` (`SuEquiv`), so **`dim_K S_u = 8`**
  (`finrank_Su`), and it is **minimal**: every nonzero `X ∈ S_u` generates it
  (`Su_minimal`).
* `fock_linearIndependent` — Furey's eight states `αᵢ†…ωω†` (6.19) form a basis.
* `Sd`, the conjugate ideal of `ω†ω`, is the Galois image `i ↦ −i` (part 1,
  `omegaD_omega_apply`).

## Part B — the `su(3)` decomposition `1 ⊕ 3 ⊕ 3̄ ⊕ 1`

The corpus colour algebra `su3 stdIm ⊂ Der𝕆` (ℚ-derivations fixing `e₁`) acts on `𝕆_K` by
base change (`extD`), still by derivations (`extD_leibniz`). Under `S_u ≃ 𝕆_K` the induced
action on the ideal is this one (left multiplication by `[D, ·]` with `D Ω = 0`). Proven:

* levels 0 and 3 (`ν = Ω`, `e⁺ = fock 7`) are killed (`extD_su3_kills_fock0/7`);
* level 1 (`L(e₁) = +i` on `Im`) and level 2 (`L(e₁) = −i` on `Im`) are preserved
  (`extD_su3_mem_levelSpace`), and contain the Fock vectors 1–3 resp. 4–6;
* the su(3)-INVARIANT vectors are exactly `span(Ω, e⁺)` (`su3_invariant_iff`) — so the two
  singlets are levels 0 and 3, and levels 1, 2 carry no invariant vector;
* levels 1 and 2 are exchanged by the Galois substitution `i ↦ −i` (definitional:
  `levelSpace (−i) s = levelSpace i (−s)`), the `3 ↔ 3̄` exchange.

NOT proven here: irreducibility of the two triplets (the classical `3`, `3̄`); only
invariance, the absence of invariant vectors, and the dimensions via the Fock basis.

## Part C — the forced-embedding test (the stream-15 question)

Tower side (corpus, not re-proved here): the quark state is the `h¹` part of one Hecke
letter, a SCALAR multiple of `1` (`QuarkState.quarkState_eq`); chirality is the eigenline
pair `P±` of the letter, with grading `J = P₊ − P₋`, `J² = 1`
(`OneSidedWeakVertex.grading_sq`); flavour `σ ↔ σ⁻¹` FIXES both eigenlines (chirality-blind).
The tower carries no action of the octonionic `su3 e₁` (its colour is the separate level-3
`gl₃` Schur–Weyl; stream 6c bridges the two).

The only forcing structures on `S_u ≅ 𝕆_K` compatible with that are: `su(3)`-equivariance
with the tower side trivial, and a `ℤ/2`-grading to intertwine `J` with. The one `ℤ/2`
grading `S_u` carries canonically is `G := i·L(e₁)`, and part 1's `Le_fock` shows
**`G = (−1)^N`** (`G_fock`). Results:

* `colourBlind_lands_in_singlets` — ANY `su(3)`-equivariant `K`-linear map from colour-blind
  data lands in `span(ν, e⁺)`: it can never reach the quark levels 1, 2.
* `forced_chirality_embedding` — if it also intertwines `J` with `G`, then the `J = +1`
  line goes into `K·ν` and the `J = −1` line into `K·e⁺`: **unique up to one scalar per
  line**, and the opposite root `−i` (which negates `G`, `G_neg_root`) swaps the two. This
  is outcome (b) for chirality alone — and its image is LEPTONIC.
* `flavour_obstruction` — Furey's `S_u ↔ S_d` exchange carries the `G = +1` vacuum to the
  `G = −1` vacuum (`G_vacD`), so NO `G`-commuting (= chirality-blind) operator realises it.
  The tower flavour flip is chirality-blind; Furey's ideal flip is chirality-odd.

**Verdict: (c).** No map from the tower data into `S_u`, `S_d` is forced by structure both
sides carry and reaches the quark states. The extra choices needed, exactly:
1. a colour index on the tower quark state — a `K`-linear identification of a tower colour
   triplet with level 1 (or 2) of `S_u`, intertwining the tower `gl₃` with `su3 e₁` (the
   stream-6c bridge); without it every equivariant map lands in the lepton singlets;
2. which of level 1 / level 2 is "the" triplet, which here is the same bit as the root
   `i` vs `−i` (Galois), i.e. not fixed by any tower structure;
3. for flavour, a map that is `G`-ODD; since the tower flip is `J`-even, matching it to
   `S_u ↔ S_d` forces abandoning `J ↦ G`, i.e. a chirality identification that is not
   the forced one.

Base ring (§7c): generic `[Field K] [CharZero K]` with `i * i = −1`; minimal instance
`ℚ(i)`. No `ℝ`, no `ℂ`, no floats.
-/

namespace QOU.Eightfold.FureyIdeal

open QOU.MathlibExt.OctonionDerivations QOU.MathlibExt.DerivationRankNullity Module

section Field

variable {K : Type*} [Field K] [CharZero K] {i : K}

/-! ## A. The ideal -/

/-- Left multiplication as a `K`-linear map. -/
def lmul (u : Fin 8 → K) : (Fin 8 → K) →ₗ[K] (Fin 8 → K) where
  toFun := omul u
  map_add' := omul_add_right u
  map_smul' c v := omul_smul_right u c v

@[simp] theorem lmul_apply (u v : Fin 8 → K) : lmul u v = omul u v := rfl

variable (i) in
/-- The vacuum functional `φ(x) = (x₀ − i x₁)/2`. -/
def phi : (Fin 8 → K) →ₗ[K] K :=
  (2 : K)⁻¹ • (LinearMap.proj 0 - i • LinearMap.proj 1)

theorem phi_apply (x : Fin 8 → K) : phi i x = (x 0 - i * x 1) / 2 := by
  simp [phi]; ring

theorem phi_vac (hi : i * i = -1) : phi i (vac i) = 1 := by
  rw [phi_apply]; simp [vac]; rw [hi]; norm_num

variable (i) in
/-- **`ωω†`** as an operator: `α₁α₂α₃α₃†α₂†α₁†` with `αⱼ = βⱼ/2`. -/
noncomputable def vacProj : Module.End K (Fin 8 → K) :=
  ((64 : K)⁻¹) • (lmul (beta i 0) ∘ₗ lmul (beta i 1) ∘ₗ lmul (beta i 2) ∘ₗ
    lmul (betaD i 2) ∘ₗ lmul (betaD i 1) ∘ₗ lmul (betaD i 0))

theorem vacProj_apply (hi : i * i = -1) (x : Fin 8 → K) :
    vacProj i x = phi i x • vac i := by
  have h := omega_omegaD_apply hi x
  simp only [Bm_eq, Bd_eq] at h
  simp only [vacProj, LinearMap.smul_apply, LinearMap.comp_apply, lmul_apply, h, smul_smul,
    phi_apply]
  congr 1
  field_simp
  ring

theorem vacProj_idem (hi : i * i = -1) : vacProj i ∘ₗ vacProj i = vacProj i := by
  refine LinearMap.ext fun x => ?_
  rw [LinearMap.comp_apply, vacProj_apply hi x, map_smul, vacProj_apply hi (vac i), phi_vac hi,
    one_smul]

variable (i) in
/-- **Furey's minimal left ideal** `S_u = End_K(𝕆_K)·ωω†`, as `{X : X ∘ ωω† = X}`. -/
noncomputable def Su : Submodule K (Module.End K (Fin 8 → K)) where
  carrier := {X | X ∘ₗ vacProj i = X}
  add_mem' {X Y} hX hY := by
    simp only [Set.mem_setOf_eq] at *; rw [LinearMap.add_comp, hX, hY]
  zero_mem' := by simp
  smul_mem' c X hX := by
    simp only [Set.mem_setOf_eq] at *; rw [LinearMap.smul_comp, hX]

theorem mem_Su {X : Module.End K (Fin 8 → K)} : X ∈ Su i ↔ X ∘ₗ vacProj i = X := Iff.rfl

/-- `S_u` is a left ideal. -/
theorem Su_left_ideal {X : Module.End K (Fin 8 → K)} (hX : X ∈ Su i)
    (Y : Module.End K (Fin 8 → K)) : Y * X ∈ Su i := by
  rw [mem_Su] at *
  rw [Module.End.mul_eq_comp, LinearMap.comp_assoc, hX]

theorem vacProj_mem_Su (hi : i * i = -1) : vacProj i ∈ Su i := vacProj_idem hi

/-- Every element of `S_u` is determined by its value on the vacuum. -/
theorem mem_Su_apply (hi : i * i = -1) {X : Module.End K (Fin 8 → K)} (hX : X ∈ Su i)
    (x : Fin 8 → K) : X x = phi i x • X (vac i) := by
  have := LinearMap.congr_fun hX x
  rw [LinearMap.comp_apply, vacProj_apply hi, map_smul] at this
  exact this.symm

variable (i) in
/-- Evaluation at the vacuum, `S_u → 𝕆_K`. -/
noncomputable def evalVac : Su i →ₗ[K] (Fin 8 → K) where
  toFun X := X.1 (vac i)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- **`S_u ≅ 𝕆_K`** as `K`-spaces (`X ↦ X Ω`, inverse `v ↦ φ(·) v`). -/
noncomputable def SuEquiv (hi : i * i = -1) : Su i ≃ₗ[K] (Fin 8 → K) :=
  LinearEquiv.ofLinear (evalVac i)
    { toFun := fun v => ⟨LinearMap.smulRight (phi i) v, by
        rw [mem_Su]; refine LinearMap.ext fun x => ?_
        simp [vacProj_apply hi, phi_vac hi]⟩
      map_add' := fun v w => by apply Subtype.ext; refine LinearMap.ext fun x => ?_; simp
      map_smul' := fun c v => by
        apply Subtype.ext; refine LinearMap.ext fun x => ?_; simp; exact smul_comm _ _ _ }
    (by refine LinearMap.ext fun v => ?_; simp [evalVac, phi_vac hi])
    (by
      refine LinearMap.ext fun X => ?_
      apply Subtype.ext; refine LinearMap.ext fun x => ?_
      simp [evalVac, mem_Su_apply hi X.2 x])

/-- **`dim_K S_u = 8`** — "eight-complex-dimensional" (Furey, before (6.19)). -/
theorem finrank_Su (hi : i * i = -1) : finrank K (Su i) = 8 := by
  rw [(SuEquiv hi).finrank_eq]; simp

/-- **Minimality**: every nonzero element of `S_u` generates `S_u` as a left ideal. -/
theorem Su_minimal (hi : i * i = -1) {X Y : Module.End K (Fin 8 → K)} (hX : X ∈ Su i)
    (hY : Y ∈ Su i) (hX0 : X ≠ 0) : ∃ T : Module.End K (Fin 8 → K), T * X = Y := by
  have hv : X (vac i) ≠ 0 := by
    intro h; apply hX0; refine LinearMap.ext fun x => ?_; simp [mem_Su_apply hi hX x, h]
  obtain ⟨m, hm⟩ := Function.ne_iff.mp hv
  refine ⟨LinearMap.smulRight ((X (vac i) m)⁻¹ • LinearMap.proj m) (Y (vac i)), ?_⟩
  refine LinearMap.ext fun x => ?_
  rw [Module.End.mul_apply, mem_Su_apply hi hX x, mem_Su_apply hi hY x]
  simp only [map_smul, LinearMap.smulRight_apply, LinearMap.smul_apply, LinearMap.proj_apply,
    smul_eq_mul, smul_smul]
  congr 1
  have hm' : X (vac i) m ≠ 0 := hm
  field_simp

/-- **Furey's eight states are a basis** of `𝕆_K` (hence, via `SuEquiv`, of `S_u`). -/
theorem fock_linearIndependent (hi : i * i = -1) : LinearIndependent K (fock i) := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  have e : ∀ m : Fin 8, (∑ k, g k • fock i k) m = 0 := fun m => by rw [hg]; rfl
  have e0 := e 0; have e1 := e 1; have e2 := e 2; have e3 := e 3
  have e4 := e 4; have e5 := e 5; have e6 := e 6; have e7 := e 7
  simp [Fin.sum_univ_eight, fock] at e0 e1 e2 e3 e4 e5 e6 e7
  have two : (2 : K) ≠ 0 := two_ne_zero
  have h7 : (16 : K) * g 7 = 0 := by linear_combination i * e0 - e1 + 8 * g 7 * hi
  have h5 : (8 : K) * g 5 = 0 := by linear_combination e2 - i * e4 + 4 * g 5 * hi
  have h6 : (8 : K) * g 6 = 0 := by linear_combination e3 - i * e7 + 4 * g 6 * hi
  have h4 : (8 : K) * g 4 = 0 := by linear_combination e5 - i * e6 + 4 * g 4 * hi
  have g7 : g 7 = 0 := (mul_eq_zero.mp h7).resolve_left (by norm_num)
  have g5 : g 5 = 0 := (mul_eq_zero.mp h5).resolve_left (by norm_num)
  have g6 : g 6 = 0 := (mul_eq_zero.mp h6).resolve_left (by norm_num)
  have g4 : g 4 = 0 := (mul_eq_zero.mp h4).resolve_left (by norm_num)
  have g0 : g 0 = 0 := by linear_combination e0 + 8 * i * g7
  have g2 : (2 : K) * g 2 = 0 := by linear_combination e4 - 4 * i * g5
  have g3 : (2 : K) * g 3 = 0 := by linear_combination e7 - 4 * i * g6
  have g1 : (2 : K) * g 1 = 0 := by linear_combination e6 - 4 * i * g4
  intro k
  fin_cases k
  · exact g0
  · exact (mul_eq_zero.mp g1).resolve_left two
  · exact (mul_eq_zero.mp g2).resolve_left two
  · exact (mul_eq_zero.mp g3).resolve_left two
  · exact g4
  · exact g5
  · exact g6
  · exact g7

/-! ## B. The `su(3)` action -/

/-- Base change of a ℚ-linear endomorphism of `𝕆_ℚ` to `𝕆_K`. -/
noncomputable def extD (D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) : (Fin 8 → K) →ₗ[K] (Fin 8 → K) :=
  Matrix.mulVecLin ((LinearMap.toMatrix' D).map (algebraMap ℚ K))

theorem extD_map (D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) (u : Fin 8 → ℚ) :
    extD D ((algebraMap ℚ K) ∘ u) = (algebraMap ℚ K) ∘ D u := by
  funext k
  simp only [extD, Matrix.mulVecLin_apply, Function.comp_apply]
  rw [← RingHom.map_mulVec, LinearMap.toMatrix'_mulVec]

theorem map_single (j : Fin 8) :
    (algebraMap ℚ K) ∘ (Pi.single j 1 : Fin 8 → ℚ) = Pi.single j 1 := by
  funext k; by_cases h : k = j <;> simp [Pi.single_apply, h]

/-- The octonion product as a `K`-bilinear map. -/
def omulₗ : (Fin 8 → K) →ₗ[K] (Fin 8 → K) →ₗ[K] (Fin 8 → K) :=
  LinearMap.mk₂ K omul omul_add_left omul_smul_left omul_add_right
    (fun c m n => omul_smul_right m c n)

/-- **Base change preserves the Leibniz rule.** -/
theorem extD_leibniz {D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)} (hD : D ∈ Der𝕆)
    (u v : Fin 8 → K) :
    extD D (omul u v) = omul (extD D u) v + omul u (extD D v) := by
  have hleib : ∀ x y : Fin 8 → ℚ, D (octMul x y) = octMul (D x) y + octMul x (D y) := by
    intro x y; simpa using mem_ker_leibnizDefect_iff.mp hD x y
  have key : (omulₗ (K := K)).compr₂ (extD D) =
      (omulₗ (K := K)).comp (extD D) + (omulₗ (K := K)).compl₂ (extD D) := by
    refine LinearMap.ext_basis (Pi.basisFun K (Fin 8)) (Pi.basisFun K (Fin 8)) fun a b => ?_
    simp only [Pi.basisFun_apply, LinearMap.compr₂_apply, LinearMap.add_apply,
      LinearMap.comp_apply, LinearMap.compl₂_apply]
    simp only [omulₗ, LinearMap.mk₂_apply]
    rw [← map_single (K := K) a, ← map_single (K := K) b, omul_map, extD_map, extD_map,
      extD_map, omul_map, omul_map, hleib]
    funext k; simp
  have := LinearMap.congr_fun₂ key u v
  simpa [omulₗ] using this

/-- `stdIm` base-changes to `eOne`. -/
theorem map_stdIm : (algebraMap ℚ K) ∘ stdIm = (eOne : Fin 8 → K) := by
  funext k; fin_cases k <;> simp [stdIm, eOne]

theorem extD_one {D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)} (hD : D ∈ Der𝕆) :
    extD D (Pi.single 0 1 : Fin 8 → K) = 0 := by
  rw [← map_single, extD_map, derivation_annihilates_one hD]; funext k; simp

theorem extD_eOne {D : Der𝕆} (hD : D ∈ su3 stdIm) : extD D.1 (eOne : Fin 8 → K) = 0 := by
  rw [← map_stdIm, extD_map, mem_su3_iff.mp hD]; funext k; simp

/-- **The colour algebra commutes with the `e₁`-complex structure** on `𝕆_K`. -/
theorem extD_comm_Le {D : Der𝕆} (hD : D ∈ su3 stdIm) (x : Fin 8 → K) :
    extD D.1 (omul eOne x) = omul eOne (extD D.1 x) := by
  rw [extD_leibniz D.2, extD_eOne hD]
  have : omul (0 : Fin 8 → K) x = 0 := by funext k; fin_cases k <;> simp [omul]
  rw [this, zero_add]

theorem vac_decomp : (vac i : Fin 8 → K) = Pi.single 0 1 + i • eOne := by
  funext k; fin_cases k <;> simp [vac, eOne]

theorem fock7_decomp : (fock i 7 : Fin 8 → K) = (-8 * i) • (Pi.single 0 1 : Fin 8 → K) + (-8 : K) • eOne := by
  funext k; fin_cases k <;> simp [fock, eOne]

/-- **Singlets**: `su(3)` kills `ν = Ω` (level 0). -/
theorem extD_su3_kills_fock0 {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    extD D.1 (fock i 0 : Fin 8 → K) = 0 := by
  rw [fock_zero, vac_decomp, map_add, map_smul, extD_one D.2, extD_eOne hD]; simp

/-- **Singlets**: `su(3)` kills `e⁺` (level 3). -/
theorem extD_su3_kills_fock7 {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    extD D.1 (fock i 7 : Fin 8 → K) = 0 := by
  rw [fock7_decomp, map_add, map_smul, map_smul, extD_one D.2, extD_eOne hD]; simp

/-- A derivation has no `e₀`-component on an imaginary unit (ℚ-side). -/
theorem der_comp0 {D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)} (hD : D ∈ Der𝕆) (m : Fin 8)
    (hm : m ≠ 0) : D (Pi.single m 1) 0 = 0 := by
  have hleib := mem_ker_leibnizDefect_iff.mp hD (Pi.single m 1) (Pi.single m 1)
  simp only [octMulₗ_apply] at hleib
  have h1 := derivation_annihilates_one hD
  have hsq : octMul (Pi.single m 1) (Pi.single m 1) = -(Pi.single 0 1 : Fin 8 → ℚ) := by
    funext k; fin_cases m <;> fin_cases k <;> simp [octMul] <;> exact absurd rfl hm
  rw [hsq, map_neg, h1, neg_zero] at hleib
  have hc := congrFun hleib m
  set y := D (Pi.single m 1) with hy
  clear_value y
  fin_cases m
  · exact absurd rfl hm
  all_goals (simp [octMul] at hc; linarith)

/-- A derivation fixing `e₁` has no `e₁`-component on `e_m`, `m ≥ 2` (ℚ-side). -/
theorem der_comp1 {D : Der𝕆} (hD : D ∈ su3 stdIm) (m : Fin 8) (hm0 : m ≠ 0) (hm1 : m ≠ 1) :
    D.1 (Pi.single m 1) 1 = 0 := by
  have hl1 := mem_ker_leibnizDefect_iff.mp D.2 stdIm (Pi.single m 1)
  have hl2 := mem_ker_leibnizDefect_iff.mp D.2 (Pi.single m 1) stdIm
  simp only [octMulₗ_apply] at hl1 hl2
  have he : D.1 stdIm = 0 := mem_su3_iff.mp hD
  have hanti : octMul stdIm (Pi.single m 1) + octMul (Pi.single m 1) stdIm = 0 := by
    funext k; fin_cases m <;> fin_cases k <;> simp [octMul, stdIm] <;>
      first | exact absurd rfl hm0 | exact absurd rfl hm1
  have h := congrArg D.1 hanti
  rw [map_add, hl1, hl2, he, map_zero] at h
  have hc := congrFun h 0
  set y := D.1 (Pi.single m 1) with hy
  clear_value y
  fin_cases m
  · exact absurd rfl hm0
  · exact absurd rfl hm1
  all_goals (simp [octMul, stdIm] at hc; linarith)

theorem toMatrix'_entry (D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) (r m : Fin 8) :
    LinearMap.toMatrix' D r m = D (Pi.single m 1) r := by
  rw [LinearMap.toMatrix'_apply]
  have e : (fun j' => if j' = m then (1 : ℚ) else 0) = Pi.single m 1 := by
    funext j'
    by_cases h : j' = m
    · subst h; simp
    · simp [Pi.single_apply, h]
  rw [e]

/-- The level subspaces of the imaginary part: `L(e₁) = s` on `Im 𝕆 ∩ span(e₂..e₇)`. -/
def levelSpace (s : K) : Set (Fin 8 → K) := {x | x 0 = 0 ∧ x 1 = 0 ∧ omul eOne x = s • x}

theorem fock_mem_level1 (hi : i * i = -1) (k : Fin 8) (hk : k = 1 ∨ k = 2 ∨ k = 3) :
    fock i k ∈ levelSpace i := by
  refine ⟨?_, ?_, ?_⟩
  · rcases hk with rfl | rfl | rfl <;> simp [fock]
  · rcases hk with rfl | rfl | rfl <;> simp [fock]
  · rw [Le_fock hi]; rcases hk with rfl | rfl | rfl <;> simp [level]

theorem fock_mem_level2 (hi : i * i = -1) (k : Fin 8) (hk : k = 4 ∨ k = 5 ∨ k = 6) :
    fock i k ∈ levelSpace (-i) := by
  refine ⟨?_, ?_, ?_⟩
  · rcases hk with rfl | rfl | rfl <;> simp [fock]
  · rcases hk with rfl | rfl | rfl <;> simp [fock]
  · rw [Le_fock hi]; rcases hk with rfl | rfl | rfl <;> simp [level, pow_succ, neg_smul]

/-- On a vector with `x₀ = x₁ = 0`, the base-changed colour derivation keeps `x₀ = x₁ = 0`. -/
theorem extD_su3_imag {D : Der𝕆} (hD : D ∈ su3 stdIm) {x : Fin 8 → K} (h0 : x 0 = 0)
    (h1 : x 1 = 0) : extD D.1 x 0 = 0 ∧ extD D.1 x 1 = 0 := by
  have c0 : ∀ m : Fin 8, m ≠ 0 → LinearMap.toMatrix' D.1 0 m = 0 := fun m hm => by
    rw [toMatrix'_entry]; exact der_comp0 D.2 m hm
  have c1 : ∀ m : Fin 8, m ≠ 0 → m ≠ 1 → LinearMap.toMatrix' D.1 1 m = 0 := fun m h0 h1 => by
    rw [toMatrix'_entry]; exact der_comp1 hD m h0 h1
  have hD0 : LinearMap.toMatrix' D.1 0 0 = 0 := by
    rw [toMatrix'_entry, derivation_annihilates_one D.2]; rfl
  constructor
  · simp only [extD, Matrix.mulVecLin_apply, Matrix.mulVec, dotProduct, Fin.sum_univ_eight,
      Matrix.map_apply]
    rw [h0, h1, c0 2 (by decide), c0 3 (by decide), c0 4 (by decide), c0 5 (by decide),
      c0 6 (by decide), c0 7 (by decide)]
    simp
  · simp only [extD, Matrix.mulVecLin_apply, Matrix.mulVec, dotProduct, Fin.sum_univ_eight,
      Matrix.map_apply]
    rw [h0, h1, c1 2 (by decide) (by decide), c1 3 (by decide) (by decide),
      c1 4 (by decide) (by decide), c1 5 (by decide) (by decide), c1 6 (by decide) (by decide),
      c1 7 (by decide) (by decide)]
    simp

/-- **`su(3)` preserves each level space** (levels 1 and 2 are `levelSpace i`,
`levelSpace (−i)`). -/
theorem extD_su3_mem_levelSpace {D : Der𝕆} (hD : D ∈ su3 stdIm) (s : K) {x : Fin 8 → K}
    (hx : x ∈ levelSpace s) : extD D.1 x ∈ levelSpace s := by
  obtain ⟨h0, h1, hL⟩ := hx
  obtain ⟨c0, c1⟩ := extD_su3_imag hD h0 h1
  refine ⟨c0, c1, ?_⟩
  rw [← extD_comm_Le hD, hL, map_smul]

/-! Two explicit members of `su3 e₁`, from the corpus 𝔤₂ basis. -/

theorem octDer6_mem : octDer 6 ∈ su3 stdIm := by
  rw [mem_su3_iff]; funext k
  fin_cases k <;> simp [octDer, octDerMat, stdIm, Matrix.mulVec, dotProduct, Fin.sum_univ_eight]

theorem octDer9_mem : octDer 9 ∈ su3 stdIm := by
  rw [mem_su3_iff]; funext k
  fin_cases k <;> simp [octDer, octDerMat, stdIm, Matrix.mulVec, dotProduct, Fin.sum_univ_eight]

theorem extD_octDer (k : Fin 14) :
    extD (K := K) (octDer k).1 = Matrix.mulVecLin ((octDerMat k).map (algebraMap ℚ K)) := by
  simp only [extD, octDer]
  rw [show Matrix.mulVecLin (octDerMat k) = Matrix.toLin' (octDerMat k) from rfl,
    LinearMap.toMatrix'_toLin']

/-- **The `su(3)`-invariant vectors are exactly `span(e₀, e₁)` = `span(ν, e⁺)`.** -/
theorem su3_invariant_iff (x : Fin 8 → K) :
    (∀ D : Der𝕆, D ∈ su3 stdIm → extD D.1 x = 0) ↔
      ∀ m : Fin 8, m ≠ 0 → m ≠ 1 → x m = 0 := by
  constructor
  · intro h
    have h6 := h _ octDer6_mem
    have h9 := h _ octDer9_mem
    rw [extD_octDer] at h6 h9
    have a := fun k => congrFun h6 k
    have b := fun k => congrFun h9 k
    have a2 := a 2; have a4 := a 4; have a5 := a 5; have a6 := a 6
    have b2 := b 2; have b3 := b 3; have b4 := b 4; have b7 := b 7
    simp [octDerMat, Matrix.mulVec, dotProduct, Fin.sum_univ_eight] at a2 a4 a5 a6 b2 b3 b4 b7
    clear h h6 h9 a b
    intro m hm0 hm1
    fin_cases m
    · exact absurd rfl hm0
    · exact absurd rfl hm1
    all_goals (first | exact a2 | exact a4 | exact a5 | exact a6 | exact b2 | exact b4)
  · intro h D hD
    have hx : x = x 0 • (Pi.single 0 1 : Fin 8 → K) + x 1 • eOne := by
      funext m
      fin_cases m <;> simp [eOne] <;> exact h _ (by decide) (by decide)
    rw [hx, map_add, map_smul, map_smul, extD_one D.2, extD_eOne hD]; simp

/-! ## C. The forced-embedding test -/

variable (i) in
/-- The canonical `ℤ/2`-grading of `S_u ≅ 𝕆_K`: `G = i · L(e₁)`. -/
def G (x : Fin 8 → K) : Fin 8 → K := i • omul eOne x

theorem G_sq (hi : i * i = -1) (x : Fin 8 → K) : G i (G i x) = x := by
  funext k; fin_cases k <;> simp [G, omul, eOne] <;> linear_combination (-(x _)) * hi

/-- **`G = (−1)^N`** on Furey's eight states. -/
theorem G_fock (hi : i * i = -1) (k : Fin 8) :
    G i (fock i k) = ((-1 : K) ^ level k) • fock i k := by
  rw [G, Le_fock hi, smul_smul]
  congr 1
  rw [pow_succ]; linear_combination (-((-1 : K) ^ level k)) * hi

/-- The opposite root negates the grading (Galois). -/
theorem G_neg_root (x : Fin 8 → K) : G (-i) x = -G i x := by simp [G]

theorem G_smul (c : K) (x : Fin 8 → K) : G i (c • x) = c • G i x := by
  simp only [G, omul_smul_right, smul_smul, mul_comm]

/-- The `S_d` vacuum `Ω' = vac(−i)` is `G`-ODD, while the `S_u` vacuum is `G`-even. -/
theorem G_vacD (hi : i * i = -1) : G i (vacD i) = -vacD i := by
  funext k; fin_cases k <;> simp [G, vacD, vac, omul, eOne] <;> linear_combination hi

/-- **Colour-blind data can only land in the lepton singlets.** Any `K`-linear map from a
module with trivial `su(3)` action that is `su(3)`-equivariant takes values in
`span(ν, e⁺)`, i.e. has zero quark-level (1, 2) components. -/
theorem colourBlind_lands_in_singlets {M : Type*} [AddCommGroup M] [Module K M]
    (f : M →ₗ[K] (Fin 8 → K)) (hcol : ∀ D : Der𝕆, D ∈ su3 stdIm → ∀ m, extD D.1 (f m) = 0)
    (m : M) : ∀ k : Fin 8, k ≠ 0 → k ≠ 1 → f m k = 0 :=
  (su3_invariant_iff (f m)).mp fun D hD => hcol D hD m

/-- **Forced chirality embedding — unique up to a scalar per line.** If such an `f` also
intertwines a tower grading `J` with `G`, the `J = +1` line goes into `K·ν` and the `J = −1`
line into `K·e⁺`. -/
theorem forced_chirality_embedding (hi : i * i = -1) {M : Type*} [AddCommGroup M] [Module K M]
    (J : M →ₗ[K] M) (f : M →ₗ[K] (Fin 8 → K))
    (hcol : ∀ D : Der𝕆, D ∈ su3 stdIm → ∀ m, extD D.1 (f m) = 0)
    (hJ : ∀ m, f (J m) = G i (f m)) (m : M) :
    (J m = m → ∃ c : K, f m = c • fock i 0) ∧ (J m = -m → ∃ c : K, f m = c • fock i 7) := by
  have hs := colourBlind_lands_in_singlets f hcol m
  set x := f m with hxdef
  have hx : x = x 0 • (Pi.single 0 1 : Fin 8 → K) + x 1 • eOne := by
    funext k
    fin_cases k <;> simp [eOne] <;> exact hs _ (by decide) (by decide)
  have hG : G i x = (-(i * x 1)) • (Pi.single 0 1 : Fin 8 → K) + (i * x 0) • eOne := by
    conv_lhs => rw [hx]
    funext k; fin_cases k <;> simp [G, omul, eOne] <;> ring
  constructor
  · intro hJm
    have hfix : G i x = x := by rw [← hJ, hJm]
    have e0 := congrFun hfix 0
    rw [hG] at e0; simp [eOne] at e0
    refine ⟨x 0, ?_⟩
    rw [hx]; funext k; fin_cases k <;> simp [fock, eOne]
    first | linear_combination i * e0 + x 1 * hi | linear_combination -(i * e0 + x 1 * hi) |
      linear_combination (-i) * e0 - x 1 * hi | linear_combination i * e0 - x 1 * hi
  · intro hJm
    have hneg : G i x = -x := by rw [← hJ, hJm, map_neg]
    have e0 := congrFun hneg 0
    rw [hG] at e0; simp [eOne] at e0
    refine ⟨-(x 1) / 8, ?_⟩
    rw [hx]; funext k; fin_cases k <;> simp [fock, eOne]
    all_goals first | ring1 | (field_simp; ring1) | linear_combination e0 |
      linear_combination -e0 | (field_simp; linear_combination e0) |
      (field_simp; linear_combination -e0) | (field_simp; linear_combination 8 * e0) |
      (field_simp; linear_combination -8 * e0)

/-- **Flavour obstruction.** No chirality-blind (`G`-commuting) operator carries the `S_u`
vacuum onto a nonzero multiple of the `S_d` vacuum: Furey's `S_u ↔ S_d` exchange is `G`-odd,
whereas the tower flavour flip `σ ↔ σ⁻¹` fixes both eigenlines (is `J`-even). -/
theorem flavour_obstruction (hi : i * i = -1) (T : (Fin 8 → K) →ₗ[K] (Fin 8 → K))
    (hT : ∀ x, T (G i x) = G i (T x)) (c : K) (h : T (vac i) = c • vacD i) : c = 0 := by
  have hv : G i (vac i) = vac i := by
    have := G_fock hi 0; simpa [level, fock_zero] using this
  have h1 : G i (T (vac i)) = T (vac i) := by rw [← hT, hv]
  rw [h, G_smul, G_vacD hi] at h1
  have h2 := congrFun h1 0
  simp [vacD, vac] at h2
  first
    | exact h2
    | (have h3 : (2 : K) * c = 0 := by linear_combination -h2
       exact (mul_eq_zero.mp h3).resolve_left two_ne_zero)
    | (have h3 : (2 : K) * c = 0 := by linear_combination h2
       exact (mul_eq_zero.mp h3).resolve_left two_ne_zero)

/-- **The tower's chirality selector cannot see the root `i`.** The left line is selected
by `|eigenvalue| > 1` (`LeftLineDefinition`), which needs an ORDERED field, and an ordered
field has no square root of `−1`. So tower data lives over an ordered subfield, is fixed by
`i ↦ −i`, while `G` changes sign (`G_neg_root`): no tower structure breaks the swap. -/
theorem no_sqrt_neg_one_of_ordered {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (j : F) : j * j ≠ -1 := by
  intro h
  have := mul_self_nonneg j
  rw [h] at this
  linarith

end Field

end QOU.Eightfold.FureyIdeal
