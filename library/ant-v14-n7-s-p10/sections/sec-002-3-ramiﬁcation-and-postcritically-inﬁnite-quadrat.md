---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-002-3-ramiﬁcation-and-postcritically-inﬁnite-quadrat
section_title: "Ramiﬁcation and postcritically inﬁnite quadratic maps"
section_number: 3
pages: 5-8
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Introduction; Some algebraic lemmas; Ramiﬁcation and postcritically inﬁ"
---
We recall standard facts and notation surrounding a ﬁnite Galois extension L/K of number ﬁelds; see
Lang [1970, Chapter 1]. Given a prime p of K , by the Galois assumption we have a factorization of the
form pOL= qe
1··· qe
r for primes q1,..., qr of L, and re f=[ L: K], where e= e(qi/p) and f= f(qi/p)
1986 Jesse Andrews and Clayton Petsche
are the (common) ramiﬁcation indices and inertial degrees of the qi, respectively. Moreover, each OL/qi
is a degree f extension of OK/p. For each 1≤ i≤ r, let
Dqi/p={σ∈ Gal(L/K)|σ( qi)= qi}
Iqi/p={σ∈ Dqi/p|σ( x)≡ x (mod qi) for all x∈ OL}
be the associated decomposition and inertia groups. Thus Iqi/p has order e(qi/p), p is unramiﬁed in L Iqi/p,
and if p′ denotes any prime of L Iqi/p lying over p, then p′ is totally ramiﬁed in L.
Lemma 6. Let L/K be a Galois extension of number ﬁelds and let p be a prime of K which is tamely
ramiﬁed in L. Let q be a prime of L lying over p. Then
e(q/p)≤| OK/p| f(q/p)− 1.
Proof. Letπ∈ OL be a uniformizer for q, and consider the group homomorphism
Iq/p→(OL/q)×
σ↦→σ(π)/π (mod q)
Standard arguments from the theory of local ﬁelds show that this map does not depend on the choice of
uniformizer, and the tame ramiﬁcation hypothesis implies that it is injective; see [Cassels and Fröhlich
1967, Section I.8]. Together with the fact that|OL/q|=| OK/p| f(q/p), we obtain the desired inequality. □
Lemma 7. Let K be a number ﬁeld, let K= K0⊂ K1⊂ K2⊂··· be a tower of distinct cyclicp-extensions
of K , and let K∞=⋃ Kn. If p is a prime of K with residue characteristic not equal to p, then p is
unramiﬁed in K∞.
Proof. Since a quotient of a cyclic p-group is another cyclic p-group, without loss of generality we may
insert intermediate ﬁelds and reindex to ensure that[Kn: Kn−1]= p for all n≥ 1. Since Gal(Kn/K) is a
cyclic p-group, its subgroups are totally ordered by inclusion, and thus the same is true of intermediate
ﬁelds K⊆ F⊆ Kn. In particular, the ﬁelds K= K0⊂ K1⊂···⊂ Kn are the only subﬁelds of Kn
containing K .
Contrary to what has been claimed, assume that p has residue characteristic not equal to p and that p
ramiﬁes (hence tamely ramiﬁes) in K∞. Let p0= p, and for each n≥ 1, let pn be a prime of Kn lying over
pn−1. Let n0 be maximal with the property that p is unramiﬁed in Kn0; thus pn0 is ramiﬁed in Kn0+1. Let
n> n0 be arbitrary, and deﬁne Fp= K
Ipn/p
n , the ﬁxed ﬁeld of the inertia subgroup Ipn/p of Gal(Kn/K). In
particular, p is unramiﬁed in Fp, and if p′ denotes any prime of Fp lying over p, then p′ is totally ramiﬁed
in Kn. Since we must have Fp= Km for some 0≤ m≤ n, the only possibility is Fp= Kn0.
To summarize, we have shown that p is unramiﬁed in Kn0, and that pn0 is totally ramiﬁed in Kn for all
n> n0. In particular, we have
f(pn/p)= f(pn0/p)≤[ Kn0: K]= pn0,
e(pn/p)= e(pn/pn0)=[ Kn: Kn0]= pn−n0.
(4)
Abelian extensions in dynamical Galois theory 1987
But for large enough n, (4) contradicts the bound
e(pn/p)≤| OK/p| f(pn/p)− 1.
which follows from Lemma 6. □
Theorem 8. Letφ(x)∈ K[x] be a quadratic polynomial which is not postcritically ﬁnite, letα∈ K , and
assume that the pair(φ,α) is stable. Then Gal(K∞/K) is nonabelian.
Proof. Letφ(x)∈ K[x] be a quadratic polynomial which is not postcritically ﬁnite, let α∈ K , assume
that the pair(φ,α) is stable, and assume that Gal(K∞/K) is abelian; we will obtain a contradiction.
We ﬁrst prove that Gal(Kn/K) is cyclic for all n≥ 1. To see this, note ﬁrst that the stability and abelian
hypotheses imply via Lemma 2 that[Kn: K]= 2n for all n≥ 1. It sufﬁces to show that Gal(Kn/K) is
cyclic for arbitrarily large n, because if Gal(Kn/K) is cyclic then so are its quotients Gal(Km/K) for
1≤ m< n. By the stability hypothesis and Lemma 4, it sufﬁces to show, for arbitrarily large n, that
Gal(Kn/K) is not contained in A2n when viewed as a subgroup of S2n via its action on the roots of
φn(x)−α. Suppose on the contrary that Gal(Kn/K)⊆ A2n for all sufﬁciently large n. By a well-known
exercise in elementary Galois theory, this means that disc(φn(x)−α) is a square in K for all sufﬁciently
large n. Letting ψ(x)=φ(x+α)−α, using Lemma 5 we have
disc(φn(x)−α)= disc(φn(x+α)−α)= disc(ψn(x))= R2
n Aψn(c)
for all n≥ 2, where A, Rn∈ K are nonzero and where c is the critical point of ψ(x). In particular,
Aψn(c) is a square in K for all sufﬁciently large n.
The pair (ψ, 0) is stable by the stability assumption on the pair (φ,α) . In particular, the degree 8
polynomialψ3(x) has eight distinct roots in K , and thus C={ y2= Aψ3(x)} is a smooth hyperelliptic
curve of genus 3. There are inﬁnitely many n≥ 3 for which Aψn(c) is a square in K and hence for
whichψn−3(c) is the x-coordinate of a K -rational point on C. Moreover, these points are distinct by
the postcritically inﬁnite hypothesis on φ (and hence onψ as well). This violation of Faltings theorem
provides a contradiction, and thus the assumption Gal(Kn/K)⊆ A2n for all large enough n is false. As
explained above, by Lemma 4 this completes the proof that Gal(Kn/K) is cyclic for all n≥ 1.
We now apply the p= 2 case of Lemma 7, which implies that no primes p of K with odd residue
characteristic can ramify in K∞. However, this violates a theorem of Bridy et al. [2017], which states that
if K∞ is generated over K by the preimage tree associated to a postcritically inﬁnite rational map, then
inﬁnitely many primes of K ramify in K∞. The contradiction completes the proof of the theorem. □
The use of Falting’s theorem to limit the number of squares in the critical orbit of a polynomial is
borrowed from Boston and Jones [2009]. In fact, Theorem 8 may be viewed as a generalization of
Theorem 3.1 of [loc. cit .], in the sense that our result implies that the hypotheses of that theorem can
never be satisﬁed.
1988 Jesse Andrews and Clayton Petsche
