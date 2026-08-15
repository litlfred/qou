---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-006-16-admissible-series-and-formal-gaussian-integra
section_title: "Admissible series and formal Gaussian integration"
section_number: 1.6
pages: 11-13
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
that the modularity of certainq-hypergeometric functions is intimately related to the vanish-
ing of certain associated classes in algebraicK-theory, as was indeed later seen in a variety of
works [37, 50, 23, 10]. The asymptotics of these q-hypergeometric functions as q appraoches
roots of unity can be defined using formal Gaussian integration [50, 13, 14]. Modularity
would then imply some triviality of these asymptotic series. We will see that this link goes
even deeper, and that the integrality of the formal series (as series in q−ζ) is also linked to
the vanishing of the same classes in algebraic K-theory.
As we will see, there are two sources of these collections of power series at roots of unity,
with complementary properties. One of these is the “admissible series” of Kontsevich–
Soibelman [36, Sec.6], which arise as generating series of cohomological Hall algebras that
appear in enumerative algebraic geometry such as Donaldson–Thomas theory.
Definition 1.7. ForN ∈ Z>0 and t = (t1,...,t N), an admissible series is a power series
F (t,q )∈ Q(q)[ [t] ] satisfyingF (t,q ) = 1 + O(t) and
logF (t,q ) = −
X
0̸=n∈(Z≥0)N
X
ℓ≥1
Ln(qℓ)
ℓ (1−qℓ)tℓn1
1 ··· tℓnN
N , where Ln(q) ∈ Z[q±1]. (27)
12 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
An equivalent way to describe admissible series is via their factorisation into Pochhammer
symbols. In particular, a series F (t,q ) is admissible if and only if the unique integers cn,i
(generalised Donaldson–Thomas invariants), defined by the equality
F (t,q ) =
Y
0̸=n∈(Z≥0)N
Y
i∈Z
(qitn1
1 ··· tnN
N ;q)cn,i
∞ , (28)
vanish for all but finitely manyi for each fixedn. Here, as usual (x;q)n =Qn−1
j=0 (1−qjx) and
(x;q)−1
∞ =P∞
k=0xk/(q;q)k. The equivalence follows from the elementary but key identity (46)
for the infinite Pochhammer symbol, which implies the relation
Ln(q) =
X
i∈Z
cn,iqi ∈ Z[q±1] (29)
between the exponents cn,i and the Laurent polynomials Ln(q).
An admissible series F (t,q ) can be expanded at each root of unity and defines a collection
of series in t1/m = (t1/m
1 ,...,t 1/m
N ) given by
fm(t,x ) = F (t1/m,ζm +x). (30)
The properties of these collections of series at roots of unity are explained in detail in
Section 2.2 below.
Certain admissible series are easy to construct, compute and analyse. A main theorem
of [36, Sec. 6.1, Thm. 9] (see also Efimov [16]) is that q-hypergeometric Nahm sums 4
FA(t,q ) =
X
n∈ZN
≥0
(−1)diag(A)·nq
1
2 (ntAn+diag(A)·n)
(q;q)n1... (q;q)nN
tn1
1 ...t nN
N (31)
defined from a symmetric, integralN×N matrixA, are always admissible series. These series
encode the Poincar´ e polynomials of representations of a quiver with symmetric potential and
arbitrary dimension vector.
An elementary proof of the admissibility ofFA(t,q ) that uses the system of linearq-difference
equations (33) is given in Section 2.3. The proof also leads to a notion of a level m admissi-
ble series defined in Section 2.4 (abbreviated by m-admissible series throughout this paper),
the prototypical example being given by exactly the same sums as in equation (31) with n
restricted to an m-congruence class k∈{ 0,...,m − 1}N
FA,m,k(t,q ) =
X
n∈k+mZN
≥0
(−1)diag(A)·(n−k)q
1
2 (ntAn−ktAk)+ 1
2 diag(A)·(n−k)
(qk1+1;q)n1−k1... (qkN+1;q)nN−kN
tn1−k1
1 ··· tnN−kN
N . (32)
On the other hand, we also have a collection of power series at roots of unity f FGI
A,m(t,x )
associated, by formal Gaussian integration, to an integer symmetric matrix A. These se-
ries were previously defined in [50, 13, 14] for the special case t = (1,..., 1) giving series
ΦA,m(h) = f FGI
A,m(1,x ), expressed there with respect to the variable h = log(1 +ζ−1
m x). This
definition mimics the perturbation expansions of complex Chern–Simons theory given in
4The original Nahm sums were given for positive definite A by the special case when t = (−1)diag(A)qb
for some b∈ ZN.
THE HABIRO RING OF A NUMBER FIELD 13
terms of state-integrals, and is discussed in detail in Section 2.5. Both collections fA,m(t,x )
and f FGI
A,m(t,x ) are in Q[ζm]( (x) )[ [t1/m] ], for every positive integerm.
Our two main results are that these two seemingly independent collections of power series
agree and that their values att = (1,..., 1) belong to explicit Habiro modules. In fact, these
series can be defined by the admissible series of Kontsevich–Soibelman and this gives a new
perspective to the arithmetic properties of DT-invariants and the enumerative properties of
the elements of the Habiro ring.
Remark 1.8. The primes p = 2 and 3 require special consideration. This is true for
the Bloch group itself, which has a uniform definition up to 2-torsion and agrees with the
algebraic third K group of a field away from some primes that always include 2 and 3.
There are further difficulties with the primes 2 and 3 due to the presence of a 1
24 whose
origin can be seen to come from the Dedekind η-function and the famous equation of Euler
Li2(1) = − 1
24(2πi)2. Therefore, throughout the paper we will only consider primes p > 3
and always assume that 2 , 3|∆ unless otherwise stated. However, a more refined approach
should be able to cover the remaining cases as well.
