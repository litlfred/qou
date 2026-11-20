---
# qou-rtec
title: Route C forward — DT count as (motivic) Euler characteristic / BPS cohomology (CoHA) of the knot character variety; R1 (#connections=A-poly L-degree) is the tractable decategorified shadow
status: todo
pr: 8199
type: task
priority: high
tags:
    - alien-habiro
    - g3-aomega
    - research-programme
    - reorg-2026-10-04
created_at: 2026-08-11T00:35:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-frzo
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

2026-09-07 (owner "1 2 3", option 3): M3 Part 5 on qou-m3ad — H_floor's remainder inputs for 4_1 and 5_2 are derived from the corpus's own shape fields (real-root counts proved in Lean, Galois-conjugate CS value sets measured). Provenance upgrade only; the H_Ad/H_floor question and the Hecke-side derivation are unchanged. D4 (qou-1rjn) is already completed; the frame-dependent half of it — which chirality GGM's S+/S- are in the derived (mu, lambda) frame — is bean qou-lrvc (a source question). Sibling #7035 works step 3 (log-trace) and KZ; no file overlap.

2026-09-07 option 2 (owner 2y): the (-2,3,7) rotated 3D-index family derived in-sandbox (GHHR engine + SnapPy m016), GGM (102) gate exact; the q->0 Stokes integers in GGM's normalisation are not derivable without the pretzel's holomorphic blocks, so qou-m3ad item 1 needs a basis-invariant restatement — see qou-m3ad Part 7 and audit §3f.

2026-09-07 CORRECTION: 'item 1 not GL-invariant as posed' overstated — S^+ is canonical; the INDEX route cannot recover it (Fitting invariants trivial for unipotent S^+); the BLOCK route (GGM eq 19, state integral -> q-series per held GK 1304.2705) can. qou-m3ad Part 8.

## Progress (PR #8199)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/RouteCDTChiralityAndQBridgeTaming.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/route-c-dt-chirality-and-qbridge-taming.witness.json` (`scriptHash: d89ffef0f347`, `scriptCommitSha: d6aa2e9463a3ba079ec1d472e356f34252ece779`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8199 (`1f4bf9af7d58a057599a62f5a8d42748dc742ea8`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8199, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
