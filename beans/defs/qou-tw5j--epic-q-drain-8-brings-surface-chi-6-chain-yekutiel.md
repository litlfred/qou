---
# qou-tw5j
title: 'EPIC [Q-Drain-8]: Bring''s Surface chi=-6 Chain, Yekutieli Gerbes & Surreal/MTC Infrastructure'
status: todo
type: epic
priority: high
created_at: 2026-11-23T20:55:49Z
updated_at: 2026-11-23T20:55:50Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Bring's Surface chi=-6 Chain, Yekutieli Gerbes & Surreal/MTC Infrastructure
**Rationale:** Completes G-equivariant Riemann surface triangulation (chi=-6 chain), Kummer/Yekutieli gerbe extensions, Hyperreal SurrealField, and Hecke MTC.
**Child Beans (13):** `qou-qhcr`, `qou-khmu`, `qou-w8es`, `qou-yslf`, `qou-m3tr`, `qou-2a2o`, `qou-n2aa`, `qou-skn4`, `qou-t1dx`, `qou-533l`, `qou-hypr`, `qou-hkmt`, `qou-rtep`

### Prioritized Beans in This Batch
- **`qou-qhcr`** (`high`, `in-progress`) — GAP: derive the branch-point count 6 from the five QOU axioms (the ONE missing step in the chi = -6 chain) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-khmu`** (`high`, `todo`) — GAP G2: lift the A5/S5 action from the fibre CP1 to the base curve M0 (chi = -6 chain) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-w8es`** (`high`, `todo`) — GAP G3: derive the irreducibility of H1(M0) = 2W as an A5-representation (chi = -6 chain) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-yslf`** (`high`, `todo`) — GAP (Antigravity): G-equivariant triangulation of a compact Riemann surface (Rado), to supply the map in GenusFourFromEquivariantMap
- **`qou-m3tr`** (`high`, `in-progress`) — Bring M3: G-equivariant cell structure of a compact Riemann surface, with chi = 2 - 2g (discharges hX/hY of genus_eq_four_of_cellular) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-2a2o`** (`high`, `in-progress`) — Route Z/2: Bring lifting obstruction as w_2-type class (centre of SU(2))
- **`qou-n2aa`** (`high`, `in-progress`) — Route Z: Bring lifting obstruction as integral Euler class; derive kappa_0 = e *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-skn4`** (`high`, `in-progress`) — T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals *(Rule 13a: 0-instance classes: `KummerSurfaceData`; Rule 13a `stays open`/conjecture guard)*
- **`qou-t1dx`** (`high`, `in-progress`) — T3/D3: genuine stacks/gerbes, minimal faithful design + first milestone
- **`qou-533l`** (`high`, `todo`) — Formalize Yekutieli central-extension-of-gerbes theorem for the brane tower (tiered) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-hypr`** (`high`, `todo`) — Discharge conj:surreal-limit-transfer from Mathlib Hyperreal (ℝ* is a SurrealField) *(Rule 13a: 0-instance classes: `BirthdayFaithful, ClassicalLimitStpart, ConwaySimplicity, DiophantineBirthday, SurrealLimitTransfer`; Rule 13a `stays open`/conjecture guard)*
- **`qou-hkmt`** (`high`, `in-progress`) — BWH-1: the Hecke category as a modular tensor category (S,T from Markov trace)
- **`qou-rtep`** (`high`, `todo`) — Bwse full closure — RT ribbon-functor+Kirby calculus AND BW=Hecke MTC identification

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
