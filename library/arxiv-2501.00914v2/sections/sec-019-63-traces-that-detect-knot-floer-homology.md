---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-019-63-traces-that-detect-knot-floer-homology
section_title: "Traces that detect knot Floer homology"
section_number: 6.3
pages: 31-34
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
sections to prove that then-trace of anyT 2,2g+1 recovers the knot Floer homology of any knot with
the samen-trace.
Proposition 6.9.Fixg≥1, and suppose for some knotK⊂S 3 and integern∈ZthatX n(K)∼=
Xn(T2,2g+1). Then
[HFK(K)∼= [HFK(T 2,2g+1)
as bigradedF-vector spaces, and ifKis not isotopic toT 2,2g+1 then it is hyperbolic.
Proof.Ifn≤0 thenK=T 2,2g+1 by Theorem 1.5, so from now on we assume thatn≥1.
SinceT 2,2g+1 is an L-space knot, Theorem 1.3 says thatKmust be an L-space knot of the
same genus asT 2,2g+1, namelyg. Since the knot Floer homology of an L-space knot is completely
determined by its Alexander polynomial [OS05], we will show that ∆ K(t) = ∆T2,2g+1(t).
32 JOHN A. BALDWIN AND STEVEN SIVEK
The identification of then-traces restricts to a homeomorphismS 3
n(K)∼= S3
n(T2,2g+1) between
their boundaries, which are rational homology spheres. The surgery formula for the Casson–Walker
invariant [Wal92] says that
λ(S3
n(K)) =λ(S 3
n(U)) + 1
n
∆′′
K(1)
2
and likewise forλ(S 3
n(T2,2g+1)), so since these two invariants are equal we must have
∆′′
K(1)
2 =
∆′′
T2,2g+1(1)
2 .
But Proposition 6.5 says that this is only possible if ∆ K(t) = ∆T2,2g+1(t), as promised, and so the
knot Floer homologies ofKandT 2,2g+1 coincide as well.
Supposing now thatKis not hyperbolic, it must be either a torus knot or a satellite knot
[Thu82, Corollary 2.5]. But ifKis an L-space knot with ∆ K(t) = ∆T2,2g+1(t), then we know by
Proposition 6.8 thatKcannot be a satellite knot. Thus it must be a torus knot, and in this case
[HFK(K)∼= [HFK(T 2,2g+1) implies thatK=T 2,2g+1 after all.□
This suffices to complete the proof of Theorem 6.1.
Proof of Theorem 6.1.Suppose thatX n(K)∼= Xn(T2,2g+1) but thatKis not isotopic toT 2,2g+1.
Then by Proposition 6.9 we know thatKis a hyperbolic L-space knot of genusg, with [HFK(K)∼=
[HFK(T 2,2g+1). In particular, sinceKis an L-space knot, it is fibered with right-veering monodromy.
Identifying the boundaries of then-traces now gives us a homeomorphism
S3
n(K)∼=S3
n(T2,2g+1).
SinceKis a fibered, hyperbolic L-space knot, it has right-veering monodromy, and then Proposi-
tion 5.7 tells us that 0<n<4g, as claimed.□
AppendixA.Non-characterizing slopes for torus knots
Here we describe a sequence of monic integer polynomialsa k(n),bk(n),ck(n),dk(n) andp k(n)
that determine a 2-parameter family of pairs of torus knots with lens space surgeries in common.
By Proposition 5.2 the torus knots in each pair must have different genera, although we do not
compute these genera directly.
Theorem A.1.For each integerk≥−1we define polynomialsa k,bk,ck,dk,pk,qk∈Z[n]by setting
(a−1,b−1,c−1,d−1,p−1,q−1) = (−1,1,1,1,0, n+ 1)
and then letting
(ak, bk, ck, dk) =

dk−1, qk−1−1
dk−1
, bk−1, qk−1 + 1
bk−1

,
(pk, qk) =

qk−1, b2
kd2
k−1
qk−1

for allk≥0. Then each ofa k,bk,ck,dk,pk,qk lies inZ[n], and fork≥0they are monic of degrees
k,k+ 1,k,k+ 1,2k+ 1, and2k+ 3respectively. Moreover, whenk≥1we havea k̸=c k and
bk̸=d k, and in these cases we have a homeomorphism
S3
pk(n)(Tak(n),bk(n))∼=S3
pk(n)(Tck(n),dk(n))
as surgeries on nontrivial torus knots for all integersn≥2.
L-SPACES AND KNOT TRACES 33
Remark A.2.Note that even thoughS 3
pk(Tak,bk)∼= S3
pk(Tck,dk) in the theorem, Proposition 5.2
says that these torus knots have different genera. Then Theorem 1.3 implies that the corresponding
traces are distinct,X pk(Tak,bk)̸∼=Xpk(Tck,dk).
Remark A.3.The restrictionn≥2 in Theorem A.1 is only needed to ensure that eachT ak,bk and
Tck,dk is a nontrivial torus knot, since whenn= 1 we can check by induction that
(ak,bk,ck,dk,pk,qk) = (2k+ 1,1,1,2k+ 3,2k+ 2,2k+ 4)
for allk≥−1, and thenb k(1) =c k(1) = 1 implies thatT ak(1),bk(1) andT ck(1),dk(1) are both unknots.
On the other hand, lettingF ℓ be theℓth Fibonacci number (withF 0 = 0,F 1 =F 2 = 1, and so on),
one can show that ifn= 2 then
(ak,bk) = (F2k +F 2k+2, F2k+3)p k =F 4k+4
(ck,dk) = (F2k+1, F2k+2 +F 2k+4)q k =F 4k+8
for allk≥−1; in this case we havea k(2), bk(2), ck(2), dk(2)≥2 for allk≥1.
Proof of Theorem A.1.A priori each ofa k,bk,ck,dk,pk,qk is only a rational function, but by con-
struction these satisfy
(A.1)a kbk + 1 =pk =c kdk−1
and
(A.2)b 2
kd2
k =p kqk + 1
for allk≥0. We compute directly that
(a0,b 0,c 0,d 0,p 0,q 0) = (1, n,1, n+ 2, n+ 1, n 3 + 3n2 +n−1),
verifying the proposition fork= 0.
We claim by induction that fork≥0, all ofa k,bk,ck,dk,pk,qk belong toZ[n] and have the
claimed degrees with leading coefficient 1. By inspection this is clearly true fork= 0. For larger
values ofk, we note thata k+1 =d k,c k+1 =b k, andp k+1 =q k satisfy the claim by inductive
hypothesis. Then (A.1) tells us thatb k andd k are relatively prime top k as elements ofZ[n], so by
combining (A.1) and (A.2) to get
pk(qk−1) = (b 2
kd2
k−1)−(c kdk−1) =d k(b2
kdk−ck)
pk(qk + 1) = (b2
kd2
k−1) + (akbk + 1) =bk(bkd2
k +ak),
we see thatd k dividesq k−1 andb k dividesq k + 1. This implies thatb k+1 = qk−1
dk
andd k+1 = qk+1
bk
are inZ[n] as well, and it follows by induction that they each have degreek+ 2 = (k+ 1) + 1 and
leading coefficient 1. This leaves onlyq k+1, for which we note that
b2
k+1d2
k+1 =
qk−1
dk
2qk + 1
bk
2
≡(b 2
kd2
k)−1 (modq k),
and by (A.2) the right side is 1 (modq k), so thatq k+1 =
b2
k+1d2
k+1−1
qk
is a polynomial as well, which
must then also have leading coefficient 1 and degree 4(k+ 2)−(2k+ 3) = 2(k+ 1) + 3. This
completes the induction.
We now establish the claim thata k ̸=c k andb k ̸=d k for anyk≥1 by noting that (A.1)
implies thatc kdk−a kbk = 2, from which gcd(a k,ck) and gcd(b k,dk) both divide 2. Since these
are polynomials of strictly positive degree with no non-constant common divisors, we cannot have
ak =c k orb k =d k.
34 JOHN A. BALDWIN AND STEVEN SIVEK
To conclude, we apply [Mos71] to see that for eachk≥1 andn≥2, we have
S3
pk(Tak,bk)∼=L(pk,b 2
k)∼=L(pk,d 2
k)∼=S3
pk(Tck,dk).
The relation (A.1) guarantees that these surgeries are the specified lens spaces, and these lens
spaces are identified in the middle because (A.2) implies thatb 2
kd2
k≡1 (modp k).□
We compute the first few values ofa k et al. in terms ofnas follows:
(a1,b 1) = (n+ 2, n2 +n−1),
(c1,d 1) = (n, n2 + 3n+ 1),
p1 =n 3 + 3n2 +n−1
(a2,b 2) = (n2 + 3n+ 1, n3 + 2n2−n−1),
(c2,d 2) = (n2 +n−1, n 3 + 4n2 + 3n−1),
p2 =n 5 + 5n4 + 6n3−2n 2−4n
(a3,b 3) = (n3 + 4n2 + 3n−1, n 4 + 3n3−3n),
(c3,d 3) = (n3 + 2n2−n−1, n 4 + 5n3 + 6n2−n−2),
p3 =n 7 + 7n6 + 15n5 + 5n4−15n 3−9n 2 + 3n+ 1
(a4,b 4) = (n4 + 5n3 + 6n2−n−2, n 5 + 4n4 + 2n3−5n 2−2n+ 1),
(c4,d 4) = (n4 + 3n3−3n, n5 + 6n4 + 10n3 +n 2−6n−1),
p4 =n 9 + 9n8 + 28n7 + 28n6−21n 5−49n 4−6n 3 + 18n2 + 3n−1
(a5,b 5) = (n5 + 6n4 + 10n3 +n 2−6n−1, n 6 + 5n5 + 5n4−6n 3−7n 2 + 2n+ 1)
(c5,d 5) = (n5 + 4n4 + 2n3−5n 2−2n+ 1, n 6 + 7n5 + 15n4 + 6n3−11n 2−6n+ 1)
p5 =n 11 + 11n10 + 45n9 + 75n8 + 6n7−126n 6−98n 5 + 50n4 + 60n3−4n 2−8n.
The casek= 1 is [NZ14, Example 1.1], up to a slight change of variables; settingn= 2 there yields
the relationS 3
21(T4,5)∼=S3
21(T2,11).
