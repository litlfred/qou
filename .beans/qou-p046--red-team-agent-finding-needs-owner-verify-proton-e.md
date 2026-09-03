---
# qou-p046
title: 'RED-TEAM (agent finding, needs owner verify): proton_electron_ratio is false-as-stated + convention-C legacy + Lean/md desync'
status: completed
type: task
priority: normal
created_at: 2026-08-29T10:40:26Z
updated_at: 2026-08-29T17:29:09Z
---

Surfaced by the background Lean-gap-drain agent (session tender-keller, 2026-08-29). File: content/quantum-observable-universe/mass-theory/mass-endomorphism-tower.lean :: proton_electron_ratio. Agent's claim (NOT independently verified — needs a check before any durable 'false' declaration per the corpus discipline): (1) provably FALSE as stated — frobeniusNorm : ℝ→ℝ is an arbitrary function, so at n=0 massPoly=frobeniusNorm(1); frobeniusNorm:=fun _=>-1 makes it <0. (2) convention-C legacy — markovParamPoly v = 1/(v+v⁻¹) = √q/(q+1). (3) desynced from its own .md, which uses convention D + Li₂^q. Disposition: claim change (restate/demote/migrate), owner decision — do NOT fix unilaterally.

FIX IN FLIGHT: re-formalization landed as PR #6036 (branch claude/proton-mass-reformalize-2026-08-29). All 3 dispositions: false proton_electron_ratio sorry removed -> proved sorry-free mass_endomorphism_nonneg/positive; convention C markovParamPoly -> convention D markovZD; refuted Faddeev Phi_q -> abstract bounded Li2q (matches .md); renamed + .ts updated. Verified lean-direct exit 0, axioms [propext, Classical.choice, Quot.sound], no sorryAx. Awaiting owner merge of #6036; close on merge.

RESOLVED via #6036 (merged 5a2737c5): the false proton_electron_ratio sorry replaced by proved mass_endomorphism_nonneg/_positive; markovParamPoly (conv C) -> markovZD (conv D); Faddeev quantumDilogPoly -> abstract bounded Li₂^q matching the .md. lean-direct EXIT 0, axiom-clean.
