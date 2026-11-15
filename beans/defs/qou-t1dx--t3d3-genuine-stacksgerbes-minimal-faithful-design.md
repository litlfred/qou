---
# qou-t1dx
title: 'T3/D3: genuine stacks/gerbes, minimal faithful design + first milestone'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T20:38:55Z
updated_at: 2026-10-12T23:00:00Z
parent: qou-533l
---

Owner: try all T3 designs. Front D3: genuine stacks/gerbes. Mathlib has none at f897ebc.

Scope a minimal faithful design: a prestack as a pseudofunctor C^op -> Grpd with descent data on covers; a gerbe as locally nonempty, locally connected, with band A.

Attempt a first sorry-free milestone, e.g. the torsor prestack Tors(G) of a presheaf of groups, and that it is a prestack. Report feasibility and a cost estimate.

## 2026-10-12 — first milestone landed (branch `t3-d3-stacks`)

- Model: target is (a) pseudofunctor `LocallyDiscrete Cᵒᵖ ⥤ Cat` with groupoid fibres (Yekutieli §2 verbatim). Strict `Cᵒᵖ ⥤ Grpd` rejected as unfaithful for `Tors(G)`.
- Proved, sorry-free (exit 0, axioms propext/choice/Quot.sound): `QOU.MathlibExt.StackGerbe.isSheaf_equivariantHom`. The presheaf of `A`-equivariant morphisms `P|_{C/X} ⟶ Q|_{C/X}` is a sheaf when `Q` is. This is the descent-of-morphisms (prestack) axiom for `A`-sheaves, hence for `Tors(G)`.
- NOT proved: Hom = Iso on torsors; effective descent of objects; any gerbe statement.
- Cost estimate for full Thm 4.17 under D3: ~10–20 sessions. Critical risks: pseudofunctor Hom-presheaf coherence (S1), and nonabelian/Čech `H²` (S5). Details in `docs/audits/2026-10-12-t3-d3-stacks.md`.
- Bean stays in-progress: the stack/gerbe definitions remain open.
