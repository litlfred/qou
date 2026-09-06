---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-016-52-satellite-knots
section_title: "Satellite knots"
section_number: 5.2
pages: 24-27
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
genus asTp,q, and ifS 3
r (K)∼=S3
r (Tp,q), thenrmust be large enough so that their commonr-surgery
is an L-space.
Lemma 5.3.Suppose for some nontrivial satellite knotK=P(C)and sloper∈Qthat the
companion torus∂ν(C)is compressible inS 3
r (K). Thenr̸= 0, and ifS 3
r (K)is irreducible then
•the patternP⊂S 1×D 2 has a nontrivialS 1×D 2 surgery, and is therefore a 0-bridge braid
or a 1-bridge braid, with winding numberw≥2in either case;
•r-surgery on the patternP⊂S 1×D 2 is a solid torus;
•andS 3
r (K)∼=S3
r/w2(C).
Proof.Since the companion torus∂ν(C) inS 3\ν(K) compresses inS 3
r (K), the resultZofr-surgery
on the patternP⊂S 1×D 2 must have compressible boundary. Thus Gabai [Gab89, Theorem 1.1]
showed that either
•Z ∼=S1×D 2, andPis either a 0-bridge braid or a 1-bridge braid; or
•Z ∼= (S1×D 2)#Y, whereYis closed with|H 1(Y)|finite and nontrivial.
L-SPACES AND KNOT TRACES 25
Scharlemann [Sch90] showed that in the latter casePmust be a cable of a 0-bridge braid, andY
is then a lens space. Thus in either casePhas nonzero winding numberw≥1.
Next, we determine how theS 1×D 2 summand ofZis glued to the exterior of the companion
Cto formS 3
r (K). WritingV=S 1×D 2 for the solid torus containingP, we know from [Gor83,
Lemma 3.3] (plus the fact thatw̸= 0) that inV r(P)∼=Z, the peripheral class
a[{pt}×∂D 2] +bw 2[S1×{pt}]
is nullhomologous. Since{pt}×∂D 2 andS 1×{pt}in∂Vare identified with the meridianµ C and
longitudeλ C ofC, respectively, it follows that theS 1×D 2 summand ofZfills the exterior ofC
along a curve of slope a
bw2 = r
w2 . In other words, we have
S3
r (K)∼=S3
r/w2(C) orS 3
r/w2(C)#Y
depending on whetherZisS 1×D 2 or (S 1×D 2)#Y.
We now claim thatZ ∼= S1×D 2. Indeed, if we assume instead thatZ ∼= (S1×D 2)#Y, then
we have seen thatS 3
r (K)∼=S3
r/w2(C)#Y; butCbeing nontrivial means thatS 3
r/w2(C)̸∼=S3, and
soS 3
r (K) would then be reducible. Assuming from now on thatS 3
r (K) is irreducible, which is
automatically satisfied ifr= 0 [Gab87], we then haveZ ∼=S1×D 2 as claimed, and soS 3
r (K) is a
Dehn filling ofC. It follows that
S3
r (K)∼=S3
r/w2(C),
and moreover thatPis a 0-bridge braid or a 1-bridge braid inS 1×D 2. The latter fact tells us
thatw≥2, because if we hadw= 1 thenPwould have to be isotopic to the core ofS 1×D 2 and
we know that it is not.
Finally, in the caser= 0 we haveS 3
0(K)∼=S3
0(C), sog(K) =g(C) [Gab87]. On the other hand,
sincew≥2 we know that
g(K) =g(P(U)) +w·g(C)≥2g(C),
henceg(C)≥2g(C) and we have a contradiction. We conclude thatr̸= 0 after all.□
Lemma 5.4.LetT p,q be a torus knot, with|p|,|q|≥2relatively prime, and fix a sloper∈Q.
(1) The Dehn surgeryS 3
r (Tp,q)is reducible if and only ifr=pq.
(2) IfS 3
r (Tp,q)has an incompressible torus, thenr= 0andT p,q =T±2,3.
Proof.Moser [Mos71] showed thatS 3
pq(Tp,q) is a connected sum of two lens spaces, of orderspand
q; and that ifr̸=pqthenS 3
r (Tp,q) is small Seifert fibered with base orbifoldS 2(p,q,∆(pq,r)),
hence irreducible. This establishes (1).
For (2), we can assume thatr̸=pqsince a sum of lens spaces is atoroidal. SinceS 3
r (Tp,q) is
small Seifert fibered it has no vertical incompressible tori, so it must be covered byT 3 [Mar16,
Corollary 10.4.13] and therefore admit a flat metric. Up to orientation, the only such 3-manifold
with cyclic first homology isS 3
0(T2,3), by [Mar16, Theorem 12.3.1] and [Mar16, Proposition 10.3.38].
But ifS 3
r (Tp,q)∼=±S3
0(T2,3) thenr= 0 for homological reasons, and by [Mos71] the two sides of
this identification are both Seifert fibered with base orbifoldsS 2(|p|,|q|,|pq|) ∼= S2(2,3,6), so we
must have{|p|,|q|}={2,3}and thereforeT p,q is a trefoil.□
Proposition 5.5.Fix a positive torus knotT p,q, wherep,q≥2are relatively prime positive inte-
gers, and suppose for some nontrivial satellite knotKand rationalr∈QthatS 3
r (K)∼=S3
r (Tp,q).
IfKis an L-space knot, thenr≥2g(K)−1.
26 JOHN A. BALDWIN AND STEVEN SIVEK
Proof.We writeK=P(C), with patternPand companionC. Ifr=pqthenS 3
r (K)∼= S3
r (Tp,q)
is a connected sum of two lens spaces, of orderspandq[Mos71], soS 3
r (K) is an L-space and
thereforer≥2g(K)−1. Thus we can assume from now on thatr̸=pq. In particular, Lemma 5.4
says thatS 3
r (K)∼= S3
r (Tp,q) is irreducible, and that it is atoroidal unlessS 3
r (K)∼= S3
0(T2,3). In
the latter case we must haver= 0, and thenKmust be fibered of genus 1 [Gab87]; but the only
genus-1 fibered knots are the trefoils and the figure eight, and none of these are satellites, so in fact
S3
r (K)∼=S3
r (Tp,q) must be atoroidal.
We have now shown that the companion torus must compress inS 3
r (K), so we can apply
Lemma 5.3 to see thatr-surgery onPis a solid torus – in other words, thatPis aBerge–Gabai
knot– and that
S3
r (K)∼=S3
r/w2(C),
wherew≥2 is the winding number ofP. As a consequence ofPbeing a Berge–Gabai knot,
Lemma 5.3 tells us via [Gab89] that the patternPis either a torus knot (i.e., a 0-bridge braid)
or a 1-bridge braid; we will handle each of these cases separately, bearing in mind that we are not
interested in arbitrary 1-bridge braids but only those with solid torus surgeries.
First, ifPis a torus knot thenKis some (m,n)-cable of the companionC, where gcd(m,n) = 1
andn=w≥2. Then sinceKis an L-space knot, Hom [Hom11] proved thatCis an L-space knot
and that
m
n ≥2g(C)−1;
in fact, the inequality must be strict sincen∤m, so m−1
n ≥2g(C)−1. Moreover, we know from
[Gor83, Corollary 7.3] thatS 3
r (K) is only irreducible and atoroidal ifr=mn± 1
k for somek∈Z,
in which case
S3
r (K)∼=S3
r/n2(C).
Now we have
r
n2 = mn± 1
k
n2 ≥ m
n− 1
n2≥ m−1
n ≥2g(C)−1,
soS 3
r (K)∼=S3
r/n2(C) is an L-space, hencer≥2g(K)−1.
More generally, Hom–Lidman–Vafaee [HLV14, Theorem 1.3] classified the L-space satellite knots
whose patterns are Berge–Gabai knots. Each Berge–Gabai knotPis described by a triple of integers
(w,b,t),0≤b≤w−2,
which are the winding number, bridge width, and twist number ofPrespectively; they show that
K=P(C) is an L-space knot if and only ifCis an L-space knot andb+tw≥w 2(2g(C)−1).
Moreover, if the Berge–Gabai knotPis specifically a 1-bridge braid, then [HLV14, Lemma 2.1]
says thatr-surgery onPis a solid torus only if
r=tw+d, d∈{b,b+ 1}.
So in this case we have
r
w2≥ b+tw
w2 ≥2g(C)−1
and henceS 3
r (K)∼= S3
r/w2(C) is an L-space. This means thatr≥2g(K)−1 once again, and we
are done. □
L-SPACES AND KNOT TRACES 27
