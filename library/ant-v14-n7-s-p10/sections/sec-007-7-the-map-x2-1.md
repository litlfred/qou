---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-007-7-the-map-x2-1
section_title: "The map x2 − 1"
section_number: 7
pages: 13-15
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Introduction; Some algebraic lemmas; Ramiﬁcation and postcritically inﬁ"
---
It is well known that there are exactly three Q-conjugacy classes of postcritically ﬁnite quadratic poly-
nomials over Q, represented by x2, x2− 1, and x2− 2. By Q-conjugacy it sufﬁces to check the family
φc(x)= x2+ c for c∈ Q, and the assumption that the critical point 0 is preperiodic (i.e.,φm
c(0)=φn
c(0)
for m< n) forces c to be an algebraic integer (hence a rational integer) and also an element of the complex
Mandelbrot set M={ c∈ C|φn
c(0)⁄→∞} . It is elementary to check that M∩ Z={− 2,−1, 0}.
Since x2 and x2− 2 are a powering map and a Chebyshev map, respectively, they are treated by
Theorems 12 and 13, and the stable postcritically inﬁnite quadratic case is treated in Theorem 8. Thus in
order to complete the proof of Theorem 1, it sufﬁces to consider the polynomial φ(x)= x2− 1 over Q in
the stable case.
In order to show that K∞(x2− 1,α)/ Q is never an abelian extension, one might hope to combine
the bound B0(Qab)≥(log 5)/12= 0.134... of Amoroso and Dvornicich with Theorem 14, but it turns
out that the Arakelov–Zhang pairing ⟨x2− 1, x2⟩= 0.167... is too large for this argument to apply
directly. However, we can recover this strategy (in the stable case) by showing that if K∞(x2− 1,α)
is an abelian extension of Q then it is contained in the subﬁeld Q(µ2∞) of Qab, which has Bogomolov
constant B0(Q(µ2∞))≥(log 2)/4= 0.173... , large enough to obtain a contradiction.
1994 Jesse Andrews and Clayton Petsche
Lemma 16. Letφ(x)= x2− 1, letα∈ K , and assume that the pair (φ,α) is stable over K and that
K∞= K∞(x2− 1,α) is an abelian extension of K . If p is a prime of K with residue characteristic not
equal to 2, then p is unramiﬁed in K∞.
Proof. The stability and abelian hypotheses imply via Lemma 2 that [Kn: K]= 2n for all n≥ 1. Let
ψ(x)=φ(x+α)−α= x2+ 2αx+α2−α− 1. The critical point of ψ(x) is c=−α, which is part of a
2-cycle; that is,ψn(c)=−α for all even n, andψn(c)=− 1−α for all odd n. Clearly
disc(φ(x)−α)= 4(1+α)
and using Lemma 5 for n≥ 2 we have
disc(φn(x)−α)= disc(φn(x+α)−α)= disc(ψn(x))=
{R2
n(−α) if n≥ 2 is even,
R2
n(−1−α) if n≥ 3 is odd,
for some nonzero Rn∈ K .
Case 1:−1−α is not a square in K . Then disc(φn(x)−α) is not a square for all odd n≥ 3, and thus
viewing Gal(Kn/K) as a subgroup of S2n via its action on the roots of φn(x)−α, Gal(Kn/K) is not a
subgroup of A2n for all odd n≥ 3. By Lemma 4, it follows that Gal(Kn/K) is cyclic for all odd n≥ 3.
Then Gal(Kn/K) must be cyclic for all n, since Gal(Km/K) is a quotient of Gal(Kn/K) when 1≤ m< n.
We conclude from Lemma 7 that no primes of K of odd residue characteristic ramify in K∞.
Case 2:−1−α= t2 for t∈ K . By the stability hypothesis we know thatdisc(φ(x)−α)= 4(1+α)=− 4t2
is not a square in K , and thus we conclude that −1 is not a square in K and K1= K(φ−1(α))=
K(√4(1+α))= K(
√
−1). In particular, no primes of K with odd residue characteristic ramify in K1,
so it now sufﬁces to show that no primes of K1 with odd residue characteristic ramify in K∞.
Letφ−1(α)={α′,α′′}. Thus for each n≥ 1, we have a disjoint union
φ−n(α)=φ−(n−1)(α′)∐φ−(n−1)(α′′).
and it follows from the transitive action of Gal(Kn/K) onφ−n(α) that Gal(Kn/K1) acts transitively on
φ−(n−1)(α′). We conclude that(φ,α′) is a stable pair over K1. Arguing as above, it follows that 1+α′ is
not a square in K1, and as−1 is a square in K1, we deduce that−1−α′ is not a square in K1. We are
now in the setting of Case 1 for the pair (φ,α′) over K1, and we conclude that no primes of K1 with odd
residue characteristic ramify in K∞. □
Theorem 17. Letφ(x)= x2− 1, letα∈ Q, and assume that the pair(φ,α) is stable. Then Gal(K∞/Q)
is nonabelian.
Proof. Assume on the contrary that K∞/Q is an abelian extension. By Lemma 16, no odd primes ramify
in K∞, and it follows from class ﬁeld theory that K∞⊆ Q(µ2∞). As we will calculate in Section 8, we
have
⟨x2− 1, x2⟩= 0.167..., (14)
Abelian extensions in dynamical Galois theory 1995
and we conclude from Theorem 14 that B0(Q(µ2∞))≤⟨ x2− 1, x2⟩= 0.167... . This is a contradiction
of the bound B0(Q(µ2∞))≥(log 2)/4= 0.173... proved in Theorem 10. □
