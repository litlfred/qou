---
# qou-f8rr
title: 6 B-population producers are blocked on absent upstream witnesses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T15:43:21Z
updated_at: 2026-10-04T15:16:06Z
parent: qou-5vkl
---

delta_n2_placeholder_audit, deuteron_delta_i_audit, build_six_term_substrate_model_b, d_from_scratch, neutron_error_diagnostic and compound_binding_via_differences all refuse to run because an upstream witness is missing. These are GUARDS WORKING CORRECTLY, not defects - several say 'Run its producer first.' Two of the named upstreams do not exist anywhere in the tree: probe-sdp-canonical-paper-formula* and atomic-braid-mass-table*. Their own witnesses carry the OLD-MUON value B and cannot be drained until the chain is regenerated from the top. PR #5889.
