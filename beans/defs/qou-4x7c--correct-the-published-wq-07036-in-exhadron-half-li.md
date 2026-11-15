---
# qou-4x7c
title: correct the published W(q₀) ≈ 0.7036 in ex:hadron-half-life-verification to the derived closed form (qou-egvf); withdraw the 11 % amplitude-reduction claim
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:51:06Z
updated_at: 2026-09-05T05:59:21Z
---

Owner 'merge and go' on #6664 read as approval of the audit doc's recommendation (option 1). Scope: obs/hadron-half-life-verification.md §T_{3,5} weak vertex — replace 0.7036 ('computed exactly') by W(q) = q²(q¹²+q⁸−1)/(q²+1)², W(q₀) ≈ 1.1875 (witness weak-vertex-t35-trace, Lean QOU.Braiding.WeakVertexT35.weakVertexTrace_eq); withdraw 'the vertex ratio yields an 11 % reduction in transition amplitude' — derived from the unreproduced 0.7036; nothing in the corpus derives an amplitude ratio from W. Update rem:hadron-half-life-fermi open computation 2 (W is now derived; whether it resolves the 10–17 % heavy-nucleus overshoot is NOT established — do not claim it). The half-life tables use the single-crossing approximation s² and do not consume W, so no table re-derivation is triggered. Dated authorNotes on both blocks.


## Result (2026-09-04)

Landed on `claude/weak-vertex-published-value-2026-09-04`.

- `ex:hadron-half-life-verification` §T_{3,5} weak vertex: 0.7036 → the derived closed form and W(q₀) ≈ 1.1875, with the Wedderburn form, the Jones cross-check and W(1) = 1/4; the 11 % amplitude-reduction sentence withdrawn; the sentence now records that the tables use the single-crossing approximation and do not consume W. Dated status authorNote.
- `rem:hadron-half-life-fermi` open computation 2 re-scoped: W derived; what stays open is wiring |W|² in place of s² into the tables and measuring the heavy-nucleus residual. Dated authorNote.
- `prf:hadron-half-life` item 1: the claim W(1) = 0 (as the mechanism of the classical vanishing) was FALSE — W(1) = 1/4 (Lean `weakVertexTrace_one`); corrected to say the vanishing is carried by the q-prefactor (`qPrefactor_classical`). Also reflowed a pre-existing '+' at line start inside display math (render hazard). Dated authorNote.

Contamination measured: 0.7036 lived at exactly one content site (plus two unrelated float coincidences in witnesses); the W(1) = 0 claim at exactly one site (two `W 1 = 0` hits in Lean are a different W). Verification: validate clean on touched blocks; qa-sweep ×3 no automated findings, sidecar hashes current; render battery clean; check-sidecars clean after the authors-note refresh.


## CORRECTION (2026-09-05, qou-ix74)
The provenance in the result note above ("descends from the deprecated convention-C hecke_division pipeline") is WRONG. Measured: 0.7036 is the LIVE hecke_division engine's former z^{len} trace rule at z_C (0.70355); the same rule at z_D gives 0.96844, the value t35-weak-vertex.witness.json carried from 2026-08-29. One engine defect, two Markov parameters. Engine fixed and the in-repo sites corrected in qou-ix74; docs/audits/2026-09-05-weak-vertex-substitution-scale-and-engine-defect.md §3.
