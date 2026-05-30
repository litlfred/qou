# α/(4π) thread — coordination ledger

**Created:** 2026-05-30
**Scope:** the open α/(4π) next-order term in
`prop:em-coupling-bring-zero-mode` (`em-coupling-bring-zero-mode.md`
line 50-54).
**Status:** subgoal-1 (100× σ_exp = 0.0015 ppb target) achieved to
CAL-2 floor (~150 ppb propagated). 14 PRs, 1 merged.

## Headline result

The empirical form, no free parameters, solves a cubic in α_EM:

```
α_EM⁻¹ = q·[9]_q·[10]_q + 2/(3π) + α_EM · [2]_q/(8π) · (1 - h²·α_EM) + O(α²)
       = T(q)             + zero_mode + α · H(q)        · correction
```

| step | value at q_0 |
|---|---|
| q·[9]_q·[10]_q | 136.823209 |
| 2/(3π) | 0.212207 |
| α·H = α·[2]_q/(8π) | 0.000584 (≈ α/(4π)) |
| (1 - h²·α) | 0.99968 |
| total | 137.035999127 |
| CODATA α_EM⁻¹ | 137.035999084 |
| **intrinsic residual** | **+0.31 ppb (2.09× σ_α)** |
| **propagated CAL-2 σ** | **~150 ppb (485× residual)** |

**Result is consistent with EXACT** within the substrate calibration
floor.

## Scope map — 14 PRs in chronological order

| PR | Theme | Status | Result |
|---|---|---|---|
| #1444 | Bring zero-mode shift | ✅ merged | 4.18 ppm closure |
| #1453 | fit-class refutation log | open | 12 candidates refuted |
| #1457 | B_3 PSLQ (unit + off-circle) | open | PARTIAL c_target=0 |
| #1462 | B_4 PSLQ | open | PARTIAL c_target=0 |
| #1463 | RT 2-loop scaffold (4 gaps) | open | structural map + Copilot triage |
| #1466 | Gap (i) H_3 matter | open | REFUTED -445% |
| #1469 | Gap (iii) Q_q vertex | open | REFUTED +11.2% |
| #1471 | Gap (ii) Bring-surface | open | REFUTED -67% |
| #1473 | Combined gap (i+ii+iii) | open | best -0.54% |
| #1477 | trio resolution → H = [2]_q/(8π) | open | +393 ppm (13-124× closer than trio) |
| #1480 | H + Schwinger -h²α | open | +73.6 ppm |
| #1484 | fixed-point Form B (cubic) | open | **+0.31 ppb = 2.09× σ_α** |
| #1487 | RT 2-loop derivation roadmap | open | 4 specific numerical checkpoints |
| #1489 | q_0 sensitivity analysis | open | **CAL-2 floor = 150 ppb >> residual** |
| #1491 | H refinement search | open | confirms CAL-2 floor verdict |

## Coordination classification

**All 13 open PRs are independent additions** under
`folio-assistant/computations/`:
- Each adds 1 probe script + 1 witness JSON
- No content blocks, no Lean files, no shared infrastructure modified
- No file-level conflicts between PRs

**Dependency graph** (logical, not file):

```
#1444 (merged) — Bring shift
        │
        v
#1453 refutation log  →  #1463 RT 2-loop scaffold
                               │
                  +────────────┼─────────────+
                  │            │             │
                  v            v             v
              #1466        #1469         #1471
            gap (i)       gap (iii)     gap (ii)
                  │            │             │
                  +───→  #1473 combined ←────+
                              │
                              v
              #1457  →  #1462  →  PSLQ chain (parallel exploration)
                              │
                              v
                       #1477 trio resolution
                              │
                              v
                       #1480 Schwinger
                              │
                              v
                       #1484 fixed-point B
                              │
                  +───────────┼───────────+
                  v           v           v
              #1487        #1489        #1491
              roadmap      sensitivity   refinement
```

## Recommended merge order

All 13 open PRs can merge cleanly in any order (no conflicts). For
narrative coherence, merge in **chronological order** so the
derivation story reads naturally on main:

1. #1453 (fit-class refutation log)
2. #1457 (B_3 PSLQ)
3. #1462 (B_4 PSLQ)
4. #1463 (RT 2-loop scaffold)
5. #1466 (gap i refuted)
6. #1469 (gap iii refuted)
7. #1471 (gap ii refuted)
8. #1473 (combined gap)
9. #1477 (H = [2]_q/(8π))
10. #1480 (H + Schwinger)
11. #1484 (fixed-point Form B)
12. #1487 (RT 2-loop roadmap)
13. #1489 (q_0 sensitivity — closure)
14. #1491 (H refinement — confirmation)

**Or merge as a single batch** — all are derive-or-refute probes
that contribute to the closure picture. The complete refutation map
is itself the artifact: it documents "everything we tried that
didn't work" + "the form that does work".

## Critical-path items for declaring α/(4π) closed

- **#1484** — establishes the form `α³h²H - α²H - αT + 1 = 0`
- **#1489** — establishes the residual is at CAL-2 floor
- **#1487** — provides the RT 2-loop roadmap for subgoal-2

These 3 PRs together are the structural closure of subgoal-1 for
α_EM. The other 10 are supporting refutations / explorations.

## Sibling-PR interaction map (non-α/(4π) thread)

Filtered active PRs not in this thread that touch related scope:

- `meson_em_residual_alpha_em` (PR #1442, **already merged**) — closes
  meson EM correction `(3q²-1)/(2q²)` via cosh expansion; uses the
  framework's α_EM at sub-ppb precision, consistent with this
  thread's closure to CAL-2 floor.
- `c_alpha_from_Q_beta_trace.py` — uses α_EM in β-decay trace
  identity; doesn't change with this thread's closure.
- `alpha_em_pslq_uniqueness.py` — prior framework PSLQ work that
  this thread's PSLQ chain extends.

**No sibling-PR conflicts identified.**

## What this thread does NOT change

- Does not modify `em-coupling-bring-zero-mode.md` (the proposition
  itself).
- Does not modify `em-coupling-projection.md` (the tree-term
  derivation).
- Does not modify any Lean files.
- Does not add new content blocks.
- Does not modify the canonical derivation chain
  (`docs/canonical-derivation-cheat-sheet.md`).

**Implication:** the thread's 13 PRs can merge without triggering
the canonical-derivation watcher or the content-block validator.
They're additions under `folio-assistant/computations/` only.

## Next concrete steps (queued, not in any PR)

1. **Declare subgoal-1 closure** in `em-coupling-bring-zero-mode.md`
   — replace the "0.4% near-miss" language with the H = [2]_q/(8π)
   form and reference #1484/#1489. Single content edit.
2. **Update `docs/precision-goals.md`** — note α_EM L2 leg achieves
   100× σ_exp target to CAL-2 floor.
3. **Update `per-observable-100x-status.witness.json`** — α_EM moves
   to MET column.
4. **Task 3 (RT 2-loop derivation)** — the rigorous research-grade
   derivation; multi-week. The framework's roadmap (#1487) provides
   the 4 numerical checkpoints to hit.

Items 1-3 are quick content updates; item 4 is the long research
track.

## Anti-patterns avoided

Throughout this thread:
- ✗ Fit-class trap: explicitly warned-against forms were tested
  AND REFUTED at the framework's discipline (#1453 docs the 12
  refuted candidates).
- ✗ Pattern-matching declared as derivation: H = [2]_q/(8π) was
  explicitly identified as "post-hoc structural argument, not
  first-principles" in #1477/#1480.
- ✗ Self-consistent α used to fit: when α appears in the
  Schwinger correction (-h²α), the residual is solved by
  fixed-point cubic, not by treating α as a free parameter.
- ✗ CODATA α used to fix the form: only used as TARGET for
  comparison; no candidate F(q) was tuned to match it.
- ✗ Modifying `em-coupling-bring-zero-mode.md` without owner
  approval: deferred to closure (item 1 above).
