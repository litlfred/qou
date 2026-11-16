---
# qou-loqn
title: 'Impact analysis: catalogue all bare_mass / intrinsic_mass occurrences needing change'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T19:09:25Z
updated_at: 2026-11-16T19:07:00Z
parent: qou-wp3h
---

## Impact Analysis Catalogue (`bare_mass` / `intrinsic_mass` / `bareMass` / `m_bare` across `folio/` and `computations/`, 2026-11-16 — PR #8160)

Scanned `origin/main` (`dc12b128ccc4bb1cccf496d04e3d548db0c4501a`) across `folio/` and `computations/` (excluding historical `.qa.json` logs):

### 1. `bare_mass` (7 occurrences across 2 Lean files)
| File | Lines | Symbol / Usage | Disposition / Action |
|---|---|---|---|
| `folio/quantum-observable-universe/predicted-spectra/antiparticle-crossing-reversal.lean` | `82, 99` (plus docstrings `11, 81, 91`) | `theorem bare_mass_invariance` | **Fixed in PR #8160 (`qou-tknh`):** renamed to `topological_mass_invariance` (with `@[deprecated]` `abbrev bare_mass_invariance`), matching `QOU/Torsion/antiparticle_crossing_reversal.lean` (`m_topological` / `impl_topological_mass_invariance`). |
| `folio/quantum-observable-universe/observations/borromean-quark.lean` | `89, 93, 126, 129, 140` | `BorromeanQuark.bare_mass : ℝ → ℝ` field and instance | Tracked by sibling bean `qou-v266` / `qou-1fv0` (`rename bare_mass -> topological_mass in BorromeanQuark.lean + GapA4MuonBranching.lean`); note that the Lake modules `QOU/Observations/BorromeanQuark.lean` and `QOU/MassTheory/GapA4MuonBranching.lean` already renamed this field to `topological_mass`, leaving only the content-block sibling `observations/borromean-quark.lean`. |

### 2. `intrinsic_mass` / `intrinsicMass` / `"intrinsic mass"` (0 identifier occurrences; 4 prose/comment occurrences)
| File | Lines | Context | Disposition |
|---|---|---|---|
| `folio/quantum-observable-universe/lean/QOU/MassTheory/ElectronCountRigidity.lean` | `89` | Docstring: *"There is no intrinsic mass in the formula: only the ratio `m/mₑ` is predicted."* | **Keep (correct negative statement):** explicitly states that QOU has no intrinsic mass. |
| `computations/me_additive_term_structure.py` | `19, 195` | Docstring & print: *"so mass in QOU is relational -- there is no intrinsic mass."* | **Keep (correct negative statement):** explicitly explains relational vs intrinsic mass. |
| `computations/m_sym_error_budget.py` | `469` | Table header `"intrinsic mass-in-u (ppQ)"` | Refers to AME2020 atomic-mass-unit (`u`) uncertainty component in error budget; non-ontological. |

### 3. `bareMass` (19 occurrences across 2 content-block sibling `.lean` files)
| File | Lines | Symbol / Usage | Disposition |
|---|---|---|---|
| `folio/quantum-observable-universe/mass-theory/reidemeister-mass-invariance.lean` | `87, 91, 99, 101, 104-106, 152-153, 202, 211, 216, 239-241` | `axiom bareMass : KnotDiagram → R_q`, `bareMass_R{1,2,3}_invariant`, `class BorromeanQuark (bareMass : ℝ → ℝ)` | Content-block sibling of `reidemeister-mass-invariance.md` (which contrasts single-knot topological mass against multi-knot binding energy under R-I/II/III). Candidate for follow-up rename `bareMass -> topologicalMass` paired with prose update in `reidemeister-mass-invariance.md` (`83-103`, `24, 108, 116`). |
| `folio/quantum-observable-universe/predicted-spectra/hydrogen-shell-writhe.lean` | `61, 65, 74, 76` | `BorromeanQuark.bareMass : ℝ → ℝ`, `bareMass_pos` | Content-block sibling; candidate for follow-up rename `bareMass -> topologicalMass` alongside `observations/borromean-quark.lean` (`qou-v266`). |

### 4. `m_bare` / `*_bare` (22 occurrences)
- **Coupling & Markov-trace undressed vs $\delta_q$-dressed quantities (NOT bare mass):**
  - `folio/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.lean:131,169,180` (`alpha_em_bare`: undressed electromagnetic coupling before $\delta_q$ dressing — keep).
  - `computations/alpha_basis_knot_couplings.py:172`, `computations/probes/substrate_consistency_window_q_from_alpha_em_probe.py:182` (`inv_alpha_em_bare`, `q_from_bare_alpha_*` — bare EM coupling, keep).
  - `computations/delta_q_decoration.py:315,321` & `computations/yekutieli_volume_join.py:501` (`trM_bare`, `log_abs_trM_bare` — undressed Markov trace before $\delta_q$ decoration, keep).
  - False-positive substring matches on `barEven`: `BarParityClusterObstruction.lean:22,48` (`sym_barEven`), `BarParityRankOne.lean:245` (`qIntSym_barEven`), `trefoil_octahedral_shape_from_rep_probe.py:110` (`boost_norm_barEven2_minus_barOdd2`).

### 5. Prose `"bare mass"` occurrences in `folio/` and `computations/` (26 lines)
- **Fixed in PR #8160 (`qou-tknh`):** `folio/quantum-observable-universe/predicted-spectra/antiparticle-crossing-reversal.lean:11,81,91` updated to `"topological (relational) mass"`.
- **Remaining prose occurrences (distinguishing torus-knot zero-volume / single-knot mass from binding energy):**
  - `folio/quantum-observable-universe/brings-surface/torus-knot-generators-interpretation.md:4`
  - `folio/quantum-observable-universe/knots-particles-confinement/binding-knots-visual-inventory.md:7`
  - `folio/quantum-observable-universe/knots-particles-confinement/knot-particle-dictionary.md:24`
  - `folio/quantum-observable-universe/knots-particles-confinement/knot-particle-generation-consequences.md:3`
  - `folio/quantum-observable-universe/mass-theory/flavor-split-habiro-derivation.lean:20`
  - `folio/quantum-observable-universe/mass-theory/reidemeister-mass-invariance.{lean,md}`
  - `folio/quantum-observable-universe/observations/electron-immortality.md:22`
  - `computations/deuteron_from_scratch_ledger.py:169,579`, `computations/knot-particle-generation.py:148,154,327`, `computations/DERIVATION-STATUS.md:308`
  - Note: `folio/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md:36` uses `"bare mass number $A$"` (standard nuclear physics nucleon count $A$, not bare mass — keep).
