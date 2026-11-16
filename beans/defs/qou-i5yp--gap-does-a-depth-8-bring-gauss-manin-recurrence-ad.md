---
# qou-i5yp
title: 'GAP: does a depth-<=8 Bring Gauss-Manin recurrence admit body-order period ratio a2:a3:a4 = 1:-0.52:+4.45?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:05:23Z
updated_at: 2026-10-04T15:19:57Z
parent: qou-n4nr
---

Falsifiable target handed back to the s5-so3 keystone by PR #5966.

thm:binding-closure-conditional gives B(K) = m_e * Sum_n a_D^(n).
prop:prolonged-periods-fixed-depth PROVES the a_D^(n) satisfy a depth-d linear
recurrence with n-independent kernel, d <= rank V <= 2g = 8 for the genus-4
Bring curve. The IDENTIFICATION half — that d and the kernel are exactly the
Bring Picard-Fuchs operator — is open, and that block itself says it needs
'the per-knot weights at n = 2, 3'.

Measured (canonical convention D, probe2 f_pn typing, mpf 50dps): given the
multiplicative/Mayer model's own body-order content, the per-order rescalings
that would make the series reproduce AME2020 are

    a_D^(3)/a_D^(2) = -0.519787
    a_D^(4)/a_D^(2) = +4.45038

i.e. a2 : a3 : a4 = 1 : -0.52 : +4.45 — a SIGN ALTERNATION between the 2- and
3-body periods, and a fourfold enhancement at 4-body.

THIS IS A DIAGNOSTIC, NOT A DERIVATION. Reading the weights off the anchors is
anchor inversion — a fit if wired, and it is NOT wired. Its only use is as a
falsifiable target: does a depth-<=8 Gauss-Manin recurrence on the Bring
periods admit that ratio? If it cannot, the multiplicative/Mayer assembly is
wrong upstream of any weight, and no choice of a_D^(n) rescues it.

Under the other three convention x typing combinations the required a3/a2
stays in [-0.70, -0.44] (always negative) while a4/a2 ranges 2.88 to 30.9 —
so the SIGN ALTERNATION at 3-body is robust across the frame, the 4-body
magnitude is not.

Producer: computations/probes/he4_body_order_shortfall_location_probe.py
Audit:    docs/audits/2026-08-29-he4-magnitude-shortfall-location.md section 3c
Ledger:   docs/coordination/s5-so3-keystone.md


## RE-SCOPED 2026-08-29 (PR #6059) — the question as posed cannot be answered

Formalize-first prune, Lean sorry-free in
QOU/MassTheory/BodyOrderRecurrenceDepth.lean (see qou-d9sk).

This bean asks whether a depth-<=8 Bring Gauss-Manin recurrence admits
a2:a3:a4 = 1 : -0.52 : +4.45. Measured answer: YES, and vacuously, so the
question carries no information as posed.

  * d >= 3 is FORCED by the vanishing one-body term (three_le_depth), not
    merely bounded above by the rank.
  * At d = 3 the map (c1,c2) -> (a3,a4) is SURJECTIVE
    (depth_three_kernel_reaches). Every ratio is admitted. Matching the target
    solves for the kernel — an anchor inversion, i.e. a fit.
  * The first value the kernel DETERMINES is at body order 2d >= 6.

REVISED, ANSWERABLE FORM: extend the Ursell cumulant inversion to 6Li/7Li to
obtain a5, a6; then a depth-3 kernel pinned by (a3,a4,a5) PREDICTS a6, and THAT
is falsifiable. Only after that does the Picard-Fuchs identification have a
target worth computing against.

Do not run the PF computation against three terms.

## Progress (Round 57)
- Round 57 (`litlfred/qou#8213`, commit `2301811899d7f5b7e6235c29e2d41d3e068ef89b`): Added `a_four_in_terms_of_a_two`, `a_five_in_terms_of_a_two`, and `depth_three_kernel_unique` in `BodyOrderRecurrenceDepth.lean` plus 80-dps mpmath witness.
