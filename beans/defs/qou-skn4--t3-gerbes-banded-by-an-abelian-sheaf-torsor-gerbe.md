---
# qou-skn4
title: 'T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:48:14Z
updated_at: 2026-10-12T19:48:14Z
parent: qou-533l
---

Tier T3 of qou-533l.

**Carried from T2.**
- (a) Port `cechObstruction_lift_change` to the presheaf setting (independence of the local lift ξ).
- (b) Refinement of covers, then the colimit over covering families for a Grothendieck topology. Mathlib's H1 file lists the same colimit as a TODO.

**Main.** Gerbes banded by an abelian sheaf A: groupoid-valued stacks, locally nonempty and locally connected, with automorphism sheaves identified with A. Then a central extension of gerbes in the sense of Yekutieli Def 3.21 (`library/arxiv-0801.0083v4`, sec-002 :671).

**First milestone.** The torsor gerbe Tors(G) (exa:27), recovering T2b. Mathlib has no stacks. Scope the minimal 2-categorical structure first, and ask the owner before committing to a large design.
