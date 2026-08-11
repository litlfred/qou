---
# qou-rtec
title: 'Route C forward — DT count as (motivic) Euler characteristic / BPS cohomology (CoHA) of the knot character variety; R1 (#connections=A-poly L-degree) is the tractable decategorified shadow'
status: todo
type: task
priority: high
tags:
    - alien-habiro
    - g3-aomega
    - research-programme
created_at: 2026-08-11T00:35:00Z
updated_at: 2026-08-11T00:35:00Z
parent: qou-vr3q
---

Owner directive 2026-08-11 ("if not then C"): Route A did not close the A_ω internal-derivation gap (qou-rt0a). Pivot to Route C = categorify the DT count as BPS cohomology / cohomological Hall algebra (Kontsevich-Soibelman CoHA; Davison-Meinhardt BPS cohomology) of the 3-CY category attached to T[K], read the count as dim/χ.

HONEST SCOPING: Route C, fully, is a research programme (Davison-scale), NOT a session — it would close the literature-open categorification gap itself. Do NOT claim closure.

TRACTABLE ENTRY POINT (handed over by qou-rt0a): the surviving cross-knot reading is R1 — DT integer = #boundary-parabolic connections = A-polynomial L-degree = χ(character-variety datum). This is Route C's DECATEGORIFIED SHADOW (Route B). Concrete next steps:
 1. Formalize/probe R1 across more knots (need DT spectra; corpus has 4_1, 5_2 certified — extend if trefoil/6_1 DT become available). Driver14CharacterVarietyDTMenu.lean already scaffolds the character-variety DT menu.
 2. Find the MOTIVIC WEIGHT that upgrades the bare #connections count to reproduce BOTH DT integers {3,4} and the 5_2 chirality split (the companion 4 that R1 alone misses).
 3. Only a genuine categorical formula F(Hecke/Bring data) → DT spectrum counts as a derivation (anti-laundering). Importing GGM's count is not it.

Reference: docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md §3 (Route C) + §5 (Route A verdict).
