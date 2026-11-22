---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-013-invariance-under-change-of-ordering
section_title: "Invariance under change of ordering"
section_number: null
pages: 67-81
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
implies Diagram 4.6 commutes.
Theorem 4.1.4 Given a coloring F = (g, f), we have
Tr(
O
σ∈T 4
Zϵ(σ)
F
(σ)) = Tr(
O
σ∈T 4
Zϵ(σ)
F
(σ)′).
As a consequence, the partition function ZD(M; T ) is independent on the choice of rep-
resentatives for each triangle color.
Proof:
It suﬃces to prove Diagram 4.10 commutes, which follows from Proposition
4.1.3 since each V +
F (τ) is acted on by exactly one Zϵ(σ)
F
(σ).
N
τ∈T 3 V +
F (τ)
L
τ∈T 3 V +
F (τ)
N
τ∈T 3 V +
F (τ)′
N
τ∈T 3 V +
F (τ)′
N
σ∈T 4
Zϵ(σ)
F
(σ)
N
τ∈T 3
T
N
τ∈T 3
T
N
σ∈T 4
Zϵ(σ)
F
(σ)′
(4.10)
4.2
Invariance under change of ordering
When deﬁning the partition function, we require that the triangulation be equipped
with an ordering on its vertices. In this section, we show that the partition function is
actually independent of the ordering, and we will use Equation 3.2 as the deﬁnition of
the partition function.
Let Sn be the permutation group on the set {0, 1, · · · , n −1} with the standard
generators si ∈Sn, i = 0, 1, · · · , n −2 swapping i and i + 1. Let Fn be the free group on
n generators ˜s0, · · · , ˜sn−1, and denote by pn : Fn−1 −→Sn the quotient map sending ˜si
58
Section 4.2
Invariance under change of ordering
to si. If ˜s and ˜s′ are any two elements in Fn−1 such that pn(˜s) = pn(˜s′) = s ∈Sn, then
we say ˜s and ˜s′ represent the same permutation s and ˜s is a representative of s.
For each s ∈Sn and any non-empty subset T ⊂{0, 1, · · · , n −1}, if we order the
elements in T and in s(T), respectively, by 0, 1, · · · , |T| −1 according to their relative
order, then we get a permutation sT, called the restriction of s on T, on {0, 1, · · · , |T|−1},
namely, sT(i) = j if s maps the i-th greatest element in T to the j-th greatest element
in s(T). When no confusion arises, we simply write sT as s. For example, if s = s0 ∈S3,
then s{0,1} = s0 ∈S2, s{0,2} = Id ∈S2. It is clear that sT is a group morphism in the
sense that s′
s(T)sT = (s′s)T.
The rough idea of proof of invariance under reordering goes as follows. Let T be a
ﬁxed ordered triangulation with vertices ordered by 0, 1, · · · , N −1, where N = |T 0|. Let
T ′ be any ordered triangulation obtained from T by reordering its vertices. Apparently,
each reordering of vertices corresponds to an element of SN. To make it clear, if s ∈SN,
then we obtain T ′ from T by replacing the label i of a vertex by s(i). See Figure 4.1
for the reordering of a 2-simplex. That is, we are thinking that the ‘physical’
unordered triangulation is ﬁxed all the time; only the labels on vertices are
permuting. For a k-simplex σ = (a0a1 · · · ak−1) ∈T k, denote by σs the corresponding
k-simplex (σ(a0)σ(a1) · · · σ(ak−1)) ∈(T ′)k.
Note that σ and σs are the same as an
unordered simplex. Given a coloring F = (g, f) on T , we wish to deﬁne a corresponding
coloring F ′ = (g′, f ′) on T ′ so that,
1. for each 2-simplex β ∈T 2, dβ = dβs ;
2. for each 4-simplex σ, there exists an isomorphism Φs
σ : VF(∂σ) −→VF ′(∂σs) such
that ˜ZF(σ) = ˜ZF ′(σs) ◦Φs
σ;
3. Φ := N
σ∈T 4 Φs
σ : VF(T ) −→VF ′(T ′) maps φF to φF ′ .
59
Section 4.2
Invariance under change of ordering
0
1
2
−→
s(0)
s(1)
s(2)
Figure 4.1: Reordering by a permutation s
If the above conditions are satisﬁed, then it is clear that ZD(M; T ) = ZD(M; T ′). The
ﬁrst condition is satisﬁed trivially as will be seen later. The Φs
σ clearly depends on the
reordering restricted to the 4-simplex σ. It is natural to try to construct Φsi
σ for each
reordering si ∈S5 and assume Φss′
σ
= Φs
σs′Φs′
σ . Namely, we wish Φs
σ acts like a group
action. Unfortunately, this turns out to be false. For instance, Φsi
σsiΦsi
σ is not equal to
the identity; it is, however, equal to the identity up to certain canonical isomorphisms.
Thus in the following, we will actually ﬁrst deﬁne an action Φ˜s
σ for ˜s ∈F4 and show that
that if ˜s and ˜s′ represent the same permutation in S5, then there is a canonical way to
identity them. To deﬁne the action Φ˜s
σ, we will need to consider in turn actions of Fi on
colors of i-simplices for i = 1, 2, 3, 4.
First we ﬁx some notations. In general letters s, s′ are used to represent elements
of Sn, and ˜s, ˜s′ elements of Fn−1. We will still think of the generators ˜si of Fn−1 as
swapping i with i+1, although this is actually the role of pn(˜si). By a colored k-simplex,
k = 1, 2, 3, 4, we mean an ordered k-simplex with a coloring on its sub 1-simplices and sub
2-simplices (if any). Let Sk be the set of all colored k-simplices, where two k-simplices
are identiﬁed up to relative ordering of their vertices. For instance,
S1 = {
0
1
a
: a ∈G}
S2 = {
0
1
2
a
b
c
A
: a, b, c ∈G, A is simple in C¯cab}
.
For k = 2, 3, 4, associated to each colored k-simplex σ is an array σ[0], · · · , σ[k],
60
Section 4.2
Invariance under change of ordering
where σ[i] is the colored (k −1)-simplex corresponding to the face ∂iσ. We combine the
indices if there are multiple of them, e.g., σ[i][j] = σ[i, j]. We use C(σ) to denote the
group element color on σ if k = 1, and the object color if k = 2. For k = 3, 4, a colored
k-simplex σ is uniquely determined by the arrays σ[i] ′s. For k = 1, 2, a colored k-simplex
σ is uniquely determined by the arrays σ[i] ′s and their colors.
In the following, we consider in order the eﬀect of the reordering of a k-simplex on
its colorings for k = 1, 2, 3, 4. This involves studying the action of Fk (resp. Sk+1) on Sk.
Firstly, deﬁne the action of F1 on S1 by
˜s0(
0
1
a
) =
1
0
¯a
.
This action factors through S2 since ˜s2
0 acts as the identity. Thus when the vertices of a
colored 1-simplex are reordered by s0, the color on the 1-simplex is changed to its inverse.
By abusing of notations, we also write s0(a) = ¯a, a ∈G.
Secondly, consider the action of F2 on S2. For each ˜s ∈F2, deﬁne
˜s(
0
1
2
a
b
c
A
) :=
˜s(0)
˜s(1)
˜s(2)
˜s(a)
˜s(b)
˜s(c)
˜s(A)
,
where ˜s(i) := p3(˜s)(i), i = 0, 1, 2, is the reordering, ˜s(a) is the action of p(˜s){0,1} on
0
1
a
, and ˜s(b), ˜s(c) are deﬁned analogously, and
˜s(A) =







A∗
˜s = ˜s0
(A∗)
b
˜s = ˜s1
Explicitly, the generators act as
61
Section 4.2
Invariance under change of ordering
˜s0(
0
1
2
a
b
c
A
) :=
1
0
2
¯a
b
c
A∗
,
˜s1(
0
1
2
a
b
c
A
) :=
0
2
1
a
¯b
c
(A∗)
b
,
or written in another way, ˜s0(b, c, a; A) = (c, b, ¯a; A∗), ˜s1(b, c, a; A) = (¯b, a, c; (A∗)
b
),
where we identify a colored 2-simplex σ with the quad (C(σ[0]), C(σ[1]), C(σ[2]); C[σ]).
It is easy to check that ˜si sends colored 2-simplices to colored 2-simplices.
The
action of F2 does not in general factor through S3 since, for instance, ˜s2
1(b, c, a; A) =
(b, c, a; (( A∗
b
)∗)
¯b
), but (( A∗
b
)∗)
¯b
is not always equal to A. However, since (( A∗
b
)∗)
¯b
is
canonically isomorphic to A, this does give us some hints on relating the action of ˜s and
˜s′ which represent the same permutation.
Let us recall some structures in D.
δA :A
∼
−→A∗∗
θA :A
∼
−→
A
g′
A ∈Cg′
φA,g : (A∗)
g
∼
−→( A
g )∗
∀g ∈G
Deﬁnition 4.2.1
1. If A, B are two objects of D, a morphism f ∈Hom(A, B) is
called a canonical isomorphism if it is a composition of morphisms which are tensor
products of δ, θ, φ, I and their inverses.
2. A linear map Φ : Hom(A, B) −→Hom(A′, B′) is called a canonical isomorphism if
Φ(ψ) = g◦ψ◦f for some canonical isomorphisms f ∈Hom(A′, A), g ∈Hom(B, B′).
Canonical isomorphisms will be denoted by can. It is clear that composition, tensor
62
Section 4.2
Invariance under change of ordering
products, inverse, dual, G-action of canonical isomorphisms are still canonical isomor-
phisms. And a canonical isomorphism from A to B is unique, if it exists.
It is straight forward to check the following equalities.
˜s2
0(b, c, a; A) = (b, c, a; A∗∗)
(4.11)
˜s2
1(b, c, a; A) = (b, c, a; (( A∗
b
)∗)
¯b
)
(4.12)
˜s0˜s1˜s0(b, c, a; A) = (¯a, ¯c,¯b; ( (A∗∗)
c
)∗)
(4.13)
˜s1˜s0˜s1(b, c, a; A) = (¯a, ¯c,¯b; (( A∗
b
)∗∗)
a
)
(4.14)
Lemma 4.2.2 Let ˜s, ˜s′ ∈F2 be such that p3(˜s) = p3(˜s′) = s ∈S3, then for any colored
2-simplex σ,
1. ˜s(σ)[s(i)] = sˆi(σ[i]) for i = 0, 1, 2, where sˆi is the restriction of s on the edge ˆi.
Namely, if ˜s is a reordering of σ, then the eﬀect of ˜s on any sub 1-simplex is equal
to the action of the restriction of s on that simplex.
2. There is a canonical isomorphism from C(˜s(σ)) to C(˜s′(σ)).
Proof:
It can be checked that if the ﬁrst part of the statement is true for ˜s and ˜s′′,
then it is true for their product ˜s˜s′′. Thus it suﬃces to verify it on the generators ˜s0 and
˜s1, which is straight forward.
To prove the second part, note that by the identities in Equations 4.11 −4.14, there
is a canonical isomorphism C(σ) −→C(˜s2
0(σ)), C(σ) −→C(˜s2
1(σ)), C(˜s0˜s1˜s0(σ)) −→
C(˜s1˜s0˜s1(σ)). The general case follows from the naturality of these isomorphisms.
Lemma 4.2.2 can be applied to the following situation. Assume σ′ and σ′′ are two
colored 2-simplices in T with a common colored 1-simplex α. Let s ∈S4 be an reordering
of σ ∪σ′, and ˜s′, ˜s′′ be a representative of sσ′, sσ′′, respectively. Then the eﬀect of ˜s′ and
˜s′′ on α coincides, both equal to the action of sα.
63
Section 4.2
Invariance under change of ordering
Also by Lemma 4.2.2, if ˜s and ˜s′ represent the same element in S3 and σ is a colored
2-simplex, then the eﬀect of ˜s and ˜s′ on C(σ) is related by a canonical isomorphism,
namely, there is a canonical isomorphism can from C(˜s(σ)) to C(˜s′(σ)).
Thirdly, we consider the reordering of 3-simplices.
Again for the same reason as
before, we will need to study the action of F3 on colored 3-simplices. If s ∈S4 is a
reordering of a colored 3-simplex σ and ˜s is a representative of s, it is natural to require
the eﬀect of ˜s on a sub 2-simplex α to be the action of a representative of sα. There is no
canonical choice of representatives. We start with generators ˜si and choose the shortest
word as the representative of (si)α. Explicitly, ˜si(σ) is deﬁned as in Equation 4.15, where
the ˜si ′s on the right hand side are considered as elements of F2 and we identify σ with
the quad (σ[0], σ[1], σ[2], σ[3]).
˜si(σ) = ˜si(σ[0], σ[1], σ[2], σ[3]) =















(σ[1], σ[0], ˜s0(σ[2]), ˜s0(σ[3]))
i = 0
(˜s0(σ[0]), σ[2], σ[1], ˜s1(σ[3]))
i = 1
(˜s1(σ[0]), ˜s1(σ[1]), σ[3], σ[2])
i = 2
(4.15)
The following lemma shows the action deﬁned indeed satisﬁes the natural requirement
mentioned above.
Lemma 4.2.3 Let ˜s ∈F3, s ∈S4 be such that p4(˜s) = s, and let σ be any colored
3-simplex, then
˜s(σ)[s(i)] = Ls(i)
˜s
(σ[i]), i = 0, 1, 2, 3,
(4.16)
where Li
(−) : F3 −→F2 is a map such that p3(Ls(i)
˜s
) = sˆi. In particular, if p4(˜s) = p4(˜s′),
then p3(Li
˜s) = p3(Li
˜s′).
Proof:
Again the statement holds for the generators, and it holds for the product
of two elements if it does for each of them.
64
Section 4.2
Invariance under change of ordering
Lemma 4.2.3 has the following consequence. Assume a 2-simplex β is the intersection
of two 3-simplices σ′ and σ′′, β = σ′[i] = σ′′[j], and s ∈S5 is a reordering of σ′ ∪σ′′.
Restricting to each 3-simplex, we get an reordering s′ on σ′ and s′′ on σ′′.
Choose
an arbitrary representative ˜s′ and ˜s′′ for s′ and s′′, respectively. Then Ls′(i)
˜s′
and Ls′′(j)
˜s′′
represent the same permutation, namely, sβ, and thus there is a canonical isomorphism
from ˜s′(σ′)[s′(i)] to ˜s′′(σ′′)[s′′(j)].
Recall that for a colored 3-simplex σ, there are associated Hilbert spaces V ±(σ), where
we have dropped the subscript symbol F since σ is assumed to be colored. Speciﬁcally,
V +(σ) = Hom(C(σ[1]) ⊗
C(σ[3])
C(σ[0,0])
, C(σ[2]) ⊗C(σ[0]))
V −(σ) = Hom(C(σ[2]) ⊗C(σ[0]), C(σ[1]) ⊗
C(σ[3])
C(σ[0,0])
)
If σ′ and σ are two colored 3-simplices which diﬀer by a reordering, we show below that
their associated Hilbert spaces are related by canonical isomorphisms.
For each ˜si ∈F3, we will deﬁne V (˜si) as a linear isomorphism from V ±(σ) from
V ∓(si(σ)), and extend the action to V (˜s) for any ˜s ∈F3. Assume σ = (0123) and denote
the colors of sub 1- and 2- simplices of σ by the simplices themselves, e.g., 12, 23, 123,
etc. Then by Equation 4.15, one can write out ˜s(σ) explicitly. For instance, σ[3] =
(12, 02, 01; 012), ˜s0(σ)[3] = ˜s0(σ[3]) = (02, 12, 01; 012∗). It is direct to check that
V −(˜s0(σ)) = Hom(013∗⊗023, 123 ⊗
012∗
23
).
Similarly, once can ﬁnd the expression for V ±(˜si(σ)). Then the action V (˜si) is deﬁned
in Figure 4.2, 4.3 and 4.4.
If p4(˜s) = p4(˜s′) = s and σ is a colored 3-simplex, then by Lemma 4.2.2 and Lemma
4.2.3, there is a canonical isomorphism canfrom C(˜s(σ)[i]) to C(˜s′(σ)[i]). If g ∈G, then
65
Section 4.2
Invariance under change of ordering
023
012
23
013
123
7−→
013
012
23
023
123
V +(σ) = Hom(023 ⊗
012
23
, 013 ⊗123)
V (˜s0)
−→
V −(˜s0(σ)) = Hom(013∗⊗023, 123 ⊗
012∗
23
)
013
123
023
012
23
7−→
013
012
23
023
123
V −(σ) = Hom(013 ⊗123, 023 ⊗
012
23
)
V (˜s0)
−→
V +(˜s0(σ)) = Hom(123 ⊗
012∗
23
, 013∗⊗023)
Figure 4.2: Deﬁnition of V (˜s0)
023
012
23
013
123
7−→
023
012
13·12
013
123
V +(σ) = Hom(023 ⊗
012
23
, 013 ⊗123)
V (˜s1)
−→
V −(˜s1(σ)) = Hom(023 ⊗123∗, 013 ⊗
012∗
13·12
)
023
012
23
013
123
7−→
013
012
13·12
023
123
V −(σ) = Hom(013 ⊗123, 023 ⊗
012
23
)
V (˜s1)
−→
V +(˜s1(σ)) = Hom(013 ⊗
012∗
13·12
, 023 ⊗123∗)
Figure 4.3: Deﬁnition of V (˜s1)
66
Section 4.2
Invariance under change of ordering
023
012
23
013
123
7−→
023
123
013
012
23
23
V +(σ) = Hom(023 ⊗
012
23
, 013 ⊗123)
V (˜s2)
−→
V −(˜s2(σ)) = Hom(012 ⊗
123∗
23
,
023∗
23
⊗
013
23
)
013
123
023
012
23
7−→
023
123
013
012
23
23
V −(σ) = Hom(013 ⊗123, 023 ⊗
012
23
)
V (˜s2)
−→
V +(˜s2(σ)) = Hom(
023∗
23
⊗
013
23
, 012 ⊗
123∗
23
)
Figure 4.4: Deﬁnition of V (˜s2)
the g-action on any canonical isomorphisms are still canonical isomorphisms. Thus by
composing and pre-composing canonical isomorphisms, we have an isomorphism can :
V ±(˜s(σ)) −→V ±(˜s′(σ)).
Lemma 4.2.4 For any colored 3-simplex σ, and ˜s, ˜s′ ∈F3 such that p4(˜s) = p4(˜s′) =
s ∈S4, the following diagram commutes:
V ±(σ)
V ±sgn(s)(˜s(σ))
V ±sgn(s)(˜s′(σ))
V (˜s)
V (˜s′)
can
(4.17)
where sgn(s) = ± is the sign the s and we use the convention that ++ = −−= +, +−=
−+ = −.
Proof:
It suﬃces to prove the statement for the pairs (˜s, ˜s′) = (˜s2
i , e), i = 0, 1, 2 and
(˜s0˜s1˜s0, ˜s1˜s0˜s1), (˜s1˜s2˜s1, ˜s2˜s1˜s2), (˜s0˜s2, ˜s2˜s0). These can be checked by direct pictorial
calculus.
67
Section 4.2
Invariance under change of ordering
Lemma 4.2.5 For any ˜s, ˜s′ ∈F3 such that p4(˜s) = p4(˜s′), σ a colored 3-simplex,
1. V (˜s)⊗V (˜s) : V +(σ)⊗V −(σ) −→V sgn(s)(˜s(σ))⊗V −sgn(s)(˜s(σ)) is pairing preserving.
2. can ⊗can : V +(˜s(σ)) ⊗V −(˜s(σ)) −→V +(˜s′(σ)) ⊗V −(˜s′(σ)) is pairing preserving.
Finally we consider the reordering of 4-simplices. For a colored 4-simplex σ, denote
by V ±(∂σ) the tensor product of the Hilbert spaces associated with its boundary:
V ±(∂σ) = V ±(σ[1]) ⊗V ±(σ[3]) ⊗V ∓(σ[0]) ⊗V ∓(σ[2]) ⊗V ∓(σ[4])
The generators of F4 act on S4 as follows:
˜si(σ) =























(σ[1], σ[0], ˜s0(σ[2]), ˜s0(σ[3]), ˜s0(σ[4]))
i = 0
(˜s0(σ[0]), σ[2], σ[1], ˜s1(σ[3]), ˜s1(σ[4]))
i = 1
(˜s1(σ[0]), ˜s1(σ[1]), σ[3], σ[2], ˜s2(σ[4]))
i = 2
(˜s2(σ[0]), ˜s2(σ[1]), ˜s2(σ[2]), σ[4], σ[3])
i = 3
(4.18)
We need to check that RHS of Equation 4.18 in each case is indeed a valid colored
4-simplex. If σ is a colored 4-simplex, then for 0 ≤i ≤4, 0 ≤j ≤3, we have
σ[i, j] =







σ[j, i −1]
i > j
σ[j + 1, i]
i ≤j
(4.19)
The following lemma asserts that the action of F4 preserves this property.
Lemma 4.2.6 If ˜s ∈F4, and σ is a colored 4-simplex, then ˜s(σ) satisﬁes Equation 4.19.
Proof:
Direct veriﬁcations on the generators.
Similar to Lemma 4.2.3, we have the following lemma.
68
Section 4.2
Invariance under change of ordering
Lemma 4.2.7 If p5(˜s) = s ∈S5 and σ ∈S4 is a colored 4-simplex, then
˜s(σ)[s(i)] = Hs(i)
˜s
(σ[i]), i = 0, 1, 2, 3, 4,
(4.20)
where Hi
(−) : F4 −→F3 is a map such that p4(Hs(i)
˜s
) = sˆi.
By Lemma 4.2.7,
V (Hs(i)
˜s
) : V ±(σ[i])
≃
−→V sgn(s)±(˜s(σ)[s(i)]),
Thus V (˜s) :=
4N
i=0
V (Hs(i)
˜s
) : V ±(∂σ)
≃
−→V sgn(s)±(∂˜s(σ)) is an isomorphism.
Lemma 4.2.8 For each colored 4-simplex σ ∈S4 and ˜s ∈F4 such that p5(˜s) = s ∈
S5, the following diagram commutes, where and for the rest of the section we drop the
subscript F for the ˜Z±
F .
V ±(∂σ)
V ±sgn(s)(∂˜s(σ))
C
V (˜s)
˜Z±(σ)
˜Z±sgn(s)(˜s(σ))
(4.21)
Proof:
It suﬃces to prove for the case ˜s = ˜si, which again is done by pictorial
calculus.
Now we are ready to prove the main theorem of the section on the independence of
the partition function on the ordering of vertices.
Theorem 4.2.9 Let T , T ′ be two ordered triangulations of M which diﬀer by a reorder-
ing s ∈SN, then for each coloring F = (g, f) of T , there is a corresponding coloring
F ′ = (g′, f ′) and an isomorphism Φ : VF(T ) −→VF ′(T ′), such that df(α) = df′(αs) for
69
Section 4.2
Invariance under change of ordering
any 2-simplex α ∈T 2, Φ(φF) = φF ′, and that the following diagram commutes.
VF(T )
VF ′(T ′)
C
Φ
N
σ∈T 4
Zϵ(σ)(σ)
N
σ∈(T ′)4
Zϵ(σ)(σ)
(4.22)
In particular, this implies that ZD(M; T ) = ZD(M; T ′).
Proof:
Fix a coloring F = (g, f) on T . For each simplex σ ∈T , denote by σ′ the
corresponding simplex σs in T ′.
For each colored 1-simplex α, identify α′ with sα(α). That is, color α′ with sα(gα).
For each colored 2-simplex β = (β[0], β[1], β[2]; C(β)), arbitrarily choose a represen-
tative ˜sβ for sβ, and identify β′ with ˜sβ(β), namely, transport the colors on ˜sβ(β) to β′
according to their relative ordering. Lemma 4.2.2 guarantees the coloring on common
edges of diﬀerent 2-simplices are consistent, which is equal to the coloring already given
above. Denote the resulting coloring on T ′ by F ′ = (g′, f ′). The map F 7→F ′ gives a
one-to-one correspondence between the set of colorings on T and the set of colorings on
T ′.
Since the dual functor and the G-action preserve the quantum dimension of objects,
it is clear from the deﬁnition of the F2−action on S2 that df(α) = df′(α′).
For each colored 4-simplex σ, arbitrarily choose a representative ˜sσ for sσ, and let
˜sσ(σ) = ˜σ. By Lemma 4.2.8, the following diagram commutes:
V ϵ(σ)(∂σ)
V ϵ(˜σ)(∂˜σ)
C
V (˜sσ)
˜Zϵ(σ)(σ)
˜Zϵ(˜σ)(˜σ)
(4.23)
Note that here we cannot identify ˜σ with σ′ directly since the color on a sub 2-simplex
of ˜σ may not be the same as that on the corresponding sub 2-simplex of σ′. However, it is
70
Section 4.2
Invariance under change of ordering
true that the colors are both determined by the action of some elements in F2 whose image
in S3 is the restriction of s on that 2-simplex. Thus there is a canonical isomorphism
connecting these two colors and hence there is a canonical isomorphism from V ±(˜σ[i]) to
V ±
F ′(σ′[i]). And the following diagram commutes:
V ϵ(σ)(∂σ)
V ϵ(˜σ)(∂˜σ)
V ϵ(σ′)
F ′
(∂σ′)
C
V (˜sσ)
˜Zϵ(σ)(σ)
˜Zϵ(˜σ)(˜σ)
can
˜Zϵ(σ′)(σ′)
(4.24)
Deﬁne Φ : VF(T ) −→VF ′(T ′) to be the tensor product over all 4-simplices of the
isomorphism on horizontal line in Diagram 4.24, i.e., Φ = N
σ∈T 4 can ◦V (˜sσ).
This implies the diagram in the theorem commutes.
Next we show Φ(φF) = φF ′.
Let τ be the common face of two 4-simplices σ1, σ2, and assume τ = σ1[i] = σ2[j].
Without loss of generality, assume V +
F (τ) appears as a component in the domain of
˜Zϵ(σ1)(σ1), and thus V −
F (τ) must be a component in the domain of ˜Zϵ(σ2)(σ2). Only for
the rest of the proof, let s1 = sσ1, s2 = sσ2, ˜s1 = ˜sσ1, ˜s2 = ˜sσ2, and let ˜σ1 = ˜sσ1(σ1) and
˜σ2 = ˜sσ2(σ2).
By Lemma 4.2.7, we have
˜σ1[s1(i)] = Hs1(i)
˜s1
(τ), ˜σ2[s2(j)] = Hs2(j)
˜s2
(τ),
and p4(Hs1(i)
˜s1
) = (s1)ˆi = sτ = p4(Hs2(j)
˜s2
).
Let H1 = Hs1(i)
˜s1
, H2 = Hs2(j)
˜s2
. Note that H1(τ), H2(τ) and τ ′ have the same underlying
3-simplex.
71
Section 4.3
