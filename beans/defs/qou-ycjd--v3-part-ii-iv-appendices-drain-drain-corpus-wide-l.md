---
# qou-ycjd
title: 'V3 [Part II-IV & Appendices Drain]: Drain Corpus-Wide L1 (671), L2 (2,513) & L3 (1,135) Fourth-Wall & Voice Leaks Outside Ch 1-2'
status: in-progress
type: task
priority: normal
tags:
    - voice-audit
    - fourth-wall-lean
    - exposition
created_at: 2026-11-19T08:35:24Z
updated_at: 2026-11-20T17:45:00Z
parent: qou-d4kh
---

## Scope: Chapters 3–21, Introduction, Glossary, Notation & Appendices (`4,319` L1–L3 hits outside Ch 1–2)

Source witness: `computations/audits/monograph-lean-and-voice-leak-audit.witness.json`

Drain all remaining fourth-wall Lean prose mentions (Class L1: `671` hits outside Ch 1–2), backticked Lean identifiers / `.lean` filenames / raw block IDs in narrative prose (Class L2: `2,513` hits outside Ch 1–2), and first/second-person pronouns (Class L3: `1,135` hits outside Ch 1–2) in chapter waves:

1. **Wave A — Front Matter & Remaining Part I (`introduction`, `models-of-qous`, `lifting-and-descent`):**
   - `introduction` (`5` L1, `0` L2, `25` L3 = `30`)
   - `models-of-qous` (`0` L1, `0` L2, `34` L3 = `34`)
   - `lifting-and-descent` (`3` L1, `10` L2, `93` L3 = `106`)
2. **Wave B — Part II Structural Mechanics (`braids-and-knots` through `gravity-spacetime`):**
   - `braids-and-knots` (`44` L1, `53` L2, `18` L3 = `115`)
   - `brings-surface` (`9` L1, `68` L2, `36` L3 = `113`)
   - `knots-particles-confinement` (`8` L1, `37` L2, `50` L3 = `95`)
   - `eightfold-way` (`18` L1, `83` L2, `2` L3 = `103`)
   - `mass-endomorphism` (`54` L1, `316` L2, `87` L3 = `457`)
   - `climax-volume-mass` (`5` L1, `24` L2, `22` L3 = `51`)
   - `mass-theory` (`197` L1, `948` L2, `78` L3 = `1,223`)
   - `nuclear-interactions` (`8` L1, `27` L2, `59` L3 = `94`)
   - `gravity-spacetime` (`0` L1, `0` L2, `7` L3 = `7`)
3. **Wave C — Part III Physical Realization (`predicted-spectra` through `organic-chemistry`):**
   - `predicted-spectra` (`89` L1, `210` L2, `123` L3 = `422`)
   - `observations` (`13` L1, `81` L2, `91` L3 = `185`)
   - `molecular-construction` (`9` L1, `24` L2, `36` L3 = `69`)
   - `organic-chemistry` (`0` L1, `0` L2, `8` L3 = `8`)
4. **Wave D — Part IV Dynamics, Information, Emergence (`fluid-dynamics` through `q-geometric-langlands`):**
   - `fluid-dynamics` (`5` L1, `51` L2, `42` L3 = `98`)
   - `stochastic-mechanics` (`83` L1, `135` L2, `11` L3 = `229`)
   - `information-theory` (`16` L1, `62` L2, `101` L3 = `179`)
   - `measurement-observation` (`0` L1, `0` L2, `4` L3 = `4`)
   - `q-geometric-langlands` (`1` L1, `19` L2, `29` L3 = `49`)
5. **Wave E — Back Matter & Appendices (`glossary` through `notation`):**
   - `glossary` (`18` L1, `39` L2, `12` L3 = `69`)
   - `appendix-knot-periodic-table` (`4` L1, `15` L2, `8` L3 = `27`)
   - `appendix-knot-operations-archimedean` (`0` L1, `0` L2, `1` L3 = `1`)
   - `appendix-transfer-matrices` (`0` L1, `0` L2, `2` L3 = `2`)
   - `appendix-mass-binding-algorithms` (`7` L1, `81` L2, `4` L3 = `92`)
   - `appendix-standard-model` (`11` L1, `13` L2, `4` L3 = `28`)
   - `appendix-qvalues` (`4` L1, `24` L2, `4` L3 = `32`)
   - `appendix-surreals` (`28` L1, `102` L2, `72` L3 = `202`)
   - `appendix-surreals-archimedean` (`3` L1, `11` L2, `15` L3 = `29`)
   - `index-of-definitions` (`14` L1, `3` L2, `0` L3 = `17`)
   - `notation` (`15` L1, `77` L2, `57` L3 = `149`)

## 2026-11-20 — W14 (https://claude.ai/code/session_01VQDpPgB5vPb2GEcGuZ9xxN)
Hit list regenerated with `voice-leak-audit.ts` (see PR #8538 + audit doc). Drain NOT started: content sweep is ask-first; framed ask posted on #8526. 926 of the 1,052 L2 `block-id` hits (388 files) are mechanically fixable from target titles.

## 2026-11-20 (afternoon) — W14: owner approved options 1, 2, 3, 5 live (not 4)
- #8563 Part I (Ch 1–2): L1/L2/L3 to 0 in both chapters. L4 (69) left: premature-q is V0 (`qou-ig2d`) structural work; 40 forward links include ~13 proof dependency inversions needing block reordering.
- #8566 mechanical: 914 raw-label link texts -> target titles (scripts/voice-drain-link-titles.ts).
- #8567 gate: voice-leak-audit --check-baseline ratchet + /prepare-merge §3 step.
- #8569 (stacked on #8566) option 3: mechanical slice + hand pass of stochastic-mechanics, eightfold-way, braids-and-knots, predicted-spectra. Paper-wide L1 672 -> 460, L2 2335 -> 1609.
- Remaining option 3: mass-theory, mass-endomorphism, appendix-surreals, information-theory, observations, notation, glossary, etc. (~460 L1, ~1,230 L2 non-repo-file). 25 caveat-bearing '## Lean' sections left for hand restatement. predicted-spectra Mathlib-infrastructure blocks (mathlib-filler, upstream-mathlib-additions, *formalization-status*) need an owner call on whether they belong in the paper.
- Option 4 (corpus first-person) NOT approved; L3 outside Part I untouched.


## 2026-11-20 — W14b duplicate (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws)
A scheduled sibling (W14b) redid options 2/1/5/3 as PRs #8577/#8584/#8585/#8588 without first seeing W14's #8563/#8566/#8567/#8569. All four W14b PRs are withdrawn to draft. Distinct W14b output: Part I L4 fixes and rem:q-generic-ground-ring (#8577); mass-theory '## Lean' restatements (12 sections #8569 leaves) and mass-theory L3 (#8588). Owner comparison and choice: #8526 comment 7042945374, which also flags that the two records of the ruling disagree on option 4. Child beans for the remaining waves: qou-t5iz, qou-a1k9, qou-rfp0, qou-e7ku, qou-qdf6, qou-tztx (counts from the W14b stack; re-measure on W14's). Content inconsistency found: qou-w14g.

## 2026-11-20 (evening) — W14 option-3 waves done on #8569
All chapters except Ch1-2 (in #8563) hand-drained. Paper-wide L1 672 -> 107, L2 2335 -> 457, failing blocks 1330 -> 764 (#8566 + #8569). What remains is blocks whose subject IS Lean/code: ~25 Mathlib-infrastructure blocks, appendix-mass-binding-algorithms (Python-API contract by design), notation/glossary/index-of-definitions, ~15 leftover sites. Framed as a second [W14 ask] on #8526 (groups 1-4; recommendation 1b, 2a, 3a, 4a; default leave).
