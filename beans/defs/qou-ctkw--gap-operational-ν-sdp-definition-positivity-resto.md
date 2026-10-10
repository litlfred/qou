---
# qou-ctkw
title: 'GAP: operational ν_SDP definition (positivity restoration reproducing D/T/³He = 1,2,2) — PREREQUISITE for any He-4 ''confirm ρ_F=2'' compute. Six routes computed+refuted (per-block PSD count, op-selection active-set, bar-fold support, #self-conjugate, bare saturation q→1⁺ and q₀, LR-branching rails) — see docs/audits/2026-06-20-he4-nu-sdp-not-computed-definition-gate.md + 2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md. The audits'' named open need — ''a derived color-flavor constraint, not the un-vetted 9-pair ansatz'' — CONVERGES with the open closed-form W of conj:inter-nucleon-channel-color-tube (now a content-bearing Lean class, PR #4458): a derived W would supply exactly the non-encoding positivity restoration. Next honest step: derive W from the SO(3)-fiber tensor (open Q1 upstream), then re-pose the SDP with the derived constraint. Do NOT run H₁₂ under a guessed definition; do NOT invent a 7th saturation rule to hit 1,2,2.'
status: completed
type: task
priority: normal
created_at: 2026-08-01T11:23:49Z
updated_at: 2026-08-01T21:44:02Z
---


IDENTITY-I / RSK BUILD-INFRA STATUS (2026-08-01, cache-restored, lean-direct
verified reads). The Σ(f^λ)²=n! "dimension side" that the Δ_λ-gate/Identity-I note
flagged as needing HLF/RSK is now PROVED on main: `OVTopAssembly.sum_numSYT_sq_eq_
factorial : ∑ i : PartitionIndex n, numSYT i.diagram^2 = n!` (commit 198942442a),
via `RegularRepBlockTrace.sumSq_dim_eq` on the assembled `snSpectralData ℚ n` — no
new axiom, no RSK, no hook-length formula. (Note: Mathlib DOES carry
`StandardYoungTableau`; `numSYT μ := Nat.card (StandardYoungTableau μ)`. Earlier
session claims that it was absent were wrong.) The ONLY residual open sorry on this
front is `DeltaLambdaSignRule.burnside` (the `dimIrrep²` form, where `dimIrrep :=
n!/hookProduct` is the HLF DEFINITION). Closing it needs (1) the famous
hook-length formula `StandardYoungTableau.numSYT_mul_hookProduct` — a BARE sorry,
textbook-famous, NOT session-closeable (bean qou-f78h / sp09), and (2) a
reindexing bridge (bean qou-vh5k, bankable but does NOT close burnside alone).
This front is therefore HLF-GATED. It is ALSO physics-irrelevant to ν_SDP: the
defect cubic (n=3,5,7) is already unconditional via decide, so burnside's ∀-n
closure does not unblock the ν_SDP definition gate — the derived color-tube W does.
Build-infra map: milestone qou-uwxy.
