---
# qou-2z9j
title: 'Arc review 2026-08-19: vacuity/lean-QA plan'
status: todo
type: milestone
priority: normal
created_at: 2026-08-19T21:00:27Z
updated_at: 2026-08-21T15:55:26Z
---

Reconciliation of the Lean-QA vacuity arc against current main (@ 5b158ef0) after the #3269/#3287/#3299 waves merged. The arc is NOT drained; live state re-measured today.

## Current measured state
- Review ledger (docs/audits/lean-vacuity-review-ledger.json, updated 2026-08-10): 178 entries — 120 genuine, 38 needs-agent, 11 advisory, 9 legit.
- Static self-assuming sweep (scripts/lean-self-assuming-audit.py): 8 identity projections, ALL live (qou-q407, re-verified today).
- #3299 salvage confirmed on main (habiro supportBound, zeta8 qInt_four_eq_zero, gns shadow-sibling deleted).

## Priority order (root-cause infra first, then drain)
1. **qou-h43i** [infra, ROOT CAUSE] — the documented per-file gate (lean-vacuity-axiom-audit.ts <file>) overwrites the committed corpus-wide audit artifact with its one-file result, silently, exit 0. Fix so a single-file gate run cannot clobber the full-corpus artifact. Highest leverage — until fixed, every other count is untrustworthy.
2. **vaud** [infra, symptom of h43i] — committed audit JSON (2026-06-17) understates the corpus by ~78 defects (reports 44; corpus ~122). Regenerate the full-corpus artifact once h43i stops the clobbering.
3. **qou-q407** [drain, concrete] — 8 self-assuming identity projections, all live, ready to work (restate-to-derive or demote to def:Prop).
4. **ledger 38 needs-agent** [review] — all proof-no-self-assuming-projection candidates awaiting a fresh agent verdict so --check-ledger passes. ~34 files.
5. **ledger 120 genuine** [big drain] — restate-to-derive 43, construct-witness/drop 34, restate-against-definition 16, restate-or-demote 9, cite-or-make-opaque 9, etc. Partially covered by scattered VACUITY beans (qou-4ekg, qou-ulfe, qou-nkfq, qou-sk6h) + the dgap conjecture-carrier epic.
6. **qou-si72** [meta] — post-mortem on why QA missed the ∃q,True stub + axiomatization status-leaks.

## Note
Do NOT trust the committed audit JSON counts until h43i+vaud land — the clobbering bug means the artifact reflects whatever file was last gated, not the corpus.



## CORRECTION 2026-08-19 (same session) — P1 + P2 were ALREADY DONE
I listed qou-h43i (P1) and vaud (P2) as live from their [todo] status WITHOUT verifying against main — the exact 'verify before declaring open' failure. Verified today:
- **qou-h43i → COMPLETED**: duplicate of qou-c7jp (already fixed on main); guard confirmed working by reproducing the bean's repro (artifact byte-identical after a file-scoped run); added the missing regression test (content/pipeline/lean-vacuity-axiom-audit.guard.test.ts, bun test green).
- **vaud → COMPLETED**: committed audit artifact is a fresh full-corpus scan (2911 files / 99 defects / generated 2026-08-15), not the stale 44.

**Corrected live plan (P1/P2 dropped):**
1. **qou-q407** — 8 self-assuming identity projections (all live, re-verified today). Now the top concrete item.
2. ledger **38 needs-agent** — clear verdicts so --check-ledger passes (~34 files).
3. **~99 corpus defects** (committed artifact total_defects=99, the authoritative count now that the artifact is trustworthy) / 120 ledger-genuine — the big drain (43 restate-to-derive, 34 construct-witness/drop, …); scattered VACUITY beans qou-4ekg/ulfe/nkfq/sk6h + dgap epic.
4. **qou-si72** — meta post-mortem.

The audit artifact is now trustworthy (h43i fixed + regression-tested), so total_defects=99 is a real backlog number to drive down.



## UPDATE 2026-08-21 — ledger re-seeded + fully adjudicated (--check-ledger green)
Item 4 (needs-agent) DONE: re-seeded stale ledger (38→69), 6-agent swarm adjudicated all 69 → 63 genuine / 5 legit / 1 advisory. --check-ledger exits 0 (all 182 candidates carry fresh verdicts). PR #5369.
Item 5 re-scoped: the ledger now carries **161 genuine vacuity defects** (the real fix-queue) across categories — 54+ self-assuming-projection, proof-no-provable-axiom, proof-no-unused-hypothesis-rfl, proof-no-trivial-true, etc. This is the next drain tranche (q407-style, but larger). The committed ledger is the authoritative tracker; work it by clustering genuine entries into reviewable batches.



## Drain started 2026-08-21 (PR #5377) + honest assessment
First increment landed: 2 dimension-synthesis unused-hypothesis-rfl defects → honest def:Prop predicates (mirroring BorelRank's rank_witness fix). genuine 161→159.

**The drain is NOT mechanical** (verified by reading the first batch). The 159 remaining genuine defects are each a trivial/self-assuming statement whose real content is open or upstream; the honest fix per defect is one of: demote-to-conjecture, name-as-predicate (def:Prop), restate-against-a-definition, or a real derivation — often with content-block / prop:-label implications. Dispositions the swarm recorded: 88 restate-to-derive-or-demote, 31 construct-witness-or-drop-pseudo-theorem, 12 restate-against-a-definition, etc.

**Batching plan (per integration-backlog, ≤49 files/PR):**
1. Smaller mechanical-ish categories first: proof-no-unused-hypothesis-rfl (6 left), proof-docstring-sorry-mismatch (2), proof-no-trivial-true (19).
2. proof-no-provable-axiom (10) — prove or honestly-cite/remove.
3. proof-no-self-assuming-projection (122) — the bulk; cluster by directory. Many are §3b-cond field-projections needing genuine-hypothesis restructuring (NOT self-assuming class fields per §3b-cond item 5).
Each batch: fix + lean-direct verify + re-seed ledger (prunes resolved) + check-ledger green + PR. The committed ledger is the authoritative tracker/queue.
