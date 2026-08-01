/-
  Fantini–Wheeler Borel–Laplace summability into state integrals — the
  Stokes-cocycle algebraic skeleton.

  **Conditional on [fantini-wheeler2024], arXiv:2410.20973 Thm 1.4.**

  Fantini–Wheeler (2024) prove that the asymptotic series `Φ_Ξ(−2πi/τ)`
  attached to a hyperbolic knot are Borel–Laplace summable, and that away
  from the (countable set of) Stokes rays the resummation is a
  `ℤ[q^±]`-linear combination of the Andersen–Kashaev state integrals
  `I_{m,ℓ}(τ)` (the Andersen–Kashaev integral is the `(m,ℓ) = (0,0)`
  member). Collecting the `max{A,B}²` independent series into a frame
  `Î_{j,ϑ}`, changing the resummation direction acts on the frame by a
  Stokes matrix (their eq. 26)

      Î_{j,ϑ₂}(τ) = Î_{j,ϑ₁}(τ) · S_{ϑ₁,ϑ₂}(q),
      S_{ϑ₁,ϑ₂}(q) ∈ GL_{max{A,B}}(ℤ[q^±]),

  and these Stokes matrices satisfy the cocycle relation (their eq. 27)

      S_{ϑ₁,ϑ₂}(q) · S_{ϑ₂,ϑ₃}(q) = S_{ϑ₁,ϑ₃}(q).

  **QOU does NOT re-derive FW Thm 1.4.** It is a literature input. This
  file follows the §3b-cond conditional-class pattern: the class
  `BorelSummableToStateIntegral` axiomatizes the *hypotheses / inputs* of
  FW Thm 1.4 (the rank-`r = max{A,B}` state-integral module, the
  Borel-sum ∈ span relation, the frame, and the Stokes cocycle valued in
  `GL r R`), and the downstream theorems *derive* genuine consequences
  from those hypotheses — Lean actually proving each implication,
  sorry-free:

    * `stokes_refl`     : `S_{ϑ,ϑ} = 1` (no Stokes jump along one ray)
    * `stokes_inv`      : `(S_{ϑ₁,ϑ₂})⁻¹ = S_{ϑ₂,ϑ₁}` (reverse = inverse)
    * `stokes_mul_symm` : `S_{ϑ₁,ϑ₂} · S_{ϑ₂,ϑ₁} = 1`
    * `frame_transport_trans` : the frame transports consistently along
      *any* chain `a → b → c` of directions — Borel–Laplace resummation
      is path-independent (derived from the transport hypothesis + the
      cocycle)
    * `ak_integral_mem_span`  : the Andersen–Kashaev integral `I_{0,0}`
      lies in the state-integral module (span)
    * `resummation_sub_ak_mem_span` : the resummation differs from the AK
      integral by an element of the state-integral span

  None of these *assume* their own conclusion: `stokes_refl` and
  `stokes_inv` come out of the `stokes_cocycle` field by the group
  structure of `GL r R` (an idempotent group element is the identity; a
  two-sided factor of `1` is the inverse), and `frame_transport_trans`
  composes the `frame_transport` field with `stokes_cocycle`. This is the
  honest way to represent a literature theorem we *assume* rather than
  *prove* (§"Axiomatization is NOT a Proof": the class assumes FW's
  inputs; the theorems derive real implications, and no downstream
  physics constant is unlocked by them).

  Base ring (§7c): the entire file is over a generic `{R : Type*}
  [CommRing R]` standing for the Laurent ring `ℤ[q^±]` — this is
  algebraic q-series content with no archimedean construct, so `R` is
  never specialized to `ℝ`.

  -- Ref: [fantini-wheeler2024] https://arxiv.org/abs/2410.20973
-/

import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup.Basic
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Algebra.BigOperators.Module
import Mathlib.Data.Matrix.Mul

namespace QOU.Mathlib.BorelStateIntegral

open scoped BigOperators

/-- **Hypotheses / inputs of Fantini–Wheeler Theorem 1.4**
    ([fantini-wheeler2024], arXiv:2410.20973), axiomatized as a Lean
    class over a generic base ring `R` (standing for `ℤ[q^±]`).

    Type parameters:
    * `R` — the base ring (`ℤ[q^±]`).
    * `M` — the `R`-module spanned by the state integrals `I_{m,ℓ}`.
    * `D` — the admissible resummation directions `ϑ` (args avoiding
      Stokes rays); left abstract.

    The rank `r = max{A,B}` is the number of critical points (FW: "there
    are `max{A,B}` critical points"). The fields carry the *inputs* FW
    proves exist; the downstream theorems derive consequences.

    The cocycle field is stated in groupoid-completed form (all triples),
    the standard resurgent-structure encoding of FW eq. (27), which holds
    for ordered `ϑ₁ < ϑ₂ < ϑ₃` and extends by `S_{ϑ,ϑ} := 1`,
    `S_{ϑ',ϑ} := S_{ϑ,ϑ'}⁻¹`.

    §3b-cond non-degeneracy: no field carries a downstream theorem's own
    conclusion. `stokes_refl` / `stokes_inv` are *derived* from
    `stokes_cocycle` via the group structure of `GL (Fin rank) R`;
    `frame_transport_trans` is *derived* from `frame_transport` + the
    cocycle. -/
class BorelSummableToStateIntegral (R : Type*) [CommRing R]
    (M : Type*) [AddCommGroup M] [Module R M] (D : Type*) where
  /-- The rank `r = max{A,B}` — the number of critical points / the size
      of the Stokes matrices. -/
  rank : ℕ
  /-- The Andersen–Kashaev state integrals `I_{m,ℓ} ∈ M`, indexed by
      `(m, ℓ) ∈ ℤ × ℤ`. The `(0,0)` member is the AK integral. -/
  stateIntegral : ℤ × ℤ → M
  /-- The Borel–Laplace resummation of `Φ_Ξ` in admissible direction `ϑ`;
      a single distinguished element of the state-integral module. -/
  resummation : D → M
  /-- **FW combination relation.** Away from Stokes rays the resummation
      is a `ℤ[q^±]`-linear combination of state integrals: it lies in the
      `R`-span of the `I_{m,ℓ}`. -/
  resummation_mem_span :
    ∀ d, resummation d ∈ Submodule.span R (Set.range stateIntegral)
  /-- The frame `Î_{j,ϑ}`: the `r`-tuple of independent resummed series
      collected in FW eq. (25), as a map `D → (Fin rank → M)`. -/
  frame : D → Fin rank → M
  /-- The Stokes matrices `S_{ϑ₁,ϑ₂}(q) ∈ GL_{max{A,B}}(ℤ[q^±])`
      (FW eq. 26). Valued in the general linear group over `R`. -/
  stokes : D → D → Matrix.GeneralLinearGroup (Fin rank) R
  /-- **FW transport (eq. 26).** Changing the resummation direction acts
      on the frame by right-multiplication by the Stokes matrix:
      `Î_{j,ϑ₂} = Î_{j,ϑ₁} · S_{ϑ₁,ϑ₂}`, i.e. componentwise
      `frame b i = ∑ⱼ (S_{a,b})ⱼᵢ • frame a j`. -/
  frame_transport :
    ∀ a b : D, ∀ i : Fin rank,
      frame b i
        = ∑ j : Fin rank,
            (stokes a b : Matrix (Fin rank) (Fin rank) R) j i • frame a j
  /-- **FW Stokes cocycle (eq. 27, groupoid form).**
      `S_{ϑ₁,ϑ₂} · S_{ϑ₂,ϑ₃} = S_{ϑ₁,ϑ₃}`. -/
  stokes_cocycle :
    ∀ a b c : D, stokes a b * stokes b c = stokes a c

namespace BorelSummableToStateIntegral

variable {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]
  {D : Type*} [ctx : BorelSummableToStateIntegral R M D]

/-- **No Stokes jump along a single ray:** `S_{ϑ,ϑ} = 1`.
    Derived from the cocycle — `S_{ϑ,ϑ}` is idempotent in the group
    `GL (Fin rank) R`, hence the identity. This is *not* a field. -/
theorem stokes_refl (a : D) :
    ctx.stokes a a = 1 :=
  -- `stokes a a * stokes a a = stokes a a` ⇒ `stokes a a = 1`.
  mul_eq_left.mp (ctx.stokes_cocycle a a a)

/-- **Reverse direction = inverse Stokes matrix:** `(S_{ϑ₁,ϑ₂})⁻¹ =
    S_{ϑ₂,ϑ₁}`. Derived from the cocycle and `stokes_refl`. -/
theorem stokes_inv (a b : D) :
    (ctx.stokes a b)⁻¹ = ctx.stokes b a :=
  inv_eq_of_mul_eq_one_right <| by
    rw [ctx.stokes_cocycle a b a, stokes_refl a]

/-- **Two-sided composition of a Stokes matrix with its reverse is the
    identity:** `S_{ϑ₁,ϑ₂} · S_{ϑ₂,ϑ₁} = 1`. -/
theorem stokes_mul_symm (a b : D) :
    ctx.stokes a b * ctx.stokes b a = 1 := by
  rw [ctx.stokes_cocycle a b a, stokes_refl a]

/-- **Path-independence of Borel–Laplace resummation.** Transporting the
    frame from `a` to `c` directly equals transporting `a → b → c`: for
    every component `i`,
    `frame c i = ∑ⱼ (S_{a,c})ⱼᵢ • frame a j`.
    Derived by composing the `frame_transport` field with the
    `stokes_cocycle` field — the genuine work of the cocycle on the
    state-integral data. -/
theorem frame_transport_trans (a b c : D) (i : Fin ctx.rank) :
    ctx.frame c i
      = ∑ j : Fin ctx.rank,
          (ctx.stokes a c : Matrix (Fin ctx.rank) (Fin ctx.rank) R) j i • ctx.frame a j := by
  -- Expand the transport b → c, then a → b inside.
  rw [ctx.frame_transport b c i]
  simp_rw [ctx.frame_transport a b, Finset.smul_sum, smul_smul]
  -- ∑ k, ∑ j, ((S_bc)_{ki} * (S_ab)_{jk}) • frame a j
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [← Finset.sum_smul]
  -- reduce the scalar sum ∑ k, (S_bc)_{ki} * (S_ab)_{jk} to (S_ac)_{ji}
  congr 1
  rw [← ctx.stokes_cocycle a b c]
  -- (↑(S_ab * S_bc)) j i = ∑ k, (S_ab)_{jk} * (S_bc)_{ki}
  rw [Matrix.GeneralLinearGroup.coe_mul, Matrix.mul_apply]
  exact Finset.sum_congr rfl (fun k _ => mul_comm _ _)

/-- **The Andersen–Kashaev integral lies in the state-integral module.**
    The AK integral is the `(m,ℓ) = (0,0)` state integral, so it is a
    generator of the span. -/
theorem ak_integral_mem_span :
    ctx.stateIntegral (0, 0) ∈ Submodule.span R (Set.range ctx.stateIntegral) :=
  Submodule.subset_span (Set.mem_range_self _)

/-- **The resummation differs from the AK integral by a `ℤ[q^±]`-combination
    of state integrals.** Both `resummation d` and `I_{0,0}` lie in the
    span (FW combination relation + `ak_integral_mem_span`), and the span
    is a submodule, so their difference does too. -/
theorem resummation_sub_ak_mem_span (d : D) :
    ctx.resummation d - ctx.stateIntegral (0, 0)
      ∈ Submodule.span R (Set.range ctx.stateIntegral) :=
  Submodule.sub_mem _ (ctx.resummation_mem_span d) ak_integral_mem_span

end BorelSummableToStateIntegral

end QOU.Mathlib.BorelStateIntegral
