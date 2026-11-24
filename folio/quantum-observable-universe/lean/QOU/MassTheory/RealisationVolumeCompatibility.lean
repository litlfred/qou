/-
# conj:archimedean-realisation-volume-compatibility — the motivic-realization coincidence, as a §3b class

**This file REFRAMES a placeholder; it does NOT prove the volume conjecture and does NOT close any
gate** (AGENTS.md §"Axiomatization is NOT a Proof"). The previous body was the vacuous placeholder
`∃ V, V = V` (`use 0,0,0`), which asserts nothing. It is replaced with a content-bearing §3b
conjecture class stating the **motivic** content (audit `2026-07-12-fibre-observable-categorical-not-analytic.md`
§3): a QOU volume class has **two distinct realizations** — the local archimedean realization `τ_∞`
(the Habiro-ring `q₀`-evaluation) and the topological / motivic realization `R_top` — and these two
*different* maps must **agree with the hyperbolic volume** `V_hyp` on every braid. That both
realizations of one motive coincide is the open conjecture (the motivic incarnation of the
fibre→observable passage); it is **not** analytic continuation.

* `RealisationVolumeCompatibility Braid` — a §3b class carrying the two realizations `tauInfty`,
  `Rtop` and the volume `Vhyp` as **fields** (three genuinely different maps `Braid → ℝ`), with the
  content field `compat : ∀ β, tauInfty β = Vhyp β ∧ Rtop β = Vhyp β` — the coincidence claim.
* the instance over `ℝ` witnesses the **shape** is inhabited (a triple satisfying `compat` exists);
  it is the shape-witness, **NOT** a claim that the framework's actual `τ_∞` / `R_top` coincide.
* `realisation_volume_compatibility` — the conditional consequence **derived** from the class: given
  the coincidence, the two realizations agree (`τ_∞ β = R_top β`). This is the motivic content:
  one motive, two realizations, one value.
* `compat_is_restrictive` — non-degeneracy: `compat` is a real constraint (not every triple of maps
  satisfies it), so the class asserts something (§3b-tax).

What is **NOT** proved: that the framework's genuine `τ_∞` (Habiro `q₀`-evaluation) and `R_top`
(motivic/topological realization) coincide with `V_hyp`. There is no instance for the framework's
actual realization functors — that coincidence is the open conjecture, forced-not-fitted by Habiro
rigidity (see `QOU.BraidKnot.Keystone.HabiroRigidity`) but not closed.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md
-- Ref: [kashaev1997] https://doi.org/10.1023/A:1007364912784
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

-- The class name intentionally repeats the namespace tail (per the block's `lean.ref`); the
-- resulting duplicated-namespace lint is cosmetic and disabled here.
set_option linter.dupNamespace false

namespace QOU.Archimedean.RealisationVolumeCompatibility

/-- **conj:archimedean-realisation-volume-compatibility (§3b class).** A QOU volume datum on a type
of braids carries **two distinct realizations** — the local archimedean realization `tauInfty` (the
Habiro-ring `q₀`-evaluation `τ_∞`) and the topological / motivic realization `Rtop` — together with
the hyperbolic volume `Vhyp`. The content (`compat`) is the **motivic coincidence**: both
realizations agree with `Vhyp` on every braid. That the framework's *actual* `τ_∞` and `R_top`
realize one motive this way is the open conjecture; the class only names the shape. -/
class RealisationVolumeCompatibility (Braid : Type*) where
  /-- Local archimedean realization `τ_∞`: the Habiro-ring `q₀`-evaluation of the volume class. -/
  tauInfty : Braid → ℝ
  /-- Topological / motivic realization `R_top` of the volume class. -/
  Rtop : Braid → ℝ
  /-- Hyperbolic volume of the braid. -/
  Vhyp : Braid → ℝ
  /-- **Content — the motivic coincidence.** Both realizations agree with the hyperbolic volume on
  every braid: `τ_∞ β = V_hyp β` *and* `R_top β = V_hyp β`. -/
  compat : ∀ β, tauInfty β = Vhyp β ∧ Rtop β = Vhyp β

/-- **The class is non-vacuous (shape-witness).** Taking all three realizations to be the identity
on `ℝ` gives a triple satisfying `compat` — the structural shape is inhabited. This witnesses the
shape is realizable; it does **not** assert that the framework's genuine `τ_∞` / `R_top` coincide
(there is no instance for the actual realization functors). -/
instance : RealisationVolumeCompatibility ℝ where
  tauInfty := id
  Rtop := id
  Vhyp := id
  compat := fun _ => ⟨rfl, rfl⟩

/-- **The `compat` field is a genuine restriction (§3b-tax non-degeneracy).** Not every triple of
maps satisfies the coincidence: constants `τ_∞ = 0`, `V_hyp = 1` violate it. So the class asserts
real content — it is not auto-satisfiable for arbitrary realizations. -/
theorem compat_is_restrictive :
    ¬ ∀ β : ℝ, (fun _ : ℝ => (0 : ℝ)) β = (fun _ : ℝ => (1 : ℝ)) β
        ∧ (fun _ : ℝ => (0 : ℝ)) β = (fun _ : ℝ => (1 : ℝ)) β := by
  intro h
  have := (h 0).1
  norm_num at this

/-- **Conditional consequence (motivic content), derived from the class — name-compat with the old
`lean.ref`.** Given the coincidence `compat`, the two realizations agree: `τ_∞ β = R_top β`. The
archimedean and the topological/motivic realizations of the one volume motive produce the same
value. This is fully verified **modulo the class instance**; the class instance for the framework's
actual realizations is the open conjecture (not proved here). -/
theorem realisation_volume_compatibility {Braid : Type*}
    [RealisationVolumeCompatibility Braid] (β : Braid) :
    RealisationVolumeCompatibility.tauInfty β = RealisationVolumeCompatibility.Rtop β := by
  obtain ⟨h1, h2⟩ := RealisationVolumeCompatibility.compat β
  rw [h1, h2]

end QOU.Archimedean.RealisationVolumeCompatibility
