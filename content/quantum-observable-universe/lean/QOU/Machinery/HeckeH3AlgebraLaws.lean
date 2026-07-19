/-
# H₃(q) NF module is an algebra object — presentation laws, associativity, and the H₂↪H₃ stabilization rung

Categorical tranche on the τ-functor source-category gap (F1/F2 of
`TauFunctorReduction`; beans `qou-pbjv` / `qou-ep0a` context). The
`HeckeBraidedCategoryScaffold` names two OPEN classes; their concrete n=3
slice (`QOU.Machinery.H3`) carried the trace laws (M1/M2/M3) but NOT the
facts that make the NF module an honest *algebra object* in the source
category. This file closes that layer, sorry-free:

* **Presentation laws completed at n=3** — the σ₁ Hecke quadratic
  (`mulσ₁_hecke`, partner of the existing `mulσ₀_hecke`) and the **braid
  relation** `σ₀σ₁σ₀ = σ₁σ₀σ₁` (`braid_operator`) as operator identities on
  the NF module: the Yang–Baxter / hexagon shadow (the F2 datum) is now
  machine-checked at the concrete rung, completing all three
  `HeckeBraidedPresentation` field contents at n=3 (far commutation is
  vacuous with two generators).
* **Algebra-object laws** — `mulNF` is R-bilinear (`mulNF_add_left/right`,
  `mulNF_smul_left/right`), unital with unit γ = e₀ (`mulNF_one_left/right`),
  and **associative** (`mulNF_assoc`). Together with the existing trace laws
  this certifies: the H₃ NF module is an associative unital R-algebra and
  `trM` is a genuine Markov trace on it — the concrete algebra object the
  braided source category 𝐂 is built from.
* **The H₂ ↪ H₃ stabilization rung** — the two-dimensional H₂ = span{γ, σ₀}
  with its Markov trace `trM₂(a·γ + b·σ₀) = a + z·b`, the inclusion
  `iota23`, and the **bottom rung of the Tier-2 Markov stabilization**:
  `trM (iota23 x) = trM₂ x` (`trM_iota23_stabilizes`), plus multiplicativity
  of the inclusion (`iota23_mul`). This is the concrete base case the
  `MarkovStabilization` class docstring points to.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): no instance of
`HeckeBraidedPresentation` or `MarkovStabilization` is declared — those
classes quantify a generator family `σ : ℕ → H` (the H_∞ inductive limit),
and NO finite-level padding satisfies them (padding σᵢ := 1 for i ≥ 2 forces
`(q − q⁻¹) • 1 = 0` via the quadratic; padding σᵢ := σ₁ violates far
commutation since σ₀σ₁ ≠ σ₁σ₀). The general-n classes stay OPEN. What this
file adds is the *proved concrete layer* those instances will one day be
built from — never a claim that they exist today. Nothing wired; `1/(8π)`
stays phase-4.

Base ring (§7c): generic `[CommRing R]` throughout — no `ℝ`, no ordering,
no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.MarkovTraceOnHecke

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-! ## Presentation laws completed at n = 3 -/

/-- **Hecke quadratic for σ₁** — partner of the existing `mulσ₀_hecke`:
`σ₁² = h·σ₁ + 1` as an operator identity on the NF module. With this, BOTH
generators satisfy the R-matrix eigenvalue equation concretely. -/
theorem mulσ₁_hecke (h : R) (v : Fin 6 → R) :
    mulσ₁ h (mulσ₁ h v) = h • mulσ₁ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₁, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- **The braid relation** `σ₀σ₁σ₀ = σ₁σ₀σ₁` as an operator identity on the
NF module — the Yang–Baxter / braiding-hexagon shadow (the F2 datum of the
`HeckeBraidedPresentation`), machine-checked at the concrete n=3 rung. All
three presentation field contents are now realized at n=3 (far commutation
is vacuous with two generators). -/
theorem braid_operator (h : R) (v : Fin 6 → R) :
    mulσ₀ h (mulσ₁ h (mulσ₀ h v)) = mulσ₁ h (mulσ₀ h (mulσ₁ h v)) := by
  funext i
  fin_cases i <;> simp [mulσ₀, mulσ₁] <;> ring

/-! ## Algebra-object laws for `mulNF` -/

/-- `mulNF` is additive in the left factor. -/
theorem mulNF_add_left (h : R) (u u' v : Fin 6 → R) :
    mulNF h (u + u') v = mulNF h u v + mulNF h u' v := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, Pi.add_apply] <;> ring

/-- `mulNF` is additive in the right factor. -/
theorem mulNF_add_right (h : R) (u v v' : Fin 6 → R) :
    mulNF h u (v + v') = mulNF h u v + mulNF h u v' := by
  funext i
  fin_cases i <;> simp [mulNF, Pi.add_apply] <;> ring

/-- `mulNF` is R-homogeneous in the left factor. -/
theorem mulNF_smul_left (h c : R) (u v : Fin 6 → R) :
    mulNF h (c • u) v = c • mulNF h u v := by
  funext i
  fin_cases i <;>
    simp [mulNF, mulσ₀, mulσ₁, Pi.smul_apply, smul_eq_mul] <;> ring

/-- `mulNF` is R-homogeneous in the right factor. -/
theorem mulNF_smul_right (h c : R) (u v : Fin 6 → R) :
    mulNF h u (c • v) = c • mulNF h u v := by
  funext i
  fin_cases i <;>
    simp [mulNF, Pi.smul_apply, smul_eq_mul] <;> ring

/-- The unit of the NF algebra: γ = e₀ = `![1,0,0,0,0,0]`. -/
def unitNF : Fin 6 → R := ![1, 0, 0, 0, 0, 0]

/-- **Right unit law**: `u · γ = u`. -/
theorem mulNF_one_right (h : R) (u : Fin 6 → R) :
    mulNF h u unitNF = u := by
  funext i
  fin_cases i <;> simp [mulNF, unitNF]

/-- **Left unit law**: `γ · v = v` — each basis word applied to γ reproduces
the corresponding NF basis element (`word_j(γ) = b_j`). -/
theorem mulNF_one_left (h : R) (v : Fin 6 → R) :
    mulNF h unitNF v = v := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, unitNF]

/-- **Associativity of the full H₃(q) NF product**: `(u·v)·w = u·(v·w)`.
The load-bearing algebra-object law — a polynomial identity in the 18
entries and `h`, closed by `ring` per entry after unfolding the nested
`mulσ` actions (same discipline as `trM_cyclic`; the operator table was
pinned by the symbolic preflight in `gram.py` and cross-verified over
`ℚ(z,h)`). With bilinearity and the unit laws above, the NF module is an
associative unital R-algebra — the concrete algebra object of the braided
source category. -/
theorem mulNF_assoc (h : R) (u v w : Fin 6 → R) :
    mulNF h (mulNF h u v) w = mulNF h u (mulNF h v w) := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁] <;> ring

/-! ## The H₂ ↪ H₃ stabilization rung (bottom rung of Tier 2)

`H₂(q) = span{γ, σ₀}` sits inside the NF module as the vectors supported on
the first two coordinates. The Markov trace at level 2 has weights `(1, z)`;
the inclusion is multiplicative; and the level-3 trace restricts to the
level-2 trace along it — the concrete base case of the `MarkovStabilization`
class (whose general-n instance stays OPEN; see the module docstring). -/

/-- The `H₂ ↪ H₃` inclusion on NF coordinates: `a·γ + b·σ₀ ↦ (a,b,0,0,0,0)`. -/
def iota23 (a b : R) : Fin 6 → R := ![a, b, 0, 0, 0, 0]

/-- The level-2 Markov trace: `trM₂(a·γ + b·σ₀) = a + z·b`
(weights `(1, z)`, the `n = 2` row of the Markov–Ocneanu–Wenzl weights). -/
def trM₂ (z a b : R) : R := a + z * b

/-- **The inclusion is multiplicative**: `iota23` carries the H₂ product
`(a₁ + b₁σ)(a₂ + b₂σ) = (a₁a₂ + b₁b₂) + (a₁b₂ + b₁a₂ + h·b₁b₂)σ` (the
Hecke quadratic in rank one) to the H₃ NF product. -/
theorem iota23_mul (h a₁ b₁ a₂ b₂ : R) :
    mulNF h (iota23 a₁ b₁) (iota23 a₂ b₂)
      = iota23 (a₁ * a₂ + b₁ * b₂) (a₁ * b₂ + b₁ * a₂ + h * (b₁ * b₂)) := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, iota23] <;> ring

/-- **Bottom rung of the Markov stabilization** (Tier-2 base case):
the level-3 trace restricts to the level-2 trace along the inclusion,
`trM(ι x) = trM₂ x`. Together with the already-proved Markov reduction
`trM_markov_σ₁` (`tr(x·σ₁) = z·tr(x)` for `x ∈ H₂`), this is the complete
concrete content of the `n = 2 → 3` stabilization step. -/
theorem trM_iota23_stabilizes (z h a b : R) :
    trM z h (iota23 a b) = trM₂ z a b := by
  simp [trM, trM₂, iota23, TRM, Fin.sum_univ_six]
  ring

/-- The level-2 trace is cyclic for the rank-one product (H₂ is
commutative): packaged for the eventual `MarkovTrace` instance at n=2. -/
theorem trM₂_cyclic (z h a₁ b₁ a₂ b₂ : R) :
    trM₂ z (a₁ * a₂ + b₁ * b₂) (a₁ * b₂ + b₁ * a₂ + h * (b₁ * b₂))
      = trM₂ z (a₂ * a₁ + b₂ * b₁) (a₂ * b₁ + b₂ * a₁ + h * (b₂ * b₁)) := by
  unfold trM₂; ring

end QOU.Machinery.H3
