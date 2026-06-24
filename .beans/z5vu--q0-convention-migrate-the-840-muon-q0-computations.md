---
# z5vu
title: 'q0-convention: migrate the ~840 muon-q0 computations witnesses to proton (owner-gated; tnjb root)'
status: todo
type: task
created_at: 2026-06-24T18:25:20Z
updated_at: 2026-06-24T18:25:20Z
---


## Finding (2026-06-24, session bold-mendel — CAL q0-convention enforcement)

Established the authoritative convention (corpus: three-calibration-discipline.md §3,
epistemic-status-of-calibrations.md, substrate-anchor-alternatives.md):
- Ideal/canonical 3-CAL: CAL-2 = m_μ/m_e (muon) → m_μ exact by construction.
- Experimental/physical-obs: q0 re-pinned on PROTON m_p/m_e (precision substitution,
  NOT a 4th CAL); m_μ becomes a 9.5σ prediction (963.6× the L2 100× target).

ENFORCED at the reporting layer this PR (docs + AGENTS.md + dashboard comment):
- AGENTS.md §"q0 anchor convention" (new STRICT rule).
- docs/observable-sector-tracker.md: m_μ → proton-anchored prediction, net 4/7→3/7,
  Q_β relabeled derived (not CAL-3).
- per_observable_100x_status.py: comment clarifies m_μ + the muon-q0 caveat.

REAL owner-gated work item (NOT done here — large blast radius):
- computations/.../q-pinning-50-digit.witness.json carries the MUON q0
  (1.10997859555733471…); ~72 producers + ~840 witnesses build on it. The package
  layer (qou_substrate.constants) is proton-pinned. Migrating the computations layer
  to proton (so the L2 dashboard reports the proton m_μ prediction natively, instead
  of reading a muon-q0 Borromean witness) is a coordinated, owner-gated regen — the
  same scope as the "143-producer canonical regen" (768d9ddf). Do NOT do blind.
- Alternative bounded fix: have per_observable_100x_status.py evaluate the m_μ
  prediction at the PACKAGE proton q0 (qou_substrate.constants.Q) instead of reading
  the muon-q0 Borromean muon_check — contains the fix to the dashboard without
  touching 840 witnesses. Needs owner nod (changes a headline L2 number's source).

Supersedes the dashboard-symptom half of bean `tnjb` (which is on branch
claude/me-codata-reconcile / PR #2725).

## Scope doc (2026-06-24, for owner review)
docs/audits/2026-06-24-q0-layer-migration-scope.md — two options (full
840-witness migration vs bounded dashboard fix), gated on a Step-0
verification: confirm in the FULL env that q_at(50) returns the TRUE
proton q₀ (m_μ → ~210 ppb). In a minimal sandbox q_at returned a
muon-behaving value (m_μ → 0.05 ppb), which—if real—would invert the
963.6× framing (and the merged AGENTS.md rule). Resolve Step 0 first.
