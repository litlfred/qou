---
# qou-2z9j
title: 'Arc review 2026-08-19: vacuity/lean-QA plan'
status: todo
type: milestone
created_at: 2026-08-19T21:00:27Z
updated_at: 2026-08-19T21:00:27Z
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
