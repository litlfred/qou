# Coordination ledger — Lean frontier (sorry-closing / honesty)

## 2026-07-05 — PR #3401 (claude/lean-frontier-queue-jfs81f)

**Scope:** `SpechtStandardBasisCore.lean` (Garnir core), `frobenius_positivity_filter.lean`/`.md` (particle-interactions), audit doc.

- **#3255** (OV brick-5, Young seminormal) — same Specht/OV Lean cluster; posted intent (Garnir lemma in `SpechtStandardBasisCore` after `polytabloid_colStab_smul`; flag if brick-5 touches that file). [comment](https://github.com/litlfred/qou/pull/3255#issuecomment-4888032797)
- **#3299** (Lean QA drain: self-assuming / statement-integrity) — my frobenius fix is a statement-integrity correction (universally-false theorem → proved conditional); posted intent to drop it from their batch if queued. [comment](https://github.com/litlfred/qou/pull/3299#issuecomment-4888032965)
- No file overlap with #3402/#3381/#3202/#3391/others (checked by title/scope).

**Own-PR review triage:** #3401 just opened; no Gemini/Copilot comments yet. Gemini out of daily quota (external limit).

## 2026-07-11 — PRs #3553 / #3584 / #3595 / #3599 (broken-on-main leaf repairs)

**Scope:** 6 standalone library `.lean` leaf files that silently did **not** compile on `main` (no `<block>.qa.json` sidecar ⇒ no per-block checker; CI billing-skipped). Surfaced while building the ~106 QOU modules missing oleans for a `lake-cache` re-seed. All merged, `lean`-direct exit 0, sorry-free.

| PR | File(s) | Fix |
|----|---------|-----|
| #3553 | `StaircaseCornerHook`, `Information/OneDimChannel/ParallelNonInteraction`, `Mass/DeuteronBindingDressing` | §7d universe pin; named-instance class projection; redundant `ring` after `field_simp` |
| #3584 | `Archimedean/ConfinedKnotBinding` | CommRing redesign (no `/` / `linarith` on `LaurentPolynomial ℤ`; pn-half as `dh+dh=-HA` hyp) **+ corrected a false theorem** `a3_equal_characters` (`Σwᵢ·V = V·(1+W_std)` → `= V`) |
| #3595 | `Mathlib/WenzlBridgeConcrete` | ~1000-line forward-ref reorder (cohort defs before use) **+ corrected wrong n=9 SYT data** (`Σf²` 378108 → 362880 = 9!); q-namespace requalify; docstrings; reserved-λ; `show`→`decide`; redundant tactics |
| #3599 | `IwahoriHecke/Tw` | missing `open QOU.IwahoriHecke.Quotient` (metavariable cascade); `[Group W]` ordering; `wordProduct_singleton` proof |

**Methodology note (reusable):** the raw full-tree build reported ~13 failures, but **most were stale-cache false positives** — a current-source file built against the cache's older-commit dep oleans throws spurious `unknown identifier` / `function expected`. Each genuine bug was confirmed by rebuilding the file's transitive dep cone fresh (`build_cone`) before touching it, so no correct code was "fixed". Two genuine **math** errors were caught this way (false `a3_equal_characters`, wrong n=9 SYT dimensions) — both fixed on the merits, not papered over.

**Coordination:** posted intent on **#1562** (IwahoriHecke Sprint-2 `Defn.lean` `universal_property` uniqueness) — sibling Sprint-2 file to the now-merged `Tw.lean`; no file overlap, rebase-to-main picks up the working `Tw.lean`. #2112 (`HeckeH3` proof-repairs) touches a file `ConfinedKnotBinding` imports but shares no statement — no conflict, no comment.
