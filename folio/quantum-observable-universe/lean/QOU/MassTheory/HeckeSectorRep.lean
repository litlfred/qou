import QOU.MassTheory.PhotonPairReachability
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import QOU.MassTheory.PhotonPairNoFactorSector

/-!
# The one-marked-strand sector is a representation of the Hecke algebra

`PhotonPairReachability` defines the operators `sig q qi i` on `ℕ → K` (the one-marked-strand
sector of the Jimbo representation) and proves the Hecke relations for them. The no-two-photon
theorems (`PhotonPairNoFactor`, `PhotonPairNoFactorSector`) are stated on that sector. This file
closes the gap to the abstract algebra: it presents the Hecke algebra by generators and relations,

  `H(q) = K⟨σ₀, σ₁, …⟩ / (σᵢ² = (q − qi)σᵢ + 1,  σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁,  σᵢσₖ = σₖσᵢ for k ≥ i+2)`,

builds the algebra map `rep : H(q) →ₐ End(ℕ → K)` with `σᵢ ↦ sig i`, and proves

* `rep_photon`, `rep_word`: `rep` sends the abstract photon and γγ word to the sector operators;
* `transfer`: if `γᵢγⱼ = μ·w` fails on the sector, it fails in `H(q)`.

`noPair_V1V0V1_1_0_H6` shows the use: each sector theorem transfers in one line.

`Hn` is the algebra on generators `σ₀ … σₙ₋₂`, and `Hn.toHecke` maps it to `H(q)`, so a
relation `γᵢγⱼ = μ·w` in `H₆(q)` would give one in `H(q)` (`transfer_Hn`).

Generic commutative ring `K`, with `q·qi = 1`. No ordering, no `ℝ`.
-/

namespace QOU.MassTheory.HeckeSectorRep

open QOU.MassTheory.PhotonPairReachability

variable {K : Type*} [CommRing K]

/-- The defining relations of the Hecke algebra on generators indexed by `ℕ`. -/
inductive HeckeRel (q qi : K) : FreeAlgebra K ℕ → FreeAlgebra K ℕ → Prop
  | quad (i : ℕ) : HeckeRel q qi (FreeAlgebra.ι K i * FreeAlgebra.ι K i)
      ((q - qi) • FreeAlgebra.ι K i + 1)
  | braid (i : ℕ) : HeckeRel q qi
      (FreeAlgebra.ι K i * FreeAlgebra.ι K (i + 1) * FreeAlgebra.ι K i)
      (FreeAlgebra.ι K (i + 1) * FreeAlgebra.ι K i * FreeAlgebra.ι K (i + 1))
  | comm (i k : ℕ) (h : i + 2 ≤ k) : HeckeRel q qi
      (FreeAlgebra.ι K i * FreeAlgebra.ι K k) (FreeAlgebra.ι K k * FreeAlgebra.ι K i)

/-- The Hecke algebra `H(q)` on infinitely many strands. -/
abbrev Hecke (q qi : K) := RingQuot (HeckeRel q qi)

/-- The generator `σᵢ`. -/
def gen (q qi : K) (i : ℕ) : Hecke q qi := RingQuot.mkAlgHom K (HeckeRel q qi) (FreeAlgebra.ι K i)

/-- `σᵢ⁻¹ = σᵢ − (q − qi)`. -/
def genInv (q qi : K) (i : ℕ) : Hecke q qi := gen q qi i - algebraMap K _ (q - qi)

theorem gen_sq (q qi : K) (i : ℕ) : gen q qi i * gen q qi i = (q - qi) • gen q qi i + 1 := by
  unfold gen
  rw [← map_mul, RingQuot.mkAlgHom_rel K (HeckeRel.quad i), map_add, map_smul, map_one]

/-- `σᵢ⁻¹` is the inverse of `σᵢ`. -/
theorem gen_mul_genInv (q qi : K) (i : ℕ) : gen q qi i * genInv q qi i = 1 := by
  unfold genInv
  rw [mul_sub, gen_sq, ← Algebra.commutes, ← Algebra.smul_def]; abel

/-- The abstract photon `γᵢ(a, b, c) = 1 + a·σᵢ + b·σᵢ₊₁ + c·σᵢσᵢ₊₁⁻¹`. -/
def photonH (q qi a b c : K) (i : ℕ) : Hecke q qi :=
  1 + a • gen q qi i + b • gen q qi (i + 1) + c • (gen q qi i * genInv q qi (i + 1))

/-- A braid word: `(k, true)` is `σₖ`, `(k, false)` is `σₖ⁻¹`, read left to right. -/
def wordH (q qi : K) : List (ℕ × Bool) → Hecke q qi
  | [] => 1
  | (k, true) :: w => gen q qi k * wordH q qi w
  | (k, false) :: w => genInv q qi k * wordH q qi w

/-- `sig i` as a linear map. -/
def sigL (q qi : K) (i : ℕ) : Module.End K (ℕ → K) where
  toFun := sig q qi i
  map_add' v w := by
    funext p; simp only [sig, Pi.add_apply]; split_ifs <;> ring
  map_smul' c v := by
    funext p; simp only [sig, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; split_ifs <;> ring

theorem sigL_apply (q qi : K) (i : ℕ) (v : ℕ → K) : sigL q qi i v = sig q qi i v := rfl

/-- **The sector representation** `H(q) → End(ℕ → K)`, `σᵢ ↦ sig i`. -/
def rep (q qi : K) (hqi : q * qi = 1) : Hecke q qi →ₐ[K] Module.End K (ℕ → K) :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K (sigL q qi), by
    intro x y h
    cases h with
    | quad i =>
      apply LinearMap.ext; intro v
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply,
        Module.End.mul_apply, LinearMap.add_apply, LinearMap.smul_apply, Module.End.one_apply,
        sigL_apply]
      rw [sig_quadratic q qi hqi i v]; funext p; simp [smul_eq_mul]
    | braid i =>
      apply LinearMap.ext; intro v
      simp only [map_mul, FreeAlgebra.lift_ι_apply, Module.End.mul_apply, sigL_apply]
      exact sig_braid q qi hqi i v
    | comm i k hik =>
      apply LinearMap.ext; intro v
      simp only [map_mul, FreeAlgebra.lift_ι_apply, Module.End.mul_apply, sigL_apply]
      exact sig_comm q qi i k hik v⟩

theorem rep_gen (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    rep q qi hqi (gen q qi i) v = sig q qi i v := by
  simp [rep, gen, sigL_apply]

/-- In the sector, `σᵢ⁻¹ = σᵢ − (q − qi)` is `sigInv`. -/
theorem sigInv_eq (q qi : K) (i : ℕ) (v : ℕ → K) :
    sigInv q qi i v = fun p => sig q qi i v p - (q - qi) * v p := by
  funext p
  simp only [sig, sigInv]
  split_ifs <;> subst_vars <;> first | omega | ring

theorem rep_genInv (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    rep q qi hqi (genInv q qi i) v = sigInv q qi i v := by
  rw [sigInv_eq q qi]
  funext p
  simp [genInv, rep_gen, Algebra.algebraMap_eq_smul_one, smul_eq_mul]

theorem rep_photon (q qi : K) (hqi : q * qi = 1) (a b c : K) (i : ℕ) (v : ℕ → K) :
    rep q qi hqi (photonH q qi a b c i) v = photon q qi a b c i v := by
  funext p
  simp [photonH, photon, rep_gen, rep_genInv, smul_eq_mul, add_assoc]

theorem rep_word (q qi : K) (hqi : q * qi = 1) (w : List (ℕ × Bool)) (v : ℕ → K) :
    rep q qi hqi (wordH q qi w) v = wordAct q qi w v := by
  induction w with
  | nil => simp [wordH, wordAct]
  | cons x w ih =>
    obtain ⟨k, s⟩ := x
    cases s
    · simp [wordH, wordAct, Module.End.mul_apply, rep_genInv, ih]
    · simp [wordH, wordAct, Module.End.mul_apply, rep_gen, ih]

/-- **Transfer.** If `γᵢγⱼ = μ·w` fails on the one-marked-strand sector, it fails in `H(q)`. -/
theorem transfer (q qi : K) (hqi : q * qi = 1) (a b c a' b' c' μ : K) (i j : ℕ)
    (w : List (ℕ × Bool))
    (hsec : ¬ ∀ v, photon q qi a b c i (photon q qi a' b' c' j v) =
      fun p => μ * wordAct q qi w v p) :
    photonH q qi a b c i * photonH q qi a' b' c' j ≠ μ • wordH q qi w := by
  intro heq
  apply hsec
  intro v
  have := congrArg (fun x => rep q qi hqi x v) heq
  simp only [map_mul, map_smul, Module.End.mul_apply, LinearMap.smul_apply, rep_photon,
    rep_word] at this
  rw [this]; funext p; simp [smul_eq_mul]

/-! ### The finite Hecke algebras `Hₙ(q)` map to `H(q)` -/

/-- The relations of `Hₙ(q)` on generators `σ₀ … σₙ₋₂`, indexed by `ℕ` with `i + 1 < n`. -/
inductive HeckeRelN (n : ℕ) (q qi : K) :
    FreeAlgebra K {i : ℕ // i + 1 < n} → FreeAlgebra K {i : ℕ // i + 1 < n} → Prop
  | quad (i) : HeckeRelN n q qi (FreeAlgebra.ι K i * FreeAlgebra.ι K i)
      ((q - qi) • FreeAlgebra.ι K i + 1)
  | braid (i j : {i : ℕ // i + 1 < n}) (hj : j.1 = i.1 + 1) : HeckeRelN n q qi
      (FreeAlgebra.ι K i * FreeAlgebra.ι K j * FreeAlgebra.ι K i)
      (FreeAlgebra.ι K j * FreeAlgebra.ι K i * FreeAlgebra.ι K j)
  | comm (i k : {i : ℕ // i + 1 < n}) (h : i.1 + 2 ≤ k.1) : HeckeRelN n q qi
      (FreeAlgebra.ι K i * FreeAlgebra.ι K k) (FreeAlgebra.ι K k * FreeAlgebra.ι K i)

/-- `Hₙ(q)`. -/
abbrev Hn (n : ℕ) (q qi : K) := RingQuot (HeckeRelN n q qi)

/-- The algebra map `Hₙ(q) → H(q)`, `σᵢ ↦ σᵢ`. -/
def Hn.toHecke (n : ℕ) (q qi : K) : Hn n q qi →ₐ[K] Hecke q qi :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K (fun i => gen q qi i.1), by
    intro x y h
    cases h with
    | quad i =>
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
      exact gen_sq q qi i.1
    | braid i j hj =>
      rw [map_mul, map_mul, map_mul, map_mul]
      simp only [FreeAlgebra.lift_ι_apply, hj]
      have e := RingQuot.mkAlgHom_rel K (@HeckeRel.braid K _ q qi i.1)
      simpa only [map_mul, HeckeSectorRep.gen] using e
    | comm i k h =>
      rw [map_mul, map_mul]
      simp only [FreeAlgebra.lift_ι_apply]
      have e := RingQuot.mkAlgHom_rel K (@HeckeRel.comm K _ q qi i.1 k.1 h)
      simpa only [map_mul, HeckeSectorRep.gen] using e⟩

/-- The generator `σᵢ` of `Hₙ(q)` (zero when `i + 1 ≥ n`, never used there). -/
def Hn.gen (n : ℕ) (q qi : K) (i : ℕ) : Hn n q qi :=
  if h : i + 1 < n then RingQuot.mkAlgHom K (HeckeRelN n q qi) (FreeAlgebra.ι K ⟨i, h⟩) else 0

theorem Hn.toHecke_gen (n : ℕ) (q qi : K) (i : ℕ) (h : i + 1 < n) :
    Hn.toHecke n q qi (Hn.gen n q qi i) = HeckeSectorRep.gen q qi i := by
  simp [Hn.gen, h, Hn.toHecke, HeckeSectorRep.gen]

/-- `σᵢ⁻¹` in `Hₙ(q)`. -/
def Hn.genInv (n : ℕ) (q qi : K) (i : ℕ) : Hn n q qi := Hn.gen n q qi i - algebraMap K _ (q - qi)

/-- The photon in `Hₙ(q)`. -/
def Hn.photon (n : ℕ) (q qi a b c : K) (i : ℕ) : Hn n q qi :=
  1 + a • Hn.gen n q qi i + b • Hn.gen n q qi (i + 1) +
    c • (Hn.gen n q qi i * Hn.genInv n q qi (i + 1))

/-- A braid word in `Hₙ(q)`. -/
def Hn.word (n : ℕ) (q qi : K) : List (ℕ × Bool) → Hn n q qi
  | [] => 1
  | (k, true) :: w => Hn.gen n q qi k * Hn.word n q qi w
  | (k, false) :: w => Hn.genInv n q qi k * Hn.word n q qi w

theorem Hn.toHecke_photon (n : ℕ) (q qi a b c : K) (i : ℕ) (h : i + 2 < n) :
    Hn.toHecke n q qi (Hn.photon n q qi a b c i) = photonH q qi a b c i := by
  simp [Hn.photon, photonH, Hn.genInv, HeckeSectorRep.genInv, Hn.toHecke_gen n q qi i (by omega),
    Hn.toHecke_gen n q qi (i + 1) (by omega)]

theorem Hn.toHecke_word (n : ℕ) (q qi : K) (w : List (ℕ × Bool))
    (hw : ∀ x ∈ w, x.1 + 1 < n) : Hn.toHecke n q qi (Hn.word n q qi w) = wordH q qi w := by
  induction w with
  | nil => simp [Hn.word, wordH]
  | cons x w ih =>
    obtain ⟨k, s⟩ := x
    have hk : k + 1 < n := hw (k, s) (List.mem_cons_self ..)
    have ih' := ih (fun y hy => hw y (List.mem_cons_of_mem _ hy))
    cases s
    · simp [Hn.word, wordH, Hn.genInv, HeckeSectorRep.genInv, Hn.toHecke_gen n q qi k hk, ih']
    · simp [Hn.word, wordH, Hn.toHecke_gen n q qi k hk, ih']

/-- **Transfer to `Hₙ(q)`.** If `γᵢγⱼ = μ·w` fails on the sector, it fails in `Hₙ(q)` whenever
the photons and the word fit on `n` strands. -/
theorem transfer_Hn (n : ℕ) (q qi : K) (hqi : q * qi = 1) (a b c a' b' c' μ : K) (i j : ℕ)
    (hi : i + 2 < n) (hj : j + 2 < n) (w : List (ℕ × Bool)) (hw : ∀ x ∈ w, x.1 + 1 < n)
    (hsec : ¬ ∀ v, photon q qi a b c i (photon q qi a' b' c' j v) =
      fun p => μ * wordAct q qi w v p) :
    Hn.photon n q qi a b c i * Hn.photon n q qi a' b' c' j ≠ μ • Hn.word n q qi w := by
  intro heq
  apply transfer q qi hqi a b c a' b' c' μ i j w hsec
  have := congrArg (Hn.toHecke n q qi) heq
  simpa [map_mul, map_smul, Hn.toHecke_photon n q qi _ _ _ i hi,
    Hn.toHecke_photon n q qi _ _ _ j hj, Hn.toHecke_word n q qi w hw] using this

/-- Worked use of `transfer_Hn`: the sector result `noPair_V1V0V1_1_0` holds in `H₆(q)` itself. -/
theorem noPair_V1V0V1_1_0_H6 {F : Type*} [Field F] (q qi : F) (hqi : q * qi = 1)
    (hh : q - qi ≠ 0) (a b c a2 b2 c2 μ : F) (hμ : μ ≠ 0) :
    Hn.photon 6 q qi a b c 1 * Hn.photon 6 q qi a2 b2 c2 0 ≠
      μ • Hn.word 6 q qi PhotonPairNoFactorSector.u0 :=
  transfer_Hn 6 q qi hqi a b c a2 b2 c2 μ 1 0 (by norm_num) (by norm_num) _
    (by simp [PhotonPairNoFactorSector.u0])
    (PhotonPairNoFactorSector.noPair_V1V0V1_1_0 q qi hqi hh a b c a2 b2 c2 μ hμ)

end QOU.MassTheory.HeckeSectorRep
