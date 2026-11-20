---
# qou-0xk8
title: 'T3/D2: Čech-cocycle gerbes and cocycle-level Yekutieli Thm 4.17'
status: todo
type: task
priority: high
created_at: 2026-10-12T20:38:55Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-533l
---

Owner: try all T3 designs. Front D2: Čech-cocycle gerbes.

A gerbe banded by an abelian presheaf A on a cover is given by cocycle data. Define a central extension of such gerbes, and prove the cocycle-level analogue of Yekutieli Thm 4.17 using the T2 machinery.

State explicitly that the equivalence between a gerbe and its cocycle is assumed and not proved. Source: Nikolaus–Waldorf, library/arxiv-1103.4815v3.

## 2026-10-12: D2 landed on branch `t3-d2-cech` (sub-agent d2-cech)

`QOU/MathlibExt/CechGerbe.lean` (517 lines) compiles with lean-direct
`-DautoImplicit=false`: exit 0, 0 sorry. Axioms are only propext,
Classical.choice and Quot.sound, checked on 11 headline declarations.

- Proved: `TwoCocycle` / `Rel` (an equivalence relation) / `H2`;
  `TwistedCocycle ζ β`, the global objects of a gerbe bound by lien(𝒢) with a
  central twist; isomorphisms preserve the twist; retwisting by a coboundary;
  `CentralGerbeExtension` (Def 3.21, cocycle form); obstruction 2-cocycle;
  `cl2` independent of the local lift; **Thm 4.17** both exactly
  (`cl2_eq_one_iff`) and up to isomorphism (`exists_iso_lift_iff`, under a
  hypothesis that sections over each `U i` lift).
- ASSUMED, not proved: that a gerbe is equivalent to its cocycle data. NOT
  covered: non-inner outer twisting. Also a single fixed cover, and the local
  lift is a hypothesis.
- Audit: `docs/audits/2026-10-12-t3-d2-cech-gerbes.md`.

The status is left `in-progress` for the parent (`qou-533l`) to adjudicate
against D1 and D3. The gerbe ≃ cocycle equivalence remains open.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch C):** in-progress → todo. Open conjecture: stale claim released; never to be completed while the conjecture is open (AGENTS rule 13a).
