---
# qou-cweq
title: derivation_chain.Q_0 is proton-pinned but c-q-q0 target is muon (11.5ppb, derivation-chain audit FAIL)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T22:07:45Z
updated_at: 2026-11-16T19:04:00Z
parent: qou-2002
---

## Symptom

`python3 computations/derivation_chain_validator.py` → FAIL (89 assertions, 1 failing node):

```
✗ c-q-q0.derivation.json  target=c_q(q_0)  value=9.092678397394828 [fully-trusted]
  - c_q algebra re-eval at q_0=1.1099785827513808 gives 9.092679456150243
    vs target 9.092678397394828 (rel_diff 1.16e-07, target_tolerance 1.00e-12)
```

## Root cause — proton/muon q₀ anchor mismatch inside the derivation-chain audit

- `derivation_chain.Q_0` (imported by `derivation_chain_validator.py:47`) = **1.1099785827513808**
  → **proton-pinned** (per AGENTS.md §q₀-anchor-convention: proton pin ≈ 1.10998, the
  package/precision layer).
- `c-q-q0.derivation.json` `target_value` = 9.092678397394828 ⟹ q₀ = **1.1099785955573347**
  → **muon-canonical** (the `computations/`-layer convention, `q-pinning-50-digit.witness.json`
  = 1.10997859555733471).
- Gap = **11.54 ppb** (exactly the muon↔proton anchor gap), amplified by
  `d(c_q)/c_q = −dq₀/(q₀−1) ≈ 9.09·(dq₀/q₀)` to the observed **1.16e-7** in `c_q`.

So the validator re-evaluates a **muon**-pinned derivation target against a **proton**-pinned
`Q_0`. This is the exact silent-flip failure class of bean **tnjb** / AGENTS.md §q₀-anchor
recurring-bug note (a compute reading the wrong-anchor q₀).

## Why NOT fixed unilaterally (owner-gated)

AGENTS.md §q₀-anchor-convention rule 4 (STRICT): *"Do NOT migrate the ~840 muon-q₀
`computations/` witnesses to proton without explicit owner sign-off."* Aligning `Q_0`
(proton→muon) touches the whole derivation chain + ~72 producers; picking the other
direction (rewrite the muon `c-q-q0` target to proton) contradicts the documented
`computations/`-layer muon convention. Owner adjudication required.

## Fix options (for owner)

1. **Align `derivation_chain.Q_0` to the muon-canonical** 1.10997859555733471 so the
   `computations/`-layer audit is internally muon-consistent (matches the convention;
   the package/precision layer stays proton). Then regen the derivation-chain witness.
2. Re-pin the `c-q-q0.derivation.json` target to the proton Q_0 (only if the derivation
   chain is meant to be proton-anchored — contradicts current docs).
3. Widen `target_tolerance` past 1.2e-7 (masks the mismatch — NOT recommended).

Recommend option 1 (internal muon consistency), pending owner sign-off.

## Provenance / scope
- Pre-existing on `main` (NOT introduced by any current branch — surfaced during the
  post-rebase witness-drift refresh on `claude/dilog-pole-cusp-phase-2026-07-11`).
- Related: bean `tnjb` (per-observable 100× status silent-flip), `b0vf` (χ He-4 q₀
  data-integrity), AGENTS.md §"q₀ anchor convention — ideal CAL-2 (muon) vs experimental (proton)".

## Resolution (2026-11-16, PR [`litlfred/qou#8158`](https://github.com/litlfred/qou/pull/8158), commit `75b6b451ceab7004d7b1dbd5350d3c71eff04c1c`)

- `computations/c-q-q0.derivation.json` was repinned to the proton anchor `q_0 = 1.1099785827513808...` (`target_value = 9.0926794561502453911039703556573825637151463686661`) under the 2026-08-07 owner directive (`qou-ibcv`), matching `derivation_chain.Q_0` to `< 10^{-48}`.
- Formalised `cq_hbarQ_cross_identity` and `cq_anchor_relative_shift` (`(c_q(q_p) - c_q(q_\mu)) / c_q(q_p) = (q_\mu - q_p) / (q_\mu - 1)`) in `folio/quantum-observable-universe/lean/QOU/Observations/SubstrateParameterLocality.lean` (`0` `sorry`) and verified at 50 dps in `computations/probes/substrate_parameter_locality_varying_constants_probe.py`.
