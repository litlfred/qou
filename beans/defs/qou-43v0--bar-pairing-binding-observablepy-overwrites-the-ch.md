---
# qou-43v0
title: bar_pairing_binding_observable.py OVERWRITES the chi-cache witness it documents as an input
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T05:54:26Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

## Mechanism (measured 2026-09-06)

`computations/bar_pairing_binding_observable.py` opens by declaring itself a
READER:

    Reads two parallel chi-cache witnesses per atom:
      - `chi-{atom}-h{n}-at-q0-50dps.witness.json`    (substrate anchor)
      - `chi-{atom}-h{n}-at-qinv-50dps.witness.json`  (Hecke bar image)

and then at **line 187** writes to that same path:

    legacy.write_text(json.dumps(_prov_payload_1, indent=2))

where `legacy = HERE / f"chi-{atom}-h{n}-at-{q_tag}-50dps.witness.json"` (l.126).

So a consumer clobbers its own input cache. The overwrite is LOSSY and the
two payloads have different shapes:

| | owner `chi_at_q0_via_hoefsmit_mpfr.py` | after `bar_pairing_*` runs |
|---|---|---|
| keys | 25 | 21 |
| `tr_M_at_q0` | 0.57517224391777187082653534398618088915249435289286 | **absent** |
| also lost | N, Z, convention, description, engineVersion, producer, q_0_50dps | |
| gained | | kind, q_str, scriptFile, _provenance, and `pr_consumer`/`pr_landing_kernel`/`rust_fn` all **None** |

Three `None` fields is the tell: the write is a partial record, not a
different-but-equal one.

## How it surfaced

I hit it from the side. PR #6857's verification pass re-ran 189 producers to
check they still imported; that executed this script, which silently
overwrote `chi-deuteron-h6-at-q0-50dps.witness.json`. The damage reached main
and a sibling caught it (qou-16yn), not my verification — I checked that
values were CORRECTED and environments GREW, never that anything DISAPPEARED.

## Scope — this is NOT specific to me

Anyone who runs `bar_pairing_binding_observable.py` clobbers the chi-cache
for whichever atoms it touches. The same is presumably true for the `qinv`
sibling path. Measured on main 2026-09-06: `chi-deuteron-h6-at-q0-50dps` is
STILL gutted there (`tr_M_at_q0` absent); no commit has touched it since
70ae502091.

## NOT fixed here, deliberately

Which payload should own that path is exactly the open question in qou-49vn,
which belongs to another session. Deciding it by editing the script would
settle their question silently. What is reportable without deciding anything:
the script's stated contract says READS and its code WRITES, and the write
loses a computed value. Restoring the owner's content (PR #6904) fixes the
instance; the collision needs the owning session's call.


---

## SUPERSEDED by `qou-w8rv` — which found the ROOT CAUSE (2026-09-06)

A sibling filed *"bar_pairing_binding_observable silently CLOBBERS three
canonical chi caches on every run — its cache-key guard reads a field name that
does not exist"*.

That is the diagnosis this bean could not reach. I established the SYMPTOM (the
script's docstring calls the path an input and its code writes it) and measured
the shape (the two payloads have DISJOINT key sets — mine `tr_M_at_q0`/`N`/`Z`/
`convention`/`description`/`producer`/`q_0_50dps`, theirs `_provenance`/`kind`/
`q_str`/`scriptFile`/`pr_*`/`rust_fn` — so two producers share one path rather
than one being a stale copy). `qou-w8rv` explains WHY: the guard that should
prevent the write tests a field that is not there, so it never fires.

**NOT closed.** `qou-w8rv` is `todo`, so the defect is live, and AGENTS.md
forbids closing a bean whose subject is still open. Work it there; this one is
the symptom record and the payload-shape measurement.

The restore of `chi-deuteron-h6-at-q0-50dps.witness.json` (PR #6904, on main)
fixed the one instance. Anyone re-running that producer re-breaks it until
`qou-w8rv` lands.

## Implementation & Witness Progress (PR #8273)
- Branch: `qou-10v9-34oo-43v0-580o-5ovu-5pgl` (`f56a97d3d6ca66bf63033f62ab41236e038a488a`), PR: `litlfred/qou#8273`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/probe2_shortfall_frame_chi_cache_clobber_pslq_detector_spelling_stage2_cache_guard_and_borromean_literal_probe.py` -> `computations/probes/probe2-shortfall-frame-chi-cache-clobber-pslq-detector-spelling-stage2-cache-guard-and-borromean-literal.witness.json` (`allPassed: true`, `scriptCommitSha: e98d91d4e01bb7197ccdfc0c0a05bab481cf2839`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8273, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). No superseded premise: this is a cache-guard code defect, basis-independent.

**Completed, verified on main today.** The root cause was fixed under `qou-w8rv` (completed): `bar_pairing_binding_observable._cached_q(w, q_tag)` at line 151. `python3 bar_pairing_binding_observable.py --self-test` -> `cache-key self-test passed (8/8)`, run 2026-11-21 on main `2ae54ab40`.
