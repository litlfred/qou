---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-014-210-langlands-duality-and-ﬂat-connections
section_title: "Langlands duality and ﬂat connections"
section_number: 2.10
pages: 24-27
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Motivated by the results of this paper, combined with [22], we can make another conjecture:
Conjecture 2.3 Let G be a compact Lie group (not necessarily of ADE type) and LG its
Langlands dual. Then, under S-duality, the boundary condition Ba corresponding to a con-
nected component inMab
ﬂat(M3,G C) of GC ﬂat connections on a 3-manifold M3 maps to
Ba ↦→ LBa =
∑
b
abelian
Sab (Bb +
∑
c
non-abelian
nbcBc ) (2.67)
where Sab is the S-matrix as in Conjecture 2.1 and nbc are the transseries coeﬃcients from
[22].
In formulating this Conjecture, we used Ba (instead of a) to emphasize its role as a
boundary condition on ∂(D2×qS1) =T 2. The mapping class group SL(2, Z) of the 2-torus
acts on the boundary conditions and we claim that, at least for boundary conditions associated
with abelian ﬂat connections, the S-transformation is given by (2.67). Indeed, at the “far end”
of the cigar, the geometry of the ﬁvebrane world-volume looks like R×M3×T 2, and we can
ﬁrst reduce onT 2 to obtain 4dN = 4 super-Yang-Mills on R×M3. The mapping class group
of T 2 then becomes the S-duality group of 4d N = 4 SYM, in particular, exchanging G and
LG under the electric-magnetic duality.
When G is of Cartan type A or D, the left-hand side of ( 2.67) is the choice of boundary
condition we used in ( 2.24), whereas the right-hand side describes the boundary condition
that gives Ha[M3] and is used in most of the paper. Then, Conjecture 2.3 is basically a
statement that both sets of boundary conditions lead to integrality and are compatible.
2.11 3-manifolds and the “bottom row”
Using a relation between the physical realizations of 3-manifold homology and a HOMFLY-PT
homology, respectively, we can produce a purely mathematical relation between the familiar
knot homologies and less familiar 3-manifold homologies of this paper.
Namely, the familiar setup for homology of a knotK⊂S3 involvesQ-cohomology (space
of BPS states) of the following system:
doubly-graded
space-time: R×T∗S3×TN
N M5-branes: R× S3 × D2
M5′-branes: R× LK × D2
phase
←−−−−−−
transition
→
triply-graded
R×X× TN
M5′: R×LK×D2
(2.68)
whereLK is the conormal bundle of the knot K, andX is the resolved conifold, i.e. the total
space ofO(−1)⊕O (−1) bundle over CP1.
Note, on the triply-graded (“resolved”) side the original M5-branes disappear and we are
only left with a system of M5′-branes in a non-trivial Calabi-Yau backgroundX. This is very
– 23 –
similar to a physical realization of 3-manifold homology in ( 1.1) or ( 2.13) where, compared
to the right-hand side of ( 2.68), the Lagrangian 3-manifold M3 plays the role of LK. Indeed,
according to the McLean’s theorem, the neighborhood of the Lagrangian submanifoldLK⊂X
in (2.68) can be identiﬁed with the total space of the cotangent bundle,
N(LK) ∼= T∗LK (2.69)
which is precisely the setup of ( 2.13). There is an important diﬀerence, however.
While in ( 2.13) the Calabi-Yau space is simply the cotangent bundle to the Lagrangian
3-manifold M3, in ( 2.68) it only looks like T∗LK in the neighborhood of LK. Globally, the
topology of X is diﬀerent from T∗LK and, in particular, has non-trivial relative homology
group
H2(X,LK)∼= Z. (2.70)
It plays an important role in the physical realization of the colored HOMFLY-PT homology of
the knot K; namely, the conserved charge captured by this relative homology is the so-called
a-grading of the HOMFLY-PT homology of K.
As in [58], we can bridge the gap between the two systems ( 2.13) and ( 2.68) by taking
the limit24
log(a) = Vol(CP1)→∞. (2.71)
This limit has a simple interpretation in almost every duality frame. For example, from the
vantage point of the Calabi-Yau 3-fold X it corresponds to the limit
X ↝ C3 (2.72)
that, on the toric diagram of the resolved conifold X, corresponds to moving two trivalent
vertices far away from each other. Keeping only one vertex in sight, we end up with C3
(whose enumerative invariants are counted by the reﬁned topological vertex). After making
this replacement in ( 2.68), we obtain a simpler ﬁvebrane system, whose BPS spectrum ( Q-
cohomology) categoriﬁes only the bottom (resp. top) row of the HOMFLY-PT polynomial
that contains the terms with minimal (resp. maximal) a-degree [58].
Now, after taking the limit ( 2.71)–(2.72), the second cohomology of X is trivial and
there is no winding around CP1 that we had in the original system ( 2.68). This, of course,
corresponds to the fact that, by taking the limit, we lost the a-grading focusing only on terms
with the lowesta-degree. The q-degree andt-degree, however, are still present and come from
U(1)q×U(1)R symmetry acting on D2⊂TN .
To summarize, by taking the limit ( 2.71)–(2.72) in the physical system ( 2.68), we obtain
a relation between the bottom row of the HOMFLY-PT homology of K and the homology of
the 3-manifold M3 =LK:
Hbottom(K) ∼= H(M3). (2.73)
24Note, in relating HOMFLY-PT homology to sl(N) knot homology one sets a =qN, so that log(a)∼N.
– 24 –
Knot K Hbottom(K)
31 q−2 +q2t2
41 t−2
51 q−4 +t2 +q4t4
52 q−2 +t +q2t2
61 t−2 +q−2t−1
Table 1: The reduced Poincar´ e polynomial of the bottom row of the HOMFLY-PT homology for
simple knots colored by λ =□. The unreduced HOMFLY-PT homology is inﬁnite-dimensional and
its Poincar´ e “polynomial” is, in fact, a power series inq and t.
In fact, the geometry and topology of M3 = LK is closely related to that of the knot com-
plementS3\K, see [59]. Namely, for a knot (= a link with one component), both M3 =LK
andS3\K haveH1∼= Z. In particular, in both cases the abelian ﬂat connections are labeled
by C∗-valued holonomies x1,...,x N.
Note, (2.73) is a purely mathematical relation whose left-hand side is knot homology and
whose right-hand side is a 3-manifold homology. One can explore it and try to make it more
concrete, in particular using the physical setup ( 2.13) and (2.68). First, we need to develop a
more precise dictionary between the RHS and LHS of ( 2.73). Following the above derivation,
we see that the M5′-branes in (2.68) correspond to M5-branes in (2.13). Therefore, the sl(N)
homology of M3 =LK gets related to the bottom row of λ-colored HOMFLY-PT homology
ofK, whereλ is a partition with N rows (orN columns). Moreover, as in [15,57], we need to
relate the “partition basis” (natural on the LHS of ( 2.73)) to the “holonomy basis” (natural
on the RHS of ( 2.73)). And, ﬁnally, it is important to keep in mind that in relating the
physical systems ( 2.13) and ( 2.68) we obtain a relation ( 2.73) that involves unreduced knot
homology25 in the sense of [13].
As a warm-up, let us take a closer look at the simple case of N = 1 and λ =□. Recall,
that LK is a special Lagrangian submanifold in R6∼= C3. The moduli space M(LK) of its
Lagrangian deformations, together with a local system that it carries, is the space of SUSY
vacua of 3dN = 2 theory T [LK;U(1)] on a circle,
M(LK) ∼= MSUSY(T [LK;U(1)]) ∼= Mﬂat(LK,U (1)C), (2.74)
where in the last relation we used the McLean theorem. The cohomology of this moduli space
is precisely the bottom row of the HOMFLY-PT homology of K colored by λ =□ [60]:
Hbottom(K) ∼= H∗(M(LK)). (2.75)
25The reduced HOMFLY-PT homology categoriﬁes normalized HOMFLY-PT polynomial; it is ﬁnite-
dimensional for λ = □ and links with one component ( i.e. for knots). The unreduced version, on the
other hand, categoriﬁes unnormalized HOMFLY-PT polynomial and is inﬁnite-dimensional for any color λ.
The former has no obvious analogue for 3-manifolds.
– 25 –
In [61], the moduli space M(LK) is described as a cluster variety.
Another simple example is K = unknot and λ = Sr (or λ = Λr), a single-row Young
tableaux. The corresponding superpolynomial is
PSr
bottom(unknot) =
r∏
i=1
1
1−q2it2(i−1). (2.76)
These expressions can be found as xr-coeﬃcients of Zvortex(x;q,t ) for a single 3d N = 2
chiral multiplet. More generally, for K = unknot colored by Young diagrams with n rows
(or columns) we end up with the S1×D2 vortex partition function of n 3dN = 2 chiral
