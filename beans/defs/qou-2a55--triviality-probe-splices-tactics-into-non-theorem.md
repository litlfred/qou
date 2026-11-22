---
# qou-2a55
title: Triviality probe splices tactics into non-theorem declarations
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:58:48Z
updated_at: 2026-11-22T09:59:45Z
parent: qou-uwyf
---

Found in the Lean-backed re-probe for qou-y1qu (docs/audits/2026-11-22-triviality-decl-not-found-triage.md §6): of 133 declarations the fixed probe found, 47 are structures (21), defs (18), classes (6), abbrevs (2). The probe's PROVABLE regex filters the FILE (does it contain a theorem anywhere), not the referenced declaration's kind, so it splices 'by <tactic>' into a def or structure and records 'open'. Those rows are noise in lean-triviality.json and should be skipped with a reason (e.g. not-a-theorem). Fix in litlfred/folio-assistant-sci pipeline/lean-triviality-probe.ts; the lexer's DeclSpan carries no kind, so the kind has to be read from the declaration's own keyword.



2026-11-22: fixed for structure/class/inductive (new skip reason not-a-proof) in litlfred/folio-assistant-sci#213 commit 2d4af1a; def/abbrev/instance deliberately still probed (Prop-valued defs are the self-assuming shape). Tests with Lean: 28 pass.
