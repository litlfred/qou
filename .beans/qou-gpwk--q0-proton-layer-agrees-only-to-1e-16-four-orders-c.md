---
# qou-gpwk
title: q0 proton layer agrees only to ~1e-16, four orders coarser than the muon layer's 9.111e-20
status: todo
type: bug
created_at: 2026-08-08T18:48:54Z
updated_at: 2026-08-08T18:48:54Z
---

Follow-up from qou-n1c4. With every leg on the proton pin, chi_dual_path_xref_audit reads 3.4e-17 (proton) .. 2.0e-16 (He-4). The muon layer used to reach 9.111e-20 at n=9 and n=12, so proton is ~4 orders coarser and the floor looks like an f64 leak.

Prime suspect: canonical_braid_crossings._avg_color_delta is documented to reach only ~5e-16 because it reads the float64 q_parameter.Q rather than the 50-dps string; AGENTS.md says deep-1ppQ callers should call flavor_split_leading(local_q0_50dps) directly.

But that is probably NOT the whole story: proton and neutron have no inter-nucleon crossing, so no colour-weighted delta at all, and they still sit at 3.4e-17 / 6.8e-17. Something common to every leg is capping at ~1e-16.

Worth checking: the muon q-pinning witness carries 70 digits while q_parameter.Q_50_DIGIT_STR carries 50 -- but 50 digits should still give ~1e-50, not 1e-16, so a float64 is being crossed somewhere in the proton path.

Acceptance: chi_dual_path_xref_audit reaches ~1e-19 or better on the proton layer, matching what the muon layer achieved.
