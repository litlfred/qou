---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-020-62-invariants-of-cusped-manifolds-and-surgery-fo
section_title: "Invariants of cusped manifolds and surgery formulas"
section_number: 6.2
pages: 29-35
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
manifold triangulations T used in [5] (see Deﬁnition 6.2 and Deﬁnition 6.3 in that paper) to deﬁne
the quantum hyperbolic invariant trace tensors HN(T ) for oriented cusped hyperbolic manifolds.
Let M be a cusped manifold.
Denote Z the pseudo-manifold obtained by taking the one point
compactiﬁcation of each cusp of M. M admits a triangulation by positively embedded hyperbolic ideal
tetrahedra, possibly including some degenerate ones of null volume (ie. having real cross-ratios). Such
a triangulation can be obtained by subdividing the canonical Epstein-Penner cell decomposition of M.
This gives rise to triangulation (T0, z0) of Z, where z0 is the cross-ratio function of the abstract edges of
T , the imaginary part of every cross-ratio being ≥0. We call it a quasi-geometric ideal triangulation
of Z.
If some quasi-geometric triangulation admits a global branching, we say that M is gentle.
More generally, M is said weakly-gentle if there is an I-triangulation (T, b, w) of Z such that (T, z),
z = w∗b, is obtained via a (possibly empty) ﬁnite sequence (T0, z0) →. . . →(Ti, zi) →. . . →(T, z) of
30
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
positive 2 →3 transits, where (T0, z0) is a quasi-geometric triangulation of Z as above. Each transit
(Ti, zi) →(Ti+1, zi+1) is deﬁned by WTi(e) = WTi+1(e), with all exponents ∗b = 1 (see (7)). Every
such a (T, b, w) can be enhanced to ﬂat/charged I-triangulations T = (T, b, w, f, c).
Given (T0, z0), it is certainly possible to get an I-triangulation (T, b, w) by performing also some
bubble moves (hence introducing new interior vertices). The authors do not know any example of
non weakly-gentle cusped manifold, that is, such that we are forced to do it. Anyway, dealing with
bubble moves is a technical diﬃculty which will appear also in the proof of Theorem 6.3 (1) below.
We overcome it as follows. We ﬁx an edge a of the canonical Epstein-Penner cell decomposition of
M, and take A made by two copies of a that intersect at non manifold points of Z; the second copy
runs parallel to a within an open cell of the decomposition. Hence, A is a circle covered by two arcs.
We need to enlarge the notions introduced in Deﬁnition 2.10. We say that (T, H) is a distinguished
triangulation of (Z, a) if H is a subcomplex of the 1-skeleton of T isotopic to A, that contains all the
regular vertices of T , and such that one arc of A is covered by an edge l of H. We say that c is a
global charge on (T, H) if
(19)
CT (e) =



4
0
2
if e = l
if e ⊂H \ l
if e ⊂T \ H
If H = ∅this reduces to the usual notion of global charge on a closed triangulated pseudo manifold
whose non manifold points have toric links. By using bubble moves and the existence of such usual
global charges, it is easily seen that (T, H) supports global charges as in (19) (see the proof of Theorem
6.8 in [5] for the details).
We say that T = (T, H, b, w, f, c) is a ﬂat/charged I-triangulation of (Z, a) if (T, H, b, c) is a branched,
charged and distinguished triangulation of (Z, a), and (T, z), z = w∗b, is obtained from a quasi
geometric (T0, z0) via a ﬁnite sequence (T0, z0) →. . . →(T, z) of transits supported by positive 2 →3
moves and bubble moves.
By setting a = ∅and H = ∅, this deﬁnition incorporates that for the
weakly-gentle case.
In [5] it is shown that ﬂat/charged I-triangulations T of (Z, a) (with arbitrary weights) do exist and
that, for every odd N ≥1,
HN(M, a) = HN(T )
is a well deﬁned invariant of (M, a), providing the weights of ﬂat/charges to be 0. To simplify the
exposition, below we continue with this normalization. When M is weakly-gentle we get invariants
HN(M). In fact, as a by product of the following discussion, we will realize that HN(M, a) does not
depend on the choice of a, so that HN(M) is always well deﬁned (see Corollary 6.4).
Let us recall now a few facts related to hyperbolic Dehn ﬁlling (see [29], [6], [27]). A quasi geometric
triangulation (T0, z0) as above corresponds to the complete structure of M. It can be deformed in a
complex variety of dimension equal to the number of cusps. If z′ is close enough to z0, (T0, z′) is a
triangulation by (possibly negative - see [27]) embedded hyperbolic ideal tetrahedra in a non-complete
hyperbolic structure, say M ′, close to M. In some case the completion of M ′ gives rise to a compact
closed hyperbolic manifold W, topologically obtained by Dehn ﬁlling of the (truncated) cusps of M.
The core of each attached solid torus is a “short” simple closed geodesic Lj of W, so that we have the
(geodesic) link L = `
j Lj. Moreover, there are sequences (W n, Ln) obtained in this way such that
the length of Ln goes to 0 when n →+∞. Hence (W n, Ln) converges to the cusped manifold M (in
a neat geometric sense). From now on we will consider small deformations z′ leading to such closed
completions.
As well as (T0, z0) gives rise to a triangulation T = (T, H, b, w, f, c) of (Z, a), z′ close to z0 gives rise to
another ﬂat/charged I-triangulation T ′ = (T, H, b, w′, f ′, c), where w′ is close to w and the log-branch
associated to the global ﬂattening f ′ corresponds to a continuous deformation of the one for f.
Lemma 6.2. (See [25], p.
469) Let z′ be a small deformation of z0 producing (W, L), and mj
be a meridian of each link component Lj. Then there exist ﬂattenings f ′′ for the deformed trian-
gulation (T, b, w′) such that the weight γ(f ′′) associated to the collection of log-branches of T ′′ =
(T, H, b, w′, f ′′, c) satisﬁes γ(f ′′)(mj) = 0 for all j.
QUANTUM HYPERBOLIC GEOMETRY
31
Proof. The logarithm of the derivative of the holonomy of mj is 0 at the complete structure, but after
deformation it represents a full 2π-rotation about Lj (see eg. [29] or [6]). Hence γ(f ′)(mj) ∈Z
√
−1π.
The result then follows from the comments after Theorem 2.12.
✷
An explicit construction of ﬂattenings f ′′ as in the lemma shall be recalled during the proof of theorem
6.3.
Hence, we dispose of two ﬂat/charged I-triangulations of (Z, a), T ′ = (T, H, b, w′, f ′, c) and
T ′′ = (T, H, b, w′, f ′′, c), relative to a small deformation z′ of the complete structure z0 as above,
leading to respective trace tensors HN(T ′) and HN(T ′′). We can now state the main results of this
Section.
Theorem 6.3. [Cusped manifold surgery formula] Let (W, L) be obtained by completion of a small
deformation z′ of z0, and T ′, T ′′ be associated triangulations. Denote by ρ the hyperbolic holonomy
of W. Then we have HN(W, L, ρ) =N HN(T ′′). Moreover, associated to each cusp Cj of M there is
an explicitely known map Λj
N(T ′′) : {N −states of T} →C such that the following surgery formula
holds:
HN(W, L, ρ) =N
X
s
Y
∆⊂T
RN(∆, b, w′, f ′, c)s
Y
j
Λj
N(T ′′)(s)
where s runs over the N-states of T and RN(∆, b, w′, f ′, c)s is the matrix dilogarithm entry determined
by s, for the tetrahedron with the continuously deformed structure.
Corollary 6.4. If {(Wn, Ln, ρn)} is a sequence of closed hyperbolic Dehn ﬁllings converging to the
cusp manifold M, then for every arc a we have limn HN(Wn, Ln, ρn) =N HN(M, a). Hence HN(M) =
HN(M, a) is always a well deﬁned invariant of M (beyond the weakly-gentle case).
Remarks 6.5. (1) Theorem 6.3 is the analog for N > 1 of Theorems 14.7 and Theorem 14.5 in [25],
which describe surgery formulas for the volume, Vol(W), and Chern-simons invariant, CS(W), of W:
√
−1(Vol(W) +
√
−1CS(W)) =
X
∆⊂T
R(∆, b, w′, f ′) −π√−1
2
X
j
λ(Lj)
where R is given by (3) and λ(Lj) is the complex length of Lj, that is, the logarithm of the dilation
factor of its holonomy, which is a loxodromic transformation of H3. The technical complications due
to the bubble moves disappear for N = 1.
(2) If M is gentle and has a geometric branched ideal triangulation (T, b, w) without degenerate
tetrahedra, then for each 3-simplex the ﬂattenings of T ′ for a suﬃciently small deformation are just
−∗b times integral charges. It follows from the proof of Theorem 6.3 that the scissors congruence class
cIfc(W, L, ρ) of [5], section 7, coincides with Neumann’s deformed scissors congruence class ˆβ(M ′) in
[25], Theorem 14.7 (see also Remark 6.12 and Conjecture 7.9 in [5], where the undeformed ˆβ(M) is
denoted cIfc(M)).
(3) In general there are small deformations z of z0 leading to complete manifolds that are still cusped,
that is only some cusps of M have supported a hyperbolic Dehn ﬁlling. There are also sequences of
such cusped manifolds M n, with (short) geodesic links Ln, converging to M. Similarly to the fusion
of QHFT with QHFT0 (see Section 5.3) we can deﬁne quantum hyperbolic invariants HN(M n, Ln)
for which the natural extensions of Theorem 6.3 and Corollary 6.4 hold.
Let us consider now (W, LF, L0, ρ). Let Lj be a component of LF, ¯λj = Lj∪L′
j, L′
j being the longitude
of Lj specifying the framing. Let U = U(Lj) be a tubular neighbourhooh of Lj in W, and l ⊂∂U be
a non separating simple closed curve. Let W(l) be obtained from W by the Dehn ﬁlling of W \ Int(U)
along l. Denote by l∗the core of the attached solid torus.
Theorem 6.6. [Closed manifold surgery formula] Assume that ρ(l) = id ∈PSL(2, C) and the weight
k satisﬁes k([l]) = 0. Denote: ρ′ the natural extension of ρ|W\U to W(l); eLF = LF \ Lj; k′ the
restriction of k to W(l). We have
(20)
HN(W, LF, L0, ρ, 0, k) =N HN(W(l), eLF, L0 ∪l∗∪¯λj, ρ′, 0, k′) .
If moreover ρ is not trivial at the meridians of LF and l is a longitude of ∂U, then
32
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
(21)
He
N(W, LF, L0, ρ, 0, k) =N He
N(W(l), eLF, L0 ∪l∗∪L′
j, ρ′, 0, k′) .
Let us assume now that L0 is made by r parallel copies of Lj along the ribbon LF that encodes the
framing. So denote L0 by λr; with this notation, ¯λ = λ2. Assume furthemore that l = m is a meridian
of Lj, so that l∗= Lj. By appling inductively both (20) and Proposition 6.1 to this situation we get
Corollary 6.7. For every r ≥2 we have
HN(W, λr, ρ) =N HN(W, λ2, ρ) .
Remarks 6.8. (1) Though disjoint and complementary by hypothesis, formula (21) is formally the
same as that of Proposition 6.1, when replacing l by m.
(2) Assume (for simplicity) that L = LF. When l is a longitude of Lj, l∗inherits a natural framing
in W(l). Hence we get a triple (W(l), ˆL ˆ
F, ρ). It follows from the very deﬁnition of the QHFT tensors
that HN(W, LF, ρ, 0, 0) = HN(W(l), ˆL ˆ
F, ρ, 0, 0) and the same with He
N (when deﬁned) replacing HN.
(3) We have seen that both HN and He
N partitions functions display interesting features of QHG. A
main advantage of the HN ones is the possibility to set in a same “holomorphic family” the QHG
tensors associated to characters that are both trivial and non trivial at link meridians.
Consider
for example a hyperbolic knot L in S3, endowed with the canonical framing F. Kashaev’s volume
conjecture concerns the asymptotic behaviour of HN(S3, L, ρtriv) when N →+∞.
A reasonable
variant of it is in terms of the partition functions HN(S3, LF, ρtriv, 0, 0) =N HN(S3, ¯λ, ρtriv).
A
family as above could be useful in order to establish connections with the HN partition functions of
(S3, LF, ρhyp), where ρhyp is the hyperbolic holonomy of the cusped manifold M = S3 \ L.
The rest of the section is devoted to the proof of these results. This goes in several steps.
A main tool is the simplicial blowing up/down procedure considered by Neumann in [25], section 11.
We use it just to get a simplicial version of (topological) Dehn ﬁlling. Let Z be a pseudo manifold
without boundary such that every non-manifold point has toric link. Let v be a non-manifold point.
Consider a closed cone neighborhood N(v) of v, and a non separating simple closed curve C on the
torus ∂N(v). The topological Dehn ﬁlling of Z at v along C is the pseudo manifold Z′ obtained by
gluing a 2-handle to Z \ Int(N(v)) along C, and then collapsing to one point the resulting boundary
component.
Now, let T be a pseudo manifold triangulation of Z. Consider the abstract star Star0(v) of v in T .
The boundary of Star0(v) is the abstract link Link(v) which is homeomorphic to ∂N(v). Assume that
the curve C is realized as a simplicial curve on Link(v). Then the cone from v over C in Star0(v)
is a triangulated disk D0. The interior of Star0(v) embeds onto the interior of the actual star of v
in T , Star(v), which is made of the union of the 3-simplices having v as a vertex. In this way D0
maps onto a triangulated singular disk D in Z, that has embedded interior and singular boundary
immersed in the boundary of Star(v). Cut open T along Int(D) and glue the double cone CD of D
(this is a triangulated singular 3-ball, see Figure 14) so that the top and the bottom get identiﬁed with
the two copies of D resulting from slicing. This gives a triangulation T ′ of the pseudo-manifold Z′
obtained by Dehn ﬁlling along C. It has the property that every (abstract) tetrahedron of T persists
in T ′. Referring to the topological description, the interior of the co-core of the 2-handle attached to
Z \ Int(N(v)) is isotopic to the interior of the union H′ of two edges, each joining v to the new vertex
v′ at the “center” of CD. In fact H′ is the core of the solid torus added by the Dehn ﬁlling.
Remark 6.9. Note that in general there are very few simplicial curves on a given Link(v). Hence
to get such a simplicial description of an arbitrary Dehn ﬁlling, we will usually have to modify a
given triangulation. For the peculiar QHG pseudo-manifold triangulations considered in this section,
retriangulating will be possible by using QHG isomorphisms, hence without altering the trace tensors.
In fact, any two triangulations of ∂N(v) are connected by a ﬁnite sequence of 2-dimensional 1 ↔1
“ﬂip” moves (see Figure 6), and 1 ↔3 moves obtained by replacing a 2-simplex with the cone of its
boundary to a point. Since N(v) is homeomorphic to Link(v), any such a sequence is the boundary
trace of a sequence of 2 ↔3 moves and bubble moves in Star(v). (Note, in particular, that H passes
QUANTUM HYPERBOLIC GEOMETRY
33
through the new interior vertices). By using the arguments of Theorem 6.8 in [5], we will always be
able to choose that sequence so that it lifts to a sequence of QHG transits.
D
C
v’
v
v
Figure 14.
An instance of double cone on a disc.
Let us consider now a distinguished triangulation (T, H) of (Z, a) as above, and let Z′, triangulated
by T ′, be the result of a simplicial Dehn ﬁlling of Z along a curve C. Denote H′′ the graph union of
the knot H′ (the core of the solid torus) and the image of H in T ′. We deﬁne the notion of global
charge on (T ′, H′′) by formally replacing H by H′′ in (19).
Lemma 6.10. Let c be a global charge on (T, H) such that the charge weight of the curve C is 0.
Then c extends to a global charge c′ on (T ′, H′).
Proof. The complex CD is made of pairs of adjacent 3-simplices, respectively above and below the
disk D. For a 3-simplex of the top layer with charges c0 and c1 at the edges in D (ordered by using
an orientation of D, say), we will put the charges −c0 and 2 −c1 at these edges for the symmetric
3-simplex in the bottom layer. Then the other charges are c2 = 1 −c0 −c1 and −c2, respectively. We
have the charge sum CT ′(e) = 2 at each interior edge of D, and CT ′(e) = CT (e) at the edges e of ∂D.
For the top edges e′ of CD we can also choose the charges so that CT ′(e′) equals CT (e), where e is
the copy of e′ in D ⊂M. Indeed, there are n degrees of freedom in doing this, where n is the number
of 1-simplices in the curve C used for blowing down. Then we check that CT ′(e′) = 2 at the bottom
edges. In particular, the subcomplex H survives in T ′.
Note that CT ′(e0) = −CT ′(e1) at the edges e0 and e1 of H′. We have to check that CT ′(e0) = 0,
so that (13) is satisﬁed on (T ′, H′′ \ l). In fact, CT ′(e0) is n minus the sum of the 2n charges at
the bottom edges of CD, which is also the sum of charges in T ′ \ CD at these edges, minus n. We
can form n pairs of such charges corresponding to the 3-simplices of the ideal triangulation T of M
having a 2-simplex in D. Replacing for each of them the pair with 1 minus the last charge, we get
that CT ′(e0) is equal to γ(a), with γ deﬁned in section 2 and a is a normal path in Link(v) that runs
parallel to C on one side (see Figure 15). Because the weight of C is zero, we deduce CT ′(e0) = 0.
If H̸ = ∅, we have to show that it can be deleted from H′′. As the two components l and H \ l are
isotopic and satisfy CT ′(l) = 4 and CT ′(e) = 0 for each edge e ∈H\l, we can retriangulate the surgered
pseudo-manifold Z′ so as to delete them, by using a sequence of charge transits starting from (T ′, H′′)
and terminating with a negative bubble move (see [4], Proposition 4.27 and [5], proof of Theorem
6.8). Retriangulating Z′ backward, we eventually ﬁnd a sequence of charge transits terminating at
(T ′, H′, c′). The result follows.
✷
Proof of Theorem 6.3. To simplify assume that M has only one cusp. Take T ′′ = (T, H, b, w′, f ′′, c).
For the ﬁrst claim we assume that the meridian m of L is a simplicial path in Link(v), where the
vertex v of T corresponds to the ﬁlled cusp. This is possible due to Remark 6.9.
Lemma 6.10 implies that c′ extends to (T ′, H′) after the Dehn ﬁlling along m. Extend the branching
b by letting the new vertex v′ be a pit of the double cone CD we splice in T . By using Lemma 6.2,
arguments similar to that of Lemma 6.10 show that we can give the same log-branches on the 3-
simplices of CD, in a pair above and below the disk D (see [25], p. 454). Hence we get a distinguished
34
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
D
v
a
C
Figure 15.
A normal path a in Link(v) running parallel to a blowing-up curve C.
Four 3-simplices of T ′ \ CD glued to three 2-simplices of D are shown in the picture.
ﬂat/charged I-triangulation for (W, L, ρ). The weight h ∈H1(W; Z/2Z) is clearly 0 because of the
epimorphism H1(M; Z/2Z) →H1(W; Z/2Z) induced by inclusion. As in the ﬁrst claim of Lemma
5.10 (2) we see that the (unnormalized) trace tensor for CD is N times the identity map from the
linear space attached to the top copy of D to that for the bottom one. Combining this with the
normalization of trace tensors in (11) gives HN(W, L, ρ) = HN(T ′′).
By Lemma 6.2 we know that γ(f ′′) −γ(f ′) ∈H1(∂M; Zπ
√
−1) is non zero only at the class of m,
where it is −2
√
−1π. Hence the collection of values of f ′′ −f ′ determines a path l normal to the
cusp triangulation induced by T , that intersects m once and whose homology class is Poincar´e dual
to (γ(f ′′) −γ(f ′))/2
√
−1π. Denote
∆(lj) = (∆1, . . . , ∆|∆(lj)|)
the sequence of ﬂat/charged I-tetrahedra (possibly with repetitions) determined by the 2-simplices
met by l. Each time l goes through a 2-simplex it selects one of its vertices, whence a cross-ratio
modulus, say zi, of the tetrahedron ∆i corresponding to the 2-simplex. The values of f ′′ on ∆i are
obtained from those of f ′ by adding or substracting 1 at the edges corresponding to the other two
vertices, as indicated in Fig.
16.
For any ﬁxed tetrahedron ∆of T all three ﬂattenings may be
eventually altered, and/or diﬀer from those of f ′ by adding or substrating ni ∈Z with ni̸ = −1 or 1,
exactly when ∆= ∆i = ∆j for some i̸ = j. Now, recall from (11) that
HN(M, a) = HN(T ′) =
s
Y
∆⊂T
RN(∆, b, w, f, c)s.
Put ζ = exp(2π
√
−1/N). For any x ∈C\{ζj, j = 1, . . . , N −1} the function g deﬁned in the Appendix
satisﬁes ([5], Lemma 8.2):
g(xζk) = g(x)
k
Y
j=1
(1 −xN)1/N
1 −xζj
.
Using this formula, it is easily checked that given a ﬂat/charged I-tetrahedron (∆, b, w′, f ′, c) with
f ′ = (f ′
0, f ′
1, f ′
2) and positive branching orientation, if f ′′ = (f ′
0 + n, f ′
1, f ′
2 −n) we have
(22)
RN(∆, b, w′, f ′′, c)s = RN(∆, b, w′, f ′, c)s
n
Y
j=1
(w′
1)−1
1 −w′
0ζi−k+j
up to multiplication by Nth roots of unity, where i and k are as in (6). For each 2-simplex met by l
we can apply (22) to the corresponding tetrahedron, or the similar formula (deduced from Corollary
5.6 of [5]) for any other branching. This deﬁnes the function ΛN(T ′′), so that we get
HN(T ′′)
=
X
s
Y
∆⊂T
RN(∆, b, w′, f ′′, c)s
=
X
s
Y
∆⊂T
RN(∆, b, w′, f ′, c)s ΛN(T ′′).
The conclusion follows from the equality HN(W, L, ρ) = HN(T ′′).
✷
QUANTUM HYPERBOLIC GEOMETRY
35
m
l
+
−
+
−
+
−
+
−
+
−
+
−
+
−
Figure 16.
Flat/charge corrections for a Dehn ﬁlling.
Proof of Theorem 6.6. Again for simplicity, assume that L is a knot (one component). We apply
the very same arguments as for the ﬁrst claim of Theorem 6.3. In particular, Lemma 6.10 applies
verbatim. Since ρ(l) is trivial, for an arbitrary ﬂattening the weight along l (computed in the ﬂattened
I-cusps) lies in Zπ
√
−1. Hence we can again use Theorem 2.12 to deduce the existence of ﬂattenings
with zero weight along l. Then we give the same log-branches on the 3-simplices of the singular 3-ball
CD, in a pair above and below the disk D (see [25], p. 454). Note that if we use D triangulations
leading to HN partition functions, then both parallel components L, L′ that make ¯λ survive in the
Hamiltonian subcomplex. If we can deal with He
N-ones, only the framing longitude L′ survives. Hence
we eventually get a distinguished ﬂat/charged I-triangulation for (W(l), l∗∪¯λ, ρ), or (W(l), l∗∪λ′, ρ)
respectively.
✷
