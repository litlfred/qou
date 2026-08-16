---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-002-2-some-useful-lemmas
section_title: "Some useful lemmas"
section_number: 2
pages: 6-11
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
In this section we will gather a few useful lemmas we will need throughout the paper.
Recall that q is a prime power with q≡ 1(mod 4) and(q, 6)= 1. Let M denote the set of monic
polynomials over Fq[t] and H be the set of monic, square-free polynomials. Let Mn denote the set of
monic polynomials of degree n over Fq[t] and M≤n be the set of monic polynomials of degree less than
or equal to n. Let Hn denote the monic, square-free polynomials of degree n and recall that H∗
n denotes
the set of monic, square-free polynomials of degree n coprime to1. The norm of a polynomial f is
deﬁned by| f|= qdeg( f). Let φ denote the Euler totient function and τ the divisor function.
We deﬁne the zeta-function as
ζq(s)=
∑
f∈M
1
| f|s
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1859
forℜ(s)> 1. By counting monic polynomials of a given degree, one can easily show that
ζq(s)= 1
1− q1−s,
and this provides a meromorphic continuation of ζq with a simple pole at s= 1. As before, we will make
the change of variables u= q−s and so the zeta-function becomes
Z(u)=ζq(s)=
∑
f∈M
udeg( f)= 1
1− qu,
with a simple pole at u= 1/q. Note that Z(u) can also be written as an Euler product
Z(u)=
∏
P
(1− udeg(P))−1,
where the product is over monic, irreducible polynomials in Fq[t].
The quadratic character over Fq[t] is deﬁned as follows. For P a monic, irreducible polynomial let
( f
P
)
=



1 if P ∤ f, f is a square modulo P,
−1 if P ∤ f, f is not a square modulo P,
0 if P| f.
We extend the deﬁnition of the quadratic residue symbol above to any monic D∈ Fq[t] by multiplicativity,
and deﬁne the quadratic character χD by
χD( f)=
( D
f
)
.
Since we assumed that q≡ 1(mod 4), note that the quadratic reciprocity law takes the following form: if
A and B are two monic coprime polynomials, then
( A
B
)
=
( B
A
)
.
Throughout the paper, we will often make use of the Perron formula over function ﬁelds. If the series∑
f∈M a( f)udeg( f) is absolutely convergent for|u|≤ r< 1 then
∑
f∈Mn
a( f)= 1
2πi
∮
|u|=r
(∑
f∈M
a( f)udeg( f)
) du
un+1,
and
∑
f∈M≤n
a( f)= 1
2πi
∮
|u|=r
(∑
f∈M
a( f)udeg( f)
) du
un+1(1− u).
1860 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Recall that the twisted elliptic curve L-function L(E⊗χD, u) is a polynomial of degree(n+2 deg(D)),
with n being deﬁned in (1-2). Thus we can write
L(E⊗χD, u)=
n+2 deg(D)∑
n=0
cnun,
where cn=∑
f∈Mnλ( f)χD( f).
Lemma 2.1. The coefﬁcients cn of L(E⊗χD, u) satisfy the following relation
cn=ϵqn−n/2−deg(D)cn+2 deg(D)−n,
withϵ as in (1-3). In particular, ifϵ=− 1 and n is even, then cn/2+deg(D)= 0.
Proof. From the functional equation (1-3) we have
n+2 deg(D)∑
n=0
cnun=ϵ
n+2 deg(D)∑
n=0
cnq n/2+deg(D)−nun+2 deg(D)−n.
By setting k:= n+ 2 deg(D)− n we get
n+2 deg(D)∑
n=0
cnun=ϵ
n+2 deg(D)∑
k=0
cn+2 deg(D)−kqk−n/2−deg(D)uk.
Comparing the coefﬁcients we obtain the lemma. □
For D∈ H∗
2g+1, we can obtain the following exact formulas for L
(
E⊗χD, 1
2
)
and L′(
E⊗χD, 1
2
)
.
These are the analogues of the approximate functional equations in the number ﬁeld setting.
Lemma 2.2. Let D∈ H∗
2g+1. Then
L
(
E⊗χD, 1
2
)
=
∑
f∈M≤[n/2]+deg(D)
λ( f)χD( f)√| f| +ϵ
∑
f∈M≤[(n−1)/2]+deg(D)
λ( f)χD( f)√| f| ,
withϵ as in (1-3).
Proof. We use Lemma 2.1 to get
L(E⊗χD, u)=
n+2 deg(D)∑
n=0
cnun
=
[n/2]+deg(D)∑
n=0
cnun+
n+2 deg(D)∑
n=[n/2]+deg(D)+1
cnun
=
[n/2]+deg(D)∑
n=0
cnun+ϵ
n+2 deg(D)∑
n=[n/2]+deg(D)+1
cn+2 deg(D)−nqn−n/2−deg(D)un.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1861
Changing the summation variable in the second sum leads to
L(E⊗χD, u)=
[n/2]+deg(D)∑
n=0
cnun+ϵ
[(n−1)/2]+deg(D)∑
n=0
cn(qu 2)n/2+deg(D)−nun.
Taking u= q−1/2 and recalling that cn=∑
f∈Mnλ( f)χD( f) concludes the proof. □
Lemma 2.3. Let D∈ H∗
2g+1. Ifϵ=− 1, then
L′(
E⊗χD, 1
2
)
= 2(log q)
∑
f∈M≤[n/2]+deg(D)
(
[n/2]+ deg(D)− deg( f)
)
λ( f)χD( f)√| f| .
Proof. The above formula follows simply by differentiating the last equation in the proof of Lemma 2.2.
Just note that as remarked in Lemma 2.1, if ϵ=− 1 and n is even, then cn/2+deg(D)= 0. □
We also have the following lemma which expresses a character sum over square-free polynomials in
terms of sums over monics.
Lemma 2.4. We have
∑
D∈H∗
2g+1
χD( f)=
∑
C1|1
µ(C1)χC1( f)
∑
C2|(1f)∞
∑
R∈M2g+1−deg(C1)−2 deg(C2)
χR( f)
− q
∑
C1|1
µ(C1)χC1( f)
∑
C2|(1f)∞
∑
R∈M2g−1−deg(C1)−2 deg(C2)
χR( f),
where by C2|(1f)∞ we mean that the prime factors of C2 divide1f .
Proof. Let
A(u)=
∑
D∈H
(D,1)=1
χD( f)udeg(D).
Then
A(u)=
∏
P ∤1f
(1+χP( f)udeg(P))
=
∏
P ∤1f
(1− u2 deg(P))(1−χP( f)udeg(P))−1
=(1− qu 2)L(u,χ f)
∏
P|1f
(1− u2 deg(P))−1 ∏
P|1
P ∤ f
(1−χP( f)udeg(P)).
Writing
∏
P|1f
(1− u2 deg(P))−1=
∑
C2|(1f)∞
u2 deg(C2),
∏
P|1
P ∤ f
(1−χP( f)udeg(P))=
∑
C1|1
µ(C1)χC1( f)udeg(C1),
and comparing the coefﬁcients of u2g+1, the conclusion follows. □
1862 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
As in [Hayes 1966] we deﬁne the exponential over function ﬁelds as follows. For a∈ Fq((1/t)) let
eq(a)= exp
( 2πi TrFq/Fp(a1)
p
)
,
where a1 is the coefﬁcient of 1/t in the Laurent expansion of a and q is a power of the prime p. We
deﬁne the generalized quadratic Gauss sum as
G(V, f)=
∑
u (mod f)
χ f(u)eq
(uV
f
)
,
whereχ f is the quadratic character deﬁned before. We gather here a few useful facts about G(V, f)
whose proofs can be found in [Florea 2017c].
Lemma 2.5. (1) If( f, h)= 1, then G(V, f h)= G(V, f)G(V, h).
(2) Write V= V1 Pα where P ∤V1. Then
G(V, P j)=



0 if j≤α and j odd ,
φ( P j) if j≤α and j even ,
−|P| j−1 if j=α+ 1 and j even ,
χP(V1)|P| j−1/2 if j=α+ 1 and j odd ,
0 if j≥ 2+α.
The following Poisson summation formula in function ﬁelds holds.
Lemma 2.6. Let f ∈ Mn. If n is even, then
∑
R∈Mm
χR( f)= qm
| f|
(
G(0, f)+(q− 1)
∑
V∈M≤n−m−2
G(V, f)−
∑
V∈Mn−m−1
G(V, f)
)
,
otherwise
∑
R∈Mm
χR( f)= qmτ(q)
| f|
∑
V∈Mn−m−1
G(V, f),
where
τ(q)=
q−1∑
c=1
χ f(c) exp
(2πi TrFq/Fp(c)
p
)
is the usual Gauss sum over Fq.
2A. Outline of the proof. We will use the approximate functional equations for the L-functions involved
in the moment computations and then truncate the Dirichlet series close to the endpoint. For the longer
Dirichlet series, we will use Poisson summation and standard techniques to compute the main terms. For
the tails, we will go back and write the Dirichlet series in terms of expressions involving moments and
then use upper bounds for moments. The key in bounding the tails is the fact that the moments behave
differently depending on the points where we evaluate them (the power of g gets smaller in different
ranges).
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1863
