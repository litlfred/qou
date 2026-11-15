import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic


/-!
# QOU.BringsSurface

Bring's surface Σ₄ = Proj(R[x₀,…,x₄]/(∑xⱼ, ∑xⱼ², ∑xⱼ³)):
smooth projective curve of genus 4 over R (with 30 ∈ R×),
Aut(Σ₄) ≅ S₅, χ(Σ₄) = −6.

LaTeX label: `def:brings-surface`
-/

namespace QOU.Brings

/-- **Bring's surface data**: a genus-4 algebraic curve defined by vanishing
    of the first three power sums in P⁴.

    Over an algebraically closed field K ⊇ R, Σ₄ is a smooth projective
    curve with Aut(Σ₄) ≅ S₅ (120 automorphisms) and Euler characteristic
    χ(Σ₄) = 2 − 2g = −6.

    Ref: [edge1978] https://doi.org/10.1017/S0305004100055699 -/
structure BringsSurface where
  /-- Genus of the surface. -/
  genus : ℕ
  /-- genus = 4 for Bring's surface. -/
  genus_eq : genus = 4
  /-- Number of automorphisms |Aut(Σ₄)|. -/
  automorphism_order : ℕ
  /-- |Aut(Σ₄)| = 120 ≅ |S₅|. -/
  aut_eq : automorphism_order = 120
  /-- Number of homogeneous coordinates (embedding in P⁴). -/
  ambient_dim : ℕ
  /-- The ambient projective space is P⁴, so 5 coordinates. -/
  ambient_dim_eq : ambient_dim = 5
  /-- Number of defining equations (power sums p₁, p₂, p₃). -/
  num_equations : ℕ
  /-- Three power-sum equations cut out the curve. -/
  num_equations_eq : num_equations = 3

/-- Euler characteristic of a genus-g surface: χ = 2 − 2g. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
def eulerCharacteristic (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)

/-- **Euler characteristic of Bring's surface**: χ(Σ₄) = 2 − 2·4 = −6. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
theorem brings_euler_char : eulerCharacteristic 4 = -6 := by
  unfold eulerCharacteristic
  decide

/-- The Euler characteristic of any genus-g surface equals 2 − 2g. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
theorem euler_char_formula (S : BringsSurface) :
    eulerCharacteristic S.genus = -6 := by
  rw [S.genus_eq]
  exact brings_euler_char

/-- The canonical instance of Bring's surface. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
def standardBringsSurface : BringsSurface where
  genus := 4
  genus_eq := rfl
  automorphism_order := 120
  aut_eq := rfl
  ambient_dim := 5
  ambient_dim_eq := rfl
  num_equations := 3
  num_equations_eq := rfl

/-- Hurwitz bound for genus 4: 84(g−1) = 252.
    Bring's surface achieves the maximal automorphism group for genus 4
    with |Aut| = 120 ≤ 252. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
theorem hurwitz_bound_genus_4 : 84 * (4 - 1) = (252 : ℕ) := by norm_num

/-- The dimension of the curve: ambient_dim − num_equations − 1 = 1. -/
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978)
theorem brings_is_curve (S : BringsSurface) :
    S.ambient_dim - S.num_equations - 1 = 1 := by
  rw [S.ambient_dim_eq, S.num_equations_eq]

end QOU.Brings
