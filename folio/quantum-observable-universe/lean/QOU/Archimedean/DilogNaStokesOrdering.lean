import QOU.Archimedean.DilogPartBIteratedLimit
import QOU.Archimedean.DilogPartBEulerTail

/-!
# Na-Stokes path-ordering selection for Dilog Part B — conditional class (§3b-cond)

**Conjecture carrier (primary) + one conditional theorem.**  This file formalises the
*ordering-selection* half of the 2026-07-26 owner na-Stokes insight
(coordination ledger `docs/coordination/dilog-part-b-cusp-attack.md`), and **only** that
half.  It packages the genuine OPEN hypothesis — that the physical Part-B observable is the
τ-shadow of a path-ordered holonomy, hence computed by the **iterated** (not joint) limit of
the regularized scalar sum — and *derives* the value `Li₂(x) − π²/3` from it plus the two
already-proved sorry-free bricks.  The class carries the **hypothesis**; the theorem
**derives** the conclusion.  Nothing here is wired to production.

## What is conjectural (the class) and what is proved (the theorem)

* **OPEN (class field, the na-Stokes identification).**  That the physical Part-B observable
  *is* the iterated limit of the specified scalar sums — i.e. that the archimedean shadow `τ`
  of the categorical path-ordered holonomy `𝒫exp` is realised by taking `q→1⁺` (mesh refine)
  *before* `ρ→1⁻` (path grow to the cusp), the ordered-refinement definition of a
  multiplicative integral.  This is a physics↔math bridge (a *modelling* claim about the
  observable), not a Lean-provable statement; it is the honest conjectural input.  The class
  takes **no** other conjecture class as a hypothesis, so it is a **primary conjecture**
  (§3b-tax; the primary/dependent split is derived from the instance binders — there are none).

* **PROVED (the two bricks the theorem feeds the hypothesis into).**
  - `wp1_outer_tendsto` (#4343, `DilogPartBIteratedLimit`): the iterated W-P1 bulk limit
    `fun ρ ↦ Li₂ x − Li₂ ρ → Li₂ x − π²/6` as `ρ → 1⁻` (sorry-free; the inner `q→1⁺`
    value `Li₂ x − Li₂ ρ` is `wp1_bulk_tendsto`).
  - `QOU.QPochhammer.euler_tail_asymptotic` (W-P2, `DilogPartBEulerTail`): the Euler /
    Dedekind-eta tail `→ π²/6` (sorry-free).

## Why this is NON-VACUOUS (anti-laundering, AGENTS.md "Axiomatization is NOT a Proof")

* The conclusion `Li₂ x − π²/3` appears in **no** class field.  The class fields carry two
  `Tendsto` propositions whose limits are the **unknown** field values `wp1Physical`,
  `wp2Physical`, plus the additive assembly `physicalPartB = wp1Physical − wp2Physical`.
* The theorem **derives** the closed values by `tendsto_nhds_unique` against the proved
  bricks (uniqueness of limits — genuine content), then combines by `ring`.  It is the
  §3b-cond pattern of `q_bkm_criterion.lean` (carry hypotheses, derive the conclusion), **not**
  a self-assuming projection (§3b-cond item 5).
* **No instance is provided** — the primary conjecture is left open (the honest state).

## What this does NOT claim

This file does **not** claim `−π²/3` is a non-abelian surface-ordering curvature/commutator
term.  That identification is a `no-match`: `−π²/3 = −2·Li₂(1)` is an *abelian* dilog cusp
value, and in the commutative scalar τ-shadow the surface-ordering defect provably vanishes
(`holonomy_perm`); see
[`docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md`](../../../../../docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md).
Only the *ordering selection* (iterated, not joint) is captured here — the sound half.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `LiTwo`, `Real.log`, `Real.pi`, and the one-sided filters
`𝓝[<] 1` live past the substrate→archimedean wall.  This is a downstream archimedean
assembly, not a generic-ring identity.

-- Ref: [leitner2026] docs/coordination/dilog-part-b-cusp-attack.md (2026-07-26 na-Stokes insight); bean qou-zbcj
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-/

namespace QOU.Archimedean

open Filter Topology QOU.QPochhammer

/-- **Na-Stokes path-ordering identification for Dilog Part B (primary conjecture).**

    Carries the genuinely-open hypothesis that the physical Part-B observable is the
    τ-shadow of a path-ordered holonomy, hence computed by the **iterated** limit of the two
    regularized scalar sums (W-P1 bulk + W-P2 tail), in the ordered-refinement `(q then ρ)`
    order — never the joint/symmetric limit (illegal on a `𝒫exp`).  The class asserts nothing
    provable-outright and no instance is fabricated; the value `Li₂ x − π²/3` is **not** a
    field — it is derived downstream in `naStokes_physical_partB_value`. -/
class NaStokesPartBOrdering (x : ℝ) where
  /-- The physical W-P1 (bulk) contribution — the unknown the identification pins. -/
  wp1Physical : ℝ
  /-- **na-Stokes identification, W-P1 (OPEN).**  The physical W-P1 value is the OUTER
      (`ρ→1⁻`) limit of the proved INNER bulk family `ρ ↦ Li₂ x − Li₂ ρ` (whose pointwise
      value is `wp1_bulk_tendsto`, #4343).  The identification of *that iterated limit* with
      the physical observable is the conjectural input; its numerical value is **not**
      asserted here. -/
  wp1_iterated_identification :
    Tendsto (fun ρ => LiTwo x - LiTwo ρ) (𝓝[<] (1 : ℝ)) (𝓝 wp1Physical)
  /-- The physical W-P2 (Euler-tail / Dedekind-eta) contribution — the second unknown. -/
  wp2Physical : ℝ
  /-- **na-Stokes identification, W-P2 (OPEN).**  The physical W-P2 tail is the `p→1⁻` limit
      of the regularized negative-factor Euler tail (`euler_tail_asymptotic`'s summand); its
      value is derived downstream, not asserted here. -/
  wp2_euler_tail_identification :
    Tendsto (fun p : ℝ => (1 - p) * ∑' m : ℕ, (-Real.log (1 - p ^ (m + 1))))
      (𝓝[<] (1 : ℝ)) (𝓝 wp2Physical)
  /-- The assembled physical Part-B observable. -/
  physicalPartB : ℝ
  /-- **Additive assembly** of Part B from its two ordered pieces: bulk minus tail.  Relates
      three unknowns; carries no closed value. -/
  partB_assembly : physicalPartB = wp1Physical - wp2Physical

/-- **Conditional value of the physical Part-B observable under the na-Stokes ordering.**

    *If* the na-Stokes identification holds (`[NaStokesPartBOrdering x]` — the OPEN hypothesis),
    *then* the physical Part-B value is `Li₂ x − π²/3`.

    Derived, not projected: `tendsto_nhds_unique` forces `wp1Physical = Li₂ x − π²/6`
    (against the proved `wp1_outer_tendsto`) and `wp2Physical = π²/6` (against the proved
    `QOU.QPochhammer.euler_tail_asymptotic`) by uniqueness of limits, then the additive
    assembly gives `(Li₂ x − π²/6) − π²/6 = Li₂ x − π²/3`.  The `−π²/3` is an *abelian* dilog
    cusp value (two `Li₂(1) = π²/6` boundary terms), **not** a claimed curvature term
    (see the audit cross-referenced in the module docstring). -/
theorem naStokes_physical_partB_value (x : ℝ) [nrm : NaStokesPartBOrdering x] :
    nrm.physicalPartB = LiTwo x - Real.pi ^ 2 / 3 := by
  have h1 : nrm.wp1Physical = LiTwo x - Real.pi ^ 2 / 6 :=
    tendsto_nhds_unique nrm.wp1_iterated_identification (wp1_outer_tendsto x)
  have h2 : nrm.wp2Physical = Real.pi ^ 2 / 6 :=
    tendsto_nhds_unique nrm.wp2_euler_tail_identification QOU.QPochhammer.euler_tail_asymptotic
  rw [nrm.partB_assembly, h1, h2]; ring

end QOU.Archimedean
