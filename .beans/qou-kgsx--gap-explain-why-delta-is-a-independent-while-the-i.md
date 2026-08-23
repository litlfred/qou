---
# qou-kgsx
title: 'GAP: explain why delta is A-independent while the interface-letter count grows (bar-involution mirror law)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T19:46:56Z
updated_at: 2026-08-23T12:58:16Z
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

ANSWERED 2026-08-19 -- BY CORRECTING MY OWN PREMISE, not by solving it.

THIS BEAN WAS OPENED ON A MISCOUNT. It asserted "the NUMBER of interface letters grows with A, yet delta does not". FALSE. Censusing the words by letter type, every atom word carries EXACTLY ONE color-weighted p-n interface, at every A. Verified on 16 nuclei up to A=10:

    1     p-n interface  (the one non-bar-odd letter)   <- ALWAYS 1
    Z-1   p-p bonds      (d = 0,  plain sigma)
    N-1   n-n bonds      (d = -h, sigma-inverse-like)
    -----
    A-1   bonds total

Both bond types are EXACTLY bar-odd (0 -> 0, -h -> +h) so they contribute nothing to delta. delta is A-independent for the plain reason that its sole source occurs once however many nucleons there are. There was no puzzle.

THE PRODUCT FORMULA (numeric: 16 nuclei A=2..10, worst |ratio-1| = 4.5e-31, the transfer floor; SYMBOLIC: 6 nuclei at n=6,9,12 including both orientations of the A=4 mirror pair):

    tr_M^free / tr_M^atom = (12 / P(q)) * (q + 1/q)^(A-1) * q^(6 + 2(N-Z))

Each factor earns its place in delta:
 * (q + 1/q)^(A-1) -- one Cayley-Hamilton denominator per bond, A-1 bonds. BAR-EVEN, so it CANCELS between R(Z,N;q) and R(N,Z;1/q). THAT CANCELLATION IS THE A-INDEPENDENCE.
 * q^(6+2(N-Z)) -- pure ISOSPIN monomial. Mirror-crossing gives q^12 exactly: the isospin dependence cancels. THE 12 IS 2x6, twice the isospin-neutral exponent.
 * P(q) -- universal, contributes P(1/q)/P(q) and nothing else.

=> exp(delta) = q^12 P(1/q)/P(q) for EVERY (Z,N), an identity given the product formula rather than three checked points. The earlier bookkeeping a = 7-3Z+N, b = A-1, a+a_mirror+2b = 12 is the same statement in worse coordinates: a = 6+2(N-Z)-(A-1), the -(A-1) being the q in each bond (q^2+1)/q.

STILL OPEN, and this bean stays open for them:
1. The PRODUCT FORMULA is verified, not proved from the transfer. Bond count and one-(q+1/q)-per-bond follow from the Cayley-Hamilton reduction in _alpha_beta; the isospin exponent 6+2(N-Z) is MEASURED.
2. P is irreducible over Q and remains UNINTERPRETED.

Audit section 4d.
