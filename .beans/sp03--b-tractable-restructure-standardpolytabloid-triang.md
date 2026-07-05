---
# sp03
title: 'B [TRACTABLE-restructure]: standardPolytabloid_triangular (SpechtStandardBasis.lean:258) relocation'
status: todo
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-07-05T16:30:00Z
---

ARCHITECTURE-blocked, NOT infra-blocked: its sorry-free replacement standardPolytabloid_triangular' exists in SpechtTriangularCore, but SpechtStandardBasis (base) can't import it (would be circular). Close by relocating the diag_unit/lead_inj/dominance machinery down the import DAG so the base file consumes it. Restructure, not new math — the most tractable Specht brick.

Parent: sp00.
