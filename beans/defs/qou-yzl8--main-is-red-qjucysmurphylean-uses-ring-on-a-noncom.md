---
# qou-yzl8
title: 'main is RED: QJucysMurphy.lean uses ring on a NONCOMMUTATIVE algebra — 6 sites, none compile'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T13:30:42Z
updated_at: 2026-10-04T15:21:24Z
parent: qou-5vkl
---

Found while building QOU for an unrelated UGB change (qou-auq3). Not mine to fix: QOU/SchurWeyl/QJucysMurphy.lean is bean qou-ck0g, in-progress with another session.

## What is red

  lake build (QOU) fails on QOU/SchurWeyl/QJucysMurphy.lean

Six sites, all the same error, all 'ring_nf made no progress on goal':

  line 170:59   174:39   176:59   197:53   201:36   203:59

The build surfaces ONE per declaration, so a casual look shows a single
error. Fixing 203 by hand exposes the other five immediately.

## Cause

H_n(q) is NONCOMMUTATIVE, and 'ring' requires a CommRing/CommSemiring.
On a noncommutative goal it does not fail loudly -- it reports 'made no
progress', which reads like a tactic that is merely unnecessary rather
than a tactic that cannot work here. Every one of the six is inside a
calc chain doing associativity/unit rearrangement, which is precisely
what 'noncomm_ring' (Mathlib.Tactic.NoncommRing) is for; several are
plain 'mul_one'/'one_mul' rewrites.

Verified: replacing line 203's 'ring' with 'rw [mul_one]' removes that
error. The change was reverted -- this bean is a report, not a fix.

## Provenance

Introduced by 76fffc0465 'feat(lean): prove qJM_mul_qJMInv and
qJMInv_mul_qJM via calc chains'. qou-ck0g's note 'Builds clean (3095
jobs, 0 errors)' describes the EARLIER delivery 3d85d20065 and predates
the breaking commit, so the bean currently reads as green.

Also present: 'declaration uses sorry' at line 286. Not investigated,
and not necessarily new.

## Why this is filed separately

qou-ck0g is in-progress under another session and touching its file
would collide. This follows the qou-mnrd idiom -- a 'main is red'
report that its owner can act on -- rather than editing a sibling's
bean or its code.
