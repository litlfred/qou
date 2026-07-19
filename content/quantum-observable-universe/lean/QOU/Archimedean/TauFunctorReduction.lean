/-
# τ-functor construction — a REDUCTION SCAFFOLD (τ is NOT constructed here)

Bean `qou-gym0`. The categorical τ-functor (the Archimedean / observation /
Markov-trace functor of the canonical derivation chain, step 9) is the genuine
multi-week object that would discharge the categorical side of the
"loop weight = Hodge Gram" wall. This file does **NOT** construct it and does
**NOT** prove it (STRICT, AGENTS.md §"Axiomatization is NOT a Proof"): nothing
here is wired to production, no fit, and the two genuinely-open inputs are
threaded as *hypotheses* from existing, honestly-open conjecture classes —
they are used, not discharged.

What a genuine construction requires (five laws): τ : 𝐂 → 𝐕𝐞𝐜_ℝ braided
monoidal, with (F1) monoidality, (F2) braiding intertwining (R-matrix →
target braiding), (F3) trace realization (categorical trace = Markov trace
`tr_M = Σ_λ y_λ χ^λ`), (F4) the archimedean wall (`q → q₀ ∈ ℝ`), (F5) reality
→ Hodge (`TauRhoHodgeLift`). See
`docs/audits/2026-07-18-tau-functor-construction-reduction.md`.

What is proved here (sorry-free, genuine):

* `observationFrame ev tr` — the observation frame `τ_∞ = ev ∘ tr_M`, with the
  archimedean wall F4 modelled as an arbitrary ring hom `ev : R →+* ℝ`
  ("specialize the formal `q` to the substrate `q₀`") composed with a Markov
  trace `tr : H → R`.
* `observationFrame_cyclic` / `observationFrame_add` — GIVEN a `MarkovTrace`
  instance, `τ_∞` is cyclic (gauge-invariant) and additive. Derived, not
  assumed: the necessary condition for `τ_∞` to be a categorical trace (F3).
* `H3Concrete.obsH3_cyclic` — a NON-VACUOUS concrete instance: the `n=3`
  observation frame `ev ∘ H3.trM` is cyclic, from the already-proved
  `H3.trM_cyclic`. Discharges the `n=3` slice of F3 with real content — no axiom.
* `tau_construction_reduces` — the REDUCTION: threading the two existing open
  classes `[MarkovTrace R H tr]` (gap: general-`n` instance) and
  `[TauRhoHodgeLift g W Wbar]` (gap: the wall), it DERIVES the two properties
  the α_EM per-loop measure consumes — gauge-invariance of the observable and
  the equal Hodge split `Wbar.trace = W.trace`. Non-degenerate: both
  consequences are *derived* from the class fields, never restated (§3b-cond
  rule 5).

Honesty: `TauRhoHodgeLift` still has NO instance (the wall stands); this file
reduces "construct τ" to that instance + the general-`n` Markov instance +
the Hecke-category infrastructure Mathlib cannot yet express (F1/F2). It closes
nothing and wires nothing.

Base ring (§7c): everything upstream of the wall is generic over `[CommRing R]`;
`ℝ` enters ONLY through `ev : R →+* ℝ`, the archimedean evaluation — exactly the
substrate→archimedean cut.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import QOU.Machinery.MarkovTraceOnHecke
import QOU.Machinery.HeckeBraidedCategoryScaffold
import QOU.Archimedean.TauRhoHodgeLiftInterface
import Mathlib.Data.Real.Basic

namespace QOU.Archimedean.TauFunctorReduction

open QOU.Machinery
open QOU.Machinery.HeckeBraidedCategory
open QOU.Archimedean.TauRhoHodgeLiftInterface
open Matrix

/-- **The observation frame `τ_∞`.** Modelling the two composable halves of the
observation side of τ: the Markov trace `tr : H → R` (the Frobenius pairing
`tr_M`, pre-wall, generic `R`) followed by the archimedean evaluation
`ev : R →+* ℝ` (the wall F4 — "specialize `q` to the substrate `q₀`", a ring
hom). `τ_∞ = ev ∘ tr_M`. This is the *observation* half; the full τ additionally
carries the monoidal/braided structure (F1/F2) and the reality→Hodge lift (F5),
none of which this composition supplies. -/
def observationFrame {R H : Type*} [CommRing R]
    (ev : R →+* ℝ) (tr : H → R) (x : H) : ℝ := ev (tr x)

/-- **Gauge-invariance of the observable (part of F3), DERIVED.** Given a Markov
trace, the observation frame is cyclic: `τ_∞(xy) = τ_∞(yx)`. This is the
necessary condition for `τ_∞` to be a categorical trace — proved from
`MarkovTrace.cyclic`, not assumed. -/
theorem observationFrame_cyclic {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (ev : R →+* ℝ) (tr : H → R) [MarkovTrace R H tr] (x y : H) :
    observationFrame ev tr (x * y) = observationFrame ev tr (y * x) := by
  show ev (tr (x * y)) = ev (tr (y * x))
  rw [‹MarkovTrace R H tr›.cyclic x y]

/-- **Additivity of the observable, DERIVED.** From `MarkovTrace.map_add` and
`ev` a ring hom, `τ_∞` is additive — part of the `R`-linearity a fibre-functor
trace must respect. -/
theorem observationFrame_add {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (ev : R →+* ℝ) (tr : H → R) [MarkovTrace R H tr] (x y : H) :
    observationFrame ev tr (x + y)
      = observationFrame ev tr x + observationFrame ev tr y := by
  show ev (tr (x + y)) = ev (tr x) + ev (tr y)
  rw [‹MarkovTrace R H tr›.map_add x y, map_add]

/-! ## `n=3` concrete slice of F3 — non-vacuous, no axiom

The `H3.trM` Markov trace (proved M1/M2/M3 sorry-free over generic `R`) gives a
CONCRETE observation frame whose cyclicity is a theorem, not a hypothesis. One
of the five construction laws (F3) is realizable *now* at `n=3`. -/
namespace H3Concrete

/-- The `n=3` observation frame `ev ∘ H3.trM` on the `Fin 6` NF module of
`H₃(q)` (basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`). -/
noncomputable def obsH3 {R : Type*} [CommRing R]
    (ev : R →+* ℝ) (z h : R) (v : Fin 6 → R) : ℝ :=
  ev (H3.trM z h v)

/-- **Concrete `n=3` gauge-invariance.** The observation frame on the full
`H₃(q)` algebra product `mulNF` is cyclic — proved from the sorry-free
`H3.trM_cyclic`. A genuine (non-vacuous) realization of the F3 slice at `n=3`. -/
theorem obsH3_cyclic {R : Type*} [CommRing R]
    (ev : R →+* ℝ) (z h : R) (u v : Fin 6 → R) :
    obsH3 ev z h (H3.mulNF h u v) = obsH3 ev z h (H3.mulNF h v u) := by
  show ev (H3.trM z h (H3.mulNF h u v)) = ev (H3.trM z h (H3.mulNF h v u))
  rw [H3.trM_cyclic z h u v]

end H3Concrete

/-! ## The reduction -/

/-- **REDUCTION — constructing the observation side of τ reduces to two named
open items.** Threading the two existing, honestly-open conjecture classes as
hypotheses:

* `[MarkovTrace R H tr]` — the general-`n` Markov trace realizing
  `tr_M = Σ_λ y_λ χ^λ` (open: only `n=2,3` are concrete; general `n` needs the
  `Ind_{H_n}^{H_{n+1}}` stabilization);
* `[TauRhoHodgeLift g W Wbar]` — τ carries the fibre reality ρ to Hodge
  conjugation (open: THE wall, no instance anywhere),

this theorem DERIVES the exact two properties the α_EM per-loop measure
derivation consumes:

1. **gauge-invariance** of the observable (`τ_∞` cyclic), from the Markov trace;
2. the **equal Hodge split** `Wbar.trace = W.trace` (the ½), from the lift.

Neither is a class field — both are *derived* (§3b-cond rule 5, non-degenerate).
So "construct the observation side of τ" is reduced to exhibiting these two
instances (on top of the Hecke-category infrastructure F1/F2 that Lean cannot
yet state). This DOES NOT discharge either hypothesis; the wall stands. -/
theorem tau_construction_reduces {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (ev : R →+* ℝ) (tr : H → R) [MarkovTrace R H tr]
    {g : ℕ} {W Wbar : Matrix (Fin g) (Fin g) ℂ} [TauRhoHodgeLift g W Wbar]
    (x y : H) :
    observationFrame ev tr (x * y) = observationFrame ev tr (y * x)
      ∧ Wbar.trace = W.trace :=
  ⟨observationFrame_cyclic ev tr x y, TauRhoHodgeLift.equal_split⟩

/-- **Tower-stability of the observation frame, DERIVED from the Markov
stabilization (bean `qou-ep0a`).** Given the general-`n` Markov stabilization
`[MarkovStabilization …]` (the dependent conjecture in
`HeckeBraidedCategoryScaffold`), the observation frame is compatible with the
Hecke tower inclusion `ι`: `τ_∞(ι x) = τ_∞(x)`. This is the consequence that
makes `observationFrame` well-defined on the inductive-limit algebra — the
stabilization feeds the derived frame. Sorry-free, derived (not assumed);
`MarkovStabilization` still has no instance (general-`n` stays OPEN). -/
theorem observationFrame_stabilizes {R Hn Hn1 : Type*} [Field R] {q : R}
    [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    {σn : ℕ → Hn} {σn1 : ℕ → Hn1}
    [HeckeBraidedPresentation R q Hn σn] [HeckeBraidedPresentation R q Hn1 σn1]
    {ι : Hn →ₐ[R] Hn1} {trn : Hn → R} {trn1 : Hn1 → R}
    [MarkovStabilization R q Hn Hn1 σn σn1 ι trn trn1]
    (ev : R →+* ℝ) (x : Hn) :
    observationFrame ev trn1 (ι x) = observationFrame ev trn x := by
  show ev (trn1 (ι x)) = ev (trn x)
  rw [‹MarkovStabilization R q Hn Hn1 σn σn1 ι trn trn1›.stabilizes x]

end QOU.Archimedean.TauFunctorReduction
