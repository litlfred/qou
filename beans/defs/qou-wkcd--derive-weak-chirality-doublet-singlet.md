---
# qou-wkcd
title: 'Derive weak chirality (doublet L vs singlet R): |q|>1, quaternion sides, literature'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
blocking:
    - qou-hlx7
created_at: 2026-11-15T13:00:00Z
updated_at: 2026-11-15T13:00:00Z
---

Owner question (relayed by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn, tracker #7735):
"L vs R on singlet vs doublets should be derivable somehow / related? anything in the lit?"
and "does it depend on |q| > 1 vs |q| < 1, or is it derivable from that? Is that the same as
the convention of which crossing carries q in the skein weighting?"

Session: https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7
Branch: claude/weak-chirality-doublet-singlet-2026-11-15

Three routes, each to a derivation or a scoped negative:
1. |q|>1: does the observable regime |q0|>1 select the L line? Is q0>1 forced?
2. Quaternions: left vs right multiplication (Sp(1)_L x Sp(1)_R) as the one-sided source.
3. Literature: Connes-Chamseddine, LR-symmetric / Pati-Salam, SO(10), Furey,
   Bilson-Thompson / Gresnigt, Finkelstein, the Ozma problem.

Starts from #7844 (OneSidedWeakVertex.lean), #7836 (HelicityCommonSource.lean),
#7825 (PolarizationActionHecke / ChiralityPolarizationHopf / PolarizationRealStructure).
