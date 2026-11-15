---
# qou-8ava
title: 'GAP: what is a ''polarization generator''? (sigma0,sigma1) is not an orthogonal pair under any H3 automorphism'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:24:51Z
updated_at: 2026-11-15T08:24:51Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u (owner D1), PR #7825, QOU/StandardModel/PolarizationActionHecke.lean. Proved: SU(2) acts transitively on orthogonal polarization pairs (cone, orth_pair_eq_leftMul_std). Conjugation in the (2,1) block of H3 is an inner automorphism preserving the Hecke and braid relations, and moves the q/-q^-1 eigenline pair of ONE letter to any pair. But generators attached to (v, v-perp) commute (eigenAxis_commute), sigma0 and sigma1 do not (s_noncomm), so no automorphism sends (sigma0,sigma1) to an orthogonal pair (no_automorphism_to_orthogonal_pair, scope (b) given the modelling step). Their q-lines sit at Bloch cos = -(q^4+1)/(q^2+1)^2 (120 deg at q=1). The linear mix a sigma0 + b sigma1 satisfies the Hecke quadratic only for (1,0),(0,1) (L+-/L- coefficients force ab=0). OPEN: the BW block's 'horizontal/vertical = sigma0/sigma1' reading has no derivation; the derivable polarization pair is the L/R eigenline pair of a single letter.
