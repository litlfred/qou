---
# qou-5ovu
title: he4_binding_k_stage2 Leg B cache has no parameter guard; Leg A does
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T17:14:15Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

## The asymmetry

`computations/deltalambda/he4_binding_k_stage2_probe.py` checkpoints both legs
to JSONL so a run can outlive one sandbox session. Both resume caches are
otherwise well built — per-item granularity, torn-line tolerance
(`try: json.loads / except: continue`), dedupe on the item key, and aggregates
(`xcheck_worst`, `min_eig_overall`) rebuilt from the cache rather than lost with
the process. That last one is the easy thing to get wrong and it is right here.

**Leg A validates its cache against the run's parameters. Leg B does not.**

    # Leg A, line ~213
    if _r.get("nf") != len(K_kinds):
        continue          # computed under a different K-factor word -> discard

    # Leg B, lines ~300-310 — no equivalent
    per_block.append(_b)
    done_lambdas.add(tuple(_b["lambda"]))

Leg A stamps each entry with `nf = len(K_kinds)` and discards on mismatch. Leg B
entries carry only `lambda` / `dim` / `chi_f64` / `chi_exact_rel_diff` /
`min_eig_sym` / `max_eig_sym` — nothing tying them to the braid word or q0 they
were computed at. So if the K-factor word or the pin changed between runs, Leg A
correctly recomputes while **Leg B silently serves stale blocks**.

## Why it matters, and why it is NOT urgent

**Latent, not active.** Nothing in the current flow changes those parameters
between runs, and the cache self-deletes on clean completion (line ~513), so the
window is only "killed mid-run, then re-run with different parameters". It cannot
affect the run in flight.

**But it is the same shape as the bug fixed in `chi_via_rust_lossless` on
2026-08-24 (PR #5623):** a cache gate that answers *"is this entry PRESENT?"*
when the question is *"is this entry CURRENT?"*. That one kept two witnesses at
convention C across the whole 2026-08-09 cascade, and re-running the producer
could not fix them — it hit the reuse branch, stamped the file so it looked
refreshed, and changed no number. Cost: the defect survived three weeks and was
only found by following a Lean docstring's citation backwards.

## Fix

Stamp Leg B entries the way Leg A already does — `nf = len(K_kinds)` at minimum,
and preferably the q0 string too — and discard on mismatch. ~4 lines, mirroring
the existing Leg A guard. Do it when the file is next touched; do not interrupt
a long run to apply it.

Found 2026-08-24 while verifying the resume path was crash-safe before relying on
it (it is — today's container restart resumed 154/154 Leg A + 74/77 Leg B free).
Related: `computations/audits/self_caching_producer_audit.py`, which measures
this class corpus-wide and found it otherwise under control.

## Implementation & Witness Progress (PR #8273)
- Branch: `qou-10v9-34oo-43v0-580o-5ovu-5pgl` (`f56a97d3d6ca66bf63033f62ab41236e038a488a`), PR: `litlfred/qou#8273`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/probe2_shortfall_frame_chi_cache_clobber_pslq_detector_spelling_stage2_cache_guard_and_borromean_literal_probe.py` -> `computations/probes/probe2-shortfall-frame-chi-cache-clobber-pslq-detector-spelling-stage2-cache-guard-and-borromean-literal.witness.json` (`allPassed: true`, `scriptCommitSha: e98d91d4e01bb7197ccdfc0c0a05bab481cf2839`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8273, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). No superseded premise: cache parameter guard, basis-independent.

**Completed, verified on main today.** `computations/deltalambda/he4_binding_k_stage2_probe.py` lines 396-399: Leg B now reads `_b.get("st")` and drops any entry whose stamp differs from `_stamp` (word / pin / dps), the same guard Leg A has at line 273-277. Legacy unstamped entries warn via `_legacy_cache_warning`.
