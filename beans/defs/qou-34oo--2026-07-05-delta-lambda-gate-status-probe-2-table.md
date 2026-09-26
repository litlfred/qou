---
# qou-34oo
title: 2026-07-05 delta-lambda gate-status PROBE 2 table is convention-C-frame and is being quoted as current
status: todo
type: task
priority: normal
created_at: 2026-08-29T07:05:14Z
updated_at: 2026-08-29T07:05:55Z
---

docs/audits/2026-07-05-delta-lambda-gate-status.md section PROBE 2 quotes
|b4c|=1.9614, sum-g=3.6310, delivered x1.540 vs needed x2.093 ('74% of target,
~26% short'). Those are convention-C-frame, computed 2026-07-06, before owner
ruling R1 (2026-08-15) made convention D canonical.

The committed witness was regenerated 2026-08-23 under D + the proton pin and
now reads z=0.612688, |b4c|=1.17395, delivered x1.398, del/need 0.6664. The
audit prose was not updated with it, so the doc and the witness it cites
disagree.

Re-measured on PR #5966 (computations/probes/he4_body_order_shortfall_location_probe.py):
the C branch reproduces the audit's numbers exactly (1.9614 / 3.63097 / 1.54019
/ 2.09252), confirming the table is C-frame rather than merely old.

Under canonical D the shortfall is LARGER: 33.4% short, not 26%. Fix is a
currency note on the audit doc naming the frame, not a recomputation — the
C-frame numbers are correct for C and should be kept as recorded per the
convention-D excision policy (scope them, do not 'fix' them).
