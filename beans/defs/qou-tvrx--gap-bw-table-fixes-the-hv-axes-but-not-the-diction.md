---
# qou-tvrx
title: 'GAP: BW table fixes the H/V axes but not the dictionary lambda in [phi1 : lambda phi0]'
status: in-progress
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:17:22Z
updated_at: 2026-11-15T08:17:22Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u, PR #7825, ChiralityPolarizationHopf.lean. The sigma_0/sigma_1 chart centres map to -i/+i for every lambda. A real mixed photon is linear at lambda = 1 (polDict_one_linear) and circular at lambda = i (polDict_i_circular), so 'real phi = linear polarisation' is a choice, not forced. The degree-2 dressing phi01 L+ has no point of P^1, so any dictionary covers only the degree-1 part. Fixing lambda needs a structure (a real form / antilinear involution) the corpus does not supply. Do not choose it by which option reproduces SM labels.
