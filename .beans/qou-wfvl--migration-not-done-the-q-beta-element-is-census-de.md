---
# qou-wfvl
title: 'MIGRATION NOT DONE: the Q_beta element is census-derived while the owner''s gamma-gamma ruling forbids census selection'
status: todo
type: task
priority: high
created_at: 2026-09-12T19:04:20Z
updated_at: 2026-09-12T19:05:36Z
---

**What is wrong.** The Q_β prediction's *functional* was migrated to the ruled
`z_D`, but the *element* it acts on was not. The dashboard scores `Δ_S`, the
**short-NF element**, whose provenance is the census / normal-form construction.

**Why that violates a ruling made the same day.** On 2026-09-08, alongside the
`ε := tr at z_D` ruling, the owner also ruled (`qou-ales`): *"All selection of
great words should be done through gamma gamma production and the semi-definite
product solutions at q₀. Shouldn't use census."* `Δ_S` is census-derived, so it
is not an admissible element under that ruling.

**The candidates, all at level 2 = `z_D`** (from `qbeta-option-e-required-level`):

| candidate Δ | residual | provenance |
|---|---|---|
| `delta_S` short NF | −43.157 % | NF/census — **what the dashboard scores** |
| nuc9 `build_nucleon_nf` | −30.936 % | census |
| **nuc11 interleaved** | **−17.496 %** | **γγ-selected** (PR #7212 Part 4) |
| nuc11 gen-grouped | −15.451 % | census; γγ-**excluded** (positive 2nd letter) |

So the γγ-selected element is **2.5× closer** to CODATA than what is published —
and, more importantly, *derived rather than selected*. Both properties point the
same way, which is unusual here and worth noting.

**Blocked on:** PR #7212, which establishes the γγ ordering result. Open at the
time of writing, so it is a claim, not corpus.

**This is an OWNER DECISION, not agent work.** Changing the scored element is
neither a precision increase nor corpus-derived (exemptions 1 and 2 of the
2026-09-07 ask-before-change directive), so it waits. The row already records
`element_scored`, `element_is_ruled: false` and all four candidates, so nobody
reading the witness mistakes `Δ_S` for the canonical element.

**Do NOT pick the element by residual.** `qbeta_zd_gap_anatomy_probe` shows
`z*`, the parameter reproducing CODATA with `Δ_S`, is 0.99850 — 0.15 % from the
inadmissible `z = 1` — and neither admissible root is within 11 %. Ranking by
residual is the selection-against-the-target the anti-fit directive forbails;
the element must be chosen by the γγ + confinement-SDP construction and its
residual reported afterwards, whatever it is.

**Highest-value item in this arc: it subsumes the Q_β accuracy question.**
Full analysis: `docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §5(a).
