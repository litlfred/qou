---
# qou-5wuz
title: 'DEFECT: neither qbeta-decay-sdp-extended-ck.witness.json nor qbeta-closed-form-wiring-n4-to-n10.witness.json records q0Anchor or any q0 value, violating AGENTS.md q0-anchor rule 4 (a witness must record its pin). So an anchor mismatch can be neither blamed nor excluded for the c_k divergence. Sibling qbeta-ck-recursion-kernel-constraint-probe does record q0Anchor: muon'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:27:52Z
updated_at: 2026-10-10T10:40:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The extended-ck witness now records q0Anchor muon. The closed-form-wiring n4→n10 witness still records none and is only tolerated by the q0-anchor ratchet baseline. Its producer must declare a pin and be re-run. Because the extended-ck c_k are now null, an anchor mismatch cannot explain any c_k divergence there: there is no c_k left to compare.

Evidence: Half fixed. `computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json` now records `q0Anchor: "muon"` and `q0Value 1.10997859564273904…` (computedAt 2026-08-30). Its `c_k_extracted_50dps` c_2..c_10 are all `null` (drained, qou-p77d). `computations/qbeta-closed-form-wiring-n4-to-n10.witness.json` (computedAt 2026-07-18) still has **no `q0Anchor`**. Its producer `computations/probes/qbeta_closed_form_wiring_n4_to_n10.py` reads q0 from `q-beta-operator-valued-N3.witness.json` (line 109) and declares no pin. It is tolerated in `computations/q0-anchor-missing-baseline.json:1218`. The sibling `qbeta-ck-recursion-kernel-constraint-probe` now records `q0Anchor: proton`, not muon as the title says.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

**Cause R1 — a convention-D input read with convention-C formulas.** `computations/q-beta-operator-valued-N3.witness.json` (2026-08-21) carries the D-frame phase (α = −0.0404857773) and Q_N2 = 0.7828047136. `qbeta_decay_sdp_full_ck.py`, `qbeta_decay_sdp_extended_ck.py` and `probes/qbeta_ck_qholonomic_recurrence_test.py` extract c_k = (R−1)/u^k from R(q0) = Q_AME/(Q_N2/N2) using C-frame rungs. Reproduced: C gives Q_N2 = 0.782334410 and c_2 = −1.0150; D gives Q_N2 = 0.782804714 and c_2 = −9.2962338, matching the witness. The c_3 = −974 and c_4…c_7 = −1.1e5…−1.8e11 follow from that. Per `qou-8ofm`/`qou-frch`, one scalar R fixes at most one rung, so no extracted c_k at k ≥ 3 is evidence in either convention.

**Consequence here.** The c_k divergence this bean worried an anchor mismatch might explain is explained by R1 instead. Also: the title says the sibling records `muon`; it records `proton`. The wiring witness still has no `q0Anchor` (`q0-anchor-missing-baseline.json:1218`); its producer reads the proton, D-frame N3 witness.

**Open step (needs owner OK):** pin or retire `qbeta_closed_form_wiring_n4_to_n10.py`; then this bean can close.

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.

## 2026-11-15 — `straddleNote` added per owner ruling `Q-AVTQ-1 = 1` (`litlfred/qou#7995`)

- Added top-level `straddleNote` to `computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json` documenting the anchor straddle: top-level `q0Anchor: "muon"`, `q0Value`, and `parameters.q_0_50dps` (`1.109978595642739046681795129380001752700065561029`) are the CODATA-2022 muon pin while `parameters.hbar_q_sq_50dps` (`0.0098171864542750738105690571795642528890492845754014`) and `parameters.hoefsmit_b_50dps` were read from the proton-pinned `q-beta-operator-valued-N3.witness.json` (`q = 1.1099785827513808074799915684402849658272397296993`), keeping the witness file in place.
- PR: [`litlfred/qou#7995`](https://github.com/litlfred/qou/pull/7995) (commit `4552d3620d0f14bf058a5a7031606034f7a2a6be`, signed `ready:` comment [`#issuecomment-6901100726`](https://github.com/litlfred/qou/pull/7995#issuecomment-6901100726)).
