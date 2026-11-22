/-
# A left-only flavour doublet on four strands

Bean `qou-wkcd` (epic `qou-qs0e`), the `n ≥ 4` lead left open in
`FlavourDoubletOnLeftLine.lean`. On two and three strands the left line of `σ₁` is
one-dimensional in every block, so a flavour `sl₂` acting on the left line only is zero.
This file shows that on four strands it is not.

## The representation

`ρ` is an explicit three-dimensional representation of the four-strand Hecke algebra
`H₄(q)` over any field `K` (generators `σ₁, σ₂, σ₃`, quadratic relation
`(σ − q)(σ + q⁻¹) = 0`, braid relations, `σ₁σ₃ = σ₃σ₁`). All relations are proved below
(`s1_quad` … `comm13`). For generic `q` it is the `(3,1)` irreducible; irreducibility is
not used. In the chosen basis `σ₁ = diag(q, q, −q⁻¹)` and `σ₃ = diag(q, −q⁻¹, q)`, so
the left line of `σ₁` (its `q`-eigenspace, the owner's `leftLine` for `q > 1`) is the
span of the first two basis vectors. It is **two-dimensional (a doublet)**. The right
line is the third vector, a **singlet**.

## Two flavour labels on the left doublet (owner choice 2026-11-15: both, side by side)

**A. `σ₃` eigenline** (pre-registered). `u` = `σ₃`'s `q`-line, `d` = its `−q⁻¹`-line.
* `eS = L_u σ₂ L_d`, `fS = L_d σ₂ L_u` form a nonzero `sl₂`-pair supported on the left
  line: `[hS, eS] = cS eS`, `[hS, fS] = −cS fS`, `cS = 2(q⁴+1)/(q²+1)²` (`sigma3_sl2_*`).
* One `γγ` vertex carries it: `L_u (σ₁σ₂⁻¹) L_d = q · eS` (`sigma3_gg_vertex`).
* Cost: `σ₂` is a three-strand letter, so a three-strand word already mixes `u ↔ d`
  (`sigma3_three_strand_letter_mixes`).

**B. `J₄` eigenline** (chosen after the `σ₃` run, for a structural reason).
`J₄ = σ₃σ₂σ₁²σ₂σ₃`, the braid in which strand 4 loops once around strands 1–3. It commutes
with `σ₁, σ₂` (`J4_comm_s1`, `J4_comm_s2`). On the left doublet it has eigenvalues `q⁻²`
(`Ja`) and `q⁴` (`Jb`).
* **No three-strand word mixes the J₄ flavour**: every `w` commuting with `J₄` has
  `Ja w Jb = 0` (`J4_no_mix`, `three_strand_word_no_mix`).
* Only strand-4 letters flip it: `eJ = Ja σ₃ Jb`, `fJ = Jb σ₃ Ja` form a nonzero
  `sl₂`-pair, `cJ = 2(q²+1)²(q⁴+1)/(q⁴+q²+1)²` (`J4_sl2_*`). The `γγ` vertex reaching
  strand 4 carries it: `Ja (σ₂σ₃⁻¹) Jb = q · eJ`, `Ja (σ₂⁻¹σ₃) Jb = q⁻¹ · eJ`.

Both pairs vanish on the right line by construction (they are sandwiched by left-line
projectors).

## Scope

Model statements about `H₄(q)`. Nothing here identifies `u, d` with physical quarks or
nucleons, and no empirical number enters. The physical reading (flavour = J₄ label,
weak vertex = the `γγ` vertex touching strand 4) is an interpretation, scope (a).

**The `J₄` label is not `n` vs `p`** (scoping note, added 2026-11-15). `J₄` commutes with
`H₃`, so its two eigenspaces are the `H₃` isotypic sectors inside the `(3,1)` of `H₄`.
On `Ja` both `σ₁` and `σ₂` act by `q`: it is the `H₃` trivial sector `(3)`. `Jb` is the
`(2,1)` sector. Under Schur–Weyl duality these are the three-strand isospin `3/2` and `1/2`
sectors, not the weight `T³`. No Hecke element, the weak vertex included, changes `T³`,
because Hecke elements commute with the quantum-group action (bean `qou-0whz`, C2;
`OverStrandWeight.lean` fixes `u` as the `T³ = +½` weight). So `eJ`, `fJ` and
`weak_site3_flips` change the three-strand isospin multiplicity, not `n ↔ p`.

The weak vertex on `σ₁` and `σ₃` keeps the left and right lines of `σ₁`; the leak between
them comes from `σ₂` (`weak_site1_keeps_lines`, `weak_site3_keeps_lines`, `s2_leaks`).

Hypotheses: `q ≠ 0`, `q² + 1 ≠ 0`, `q⁴ + q² + 1 ≠ 0`, and `q² ≠ 1` (distinct `J₄`
eigenvalues); `q⁴ + 1 ≠ 0` for non-vanishing.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra; Wedderburn decomposition for generic q)
-- Ref: Jucys–Murphy elements: J_{k+1} = T_k J_k T_k commutes with H_k (standard).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Group.Commute.Basic

namespace QOU.QuarkState.FlavourDoubletFour

open Matrix

/-- Entrywise check of a `3 × 3` matrix identity over a field: multiply out the literal
matrices, then clear denominators. -/
local macro "mat3" : tactic =>
  `(tactic| ((try simp only [Matrix.mul_fin_three, Matrix.one_fin_three, Matrix.smul_of,
      Matrix.smul_vec3, Matrix.of_sub_of, Matrix.of_add_of]) <;> ext i j <;>
    fin_cases i <;> fin_cases j <;> (try simp) <;> (try field_simp) <;> (try ring) <;> (try simp)))

variable {K : Type*} [Field K]

/-- `σ₁ = diag(q, q, −q⁻¹)`. -/
def s1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, q, 0; 0, 0, -q⁻¹]
/-- `σ₁⁻¹`. -/
def s1i (q : K) : Matrix (Fin 3) (Fin 3) K := !![q⁻¹, 0, 0; 0, q⁻¹, 0; 0, 0, -q]

/-- `σ₃ = diag(q, −q⁻¹, q)`. -/
def s3 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, -q⁻¹, 0; 0, 0, q]
/-- `σ₃⁻¹`. -/
def s3i (q : K) : Matrix (Fin 3) (Fin 3) K := !![q⁻¹, 0, 0; 0, -q, 0; 0, 0, q⁻¹]

/-- `σ₂`, written as `(q(q²+1))⁻¹ · M` with `M` polynomial in `q`. -/
def s2 (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![(q ^ 2 - 1) / (q * (q ^ 2 + 1)), -(q ^ 4 + 1) / (q * (q ^ 2 + 1)), q * (q ^ 4 + 1) / (q ^ 2 + 1);
     -q / (q ^ 2 + 1), q ^ 3 / (q ^ 2 + 1), q ^ 3 / (q ^ 2 + 1);
     1 / (q * (q ^ 2 + 1)), 1 / (q * (q ^ 2 + 1)), q ^ 3 / (q ^ 2 + 1)]
/-- `σ₂⁻¹ = σ₂ − (q − q⁻¹)`. -/
def s2i (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![-(q * (q ^ 2 - 1)) / (q ^ 2 + 1), -(q ^ 4 + 1) / (q * (q ^ 2 + 1)), q * (q ^ 4 + 1) / (q ^ 2 + 1);
     -q / (q ^ 2 + 1), 1 / (q * (q ^ 2 + 1)), q ^ 3 / (q ^ 2 + 1);
     1 / (q * (q ^ 2 + 1)), 1 / (q * (q ^ 2 + 1)), 1 / (q * (q ^ 2 + 1))]

/-- Left line of `σ₁` (its `q`-eigenspace). -/
def PL : Matrix (Fin 3) (Fin 3) K := !![1, 0, 0; 0, 1, 0; 0, 0, 0]
/-- Right line of `σ₁` (its `−q⁻¹`-eigenspace). -/
def PR : Matrix (Fin 3) (Fin 3) K := !![0, 0, 0; 0, 0, 0; 0, 0, 1]
/-- `σ₃`-flavour `u` on the left line. -/
def Lu : Matrix (Fin 3) (Fin 3) K := !![1, 0, 0; 0, 0, 0; 0, 0, 0]
/-- `σ₃`-flavour `d` on the left line. -/
def Ld : Matrix (Fin 3) (Fin 3) K := !![0, 0, 0; 0, 1, 0; 0, 0, 0]

/-- The Jucys–Murphy element `J₄ = σ₃σ₂σ₁²σ₂σ₃` (strand 4 loops once around strands 1–3). -/
def J4 (q : K) : Matrix (Fin 3) (Fin 3) K := s3 q * s2 q * s1 q * s1 q * s2 q * s3 q

/-- `J₄`-flavour `a` (eigenvalue `q⁻²`) on the left line. -/
def Ja (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![q ^ 2 / (q ^ 4 + q ^ 2 + 1), -(q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1), 0;
     -q ^ 2 / (q ^ 4 + q ^ 2 + 1), (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1), 0;
     0, 0, 0]

/-- `J₄`-flavour `b` (eigenvalue `q⁴`) on the left line. -/
def Jb (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![(q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1), (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1), 0;
     q ^ 2 / (q ^ 4 + q ^ 2 + 1), q ^ 2 / (q ^ 4 + q ^ 2 + 1), 0;
     0, 0, 0]

/-! ## The representation of `H₄(q)` -/

section Relations

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

theorem s1_quad : s1 q * s1 q = (q - q⁻¹) • s1 q + 1 := by unfold s1; mat3
theorem s2_quad : s2 q * s2 q = (q - q⁻¹) • s2 q + 1 := by unfold s2; mat3
theorem s3_quad : s3 q * s3 q = (q - q⁻¹) • s3 q + 1 := by unfold s3; mat3

theorem s1_mul_s1i : s1 q * s1i q = 1 := by unfold s1 s1i; mat3
theorem s2_mul_s2i : s2 q * s2i q = 1 := by unfold s2 s2i; mat3
theorem s2i_mul_s2 : s2i q * s2 q = 1 := by unfold s2 s2i; mat3
theorem s3_mul_s3i : s3 q * s3i q = 1 := by unfold s3 s3i; mat3

theorem braid12 : s1 q * s2 q * s1 q = s2 q * s1 q * s2 q := by unfold s1 s2; mat3
theorem braid23 : s3 q * s2 q * s3 q = s2 q * s3 q * s2 q := by unfold s3 s2; mat3
theorem comm13 : s1 q * s3 q = s3 q * s1 q := by unfold s1 s3; mat3

/-- The left line is the `q`-eigenspace of `σ₁`, the right line its `−q⁻¹`-eigenspace,
and they split the space. -/
theorem s1_PL : s1 q * PL = q • PL := by unfold s1 PL; mat3
theorem s1_PR : s1 q * PR = (-q⁻¹) • PR := by unfold s1 PR; mat3
theorem PL_add_PR : (PL : Matrix (Fin 3) (Fin 3) K) + PR = 1 := by unfold PL PR; mat3

end Relations

/-! ## A. The `σ₃` doublet -/

/-- `eS = L_u σ₂ L_d`. -/
def eS (q : K) : Matrix (Fin 3) (Fin 3) K := Lu * s2 q * Ld
/-- `fS = L_d σ₂ L_u`. -/
def fS (q : K) : Matrix (Fin 3) (Fin 3) K := Ld * s2 q * Lu
/-- `hS = [eS, fS]`. -/
def hS (q : K) : Matrix (Fin 3) (Fin 3) K := eS q * fS q - fS q * eS q

section Sigma3

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

omit hq hn in
theorem Lu_add_Ld : (Lu : Matrix (Fin 3) (Fin 3) K) + Ld = PL := by unfold Lu Ld PL; mat3

theorem s3_Lu : s3 q * Lu = q • Lu := by unfold s3 Lu; mat3
theorem s3_Ld : s3 q * Ld = (-q⁻¹) • Ld := by unfold s3 Ld; mat3

theorem eS_eq : eS q = !![0, -(q ^ 4 + 1) / (q * (q ^ 2 + 1)), 0; 0, 0, 0; 0, 0, 0] := by
  unfold eS Lu Ld s2; mat3

theorem fS_eq : fS q = !![0, 0, 0; -q / (q ^ 2 + 1), 0, 0; 0, 0, 0] := by
  unfold fS Lu Ld s2; mat3

/-- `[hS, eS] = cS · eS` with `cS = 2(q⁴+1)/(q²+1)²`. -/
theorem sigma3_sl2_e :
    hS q * eS q - eS q * hS q = (2 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) • eS q := by
  unfold hS; rw [eS_eq hq hn, fS_eq hq hn]; mat3

theorem sigma3_sl2_f :
    hS q * fS q - fS q * hS q = (-(2 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2)) • fS q := by
  unfold hS; rw [eS_eq hq hn, fS_eq hq hn]; mat3

/-- The pair is supported on the left line: it vanishes against the right line. -/
theorem sigma3_left_only : eS q * PR = 0 ∧ PR * eS q = 0 ∧ fS q * PR = 0 ∧ PR * fS q = 0 := by
  rw [eS_eq hq hn, fS_eq hq hn]; unfold PR
  refine ⟨?_, ?_, ?_, ?_⟩ <;> mat3

/-- The `σ₃`-flavour raising operator is nonzero. Since `σ₂` is a three-strand letter,
a three-strand word already moves `d` to `u`. -/
theorem sigma3_three_strand_letter_mixes (h4 : q ^ 4 + 1 ≠ 0) : eS q ≠ 0 := by
  rw [eS_eq hq hn]
  intro h
  have := congrFun (congrFun h 0) 1
  simp at this
  rcases this with h1 | h1
  · exact h4 (by linear_combination -h1)
  · rcases h1 with h1 | h1
    · exact hq h1
    · exact hn h1

/-- One `γγ` vertex `V = σ₁σ₂⁻¹` carries the `σ₃` raising operator: `L_u V L_d = q · eS`. -/
theorem sigma3_gg_vertex : Lu * (s1 q * s2i q) * Ld = q • eS q := by
  rw [eS_eq hq hn]; unfold Lu Ld s1 s2i; mat3

end Sigma3

/-! ## B. The `J₄` doublet -/

/-- `eJ = Ja σ₃ Jb`. -/
def eJ (q : K) : Matrix (Fin 3) (Fin 3) K := Ja q * s3 q * Jb q
/-- `fJ = Jb σ₃ Ja`. -/
def fJ (q : K) : Matrix (Fin 3) (Fin 3) K := Jb q * s3 q * Ja q
/-- `hJ = [eJ, fJ]`. -/
def hJ (q : K) : Matrix (Fin 3) (Fin 3) K := eJ q * fJ q - fJ q * eJ q

section JM

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

/-- Explicit form of `J₄`. -/
theorem J4_eq :
    J4 q = !![q ^ 4 - q ^ 2 + 1, q ^ 4 - q ^ 2 + 1 - (q ^ 2)⁻¹, 0;
              q ^ 2 - 1, q ^ 2 - 1 + (q ^ 2)⁻¹, 0;
              0, 0, q ^ 4] := by
  unfold J4 s1 s2 s3; mat3

theorem J4_comm_s1 : Commute (s1 q) (J4 q) := by
  unfold Commute SemiconjBy; rw [J4_eq hq hn]; unfold s1; mat3

theorem J4_comm_s2 : Commute (s2 q) (J4 q) := by
  unfold Commute SemiconjBy; rw [J4_eq hq hn]; unfold s2; mat3

theorem J4_comm_s1i : Commute (s1i q) (J4 q) := by
  unfold Commute SemiconjBy; rw [J4_eq hq hn]; unfold s1i; mat3

theorem J4_comm_s2i : Commute (s2i q) (J4 q) := by
  unfold Commute SemiconjBy; rw [J4_eq hq hn]; unfold s2i; mat3

variable (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hD

omit hq hn in
/-- The same hypothesis in the normal form `simp` produces, for `field_simp`. -/
theorem D_ne' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
  rwa [show (1 : K) + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 by ring]

omit hq hn in
/-- … and in the factored form `field_simp` produces. -/
theorem D_ne'' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
  rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]

theorem Ja_add_Jb : Ja q + Jb q = PL := by have := D_ne' hD; have := D_ne'' hD; unfold Ja Jb PL; mat3

theorem Ja_J4 : Ja q * J4 q = (q ^ 2)⁻¹ • Ja q := by have := D_ne' hD; have := D_ne'' hD; rw [J4_eq hq hn]; unfold Ja; mat3

theorem J4_Jb : J4 q * Jb q = q ^ 4 • Jb q := by have := D_ne' hD; have := D_ne'' hD; rw [J4_eq hq hn]; unfold Jb; mat3

theorem Ja_idem : Ja q * Ja q = Ja q := by have := D_ne' hD; have := D_ne'' hD; unfold Ja; mat3
theorem Jb_idem : Jb q * Jb q = Jb q := by have := D_ne' hD; have := D_ne'' hD; unfold Jb; mat3
theorem Ja_Jb : Ja q * Jb q = 0 := by have := D_ne' hD; have := D_ne'' hD; unfold Ja Jb; mat3

theorem Jb_Ja : Jb q * Ja q = 0 := by have := D_ne' hD; have := D_ne'' hD; unfold Ja Jb; mat3

/-- **No word commuting with `J₄` mixes the `J₄` flavour.** -/
theorem J4_no_mix (h2 : q ^ 2 ≠ 1) {w : Matrix (Fin 3) (Fin 3) K} (hw : Commute w (J4 q)) :
    Ja q * w * Jb q = 0 := by
  have key : (q ^ 2)⁻¹ • (Ja q * w * Jb q) = q ^ 4 • (Ja q * w * Jb q) := by
    calc (q ^ 2)⁻¹ • (Ja q * w * Jb q) = Ja q * J4 q * w * Jb q := by
          rw [Ja_J4 hq hn hD, smul_mul_assoc, smul_mul_assoc]
      _ = Ja q * (w * J4 q) * Jb q := by rw [hw.eq, mul_assoc (Ja q)]
      _ = Ja q * w * (J4 q * Jb q) := by simp only [mul_assoc]
      _ = q ^ 4 • (Ja q * w * Jb q) := by rw [J4_Jb hq hn hD, mul_smul_comm]
  have hne : (q ^ 2)⁻¹ - q ^ 4 ≠ 0 := by
    intro h
    have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
    have h6 : q ^ 6 = 1 := by
      have e : (q ^ 2)⁻¹ * q ^ 2 = 1 := inv_mul_cancel₀ hq2
      have h' : (q ^ 2)⁻¹ = q ^ 4 := sub_eq_zero.mp h
      rw [h'] at e
      linear_combination e
    have : (q ^ 2 - 1) * (q ^ 4 + q ^ 2 + 1) = 0 := by linear_combination h6
    rcases mul_eq_zero.mp this with h | h
    · exact h2 (sub_eq_zero.mp h)
    · exact hD h
  have : ((q ^ 2)⁻¹ - q ^ 4) • (Ja q * w * Jb q) = 0 := by rw [sub_smul, key, sub_self]
  exact (smul_eq_zero.mp this).resolve_left hne

/-- **Every three-strand word keeps the `J₄` flavour**: any product of `σ₁^{±1}`,
`σ₂^{±1}` has no `Ja ← Jb` component. -/
theorem three_strand_word_no_mix (h2 : q ^ 2 ≠ 1) (l : List (Matrix (Fin 3) (Fin 3) K))
    (hl : ∀ x ∈ l, x = s1 q ∨ x = s2 q ∨ x = s1i q ∨ x = s2i q) :
    Ja q * l.prod * Jb q = 0 := by
  apply J4_no_mix hq hn hD h2
  apply Commute.list_prod_left
  intro x hx
  rcases hl x hx with rfl | rfl | rfl | rfl
  · exact J4_comm_s1 hq hn
  · exact J4_comm_s2 hq hn
  · exact J4_comm_s1i hq hn
  · exact J4_comm_s2i hq hn

theorem eJ_eq : eJ q = (q * (q ^ 2 + 1) * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2) •
    !![1, 1, 0; -1, -1, 0; 0, 0, 0] := by
  have := D_ne' hD; have := D_ne'' hD; unfold eJ Ja Jb s3; mat3

theorem fJ_eq : fJ q = ((q ^ 2 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2) •
    !![q * (q ^ 4 + 1), -(q ^ 4 + 1) ^ 2 / q, 0; q ^ 3, -(q * (q ^ 4 + 1)), 0; 0, 0, 0] := by
  have := D_ne' hD; have := D_ne'' hD; unfold fJ Ja Jb s3; mat3

set_option maxHeartbeats 2000000 in
/-- `[hJ, eJ] = cJ · eJ` with `cJ = 2(q²+1)²(q⁴+1)/(q⁴+q²+1)²`. -/
theorem J4_sl2_e :
    hJ q * eJ q - eJ q * hJ q
      = (2 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2) • eJ q := by
  have := D_ne' hD; have := D_ne'' hD; unfold hJ; rw [eJ_eq hq hn hD, fJ_eq hq hn hD]; mat3

set_option maxHeartbeats 2000000 in
theorem J4_sl2_f :
    hJ q * fJ q - fJ q * hJ q
      = (-(2 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2)) • fJ q := by
  have := D_ne' hD; have := D_ne'' hD; unfold hJ; rw [eJ_eq hq hn hD, fJ_eq hq hn hD]; mat3

/-- The `J₄` pair is supported on the left line. -/
theorem J4_left_only : eJ q * PR = 0 ∧ PR * eJ q = 0 ∧ fJ q * PR = 0 ∧ PR * fJ q = 0 := by
  have := D_ne' hD; have := D_ne'' hD; rw [eJ_eq hq hn hD, fJ_eq hq hn hD]; unfold PR
  refine ⟨?_, ?_, ?_, ?_⟩ <;> mat3

/-- The strand-4 `γγ` vertex `σ₂σ₃⁻¹` carries the `J₄` raising operator. -/
theorem J4_gg_vertex : Ja q * (s2 q * s3i q) * Jb q = q • eJ q := by
  have := D_ne' hD; have := D_ne'' hD; rw [eJ_eq hq hn hD]; unfold Ja Jb s2 s3i; mat3

/-- … and so does its mirror `σ₂⁻¹σ₃`. -/
theorem J4_gg_vertex_mirror : Ja q * (s2i q * s3 q) * Jb q = q⁻¹ • eJ q := by
  have := D_ne' hD; have := D_ne'' hD; rw [eJ_eq hq hn hD]; unfold Ja Jb s2i s3; mat3

/-- `eJ ≠ 0`, so the `J₄` doublet is a genuine (nonzero) `sl₂`-pair. -/
theorem eJ_ne_zero (h4 : q ^ 4 + 1 ≠ 0) : eJ q ≠ 0 := by
  have hx : q * (q ^ 2 + 1) * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2 ≠ 0 :=
    div_ne_zero (mul_ne_zero (mul_ne_zero hq hn) h4) (pow_ne_zero 2 hD)
  intro h
  rw [eJ_eq hq hn hD] at h
  apply hx
  simpa using congrArg (fun M => M 0 0) h

/-! ### The weak vertex on the `J₄` doublet

The corpus weak vertex on a letter `σ` is `σ − h·P_L(σ)` with `h = q − q⁻¹` and
`P_L(σ) = [2]⁻¹(σ + q⁻¹)` (`WeakVertexLeftProjector.weakVertex_sub_letter`). Written out
here for the three letters of the `(3,1)` representation. -/

/-- The left projector of a letter: `[2]⁻¹ (σ + q⁻¹)`. -/
def letterPL (q : K) (s : Matrix (Fin 3) (Fin 3) K) : Matrix (Fin 3) (Fin 3) K :=
  (q + q⁻¹)⁻¹ • (s + q⁻¹ • (1 : Matrix (Fin 3) (Fin 3) K))

/-- The weak vertex on a letter: `σ − h·P_L(σ)`. -/
def weakAt (q : K) (s : Matrix (Fin 3) (Fin 3) K) : Matrix (Fin 3) (Fin 3) K :=
  s - (q - q⁻¹) • letterPL q s

/-- A weak vertex on strand 1 or 2 keeps the `J₄` flavour: it commutes with `J₄`. -/
theorem weak_site1_comm : Commute (weakAt q (s1 q)) (J4 q) := by
  have h := J4_comm_s1 hq hn
  exact h.sub_left (((h.add_left ((Commute.one_left _).smul_left _)).smul_left _).smul_left _)

/-- See `weak_site1_comm`. -/
theorem weak_site2_comm : Commute (weakAt q (s2 q)) (J4 q) := by
  have h := J4_comm_s2 hq hn
  exact h.sub_left (((h.add_left ((Commute.one_left _).smul_left _)).smul_left _).smul_left _)

/-- **The strand-4 weak vertex converts the `J₄` flavour, by the `sl₂` raising operator.**
Between `Jb` and `Ja` the insertion `weakAt − σ₃ = −h·P_L(σ₃)` is `−h/[2]` times `eJ`. -/
theorem weak_site3_flips :
    Ja q * (weakAt q (s3 q) - s3 q) * Jb q = (-(q - q⁻¹) * (q + q⁻¹)⁻¹) • eJ q := by
  have hab := Ja_Jb hq hn hD
  unfold weakAt letterPL eJ
  simp only [sub_sub_cancel_left, Matrix.mul_neg, Matrix.neg_mul, Matrix.mul_smul,
    Matrix.smul_mul, Matrix.mul_add, Matrix.add_mul, Matrix.mul_one, smul_smul]
  rw [hab, smul_zero, add_zero, neg_mul, neg_smul]

/-- The reverse direction, by the lowering operator `fJ`. -/
theorem weak_site3_flips_back :
    Jb q * (weakAt q (s3 q) - s3 q) * Ja q = (-(q - q⁻¹) * (q + q⁻¹)⁻¹) • fJ q := by
  have hba := Jb_Ja hq hn hD
  unfold weakAt letterPL fJ
  simp only [sub_sub_cancel_left, Matrix.mul_neg, Matrix.neg_mul, Matrix.mul_smul,
    Matrix.smul_mul, Matrix.mul_add, Matrix.add_mul, Matrix.mul_one, smul_smul]
  rw [hba, smul_zero, add_zero, neg_mul, neg_smul]

end JM

/-! ### Where the left/right leak comes from

The weak vertex on `σ₁` or `σ₃` never moves a state between the left and right lines of
`σ₁`: both letters are diagonal in this basis, so their left projectors commute with
`PL`. The leak between the lines comes from the letter `σ₂` alone. -/

section Leak

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

/-- The left projector of `σ₁` is `PL`. -/
theorem letterPL_s1 : letterPL q (s1 q) = PL := by unfold letterPL s1 PL; mat3

/-- The weak vertex on `σ₁` keeps the left and right lines of `σ₁`. -/
theorem weak_site1_keeps_lines : Commute (weakAt q (s1 q)) PL := by
  unfold Commute SemiconjBy weakAt letterPL s1 PL; mat3

/-- The weak vertex on `σ₃` keeps the left and right lines of `σ₁`. -/
theorem weak_site3_keeps_lines : Commute (weakAt q (s3 q)) PL := by
  unfold Commute SemiconjBy weakAt letterPL s3 PL; mat3

/-- **The leak is `σ₂`.** It moves the left line of `σ₁` into the right line. -/
theorem s2_leaks : PR * s2 q * PL ≠ 0 := by
  intro h
  have h20 := congrArg (fun M => M 2 0) h
  simp [PR, PL, s2, Matrix.mul_apply, Fin.sum_univ_three, hq, hn] at h20

end Leak

end QOU.QuarkState.FlavourDoubletFour
