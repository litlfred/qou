---
# qou-d4kh
title: 'EPIC: Drain Fourth-Wall Lean Leaks, First/Second-Person Voice & Part I Reading-Order Anachronisms Across Monograph'
status: todo
type: epic
priority: high
tags:
    - voice-audit
    - fourth-wall-lean
    - exposition
created_at: 2026-11-19T08:34:29Z
updated_at: 2026-11-20T17:45:00Z
parent: qou-lpep
---

## Overview & Motivation

Owner audit of Chapter 1 (`folio/quantum-observable-universe/quantum-universes/`) and Chapter 2 (`quantum-observable-universes/`) exposed four classes of fourth-wall, voice, and reading-order leaks that slipped past `folio/pipeline/paper-commentary-audit.ts` and `cat-harness-tools/pipeline/qa-checkers-voice.ts`:

- **Reproducible Scanner:** `computations/audits/monograph_lean_and_voice_leak_audit.py`
- **Machine-Counted Witness:** `computations/audits/monograph-lean-and-voice-leak-audit.witness.json` (`q0Anchor: "independent"`, `0` float64)
- **Parent Milestone:** `qou-lpep` (*Exposition and paper*)
- **Cross-Linked Sibling Epics / Beans:** `qou-mub3` (*Exposition drain and chapter work*), `qou-9iqh` (*Paper voice: remove audit/agent commentary from Ch1-2 + detector*)

---

## Four Leak Classes & Root Causes of Checker Gaps

1. **Class L1 (`lean-prose-mention` — `678` corpus hits; `4` in Ch 1, `3` in Ch 2):**
   - Explicit prose mentions of `Lean`, `Lean carrier`, `Lean sibling`, `Lean structure`, `Mathlib`, `proved formally`, `formalised in`, `discharges the axiom`.
   - **Why missed:** `folio/pipeline/paper-commentary-audit.ts` (lines 11–12 & 74) explicitly exempted naming Lean declarations/carriers unless followed within 80 chars by `does not | doesn't | cannot`.
2. **Class L2 (`lean-ident-in-prose` — `2,540` corpus hits; `10` in Ch 1, `17` in Ch 2):**
   - Backticked Lean FQNs (`` `QOU.AlgebraicSubstrate.IsQGeneric` ``), `.lean` filenames (`` `SU2EmergenceRankForced.lean` ``), Lean typeclasses/types (`` `CommRing` ``, `` `HochschildZero R A` ``, `` `[Add H]` ``), raw block-ID backticks (`` `def:quantum-universe` ``), and Lean snake/camel declaration names (`` `dimQK0_eq_evDimQ_chernCharacter` ``, `` `su2Character_one` ``, `` `exteriorSquareDim_ne_zero_iff` ``) in narrative `.md` prose where the $\forall$ badge and `.ts` `lean:` metadata are the sole formalization link.
   - **Why missed:** `qa-checkers-voice.ts` (`scanProse` line 180, `stripInlineCode` line 572) strips all backticked spans `` `...` `` before scanning.
3. **Class L3 (`first-second-person` — `1,224` corpus hits; `22` in Ch 1, `67` in Ch 2):**
   - First-person (`we`, `our`, `us`, `let's`) and second-person (`you`, `your`, `the reader will`) in narrative `.md` prose (e.g. `quantum-universe-axiom-motivation.md:5`, `axiom-independence.md:3`).
   - **Why missed:** `checkFirstPersonWork` (line 286) only matches work-tracker futures/pasts (`we'll add/fix`, `we should fix`), and `checkScholarlyDefault` (lines 744, 754) only matches `So what we...`, `Now we want...`, or `we proved/showed... above/earlier`.
4. **Class L4 (`chapter-order-anachronism` in Part I — `86` hits: `64` in Ch 1, `22` in Ch 2):**
   - **(L4a)** Premature Chapter 1 references to the substrate parameter $q$, quantum integers $[n]_q$, cyclotomic polynomials $\Phi_d(q)$, Hecke bases/algebras, $\mathrm{SU}_q(2)$, and `"past the archimedean wall"` (e.g. `quantum-universes/quantum-universe.md:28-38`) before $q$ is introduced in Chapter 2 Section 7 (`sec:substrate-parameter`).
   - **(L4b)** Forward cross-reference links `](#label)` in Chapters 1 and 2 pointing to blocks defined later in monograph reading order (e.g. `[Frobenius–Hopf algebra](#def:frobenius-hopf-substrate)` at `quantum-universe.md:4` pointing to Ch 2 §9).

---

## Corpus-Wide Summary Across All 36 Chapters & Appendices (`3,668` Active `.md` Files)

| # | Chapter / Appendix Directory | MDs | L1 (Lean) | L2 (`` `id` ``) | L3 (we/you) | L4 (Order) | Total |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `introduction` | 7 | 5 | 0 | 25 | 0 | **30** |
| 2 | `quantum-universes` | 62 | 4 | 10 | 22 | 64 | **100** |
| 3 | `quantum-observable-universes` | 313 | 3 | 17 | 67 | 22 | **109** |
| 4 | `models-of-qous` | 54 | 0 | 0 | 34 | 0 | **34** |
| 5 | `lifting-and-descent` | 128 | 3 | 10 | 93 | 0 | **106** |
| 6 | `braids-and-knots` | 133 | 44 | 53 | 18 | 0 | **115** |
| 7 | `brings-surface` | 181 | 9 | 68 | 36 | 0 | **113** |
| 8 | `knots-particles-confinement` | 169 | 8 | 37 | 50 | 0 | **95** |
| 9 | `eightfold-way` | 19 | 18 | 83 | 2 | 0 | **103** |
| 10 | `mass-endomorphism` | 133 | 54 | 316 | 87 | 0 | **457** |
| 11 | `climax-volume-mass` | 61 | 5 | 24 | 22 | 0 | **51** |
| 12 | `mass-theory` | 825 | 197 | 948 | 78 | 0 | **1223** |
| 13 | `nuclear-interactions` | 167 | 8 | 27 | 59 | 0 | **94** |
| 14 | `gravity-spacetime` | 6 | 0 | 0 | 7 | 0 | **7** |
| 15 | `predicted-spectra` | 305 | 89 | 210 | 123 | 0 | **422** |
| 16 | `observations` | 261 | 13 | 81 | 91 | 0 | **185** |
| 17 | `molecular-construction` | 79 | 9 | 24 | 36 | 0 | **69** |
| 18 | `organic-chemistry` | 27 | 0 | 0 | 8 | 0 | **8** |
| 19 | `fluid-dynamics` | 110 | 5 | 51 | 42 | 0 | **98** |
| 20 | `stochastic-mechanics` | 78 | 83 | 135 | 11 | 0 | **229** |
| 21 | `information-theory` | 178 | 16 | 62 | 101 | 0 | **179** |
| 22 | `measurement-observation` | 14 | 0 | 0 | 4 | 0 | **4** |
| 23 | `q-geometric-langlands` | 51 | 1 | 19 | 29 | 0 | **49** |
| 24 | `glossary` | 31 | 18 | 39 | 12 | 0 | **69** |
| 25 | `appendix-knot-periodic-table` | 15 | 4 | 15 | 8 | 0 | **27** |
| 26 | `appendix-knot-operations` | 12 | 0 | 0 | 0 | 0 | **0** |
| 27 | `appendix-knot-operations-archimedean` | 3 | 0 | 0 | 1 | 0 | **1** |
| 28 | `appendix-transfer-matrices` | 45 | 0 | 0 | 2 | 0 | **2** |
| 29 | `appendix-mass-binding-algorithms` | 21 | 7 | 81 | 4 | 0 | **92** |
| 30 | `appendix-standard-model` | 22 | 11 | 13 | 4 | 0 | **28** |
| 31 | `appendix-nf-witnesses` | 4 | 0 | 0 | 0 | 0 | **0** |
| 32 | `appendix-qvalues` | 19 | 4 | 24 | 4 | 0 | **32** |
| 33 | `appendix-surreals` | 100 | 28 | 102 | 72 | 0 | **202** |
| 34 | `appendix-surreals-archimedean` | 21 | 3 | 11 | 15 | 0 | **29** |
| 35 | `index-of-definitions` | 1 | 14 | 3 | 0 | 0 | **17** |
| 36 | `notation` | 13 | 15 | 77 | 57 | 0 | **149** |
| — | **TOTAL** | **3,668** | **678** | **2,540** | **1,224** | **86** | **4,528** |

## 2026-11-20 — W14b duplicate (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws)
A scheduled sibling (W14b) redid options 2/1/5/3 as PRs #8577/#8584/#8585/#8588 without first seeing W14's #8563/#8566/#8567/#8569. All four W14b PRs are withdrawn to draft. Distinct W14b output: Part I L4 fixes and rem:q-generic-ground-ring (#8577); mass-theory '## Lean' restatements (12 sections #8569 leaves) and mass-theory L3 (#8588). Owner comparison and choice: #8526 comment 7042945374, which also flags that the two records of the ruling disagree on option 4. Child beans for the remaining waves: qou-t5iz, qou-a1k9, qou-rfp0, qou-e7ku, qou-qdf6, qou-tztx (counts from the W14b stack; re-measure on W14's). Content inconsistency found: qou-w14g.
