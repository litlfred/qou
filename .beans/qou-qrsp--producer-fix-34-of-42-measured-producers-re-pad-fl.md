---
# qou-qrsp
title: 'PRODUCER FIX: 34 of 42 measured producers re-pad float64 on re-run (qou-gqt5 follow-up)'
status: todo
type: task
priority: high
created_at: 2026-08-07T09:01:16Z
updated_at: 2026-08-07T09:01:16Z
---

Follow-up to qou-gqt5 (parent-less: beans disallows task-under-task).
MEASURED, not assumed -- docs/audits/2026-08-07-producer-repadding-empirical-sweep.md
Tool: computations/producer_repad_sweep.py (reproducible; detached worktree).

Commit 4aa48b63 stripped 58 witnesses (452 -> 13 padded fields). The strip is
value-preserving but NOT durable: re-running the producers regenerates 299 of
those fields in ONE pass. 34/42 measurable producers re-pad (81%); 11 could not
be measured at all and are NOT clean.

Consequence, and why this is high priority: the strip drains the ratchet BASELINE
while leaving the defect intact. The gate reads green, the producers still emit
fake precision, and the next routine re-run silently re-pads with no signal. This
is the hand-edit branch of what qou-gqt5 explicitly prescribed ("fix producers to
carry values as strings then re-run -- never hand-edit").

Clean (8, leave alone): binding_a3plus_joint_ji_combiner,
binding_block_multiplicative, binding_depth_stratified, meson_gen3_eta_phi,
probe_k_ud_bring_color_tube_empirical_baseline, probe_k_ud_fractional_and_alt_ansatz,
qbeta_habiro_element_probe, su2_spinor_multiplicity_resolution.
Heaviest re-padders: the qbeta_* and option_e_* families.

Known mechanism -- the mpf(<float-valued NAME>) blind spot, which the source
detector (23075055) documents it cannot catch. Live instance,
binding_factor_f_sequence.py:76:  return mpf(tf) - mpf(ta)   # tf, ta are floats

NOT MECHANIZABLE -- per-file judgment. For each re-padder decide whether the
quantity is GENUINELY float64 (then stop promoting it to mpf) or was DOWNCAST
upstream from full precision (then padding is a symptom and the real defect is the
lost precision). Guessing wrong either fakes precision or hides a real loss. This
is the part worth fanning out across agents; the strip was not.

Blocked in part by qou-wu80 (stale folio-assistant path) and qou-dgkf
(pyhecke_native has no wheel) -- both hide producers from measurement.
