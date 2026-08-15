---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
Suppose that M is a compact oriented 3–manifold without boundary.
The sl2 Witten-Reshetikhin-Turaev invariant (see (Wi), (RT)) is a
complex number invariant ZK(M,L ) of embeddings of links L in M,
dependent on an integer K. It is known that for links inS3, ZK(S3,L)
is a polynomial in q = exp 2πi
K and q−1, namely the generalised Jones
polynomial of the link L.
Now assume thatM is a rational homology sphere withH =|H1(M, Z)|.
In this paper we will only consider the case of invariants where the link
L is empty. From its algebraic deﬁnition, e.g. via quantum groups,
ZK(M, ∅) can be written as a rational (or polynomial) function of q
at Kth roots of unity. In the normalization for which ZK(S3, ∅)=1 ,
denote the invariant for the pair (M, ∅), by ZK(M). For odd prime K,
ZK(M) ∈ Z[q] (see (M1), (M2)), so that for some am,K(M) ∈ Z,o n e
53
53–70.
C© 2004 Kluwer Academic Publishers. Printed in the Netherlands.
J.M. Bryden (ed.), Advances in Topological Quantum Field Theory,
N. Jacoby & R. Lawrence
has
ZK(M)=
∞∑
m=0
am,K(M)(q − 1)m . (1)
Although the am,K are not uniquely determined from this relation since
qK −1
q−1 = 0, however they are determined moduloK for m ≤ K −2 when
K is prime. It is known from (O1) and (O2) that there exist rational
numbers λm(M) such that,
am,K(M) ≡
( H
K
)
λm(M)( 2)
as elements ofZ/KZ for all suﬃciently primesK ≥ 2m+3. The formal
power series
Z∞(M)=
∞∑
m=0
λm(q − 1)m ,
is known as the Ohtsuki series of M and by (R3) Z∞(M) ∈ Z[ 1
2H ][[h]]
where q =1 + h. For integer homology spheres ( H =1 )w eh a v e
Z∞(M) ∈ Z[[h]], while λ0(M)=1a n d λ1(M)=6 λ(M) where λ(M)
denotes the Casson invariant ofM. In generalZ∞ is expected to be the
asymptotic expansion of the trivial connection contribution toZK(M)
in Chern-Simons theory.
Relatively few computations of Z∞ have been carried out. For Lens
spaces, Jeﬀrey’s closed formula (Je) for ZK gives a formula for Z∞,
Z∞(L(P,Q )) = q±3s(Q,P) q
1
2P − q− 1
2P
q1/2 − q−1/2
,
where s(Q, P) is a modiﬁed Dedekind sum. For Seifert ﬁbred manifolds,
ZK can be written as the asymptotic expansion around q = 1 of a
holomorphic function of q expressed as a complex (contour) integral
(LR). Thus for a Seifert ﬁbred manifold which is an ZHS,
Z∞
(
Σ
( Q1
P1
,..., QN
PN
))
= c.q−φ
4
∫
e
iKy2
8πP
∏ N
j=1 sinh y
2Pj
(sinh y
2)N −2 dy ,
where P = ∏ Pj, c is a constant (dependent on P)a n dφ is a rational
number,
φ =3 s i g nP +
N∑
j=1
(
12s(Qj,P j) − Qj
Pj
)
.
For special cases some other formulae are known, for example for ±1
surgery around the trefoil, that is for the Poincar´ e homology sphere
54
Some computations of Ohtsuki series 
Σ(2,3, 5) and for Σ(2, 3, 7), (see (LZ), (Le))
q(q − 1)Z∞(Σ(2,3, 5))(q)= 1 − 1/2
∞∑
n=1
χ(n)q(n2−1)/120
(q − 1)Z∞(Σ(2,3, 7))(q)=
∞∑
n=0
q−1
2 n(n+1)(qn+1 − 1)... (q2n+1 − 1)
where the odd function χ : Z/60Z −→ { −1, 0, 1} takes value +1
precisely at 1, 11, 19 and 29 (and nowhere else).
Such computations have been obtained using three approaches. All
use a surgery presentation of the manifold via a link.
− O n ec a nw r i t eas t a t es u mf o rZK in which a state is a labeling
of the regions and components of a diagram of the link (see (KL))
and the local weights are quantum dimensions, θ-nets and quan-
tum 6j -symbols on the diﬀerent elements of the diagram (com-
ponents/regions, edges, crossings, respectively). One can use the
method of recombination here to rewrite the state sum obtained in
a possibly simpler way. To extract a formula forZ
∞ now requires
some manipulations of the form of the sums involved inZK which
only work for a small class of manifolds. This was used in (L) and
(LZ).
− Using conformal ﬁeld theory, one can write ZK as a sum of prod-
ucts of S and T matrix elements which take a particular simple
form for special manifolds. This was used to obtain Z∞ in (Je),
(LR).
− Using the formulation ofJL(ρ1,...,ρ c), the coloured Jones polyno-
mial of a linkL coloured by representationsρi on its c components,
as the image of the link (or rather of a 1-tangle whose closure is
the link) under a representation of the category of tangles, one can
write J
L in terms of the universal R-matrix, as the scalar value
taken by an element of Uqsl2⊗c in the representations ρi.F r o m
this universal invariant of the link an expression for Z∞(M)c a n
be obtained as an inﬁnite sum with the property that coeﬃcients
of (q − 1)
n (for any n) arise only form a ﬁnite number of terms in
the sum. This was the method used by Le, (Le).
To obtain closed forms forZ∞ using the ﬁrst two approaches, relies
on the manifold being obtainable from a particularly simple link, since
in the end the combinatorial formulae for Z
K depend on quantum 6j-
symbols (or what is the same thing, R-matrix entries) which enter at
each crossing in a link diagram presentation. These have complicated
55
N. Jacoby & R. Lawrence
formulae even for Uqsl2 and so only for those manifolds for which the
quantum 6j symbols can be manipulated to cancel can a closed form be
expected suﬃcient to ﬁnd Z∞. This occurs for Seifert ﬁbred manifolds.
In this paper we will consider a special (two parameter) class of
manifolds (see §2) for which the state sum formula is relatively sim-
ple, although still complicated enough that a closed formula for Z∞ is
unknown. In (Ja), computer computations were carried out for Z∞ on
this family; we outline the method and some peculiarities relating to
numerical precision, in §3. In §4, some of the results are given graph-
ically along with conjectures that they support. Finally, in §5, some
possible generalizations are suggested.
