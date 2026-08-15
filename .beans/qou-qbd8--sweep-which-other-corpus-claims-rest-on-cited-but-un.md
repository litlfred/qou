---
# qou-qbd8
title: 'Sweep: which other corpus claims rest on cited-but-unchecked literature assertions?'
status: todo
type: task
priority: normal
created_at: 2026-08-08T09:35:00Z
updated_at: 2026-08-08T09:35:00Z
---

Follow-on from `qou-qbp5` / `qou-qbc7`. The C1 mis-citation was not a computation
error -- every number was right -- it was a **reading** error about what a cited
theorem says, and it survived months and drove a work plan.

**Question:** where else does a corpus claim rest on a paraphrase of an external
theorem whose hypotheses were never written down?

**Method (cheap, do not over-engineer):**
1. Grep audits/content for citation keys with strong structural verbs near them
   ("=>", "hence", "therefore", "so the level is", "which gives").
2. For each, ask the two questions that would have caught this one:
   - Does the cited statement carry a HYPOTHESIS the corpus quietly drops?
     (here: "integral slopes")
   - Is a defined SYMBOL being read with a different meaning than the source's?
     (here: `d` = slope difference, read as denominator)
3. Rank by how much downstream work each supports. Only chase the top few.

**Deliverable:** a short table of at-risk citations with a verdict each
(checked-OK / hypothesis-dropped / symbol-misread / unable-to-check-no-source).
"Unable to check because the PDF is not in library/" is a legitimate and useful
verdict -- record it rather than guessing.

**Note.** Several sources ARE local (`library/` has 0903.0853v3, 2410.20973v1,
Equations_aux_q-differences, and many more) and this sandbox has no pdftotext,
but text extracts fine straight from the FlateDecode streams -- see the method
used in `qou-qbp5`. So "no PDF tooling" is not a reason to skip a check.
