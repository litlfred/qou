---
# qou-mhij
title: 'z-parameter-echo is NOT a safe class: C propagates into payload that never equals z_C'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T23:05:02Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

The 2026-08-23 convention-C witness triage (docs/audits/2026-08-23-convention-c-witness-triage.{md,json}, bean qou-z11r, PR #5510) classifies 40 of 58 witnesses as z-parameter-echo -- 'C appears ONLY in z/markov-named fields, the witness recording which z it used' -- i.e. the benign class. That classification has a structural blind spot and vhat-per-crossing-chain is a MEASURED instance. The classifier keys on which FIELDS HOLD THE C VALUE 0.4993203340. But a producer can CONSUME z_C arithmetically and emit a result that does not equal z_C, so no value test can see it. vhat_per_crossing_chain computes V-hat = z*a + b. Its witness is classified z-parameter-echo with n_fields 1 (.constants.z). Regenerated under D it moves vhat_genuine_z_a_plus_b from 1.146101521079414 to 1.282420580225582 (+11.9 pct) on the proton sigma_0 record, and 0.9295042446238508 to 0.8934352738524302 (-3.9 pct) on another, with the p/n Delta figures moving with them. That is payload-or-mixed wearing an echo label. SAME SHAPE AS THE DETECTOR-BLINDNESS TAXONOMY, ONE LEVEL UP: that taxonomy catalogues detector-blind SOURCE spellings and the triage's value test is the correct answer to it; this is a detector-blind PAYLOAD PROPAGATION, which the value test is blind to by construction. The right discriminator is not the witness's field values but whether the PRODUCER uses z downstream of reading it -- which requires the producer, not the witness. NOT EXTRAPOLATED: I have one measured instance, not a count. The other 39 echo-class witnesses need re-checking against their producers; some will be genuine echoes (a witness that records z and never uses it). Do not assume the class is empty and do not assume it is all payload. Two of the 40 have producer null in the JSON twin, so for those the producer check is not even available.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8378, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
