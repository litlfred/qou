---
# qou-dk7p
title: 'Constructive turn: replace analytic arguments with algebraic ones'
status: in-progress
type: epic
priority: high
tags:
    - constructive
created_at: 2026-11-27T14:50:12Z
updated_at: 2026-11-27T14:50:12Z
parent: qou-rtxm
---

Owner request (Carl/litlfred, 2026-11-27, verbatim): "open thread to review QOU to move towards constructivist, less analyics based arguments. want a bean to track anything outstanding. give discussion of where still using anlutics and options to move to algebraic"

Tracking epic for replacing analytic arguments (limits, real/complex analysis, integrals, asymptotics, Classical.choose in definitions, Float) with constructive/algebraic ones (generic rings, Q(q), Laurent/Habiro, formal power series, h-adic, Hecke/TL, combinatorics). Nothing here is a ruling; each child waits on the owner's option pick (ASK-FIRST rule 2026-09-07), except Float removal (precision exemption).

Discussion doc (options numbered item.option): https://claude.ai/artifact/HSigAfgC55NiGZeB7KgkXd
Project thread: "Move QOU toward constructive algebraic arguments".

## Baseline (measured 2026-11-27 on main 6aaf7e77b, lean tree folio/quantum-observable-universe/lean, 2143 files / 438k lines)
- files mentioning R: 1157; C: 320; Tendsto: 59; interval integral: 69; tsum/Summable/HasSum: 52; Classical.choose/Exists.choose: 26; Float: 3.
- scripts/check-base-ring.ts --sweep folio/quantum-observable-universe: 1177/1264 pass, 87 warn, 800 hits (gratuitous R/C on algebraic side of the wall).
- Paper blocks with analytic language: mass-theory 214/878, quantum-observable-universes 92/338, appendix-surreals 79/123, fluid-dynamics 63/117, brings-surface 58/201, mass-endomorphism 50/139.
BASELINE: re-measure before quoting.

## Ranked items (children)
1. Goal #1 MI-integral via continuous KZ / Drinfeld-Kohno (qou-ywyq) -> discrete or formal h-adic KZ.
2. Mass as norm, binding as log (def:mass-identity, qou-2pnv) -> value in Q(q), norm/log only at comparison.
3. 87 base-ring warnings -> drain by chapter or ratchet.
4. Hyperbolic volume by real integrals (101 files) -> Bloch-group class / exact gluing variety.
5. Dilog/Stokes/Borel asymptotics (129 files) -> Habiro ring, formal series.
6. Moment problems / q-CLT (26 files) -> combinatorial moments (Touchard-Riordan, RSK).
7. Hyperreal/surreal transfer (10 files, hypr) -> h-adic inverse limits or Q((eps)).
8. Fluid dynamics q-NS (45 files) -> fence as analytic chapter, or q-difference lattice.
9. Classical.choose in model definitions; Float in 3 files.

Related: knot-volume thread (analytic squeeze), dilog-Bloch thread (algebraic Bloch group), observer-intent thread (h-adic).
