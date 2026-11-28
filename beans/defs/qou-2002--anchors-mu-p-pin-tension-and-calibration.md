---
# qou-2002
title: Anchors, mu-p pin tension and calibration
status: todo
type: epic
priority: normal
tags:
    - reorg-2026-10-04
    - compute-accuracy
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-28T10:56:30Z
parent: qou-10v9
---

Sub-epic P1.ANCHOR of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## Round 84 Progress (PR #8393)
- Branch: `feat/round84-colourdisc-fixedratio-comptrace-zeroslope-equidcap-43c1`
- Commit 1 (code + probe): `02a557115ca6d2779725ccfdca969ee6ef80dff4`
- Commit 2 (witness): `f21ac2e565e6a27158e92746366f1616c0d9fd98` (`scriptSha256 = 930736b7600cb1fb1ca87062021ff390088ea82549e2ac7bf6e2fad10cdf9749`)



## Claim reset 2026-11-22
In-progress only through an untouched batch PR / no live branch (applicability review, thread "Coordinate the L2 1-ppQ derivation plan"; plan doc /mnt/project-files/l2-1ppq-coordination/). Reset to todo under the stalled-claim policy; nothing in the work was judged. Re-claim if you pick it up.

## 2026-11-28 Owner Directive — Proton Pin ONLY; Muon Pin ON HOLD (STRICT)
Verbatim (`2026-11-28`): *"make sure you are working proton pin... no longer muon (on hold, until rederivation)"*.
- All active compute producers, probes, and witnesses MUST run on the **proton pin** (`physical_proton`).
- The **muon pin** is **ON HOLD** until `m_μ/m_e = Vol(4₁)/ℏ_q²` (or its replacement under the new lepton ladder) is genuinely derived; zero newly-added active muon-pin witnesses may merge onto `main`.
