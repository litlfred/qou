/-
# Is there a flavour `su(2)` acting on the left line only? Not inside one letter

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). Owner decision 1 (2026-11-15): does
the left-line weak vertex, together with a flavour grading, generate an `su(2)`/`sl₂`
that acts ONLY on `leftLine` (a doublet) and trivially on the right line (singlets)?

## Proved here (generic `[Field K] [Ring A] [Algebra K A]`)

1. **On the left line, `u` and `d` are proportional.** `σ P₊ = q P₊` and
   `σ⁻¹ P₊ = q⁻¹ P₊`, so `q⁻¹ (σ P₊) = q (σ⁻¹ P₊)`
   (`flavours_proportional_on_Pp`, and `_on_Pm` for the other line). In the algebra one
   letter generates, `u_L` and `d_L` are the same vector up to scale. The left line is
   one-dimensional there and cannot carry a doublet.
2. **Each flavour has a component on both lines.** `σ = q P₊ − q⁻¹ P₋` and
   `σ⁻¹ = q⁻¹ P₊ − q P₋` (`sigma_split`, `flip_split`). The two-dimensional space
   `span{u, d} = span{P₊, P₋}` is `L ⊕ R`, so an `sl₂` on the pair `(u, d)` mixes the
   two lines. This is the same failure as the quaternion `Sp(1)_left` of
   `QuaternionSidedSymmetry.lean`, where the doublet space is the chirality pair itself.
3. **The corner over a line is commutative.** Every one-letter element `a + b σ`
   satisfies `P₊ (a + b σ) P₊ = (a + b q) P₊` (`corner_Pp`). Elements supported on the
   left line therefore commute.
4. **A commuting `sl₂`-triple is zero** (`sl2_triple_trivial_of_comm`): from
   `[e, f] = h`, `[h, e] = 2e`, `[h, f] = −2f` and `e f = f e`, with `2 ≠ 0`, it follows
   that `e = f = h = 0`.

Verdict for this setting, scope (b): there is no flavour `sl₂` acting on the left line
only. The invariant is that the corner is commutative (the left line is
one-dimensional). The SM doublet structure is `V_flavour ⊗ V_chirality` (dimension 4),
with `su(2)` acting as `E ⊗ P_L`. Here flavour (letter orientation) and chirality
(eigenline) live in the same two-dimensional `span{1, σ}`, so the tensor product is
absent.

## Beyond one letter, cited and not proved here

* `H₃ ≅ K ⊕ K ⊕ M₂(K)` for generic `q` (cited, as in #7825). The `q`-line projector of
  `σ₀` is `1 ⊕ 0 ⊕ e` with `e` of rank 1, so the corner `P₊ H₃ P₊ ≅ K ⊕ K` is
  commutative. By item 4, no left-only `sl₂` exists in `H₃` either. Conditional on the
  cited decomposition.
* For `n ≥ 4` the corner `P₊ H_n P₊` is not commutative (it contains the commuting
  letter `σ₃` and longer words), so the question is open there. A LEAD, not a result:
  the commuting letters `σ₁, σ₃` give `K[σ₁] ⊗ K[σ₃]` of dimension 4, which is the shape
  `chirality ⊗ flavour`. Nothing here builds `E ⊗ P_L` from it.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra; Wedderburn decomposition for generic q)
-/
import QOU.QuarkState.LeftLineDefinition

namespace QOU.QuarkState.FlavourDoublet

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex

section Abstract

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- **`u` and `d` are proportional on the `q`-line.** -/
theorem flavours_proportional_on_Pp (hq : q ≠ 0) (hs : IsLetter q s) :
    q⁻¹ • (s * Pp q s) = q • (flip q s * Pp q s) := by
  rw [eigen_plus hq hs, flip_eigen_plus hq hs, smul_smul, smul_smul, inv_mul_cancel₀ hq,
    mul_inv_cancel₀ hq]

/-- **… and on the `(−q⁻¹)`-line.** -/
theorem flavours_proportional_on_Pm (hq : q ≠ 0) (hs : IsLetter q s) :
    q • (s * Pm q s) = q⁻¹ • (flip q s * Pm q s) := by
  rw [eigen_minus hq hs, flip_eigen_minus hq hs, smul_smul, smul_smul]
  congr 1
  field_simp

/-- `σ = q P₊ − q⁻¹ P₋`. -/
theorem sigma_split (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    s = q • Pp q s + (-q⁻¹) • Pm q s := by
  calc s = s * (Pp q s + Pm q s) := by rw [Pp_add_Pm hq2, mul_one]
    _ = q • Pp q s + (-q⁻¹) • Pm q s := by rw [mul_add, eigen_plus hq hs, eigen_minus hq hs]

/-- `σ⁻¹ = q⁻¹ P₊ − q P₋`. -/
theorem flip_split (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    flip q s = q⁻¹ • Pp q s + (-q) • Pm q s := by
  calc flip q s = flip q s * (Pp q s + Pm q s) := by rw [Pp_add_Pm hq2, mul_one]
    _ = q⁻¹ • Pp q s + (-q) • Pm q s := by
      rw [mul_add, flip_eigen_plus hq hs, flip_eigen_minus hq hs]

/-- **The corner over the `q`-line is a line**: `P₊ (a + b σ) P₊ = (a + b q) P₊`. -/
theorem corner_Pp (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (a b : K) :
    Pp q s * (a • (1 : A) + b • s) * Pp q s = (a + b * q) • Pp q s := by
  rw [mul_add, mul_smul_comm, mul_one, mul_smul_comm, Pp_eigen_right hq hs, smul_smul,
    add_mul, smul_mul_assoc, smul_mul_assoc, Pp_idem hq hq2 hs, ← add_smul, mul_comm b q]

/-- Corner elements commute. -/
theorem corner_comm (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (a b c d : K) :
    (Pp q s * (a • (1 : A) + b • s) * Pp q s) * (Pp q s * (c • (1 : A) + d • s) * Pp q s)
      = (Pp q s * (c • (1 : A) + d • s) * Pp q s)
          * (Pp q s * (a • (1 : A) + b • s) * Pp q s) := by
  rw [corner_Pp hq hq2 hs, corner_Pp hq hq2 hs, smul_mul_smul_comm, smul_mul_smul_comm,
    mul_comm (a + b * q)]

end Abstract

section Sl2

variable {K S : Type*} [Field K] [Ring S] [Algebra K S]

/-- **A commuting `sl₂`-triple is zero.** -/
theorem sl2_triple_trivial_of_comm (h2 : (2 : K) ≠ 0) {e f h : S}
    (hef : e * f - f * e = h) (hhe : h * e - e * h = (2 : K) • e)
    (hhf : h * f - f * h = (-2 : K) • f) (hcomm : e * f = f * e) :
    e = 0 ∧ f = 0 ∧ h = 0 := by
  have hh : h = 0 := by rw [← hef, hcomm, sub_self]
  subst hh
  refine ⟨?_, ?_, rfl⟩
  · have : (2 : K) • e = 0 := by rw [← hhe]; simp
    exact (smul_eq_zero.mp this).resolve_left h2
  · have : (-2 : K) • f = 0 := by rw [← hhf]; simp
    exact (smul_eq_zero.mp this).resolve_left (neg_ne_zero.mpr h2)

end Sl2

end QOU.QuarkState.FlavourDoublet
