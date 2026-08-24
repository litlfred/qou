# Functor-taxonomy follow-up — remaining "functor" claims (items 1–3)

**Date:** 2026-08-22
**Branch:** `claude/functor-taxonomy-followup-2026-08-22`
**Predecessor:** [`2026-07-11-archimedean-functor-taxonomy.md`](2026-07-11-archimedean-functor-taxonomy.md)
(PR #3504, merged — resolved the *archimedean* cluster: `R_top`, `τ_arch`,
`𝓕_Arch`/standard-part, and the Lean `MotivesArchimedean` upgrade).

Owner picked all three remaining catalog items (1 + 3 + 2). **Each was
re-verified against current `main` before editing.** The headline result:
the predecessor's binary "No" verdicts over-stated the remaining problem.
Most of the surface is either already honest or a naming-synonym question,
not a functor-vs-map category error. Applying the anti-over-claim discipline,
the edits are limited to genuine overstatements; where the code is already
honest it was left alone and recorded as such.

## Item 1 — Observation Frame / Markov trace τ — **NO FIX (already correct)**

Re-verified: nothing calls the Observation Frame a non-functor "functor".
Where "Observation Frame" appears with "functor"
(`mass-theory/hoefsmit-scattering-pipeline.md:40,74`), the corpus says
*"the observation frame $\tau$ **is the fibre functor** of the Tannakian
category $(\mathbf{C}, A, \tau)$"* — which is correct: τ is a genuine
functor, and its *evaluation* on a knot complement yields the geometric
invariant. The Lean `Obs` in
`lean/QOU/BraidKnot/FrobeniusSelfDualityForcesLPDualExtraction.lean` is
honestly typed `Obs a : A → R` with the docstring "(a linear functional)"
and an `Obs_add` additivity theorem. **No mislabel; no edit.**

## Item 2 — standalone "functors" — **1 real fix + 2 light notes + 1 none**

Deep investigation (all four `.lean` byte-identical to `origin/main`; none
import `CategoryTheory`; none load-bearing on functoriality):

| # | File / decl | Genuine functor? | What it actually is | Disposition |
|---|---|---|---|---|
| 1 | `CMBFunctor.lean` `structure CMBFunctor` | **No** | object-map `CMB : Aeon → M` (one abelian group `M`), pinned `jetColimit ∘ boundary`; no morphism-map | **docstring note added** — prose oversold a "composite of two functors into `Mod_R`" |
| 2 | `HorizonFunctor.lean` `structure HorizonFunctor` | **No** | set-valued map `boundary : Aeon → Set Config` | **one-line note added** — prose already honest (power-set target `𝒫`) |
| 3 | `FlavorDressing/FlavorDressingFunctor.lean` `class FlavorDressingFunctor` | **No** (defensible) | typeclass field `μ : Flavor → ℝ` + `μ_pos`; `Flavor` discrete ⇒ functor-out-of-discrete = object-map | **note added** — softened the unbacked "natural transformations" claim |
| 4 | `AppendixSurreals/CasimirModeCountFunctor.lean` `class PlateModeCountFunctor` | **No** | ℝ-valued standard-part interface `modeCountDiff : ℝ → ℝ → ℝ` | **NONE** — file already states "the target type, not the construction"; the genuine functor is explicitly unbuilt |

None of the four is a `CategoryTheory.Functor`; in every case "functor" is
decorative naming and nothing downstream uses a morphism-map or functor law.
Edits are docstring-only (zero compilation impact). No genuine upgrade is
needed for the surrounding proofs to stand.

## Item 3 — "forgetful functor τ" / codomain sweep — **NOT errors; 1 register note**

The ~10 sites that write `τ : C → Vec_ℝ` or "the **forgetful functor** τ"
(`tau-notation.md`, `quantum-observable-universe.md`,
`quantum-observable-universe-exists.md`, …) are **not category errors**: τ
is a genuine functor, and "forgetful functor" is the *classical Tannakian
name* for the fibre functor (Rep(G) → underlying modules, forgetting the
coaction). The core QOU definition — *"a QOU is $(\mathbf{C}, A, \tau)$ with
the forgetful functor τ faithful"* — is standard and correct.

The only genuine issue is terminological: the register's own table lists
"fibre functor τ" and "forgetful functor U" as *distinct* rows, which reads
as if τ is not the forgetful functor. **Fix: a reconciliation note added to
`notation-collisions.md`** — "forgetful functor τ" and "fibre functor τ"
name the *same* genuine functor at different codomain levels (the classical
forgetful τ is the composite `U ∘ τ : C → Vec_ℝ`, row 2 of the composite
table); only the intermediate `U : Arch → Vec_ℝ` is a distinct forgetful
arrow. **The core definition blocks need no change** — churning them would
fight correct classical usage.

## Net

- **Edits:** CMB/Flavor/Horizon docstring notes (item 2), one register
  reconciliation note (item 3). All docstring/prose only.
- **Left as-is (verified honest):** Observation Frame (item 1), Casimir
  (item 2 #4), and every core "forgetful functor τ" definition block
  (item 3).
- **Takeaway:** after the archimedean cluster (PR #3504), the residual
  "functor" mislabels are minor and non-load-bearing. The framework's one
  genuine, load-bearing functor is the fibre functor τ; the naming hygiene
  around it is now consistent.
