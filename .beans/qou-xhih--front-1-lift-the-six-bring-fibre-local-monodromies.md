---
# qou-xhih
title: 'Front 1: lift the six Bring-fibre local monodromies from S3 to B3 and compute the subgroup (PR #6449 F5 residual, qou-dg07)'
status: todo
type: task
created_at: 2026-09-03T04:37:53Z
updated_at: 2026-09-03T04:37:53Z
parent: qou-icj2
---


## 2026-09-03 — verified by a different route; #6449 had already lifted (PR #6458)

PR #6449 (`qou-dg07`) landed the lift first (six half-twists, image `= B₃`, `μ̄₁₂₃ = −1`);
this branch VERIFIES by a different route: `computations/probes/bring_monodromy_full_twist_probe.py`
(+ witness), audit `docs/audits/2026-09-03-bring-monodromy-full-twist-verification.md`,
Lean `QOU/Eightfold/BorromeanBraidPure.lean` (sorry-free, lean-direct exit 0). Runtime 146 s, 50 dps, no float.

- **Reader:** generic projection `e^{i·37/100}` + base point `5/2 + 3i/4`, so
  #6449's degenerate-real-projection defect cannot recur. All six lifts are
  half-twists, e-sum `−1`; loop-by-loop CONJUGATE to #6449's words with explicit
  conjugator `σ₂` (Artin action). Burau char-poly equality reported as necessary only.
- **New joint check:** six-lift product in angular order `[5,3,1,0,2,4]` == the
  independently transported large circle `|z−z₀|=4` == `Δ⁻²`; 72/720 orderings
  pass (the interleavings). #6449's words pass it too. `(ab)³ = Δ⁻²` is the
  `B₃` lift of `rem:holonomy-trefoil`'s `(H₁H₂)³ = id`.
- **Generation via SL(2,ℤ):** Burau at `t=−1`, `S = g₁g₁g₀`, `T = g₁⁻¹`;
  `ρ(H)=SL(2,ℤ)` + `Δ²∈H` + imported `ker ρ = ⟨Δ⁴⟩` ⇒ `H = B₃`. Independent of
  #6449's generator words.
- **Correction to #6449 §11.1 wording:** "four distinct words" are TWO elements
  of `B₃` (`σ₁⁻¹` on {0,3,4}, `σ₂σ₁⁻¹σ₂⁻¹` on {1,2,5}); conclusion unaffected.
- **Task C (six strands):** scope-(a) "no object to lift" — corpus has `H₆`/`B₆`
  Hecke material (block_transposition_lift_probe, PR #6415 blind blocks) but no
  six-sheeted cover; two copies of the cubic give `B₃×B₃`, which excludes the
  block-swap exchange braid.
- **Untouched:** statement B's premise (Alt³ occupancy still an input); μ̄.
