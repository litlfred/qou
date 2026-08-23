---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-012-18-tom-h-koornwinder-and-ren-e-f-sw-arttouw
section_title: "TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW"
section_number: 18
pages: 18-19
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Now, by [11, Lemma A.1] (read −1 ≤ µ − λ instead of 0 ≤ µ − λ in the formulation
of that lemma), we see that
q(α +j)/ 2 − q1+(α +j)/ 2
1 − q1+α +j
increases to (1 + α + j)− 1 as q ↑ 1 if α + j ≥ 0. So, the expression in (A.1), for
1/ 2 < q < 1, is dominated by
(2α/ 2|z|)k
(α + 1)k k! if α ≥ 0
and by
const. |z|k
(α + 1)k k! if −1 < α < 0.
So the proposition follows by dominated convergence. □
Appendix B. Proof of Propostion 4.2
First observe that u(z) := 2φ 1(a, b ; c; q, z ) (c not a non-positive integer power of
q) is analytic in z on C outside the set {q− l | l = 0 , 1, 2, . . . }, on which points the
function has possible poles. This follows immediately by re writing the second order
q-diﬀerence equation for u, given in [6, Exercise 1.13], as
(B.1) u(z) = ( z − 1)− 1(
((qa + qb)z − qc− 1 − 1)u(qz) + (qc− 1 − qa+bz)u(q2z)
)
.
Indeed, u(z) is analytic in z for |z| < 1. Then (B.1) shows that u(z) can be extended
to an analytic function in z for |z| < q − 1 with possible pole in 1, and then by iter-
ation to an analytic function for |z| < q − l with possible poles in 1 , q − 1, . . . , q − l+1.
Now use the identity (see [6, (4.3.2)])
(B.2) 2φ 1(a, b ; c; q, z ) = (b, c/a, az, q/ (az); q)∞
(c, b/a, z, q/z ; q)∞
2φ 1(a, aq/c ; aq/b ; q, cq/ (abz))
+ (a, c/b, bz, q/ (bz); q)∞
(c, a/b, z, q/z ; q)∞
2φ 1(b, bq/c ; bq/a ; q, cq/ (abz)),
where a/b and z are not an integer power of q, where c and cq/ (abz) are not a
non-positive integer power of q, and where a, b, c, z ⁄= 0. Now put z := qn+1/a
(n = 0 , 1, 2, . . . ) in (B.2). Then the ﬁrst term on the right-hand side of (B.2)
vanishes and after some rewriting of the coeﬃcient in the sec ond term we obtain
(B.3) 2φ 1(a, b ; c; q, q n+1/a ) = (qb/a, c/b ; q)∞
(c, q/a ; q)∞
b− n
2φ 1(qb/c, b ; qb/a ; q, q − nc/b ),
where initially a/b and a are not an integer power of q, c and q− nc/b are not a
non-positive integer power of q, and a, b, c ⁄= 0. By continuity we see that (B.3)
more generally holds if c, qb/a, q/a, q − nc/b are not a non-positive integer power of
q and a, b, c ⁄= 0. The case of (B.3) with n a non-positive integer then follows by
redeﬁning the parameters in (B.3). Finally we can state:
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 19
Lemma B.1. Formula (B.3) is valid for integer n if c, qb/a, q/a, q n+1/a, q − nc/b, c/b
are not a non-positive integer power of q and a, b, c ⁄= 0.
Now consider (2.5). Initially this is proved (see [6, (1.4.1 )]) for |z|, |b| < 1 and
c, az not a non-positive integer power of q. By analytic continuation (2.5) is more
generally valid for z, b, c, az not a non-positive integer power of q.
Let us turn to the proof of Proposition 4.2. Proceed with (4.5 ) as written just
before Proposition 4.2 and take into account the constraint s for (2.5) as just men-
tioned. Then we initially obtain, under the assumptions tha t |sxy| < 1 and x2, y 2
are not non-positive integer powers of q, that (4.7) holds with the ﬁrst expression
taken on the right-hand side if n ≥ m and qn− ms− 1xy− 1 not a non-positive integer
power of q, and that it holds with the second expression taken on the rig ht-hand
side if m ≥ n and qm− ns− 1yx− 1 not a non-positive integer power of q. However,
by Lemma B.1, the two expressions on the right-hand side of (4 .7) are equal to each
other for all integer values of m, n if s− 1xy− 1, q n− ms− 1xy− 1, s − 1yx− 1, q m− ns− 1yx− 1
are not a non-positive integer power of q. Hence, under these last constraints the
left-hand side of (4.7) is equal to both expressions on the ri ght-hand side for all
integer values of m, n . Finally, if s− 1xy− 1, q n− ms− 1xy− 1 are not a non-positive
integer power of q but s− 1yx− 1 or qm− ns− 1yx− 1 is a non-positive integer power of
q, then by continuity the left-hand side of (4.7) is still equa l to the ﬁrst expression
on the right-hand side. Similarly, if s− 1yx− 1, q m− ns− 1yx− 1 are not a non-positive
integer power of q but s− 1xy− 1 or qn− ms− 1xy− 1 is a non-positive integer power
of q, then the left-hand side of (4.7) is still equal to the second expression on the
right-hand side.
