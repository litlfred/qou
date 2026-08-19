---
# qou-kgsx
title: 'GAP: explain why delta is A-independent while the interface-letter count grows (bar-involution mirror law)'
status: todo
type: task
priority: normal
created_at: 2026-08-19T19:46:56Z
updated_at: 2026-08-19T20:12:14Z
---

From qou-e58e. Measured: the bar mirror law L(Z,N;q) - L(N,Z;1/q) = delta(q) has delta EXACTLY nucleus-independent (22-30 digits, A=2..6). Symbolically the ONLY non-bar-odd letter is the color-weighted interface, defect (q-1)^4 (q+1)^2 (q^2+1)^2 / (12 q^5) -- and interface letters are also exactly what separates the atom word from the free word. But the NUMBER of interfaces grows with A while delta does not. Nothing explains how a growing set of interface defects nets to an A-independent amount. This is the real open step; any closed form for delta comes through it. Blocked in practice by qou-j320 (symbolic trace). Audit: docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md section 4b.

LARGELY ANSWERED 2026-08-19 once qou-j320 landed. Symbolically, R(Z,N;q) = 12 q^a(Z,N) (q^2+1)^b(A) / P(q) with the SAME universal P at n=6, 9 and 12:

  P(q) = q^10 - 2q^9 + 7q^8 - 2q^6 + 4q^5 + 4q^4 + q^2 - 2q + 1   (irreducible over Q)

All nucleus dependence is in the MONOMIAL prefactor. The mirror-crossed ratio contributes q^(a + a_mirror + 2b), and that exponent is 12 in every case measured -- (1,1) 5+5+2, (1,2)/(2,1) 6+2+4, (2,2) 3+3+6 -- while P is universal. THAT CANCELLATION IS THE A-INDEPENDENCE. It is not a puzzle about growing interface counts after all: the interface count enters only through a and b, whose mirror sum is constant.

  exp(delta(q)) = q^12 P(1/q) / P(q)     -- verified against all five independent numeric measurements, 1e-29..2e-23 relative (the transfer floor). NOT fitted.

STILL OPEN (this bean stays open for these):
1. a + a_mirror + 2b = 12 is VERIFIED AT THREE n, NOT PROVED. A general-A argument closes this bean outright.
2. P is irreducible over Q and has NO structural interpretation -- correct and verified, but not explained. Where the coefficients (1,-2,7,0,-2,4,4,0,1,-2,1) come from is open.

Audit section 4c.
