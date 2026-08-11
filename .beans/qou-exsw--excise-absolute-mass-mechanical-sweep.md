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

---
2026-08-11 PROGRESS (branch claude/excise-abs-mass-sweep-2026-08-11): framing docs DONE —
AGENTS.md mass-banner excision banner; computations/canonical_mass.py docstring (m_e-scaled ratio
realization, no compute change); docs/canonical-mass-formula-guardrail.md banner; docs/canonical-
derivation-cheat-sheet.md banner. REMAINING = the 15 math-bearing content .md blocks presenting
absolute m_p/m_n in MeV as a prediction (delicate — render-QA gated per AGENTS §Render-QA gate;
reframe "prediction 938.27 MeV" -> the ratio m_p/m_e, keep the number as an m_e-scaled rendering).
Files:
  observations/terminal-resolution-cz.md, observations/substrate-consistency-window-table3-data.md,
  observations/mass-comparison-table-table2-data.md, observations/observations-intro.md,
  appendix-mass-binding-algorithms/mba-step09a-mass-identity.md,
  appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md,
  mass-theory/six-term-per-derivation-weights-table2-data.md,
  mass-theory/partition-sum-proton-residual-table4-data.md,
  mass-theory/six-term-per-derivation-weights-table3-data.md, mass-theory/terminal-resolution.md,
  mass-theory/h3-markov-wenzl-weights-context.md,
  appendix-qvalues/proton-mass-substrate-identity-derivation.md,
  mass-endomorphism/atomic-mass-gb-nf-interpretation.md, mass-endomorphism/mass-endomorphism-conjecture.md,
  mass-endomorphism/recomputed-low-isotope-mass-table-table2-data.md.
This content sub-sweep is agent-dispatchable (mechanical reframe + render-QA per block).
