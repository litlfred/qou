---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-015-62-invariants-of-cusped-manifolds-and-surgery-fo
section_title: "Invariants of cusped manifolds and surgery formulas"
section_number: 6.2
pages: 29-40
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
manifold triangulations T used in [5] (see Deﬁnition 6.2 and Deﬁnition 6.3 in that paper) to deﬁne
the quantum hyperbolic invariant trace tensors HN (T ) for oriented cusped hyperbolic manifolds.
Let M be a cusped manifold. Denote Z the pseudo-manifold obtained by taking the one point
compactiﬁcation of each cusp of M . M admits a triangulation by positively embedded hyperbolic ideal
tetrahedra, possibly including some degenerate ones of null volume (ie. having real cross-ratios). Such
a triangulation can be obtained by subdividing the canonical Epstein- Penner cell decomposition of M .
This gives rise to triangulation (T0,z 0) ofZ, wherez0 is the cross-ratio function of the abstract edges of
T , the imaginary part of every cross-ratio being ≥ 0. We call it a quasi-geometric ideal triangulation
of Z. If some quasi-geometric triangulation admits a global branching, w e say that M is gentle.
More generally, M is said weakly-gentle if there is an I-triangulation (T,b,w ) of Z such that (T,z ),
z =w∗b , is obtained via a (possibly empty) ﬁnite sequence ( T0,z 0) →... → (Ti,zi) →... → (T,z ) of
30 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
positive 2 → 3 transits, where ( T0,z 0) is a quasi-geometric triangulation of Z as above. Each transit
(Ti,zi) → (Ti+1,zi+1) is deﬁned by WTi (e) = WTi+1 (e), with all exponents ∗b = 1 (see (7)). Every
such a (T,b,w ) can be enhanced to ﬂat/charged I-triangulations T = (T,b,w,f,c ).
Given (T0,z 0), it is certainly possible to get an I-triangulation (T,b,w ) by performing also some
bubble moves (hence introducing new interior vertices). The autho rs do not know any example of
non weakly-gentle cusped manifold, that is, such that we are force d to do it. Anyway, dealing with
bubble moves is a technical diﬃculty which will appear also in the proof o f Theorem 6.3 (1) below.
We overcome it as follows. We ﬁx an edge a of the canonical Epstein-Penner cell decomposition of
M , and take A made by two copies of a that intersect at non manifold points of Z; the second copy
runs parallel to a within an open cell of the decomposition. Hence, A is a circle covered by two arcs.
We need to enlarge the notions introduced in Deﬁnition 2.10. We say th at (T,H ) is a distinguished
triangulation of (Z,a ) if H is a subcomplex of the 1-skeleton of T isotopic to A, that contains all the
regular vertices of T , and such that one arc of A is covered by an edge l of H. We say that c is a
global charge on (T,H ) if
(19) CT (e) =



4
0
2
if e =l
if e ⊂H \l
if e ⊂T \H
If H = ∅ this reduces to the usual notion of global charge on a closed triang ulated pseudo manifold
whose non manifold points have toric links. By using bubble moves and t he existence of such usual
global charges, it is easily seen that ( T,H ) supports global charges as in (19) (see the proof of Theorem
6.8 in [5] for the details).
We say that T = (T,H,b,w,f,c ) is a ﬂat/charged I-triangulation of (Z,a ) if (T,H,b,c ) is a branched,
charged and distinguished triangulation of ( Z,a ), and ( T,z ), z = w∗b , is obtained from a quasi
geometric (T0,z 0) via a ﬁnite sequence ( T0,z 0) →... → (T,z ) of transits supported by positive 2 → 3
moves and bubble moves . By setting a = ∅ and H = ∅, this deﬁnition incorporates that for the
weakly-gentle case.
In [5] it is shown that ﬂat/charged I-triangulations T of (Z,a ) (with arbitrary weights) do exist and
that, for every odd N ≥ 1,
HN (M,a ) = HN (T )
is a well deﬁned invariant of ( M,a ), providing the weights of ﬂat/charges to be 0. To simplify the
exposition, below we continue with this normalization. When M is weakly-gentle we get invariants
HN (M ). In fact, as a by product of the following discussion, we will realize t hat HN (M,a ) does not
depend on the choice of a, so that HN (M ) is always well deﬁned (see Corollary 6.4).
Let us recall now a few facts related to hyperbolic Dehn ﬁlling (see [29], [6], [27]). A quasi geometric
triangulation (T0,z 0) as above corresponds to the complete structure of M . It can be deformed in a
complex variety of dimension equal to the number of cusps. If z′ is close enough to z0, (T0,z ′) is a
triangulation by (possibly negative - see [27]) embedded hyperbolic ide al tetrahedra in a non-complete
hyperbolic structure, say M ′, close to M . In some case the completion of M ′ gives rise to a compact
closed hyperbolic manifold W , topologically obtained by Dehn ﬁlling of the (truncated) cusps of M .
The core of each attached solid torus is a “short” simple closed geod esicLj ofW , so that we have the
(geodesic) link L = ∐
jLj. Moreover, there are sequences ( Wn,Ln) obtained in this way such that
the length of Ln goes to 0 when n → +∞. Hence ( Wn,Ln) converges to the cusped manifold M (in
a neat geometric sense). From now on we will consider small deforma tions z′ leading to such closed
completions.
As well as (T0,z 0) gives rise to a triangulation T = (T,H,b,w,f,c ) of (Z,a ),z′ close to z0 gives rise to
another ﬂat/charged I-triangulation T ′ = (T,H,b,w ′,f ′,c ), where w′ is close to w and the log-branch
associated to the global ﬂattening f ′ corresponds to a continuous deformation of the one for f .
Lemma 6.2. (See [25], p. 469) Let z′ be a small deformation of z0 producing (W,L ), and mj
be a meridian of each link component Lj. Then there exist ﬂattenings f ′′ for the deformed trian-
gulation (T,b,w ′) such that the weight γ(f ′′) associated to the collection of log-branches of T ′′ =
(T,H,b,w ′,f ′′,c ) satisﬁes γ(f ′′)(mj) = 0 for all j.
QUANTUM HYPERBOLIC GEOMETRY 31
Proof. The logarithm of the derivative of the holonomy of mj is 0 at the complete structure, but after
deformation it represents a full 2 π-rotation about Lj (see eg. [29] or [6]). Hence γ(f ′)(mj ) ∈ Z
√
−1π.
The result then follows from the comments after Theorem 2.12. ✷
An explicit construction of ﬂattenings f ′′ as in the lemma shall be recalled during the proof of theorem
6.3. Hence, we dispose of two ﬂat/charged I-triangulations of ( Z,a ), T ′ = (T,H,b,w ′,f ′,c ) and
T ′′ = (T,H,b,w ′,f ′′,c ), relative to a small deformation z′ of the complete structure z0 as above,
leading to respective trace tensors HN (T ′) and HN (T ′′). We can now state the main results of this
Section.
Theorem 6.3. [Cusped manifold surgery formula] Let (W,L ) be obtained by completion of a small
deformation z′ of z0, and T ′, T ′′ be associated triangulations. Denote by ρ the hyperbolic holonomy
of W . Then we have HN (W,L,ρ ) =N HN (T ′′). Moreover, associated to each cusp Cj of M there is
an explicitely known map Λj
N (T ′′) : {N − states of T } → C such that the following surgery formula
holds:
HN (W,L,ρ ) =N
∑
s
∏
∆ ⊂T
RN (∆ ,b,w ′,f ′,c )s
∏
j
Λj
N (T ′′)(s)
wheres runs over the N -states of T and RN (∆ ,b,w ′,f ′,c )s is the matrix dilogarithm entry determined
by s, for the tetrahedron with the continuously deformed struct ure.
Corollary 6.4. If {(Wn,Ln,ρn)} is a sequence of closed hyperbolic Dehn ﬁllings converging t o the
cusp manifold M , then for every arc a we have limnHN (Wn,Ln,ρn) =N HN (M,a ). Hence HN (M ) =
HN (M,a ) is always a well deﬁned invariant of M (beyond the weakly-gentle case).
Remarks 6.5. (1) Theorem 6.3 is the analog for N >1 of Theorems 14.7 and Theorem 14.5 in [25],
which describe surgery formulas for the volume, Vol( W ), and Chern-simons invariant, CS( W ), of W :
√
−1(Vol(W ) +
√
−1CS(W )) =
∑
∆ ⊂T
R(∆ ,b,w ′,f ′) − π√−1
2
∑
j
λ(Lj)
where R is given by (3) and λ(Lj ) is the complex length of Lj, that is, the logarithm of the dilation
factor of its holonomy, which is a loxodromic transformation of H3. The technical complications due
to the bubble moves disappear for N = 1.
(2) If M is gentle and has a geometric branched ideal triangulation ( T,b,w ) without degenerate
tetrahedra, then for each 3-simplex the ﬂattenings of T ′ for a suﬃciently small deformation are just
−∗b times integral charges. It follows from the proof of Theorem 6.3 th at the scissors congruence class
cIf c(W,L,ρ ) of [5], section 7, coincides with Neumann’s deformed scissors congr uence class ˆβ(M ′) in
[25], Theorem 14.7 (see also Remark 6.12 and Conjecture 7.9 in [5], wher e the undeformed ˆβ(M ) is
denoted cIf c(M )).
(3) In general there are small deformations z ofz0 leading to complete manifolds that are still cusped,
that is only some cusps of M have supported a hyperbolic Dehn ﬁlling. There are also sequences o f
such cusped manifolds Mn, with (short) geodesic links Ln, converging to M . Similarly to the fusion
of QHFT with QHFT 0 (see Section 5.3) we can deﬁne quantum hyperbolic invariants HN (Mn,Ln)
for which the natural extensions of Theorem 6.3 and Corollary 6.4 ho ld.
Let us consider now (W,L F,L 0,ρ ). Let Lj be a component of LF , ¯λj =Lj ∪L′
j,L′
j being the longitude
of Lj specifying the framing. Let U =U (Lj) be a tubular neighbourhooh of Lj inW , and l ⊂∂U be
a non separating simple closed curve. Let W (l) be obtained from W by the Dehn ﬁlling of W \ Int(U )
along l. Denote by l∗ the core of the attached solid torus.
Theorem 6.6. [Closed manifold surgery formula] Assume that ρ(l) = id ∈PSL (2, C) and the weight
k satisﬁes k([l]) = 0 . Denote: ρ′ the natural extension of ρ|W \U to W (l); ~LF = LF \Lj; k′ the
restriction of k to W (l). We have
(20) HN (W,L F,L 0,ρ, 0,k ) =N HN (W (l), ~LF,L 0 ∪l∗ ∪ ¯λj,ρ ′, 0,k ′) .
If moreover ρ is not trivial at the meridians of LF and l is a longitude of ∂U , then
32 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
(21) He
N (W,L F,L 0,ρ, 0,k ) =N He
N (W (l), ~LF,L 0 ∪l∗ ∪L′
j,ρ ′, 0,k ′) .
Let us assume now that L0 is made by r parallel copies of Lj along the ribbon LF that encodes the
framing. So denote L0 byλr; with this notation, ¯λ =λ2. Assume furthemore that l =m is a meridian
of Lj, so that l∗ =Lj. By appling inductively both (20) and Proposition 6.1 to this situation w e get
Corollary 6.7. For every r ≥ 2 we have
HN (W,λr,ρ ) =N HN (W,λ 2,ρ ) .
Remarks 6.8. (1) Though disjoint and complementary by hypothesis, formula (21 ) is formally the
same as that of Proposition 6.1, when replacing l bym.
(2) Assume (for simplicity) that L =LF . When l is a longitude of Lj, l∗ inherits a natural framing
inW (l). Hence we get a triple ( W (l), ˆL ˆF,ρ ). It follows from the very deﬁnition of the QHFT tensors
that HN (W,L F,ρ, 0, 0) = HN (W (l), ˆL ˆF,ρ, 0, 0) and the same with He
N (when deﬁned) replacing HN .
(3) We have seen that both HN and He
N partitions functions display interesting features of QHG. A
main advantage of the HN ones is the possibility to set in a same “holomorphic family” the QHG
tensors associated to characters that are both trivial and non t rivial at link meridians. Consider
for example a hyperbolic knot L in S3, endowed with the canonical framing F . Kashaev’s volume
conjecture concerns the asymptotic behaviour of HN (S3,L,ρ triv) when N → +∞. A reasonable
variant of it is in terms of the partition functions HN (S3,L F,ρ triv, 0, 0) = N HN (S3, ¯λ,ρ triv). A
family as above could be useful in order to establish connections with the HN partition functions of
(S3,L F,ρ hyp), where ρhyp is the hyperbolic holonomy of the cusped manifold M =S3 \L.
The rest of the section is devoted to the proof of these results. T his goes in several steps.
A main tool is the simplicial blowing up/down procedure considered by Neumann in [25], section 11.
We use it just to get a simplicial version of (topological) Dehn ﬁlling. Let Z be a pseudo manifold
without boundary such that every non-manifold point has toric link. Let v be a non-manifold point.
Consider a closed cone neighborhood N (v) of v, and a non separating simple closed curve C on the
torus ∂N (v). The topological Dehn ﬁlling of Z at v along C is the pseudo manifold Z ′ obtained by
gluing a 2-handle to Z \ Int(N (v)) along C, and then collapsing to one point the resulting boundary
component.
Now, let T be a pseudo manifold triangulation of Z. Consider the abstract star Star0(v) of v in T .
The boundary of Star 0(v) is the abstract link Link(v) which is homeomorphic to ∂N (v). Assume that
the curve C is realized as a simplicial curve on Link( v). Then the cone from v over C in Star 0(v)
is a triangulated disk D0. The interior of Star 0(v) embeds onto the interior of the actual star of v
in T , Star(v), which is made of the union of the 3-simplices having v as a vertex. In this way D0
maps onto a triangulated singular disk D in Z, that has embedded interior and singular boundary
immersed in the boundary of Star( v). Cut open T along Int(D) and glue the double cone CD of D
(this is a triangulated singular 3-ball, see Figure 14) so that the top a nd the bottom get identiﬁed with
the two copies of D resulting from slicing. This gives a triangulation T ′ of the pseudo-manifold Z ′
obtained by Dehn ﬁlling along C. It has the property that every (abstract) tetrahedron of T persists
in T ′. Referring to the topological description, the interior of the co-c ore of the 2-handle attached to
Z \ Int(N (v)) is isotopic to the interior of the union H ′ of two edges, each joining v to the new vertex
v′ at the “center” of CD. In fact H ′ is the core of the solid torus added by the Dehn ﬁlling.
Remark 6.9. Note that in general there are very few simplicial curves on a given L ink(v). Hence
to get such a simplicial description of an arbitrary Dehn ﬁlling, we will us ually have to modify a
given triangulation. For the peculiar QHG pseudo-manifold triangulat ions considered in this section,
retriangulating will be possible by using QHG isomorphisms, hence witho ut altering the trace tensors.
In fact, any two triangulations of ∂N (v) are connected by a ﬁnite sequence of 2-dimensional 1 ↔ 1
“ﬂip” moves (see Figure 6), and 1 ↔ 3 moves obtained by replacing a 2-simplex with the cone of its
boundary to a point. Since N (v) is homeomorphic to Link( v), any such a sequence is the boundary
trace of a sequence of 2 ↔ 3 moves and bubble moves in Star( v). (Note, in particular, that H passes
QUANTUM HYPERBOLIC GEOMETRY 33
through the new interior vertices). By using the arguments of The orem 6.8 in [5], we will always be
able to choose that sequence so that it lifts to a sequence of QHG tr ansits.
D
C
v’
v
v
Figure 14. An instance of double cone on a disc.
Let us consider now a distinguished triangulation ( T,H ) of (Z,a ) as above, and let Z ′, triangulated
byT ′, be the result of a simplicial Dehn ﬁlling of Z along a curve C. Denote H ′′ the graph union of
the knot H ′ (the core of the solid torus) and the image of H in T ′. We deﬁne the notion of global
charge on (T ′,H ′′) by formally replacing H byH ′′ in (19).
Lemma 6.10. Let c be a global charge on (T,H ) such that the charge weight of the curve C is 0.
Then c extends to a global charge c′ on (T ′,H ′).
Proof. The complex CD is made of pairs of adjacent 3-simplices, respectively above and belo w the
disk D. For a 3-simplex of the top layer with charges c0 and c1 at the edges in D (ordered by using
an orientation of D, say), we will put the charges −c0 and 2 −c1 at these edges for the symmetric
3-simplex in the bottom layer. Then the other charges are c2 = 1 −c0 −c1 and −c2, respectively. We
have the charge sum CT ′ (e) = 2 at each interior edge of D, and CT ′ (e) = CT (e) at the edges e of∂D.
For the top edges e′ of CD we can also choose the charges so that CT ′ (e′) equals CT (e), where e is
the copy of e′ inD ⊂M . Indeed, there are n degrees of freedom in doing this, where n is the number
of 1-simplices in the curve C used for blowing down. Then we check that CT ′ (e′) = 2 at the bottom
edges. In particular, the subcomplex H survives in T ′.
Note that CT ′ (e0) = −CT ′ (e1) at the edges e0 and e1 of H ′. We have to check that CT ′ (e0) = 0,
so that (13) is satisﬁed on ( T ′,H ′′ \l). In fact, CT ′ (e0) is n minus the sum of the 2 n charges at
the bottom edges of CD, which is also the sum of charges in T ′ \CD at these edges, minus n. We
can form n pairs of such charges corresponding to the 3-simplices of the ideal triangulation T of M
having a 2-simplex in D. Replacing for each of them the pair with 1 minus the last charge, we g et
thatCT ′ (e0) is equal to γ(a), with γ deﬁned in section 2 and a is a normal path in Link( v) that runs
parallel to C on one side (see Figure 15). Because the weight of C is zero, we deduce CT ′ (e0) = 0.
If H ⁄= ∅, we have to show that it can be deleted from H ′′. As the two components l and H \l are
isotopic and satisfy CT ′ (l) = 4 and CT ′ (e) = 0 for each edge e ∈H \l, we can retriangulate the surgered
pseudo-manifoldZ ′ so as to delete them, by using a sequence of charge transits start ing from (T ′,H ′′)
and terminating with a negative bubble move (see [4], Proposition 4.27 a nd [5], proof of Theorem
6.8). Retriangulating Z ′ backward, we eventually ﬁnd a sequence of charge transits termin ating at
(T ′,H ′,c ′). The result follows. ✷
Proof of Theorem 6.3. To simplify assume that M has only one cusp. Take T ′′ = (T,H,b,w ′,f ′′,c ).
For the ﬁrst claim we assume that the meridian m of L is a simplicial path in Link( v), where the
vertexv of T corresponds to the ﬁlled cusp. This is possible due to Remark 6.9.
Lemma 6.10 implies that c′ extends to (T ′,H ′) after the Dehn ﬁlling along m. Extend the branching
b by letting the new vertex v′ be a pit of the double cone CD we splice in T . By using Lemma 6.2,
arguments similar to that of Lemma 6.10 show that we can give the sam e log-branches on the 3-
simplices of CD, in a pair above and below the disk D (see [25], p. 454). Hence we get a distinguished
34 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
D
v
a
C
Figure 15. A normal path a in Link(v) running parallel to a blowing-up curve C.
Four 3-simplices of T ′ \CD glued to three 2-simplices of D are shown in the picture.
ﬂat/charged I-triangulation for ( W,L,ρ ). The weight h ∈ H 1(W ; Z/2Z) is clearly 0 because of the
epimorphism H1(M ; Z/2Z) → H1(W ; Z/2Z) induced by inclusion. As in the ﬁrst claim of Lemma
5.10 (2) we see that the (unnormalized) trace tensor for CD is N times the identity map from the
linear space attached to the top copy of D to that for the bottom one. Combining this with the
normalization of trace tensors in (11) gives HN (W,L,ρ ) = HN (T ′′).
By Lemma 6.2 we know that γ(f ′′) −γ(f ′) ∈ H 1(∂M ; Zπ
√
−1) is non zero only at the class of m,
where it is −2
√
−1π. Hence the collection of values of f ′′ −f ′ determines a path l normal to the
cusp triangulation induced by T , that intersects m once and whose homology class is Poincar´ e dual
to (γ(f ′′) −γ(f ′))/2
√
−1π. Denote
∆( lj ) = (∆ 1,..., ∆ |∆( lj)|)
the sequence of ﬂat/charged I-tetrahedra (possibly with repetitions) determined by the 2-simplic es
met by l. Each time l goes through a 2-simplex it selects one of its vertices, whence a cro ss-ratio
modulus, say zi, of the tetrahedron ∆ i corresponding to the 2-simplex. The values of f ′′ on ∆ i are
obtained from those of f ′ by adding or substracting 1 at the edges corresponding to the oth er two
vertices, as indicated in Fig. 16. For any ﬁxed tetrahedron ∆ of T all three ﬂattenings may be
eventually altered, and/or diﬀer from those of f ′ by adding or substrating ni ∈ Z with ni ⁄= −1 or 1,
exactly when ∆ = ∆ i = ∆ j for some i ⁄=j. Now, recall from (11) that
HN (M,a ) = HN (T ′) =
∑
s
∏
∆ ⊂T
RN (∆ ,b,w,f,c )s.
Putζ = exp(2π
√
−1/N). For any x ∈ C\{ζj,j = 1,...,N −1} the function g deﬁned in the Appendix
satisﬁes ([5], Lemma 8.2):
g(xζk) = g(x)
k∏
j=1
(1 −xN )1/N
1 −xζj .
Using this formula, it is easily checked that given a ﬂat/charged I-tetrahedron (∆ ,b,w ′,f ′,c ) with
f ′ = (f ′
0,f ′
1,f ′
2) and positive branching orientation, if f ′′ = (f ′
0 +n,f ′
1,f ′
2 −n) we have
(22) RN (∆ ,b,w ′,f ′′,c )s = RN (∆ ,b,w ′,f ′,c )s
n∏
j=1
(w′
1)−1
1 −w′
0ζi−k+j
up to multiplication by N th roots of unity, where i and k are as in (6). For each 2-simplex met by l
we can apply (22) to the corresponding tetrahedron, or the similar formula (deduced from Corollary
5.6 of [5]) for any other branching. This deﬁnes the function Λ N (T ′′), so that we get
HN (T ′′) =
∑
s
∏
∆ ⊂T
RN (∆ ,b,w ′,f ′′,c )s
=
∑
s
∏
∆ ⊂T
RN (∆ ,b,w ′,f ′,c )s ΛN (T ′′).
The conclusion follows from the equality HN (W,L,ρ ) = HN (T ′′). ✷
QUANTUM HYPERBOLIC GEOMETRY 35
m
l
+
−
+ −
+ −
+ −
+ −
+ − +
−
Figure 16. Flat/charge corrections for a Dehn ﬁlling.
Proof of Theorem 6.6. Again for simplicity, assume that L is a knot (one component). We apply
the very same arguments as for the ﬁrst claim of Theorem 6.3. In pa rticular, Lemma 6.10 applies
verbatim. Since ρ(l) is trivial, for an arbitrary ﬂattening the weight along l (computed in the ﬂattened
I-cusps) lies in Zπ
√
−1. Hence we can again use Theorem 2.12 to deduce the existence of ﬂ attenings
with zero weight along l. Then we give the same log-branches on the 3-simplices of the singula r 3-ball
CD, in a pair above and below the disk D (see [25], p. 454). Note that if we use D triangulations
leading to HN partition functions, then both parallel components L,L ′ that make ¯λ survive in the
Hamiltonian subcomplex. If we can deal with He
N -ones, only the framing longitude L′ survives. Hence
we eventually get a distinguished ﬂat/charged I-triangulation for (W (l),l ∗ ∪ ¯λ,ρ ), or (W (l),l ∗ ∪λ′,ρ )
respectively. ✷
6.3. Manifolds that ﬁber over S1 - Examples. Lemma 5.10 (3) gives a practical recipe to compute
the QHFT partition functions of mapping tori. A speciﬁc class of distin guished ﬂat/charged I-
triangulations of ( ˜W[ψ], ˜L[ψ],ρ ) is obtained by composing one for the trivial mapping cylinder F ×
[−1, 1], say Ttriv, with the monodromy action on the e-triangulation (T,b ) of F × {1}, and then gluing
the two boundary components. The monodromy action can always b e decomposed as a sequence of
ﬂip moves: a single ﬂip on the ideal triangulation T ′ associated to T deﬁnes a ﬂip on ( T,b ) if it is
not adjacent to a marked corner, and it lifts to sequences as in Figu re 17 otherwise. We view these
sequences as the result of gluing tetrahedra. Hence the monodro my action determines a branched
triangulated pseudo-manifold Ts. This can be completed with global charges, and, as for any ρ we are
free to choose the cocycle in Ttriv, we can also complete Ts to a ﬂattened I-triangulation. Equivalently
we can deﬁne a sequence
(23) s : (T,b, L) →... →ψ(T,b, L)
of e-triangulations with (+)-Log- I-parameters compatible with ρ. Note that the edges of the as-
sociated pattern Ts of ﬂat/charged I-tetrahedra are disjoint from the Hamiltonian link H. Since
HN (Ttriv) =N id, we deduce that HN ( ˜W[ψ], ˜L[ψ],ρ ) =N HN (Ts).
Figure 17. Lifts to e-triangulations (economic ones - see Remark 3.12 - at the ﬁrst
row) of ﬂip moves on the corresponding ideal triangulations near ma rked corners.
The tetrahedron associated to the ﬁrst ﬂip (ﬁrst and third ones f or the second row)
degenerates for a sequence s with ( −)-Log-I-parameters.
Using a similar construction we now prove the relationship with the qua ntum hyperbolic invariants
HN of ﬁbered cusped manifolds [5]. Recall that W \L is homeomorphic to Int( ˜W[ψ]). Denote by l
the number of components of L.
36 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Proposition 6.11. If Int( ˜W[ψ]) supports a (necessarily unique) complete hyperbolic struc ture with
holonomy ρc, then HN ( ˜W[ψ], ˜L[ψ],ρc, 0, 0) =N N 2l HN (W \L).
Proof. Let S \V be the ﬁber of W \L →S1, equipped with an ideal triangulation T ′. First we show
the existence of sequences s : T ′ → ... → ψ(T ′) of ﬂip moves decomposing the monodromy action,
such that the associated pseudo-manifolds T ′
s are topological ideal triangulations of W \L, which
moreover have maximal volume.
The ﬁrst condition follows from the fact that the monodromy is homo topically aperiodic (ie. pseudo-
Anosov), so that T ′
s is genuinely three-dimensional. When S \V is a once-punctured torus, the
second condition is a consequence of a result of Lackenby [23], sho wing that the monodromy ideal
triangulation of Floyd and Hatcher [17] is isotopic to the canonical Epstein-Penne r cellulation. More
in general, since no edge of T ′
s is homotopically trivial, the results of [15] imply that we can straighten
the tetrahedra to oriented geodesic ones, possibly with overlappin gs, so that the algebraic sum of
volumes is Vol(W \L). This is known to be maximal [16].
As in Section 6.2 we can complete T ′
s to a ﬂat/charged I-triangulation T ′. Hence the invariants
HN (W \L) can be computed as trace tensors HN (T ′). We note that in the case when there are
several ﬁbrations of W \L, or T ′
s is not canonical, the invariance follows from Theorem 6.8 (2) in [5],
which shows that any two ﬂat/charged I-triangulations of W \L with maximal volume are QHG-
isomorphic.
Let us denote T ′
s the result of cutting T ′ along the ﬁber. The two boundary copies are marked
pleated hyperbolic surfaces (T ′,b ′, L) →S \V and (T ′,b ′, L) →ψ(S \V ), with shear-bend coordinates
(ie. ( −)-Log-I-parameters) L that determine completely the log-branches of T ′
s . Recall from Section
5.5 the families of ﬂat/charged I-triangulations Ft and F , and let C ∈ F , Ct ∈ Ft have boundary
structures (T,b, L), associated to ( T ′,b ′, L), and (T,b, Lt), respectively, at F × {1}. We have:
HN (T ′) = Tr( HN (T ′
s ))
= N −2l Tr
(
HN (T ′
s ) ⊗ id⊗2l
)
= N −2l Tr
(
HN (C) ◦ (HN (T ′
s ) ⊗ id⊗2l) ◦ HN (ψ(C))−1
)
= N −2l lim
t→id
Tr
(
HN (Ct) ◦ (HN (T ′
s,t) ⊗ id⊗2l) ◦ HN (ψ(Ct))−1
)
= N −2l lim
t→id
Tr(HN (Ct ∗ T ′
s,t ∗ (−ψ(Ct)))).
Here we use the invertibility of HN (C) (Proposition 5.12) and the equality HN (C) =N HN (ψ(C)).
We deﬁne T ′
s,t as the continuous deformation of T ′
s obtained from the sequence
st : (T,b, Lt) →... →ψ(T,b, Lt)
similarly as in (23) (see also Figure 17). In the last equality, Ct ∗ T ′
s,t ∗ (−ψ(Ct)) is for any ﬁxed t a
distinguished ﬂat/charged I-triangulation of the mapping cylinder of ψ. Hence HN (Ct∗T ′
s,t∗(−ψ(Ct)))
does not depend on t up to conjugacy, and we conclude with Lemma 5.10 (3). ✷
By following the above computation backwards, we see more in gener al that for any PSL (2, C)-
character ρ that can be realized by ( −)-Log-I-parameters on some ideal triangulation of the ﬁber
S \V , we have
(24) HN ( ˜W[ψ], ˜L[ψ],ρ,h,k ) = N 2l Tr(HN (T ′
s ))
where T ′
s is a pattern of ﬂat/charged I-tetrahedra associated to a sequence similar to (23), but with
e-triangulations equipped with ( −)-Log-I-parameters compatible with ρ.
Remark 6.12. The formula HN (W \L) = Tr(HN (T ′
s )) expresses the quantum hyperbolic invariants
of ﬁbered cusped manifolds as amplitudes between two markings of t he ﬁber, identiﬁed with a pleated
hyperbolic surface. For a similar construction based on represent ations of quantum Teichmuller spaces,
see [9].
Example: the ﬁgure-eight knot complement Here we compute the QHFT partition functions
of (S3,K 0), where K0 is the 0-framed ﬁgure-eight knot in S3. Recall that S3 \K is ﬁbered over
S1, with ﬁber the once-punctured torus Σ 1,1; the 0-framing of K is induced by the ﬁbration. For
QUANTUM HYPERBOLIC GEOMETRY 37
simplicity, below we consider only characters ρ of injective representations π1(S3 \K) →PSL (2, C).
The restriction to Σ 1,1 of such representations can be realized by ( −)-Log-I-parameters on any ideal
triangulation of Σ 1,1, so that, by (24), we can determine the corresponding subspace (still denoted
Def (S3,K )) of the phase space of Deﬁnition 5.8 by using the monodromy ideal t riangulation.
The monodromy Φ : Σ 1,1 → Σ 1,1 of S3 \K is isotopic to the hyperbolic element
( 2 1
1 1
)
=
( 1 1
0 1
) ( 1 0
1 1
)
∈SL(2, Z).
This description of [Φ] ∈ Mod(Σ 1,1) can be understood in terms of the Diagram of PSL (2, Z) (see eg.
[17]) via the action of Φ on topological ideal triangulations of Σ 1,1, which can be represented by two
ﬂip moves. See Figure 18, where the left picture is a lift to R2 \ Z2 of such a triangulation.
B
A
C BA
D
Figure 18. The composition of ﬂip transformations for the monodromy of S3 \K.
The monodromy ideal triangulation T ofS3 \K is obtained by realizing each ﬂip move via the gluing of
an ideal tetrahedron, ﬁrst on a ﬁxed triangulation of Σ 1,1, then on the resulting one. The remaining
four free faces are identiﬁed under Φ. It is not diﬃcult to see that T is isotopic to the canonical
geodesic ideal triangulation of S3 \K with its complete hyperbolic structure. The gluing pattern of
the tetrahedra in T is shown in Figure 19.
A B
D
A
B D
C
C
Figure 19. The face and edge identiﬁcations for the canonical geodesic ideal t rian-
gulation of S3 \K.
It is well-known (see [29]) that the deformation space of smooth (no n necessarily complete) hyperbolic
structures on S3 \K is isomorphic to the algebraic set Defhyp(S3 \K) ⊂ H2 × H2 of points (w2,z 0)
such that
w2 ∈ H2 \
{ 1
2 + t
2i |t ≥
√
15
}
, z 0 = 1
2 +
( 1
4 + 1
w2(w2 − 1)
) 1
2
where w2 is the cross-ratio modulus of the edge e2 in the tetrahedron ∆ + with positive branching
orientation (back edge in the left tetrahedron of Figure 19), and s imilarly for z0 in ∆ −. The space
Defhyp(S3 \K) is a subspace of
(25) C = {(w2,z 0) ∈ (C \ {0, 1})2 |w1w2
2z−2
0 z−1
1 = 1},
which is isomorphic to the whole set of solutions of the edge compatibilit y relations for cross-ratio
moduli (see Deﬁnition 2.6). By an easy computation we ﬁnd that the e dge compatibility relations for
log-branches and charges are:
(26) ( S)
{ f −
1 + 2f −
0 + 2f +
0 +f +
1 = (arg(w1) + 2 arg(w2) − arg(z1) − 2 arg(z0)) − 2∗+
c−
1 + 2c−
0 + 2c+
0 +c+
1 = 0
38 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
where ∗+ is the sign of the imaginary part of the wi, and the ﬂattenings f +
i and f −
i correspond to
the cross-ratio moduli wi and zi of ∆ + and ∆ −, respectively. Hence, by (2) we see that the QHFT
phase space Def (S3,K ) is the covering of C given by
Def (S3,K ) = {((w2;f +
2 −c+
2,f +
0 −c+
0 ), (z0;f −
0 +c−
0,f −
1 +c−
1 )) ∈ ˆC× ˆC | (w2,z 0) ∈ C, (S) is satisﬁed }.
Let us point out some geometrically meaningful subspaces (compar e with [25], Section 15). The
dilation factors of the standard meridian m and longitude l of K are
µ(m) = z2w−1
2 , µ (l) = z2
0z−2
2 .
The complete hyperbolic structure of S3 \K is obtained by solving µ(m) = 1 and µ(l) = 1 for points
of Defhyp(S3 \K), which gives zj = (wj )∗ = exp(iπ/3). We already noticed that the weights k for
this solution take values in 2 Z (see [25], Proposition 5.2). Corresponding ﬂattenings satisfy
(27) f −
2 −f +
2 =k(m), 2f −
0 − 2f −
2 =k(l)
and (26) simpliﬁes to
(28) f −
1 + 2f −
0 + 2f +
0 +f +
1 = 0.
Together with (27) this gives
(29) f +
1 = k(l)
2 − 1 − 2f +
0 ,



f −
0 =k(m) −f +
0
f −
1 = 2k(m) − k(l)
2 + 1 + 2f +
0
Similarly, integral charges are obtained by letting c+
i = −f +
i on ∆ + and c−
i = +f −
i on ∆ −. It can
be checked that h = 0. Of course, (29) is still true for points of Def (S3,K ) suﬃciently near the
complete solution, if now k(m) and k(l) are replaced with ˜k(m) = k(m) − log(µ(m))/
√
−1π and
˜k(l) = k(l) − log(µ(l))/
√
−1π. Hence, in the vicinity of the complete structure we have the strat a
{((w2; 2f +
0 − ˜k(l), 2f +
0 ), (z0; 2˜k(m) − 2f +
0 , 2(2˜k(m) + 1 + 2f +
0 ) − ˜k(l)), f+
0 ∈ Z},
parametrized by the lifts k(m) and k(l) of µ(m) and µ(l).
For points of C corresponding to hyperbolic structures whose metric completion is obtained fromS3\K
by (p,q ) Dehn ﬁlling, we have pµ(m) +qµ(l) = 2π
√
−1. Hence the ﬂattenings f =f ′′ of Lemma 6.2
are to satisfy
p(f −
2 −f +
2 ) +q(2f −
0 − 2f −
2 ) = −2
Let us ﬁx r, s ∈ Z such that ps −qr = 1. Solving simultaneously (28) and the last equation gives
(30) f +
1 =r − 1 − 2f +
0 ,
{
f −
0 = −2s −f +
0
f −
1 = −r + 4s + 1 + 2f +
0
The parity condition f +
0 +f +
1 +f −
0 +f −
1 ∈ 2Z (for the class h to be 0) is automatically satisﬁed.
Now we can compute the QHFT invariants of ( S3,K 0) as functions on Def (S3,K ). Given a N -state
s ofT , put α =s(ˆ
2), β =s(ˆ
0),γ =s(ˆ
3) and δ =s(ˆ
1), where ˆi denotes the face of ∆ + opposite to the
ith vertex. By 24) we have:
N −2HN (S3,K 0,ρ ) =
N −1∑
α,β,γ,δ =0
RN (∆ +,b +,w,f +,c +)γ,δ
α,β RN (∆ −,b −,z,f −,c −)δ,γ
β,α
=
N −1∑
α,β,γ,δ =0
(w
′−c+
1
0 w
′c+
0
1 )
N −1
2
g(w′
0)
g(1) ζγβ +(m+1)γ2
ω(w′
0,w ′−1
1 |α −γ) δ(α +β −δ)
×(z
′−c−
1
0 z
′c−
0
1 )
N −1
2
[z′
0]g(1)
g(z′
0) ζ−αδ−(m+1)δ2 δ(α +β −γ)
ω(z′
0/ζ,z ′−1
1 |β −δ)
= ( w′−c+
1
0 w′c+
0
1 z′−c−
1
0 z′c−
0
1 )
N −1
2
[z′
0]g(w′
0)
g(z′
0)
N −1∑
α,β=0
ζβ2−α2
ω(w′
0,w ′−1
1 |N −β) ω(z′
0/ζ,z ′−1
1 |N −α)−1.
QUANTUM HYPERBOLIC GEOMETRY 39
By the proof of Proposition 8.6 in [5] we have
[z′
0]g(w′
0)
g(z′
0) = g((z′
0)∗)∗g(w′
0)
|g(1)|2
and
ω(z′
0/ζ,z ′−1
1 |N −α)−1 =ω((z′
0)∗, (z′−1
1 )∗|α)∗
where z∗ is the complex conjugate of z. Thus, setting
S(w′
0,w ′
1) =
N −1∑
β=0
ζβ2
ω(w′
0,w ′−1
1 |β) = 1 +
N −1∑
β=1
ζβ2
β∏
k=1
w′−1
1
1 −w′
0ζk
we get
HN (S3,K 0,ρ ) = N 2(w′−c+
1
0 w′c+
0
1 z′−c−
1
0 z′c−
0
1 )
N −1
2
g((z′
0)∗)∗g(w′
0)
|g(1)|2 S(w′
0,w ′
1) S((z′
0)∗, (z′
1)∗)∗.
Using (29) with k(m) = k(l) = f +
0 = 0 and the global charge with c+
0 =c−
0 = 0, we see that for the
complete hyperbolic structure ρcomp on S3 \K we have
z′
0 = (w′
0)∗ = exp(iπ/3N ), z ′
1 = (w′
1)∗ = exp(−5iπ/3N ).
Hence
HN (S3,K 0,ρ comp) = N 2 |g(eiπ/3N )|2
|g(1)|2 |S(eiπ/3N,e −5iπ/3N )|2.
Let us ﬁnally consider hyperbolic (p,q ) Dehn ﬁlling of S3\K. Denote S3(K(p,q)) the surgered manifold,
L the core of the surgery, and ρ(p,q) its hyperbolic holonomy. Because of (30) the diﬀerence f ′′ −f
is given on the edges e0, e1 and e2 of ∆ + (resp. ∆ −) by 0, r and −r (resp. −2s, 4s and 0). Put
N = 2m + 1. From Theorem 6.3 we deduce
HN (S3(K(p,q)),L,ρ (p,q)) = N 2(w
′−c+
1
0 w
′c+
0
1 z
′−c−
1
0 z
′c−
0
1 )
N −1
2
g((z′
0)∗)∗g(w′
0)
|g(1)|2
N −1∑
α,β=0
ζβ2−α2
ω(w′
0,w ′−1
1 |N −β) ω((z′
0)∗, (z′−1
1 )∗|α)∗ ζr(N −β)(m+1)
N −2s∏
j=1
(z′−1
1 )∗ζ−4sα(m+1)
1 − (z′
0)∗ζj+α .
Remark 6.13. Recall the space C in (25). As already mentionned after Deﬁnition 2.6, we have
a holonomy map hol : C → X to the character variety X = X(π1(S3 \K)). (See [28] or [18] for
a complete description of the latter). The map hol is generically 2 : 1, and is onto the geometric
component of X [12]. We can express the above partition functions in terms of stand ard generators
of X by the following observation. Considering S3 \K as the mapping torus of the monodromy Φ,
the edges e0, e1 of ∆ + are identiﬁed with a longitude l and meridian m of the punctured torus Σ 1,1,
and in ∆ − we have (e′
0 is opposite to e0):
e0 = Φ(l.m), e 1 = Φ(l), e ′
0 = Φ(m).
As above, assume that ρ has non trivial holonomy at m,l andl.m. Take a ﬂat/charged I-triangulation
of (S3,K 0,ρ ) as in Section 6.3, with PSL (2, C)-valued cocycle z. Denote zl the value at l, and so
on. Note that zΦ(m) =AzmA−1, where A =z(S1), the cocycle value on the standard meridian of the
knot K. Then the cross ratio moduli of ∆ + and ∆ − are given by
w0 = [0 : zl(0) : zlzm(0) : zΦ(m)(0)], z 0 = [0 : zΦ(l)zΦ(m)(0) : zΦ(l)zΦ(m)zΦ(l)(0) : zmzl(0)].
(We use the branching to remove the twofold ambiguity of hol, as it allows to specify an equivariant
association of a ﬁxed point for each peripheral subgroup of ρ(π1(S3 \K)).)
Remark 6.14. Formulas for Cheeger-Chern-Simons invariants H1(S3,K 0,ρ ) of arbitrary PSL (2, C)-
characters of S3 \K come exactly in the same way (See Remark 1.1 and Remark 5.5). In the peculiar
situation of the complete hyperbolic structure and its hyperbolic De hn ﬁllings, they coincide with
those of [25], Section 15.
40 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
