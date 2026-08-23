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

## 2026-08-11 update — scalar avenue PROVABLY exhausted; Route C is now REQUIRED

Route A's R1 (#connections = A-poly L-degree) is the best scalar candidate — it hits the dtMax vector (4_1,5_2)↦(3,4) exactly, and it is a NEW scalar not in the Driver14CharacterVarietyDTMenu menu. BUT Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum (sorry-free) proves the 5_2 DT datum is a 2-element SET {3,4} (chirality split), so NO scalar — R1 included — can equal it. The scalar family is proved insufficient.

So Route C is not optional: the internal A_ω count must be a chirality-refined, set-valued Behrend-weighted DT moduli / BPS Hilbert space (the "driver-14" object). The tractable-scalar-shadow entry point is closed (proved). Forward work = the genuine categorification (CoHA / BPS cohomology producing a chirality-graded count) — research programme, out of session scope. R1 stays recorded as the sharpest scalar shadow.

## Attack options (2026-08-15 ledger, post-d999b21d7 correction)

M2 is a CONDITIONAL characterization (no (Q,W) built, no cohomology computed,
A_ω still imported). Honest rungs:

- **D1 — M1: construct the (Q,W)** [the real next rung; medium-large]. The
  abelian finding constrains it sharply (distinct Borel rays ⇒ no motivic
  multiplicity needed): find the smallest quiver-with-potential whose DT
  spectrum reproduces {3,4} + the bar split (7,1). ANTI-LAUNDERING: a quiver
  fitted to the data is a CANDIDATE, labeled as such — only a construction
  from Hecke/Bring data counts as the derivation.
- **D2 — M3 as a §3b class** [small]. Content-bearing conjecture class for
  "closed-sector category = this (Q,W)"; enables conditional downstream
  without laundering.
- **D3 — cross-knot data** [small; import]. Extend certified DT spectra
  (6₁; harden 5₂ via qou-52sn / SnapPy) to give M1 candidates more
  falsification targets.
- **D4 — chirality = bar-involution link** [small-medium]. Formalize the
  rtec audit's lever ({S⁺,S⁻} split IS q↦q⁻¹) as conditional Lean tying the
  DT set to the corpus bar-parity machinery.

## 2026-08-19 — M3 rung reframed by a sibling (qou-m3ad)

This programme's M3 rung is recorded here as "build a CoHA". A sibling has
reframed it to **"derive the index set Ω"**, on M2's abelian-spectrum finding,
and landed `QOU/QBeta/AdjointIndexSetM3.lean` (sorry-free) with H_Ad (the sl₂
adjoint) as the knot-independent core. The reframing is materially sharper than
the CoHA framing — deriving an index set is a smaller, better-posed target than
constructing a cohomological Hall algebra — and it is now owned by `qou-m3ad`
(in-progress, high). Treat that bean, not this text, as M3's live statement.
