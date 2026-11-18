import Mathlib.Tactic
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Topology.Algebra.Order.Field
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.BraidsKnots.nsi_q_deformed_kernel

Content block
[`lem:nsi-q-deformed-kernel`](../../../quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.md):
*$q$-deformed commutator replaces $1/r^2$ with a hard kernel at
$r = \hbar_q$*.

**Manuscript statement.**
*For $q \neq 1$, the categorical mass of a vortex filament $\varrho$
inherits a kernel*

$$
  \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
   \longmapsto
  \frac{[2]_q}{\lvert \varrho(s) - \varrho(t) \rvert^2 - \hbar_q^{2}},
$$

*where $[2]_q = q + q^{-1}$, $\hbar_q = 1 - q^{-1}$, and the kernel
has a hard singularity at
$\lvert \varrho(s) - \varrho(t) \rvert = \hbar_q$.*

## Disposition (integrity)

The previous encoding was a self-assuming projection (AGENTS.md
§3b-cond item 5): the class carried a `claim_nsi_q_deformed_kernel`
field that *was* the kernel identity, and a `def` merely projected it
back out.  Here the kernel is **defined concretely**
(`qDeformedKernel q r = (q + q⁻¹) / (r² − (1 − q⁻¹)²)`), which splits
the lemma into its two honest parts:

- `nsi_q_kernel_hard_singularity` is **derived sorry-free**: for
  `q ≠ 0`, `q ≠ 1` the kernel genuinely blows up at `r = ℏ_q` —
  `|qDeformedKernel q r| → ∞` as `r → ℏ_q`, `r ≠ ℏ_q`.  The proof is
  real analysis, not a projection: `ℏ_q ≠ 0` (else `q = 1`),
  `[2]_q ≠ 0` (over `ℝ`, `q + q⁻¹ = 0` forces `q² + 1 = 0`), the
  denominator `r² − ℏ_q²` tends to `0` and is eventually nonzero on
  the punctured neighbourhood (its only roots are `±ℏ_q`), so the
  reciprocal diverges.
- `nsi_q_kernel_identification` — that the trace-side kernel the
  categorical mass of the filament inherits *is*
  `qDeformedKernel q ‖ϱ(s) − ϱ(t)‖` — is proved conditional on
  `NsiQDeformedKernelContext` (`K_cat_eq` and `qDeformedCommutator_eq`),
  which is where the un-formalised `q`-deformed commutator / `q`-Hodge
  star hypotheses sit per AGENTS.md §3b-cond.

The resolving declaration `nsi_q_deformed_kernel` conjoins the two.
-/

namespace QOU.BraidsKnots

open Filter Topology

/-- Substrate `q`-Planck constant `ℏ_q = 1 − q⁻¹`. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- The `q`-integer `[2]_q = q + q⁻¹`. -/
noncomputable def qInt2 (q : ℝ) : ℝ := q + q⁻¹


/-- **Bridge to the canonical bracket.** The longhand `q + q⁻¹` is this site's
body and its proofs use it, so the consolidation is the identity, not an alias.
Conditional: the two agree away from `q − q⁻¹ = 0`. -/
theorem qInt2_eq_canonical (q : ℝ) (h : q - q⁻¹ ≠ 0) :
    qInt2 q = QOU.QInteger.qIntBal q 2 := (QOU.QInteger.qIntBal_two q h).symm

/-- The `q`-deformed Möbius kernel of
    [`lem:nsi-q-deformed-kernel`]: `[2]_q / (r² − ℏ_q²)` as a
    function of the inter-point separation `r`. -/
noncomputable def qDeformedKernel (q r : ℝ) : ℝ :=
  qInt2 q / (r ^ 2 - hbarQ q ^ 2)

/-- For `q ≠ 1` the `q`-Planck constant `ℏ_q = 1 − q⁻¹` is nonzero.
    (At `q = 0` one has `q⁻¹ = 0` and `ℏ_q = 1`.) -/
theorem hbarQ_ne_zero {q : ℝ} (hq1 : q ≠ 1) : hbarQ q ≠ 0 := by
  unfold hbarQ
  rw [sub_ne_zero]
  intro h
  exact hq1 (inv_eq_one.mp h.symm)

/-- Over `ℝ` the `q`-integer `[2]_q = q + q⁻¹` never vanishes for
    `q ≠ 0`: `q·(q + q⁻¹) = q² + 1 > 0`. -/
theorem qInt2_ne_zero {q : ℝ} (hq0 : q ≠ 0) : qInt2 q ≠ 0 := by
  unfold qInt2
  intro h
  have hc : q * (q + q⁻¹) = q ^ 2 + 1 := by
    rw [mul_add, mul_inv_cancel₀ hq0]; ring
  have h2 : q ^ 2 + 1 = 0 := by rw [← hc, h, mul_zero]
  linarith [sq_nonneg q]

/-- **Hard singularity at `r = ℏ_q`** — derived sorry-free.

    For `q ≠ 0`, `q ≠ 1` the `q`-deformed kernel blows up at the
    `q`-Planck separation: `|[2]_q / (r² − ℏ_q²)| → ∞` as
    `r → ℏ_q` through `r ≠ ℏ_q`.  Genuine analysis (numerator is a
    nonzero constant, denominator tends to `0` and is eventually
    nonzero on the punctured neighbourhood since its only roots are
    `±ℏ_q` and `ℏ_q ≠ 0`), not a projected field. -/
-- Ref: [leitner2026] lem:nsi-q-deformed-kernel, quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.md
theorem nsi_q_kernel_hard_singularity {q : ℝ} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    Filter.Tendsto (fun r => |qDeformedKernel q r|)
      (nhdsWithin (hbarQ q) {r : ℝ | r ≠ hbarQ q}) Filter.atTop := by
  have hbne : hbarQ q ≠ 0 := hbarQ_ne_zero hq1
  have hnum : qInt2 q ≠ 0 := qInt2_ne_zero hq0
  -- `|kernel r| = |[2]_q| · |r² − ℏ_q²|⁻¹`
  have hker : ∀ r : ℝ,
      |qDeformedKernel q r| = |qInt2 q| * |r ^ 2 - hbarQ q ^ 2|⁻¹ := by
    intro r
    rw [qDeformedKernel, abs_div, div_eq_mul_inv]
  -- the denominator's absolute value tends to `0` from within `(0, ∞)`
  have hden : Filter.Tendsto (fun r : ℝ => |r ^ 2 - hbarQ q ^ 2|)
      (nhdsWithin (hbarQ q) {r : ℝ | r ≠ hbarQ q})
      (nhdsWithin 0 (Set.Ioi 0)) := by
    rw [tendsto_nhdsWithin_iff]
    constructor
    · -- continuity: the value at `r = ℏ_q` is `|ℏ_q² − ℏ_q²| = 0`
      have hc : Continuous fun r : ℝ => |r ^ 2 - hbarQ q ^ 2| :=
        ((continuous_pow 2).sub continuous_const).abs
      simpa using (hc.tendsto (hbarQ q)).mono_left nhdsWithin_le_nhds
    · -- eventual positivity: the denominator's only roots are `±ℏ_q`
      have h1 : ∀ᶠ r in nhdsWithin (hbarQ q) {r : ℝ | r ≠ hbarQ q},
          r ∈ {r : ℝ | r ≠ hbarQ q} := eventually_mem_nhdsWithin
      have hne : hbarQ q ≠ -hbarQ q := fun h => hbne (by linarith)
      have h2 : ∀ᶠ r in nhdsWithin (hbarQ q) {r : ℝ | r ≠ hbarQ q},
          r ≠ -hbarQ q :=
        (eventually_ne_nhds hne).filter_mono nhdsWithin_le_nhds
      filter_upwards [h1, h2] with r hr hr'
      rw [Set.mem_Ioi, abs_pos]
      intro h
      rcases sq_eq_sq_iff_eq_or_eq_neg.mp (sub_eq_zero.mp h) with h3 | h3
      · exact hr h3
      · exact hr' h3
  -- reciprocal of the denominator diverges; scale by the nonzero numerator
  have hinv : Filter.Tendsto (fun r : ℝ => |r ^ 2 - hbarQ q ^ 2|⁻¹)
      (nhdsWithin (hbarQ q) {r : ℝ | r ≠ hbarQ q}) Filter.atTop :=
    hden.inv_tendsto_nhdsGT_zero
  exact (hinv.const_mul_atTop (abs_pos.mpr hnum)).congr
    fun r => (hker r).symm

/-- Data of the NSI `q`-deformed-kernel claim
    ([`lem:nsi-q-deformed-kernel`]).  All fields are *inputs*; none
    is the conclusion. -/
class NsiQDeformedKernelContext (E : Type*) [NormedAddCommGroup E] where
  /-- Substrate deformation parameter `q`. -/
  q : ℝ
  /-- Vortex filament curve `ϱ : ℝ → E`. -/
  ϱ : ℝ → E
  /-- Trace-side kernel `K_cat s t` inherited by the categorical mass
      of the filament (the `q`-deformed commutator's replacement of
      the classical `1/r²`). -/
  K_cat : ℝ → ℝ → ℝ
  /-- The q-deformed commutator. -/
  qDeformedCommutator : ℝ → ℝ → ℝ
  /-- The categorical kernel is derived from the q-deformed commutator evaluated on the filament. -/
  K_cat_eq : ∀ s t, K_cat s t = qDeformedCommutator q ‖ϱ s - ϱ t‖
  /-- The q-deformed commutator matches the concrete q-deformed kernel for q ≠ 1. -/
  qDeformedCommutator_eq : ∀ r, q ≠ 1 → qDeformedCommutator q r = qDeformedKernel q r

/-- **Identification of the inherited kernel** — the trace-side
    kernel of the filament's categorical mass equals the concrete
    `q`-deformed kernel `[2]_q / (‖ϱ(s) − ϱ(t)‖² − ℏ_q²)` for
    `q ≠ 1`.  Sorry-free, but §3b-**conditional** on
    `NsiQDeformedKernelContext`: the un-formalised content (the
    `q`-deformed commutator and `q`-Hodge star) is carried as the explicit
    hypothesis fields `K_cat_eq` and `qDeformedCommutator_eq`, from which
    the identification is derived.  The premise is assumed, not
    established — see AGENTS.md §"Conditional-proved ≠ premise-established". -/
-- Ref: [leitner2026] lem:nsi-q-deformed-kernel, quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.md
theorem nsi_q_kernel_identification {E : Type*} [NormedAddCommGroup E]
    [ctx : NsiQDeformedKernelContext E] (s t : ℝ) (hq1 : ctx.q ≠ 1) :
    ctx.K_cat s t = qDeformedKernel ctx.q ‖ctx.ϱ s - ctx.ϱ t‖ := by
  rw [ctx.K_cat_eq, ctx.qDeformedCommutator_eq _ hq1]

/-- **`q`-deformed commutator replaces `1/r²` with a hard kernel at
    `r = ℏ_q`** ([`lem:nsi-q-deformed-kernel`]) — the resolving
    declaration for `lean.ref`
    `qou:QOU.BraidsKnots.nsi_q_deformed_kernel`.

    Conjoins the two parts of the manuscript lemma: (1) the
    identification of the inherited trace-side kernel with
    `[2]_q / (r² − ℏ_q²)` at `r = ‖ϱ(s) − ϱ(t)‖` (**sorry-free but
    §3b-conditional** — `nsi_q_kernel_identification` derives it from the
    context's `K_cat_eq` / `qDeformedCommutator_eq` hypothesis fields,
    which is where the un-formalised commutator content sits), and (2) the
    hard singularity at `r = ℏ_q` (**derived sorry-free** in
    `nsi_q_kernel_hard_singularity` from the concrete kernel).
    Neither conjunct projects a conclusion field. -/
-- Ref: [leitner2026] lem:nsi-q-deformed-kernel, quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.md
theorem nsi_q_deformed_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : NsiQDeformedKernelContext E] (s t : ℝ)
    (hq0 : ctx.q ≠ 0) (hq1 : ctx.q ≠ 1) :
    ctx.K_cat s t = qDeformedKernel ctx.q ‖ctx.ϱ s - ctx.ϱ t‖ ∧
    Filter.Tendsto (fun r => |qDeformedKernel ctx.q r|)
      (nhdsWithin (hbarQ ctx.q) {r : ℝ | r ≠ hbarQ ctx.q}) Filter.atTop :=
  ⟨nsi_q_kernel_identification s t hq1,
   nsi_q_kernel_hard_singularity hq0 hq1⟩

/-- At the classical point `q = 1`, `ℏ_q = 0` and `[2]_q = 2`, so the
    concrete kernel `qDeformedKernel 1 r` collapses identically to `2 / r ^ 2`. -/
theorem qDeformedKernel_at_one (r : ℝ) :
    qDeformedKernel 1 r = 2 / r ^ 2 := by
  have hb : hbarQ 1 = 0 := by
    unfold hbarQ
    norm_num
  have h2 : qInt2 1 = 2 := by
    unfold qInt2
    norm_num
  unfold qDeformedKernel
  rw [hb, h2]
  ring

/-- Exact algebraic decomposition of the difference between the `q`-deformed
    kernel `qDeformedKernel q r` and its classical `q = 1` counterpart `2 / r ^ 2`
    away from `r = 0` and `r = ±ℏ_q`. -/
theorem qDeformedKernel_sub_classical (q r : ℝ)
    (hr : r ^ 2 ≠ 0) (hd : r ^ 2 - hbarQ q ^ 2 ≠ 0) :
    qDeformedKernel q r - 2 / r ^ 2
      = ((qInt2 q - 2) * r ^ 2 + 2 * hbarQ q ^ 2)
        / (r ^ 2 * (r ^ 2 - hbarQ q ^ 2)) := by
  unfold qDeformedKernel
  have hden : r ^ 2 - hbarQ q ^ 2 ≠ 0 := hd
  rw [div_sub_div _ _ hden hr]
  ring

/-- Concrete `NsiQDeformedKernelContext` over `E = ℝ` at substrate parameter `q₀`:
    witnesses that the context class is inhabited for every `q₀ : ℝ`. -/
noncomputable def concreteNsiQDeformedKernelContext (q₀ : ℝ) :
    NsiQDeformedKernelContext ℝ where
  q := q₀
  ϱ := id
  K_cat := fun s t => qDeformedKernel q₀ ‖s - t‖
  qDeformedCommutator := qDeformedKernel
  K_cat_eq := fun _ _ => rfl
  qDeformedCommutator_eq := fun _ _ => rfl

/-- Inhabitation witness for `NsiQDeformedKernelContext ℝ` at `q₀`. -/
theorem nsiQDeformedKernelContext_inhabited (q₀ : ℝ) :
    ∃ ctx : NsiQDeformedKernelContext ℝ,
      ctx.q = q₀ ∧ ∀ s t : ℝ, ctx.K_cat s t = qDeformedKernel q₀ ‖s - t‖ :=
  ⟨concreteNsiQDeformedKernelContext q₀, rfl, fun _ _ => rfl⟩

end QOU.BraidsKnots
