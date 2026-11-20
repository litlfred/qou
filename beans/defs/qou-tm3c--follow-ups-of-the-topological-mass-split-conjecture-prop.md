---
# qou-tm3c
title: 'Follow-ups of the topological-mass split: provable blocks now depending on conj:topological-mass, stale labels in Lean/compute/generated files'
status: in-progress
type: task
priority: high
created_at: 2026-11-20T09:10:00Z
updated_at: 2026-11-20T18:30:00Z
parent: qou-ncxf
---

Follow-ups to the split of `thm:topological-mass` into `conj:topological-mass` and `prop:topological-mass-upper-bound` (owner "Y", 2026-11-20; bean qou-27ys; PR on branch `claude/topological-mass-split-2026-11-20`).

## 1. Conjecture-propagation (AGENTS.md §3b): owner decision, not done
Three provable blocks now visibly depend on the open equality. It was always conjectural; the `theorem` label hid that.
- `prop:hecke-mass-trace` (`mass-theory/hecke-mass-trace.md:19`, "the topological decomposition descends to H_n(R,q)").
- `prop:topological-mass-formula` (`mass-theory/topological-mass-formula.md:29`, "derivation proceeds from the categorical decomposition").
- `cor:quantum-dilogarithm` (`lifting-and-descent/quantum-dilogarithm.md:1`, "the transient trace contribution ... evaluates to Φ_q(z_i)"). This one may only need the transient term's definition, not the equality, so it may be retargetable rather than demoted.
For each block the options are: demote to conjecture; restate as conditional per §3b-cond, which needs a non-degenerate hypothesis class; or retarget to the upper bound when only the bound is used. Not done without owner/W1 sign-off.

## 2. Stale `thm:topological-mass` mentions left on purpose
These are outside the content-block edit. W11 promised to edit no existing `.lean` file, and the compute belongs to W2.
- Lean docstrings and comments: `quantum-universes/topological-mass-formula.lean:10`, `mass-theory/mass-endomorphism-tower.lean:45`, `lean/QOU/MassDerivation.lean:57`, `lean/QOU/ArchimedeanMassFormula.lean:13`, `lean/QOU/Torsion/TopologicalMass.lean:62,135`, `mass-endomorphism/topological-mass-conjecture.lean:24,43`.
- Compute: `computations/mass-from-q-symbolic.py:425` (`w.set_content_block("thm:topological-mass")`) and its witness field `contentBlock`. Fixing it needs a producer re-run.
- Audit witnesses in `computations/audits/*.witness.json` record the old label; they are historical.
- `lean/QOU/Torsion/mass_decomposition_categorical.lean`: the self-assuming projection no longer has a content-block consumer. Delete or de-vacuify it (W8 scope).

## 3. Generated artifacts
- The `.jsonld` files of the 11 touched blocks were regenerated with `gen-block-jsonld` at the pinned platform 82b3899. Unrelated drift was reverted: a full run rewrote 3602 files, and the platform's namespace change from `folio-assistant-core:` to `folio-assistant-sci:` now shows on these 11 files only.
- `build-foreshadows` crashes at the pin (build-foreshadows.ts:163). `foreshadows.json` was hand-patched: 5 label strings changed from thm: to conj:. Re-run it once the platform tool works.

## 2026-11-20 W11b (PR #8575, branch claude/topological-mass-dependents-2026-11-20)
Claimed by W11b. The stalled-claim check passed: the bean was `todo` with no backing branch. Owner ruling 1(a) is PR #8526 comment 7041693067.
- **Item 1 done in #8575.** `cor:quantum-dilogarithm` was retargeted to `prop:topological-mass-upper-bound`, because its proof evaluates one transient term and never sums the terms. `prop:hecke-mass-trace` became `conj:hecke-mass-trace`, and `prop:topological-mass-formula` became `conj:topological-mass-formula`. `prf:hecke-mass-trace` became the remark `rem:hecke-mass-trace-sketch`. In the library file `QOU/Braiding/hecke_mass_trace.lean`, the self-projecting `def hecke_mass_trace` was removed. The trace split is now derived (`trace_split_of_phi_split`, sorry-free).
- §3b audit: violators went 257 → 250, with 0 new. Four more blocks cleared through the corollary: quantum-dilog-convergence, topological-decomposition-mass, recursive-atom-knot-atlas and rigid-monoidal-structural-gap-invariance.
- **Open: the five remaining dependents.** They are volume-tower-decomposition, cs-evaluation-faithfulness, local-substrate-q, terminal-resolution and tower-binding-energy. The framed ask is [W11b ask] on #8526, comment 7042623275. The recommendation is to cut the edges their text does not use. Not acted on.
- Item 2 partly done: the `thm:` mention in `lean/QOU/ArchimedeanMassFormula.lean` is fixed. The `topological-mass.ts` authorNote now says "Demoted from thm:".

## 2026-11-20 tm (PR #8581, branch claude/topological-mass-equality-2026-11-20)
Not a closure of anything here. Proved (sorry-free, `QOU/Torsion/TopologicalMassEquality.lean`) that `conj:topological-mass` ⟺ all trace pieces pairwise on a common ray (`mass_decomposition_eq_iff`), with strict inequality under anti-alignment. Full note on qou-27ys. Consequence for this bean's §3b dependents: anything that *uses* the equality inherits exactly the open alignment condition; a dependent can be restated conditionally on a ray-alignment hypothesis (non-degenerate: it is a hypothesis on the pieces, not the conclusion).
- **2026-11-20, later:** the owner chose option 2 live, then "retarget to CAL-2" for the q₀ pair. Both are done on #8575.
  - Edges cut: `volume-tower-decomposition` (also clears `cs-evaluation-faithfulness`) and `tower-binding-energy`.
  - `local-substrate-q` and `terminal-resolution` now point at `def:three-calibration-discipline`.
  - §3b audit: `origin/main` 247 → branch 237, 0 new. No sole-mass dependents remain.
  - **Still open:** the CAL-2 block itself reaches `conj:wigner-axiom` plus 3 others, through `prop:substrate-consistency-window` and `prop:calibration-cohomology-alignment`. Pre-existing and not framed yet.
  - Also still open: the leftover `thm:topological-mass` mentions from item 2.
- **2026-11-20, CAL split (PR #8611, stacked on #8575).** The owner asked why CAL-2 depended on conjectures, and then chose to split the definition from the claim and to fix the sl2 cycle.
  - **Findings.** The block `def:three-calibration-discipline` mixed a definition with a universal claim: every mass factors as m_e^a m_π^c Q(q₀). Its Lean headline theorem just returned the class field holding that claim. `prop:three-calibration-inputs` restated the same claim, and its Lean `∃ f, obs = f …` held for every `obs`. `prop:calibration-cohomology-alignment` had a Lean self-projection plus `2+1=3 := rfl`. The links to conjectures came from two defects: 10–14-hop chains through remarks (reaching `conj:wigner-axiom`), and a `uses[]` cycle between the sl2 recurrence and the conserved-quantity block (reaching `conj:binding-manybody`).
  - **Done.**
    - The definition is now pure: `QOU.Observations.CalibrationTriple` proves q₀ is the unique root, sorry-free.
    - `conj:three-calibration-inputs` has the class `ThreeCalibrationFactorisation`.
    - `conj:calibration-cohomology-alignment` lost its Lean sibling.
    - The sl2 back-edge is cut.
    - 20 compute producers were retargeted to the definition and re-run.
    - §3b audit: 237 → 234, with 0 new. `local-substrate-q` and `terminal-resolution` are now clear.
  - **Left.**
    - `qbeta_level_k_binding_operator_probe` crashes on main: `TypeError: mpf from list` at line 396, plausibly the mpmath version.
    - Docstring-only `prop:three-calibration-inputs` mentions remain in `binding_canonical`, `isotope_record_schema` and `rho_k_full_via_wenzl_lr`. They were left so the scriptHash and import cone don't drift.
    - `prop:sl2-prolongation-recurrence` and `prop:electron-period-base` still reach `conj:wigner-axiom` through remark chains. That path was not examined.
- **2026-11-20, later (PR #8611).**
  - **Wigner entry edge.** 108 of the 109 Wigner-axiom reaches came through one edge, `def:archimedean-condition` → `rem:three-euler-characteristics`, which is a terminology pointer. Cutting it took §3b violators from 234 to 124.
  - **Remark-only edges.** The owner chose to review them one by one. 28 blocks were reached only through remark, prose or example edges, and those came down to 15 distinct edges. All 15 were cut after reading each source block: 12 not cited, 3 cited only as pointers. Violators went from 124 to 99.
  - **Total for #8611:** 237 → 99 violators, with 0 new.
