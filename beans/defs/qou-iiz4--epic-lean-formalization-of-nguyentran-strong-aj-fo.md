---
# qou-iiz4
title: Lean formalization of Nguyen–Tran strong AJ for 4₁ (library/arxiv-2006.02042v1/2006.02042v1.pdf) — q-Weyl/q-holonomy infra reusable for keystone q-lift identification + q-difference connections corpus-wide
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T03:21:57Z
updated_at: 2026-11-22T21:45:34Z
parent: c7vs
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-20 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: Lean formalization of Nguyen–Tran strong AJ for 4₁ (library/arxiv-2006.02042v1/2006.02042v1.pdf) — q-Weyl/q-holonomy infra reusable for keystone q-lift identification + q-difference connections corpus-wide

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change in status. Blocked on the same defect as `qou-y7o7`: the corpus's `TransferLemmas` encoding is uninhabitable (`not_transferLemmas`), so a Nguyen–Tran formalization would first need the class restated with the L-length order. Owner decision requested 2026-11-22.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.

## 2026-11-22 — TransferLemmas restated (owner card "Restate with L-length")

Done on PR #9141, commit f6b5788f1. TransferLemmas (Machinery/StrongAJFigureEight.lean) now measures order by lLength = top − bottom of the L-support. strong_aj_figure_eight_of_transfer derives I = span {Â} via principal_of_length_division_minimality (sorry-free, standard axioms), and a non-vacuity example (I = ⊤, Â = 1) shows the class is inhabited. The old topDeg class is kept as TransferLemmasTopDeg with not_transferLemmasTopDeg. Still open for a 4₁ instance: division for the length (skew-Laurent Euclidean property; NOT brick B3, which divides topDeg) and minimality (plain AJ content; AJMinimality.lean shows [Tr4] L3.1–3.3 do not supply it). aj_mem is corpus-proved.
