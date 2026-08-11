---
# qou-exsw
title: 'excise-absolute-mass: mechanical sweep (AGENTS.md, cheat-sheet, canonical_mass, content)'
status: todo
type: task
priority: high
created_at: 2026-08-11T01:00:00Z
updated_at: 2026-08-11T01:00:00Z
---

Parent qou-exam. After the ruling audit + precision-goals anchor edit (PR #4977), sweep the rest:
 1. AGENTS.md — the mass-formula 🛑 banners (m(K)=m_e·Vol·ρ/ℏ_q²; canonical_mass) + §Precision-goals
    L2 table: annotate absolute mass EXCISED; keep ratio/binding framing.
 2. docs/canonical-derivation-cheat-sheet.md + docs/canonical-mass-formula-guardrail.md — relabel
    "absolute nucleon mass" -> "m_e-scaled ratio realization".
 3. computations/canonical_mass.py — docstring + emit metadata relabel (NO compute change; numbers
    still available as m_e·ratio, just not called an absolute prediction).
 4. content/ mass-theory blocks stating absolute m_p/m_n as predictions -> reframe to the ratio.
    Audit: grep -rl "938.27\|absolute mass" content/.
Candidate for agent dispatch (mechanical, parallelizable). Each item its own commit.
