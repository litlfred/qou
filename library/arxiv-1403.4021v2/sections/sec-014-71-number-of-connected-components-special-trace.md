---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-014-71-number-of-connected-components-special-trace
section_title: "Number of connected components, special trace and change of variables"
section_number: 7.1
pages: 42-44
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
is a braid onn strands, then its closureL is an oriented link. As before, we denote 𝓁 :Bn→ Z
the abelianization morphism which maps σi to 1. We will use the following classical fact :
Lemma 7.1. If β∈Bn and L is the closure of β, then n +𝓁(β)≡ (#L) mod 2 , where #L
denote the number of components of the link L.
Proof. Decomposing the projection β∈ Sn of β under Bn→ Sn into a product of disjoint
cycles, we getr cycles of even lengths 2a1,..., 2ar ands cycles of odd lengthsb1,...,b s. Then
#L =r +s, n = 2∑ai +∑bi≡s mod 2 and 𝓁(β)≡r mod 2. This proves the claim.
□
This provides a simple interpretation of the tracet††
n , with values inS††. Recall that a2 = 1
inside S††.
Proposition 7.2. If β∈Bn and L is the closure of β, then t††
n (β) =a#L.
Proof. By construction, we have t††
n (β) = ana𝓁(β) = an+𝓁(β). Since a2 = 1 the conclusion
follows from lemma 7.1. □
MARKOV TRACES ON THE BMW-ALGEBRAS 43
There is a well-known connection between ‘two versions’ of the Kauﬀman polynomial,
one being connected to the other through a sign depending on the number of connected
components of the link. In our formalism this is seen as follows, using the automorphism E
of BMW n⊗RS = BMW +
n ⊕BMW−
n . First recall that the values of t+
n and t−
n on braids
belong to a submodule S0 = Q [a±1,x±1] of S+ and S−, respectively. Also recall that S0 can
be considered as a submodule of Q (α,q ) undera↦→α−2,x↦→α−1(q±q−1). We let τ±
n denote
the Markov traces t±
n viewed as functions with values in the same ring S0.
We can now show how this well-known connection between the two versions ﬁts into our
setting. This connection can be stated as follows (see e.g. [13], p. 177).
Proposition 7.3. If β is a braid on n strands whose closure is the link L, then
τ−
n (β)
⏐⏐a↦→−a
x↦→−x
= (−1)#L−1τ +
n (β)
where we identiﬁed β with its image in BMW +
n on the LHS, and its image in BMW−
n in the
RHS, and #L denotes the number of components of L.
Proof. The LHS can be viewed insideS+ asη◦t−
n◦E(E(β)), which is equal to (−1)n−1t+
n (E(β))
by corollary 5.4. Now (−1)n−1t+
n (E(β)) = (−1)n−1(−1)𝓁(β)t+
n (β) where𝓁 :Bn→ Z denotes as
before the abelianization morphism. The conclusion then follows from the identity n+𝓁(β)≡
(#L) mod 2, proved in lemma 7.1. □
7.2. The special case a =±1, b =∓j, c =∓j2. Recall thatj denotes a primitive 3-root of
1. We have y = 1,x =a. In this case, the link invariant aﬀorded by the Kauﬀman trace t+
n is
constant equal to 1 (that is, it takes the value 1 on every link), see [13] p. 186, table 16.3 row
A, and this is reproved by the observation that, in this case,δK =a hencetK
n =t††
n . For y = 1
andx =a =−1, according to [13] p. 186, table 16.3 row D, the link invariant associated totH
n
maps a linkL to (i
√
2)d2(T (L)), whereT (L) is the 3-fold cyclic cover ofS3 branched overL, and
d2(T (L)) = dimF 2H1(T (L), F 2). When y = 1,x =a = 1, we consider the automorphismϕ of
the group algebra of the braid group deﬁned bysi↦→s−1
i , and show that, as in the proposition
7.3 and corollary 5.4, the formula Tn(b) = (−1)n−1tn(ϕ(b)) induces a bijection between the
traces factorizing through the two Hecke algebras with quadratic conditions s2 +s + 1 = 0
and s2−s + 1 = 0, hence the two invariants are related by multiplication by ( −1)#L−1. As
a consequence we get the general formula tH
n (β) =a#ˆβ−1(i
√
2)d2(T (L)).
We are looking for a Markov trace t0
n on ~BMW n⊗RR/(a =±1,b =∓j,c =∓j2) such
that t0
3(1) =t0
3(s1) = 0 and t0
3(s1s2) = 1. This implies t0
3(sα
1sβ
2) = 1 for all α,β ∈{− 1, 1}.
We checked by computer that there is a (necessarily unique) extension oft0
3 toF4 satisfying
the Markov property. If there is an obstruction to these traces to genuine Markov traces one
thus needs to look for it on at least 5 strands.
Conjecture 7.4. The trace t0
3 can be extended to a Markov trace on the tower (Fn).
Assuming that conjecture, we get that the corresponding link invariant would take the
valuean× (4.2n− 4− 2n) on the (n + 3)-components unlink.
7.3. The special case a =b =c =±1. We havey = 1, x = 2a =±2. In this case, δH =a,
hencetH
n coincides with t††
n (see also [13] table 6.3, row A), and, for a =y = 1, the Kauﬀman
invariant maps a link L to (detL)2, where detL = ∆L(−1) =∇L(0) (see [13] table 6.3, row
B). Since this invariant is aﬀorded by t+
n , and because of proposition 7.3, this implies that
tK
n (β) =a#ˆβ−1(det ˆβ)2 for every braid β∈Bn.
44 Ivan Marin & Emmanuel Wagner
We are looking for a Markov trace t0
n on ~BMW n⊗R R/(a = b = c =±1) such that
t0
3(1) = 1,t0
3(s1) =t0
3(s1s2) = 0. This implies t0
3(sα
1sβ
2) = 0 for all α,β ∈{− 1, 1}. By theorem
6.26 we know that such a Markov trace exists, factoring through Fn. Moreover, by induction
we easily get thatt0
n+3(1) =an× (n + 1), and therefore the corresponding link invariant takes
the value an× (n + 1) on the (n + 3)-components unlink. Finally, we can easily identify its
restriction to the subalgebra ~TLn(0), as follows.
Proposition 7.5. There exists a family of traces tn : ~TLn(0)→ A0 satisfying tn(C) = an,
t1(1) = 0 , tn(1) = (n− 2)an+1 if n≥ 2, that would coincide with the restriction of t0
n to
~TLn(0) if (t0
n) is well-deﬁned.
Proof. Letting un =−an,v1 = 0, vn = (n− 2)an+1 in proposition 6.17 provides a family of
traces tn. We know prove that tn necessarily coincides with the restriction of the putative
Markov trace t0
n. We have tn(1) = t0
n(1) for n≤ 3 and, by proposition 6.3 (iii), t0
n+3(1) =
2at0
n+2(1)−t0
n+1(1) since, we know that t0
n factors through (Fn) by theorem 6.8. Because of
this, we have t0
n(1) =tn(1) for all n. By proposition 6.3 we also get tn(C) =t0
n(C) for all n.
From the relation ei = (si +s−1
i )/2−a and the Markov property we get t0
n(ei) = tn(ei) for
all i. It is well-known that the Temperley-Lieb algebra admits a basis made of words in the
ei which has the property that the ei of maximal index appears exactly once. Let us consider
such a basis element of ~TLn of the formAeiB withA,B words in theej forj <i. Expanding
ei as before, we get from the Markov property that t0
n+1(AeiB) =t0
n(AB)−at0
n+1(AB). By
induction on the length of the words in theei’s, we get from this formula thatt0
n+1(AeiB) = 0
as soon as A or B has length≥ 1, and therefore t0
n coincides on tn on every basis element of
~TLn(0), which proves the claim.
□
