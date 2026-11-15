import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Hadron.hadron_operations_closure — Closure of hadron operations

The symmetric product `Sym^n(K)` is closed under braiding, Hopf linking,
skein resolution, and fusion.  Each operation preserves the hadron
structure or produces a fused hadron in `Sym^{n₁+n₂}(K)` satisfying:
1. Braiding involution `(braidingOp n ∘ braidingOp n) = id` and alternating-sector sign flip `-1`.
2. Hopf-linking two-sided inverse `hopfLinkOp n (-k) ∘ hopfLinkOp n k = id` and trivial-link identity.
3. Skein resolution idempotence and the linear skein mass decomposition
   `M(H) = Q(q) * M(L_Hopf) + ∑_i M(K_i)`.
4. Fusion associativity across `(n₁ + n₂) + n₃` and mass additivity under `⋆`.

## References

- [leitner2026] Ch. 4, §10
- [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

namespace QOU.Hadron

/-- Concrete carrier for an `n`-constituent hadron state in `Sym^n(K) ⊗ L_Hopf` (`qou-z3k1`). -/
@[ext]
structure HadronState (n : ℕ) where
  /-- Constituent knot masses `(M(K_1), ..., M(K_n))`. -/
  constituents : List ℝ
  /-- Constituent count equals `n`. -/
  length_eq : constituents.length = n
  /-- Net Hopf linking number with `L_Hopf`. -/
  hopfLinkCount : ℤ
  /-- Alternating-sector exchange amplitude. -/
  altAmplitude : ℝ

set_option linter.dupNamespace false in
/-- Alias `Hadron n` for an `n`-constituent hadron state in `Sym^n(K)`. -/
abbrev Hadron (n : ℕ) : Type := HadronState n

/-- Braiding operation on `Sym^n(K)`: reverses constituent order and flips the
    alternating-sector sign (`β|_{alt} = -1`). -/
def braidingOp (n : ℕ) (h : Hadron n) : Hadron n where
  constituents := h.constituents.reverse
  length_eq := by simp [h.length_eq]
  hopfLinkCount := h.hopfLinkCount
  altAmplitude := -h.altAmplitude

/-- Hopf linking endomorphism on `Sym^n(K) ⊗ L_Hopf` shifting the Hopf linking
    number by `k : ℤ`. -/
def hopfLinkOp (n : ℕ) (k : ℤ) (h : Hadron n) : Hadron n where
  constituents := h.constituents
  length_eq := h.length_eq
  hopfLinkCount := h.hopfLinkCount + k
  altAmplitude := h.altAmplitude

/-- Skein resolution on `Sym^n(K)`: projects a linked composite onto its
    unlinked constituent state (`hopfLinkCount = 0`). -/
def skeinOp (n : ℕ) (h : Hadron n) : Hadron n where
  constituents := h.constituents
  length_eq := h.length_eq
  hopfLinkCount := 0
  altAmplitude := h.altAmplitude

/-- Skein mass functional `M(H) = hopfLinkCount * Q(q) * M(L_Hopf) + ∑_i M(K_i)`. -/
def hadronMass {n : ℕ} (Qq mHopf : ℝ) (h : Hadron n) : ℝ :=
  (h.hopfLinkCount : ℝ) * Qq * mHopf + h.constituents.sum

/-- Fusion of two hadrons `Sym^{n₁}(K) × Sym^{n₂}(K) → Sym^{n₁ + n₂}(K)`. -/
def fusionOp (n₁ n₂ : ℕ) (h₁ : Hadron n₁) (h₂ : Hadron n₂) : Hadron (n₁ + n₂) where
  constituents := h₁.constituents ++ h₂.constituents
  length_eq := by simp [h₁.length_eq, h₂.length_eq]
  hopfLinkCount := h₁.hopfLinkCount + h₂.hopfLinkCount
  altAmplitude := h₁.altAmplitude + h₂.altAmplitude

@[simp]
theorem braidingOp_involution (n : ℕ) (h : Hadron n) :
    braidingOp n (braidingOp n h) = h := by
  ext <;> simp [braidingOp]

@[simp]
theorem braidingOp_alt_sign (n : ℕ) (h : Hadron n) :
    (braidingOp n h).altAmplitude = -h.altAmplitude :=
  rfl

@[simp]
theorem hopfLinkOp_left_inv (n : ℕ) (k : ℤ) (h : Hadron n) :
    hopfLinkOp n (-k) (hopfLinkOp n k h) = h := by
  ext <;> simp [hopfLinkOp]

@[simp]
theorem hopfLinkOp_right_inv (n : ℕ) (k : ℤ) (h : Hadron n) :
    hopfLinkOp n k (hopfLinkOp n (-k) h) = h := by
  ext <;> simp [hopfLinkOp]

@[simp]
theorem hopfLinkOp_zero (n : ℕ) (h : Hadron n) :
    hopfLinkOp n 0 h = h := by
  ext <;> simp [hopfLinkOp]

@[simp]
theorem skeinOp_idem (n : ℕ) (h : Hadron n) :
    skeinOp n (skeinOp n h) = skeinOp n h := by
  ext <;> simp [skeinOp]

theorem skein_mass_decomposition (n : ℕ) (Qq mHopf : ℝ) (h : Hadron n) :
    hadronMass Qq mHopf (hopfLinkOp n 1 (skeinOp n h)) =
      Qq * mHopf + h.constituents.sum := by
  simp [hadronMass, hopfLinkOp, skeinOp]

theorem fusionOp_constituents_assoc (n₁ n₂ n₃ : ℕ)
    (h₁ : Hadron n₁) (h₂ : Hadron n₂) (h₃ : Hadron n₃) :
    (fusionOp (n₁ + n₂) n₃ (fusionOp n₁ n₂ h₁ h₂) h₃).constituents =
      (fusionOp n₁ (n₂ + n₃) h₁ (fusionOp n₂ n₃ h₂ h₃)).constituents := by
  simp [fusionOp, List.append_assoc]

theorem fusionOp_mass_add (n₁ n₂ : ℕ) (Qq mHopf : ℝ)
    (h₁ : Hadron n₁) (h₂ : Hadron n₂) :
    hadronMass Qq mHopf (fusionOp n₁ n₂ h₁ h₂) =
      hadronMass Qq mHopf h₁ + hadronMass Qq mHopf h₂ := by
  simp only [hadronMass, fusionOp, List.sum_append, Int.cast_add]
  ring

/-- `Sym^n(K)` is closed under braiding, Hopf linking, skein resolution,
    and fusion, satisfying braiding involution and alternating sign flip,
    Hopf-linking two-sided invertibility, the skein mass decomposition,
    and fusion associativity and mass additivity (`qou-z3k1`). -/
theorem hadron_operations_closure :
    -- (1) Braiding is an involution on Sym^n(K) and flips the alternating sign
    (∀ n (h : Hadron n),
      braidingOp n (braidingOp n h) = h ∧
      (braidingOp n h).altAmplitude = -h.altAmplitude) ∧
    -- (2) Hopf linking has a two-sided inverse and is the identity at linking number 0
    (∀ n (k : ℤ) (h : Hadron n),
      hopfLinkOp n (-k) (hopfLinkOp n k h) = h ∧
      hopfLinkOp n k (hopfLinkOp n (-k) h) = h ∧
      hopfLinkOp n 0 h = h) ∧
    -- (3) Skein resolution is idempotent and yields the linear skein mass formula
    (∀ n (Qq mHopf : ℝ) (h : Hadron n),
      skeinOp n (skeinOp n h) = skeinOp n h ∧
      hadronMass Qq mHopf (hopfLinkOp n 1 (skeinOp n h)) =
        Qq * mHopf + h.constituents.sum) ∧
    -- (4) Fusion is associative on constituents across (n₁ + n₂) + n₃ and additive in mass
    (∀ n₁ n₂ n₃ (Qq mHopf : ℝ) (h₁ : Hadron n₁) (h₂ : Hadron n₂) (h₃ : Hadron n₃),
      (fusionOp (n₁ + n₂) n₃ (fusionOp n₁ n₂ h₁ h₂) h₃).constituents =
        (fusionOp n₁ (n₂ + n₃) h₁ (fusionOp n₂ n₃ h₂ h₃)).constituents ∧
      hadronMass Qq mHopf (fusionOp n₁ n₂ h₁ h₂) =
        hadronMass Qq mHopf h₁ + hadronMass Qq mHopf h₂) := by
  refine ⟨fun n h => ⟨braidingOp_involution n h, braidingOp_alt_sign n h⟩,
          fun n k h => ⟨hopfLinkOp_left_inv n k h, hopfLinkOp_right_inv n k h, hopfLinkOp_zero n h⟩,
          fun n Qq mHopf h => ⟨skeinOp_idem n h, skein_mass_decomposition n Qq mHopf h⟩,
          fun n₁ n₂ n₃ Qq mHopf h₁ h₂ h₃ =>
            ⟨fusionOp_constituents_assoc n₁ n₂ n₃ h₁ h₂ h₃,
             fusionOp_mass_add n₁ n₂ Qq mHopf h₁ h₂⟩⟩

end QOU.Hadron
