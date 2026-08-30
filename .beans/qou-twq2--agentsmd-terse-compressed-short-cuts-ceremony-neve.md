---
# qou-twq2
title: 'AGENTS.md: ''Terse != compressed'' — short cuts ceremony, never evidence/implications/options'
status: completed
type: task
priority: normal
created_at: 2026-08-25T09:50:12Z
updated_at: 2026-08-29T18:22:17Z
---

LANDED — PR #5756 (draft), branch claude/agents-md-terseness-directive-2026-08-25.

Owner instruction, verbatim: "you are as USUAL too terse (PLEASE update
Agents.md linked directives)."

WHAT THE RULE FIXES

§User accessibility opens with "Short answers. One-liners when possible."
Agents read that as licence to compress a MEASURED FINDING into a headline and
drop the evidence, implications and options with it. That is backwards on the
rule's own terms: the rule exists because the owner types with difficulty, so
it optimises TOTAL keystrokes across the exchange. A one-liner that provokes
three follow-ups costs four messages; the full answer costs one.

THREE EDITS

  AGENTS.md §User accessibility
    - "Short answers" now cross-refs the new rule instead of standing alone.
    - New STRICT "Terse != compressed": what short may cut (preamble, status
      theatre, unpursued options, re-derivation) vs what it may never cut —
      the same four-part frame AskUserQuestion already demands of questions:
      claim-with-number / evidence (path, line, command, before-value, sample
      size) / implications in physics-and-paper terms / options with cost,
      risk and a recommendation marked as judgement, plus the no-op.
    - Binds chat, commit messages, PR bodies and bean updates alike.

  AGENTS.md §work-plan item 3
    - The "up to 50 words" bean cap now says it bounds the LEDGER, not the
      turn. As written it read as a global budget and argued against the new
      rule 200 lines above it.

  .claude/skills/local/delivery-summary.md
    - Says it is packaging (restart cmd, viewer links) and points at the new
      rule for the report that must accompany it.

TWO NAMED TRIGGERS (compressed form is misleading, not merely thin)

  1. Correcting your own earlier claim — the dropped part is always "what else
     did that error contaminate", i.e. which beans / PR bodies / audit docs
     repeated the wrong figure.
  2. Negative or absence-of-evidence results — "no rationale in the source" is
     not "there is no rationale".

INCIDENT: trigger 2. I reported aoperator_a5_crosscheck "carries no muon
rationale in its source" and stopped, in a session that had ALREADY MEASURED
that its own assertions FAIL at muon and PASS at proton. Reported the weaker
evidence only. The migration that followed (#5755) reversed my own HOLD.

VERIFICATION: docs only. No .lean, no witness, no computations/ script — no
Lean check, no qa-sweep criterion and no precision gate applies.

=== LANDED 2026-08-29 — PR #5756 merged to main as 1c503bf4a7 ===

Rebase-merged, 2 commits, 4 files (+204/-2).

THE MERGE CONFLICT IS THE INTERESTING PART. AGENTS.md conflicted because a
SIBLING added a rule at the same insertion point four days later:

  main   "NAMING A DECISION IS ASKING A QUESTION — the frame above applies
          wherever you raise one, not only in AskUserQuestion" (2026-08-29)
  mine   "Terse != compressed: short governs ceremony, never content" (2026-08-25)

KEPT BOTH. Picking a side would have deleted a standing owner directive. They
are not rivals: main's generalises the six-part frame from the AskUserQuestion
TOOL to the ACT of handing over a decision; mine generalises "Short answers"
from a licence-to-compress into a rule about ceremony vs content. The same
insight applied to the two halves of an agent's output — questions and reports
— which is presumably why two agents reached it independently within four days.

Verified on main after landing: both rules present, my three edits present (the
rule, the "Short answers" cross-reference, and the item-3 clarification that the
50-word cap bounds the LEDGER not the turn).
