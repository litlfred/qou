---
# qou-d5hn
title: 'TRAP: mu = A+1 is carried as a HYPOTHESIS in SLq2LabelParity.lean:77 and TorusKnotPages.lean:82 but total_curvature_is_the_computable_half_probe.py:43 and its witness cite it as ''(exact, Lean-proved)'' — conditional-proved != premise-established; the only derivation is probe-level'
status: completed
pr: 8248
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:11:57Z
updated_at: 2026-11-22T21:33:06Z
parent: qou-5vkl
---

## Progress (2026-11-17, PR #8248)

- [x] Update `computations/probes/total_curvature_is_the_computable_half_probe.py` and its witness description to state that $\mu = A + 1$ is probe-derived by exact integer permutation-cycle count and carried as hypothesis `hmu : mu = A + 1` in `SLq2LabelParity.lean:77` and `TorusKnotPages.lean:82` (PR #8248, Commit 1 `d3dcd4c4757a988299ad0246ed502bd2358a90e4`, Commit 2 `b4185f1dac70a76b08299e291f3137fb9b60fe3c`).
- [ ] Merge PR #8248 (`claude/round53-trd0-9nnz-fixes`, HEAD `b4185f1dac70a76b08299e291f3137fb9b60fe3c`)

## 2026-11-22 — CLOSED: the fix is on main via port #8248 (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Checked against main `3c4c98fccf3`.

The "Progress" entry above records the fix on a batch PR that never merged. It reached main as `d226f1ed95` ("port #8248: ..."), which names this bean. Verified on main: `total_curvature_is_the_computable_half_probe.py` now says `mu = A + 1` is carried as the hypothesis `hmu` in the two Lean files.

## 2026-11-22 — Applicability review (owner instruction 2026-11-22, bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Retroactive review of this pass's closure against `docs/coordination/owner-rulings.md` on main `3c4c98fccf3`.

**Verdict: ALREADY-DONE (closure stands).** The bean is about tooling or arithmetic precision (gates, audits, float64 paths, provenance, tracker structure). Its premises name no physics object, convention, anchor or particle assignment, so none of the retired premises (σ₀σ₁ photon, trefoil electron, convention C, the z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photons, adopted quark charges) or today's rulings (strand colour states, b = −qX, the fixed constant term 1 of the photon, the block U(1)_em charge) bear on it. What landed still answers its question.
