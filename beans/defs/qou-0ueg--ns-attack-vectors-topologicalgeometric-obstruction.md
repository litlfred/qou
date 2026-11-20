---
# qou-0ueg
title: 'NS attack vectors: topological/geometric obstructions for unforced NS, mapped to QOU'
status: todo
type: task
priority: normal
created_at: 2026-10-12T20:50:47Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-vo9t
---

Owner (2026-10-12): for UNFORCED 3D NS, can the QOU framework be reformulated to give a topological or geometric obstruction to regularity, or support for it? What are the open attack vectors, and what hints are in the literature?

Research survey only; no content edits. Mapping literature criteria (Constantin–Fefferman vorticity-direction, BKM, helicity/linking, reconnection, Tao averaged-NS barrier, Hou/Chen–Hou Euler blowup, Elgindi, Enciso–Peralta-Salas knotted structures, Etnyre–Ghrist contact/Beltrami) onto corpus objects.

## 2026-10-12 — survey landed (`docs/audits/2026-10-12-ns-attack-vectors-unforced.md`)

The survey covers 25 literature handles. Thirteen of them were verified this session against bibliographic or abstract records. The library holds no NS-regularity source.

**Verdict.** No topological obstruction is available from the domain: $\mathbb R^3$ is contractible and $T\mathbb T^3$ is trivial, so this is a scope-(b) exclusion. Vortex-line topology change does not obstruct NS either. Enciso–Lucà–Peralta-Salas (Adv. Math. 2017) construct smooth NS reconnection, so "topology change ⇒ singularity" holds for Euler only. The sharpest geometric theorem is Constantin–Fefferman 1993 with Beirão da Veiga–Berselli 2002 (½-Hölder vorticity direction ⇒ regular), and it runs **against** branch (A) of `levi-degeneracy-conjecture`. Tao's 2016 averaged-NS barrier makes the three obstructions in `regularity-breakdown` uninformative in both directions.

**Ranked vectors.**
- **V1:** recast the Levi chain on the vorticity plane field $\omega^\perp$. This gives a correctly signed necessary condition for blow-up.
- **V2:** a Hecke/Jones invariant of KAM vortex tubes. It is frozen by smooth Euler and broken smoothly by NS, so it yields an Euler/inviscid-limit criterion.
- **V3:** helicity/Beltrami depletion. It is heuristic and points toward regularity.
- **V4:** Tao/CMPP universality. It is heuristic, and no construction exists.

V1 and V2 both need a framework change: flow-dependent fields on $\mathbb R^3$ or $\mathbb T^3$ instead of a fixed $\ker\varTheta$.

Two owner decisions are framed in audit §4: Q1, re-scope the Levi chain; Q2, scope the vortex-topology claims to Euler. In both the default is that nothing changes.

**Still open:**
- whether Tao's averaged nonlinearity preserves Kelvin circulation or helicity;
- whether a Lamb-vector regularity criterion exists;
- `corpus_search` was down, so the corpus negatives above are lexical only.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch B):** in-progress → todo. Stale claim (session ended); work not finished — see docs/coordination/2026-11-20-dangling-claims-proposal.md.
