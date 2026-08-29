---
# qou-i5yp
title: 'GAP: does a depth-<=8 Bring Gauss-Manin recurrence admit body-order period ratio a2:a3:a4 = 1:-0.52:+4.45?'
status: todo
type: task
priority: normal
created_at: 2026-08-29T07:05:23Z
updated_at: 2026-08-29T07:06:13Z
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
