---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-027-47-a-note-on-modularity
section_title: "A note on modularity"
section_number: 4.7
pages: 57-58
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
associated to torsion classes in K3. We will consider two simple examples: one coming from
a quadratic Gauss sum (and hence related to the asymptotics of Jacobi θ-series) and the
other related to the Roger-Ramanujan functions, which are well known to be modular.
Example 4.4 (A quadratic Gauss sum) . Consider
Fm(x) = 1
m
 X
k∈Z/mZ
ζk2
m
 X
k∈Z/mZ
ζ−k2
m

= 1
2(1 +ζm
4 )(1 +ζ−m
4 )
=



1 if m≡ 1 (mod 4) ,
0 if m≡ 2 (mod 4) ,
1 if m≡ 3 (mod 4) ,
2 if m≡ 4 (mod 4) .
(289)
We see that this gives an almost trivial element of the Habiro ring HZ[1/2]. We can also
consider
Gm(x) = ζ4
m
 X
k∈Z/mZ
ζk2
m
2
= 1
2(1 +ζm
4 )2 =



i if m≡ 1 (mod 4) ,
0 if m≡ 2 (mod 4) ,
−i if m≡ 3 (mod 4) ,
2 if m≡ 4 (mod 4) ,
(290)
giving a slightly less trivial element of HZ[i,1/2].
Example 4.5 (Rogers-Ramanujan symmetrised). The Rogers-Ramanujan function has an
associated field Q(
√
5), which has an abelian Galois group over Q. Consider
J(z,q ) =
∞X
k=0
qk(k+1)z2k
(qz;q)k
∈ HQ(z). (291)
58 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
This J has the special property that
J(z,ζm(1−u)) ∈ Z[z, (1−zm−z2m)−1][ζm]JuK. (292)
We define for ξ2 +ξ− 1 = 0
Fm(u) =
X
θm=ξ
Res
z=θ
J(z,ζm(1−u))dz
z . (293)
EachFm(u) in Q(
√
5,ζm) is constant, the first five values being:
F1(u) = −1
2−
√
5
10 , F 2(u) = −1
2 +
√
5
10 ,
F3(u) = −1
2 +
√
5
10 , F 4(u) = −1
2−
√
5
10 ,
F5(u) =
√
5
5 ζ3
5 +
√
5
5 ζ2
5− 1
2 +
√
5
10 .
(294)
Note that, depending on the embeddings, F5(u) is equal to either 0 or −1 in C. In fact,
using the modularity of the Rogers-Ramanujan functions, one can show that
−5F 2
m(u)− 5Fm(u) =

1 if ( m, 5) = 1 ,
0 otherwise , (295)
the expressions on either side being the value at ζm(1−u) of an element of HZ[1/5]. More
generally,HZ[1/5] contains an element χN sending ζm to δv5(m),N. These elements can be
constructed using the operation f(q)7→ f(q5) — which does act on the usual Habiro ring
of Z. Note that the operation f(q)7→f(qk) is in general only defined on the Habiro ring of
a ring R if it contains 1/k. For example for k = 2 we see that f((1−u)2) =f((−(1−u))2)
and hence the re-expansion will not require a Frobenius φ2, which it should.)
This example illustrates how the different roots of unity can be disconnected by denomi-
nators. This viewpoint will be pushed further in the next section; where it will be used to
give an alternative approach to the Habiro ring of a number field.
