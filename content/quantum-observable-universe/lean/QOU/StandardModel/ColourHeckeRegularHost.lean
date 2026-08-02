import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Tactic.FinCases

/-!
# QOU.StandardModel.ColourHeckeRegularHost — the colour action cannot live on the
regular three-strand Hecke carrier (a Hecke-compatibility obstruction)

The colour conjecture `conj:sm-colour-stabilizer-action` records, as its
surviving open content, an action of the colour algebra `𝔰𝔲(3) = ker(ev_e)`
(8-dimensional by the corpus gate) on *the framework's own three-strand Hecke
state space*, **compatible with its braid/Hecke structure** — "not merely some
faithful module somewhere."

The abstract class `QOU.StandardModel.ColourStabilizerAction` asks only for an
injective **linear** map `g →ₗ End V`. That is tautologically satisfiable for
any `V` with `finrank V ≥ 3` (since `8 ≤ 3² = 9`); the octonion base module
already witnesses it (`OctonionColourActionBaseModule`), and so would *any*
6-dimensional `V`. So instantiating the weak class on the Hecke carrier closes
nothing — the genuine content is **Hecke-compatibility**.

The framework's own three-strand state space is the **6-dimensional regular
carrier** `H₃(q)` implemented in `QOU.Mathlib.HeckeAlgebra` as
`H3Carrier = ℚ⁶`, with the two braid generators acting by left multiplication
`H3.mulSigma1`, `H3.mulSigma2`. Modelling it here as `Fin 6 → ℚ` (the same
basis `{1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}`, positions `0..5`), the generators are
the matrices `L₁ = mulSigma1`, `L₂ = mulSigma2` (formulas copied verbatim from
`HeckeAlgebra.lean`, reproduced self-contained so this file verifies against
Mathlib alone).

**Result (this file, sorry-free).** "Hecke-compatible" in the Schur–Weyl sense
means the colour action **commutes with the Hecke action** `L₁, L₂`. On the
regular carrier this is *structurally impossible* for an 8-dimensional colour
algebra:

* `evAtOne_injective` — the centralizer of the regular Hecke action injects into
  `V` by evaluation at the cyclic vector `1 = e₀` (the six words
  `1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁` applied to `e₀` are the standard basis, so a
  centralizing `T` is determined by `T e₀`).
* `finrank_heckeCentralizer_le_six` — hence `finrank (centralizer) ≤ 6`.
* `no_heckeCompatible_colour_action_on_regularH3` — no injective linear
  `Φ : g →ₗ End V` with every `Φ x` commuting with `L₁, L₂` exists when
  `finrank g = 8`, since it would force `8 ≤ 6`.

This is a **scope-(b) structural exclusion** (per AGENTS.md "Before declaring
refuted"), cited to a *proved dimension invariant* — `finrank(End_{H₃}(H₃)) =
finrank H₃ = 6 < 8`. It is scoped to the **regular carrier** with the
**centralizer** reading of compatibility; it does **not** exclude the colour
action on the larger Schur–Weyl tensor host `(ℂ³)^{⊗3}` (dim 27), where the
Hecke centralizer is the DV–Todorov diagonal `𝔰𝔲(3)` itself. That positive
construction is the genuine remaining open derivation (see the conjecture's
`authorNotes`).

Applies to `𝔰𝔲(3) = ker(ev_e)` via the corpus gate `finrank (su3 e) = 8`
(`QOU.MathlibExt.OctonionSU3Stabilizer`): substitute `g := ↥(su3 e)`.

Base ring ℚ; exact rational linear algebra, nothing archimedean.
-/

namespace QOU.StandardModel.ColourHeckeRegularHost

open Matrix Module

/-- The framework's 6-dimensional regular three-strand Hecke state space,
`H3Carrier = ℚ⁶` (basis `{1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}` at positions `0..5`),
modelled as `Fin 6 → ℚ`. -/
abbrev V : Type := Fin 6 → ℚ

/-- Hecke off-diagonal weight `d = q − q⁻¹` (the coefficient in
`σ_i² = (q − q⁻¹)σ_i + 1`). -/
def d (q : ℚ) : ℚ := q - q⁻¹

/-- Matrix of **left-multiplication by `σ₁`** on the regular carrier, copied
from `QOU.Mathlib.HeckeAlgebra.H3.mulSigma1`. Row `i` = coefficients of the
`i`-th output coordinate:
`(x₁, x₀+d·x₁, x₃, x₂+d·x₃, x₅, x₄+d·x₅)`. -/
def M1 (q : ℚ) : Matrix (Fin 6) (Fin 6) ℚ :=
  !![0, 1, 0, 0, 0, 0;
     1, d q, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0;
     0, 0, 1, d q, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 1, d q]

/-- Matrix of **left-multiplication by `σ₂`** on the regular carrier, copied
from `QOU.Mathlib.HeckeAlgebra.H3.mulSigma2`. Output
`(x₂, x₄, x₀+d·x₂, x₅, x₁+d·x₄, x₃+d·x₅)`. -/
def M2 (q : ℚ) : Matrix (Fin 6) (Fin 6) ℚ :=
  !![0, 0, 1, 0, 0, 0;
     0, 0, 0, 0, 1, 0;
     1, 0, d q, 0, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 1, 0, 0, d q, 0;
     0, 0, 0, 1, 0, d q]

/-- Left-multiplication by `σ₁` as an endomorphism of the state space. -/
noncomputable def L1 (q : ℚ) : Module.End ℚ V := Matrix.toLin' (M1 q)

/-- Left-multiplication by `σ₂` as an endomorphism of the state space. -/
noncomputable def L2 (q : ℚ) : Module.End ℚ V := Matrix.toLin' (M2 q)

/-- The **Hecke centralizer**: endomorphisms of the state space commuting with
both regular Hecke generators — the target of a Hecke-compatible colour action
(Schur–Weyl reading). A submodule as the intersection of the two commuting
kernels. -/
noncomputable def heckeCentralizer (q : ℚ) : Submodule ℚ (Module.End ℚ V) :=
  LinearMap.ker (LinearMap.mulRight ℚ (L1 q) - LinearMap.mulLeft ℚ (L1 q)) ⊓
  LinearMap.ker (LinearMap.mulRight ℚ (L2 q) - LinearMap.mulLeft ℚ (L2 q))

/-- Membership unfolds to the two commuting relations `T * Lᵢ = Lᵢ * T`. -/
theorem mem_heckeCentralizer_iff (q : ℚ) (T : Module.End ℚ V) :
    T ∈ heckeCentralizer q ↔ T * L1 q = L1 q * T ∧ T * L2 q = L2 q * T := by
  simp only [heckeCentralizer, Submodule.mem_inf, LinearMap.mem_ker,
    LinearMap.sub_apply, LinearMap.mulRight_apply, LinearMap.mulLeft_apply,
    sub_eq_zero]

end QOU.StandardModel.ColourHeckeRegularHost
