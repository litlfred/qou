---
# qou-mgg1
title: 'Magic shells via gamma-gamma processes in Hecke normal form (capture, photon excitation, e-e interaction)'
status: in-progress
type: task
priority: high
created_at: 2026-11-21T04:10:00Z
updated_at: 2026-11-21T04:10:00Z
parent: qou-6qbv
---

## Owner request (2026-11-21, chat)
Explore the magic shells through the Gröbner-basis gamma-gamma production viewpoint: add one electron at a time, track the knot convolution operators as it binds, and see directly from GB normal forms whether the binding operator is more complicated at closures. Card answers: D1 nucleus-as-one-strand model in H_{Z+1}; D2 full photon gamma(phi) — "model the physics so a photon can excite an electron and a particle interaction; also model the interaction where an electron gets bound"; D3 report both Frobenius positivity (reading 3) and the SDP-value change.

## Prior work (corpus-grepped 2026-11-21)
shell-closure-normal-form.md (2026-04), shell-closure-nf-term-count.md (2026-04, parity signal only), knot-operator-transition.md (2026-04), jet-filtered-knot-factor.md (opposite direction); later negatives: shell_shadow_price_magic_contrast_probe, symbolic_nf_q_degree_magic_probe, gs_filtration_jet_shape_magic_probe; beans qou-fcn8, qou-pz4m. None used gamma-gamma words or the confinement SDP.

## Discipline
phi = (phi0, phi1, phi01) is NOT derived. It is carried as a variable; binding is reported as a region in phi-space, never tuned. Model choices are written in docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md and confirmed with the owner before scaling past small Z.

## 2026-11-21 — first results (PR #8710, merged 94459335c9)
Complexity smooth (W_k 6*4^(k-2) terms, O_k 2^k+4), no closure feature to k=7. Bare atom positivity: binds Z=1,2, fails Z=3..10 only in (Z-1,2) block (first exists at Z=3) -> block-appearance artifact, not a closure signal. No change at Z=10. SDP-value test awaiting a per-element definition (owner). Next: owner choices on model variants.
