---
# qqki
title: Migrate 341 inline proofs from .md into .proof.md
status: todo
type: task
priority: normal
created_at: 2026-06-24T03:52:14Z
updated_at: 2026-06-24T03:52:34Z
parent: k65k
---

Blocks whose .md already contains an inline proof. Move the proof prose into <root>.proof.md, leave the statement in .md. SEQUENCING: do AFTER folio-assistant render wiring (R3) lands, else migrated proofs drop from the PDF. Most lack a clean 'Proof.' delimiter, so per-block editorial judgment is needed (not a pure codemod).
