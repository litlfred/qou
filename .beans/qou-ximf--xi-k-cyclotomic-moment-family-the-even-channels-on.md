---
# qou-ximf
title: 'Xi_k cyclotomic moment family — the even channel''s only derived source'
status: todo
type: task
priority: normal
created_at: 2026-08-26T03:28:36Z
updated_at: 2026-08-26T03:28:36Z
---

Parent: `qou-cds1`. Structural only; nothing wired, no c_k value.

The proved loop-mean identity `2z - h = [2]_q * Xi` (2026-08-21 audit,
sorry-free `loopMean_eq_twoQ_mul_moment`) uses the ordinary S_n character at a
TRANSPOSITION. Nothing in the argument is special to one. By Frobenius,
`Xi_mu = p_mu(1,Q)/(1+Q)^n`, and on the k-cycle classes this collapses to an
n-INDEPENDENT family

    Xi_k = (1 + Q^k)/(1 + Q)^k ,   Q = q^2 .

VERIFIED exact over Q(q) from actual Murnaghan-Nakayama characters against the
actual convention-D weights, n = 2..7, k = 1..n (4/4, exit 0). k=2 reproduces
the corpus's proved identity -- that assertion is the harness calibration.
Every member is exactly bar-EVEN (twist 1); numerators `1 + q^{2k}` are
CYCLOTOMIC (k=1,2,3,4 -> 1, Phi_8, Phi_12, Phi_16).

WHY RECORDED. qou-cds1's D-frame result leaves exactly one undetermined object:
`ce = z* - z_D^even = -0.0090534`, which is BAR-EVEN and so untouched by the
parity argument that fixes the odd half uniquely (co = -h/2). A four-path corpus
grep finds no other DERIVED, parameter-free, n-independent family of bar-even
weight functionals. Registry KC20 ("the bar-odd carrier is not a root-of-unity
object") does NOT bind it: KC20 is about the bar-ODD carrier, and the bar-even
channel has never been examined cyclotomically.

*** ANTI-FIT FENCE -- READ BEFORE USING THIS. *** ce is resolved to only 1.45%
(68.8 sigma) by sigma(Q_beta)/Q_beta. A family with a free index k supplies a
member inside a 1.45% window BY ARITHMETIC ALONE. The probe deliberately does
NOT compare any Xi_k to ce and no such comparison may be quoted as evidence.
The value is STRUCTURAL -- a derived source a derivation may draw on -- not a
match. Selecting k against the data is a fit and is banned by qou-cds1's own
discipline.

This is a one-line corollary of an already-proved identity, not new mathematics.
It is recorded because it is derived and the even channel has nothing else.

Probe: computations/qbeta/qbeta_xi_moment_family_probe.py
Audit: docs/audits/2026-08-26-three-gap-assessment-and-ck-cache-convention-confirm.md
