---
# qou-e7xv
title: 38 content-block sibling .lean files do not compile — nothing in the corpus checks them
status: todo
type: task
priority: normal
created_at: 2026-09-03T22:46:23Z
updated_at: 2026-09-04T02:33:47Z
---

Audit: `docs/audits/2026-09-03-sibling-lean-compile-sweep.md`
Data:  `docs/audits/2026-09-03-sibling-lean-compile-sweep.tsv`

## Measured 2026-09-03

`lean`-direct on all 908 `.lean` under `content/quantum-observable-universe/`
outside `lean/`, then EVERY failure re-verified under a widened LEAN_PATH:

    raw failures                                        41
      harness: QOU-only LEAN_PATH, file imports UGB     -1
      harness: `import Mathlib` (aggregator olean absent) -2
    REAL                                                38   (4.2 %)

Both harness classes confirmed by re-running, not by inspection.
`vertex-algebra-relations.lean`: `unknown module prefix 'UGB'` under a
QOU-only path, exit 0 with all three paper packages. `Mathlib.olean` is
genuinely absent from the restore, so two files that `import Mathlib`
wholesale fail for a reason a real `lake build` would not have.

## Why nothing caught them

Siblings sit outside the Lake globs (`globs = ["QOU", "QOU.+"]`,
`srcDir = "."` = the `lean/` dir), so `lake build QOU` never sees them; CI is
`workflow_dispatch`-only; `lean-content-siblings.yml` gates content-block
siblings, not these.

## Largest shared causes

- `Inv GroundRing.R_q` fails to synthesise in **5 files** — ONE missing
  instance on the corpus's own ground ring, not five independent defects.
  Highest-leverage single fix in the list.
- 4 files fail at the PARSER.
- Mathlib drift: `Real.tendsto_log_mul_rpow_nhdsGT_zero`,
  `MonoidalCategory.whiskerRight_comp` -> `comp_whiskerRight`.
- `delta-max-uniform-bound.lean` imports `QOU.MassEndomorphism.JetTower`,
  which does not exist in source, and `QOU.BraidsAndKnots.MarkovTrace` where
  the tree spells the namespace `BraidKnot`. Absent olean AND absent source
  is what distinguishes this from a harness gap.
- Worst single file: `spin-involution-lp-dual-invariance.lean`, 24 errors.

## Scope

A sibling failing to compile is NOT automatically a false claim — most are
stale references and missing instances, not wrong mathematics. It means the
block's `lean.ref` points into a file that does not typecheck, so the
formalisation cannot be relied on as stated. Triage per file; do not read 38
as 38 refuted propositions.

## Already partly done on this branch

- `n-v-bring-action.lean` — was 8 parse errors (`Σ` used as a binder name);
  now exit 0, zero warnings, and its axiom + self-discharging instance removed.
- `braid-action-tensor.lean` — 5 errors -> 2 (bean `qou-8qby`).


## 🛑 CORRECTION (same day): the `Inv GroundRing.R_q` diagnosis above is WRONG

This bean and the audit first called the 5-file `Inv GroundRing.R_q` failure
"ONE missing instance on the corpus's own ground ring, not five independent
defects" and named it the highest-leverage single fix. **Retracted. Adding an
`Inv` instance is exactly what must not happen.**

`lean/QOU/GroundRingCore.lean` says so in its own docstring, on
`q_inv_param`:

  "Carried as its own declaration rather than written `q_param⁻¹`: `R_q` is a
   ring, not a field, so it has no `Inv` instance and `q⁻¹` cannot be written."

The absence is deliberate. An `Inv` instance on a non-field makes `x⁻¹`
elaborate to a junk value for every non-unit, so it would convert five
compile errors into five silently wrong formulas. Strictly worse than the
current state.

The real defect is at the five call sites, which write `(sp.field p)⁻¹` — the
inverse of an ARBITRARY ring element. In ℤ[q,q⁻¹] the indeterminate has an
inverse (`q_inv_param = T (-1)`); a general element does not. Each site needs
either `q_inv_param`, or an explicit inverse field carrying `q * q_inv = 1`
(the pattern used by `alternating_projection_weak_vertex`). That is a
per-site mathematical decision, not one-line infra.

Sites: information-theory/quantum-volume.lean,
quantum-observable-universes/{q-connection,q-ext-deriv,quantum-planck-constant,q-lie-bracket}.lean

Worth noting WHY the wrong fix was attractive: the "five files, one root
cause" framing. A shared error message is not a shared defect.


## UPDATE 2026-09-04: 38 -> 27, and the dominant cause is now clear

It is NOT Mathlib drift and NOT bad mathematics. **Migrations stop at the
sibling boundary.** A library object changes shape; every consumer inside the
Lake globs is updated because `lake build` forces it; the content-block
siblings are left behind because nothing builds them.

    SubstrateParameter split (categorical R_q / ArchimedeanSubstrateField ℝ)   6 files
    theorem specialised generic `Field R` -> ℝ, ascription left as `(q : R)`   1
    HeckeExpansion gained `(R : Type*) [Field R]` before `n`                   1
    HasPentagonRelation / HasBlochGroup given real fields instead of True-ish  1

That is 9 of the 11 repaired so far. The other two were a Lean-notation token
used as a binder name (`Σ`, `λ`) and orphaned docstrings.

CONSEQUENCE: a mechanically-enforced migration is NOT enforced here. Anyone
changing a library signature must grep `content/<paper>/**/*.lean` outside
`lean/` as a separate step — the compiler will not ask.

The Bloch-group case is the sharpest: the stranded sibling was WRONG, not
merely stale. It carried an instance with every field `:= trivial`, and the
library's strengthening (real `AddSubgroup` / `→+ ℝ` / torsion fields, its
docstrings saying "not a `True` placeholder") is exactly what stopped it
typechecking. The compile error was the guard working, and the fix was
deletion — supplying `⊥` and the zero hom would typecheck and assert nothing.

Fixed to ZERO errors and ZERO warnings so far (11):
  n-v-bring-action, quantum-volume, q-connection, q-ext-deriv,
  quantum-planck-constant, q-lie-bracket, substrate-parameter-exists,
  confinement-phase-stratification, gram-determinant-plancherel-ratio,
  flavor-mass-splitting-bound, bloch-group-quotient-construction,
  knot-factor-shell-closed

Improved but still failing (2): braid-action-tensor 5->2 (`qou-8qby`),
townsend-biot-savart-strain 9->7 (real-analysis proof drift, not names).

Re-verified against main after merging its 39 commits: those were library-side
and fixed none of the siblings.
