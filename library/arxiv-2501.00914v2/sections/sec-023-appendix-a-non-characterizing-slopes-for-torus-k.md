---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-023-appendix-a-non-characterizing-slopes-for-torus-k
section_title: "Appendix A. Non-characterizing slopes for torus knots"
section_number: null
pages: 32-34
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Here we describe a sequence of monic integer polynomials ak(n), bk(n), ck(n), dk(n) and pk(n)
that determine a 2-parameter family of pairs of torus knots with lens space surgeries in common.
By Proposition 5.2 the torus knots in each pair must have different genera, although we do not
compute these genera directly.
Theorem A.1. For each integer k ≥−1 we define polynomials ak, bk, ck, dk, pk, qk ∈Z[n] by setting
(a−1, b−1, c−1, d−1, p−1, q−1) = (−1, 1, 1, 1, 0, n + 1)
and then letting
(ak, bk, ck, dk) =

dk−1, qk−1 −1
dk−1
, bk−1, qk−1 + 1
bk−1

,
(pk, qk) =

qk−1, b2
kd2
k −1
qk−1

for all k ≥0. Then each of ak, bk, ck, dk, pk, qk lies in Z[n], and for k ≥0 they are monic of degrees
k, k + 1, k, k + 1, 2k + 1, and 2k + 3 respectively. Moreover, when k ≥1 we have ak̸ = ck and
bk̸ = dk, and in these cases we have a homeomorphism
S3
pk(n)(Tak(n),bk(n)) ∼= S3
pk(n)(Tck(n),dk(n))
as surgeries on nontrivial torus knots for all integers n ≥2.
L-SPACES AND KNOT TRACES
33
Remark A.2. Note that even though S3
pk(Tak,bk) ∼= S3
pk(Tck,dk) in the theorem, Proposition 5.2
says that these torus knots have different genera. Then Theorem 1.3 implies that the corresponding
traces are distinct, Xpk(Tak,bk)̸ ∼= Xpk(Tck,dk).
Remark A.3. The restriction n ≥2 in Theorem A.1 is only needed to ensure that each Tak,bk and
Tck,dk is a nontrivial torus knot, since when n = 1 we can check by induction that
(ak, bk, ck, dk, pk, qk) = (2k + 1, 1, 1, 2k + 3, 2k + 2, 2k + 4)
for all k ≥−1, and then bk(1) = ck(1) = 1 implies that Tak(1),bk(1) and Tck(1),dk(1) are both unknots.
On the other hand, letting Fℓbe the ℓth Fibonacci number (with F0 = 0, F1 = F2 = 1, and so on),
one can show that if n = 2 then
(ak, bk) = (F2k + F2k+2, F2k+3)
pk = F4k+4
(ck, dk) = (F2k+1, F2k+2 + F2k+4)
qk = F4k+8
for all k ≥−1; in this case we have ak(2), bk(2), ck(2), dk(2) ≥2 for all k ≥1.
Proof of Theorem A.1. A priori each of ak, bk, ck, dk, pk, qk is only a rational function, but by con-
struction these satisfy
(A.1)
akbk + 1 = pk = ckdk −1
and
(A.2)
b2
kd2
k = pkqk + 1
for all k ≥0. We compute directly that
(a0, b0, c0, d0, p0, q0) = (1, n, 1, n + 2, n + 1, n3 + 3n2 + n −1),
verifying the proposition for k = 0.
We claim by induction that for k ≥0, all of ak, bk, ck, dk, pk, qk belong to Z[n] and have the
claimed degrees with leading coefficient 1. By inspection this is clearly true for k = 0. For larger
values of k, we note that ak+1 = dk, ck+1 = bk, and pk+1 = qk satisfy the claim by inductive
hypothesis. Then (A.1) tells us that bk and dk are relatively prime to pk as elements of Z[n], so by
combining (A.1) and (A.2) to get
pk(qk −1) = (b2
kd2
k −1) −(ckdk −1) = dk(b2
kdk −ck)
pk(qk + 1) = (b2
kd2
k −1) + (akbk + 1) = bk(bkd2
k + ak),
we see that dk divides qk −1 and bk divides qk + 1. This implies that bk+1 = qk−1
dk
and dk+1 = qk+1
bk
are in Z[n] as well, and it follows by induction that they each have degree k + 2 = (k + 1) + 1 and
leading coefficient 1. This leaves only qk+1, for which we note that
b2
k+1d2
k+1 =
qk −1
dk
2 qk + 1
bk
2
≡(b2
kd2
k)−1
(mod qk),
and by (A.2) the right side is 1 (mod qk), so that qk+1 =
b2
k+1d2
k+1−1
qk
is a polynomial as well, which
must then also have leading coefficient 1 and degree 4(k + 2) −(2k + 3) = 2(k + 1) + 3. This
completes the induction.
We now establish the claim that ak̸ = ck and bk̸ = dk for any k ≥1 by noting that (A.1)
implies that ckdk −akbk = 2, from which gcd(ak, ck) and gcd(bk, dk) both divide 2. Since these
are polynomials of strictly positive degree with no non-constant common divisors, we cannot have
ak = ck or bk = dk.
34
JOHN A. BALDWIN AND STEVEN SIVEK
To conclude, we apply [Mos71] to see that for each k ≥1 and n ≥2, we have
S3
pk(Tak,bk) ∼= L(pk, b2
k) ∼= L(pk, d2
k) ∼= S3
pk(Tck,dk).
The relation (A.1) guarantees that these surgeries are the specified lens spaces, and these lens
spaces are identified in the middle because (A.2) implies that b2
kd2
k ≡1 (mod pk).
□
We compute the first few values of ak et al. in terms of n as follows:
(a1, b1) = (n + 2, n2 + n −1),
(c1, d1) = (n, n2 + 3n + 1),
p1 = n3 + 3n2 + n −1
(a2, b2) = (n2 + 3n + 1, n3 + 2n2 −n −1),
(c2, d2) = (n2 + n −1, n3 + 4n2 + 3n −1),
p2 = n5 + 5n4 + 6n3 −2n2 −4n
(a3, b3) = (n3 + 4n2 + 3n −1, n4 + 3n3 −3n),
(c3, d3) = (n3 + 2n2 −n −1, n4 + 5n3 + 6n2 −n −2),
p3 = n7 + 7n6 + 15n5 + 5n4 −15n3 −9n2 + 3n + 1
(a4, b4) = (n4 + 5n3 + 6n2 −n −2, n5 + 4n4 + 2n3 −5n2 −2n + 1),
(c4, d4) = (n4 + 3n3 −3n, n5 + 6n4 + 10n3 + n2 −6n −1),
p4 = n9 + 9n8 + 28n7 + 28n6 −21n5 −49n4 −6n3 + 18n2 + 3n −1
(a5, b5) = (n5 + 6n4 + 10n3 + n2 −6n −1, n6 + 5n5 + 5n4 −6n3 −7n2 + 2n + 1)
(c5, d5) = (n5 + 4n4 + 2n3 −5n2 −2n + 1, n6 + 7n5 + 15n4 + 6n3 −11n2 −6n + 1)
p5 = n11 + 11n10 + 45n9 + 75n8 + 6n7 −126n6 −98n5 + 50n4 + 60n3 −4n2 −8n.
The case k = 1 is [NZ14, Example 1.1], up to a slight change of variables; setting n = 2 there yields
the relation S3
21(T4,5) ∼= S3
21(T2,11).
