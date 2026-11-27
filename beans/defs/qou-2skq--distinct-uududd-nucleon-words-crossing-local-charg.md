---
# qou-2skq
title: 'Distinct uud/udd nucleon words: crossing-local charge dressing replaces C2'
status: in-progress
type: task
priority: normal
tags:
    - compute-accuracy
created_at: 2026-11-27T17:28:59Z
updated_at: 2026-11-27T17:39:42Z
parent: qou-myts
---

Route 2 of the nucleon split (C1 item of qou-myts). Owner 2026-11-27: build different proton and neutron elements from uud and udd words under the three-colour working assumption; this changes C2. Construction: dress each crossing sigma_k with (1 + c Q_k Q_{k+1}), Q = diag(a,b). Lean QOU/Nuclear/NucleonChargeDressedWords.lean (sorry-free, generic field): tr Mn - tr Mp = c(a-b)(1+abc)^3 G/q^6. Colour alone cannot separate p and n (singlet is shared). Coupling c is not derived (shared with route 1, the Gibbs-map thread). Branch claude/nucleon-uud-udd-words-2026-11-27.

2026-11-27: PR #9511 (head 1d31ea024f) opened, ready for review. Lean exit 0, probe 7/7. Owner card: option 1 (crossing-local charge words). Open: sign and value of c (route 1), alternatives listed in the audit §4.

2026-11-27 follow-up: charges in the ruled photon weights. Factorisation L^3 = 1 + h^2 L - h^2 L^2 forces c = 0 (Lean ac_eq_zero_of_photon_factorisation; probe: only common root for quark charges). Dressed photon pair alone splits at O((q^2-1)^4). PR #9517.
