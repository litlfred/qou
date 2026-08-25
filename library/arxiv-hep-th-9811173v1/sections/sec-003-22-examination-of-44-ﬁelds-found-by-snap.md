---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-003-22-examination-of-44-ﬁelds-found-by-snap
section_title: "Examination of 44 ﬁelds found by Snap"
section_number: 2.2
pages: 4-5
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
For the remaining 140−96 = 44 results of Tables 2–12, we made reference to the impressive
body of ﬁles 3 at the University of Melbourne. These were obtained by Coulson, Go odman,
Hodgson and Neumann [7] (hereafter referred to as CGHN) using 5 0-digit precision, in
marked distinction to the 5 digits which suﬃce for the ﬁndings above.
CGHN make no reference to Dedekind zeta values; they do, howeve r, ﬁnd single-
complex-place invariant trace ﬁelds for about 9% of the Hodgson–W eeks manifolds. The
next step was to examine the overlap between our single-complex-p lace ﬁelds and theirs.
We found that the CGHN ﬁle closed
census algebras contains 95 of our 96 single-
complex-place ﬁelds. The exception was the quintic ﬁeld with D = −14103, for which our
low-precision method had readily yielded the rational invariant a/b = 2 of the manifold
s784(+5, 2), which was absent from the ﬁle closed census algebras, obtained by CGHN
from 50-digit searches for ﬁelds of degree 4 not exceeding 16. We then referred to the ﬁle
closed.fields, where s784(+5, 2) indeed appears, with the expected invariant trace ﬁeld,
x5 − 2x4 + 2x3 −x2 − 2x − 1.
Thus assured that all our 96 ﬁnds were genuine, we extracted all o f the invariant trace
ﬁelds from the CGHN ﬁles closed census algebras and closed.fields, and asked Pari
to determine their signatures and discriminants. This revealed 44 ca ses beyond the ranges
of our search, namely the 32 below the lines in Tables 4–7 and the 12 in T ables 8–12.
Within our selected ranges, CGHN had found all and only our 96 single- complex-place
ﬁelds, indicating the reliability of both their methods and ours.
The next step was obvious, yet computationally demanding: to dete rmine rational
Dedekind-zeta invariants for the manifolds associated by Snap to t he remaining 44 large-
discriminant single-complex-place ﬁelds. The zetak command of Pari was entirely ade-
3http://www.ms.unimelb.edu.au/~snap
4We later ran Snap at 100-digit precision, and found a group ﬁeld of de gree 20.
3
quate to complete Tables 4–7, at 19-digit precision, yielding numerat ors and denominators
bounded by a ≤ 976 and b ≤ 5, for which merely 7-digit precision would have been amply
suﬃcient. The 12 ﬁelds of Tables 8–12 presented a much tougher co mputational challenge.
At degreen = 8, Pari-GP 2.0.11 began to falter, with zetak yielding results drastically
below the requested precision (as warned in the Pari manual) or run ning out of memory
(when allocated 100MB of core). Accordingly we devised a method ba sed on the dirzetak
command, which returns the multiplicities, mK(n), of the ideals of K with norm n, up
to some requested maximum, N, that may comfortably extend to N = 10 6. These
multiplicities are the numerators of the Dirichlet series
ζK(2) =
∑
n>0
mK(n)
n2 (3)
We then computed the truncated sums SN := ∑ N
n=1mK(n)/n 2, and accelerated their
convergence by forming TN,M := (SNN −SMM)/ (N −M), with M ≈ 1
2N. This removes
a predictable O(1/N ) truncation error, leaving an O(1/N 3/ 2) “random-walk” error. With
N ≤ 106, we were able to achieve 10-digit precision, by averaging out ﬂuctua tions inTN,M .
Even in the most demanding case of Table 12, where the rational inva riant is a 7-digit
integer, we were left with 3 vanishing decimal places for a/b = 9408656. 000 ± 0. 001.
Hence we completed the task for Hodgson–Weeks manifolds. Tables 2–12 give 140
single-complex-place invariant trace ﬁelds of closed census manifold s, of which 96 were
detected by us without reference to CGHN. The 224 distinct censu s volumes rationally
related to the Dedekind zeta values of these ﬁelds are given in Tables 13a-f. These 224
distinct volumes correspond to 998 of the 11,031 entries of the Hod gson–Weeks census ﬁle
ClosedManifolds available5 from the Geometry Center at the University of Minnesota.
