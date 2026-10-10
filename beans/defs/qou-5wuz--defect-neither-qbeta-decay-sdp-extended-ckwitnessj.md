---
# qou-5wuz
title: 'DEFECT: neither qbeta-decay-sdp-extended-ck.witness.json nor qbeta-closed-form-wiring-n4-to-n10.witness.json records q0Anchor or any q0 value, violating AGENTS.md q0-anchor rule 4 (a witness must record its pin). So an anchor mismatch can be neither blamed nor excluded for the c_k divergence. Sibling qbeta-ck-recursion-kernel-constraint-probe does record q0Anchor: muon'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:27:52Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The extended-ck witness now records q0Anchor muon. The closed-form-wiring n4→n10 witness still records none and is only tolerated by the q0-anchor ratchet baseline. Its producer must declare a pin and be re-run. Because the extended-ck c_k are now null, an anchor mismatch cannot explain any c_k divergence there: there is no c_k left to compare.

Evidence: Half fixed. `computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json` now records `q0Anchor: "muon"` and `q0Value 1.10997859564273904…` (computedAt 2026-08-30). Its `c_k_extracted_50dps` c_2..c_10 are all `null` (drained, qou-p77d). `computations/qbeta-closed-form-wiring-n4-to-n10.witness.json` (computedAt 2026-07-18) still has **no `q0Anchor`**. Its producer `computations/probes/qbeta_closed_form_wiring_n4_to_n10.py` reads q0 from `q-beta-operator-valued-N3.witness.json` (line 109) and declares no pin. It is tolerated in `computations/q0-anchor-missing-baseline.json:1218`. The sibling `qbeta-ck-recursion-kernel-constraint-probe` now records `q0Anchor: proton`, not muon as the title says.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
