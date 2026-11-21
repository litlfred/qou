/-
  Electron-word candidates: two structural facts that separate them.

  Measurement module for `docs/audits/2026-11-21-electron-word-gs-interactions.md`.
  It decides nothing about which word is the electron; it records two facts the
  study found to separate the candidates `σ₀σ₁σ₀` (the corpus's `e⁻`) and `σ₀³`
  (the trefoil braid in `B₂ ⊂ B₃`).

  1. **Closure parity in `B₃`.** The closure of a braid word on three strands has
     one component per cycle of the word's permutation. Every word of odd length
     permutes the strands by a transposition, so its closure has exactly two
     components. Hence no three-crossing word in `B₃` (in particular neither
     `σ₀σ₁σ₀`, whose closure is the Hopf link, nor `σ₀³`, whose closure is the
     trefoil plus a split unknot) closes to a knot on three strands. Positive
     words of even length close to one or three components.

  2. **`σ₀³` is a rescaled photon.** In any algebra where `σ₀² = h σ₀ + 1`
     (the Hecke relation, `h = q − q⁻¹`), `σ₀³ = h·1 + (h² + 1)·σ₀`; when `h` is a
     unit this is `h · γ((h²+1)/h, 0, 0)` with `γ` the photon of `QOU.Photon`
     (`1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`). So in `H₃(q)` the trefoil braid `σ₀³` lies in
     the single-photon family, while `σ₀σ₁σ₀ = T_{w₀}` is the one standard-basis
     element outside the span of photon terms (measured exactly in
     `computations/probes/electron_word_gs_interactions_probe.py`).

  Generic commutative ring `R` (§7c); the permutation part is pure `Fin 3`
  combinatorics.

  -- Ref: [kassel2008] Kassel & Turaev, Braid Groups, §2.2 (closure components
  --      = cycles of the underlying permutation) and §4.2 (Hecke relation).
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import QOU.Photon

namespace QOU.BraidKnot.ElectronWordCandidates

/-! ### 1. Closure parity in `B₃` -/

/-- The transposition of `Fin 3` underlying the generator `σᵢ` (`i = 0, 1`). -/
def gen (i : Fin 2) (x : Fin 3) : Fin 3 :=
  if i = 0 then (if x = 0 then 1 else if x = 1 then 0 else 2)
  else (if x = 1 then 2 else if x = 2 then 1 else 0)

/-- The permutation of a braid word on three strands. Signs do not matter
    (`σᵢ` and `σᵢ⁻¹` induce the same transposition), so a word is given by its
    letters. -/
def permOf : List (Fin 2) → Fin 3 → Fin 3
  | [] => id
  | i :: w => gen i ∘ permOf w

/-- Number of cycles of a map `Fin 3 → Fin 3`, counted as orbit minima. For a
    permutation this is the number of components of the braid closure. -/
def numCycles (p : Fin 3 → Fin 3) : ℕ :=
  ((List.finRange 3).filter
    (fun i => (List.finRange 3).all (fun k => decide (i ≤ p^[k.val + 1] i)))).length

/-- The six elements of `S₃`, named, with their tables of images. -/
inductive S3 | e | r | r2 | t01 | t12 | t02
  deriving DecidableEq

/-- The table of images of each element of `S₃`. -/
def S3.toFun : S3 → Fin 3 → Fin 3
  | .e => id
  | .r => fun x => if x = 0 then 1 else if x = 1 then 2 else 0
  | .r2 => fun x => if x = 0 then 2 else if x = 1 then 0 else 1
  | .t01 => gen 0
  | .t12 => gen 1
  | .t02 => fun x => if x = 0 then 2 else if x = 1 then 1 else 0

/-- Left multiplication by a generator, as a table on `S3`. -/
def S3.gmul : Fin 2 → S3 → S3
  | 0, .e => .t01 | 0, .r => .t12 | 0, .r2 => .t02
  | 0, .t01 => .e | 0, .t12 => .r | 0, .t02 => .r2
  | 1, .e => .t12 | 1, .r => .t02 | 1, .r2 => .t01
  | 1, .t01 => .r2 | 1, .t12 => .e | 1, .t02 => .r

/-- Every element of `S3`, for finite checks. -/
def S3.all : List S3 := [.e, .r, .r2, .t01, .t12, .t02]

/-- The table `gmul` is composition with the generator's transposition
    (checked pointwise on all 2 × 6 × 3 cases). -/
theorem gmul_correct :
    ∀ i : Fin 2, ∀ p ∈ S3.all, ∀ x : Fin 3,
      (S3.gmul i p).toFun x = gen i (p.toFun x) := by decide

theorem mem_all (p : S3) : p ∈ S3.all := by cases p <;> decide

/-- `true` on the three transpositions. -/
def S3.isOdd : S3 → Bool
  | .t01 | .t12 | .t02 => true
  | _ => false

/-- The word's permutation, computed in `S3`. -/
def permS : List (Fin 2) → S3
  | [] => .e
  | i :: w => S3.gmul i (permS w)

theorem permOf_eq (w : List (Fin 2)) : permOf w = (permS w).toFun := by
  induction w with
  | nil => rfl
  | cons i w ih =>
    funext x
    simp only [permOf, permS, Function.comp, ih]
    exact (gmul_correct i (permS w) (mem_all _) x).symm

theorem gmul_flips : ∀ i : Fin 2, ∀ p ∈ S3.all,
    (S3.gmul i p).isOdd = !p.isOdd := by decide

/-- A word's permutation is a transposition exactly when its length is odd. -/
theorem isOdd_permS (w : List (Fin 2)) : (permS w).isOdd = (w.length % 2 == 1) := by
  induction w with
  | nil => rfl
  | cons i w ih =>
    simp only [permS, List.length_cons]
    rw [gmul_flips i _ (mem_all _), ih]
    rcases Nat.mod_two_eq_zero_or_one w.length with h | h <;>
      simp [h, Nat.add_mod]

theorem numCycles_odd : ∀ p ∈ S3.all, p.isOdd = true → numCycles p.toFun = 2 := by
  decide

theorem numCycles_even : ∀ p ∈ S3.all, p.isOdd = false →
    numCycles p.toFun = 1 ∨ numCycles p.toFun = 3 := by decide

/-- **Odd words close to two components.** Every braid word of odd length in
    `B₃` closes to a two-component link. In particular no word with three
    crossings closes to a knot on three strands. -/
theorem numCycles_permOf_of_odd (w : List (Fin 2)) (hw : w.length % 2 = 1) :
    numCycles (permOf w) = 2 := by
  rw [permOf_eq]
  exact numCycles_odd _ (mem_all _) (by rw [isOdd_permS]; simp [hw])

/-- Even words close to one or three components. -/
theorem numCycles_permOf_of_even (w : List (Fin 2)) (hw : w.length % 2 = 0) :
    numCycles (permOf w) = 1 ∨ numCycles (permOf w) = 3 := by
  rw [permOf_eq]
  exact numCycles_even _ (mem_all _) (by rw [isOdd_permS]; simp [hw])

/-- `σ₀σ₁σ₀` closes to two components (the Hopf link). -/
theorem numCycles_s0s1s0 : numCycles (permOf [0, 1, 0]) = 2 :=
  numCycles_permOf_of_odd _ rfl

/-- `σ₀³` closes to two components on three strands (trefoil ⊔ unknot). -/
theorem numCycles_s0cubed : numCycles (permOf [0, 0, 0]) = 2 :=
  numCycles_permOf_of_odd _ rfl

/-- `(σ₀σ₁)²` closes to one component (the trefoil as `T(3,2)`). -/
theorem numCycles_s0s1_sq : numCycles (permOf [0, 1, 0, 1]) = 1 := by
  rw [permOf_eq]; decide

/-! ### 2. `σ₀³` is a rescaled photon -/

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Under the Hecke relation `σ₀² = h σ₀ + 1`, `σ₀³ = h·1 + (h² + 1)·σ₀`. -/
theorem cube_of_hecke (h : R) (σ₀ : A) (hs : σ₀ * σ₀ = h • σ₀ + 1) :
    σ₀ ^ 3 = h • (1 : A) + (h ^ 2 + 1) • σ₀ := by
  have h3 : σ₀ ^ 3 = σ₀ * (σ₀ * σ₀) := by rw [pow_succ, pow_two, mul_assoc]
  rw [h3, hs, mul_add, mul_one, Algebra.mul_smul_comm, hs, smul_add, smul_smul, add_smul,
    one_smul, ← pow_two]
  abel

/-- When `h` is a unit (inverse `u`), `σ₀³ = h · γ((h² + 1)u, 0, 0)`: the trefoil
    braid is a scalar multiple of a single photon. -/
theorem cube_eq_smul_photon (h u : R) (hu : h * u = 1) (σ₀ : A) (σ₁ : Aˣ)
    (hs : σ₀ * σ₀ = h • σ₀ + 1) :
    σ₀ ^ 3 = h • QOU.Photon.photon σ₀ σ₁ ⟨(h ^ 2 + 1) * u, 0, 0⟩ := by
  rw [cube_of_hecke h σ₀ hs]
  simp only [QOU.Photon.photon, zero_smul, add_zero, smul_add, smul_smul]
  congr 1
  congr 1
  calc h ^ 2 + 1 = (h ^ 2 + 1) * (h * u) := by rw [hu, mul_one]
    _ = h * ((h ^ 2 + 1) * u) := by ring

end QOU.BraidKnot.ElectronWordCandidates
