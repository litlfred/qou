---
# qou-hlx6
title: 'Helicity: do flavour and chirality share the letter orientation as common source?'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
parent: qou-qs0e
created_at: 2026-11-15T09:00:00Z
updated_at: 2026-11-15T10:30:00Z
---

Owner 2026-11-15: "work Helicity bean. Derive whether flavour and chirality share the
photon's letter orientation as their common source."

Hypothesis (coordinator's, NOT a finding): the letter orientation sigma vs sigma^{-1}
(6a, #7827: the net-flavour bit) is the same datum as the q / -q^{-1} eigenline choice
of that letter (6b, #7825: the L/R chirality pair).

Plan: (1) does sigma -> sigma^{-1} swap the eigenlines? (2) is the net-flavour sign a
function of the eigenline labelling? (3) physics consistency (u_L,u_R,d_L,d_R; isospin on
L only); (4) photon orientation bit as photon helicity, gamma gamma combinations.

Session: https://claude.ai/code/session_01Qmmkt6YuWNGS7sPqGwpD1Q

## 2026-11-15 result (verdict: hypothesis REFUTED, scope (b))

Lean `QOU/QuarkState/HelicityCommonSource.lean` (sorry-free, lean-direct exit 0, axioms
standard). The orientation flip s -> s^{-1} = s - h is the bar involution on one letter:
Hecke at q^{-1}, SAME eigenprojectors (flip_Pp/flip_Pm), eigenvalues inverted on BOTH
lines. The L<->R swap is s -> -s^{-1} = h - s: Hecke at q, projectors exchanged.
flip_ne_swap: distinct whenever P+ != 0. Net flavour of s, s^{-1}, -s^{-1} = 0, -1, +1;
corpus flavours share eigenlines, so net flavour is not a function of L/R labelling.
no_one_sided_letter: a left-only flip is a letter at no parameter unless q^2 = 1
(chiral isospin is not a letter; scope (a) for V-A overall). Photon orientation is not
BW photon helicity. Only a modulus (archimedean) labelling makes flip look like a swap
— recorded as owner decision D-H1. Audit:
docs/audits/2026-11-15-helicity-common-source-flavour-chirality.md.
