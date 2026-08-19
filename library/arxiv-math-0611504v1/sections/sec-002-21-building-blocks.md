---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-002-21-building-blocks
section_title: "Building blocks"
section_number: 2.1
pages: 4-7
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry STEPHANE BASEILHAC RICCARDO BENEDETTI — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
matrix dilogarithms RN (∆( b,w,f,c )) ∈ Aut(CN ⊗ CN ) deﬁned for every odd positive integer N [5].
Flat/charged-I tetrahedra. Consider the half-space model of the oriented hyperbolic space H3,
with the group of direct isometries identiﬁed with PSL (2, C) by the conformal action on ∂H
3
= CP1 =
C ∪ {∞} by Moebius transformations. An I-tetrahedron is an oriented ideal tetrahedron ∆ in ∂H
3
with distinct ordered vertices v0, v1, v2 and v3 on ∂H
3
.
In fact we consider ∆ as an abstract oriented simplex equipped with a n additional decoration. The
ordering of the vertices is encoded by a branchingb, that is, edge orientations obtained via the rule:
each edge points towards the biggest end-point. Each 2-face has an induced branching, and a b-
orientation, which is just compatible with that of two edges on the boundary. We order the 2-faces
δ0, ...δ 3 by the opposite vertices, and the edges e0, e1, e2 of δ3 by stipulating that for j = 0, 1, vj
is the ﬁrst end-point of ej. For exactly two 2-faces the b-orientation and the boundary orientation
are the same. The b-orientation of ∆ coincides with the given one if the b-orientation of δ3 looks
anti-clockwise from v3. We give ∆ and each 2-face δ a b-sign ∗b and σ(δ) respectively, which is 1 if
the two orientations agree, and −1 otherwise.
The hyperbolic structure is encoded by the cross-ratio moduli tha t label the edges of ∆. Recall
that opposite edges share the same cross-ratio moduli. We set w = (w0,w 1,w 2) with wj = w(ej) ∈
C \ {0, 1}. Hence wj+1 = 1/(1 −wj) (indices mod( Z/3Z), and
w0 = (v2 −v1)(v3 −v0)/(v2 −v0)(v3 −v1).
We say that the I-tetrahedron (∆ ,b,w ) is non-degenerate if it is of non zero volume, that is if the
imaginary part of each wi is not zero; then they have the same sign ∗w = ±1.
It is very convenient to encode (∆ ,b,w ) in dual terms. In Figure 1 we show the 1-skeleton of the dual
cell decomposition of Int(∆) ( x and the indices i, j, k and l are considered below). It is understood
that (dual) edges without arrows are incoming at the crossing. Not e that an oriented edge is outgoing
exactly when the b-sign of the dual 2-face is 1.
x x
*b =1 *  = −1b l
k
j
j
j
l
i
k
Figure 1. I-tetrahedra and dual encoding.
A ﬂat/charged I-tetrahedron is an I-tetrahedron equipped with a ﬂattening f and a charge c, two
notions ﬁrst introduced in [24] and [25]. Flattenings and charges a re Z-valued functions deﬁned on the
edges of ∆ that take the same value on opposite edges and satisfy t he following properties, respectively
(where log has the imaginary part in ] −π,π ]):
F. Flattening condition: l0 + l1 + l2 = 0, where
(1) l j = lj(b,w,f ) = log(wj) +
√
−1πfj,
C. Charge condition: c0 +c1 +c2 = 1.
QUANTUM HYPERBOLIC GEOMETRY 5
We call lj a (classical) log-branch, and for every odd N >1 we deﬁne the (levelN ) quantum log-branch
as
(2) l j,N = log(wj ) +
√
−1π(N + 1)(fj − ∗bcj).
The bijective map
(l0, l1, l2) ↦→
(
w0; l0 − log(w0)√−1π , l1 − log(w1)√−1π
)
yields an identiﬁcation of the set of log-branches on (∆ ,b ) with the Riemann surface ˆC of the maps
w0 ↦→(log(w0) +επ
√
−1, log((1 −w0)−1) +ε′π
√
−1), with ε,ε ′ ∈ { 0, 1}. Similarly, the set of triples
(w′
0,w ′
1,w ′
2) with w′
j = exp(lj,N/N) gets identiﬁed with the quotient covering by N Z ×N Z. These
two spaces are the domains of deﬁnition for the matrix dilogarithms t o be described next, when N = 1
and N >1 respectively.
Matrix dilogarithms. Denote by log the standard branch of the logarithm, which has the im aginary
part in ] −π,π ]. Recall that the space of triples of log-branches on a branched or iented tetrahedron
is identiﬁed with the Riemann surface ˆC.
ForN = 1, we forget the integral charge c, so that R1 is deﬁned on ﬂattened I-tetrahedra:
(3) R1(∆ ,b,w,f ) = exp
( ∗b
π√−1 R(w0;f0,f 1)
)
= exp
( ∗b
π√−1
(
−π2
6 − 1
2
∫ w0
0
( l0(t)
1 −t − l1(t)
t
)
dt
))
where l 0(t) = log( t) +
√
−1πf0 and l 1(t) = log((1 −t)−1) +
√
−1πf1. The map R : ˆC → C/π2Z
is holomorphic, and takes values in C/2π2Z on the component with even valued ﬂattenings ([25],
Proposition 2.5).
ForN = 2m+1 > 1 and every complex number x setx1/N = exp(log(x)/N) (01/N = 0 by convention).
Put
(4) g(x) :=
N −1∏
j=1
(1 −xζ−j )j/N.
The function g is deﬁned over C, and analytic over the complement of the rays from x =ζk to inﬁnity,
k = 1,..., N − 1. Set h(x) := g(x)/g(1) (we have |g(1)| = N 1/2). For any u′,v ′ ∈ C satisfying
(u′)N + (v′)N = 1 and any n ∈ N, let
ω(u′,v ′|n) =
n∏
j=1
v′
1 −u′ζj
withω(u′,v ′|0) = 1 by convention. The functions ω are periodic in their integer argument, with period
N . Write [x] = N −1(1 −xN )/(1 −x). Given a ﬂat/charged I-tetrahedron (∆ ,b,w,f,c ), set
(5) w′
j = exp(lj,N/N)
with lj,N as in (2). Put the standard tensor product basis on CN ⊗ CN . The matrix dilogarithm of
levelN >1 is the tensor valued function of ﬂat/charged I tetrahedra deﬁned by
(6) RN (∆ ,b,w,f,c ) =
(
(w′
0)−c1(w′
1)c0
) N −1
2 (LN )∗b(w′
0, (w′
1)−1) ∈ Aut(CN ⊗ CN )
where (recall that N = 2m + 1)
LN (u′,v ′)i,j
k,l = h(u′) ζkj+(m+1)k2
ω(u′,v ′|i −k) δ(i +j −l)
(
LN (u′,v ′)−1) i,j
k,l = [u′]
h(u′) ζ−il−(m+1)i2 δ(k +l −j)
ω(u′/ζ,v ′|k −i)
withδ the Kronecker symbol with period N , that is δ(n) = 1 if n ≡ 0 mod(N ), and δ(n) = 0 otherwise.
Note that we use the branching in order to associate an index among i, j, k and l to each 2-face of
∆. The rule is shown in Figure 1.
6 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Up to multiplication by N th roots of unity, the map RN is holomorphic on ˆC, because w′
j =
exp((1/N)(lj − ∗bcj)) exp((fj − ∗bcj)πi) and the parity of fj is unaltered when we move lj con-
tinuously. The ambiguity of RN is a consequence of the jumps of g along the cuts from the ζk to
inﬁnity.
On matrix dilogarithms via geometric quantization. As explained in Remark 1.1, in this paper
we concentrate on the quantum matrix dilogarithms (ie. with N >1). These were derived in [5] from
the Kashaev’s 6j-symbols for the cyclic representation theory of a Borel quantum subalgebra Bζ of
Uζ(sl(2, C)), where ζ = exp(2iπ/N). Let us outline here very brieﬂy an alternative construction base d
on geometric quantization of R1, thus clarifying their geometric origin (for details see [3]).
Consider an abstract oriented quadrilateral Q, triangulated by two triangles. Order the triangles of
Q, and associate to each a copy Xi, i = 1, 2, of X = {(u,v,w ) ∈ (C∗)3 | uvw = −1}, where u, v
and w correspond to the corners, ordered cyclically by using the orienta tion. Let us regard C as the
Riemann surface of log, ie.
C = {(z;p) ∈ C∗ × 2Z}/((z +i0;p) ∼ (z −i0;p + 2), ∀z ∈ (−∞; 0)).
As in (1), we set l( z;p) = log(z) +
√
−1πp. Let
ˆX = {((u;p), (v;q), (w;r)) ∈ ˜X | l(u;p) + l(v;q) + l(w;r) = 0 }
a subspace of the universal covering ˜X of X, and put
ˆC(z;p,q ) = {(l(z;p), l((1 −z)−1;q))} = {((z;p), ((1 −z)−1;q), (1 −z−1;r)) ∈ ˆX} .
DenotebQ =d logu1 ∧d logv1 +d logu2 ∧d logv2 the canonical complex symplectic form on X1 ×X2,
and
θQ = (1/2) ((l(u1;p1)d logv1 − l(v1;q1)d logu1) + (l(u2;p2)d logv2 − l(v2;q2)d logu2)))
the symplectic potential for the lift of bQ to ˆX1 × ˆX2. Consider the four punctured sphere S2
Q
obtained by gluing along the boundary in the natural way Q and the quadrilateral Q′ obtained from
it by exchanging the diagonal. The S4-action on the vertices of S2
Q reorders the copies Xi (i = 1,..., 4)
attached to the triangles, and induces the usual action of PSL (2, Z) on each ˆXi ∼
= C2, with standard
basis l(ui;pi) and l(vi;qi), by symplectomorphisms.
Proposition 2.1. There is a canonical family { ˜φn
Q}n∈Z : ( ˆX1 × ˆX2,bQ) → ( ˆX3 × ˆX4,bQ′ ) of analytic
symplectomorphisms equivariant for the S4-action on S2
Q, given by (see Figure 2)
˜φn
Q((l(u1;p1), l(v1;q1)), (l(u2;p2), l(v2;q2))) = ((l(u′
1;p′
1), l(v′
1;q′
1)), (l(u′
2;q′
2), l(v′
2;q′
2))),
where we identify ˆX with C2 (ﬁrst two coordinates) and
{
l(u′
1;p′
1) = l( u1;p1) − l(u′
2;p′
2)
l(v′
1;q′
1) = l( v1;q1) + l(u2;p2)
{
l(u′
2;p′
2) = l( u2;p2) − l((1 −u1v2)−1;n)
l(v′
2;q′
2) = l( v2;q2) + l(u′
1;p′
1) + l(v′
1;q′
1) .
The maps ˜φn
Q satisfy the pentagon relation, that is, ˜φn1
Q1 ◦ ˜φn2
Q2 ◦ ˜φn3
Q3 ◦ ( ˜φn4
Q4 )−1 ◦ ( ˜φn5
Q5 )−1 = Id bX 3 , where
Qi has diagonal the ith edge exchanged in Figure 3, for the positive cyclic orderi ng starting from the
top left pentagon. Moreover θQ − ˜φ∗
nθQ′ = −dR, where R : ˆC(u1v2;m,n ) → C/2πZ is the extended
dilogarithm of (3), and ˆC(u1v2;m,n ) = {(l(u1;p1) + l(v2;q2), l((1 −u1v2)−1;n))} is attached to the
diagonal of Q.
By “canonical” we mean that { ˜φn
Q} is the unique satisfying some natural properties related to conﬁgu -
ration spaces of points in CP 1. In fact, ˆC(z;p,q ) is isomorphic to the moduli space of similarity classes
of triangles in the complex plane endowed with lifts to R of the angles, or, equivalently, to the moduli
space of isometry classes of hyperbolic ideal tetrahedra with even valued ﬂattenings. The complex
symplectic form d logu ∧d logv restricts to the real symplectic form w = −d log(z) ∧d log(1 −z) on
ˆC(z;p,q ). It is the diﬀerential version of the extended complex Dehn invaria nt ˆδ : ˆC(z;p,q ) → C ∧ C,
(z;p,q ) ↦→l(z;p) ∧Z l(1 −z;q) of [25].
QUANTUM HYPERBOLIC GEOMETRY 7
When Im(z) ⁄= 0 the form w is K¨ ahler for the usual complex structure on R2. Replace ˆC with the
ramiﬁed covering ˆCN of C∗ obtained by taking the quotient with N Z ×N Z. Put the forms Nw and
Nθ on ˆCN . Standard half-form quantization of ˆCN produces a N -dimensional vector space Γ N of
sections of a line bundle over ˆCN (the coherent states ), and the maps ˜Φn
Q : Γ N
1 ⊗ ΓN
2 → ΓN
3 ⊗ ΓN
4
induced by pull back via { ˜φn
Q}, that is such that ˜Φn
Q(s) = s ◦ ˜φn
Q for any s ∈ ΓN
1 ⊗ ΓN
2 , coincide with
the matrix dilogarithms RN for some suitable basis. In particular, the pentagon relation for ˜φn
Q lifts
to the ﬁve term identities mentionned after Proposition 2.5 below.
u1 v1
u2
v2
u2’
u1’ v1’
v2’
Figure 2. A diagonal exchange.
Figure 3. The pentagon relation.
