---
# qou-b5ic
title: 'GAP: no action of Bring''s S5/A5 on the model cone''s chirality units u'
status: todo
pr: 8196
type: task
priority: normal
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Opened from `qou-wqto` (owner ruling 2026-11-15, option 2: look for a point Bring's
own S5 symmetry singles out, to fix the chirality unit `u` of `Γ_u = L_u ∘ M_i`).

**The gap.** The corpus has no homomorphism from Bring's automorphism group to the
symmetries of the model cone `BringCone R = Quaternion R`. The A5 actions it holds are
Klein's on `ℙ(V)` (`klein-bring-icosahedral-bridge`) and S5 = Aut(Σ₄) on Bring's curve;
the S² of admissible `u` is the Hopf base of the quaternionic model, not Bring's link
`UT(Σ₄)` (`qou-rydq`). Searched: brings-surface, lean/QOU/BringCone*, lean/QOU/Brings,
docs/audits, docs/coordination, computations, beans/defs, library INDEX + sections + ocr.

**What any such link must look like.** Triad-commuting linear maps are left
multiplications (`commutes_reeb_triad_iff_leftMul`), and they act on `u` by conjugation
(`leftMul_conj_chiralGammaU`, `QOU/BringConeIcosahedral.lean`). S5 has no faithful real
3-dim rep, so only A5 can act, through 2I; the two icosahedral embeddings are swapped by
S5's odd coset. The placement of 2I inside the unit quaternions would also have to be
fixed — the Reeb triad does not constrain it.

**Why closing it would not by itself fix `u`.** Granting the action, the maximal
stabiliser rule selects the 12 vertex directions (6 axes), but each vertex's antipode is
in the same orbit via a perpendicular half-turn, and `leftMul_flips_chiralGammaU` shows
that half-turn carries `Γ_u` to `−Γ_u`. An A5-invariant rule identifies L with R.

Audit: `docs/audits/2026-11-15-bring-s5-distinguished-unit-preregistration.md` §5.
Probe: `computations/probes/bring_cone_icosahedral_unit_orbits_probe.py`.
PR #7818. Stays `todo` (open, rule 13a).

## Progress (2026-11-16, PR #8196)
- [x] Formalized `exceptionalOrbitSize`, `order60_exceptional_orbits_and_euler_deficit`, and `antipodal_pair_chirality_sum_zero_and_distinction` in `folio/quantum-observable-universe/lean/QOU/Eightfold/LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit.lean` + 50-dps mpmath witness (`qou_b5ic_icosahedral_orbits_and_antipodal_chirality`) in PR #8196 (`38b68fa660bb34e2ffb7a2e1a09e5c4f5308e2cf`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8196, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
