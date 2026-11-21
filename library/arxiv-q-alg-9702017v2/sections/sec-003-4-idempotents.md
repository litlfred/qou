---
doc_id: arxiv-q-alg-9702017v2
doc_title: "Idempotents of Hecke algebras of type A"
section_id: sec-003-4-idempotents
section_title: "Idempotents"
section_number: 4
pages: 9-14
source_pdf: 9702017v2.pdf
source_sha256: 282c911abb2a54e9
toc_source: outline
doc_brief: "Idempotents of Hecke algebras of type A — We use a skein-theoretic version of the Hecke algebras of type A to present three-dimensional diagrammatic views of Gyoja’s idempotent el- ements, based"
---
9
4
Idempotents
The Hecke algebra Hn is closely related to the group algebra of Sn, whose idem-
potents are described by the classical Young symmetrisers. For a Young diagram
λ its Young symmetriser is the product of the sum of permutations which pre-
serve the rows of T(λ) and the alternating sum of permutations which preserve
columns.
With care it is possible to make a similar construction of idempo-
tents in Hn, replacing permutations by suitably weighted positive permutation
braids. Jones [11] gives a good description of the two idempotents corresponding
to single row and column Young diagrams. Other authors, for example Wenzl
and Cherednik, have given descriptions for general λ, but we shall here adapt
the construction of Gyoja [8] to construct idempotents in Hn regarded as the
skein S(Rn
n). We shall follow the account in [13] for the basic row and column
idempotents, and use these to construct an idempotent for each Young diagram
λ.
We start from the visually appealing 3-dimensional picture for the idempotent
as a linear combination of braids in a 3-ball based very closely on the diagram λ
rather than as a linear combinations of diagram in a rectangle.
We consider a 3-ball B ∼= B3, with a chosen subset P of 2n points on its
boundary sphere, designated as n inputs PI and n outputs PO.
An oriented
tangle T in (B, P) is made up of n oriented arcs in B joining the points PI to
the points PO, together with any number of oriented closed curves. The arcs and
curves of T are assumed to carry a framing deﬁned by a speciﬁc choice of parallel
for each component.
The skein S(B, P) is deﬁned as linear combinations of such tangles, modulo
the framed Homﬂy skein relations applied to tangles which diﬀer only as in Fig. 2
inside some ball. The case when B = D2 × I and the points PI and PO are lined
up along the top and bottom respectively, gives a skein which can readily be
identiﬁed with S(Rn
n) = Hn. There is a homeomorphism mapping any other pair
(B′, P ′) to this pair, when |P ′| = 2n. This induces a linear isomorphism from
each S(B′, P ′) to the Hecke algebra Hn.
As in the case of diagrams, a wiring W of (B, P) into (B′, P ′) is an inclusion
of the ball B into the interior of B′ and a choice of framed oriented arcs in B −B′
ending with compatible orientation at the boundary points P ∪P ′. Given a tangle
T in (B, P) and a wiring W their union determines a tangle W(T) in (B′, P ′),
and induces a linear map S(W) : S(B, P) →S(B′, P ′).
The region between two balls is homeomorphic to S2 × I. A simple example
of wiring W consists of n arcs with each lying monotonically in the I coordinate,
sometimes called an n-braid in S2. In such a case the map S(W) is a linear
isomorphism whose inverse is induced by the inverse braid. Such a wiring can
always be chosen to determine an explicit isomorphism from any S(B, P) to
Hn = S(Rn
n) when |P| = 2n.
In terms of calculation the 3-dimensional viewpoint has advantages and dis-
Idempotents of the Hecke algebra.
10
a
a 4
a
1
2
1b
b1
b3
2b
Figure 8: The 3-dimensional quasi-idempotent associated to ν
advantages. There may not be a natural way to compose tangles in the skein
S(B, P), so the isomorphism with Hn does not immediately carry any algebra in-
formation. On the other hand a suitable choice of wiring may show when certain
elements are zero in the skein, and hence exhibit relations in Hn.
The following picture gives the heart of the construction of the idempotent
for the Young diagram λ. It lies in the skein of B3 ∼= D2 × I where the points
PI and PO are the centres of cells of templates in the shape of λ at the top and
bottom respectively. The strings in each rows are ﬁrst grouped together using
a linear combination aj of braids for a row with j cells. Below this the strings
in the columns are grouped with linear combinations bj of braids, to deﬁne an
element Eλ of the skein. The elements aj and bj are Jones’ basic row and column
quasi-idempotents, described shortly in more detail.
We give the 3-dimensional picture for Eν in Fig. 8. Note how the strings are
ﬁrst grouped in rows and then in columns. Although the braids run vertically the
boxes have been drawn in the horizontal plane to emphasize how the idempotent
is related to the shape of the Young diagram.
This 3-dimensional view will be discussed further in the next section, along
with some closely related choices of wiring. For the moment we will work with a 2-
dimensional picture given by using the standard tableau T(λ) to produce a wiring
which straightens out the strings to lie in order on a line. The corresponding
ﬁgure, more immediately related to Gyoja’s idempotents, is shown in Fig. 10.
We ﬁrst deﬁne the row and column elements aj and bj, following the account
in Morton [13].
Write En(σ1, σ2, · · ·, σn−1) =
X
π∈Sn
ωπ for the sum of the positive permutation
braids.
Theorem 4.1 ([13]) For each i, we can factorise En in Hn as
En = (σi + 1)E(i)
n ,
En = E′(i)
n (σi + 1),
Idempotents of the Hecke algebra.
11
where E(i)
n =
X
π(i)<π(i+1)
ωπ and E′(i)
n =
X
π(i)<π(i+1)
ωπ−1 .
Proof.
The proof follows the argument in [13], adapted for the fact that
our convention for labelling permutations is the opposite of that in [13].
Given i, we can pair the permutations as follows. For each permutation π
consider its composite π′ = π ◦(i i+1) with the transposition (i i+1). Exactly
one of the pair preserves the order of i and i + 1. Suppose that it is π, so that
π(i) < π(i + 1) and π′(i) > π′(i + 1). Then the braid σiωπ is itself a positive
permutation braid. Since its permutation is π′ we have σiωπ = ωπ′. Then
En
=
X
π(i)<π(i+1)
ωπ
+
X
π′(i)>π′(i+1)
ωπ′
=
X
π(i)<π(i+1)
ωπ
+
X
π(i)<π(i+1)
σiωπ
=
(σi + 1)E(i)
n ,
with E(i)
n =
X
π(i)<π(i+1)
ωπ.
The second equation in the theorem follows from the ﬁrst by applying the
braid-reversing antiautomorphism Rev of Hn, deﬁned by
Rev(AB)
=
Rev(B)Rev(A)
Rev(σi)
=
σi.
Then Rev(ωπ) = ωπ−1, and so
En = Rev(En) = Rev(E(i)
n )(σi + 1) = E′(i)
n (σi + 1).
✷
The elementary braids σi satisfy the quadratic relation (σi −a)(σi −b) = 0 in Hn,
where a = −xs−1 and b = xs, with the variants −s−1, s or −1, q for the roots a
and b in the other versions of the Hecke algebra. Deﬁne an and bn by substituting
−a−1σi or −b−1σi respectively for σi in En. Thus
an =
X
π
(−a)−l(π)ωπ ,
bn =
X
π
(−b)−l(π)ωπ
where l(π) is the writhe of ωπ, known in algebraic terms as the length of the
permutation π.
Corollary 4.2 We can factorise an and bn in Hn as
an = (σi −a)a(i)
n = a′(i)
n (σi −a) ,
bn = (σi −b)b(i)
n = b′(i)
n (σi −b) .
Idempotents of the Hecke algebra.
12
Eν(a)
=
4
a
a2
.
Figure 9: The element Eν(a)
Proof.
Substitute −a−1σi or −b−1σi for σi in Theorem 4.1.
✷
In our diagrams the elements an and bn are drawn as rectangles.
Those
denoting bn are shaded to distinguish them from those carrying an. In the classical
case, with x = s = 1, an reduces to a sum of permutations and bn to an alternating
sum.
Applying Cor. 4.2 and the factorisation of the quadratic relation we obtain
the following result.
Lemma 4.3 ([13]) Let φa and φb be the linear homomorphisms from the Hecke
algebra, Hn, to the ring of scalars Λ deﬁned by φa(σi) = a and φb(σi) = b for
i = 1, . . . , n −1. Then for all h ∈Hn,
anh = han = φb(h)an and bnh = hbn = φa(h)bn .
In particular, we note the following consequence of Lemma 4.3. A copy of an
ai can be swallowed (from above or below) by an ak, if i ≤k, at the expense of
multiplying the resulting diagram by a scalar. This scalar is α(i) (see page 14),
which is non-zero. Thus an ak can also throw out extra copies of ai, multiplying
the resulting diagram by α−1
(i) . Further, there is no net eﬀect if we introduce and
then later remove an ai. This works equally well with b in place of a. We make
further use of this property, with variants, in the next section.
We now deﬁne the quasi-idempotent elements eλ ∈Hn for each Young diagram
λ = (λ1, λ2, . . . , λk). To each cell of λ we assign a braid string, ordered according
to T(λ). Deﬁne Eλ(a) ∈Hn as a linear combination of braids by placing aλi on
the strings corresponding to the ith row of λ for each i, and similarly Eλ(b) using
bλi. The element Eν(a) is depicted in Fig. 9.
Now deﬁne eλ = Eλ(a)ωπλEλ∨(b)ω−1
πλ ∈Hn.
The element eν is shown in
Fig. 10. This picture can be obtained from the 3-dimensional picture of Fig. 8 by
sliding the rows apart at the top of the diagram and sliding the columns apart
at the bottom, using the standard tableau T(ν) to determine how to order the
strings.
For each λ write H(λ) ⊂Hn for the subspace spanned by {ωρ, ρ ∈R(λ)}.
Then Eλ(a), Eλ(b) ∈H(λ) and Eλ(a)h = hEλ(a) = φb(h)Eλ(a) for h ∈H(λ); a
similar result holds with a and b interchanged.
Idempotents of the Hecke algebra.
13
a4
3
2
b
b
a2
Figure 10: The quasi-idempotent eν
Lemma 4.4 Let λ and µ be Young diagrams with n cells, and let π ∈Sn be a
permutation which does not separate λ from µ. Then
Eλ(a)ωπEµ(b) = 0 = Eλ(b)ωπEµ(a).
Proof.
Since π does not separate λ from µ, there are two cells in some
row of λ, the lth say, which are sent to two cells in the same row of µ, the pth
say, by π. We can ﬁnd ρ ∈R(λ) and σ ∈R(µ) such that π′ = ρπσ sends the
two adjacent cells i and i + 1 in the lth row of λ to cells j and j + 1 in the pth
row of µ. By Cor. 3.5 we can write ωπ = ωρ′ωρ′′ωπ′ωσ′ωσ′′, with ρ′, ρ′′ ∈R(λ)
and σ′, σ′′ ∈R(µ). Hence ωπ = hωπ′h′, with h ∈H(λ) and h′ ∈H(µ). Then
Eλ(a)ωπEµ(b) = φb(h)φa(h′)Eλ(a)ωπ′Eµ(b).
We can thus replace π by π′, and assume that there are two adjacent cells,
i and i + 1, with π(i + 1) = π(i) + 1 = j + 1, where (i i + 1) ∈R(λ) and
(j j + 1) ∈R(µ). Since strings i and i + 1 ﬁnish at adjacent points, any other
string in ωπ either crosses above or below both strings. Then σi ωπ = ωπ σj, and
so (σi −a)ωπ = ωπ(σj −a). Knowing that (i i + 1) ∈R(λ) we can use Cor. 4.2
to write Eλ(a) = h(σi −a), and similarly Eµ(b) = (σj −b)h′. Then
Eλ(a)ωπEµ(b)
=
h(σi −a)ωπ(σj −b)h′
=
hωπ(σj −a)(σj −b)h′ = 0.
Interchange a and b to get the other equation.
✷
Corollary 4.5 If λ and µ are inseparable then
Eλ(a)HnEµ(b) = 0 = Eλ(b)HnEµ(a) .
Proof.
Hn is spanned by {ωπ; π ∈Sn}, and no π separates λ from µ.
✷
Lemma 4.6 Let λ have n cells.
Then Eλ(a)ωπEλ∨(b) is a scalar multiple of
Eλ(a)ωπλEλ∨(b) for each π ∈Sn.
Idempotents of the Hecke algebra.
14
Proof.
By Lemma 4.4, we need only consider the case when π separates
λ from λ∨.
In this case ωπ = ωρωπλωσ with ρ ∈R(λ), σ ∈R(λ∨). Then
Eλ(a)ωπEλ∨(b) = Eλ(a)ωρωπλωσEλ∨(b) = φa(ωρ)φb(ωσ)Eλ(a)ωπλEλ∨(b).
✷
Theorem 4.7 Let λ and µ be Young diagrams with n cells. Then
eλeµ
=
0
for λ̸ = µ,
e2
λ
=
αλeλ
for some scalar αλ.
Thus distinct Young diagrams determine orthogonal elements, while each eλ
is a quasi-idempotent element of Hn.
Proof.
By deﬁnition,
eλeµ = Eλ(a)ωπλEλ∨(b)ω−1
πλ Eµ(a)ωπµEµ∨(b)ω−1
πµ .
If λ̸ = µ then either λ∨and µ are inseparable, and so Eλ∨(b)

ω−1
πλ

Eµ(a) = 0, or
λ and µ∨are inseparable and then Eλ(a)

ωπλEλ∨(b)ω−1
πλ Eµ(a)ωπµ

Eµ∨(b) = 0.
Thus eλeµ = 0 when λ̸ = µ.
When λ = µ we can write
Eλ(a)

ωπλEλ∨(b)ω−1
πλ Eλ(a)ωπλ

Eλ∨(b) = αλEλ(a)ωπλEλ∨(b),
by Lemma 4.6. Then e2
λ = αλEλ(a)ωπλEλ∨(b)ω−1
πλ = αλeλ.
✷
The scalar αλ is calculated explicitly in [1] as
αλ =
Y
(i,j)∈λ
sj−i[λi + λ∨
j −i −j + 1] ,
where [k] = sk −s−k
s −s−1 denotes the ‘quantum integer k’.
Note that λi + λ∨
j −i −j + 1 is the hook length of the cell in the ith row and
jth column.
