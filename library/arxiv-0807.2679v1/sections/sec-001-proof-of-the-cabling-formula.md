---
doc_id: arxiv-0807.2679v1
doc_title: "A cabling formula for the colored Jones polynomial Roland van der Veen"
section_id: sec-001-proof-of-the-cabling-formula
section_title: "Proof of the cabling formula"
section_number: null
pages: 4-12
source_pdf: 0807.2679v1.pdf
source_sha256: 69ef10f8e70fc6f6
doc_brief: "A cabling formula for the colored Jones polynomial Roland van der Veen — We prove an explicit cabling formula for the colored Jones po lynomial."
---
Let us ﬁx a banded link L with c components L1, . . . , L c. Choosing a component
Li of L and opening it up we can write L as the closure of a banded (1 , 1)-tangle
Ti. Deﬁne Ti;s to be the banded ( s, s )-tangle obtained from Ti by replacing the
opened component Li of Ti by s parallel bands. In terms of these tangles the
(i; r, s )-cabling of L is equal to the closure of the composition Ti;s ◦ Br
s , see also
ﬁgure 1.
Note that the link Lr
i;s has c + g − 1 components, where g = gcd(r, s ), since
the component Li of L is replaced by the g-component torus link that is the
closure of Br
s . If we number the strands of the braid Br
s starting at 0 then two
strands are in the same component of the closure if and only if their n umbers
are congruent modulo g. Therefore each component of the closed braid consists
of p = s/g strands. Let us suppose that our link Lr
i;s is colored by the integers
(M1, . . . , M i−1, N, . . . , M c), where the vector N = ( N0, . . . , N g−1) represents
the new colors used to color the components of the torus link that r eplaces the
component Li.
We denote the the N -dimensional irreducible representation of quantum sl2
by VN . Using the above coloring, the torus braid corresponds to a morph ism
from V = ⨂ s−1
k=0 VNk modg to itself. In terms of these morphisms we can now state
that the unnormalized ( M1, . . . , M i−1, N, . . . , M c)-colored Jones polynomial of
the ( i; r, s )-cabling of L (abbreviated by J) is the following quantum trace:
J = JM1,...,M i− 1, N,...,M c(Lr
i;s) = Trq(Br
s ◦ Ti;s, V ) (1)
The ﬁrst step in calculating this trace is to expand it using the isotypic al de-
composition of the tensor product as quantum sl2 representations:
V =
s−1⨂
k=0
VNk modg
∼=
p|N|−s+1⨁
j=1
Hom(Vj , V ) ⊗ Vj (2)
The range of the summation is calculated by the Clebsch-Gordan rule [17].
The isomorphism maps ( α j ⊗ v) on the right to α j (v) and Br
s ◦ Ti;s acts on
Hom(Vj, V ) only, while quantum sl2 acts on the Vj only. We can therefore
expand the quantum trace in (1) as follows:
J = Trq(Br
s ◦ Ti;s, V ) =
∑
j
Tr(Br
s ◦ Ti;s, Hom(Vj, V ))Trq(Id, V j ) (3)
We know that Trq(Id, V j) = [ j] = ( qj/ 2 − q−j/ 2)/ (q1/ 2 − q−1/ 2). To calculate the
other traces we study how Br
s ◦ Ti;s acts on an element α ∈ Hom(Vj , V ). The
action is by composition so ﬁrst we look at Ti;s ◦ α , the action of Ti;s. According
to the graphical calculus [18] the colored tangle Ti;s represents the same map as
the (1 , 1)-tangle Ti colored with V . Furthermore we can depict α as a coupon
connecting the top of a vertical strand colored Vj to the lower end of Ti (this
end is colored V ), see ﬁgure 2.
4
Now we can slide the coupon α up along the (1 , 1)-tangle Ti. We obtain
α on top of Ti, where Ti is now colored with Vj . Since Vj is irreducible, the
operator represented by Ti is multiplication by a scalar. By closing Ti one
sees that this scalar is exactly [ j]−1JM1,...,M i− 1,j,...,M c(L). We conclude that
Ti;s ◦ α = [j]−1JM1,...,M i− 1,j,...,M c(L)α .
Figure 2: Sliding the coupon α up through the tangle Ti;s.
The above argument shows that Br
s ◦ Ti;s ◦ α = [j]−1JM1,...,M i− 1,j,...,M c(L)Br
s ◦ α .
Therefore equation (3) becomes:
J =
p|N|−s+1∑
j=1
Tr(Br
s , Hom(Vj , V ))JM1,...,M i− 1,j,...,M c (L) (4)
Note that an equation such as (4) remains valid when one replaces Br
s by any
braid B. Such a satellite formula also appears in [13].
We now concentrate on calculating the trace Tr( Br
s , Hom(Vj , V )). Note that
(Br
s )s = (( σ1 · · ·σs−1)s)r is a central element of the braid group. The element
C = ( σ1 · · · σs−1)s can also be thought of as a curl in s parallel strands (hence
the extra curls in the deﬁnition of Br
s ), so it acts on α as C ◦ α = q
j2 − 1
4 α . If we
set D = q− r
s
j2 − 1
4 Br
s , then Ds acts as the identity on Hom( Vj, V ). An argument
by Jones and Rosso [9] shows that its trace does not depend on q. For the record
we express the trace we were looking for in terms of D:
Tr(Br
s , Hom(Vj , V )) = q
r
s
j2 − 1
4 Tr(D, Hom(Vj , V )) (5)
Since the trace of D does not depend on q we can calculate it at q = 1. In
this case Br
s = D equals the permutation ( σ1 · · · σs−1)r and the representation
V can be viewed as an SL(2) representation. By collecting common factors in
the tensor product we see that V ∼=
⨂ g−1
k=0 V ⊗p
Nk , where p = s/g . Note that our
permutation D acts on V by permuting the factors inside each tensor power.
5
More precisely D = c0 · · · cg−1 where the ck are disjoint p-cycles and ck permutes
the factors of V ⊗p
Nk . We can therefore interpret D as an element of the Cartesian
product Sg
p .
One can view each of the tensor powers V ⊗p
Nk
as a Sp × GL(VNk ) repre-
sentation, where Sp acts by permuting the tensor factors and GL(VNk ) acts
diagonally. By Schur-Weyl duality [17] this space allows a simultaneous decom-
position into irreducibles:
V ⊗p
Nk
∼=
⨁
λ k⊢p
Eλ k ⊗ Wλ k
Here Eλ k is an irreducible Sp representation and Wλ k is an irreducible GL(VNk )
representation and the sum is over all partitions of length no more t han Nk.
Taking the tensor product over all such powers and rearranging t he factors
gives the following decomposition of V as an Sg
p × GL(VN0) × · · · × GL(VNg− 1 )
representation.
V ∼=
⨁
λ 0...λ g− 1⊢p
Eλ 0 ⊗ · · · ⊗ Eλ g− 1 ⊗ Wλ 0 ⊗ · · · ⊗ Wλ g− 1
The GL(VN0 ) × · · · × GL(VNg− 1 ) representation Wλ 0 ⊗ · · · ⊗ Wλ g− 1 is in a nat-
ural way also an SL(2)-representation. We can therefore decompose it into
irreducible SL(2)-representation as follows:
Wλ 0 ⊗ · · · ⊗ Wλ g− 1
∼=
⨁
j
Hom(Vj , W λ 0 ⊗ · · · ⊗ Wλ g− 1 ) ⊗ Vj
Hence we ﬁnd the following decomposition of V :
V ∼=
⨁
j

 ⨁
λ 0...λ g− 1⊢p
Eλ 0 ⊗ · · · ⊗ Eλ g− 1 ⊗ Hom(Vj , W λ 0 ⊗ · · · ⊗ Wλ g− 1 )

 ⊗ Vj
Note that we only allow λ k to have length ≤ Nk. Comparing this decomposition
with the isotypical decomposition (2) for q = 1 we see that:
Hom(Vj , V ) ∼=
⨁
λ 0...λ g− 1⊢p
Eλ 0 ⊗ · · · ⊗ Eλ g− 1 ⊗ Hom(Vj , W λ 0 ⊗ · · · ⊗ Wλ g− 1 ) (6)
The action of D on this space is only on the Eλ k . As above we write D =
c0 · · ·cg−1 as a product of disjoint p-cycles and we note that the cycle ck acts in
Eλ k . If we deﬁne Rj,λ 0...,λ g− 1 = dim(Hom( Vj, W λ 0 ⊗ · · · ⊗ Wλ g− 1 )) and denote
all ck by c we have the following expression for the trace:
Tr(D, Hom(Vj , V )) =
∑
λ 0,...λ g− 1⊢p
χ λ 0 (c) · · · χ λ g− 1 (c) Rj,λ 0...,λ g− 1 (7)
6
Here χ λ is the character of the symmetric group Sp. To calculate these traces
we note that the dimensions Rj,λ 1...,λ g are encoded in the following product
expansion of Schur functions [12]:
g−1∏
k=0
sλ k (tNk−1, t Nk−3, ..., t −Nk+1) =
∑
µ ⊢p|N|−s
Rµ 1−µ 2+1,λ 0...,λ g− 1 sµ (t, t −1) (8)
The above condition on the direct sum in (6) that the length of λ k is no more
than Nk is now incorporated into the Schur functions, because an N -variable
Schur function sλ is nonzero only if λ has no more than N parts.
As a quick check that the above formula (8) includes all the dimension s R,
note that λ k ⊢ p and so the highest degree term of sλ (tNk−1, t Nk−3, ..., t −Nk+1)
is tpNk−p, hence µ ⊢ p|N| − s because the highest degree term of sµ (t, t −1) is
tµ 1 . Note also that only length-two partitions µ contribute to the sum because
the Schur functions sµ have only two variables. In case µ = ( µ 1µ 2) we have
sµ (x, y ) = xµ 1+1yµ 2 −xµ 2 yµ 1 +1
x−y and sµ (t, t −1) = tµ 1 +1− µ 2 −t− (µ 1 +1− µ 2)
t−t− 1 . The range
of the summation in (8) therefore agrees exactly with the range of j in the
decomposition of the tensor product (2). From now on we will param etrize this
range by two part partitions µ ⊢ p|N|− s and set Vµ = Vj , where j = µ 1 −µ 2 +1.
Using the product of Schur functions in (8) as a generating functio n for
the dimensions R we can compute Tr( D, Hom(Vµ , V )) simultaneously for all µ .
First we sum the right hand side and the left hand side of equation (8) with the
characters as in the sum in (7):
∑
µ ⊢|N|−s

 ∑
λ 0,...λ g− 1⊢p
χ λ 0 (c) · · · χ λ g− 1 (c)Rµ,λ 0...,λ g− 1

 sµ (t, t −1) = (9)
∑
λ 0,...λ g− 1⊢p
χ λ 0 (c) · · · χ λ g− 1 (c)
g−1∏
k=0
sλ k (tNk−1, t Nk−3, ..., t −Nk+1) =
g−1∏
k=0
∑
λ k⊢p
χ λ k (c)sλ k (tNk−1, t Nk−3, ..., t −Nk+1) =
g−1∏
k=0
pp(tNk−1, t Nk−3, ..., t −Nk+1) (10)
In the last line we used the expansion of the power sum function pp in terms
of Schur functions [12] p.114. We can use the notion of plethysm [12] p.138 to
write the power sums in terms of the complete symmetric functions h as follows:
pp(tNk−1, t Nk−3, ..., t −Nk+1) = ( pp ◦ hNk−1)(t, t −1) = hNk−1(tp, t −p)
As with partitions we deﬁne hN−1 = ∏ g−1
k=0 hNk−1 so that we can write the above
product (10) as:
7
g−1∏
k=0
pp(tNk−1, t Nk−3, ..., t −Nk+1) = hN−1(tp, t −p) (11)
Comparing equations (9) and (11) we see that to compute the trac es in (7) we
need to express hN−1(tp, t −p) in terms of the sµ (t, t −1). The coeﬃcients in this
expansion will be our traces.
First we consider the case where p = 1. Since we have s = g there are
⌊(|N| − g)/ 2⌋ + 1 two part partitions µ ⊢ | N| − s, that we will number by the
half integers w = (µ 1 −µ 2)/ 2. Since hN−1(t, t −1) is a product of geometric series
we can use the notation deﬁned in the introduction to write: hN−1(t, t −1) =
(|N|−g)/ 2∑
w=(|N|−g)/ 2−⌊(|N|−g)/ 2⌋
(( g
w
)
N
−
( g
w + 1
)
N
) t2w+1 − t−2w−1
t − t−1 (12)
The above equation settles the case p = 1 since the Schur functions are exactly
the geometric series in the two variable case. We will come back to the p = 1
case after we have found the coeﬃcients for p > 1. We will then show that
these cases can be uniﬁed into a single cabling formula for the colored Jones
polynomial.
From now on let’s assume that p ≥ 2. We will carry out the expansion of
hN−1(tp, t −p) into two variable Schur functions in a little more generality by
setting x1 = t and x2 = t−1. As a ﬁrst step consider the following fundamen-
tal identity [12] p.62 relating the complete symmetric functions to th e Schur
functions:
∑
λ
hλ (x)mλ (y) =
∏
i,j
(1 − xiyj)−1 =
∑
λ
sλ (x)sλ (y) (13)
Here mλ (y) is the monomial symmetric function and x = ( x1, x 2, . . . ) and the
sums range over all partitions λ. The ﬁrst part of the identity (13) implies
that hN−1(xp
1, x p
2) is the coeﬃcient of yp(N−1) = yp(N0−1)
0 · · ·yp(Ng− 1−1)
g−1 in the
expansion of the product ∏ g−1
k=0(1 − xp
1yp
k)−1(1 − xp
2yp
k)−1. Factoring we can
also write this product as ∏ g−1
k=0
∏ p−1
u=0(1 − x1ω uyk)−1(1 − x2ω uyk)−1, where
ω = exp(2 πi/p ). Using the second half of the identity (13) we can expand the
same product into two variable Schur functions:
g−1∏
k=0
p−1∏
u=0
(1 − x1ω uyk)−1(1 − x2ω uyk)−1 =
∑
µ
sµ (y0, ωy 0, . . . , ω p−1yg−1)sµ (x1, x 2)
Taking the coeﬃcient of yp(N−1) on the left gives hN−1(xp
1, x p
2) back, while the
coeﬃcient of yp(N−1) on the right hand side is ∑
µ Kµ sµ (x1, x 2), where Kµ is
the coeﬃcient of yp(N−1) in sµ (y0, ωy 0, . . . , ω p−1yg−1). It follows that the trace
we wanted to calculate is equal to this coeﬃcient: Tr( D, Hom(Vµ , V )) = Kµ .
8
We proceed with the calculation of Kµ . By [12] p.72 we can expand the Schur
function sµ (y0, ωy 0, . . . , ω p−1yg−1) in terms of skew Schur functions making it
possible to extract the powers of yj.
sµ (y0, ωy 0, . . . , ω p−1yg−1) =
∑ g−1∏
j=0
y|ν (j)−ν (j− 1)|
j sν (j)/ν (j− 1) (1, ω, . . . , ω p−1)
The sum ranges over all sequences of partitions 0 = ν(0) ⊂ ν(1) . . . ⊂ ν(g) = µ .
Only the sequences of partitions satisfying |ν(j) − ν(j−1)| = p(Nj − 1) contribute
to the coeﬃcient of yp(N−1) in this sum. The contribution of such a sequence is∏ g−1
j=0 sν (j)/ν (j− 1) (1, ω, . . . , ω p−1). In the cases we are interested in µ has length
2 and it follows from [12] p.91 that this contribution is zero unless ν(j) can
be obtained from ν(j−1) by attaching Nj − 1 border strips of length p. A
set theoretical diﬀerence between two nested partitions is called a border strip
of length p if it is connected, does not contain any 2 × 2 squares and has p
elements. If this is the case for all j, then the contribution is σp(µ ) = ( −1)r2,
where 0 ≤ r2 < p is the residue of µ 2 modulo p.
The above argument shows that Kµ = σp(µ )|Kµ |, and that |Kµ | is the
number of sequences of partitions 0 = ν(0) ⊂ ν(1) . . . ⊂ ν(g) = µ satisfying the
condition that ν(j) is obtained from ν(j−1) by attaching Nj − 1 border strips of
length p.
To count the number of such sequences we ﬁrst look a all ways of co nstructing
two part partitions by attaching length p-border strips, starting with the empty
partition. One notices that the lower leftmost corner of a new bord er strip can
be attached at exactly two places: either the end of the ﬁrst row o r the end
of the second row. It follows that we can list all possibilities in a Pascal- like
triangle, see ﬁgure 3.
Figure 3: The Pascal-like triangle of all two part partitions that can b e glued
from 5 or less border strips of length p = 4.
The k-th row of our Pascal triangle contains k + 1 partitions that we index by
9
the half integers −k
2 , −k
2 + 1, . . . , k
2 . The triangle is ordered such that if µ has
index w(µ ) = w then µ 1 − µ 2 + 1 = sgn( w)(2wp + 1) and sgn( w) = σp(µ ),
provided that we agree that sgn(0) = 1.
Interpreting |Kµ | in terms of the Pascal triangle we see that |Kµ | is equal to
the number of ways to move from the (empty) top of the triangle to µ ⊢ p|N| −s
in g steps of length Nk −1, for k = 0 . . . , g −1. A step of length A can go in A+1
directions that are conveniently indexed by −A
2 , −A
2 +1, . . . , A
2 . The sum of these
indices must be the index of µ , that is w. Therefore the number of ways is exactly
the coeﬃcient of xw in the product ∏ g−1
k=0(x−
Nk − 1
2 + x−
Nk − 1
2 +1 + . . . + x
Nk − 1
2 ).
Using the notation deﬁned in the introduction we see that |Kµ | =
( g
w
)
N and so
Kµ = sgn(w)
( g
w
)
N.
We can now summarize the calculation of J = JM1,...,M i− 1, N,...,M c(Lr
i;s) as
follows. First we expressed it in equation (4) as a sum over the colors j of a
trace times the colored Jones of the uncabled link. In (5) the depen dence on
q was extracted and ﬁnally the rest of the trace was shown to be give n by the
coeﬃcients in equation (12) for p = 1 and by Kµ for p ≥ 2. Along the we changed
the sum over colors into a sum over two part partitions µ , via j = µ 1 − µ 2 + 1.
We just saw that we can enumerate the µ for which Kµ is nonzero by the half
integers w. Combining all this we ﬁnd for p ≥ 2: JM1,...,M i− 1, N,...,M c (Lr
i;s) =
(|N|−g)/ 2∑
w=−(|N|−g)/ 2
q
rwp(wp+1)
s sgn(w)
( g
w
)
N
JM1,...,M i− 1, |2wp+1|,...,M c(L)
Remarkably this formula is also valid for p = 1. In this case the non-negative
w run through all partitions and both w and −(w + 1) contribute to the same
term JM1,...,M i− 1, |2w+1|,...,M c (L), thus producing the coeﬃcients found in (12).
Finally the convention JM1,...,M i− 1, −k,...,M c = −JM1,...,M i− 1,k,...,M c allows us
to incorporate the sign into the colored Jones polynomial because s gn(w) =
sgn(2wp + 1). Noting that p = s/g the proof of theorem 1 is complete.
3 Proof of the volume conjecture for zero vol-
ume links
As an application of the cabling formula we just proved we will show tha t the
volume conjecture holds true for all zero volume knots and links (co rollary 1).
Such links are related to cabling by the fact that all links of zero simplic ial
volume are obtained from the unknot by repeated cabling and conne cted sum
[5].
In the volume conjecture the usual normalization of the colored Jo nes poly-
nomial for knots is to divide by the value of the unknot. However, if a link has
s split components then the unnormalized Jones has at least an s fold zero at
the N -th root of unity [19]. We therefore choose to normalize it by dividing
by [ N ]s. For convenience we work with A = q1/ 4 instead of q so that for the
volume conjecture we need to evaluate at A = eπi/ 2N .
10
The unnormalized colored Jones polynomial of a link with c components is
a multi-sequence of Laurent polynomials in A of the form PN(A) = ∑
j aj, NAj,
where N = ( N1, . . . , N c). We say that a multi-sequence is moderate if there
exist C, m > 0 such that
∀ N : |maxdegPN|, |mindegPN|, |aj, N| < C |N|m
It is clear that the set of moderate sequences is closed under prod ucts and
diﬀerentiation with respect to A.
To prove the volume conjecture for all zero volume links we ﬁrst sho w that
their unnormalized colored Jones polynomials are moderate. Since su ch links are
obtained from the unknot by repeated cabling and connected sum, we need to
show that [N ] is moderate (trivial) and that the set of moderate multi-sequence s
is closed under taking products and under an operation that gener alizes cabling
of links that we now deﬁne. Given two multi-sequences PM(A) and QN,w (A)
deﬁne a new multi-sequence R by
RM1,...M i− 1, N,...,M c(A) =
∑
|w|≤(|N|−g)/ 2
QN, 2w(A)PM1,...,M i− 1, |2wp+1|,...,M c(A)
The triangle inequality shows that that if P and Q are moderate then so is
R. The cabling formula applied to the colored Jones polynomial J of any link
is an example of the above deﬁned operation where P = J and QN,w (A) is a
multi-sequence that does not depend on the link and is readily read oﬀ from
the cabling formula or rather the version at the end of the last sect ion. It is not
hard to see that this Q is indeed moderate.
Now that we know that the unnormalized colored Jones polynomial of a zero
volume knot JN(A) is moderate we conclude the proof of corollary 1 as follows.
To evaluate the normalized Jones polynomial we will use ’l Hospital’s rule after
writing it as
JN,...,N (A)/ [N ]s = ˜JN,...,N (A)/ (A2N − A−2N )s
where ˜J = ( A2 − A−2)sJ is again moderate. If we diﬀerentiate both numera-
tor and denominator s times with respect to A and evaluate at eπi/ 2N we get
( eπi/ 2N
−4N ) ds
dAs ˜JN,...,N (eπi/ 2N ). Since ds
dAs ˜JN is again moderate, it follows that:
lim
N →∞
2π
N | JN,...,N
[N ]k (e
πi
2N )| = 0
11
References
[1] G. Andrews, Euler’s ”exemplum memorabile inductionis f allacis” and q-Trinomial coef-
ﬁcients, J. Amer. Math. Soc. , 3 (1990), 653–669.
[2] J. Dubois, R. Kashaev, On the asymptotic expansion of the colored Jones polynomial
for torus knots, preprint, Arxiv 0510.5607.
[3] S. Garoufalidis, On the characteristic and deformation varieties of a knot, proceedings
of the Casson fest, Geometry and Topology Monographs , 7 (2004), 291–309.
[4] S. Garoufalidis, T. Le, The colored Jones function is q-h olonomic, Geometry and Topol-
ogy, 9 (2005) 1253–1293.
[5] C. Gordon, Dehn surgery and satellite knots, Trans. Amer. Math. Soc. , 275, 2 (1983),
687-708.
[6] K.Hikami, Volume conjecture and asymptotic expansion o f q-series, Exp. Math. , 12
(2003), 319–337.
[7] K. Hikami, Quantum invariant for torus link and modular f orms, Commun. Math. Phys. ,
246 (2004), 403–426.
[8] K. Hikami, H. Murakami, Colored Jones polynomials with p olynomial growth, preprint,
Arxiv 0711.2836.
[9] V. Jones, M. Rosso, On the invariants of torus knots deriv ed from quantum groups,
Journal of Knot Theory and its Ramiﬁcations , 2,1 (1993), 113–123.
[10] R. Kashaev, The hyperbolic volume of knots from the quan tum dilogarithm, Lett. Math.
Phys., 39, 3 (1997), 269–275.
[11] R. Kashaev, O. Tirkkonen, Proof of the volume conjectur e for torus knots, Journal of
Mathematical Sciences, 115, 1 (2003), 2033–2036.
[12] I. Macdonald, Symmetric functions and Hall polynomial s, Clarendon Press, 1995.
[13] H.Morton, P.Strickland, Jones polynomial invariants for knots and satellites, Math. Proc.
Camb. Phil. Soc. , 109 (1991), 83–103.
[14] H. Morton, The coloured Jones function and Alexander po lynomial for torus knots,
Math. Proc. Camb. Phil. Soc. , 117 (1995), 129–135.
[15] H. Murakami, An introduction to the volume conjecture a nd its generalizations, preprint,
Arxiv 0802.0039.
[16] H. Murakami, J. Murakami, The colored Jones polynomial s and the simplicial volume
of a knot, Acta Math. , 186 (2001), 85–104.
[17] C.Procesi, Lie groups, an approach through invariants and representat ions, Springer,
2007.
[18] V.Turaev, Quantum invariants of knots and 3-manifolds , W alter de Gruyter, 1994.
[19] R. van der Veen, The volume conjecture for augmented kno tted trivalent graphs,
preprint, Arxiv 0805.0094.
[20] H. Zheng, Proof of the volume conjecture for Whitehead d oubles of a family of torus
knots, Chin. Ann. of Math. B , 28, 4 (2007), 375–388.
12
