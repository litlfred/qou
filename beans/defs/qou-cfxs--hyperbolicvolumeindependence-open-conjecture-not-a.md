---
# qou-cfxs
title: 'HyperbolicVolumeIndependence: OPEN CONJECTURE, not actionable'
status: draft
type: task
priority: deferred
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T07:04:17Z
updated_at: 2026-11-22T21:33:05Z
parent: qou-n4nr
---

`QOU/Archimedean/HyperbolicVolumeIndependence.lean:39`.

**Not a missing proof.** Algebraic independence over ℚ of Vol(4₁),
Vol(5₂), Vol(𝓑₃) is an open problem — Borel–Zagier circle of
conjectures. The file states this explicitly.

Filed as `draft`/`deferred` purely so the `sorry` is accounted for and
nobody mistakes it for work someone forgot to do. **Do not attempt.**
The only honest resolutions are: upstream mathematics settles it, or the
dependent results get restated conditionally on the conjecture.

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

Untouched by design: algebraic independence of the volumes is an open problem (Borel–Zagier circle). Stays draft/deferred.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.
