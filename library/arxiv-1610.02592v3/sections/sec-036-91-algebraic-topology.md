---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-036-91-algebraic-topology
section_title: "Algebraic topology"
section_number: 9.1
pages: 277-280
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
like products of numbers: every closed three-manifold splits in a unique way
in a unique list of prime factors. Finally we introduce the important notion of
incompressible surface.
9.1. Algebraic topology
The algebraic topology of compact three-manifolds is not very complicate.
9.1.1. Integral homology. In this section all the homology groups are
considered over Z. We ﬁrst note that, for closed orientable 3-manifolds, the
fundamental group determines everything.
Proposition 9.1.1.The homologyH∗(M) of a closed orientable 3-manifold
M is determined byπ1(M).
Proof. As in every path connected space, the groupH1(M) is the abelian-
isation ofπ1(M) and H1(M) = Hom(H1(M), Z), which is hence isomorphic
269
270 9. TOPOLOGY OF THREE-MANIFOLDS
to H1(M) modulo its torsion. By Poincaré duality H2(M) = H1(M) and
H2(M) =H1(M). FinallyH3(M) = Z. □
9.1.2. Homology spheres. A homology n-sphere is a closed orientable
n-manifold M whose homology is the same as that ofSn. That is, we have
H0(M) =Hn(M) = Z andHi (M) vanishes for all0<i <n.
By Poincaré duality, a closed 3-manifoldM is a homology sphere if and
only if H1(M) vanishes. Since H1(M) is the abelianization ofπ1(M), this
happens precisely whenπ1(M) is aperfect group, that is a group with trivial
abelianization.
In 1900 Poincaré conjectured that every homology 3-sphere should be
homeomorphic toS3. Four years later, he found himself a counterexample
by constructing what is known today asPoincaré’s homology sphere, a closed
3-manifold with a perfect fundamental group of order 120. He then modiﬁed
his original conjecture by asking whether every simply connected closed 3-
manifoldshouldbehomeomorphicto S3. Thisfact,widelyknownas Poincaré’s
Conjecture, was proved only in 2002 by Perelman.
We will construct Poincaré’s homology sphere (and many more homology
spheres) in Chapter 10, and we will discuss the Poincaré Conjecture in Section
12.9, as a part of Thurston’s widerGeometrisation Conjecture, also proved by
Perelman in 2002.
9.1.3. The boundary. The Euler characteristicχ(M) of a closed odd-
dimensional manifold vanishes, and on manifolds with boundary we have the
following.
Proposition 9.1.2. IfM is a compact 3-manifold with boundary, then
χ(M) = χ(∂M )
2 .
Proof. We only use thatM has odd dimension n. If M is closed and
orientable, we haveχ(M) =∑n
i=0(−1)ibi and the Betti numbersbi andbn−i
are equal by Poincaré duality, henceχ(M) = 0 . If M is non-orientable then
it has an orientable double-coverN and χ(N) = dχ(M) on degree-d covers,
henceχ(N) = 0 impliesχ(M) = 0. IfM has boundary then
0 =χ(DM) = 2χ(M)−χ(∂M )
where DM is thedouble of M, constructed by taking two identical copies of
M and identifying their boundaries in the obvious way. □
The manifoldM has half the Euler characteristic of∂M, and is also re-
sponsible for half of the ﬁrst homology group of∂M. More precisely, we are
interested in the boundary map
∂ :H2(M,∂M )−→H1(∂M )
9.1. ALGEBRAIC TOPOLOGY 271
and we want to prove that its image is a particular half-dimensional subgroup.
Recall from Proposition 1.7.16 that every class inH2(M,∂M ) is represented
by an oriented properly embedded surfaceΣ, and∂ sends [Σ] to [∂Σ].
LetM be oriented. The boundary∂M may be disconnected and inherits an
orientation. Recall thatH1(∂M )∼= Z2n for somen and H1(∂M ) is equipped
with a symplectic intersection formω, see Section 6.1.3. A subgroupL <
H1(∂M ) is lagrangian ifω|L≡ 0.
Exercise 9.1.3. IfL is lagrangian thenrkL⩽n.
When rkL =n we say thatL has maximal rank.
Proposition 9.1.4.LetM be an oriented compact 3-manifold with bound-
ary. The image of the map
∂ :H2(M,∂M, Z)−→H1(∂M, Z)
is a lagrangian subgroup ofH1(∂M, Z) of maximal rank.
Proof. Consider the long exact sequence
... −→H2(M,∂M ) ∂−→H1(∂M ) i∗
−→H1(M)−→...
We have two pairings
ω :H1(∂M )×H1(∂M )−→ Z,
η :H2(M,∂M )×H1(M)−→ Z.
The latter is provided by Lefschetz duality and is non-degenerate after quoti-
enting the torsion subgroups. We have
ω(∂α,β ) =η(α,i∗β)
for allα∈H2(M,∂M ) andβ∈H1(M): this equality can be proved easily by
representing the elements ofH2(M,∂M ) as surfaces (which we can do thanks
to Proposition 1.7.16). Now ifβ =∂α′ we get
ω(∂α,∂α′) =η(α,i∗∂α′) =η(α, 0) = 0
and henceIm∂ is lagrangian. It has maximal rank sinceH2(M,∂M ) =H1(M)
andH1(M) have the same rank: ifrk Im∂ <1
2b1(∂M ), then we getrk Imi∗>
1
2b1(∂M ) and rk ker∂ > b1(M)− 1
2b1(∂M ), a contradiction sinceImi∗ and
ker∂ areη-orthogonal. □
Corollary 9.1.5.LetM be an oriented compact 3-manifold. We have
b1(M)> b1(∂M )
2 .
Proof. The rank ofH1(M) equals that ofH1(M) =H2(M,∂M ). □
Corollary 9.1.6.The boundary of a simply connected compact 3-manifold
consists of spheres.
272 9. TOPOLOGY OF THREE-MANIFOLDS
9.1.4. Non-orientable surfaces. LetM be an orientable 3-manifold and
S⊂M be a connected surface. IfS is orientable, then by Proposition 1.1.12
every tubular neighbourhood forS is diﬀeomorphic to the productS× R.
The orientable manifoldM may also contain anon-orientable surfaceS:
for instance the orientable projective spaceRP3 contains the non-orientable
projective planeRP2. In that case a tubular neighbourhood ofS is diﬀeomor-
phic to the unique orientable interval bundleS×∼ R over S, see Proposition
1.1.12 again. A compact tubular neighbourhood ofS is an interval bundle
S×∼ I, whose boundary is the orientable double cover ofS. For instance, the
boundary of RP2×∼ I is a sphere.
A non-orientable properly embedded surfaceS ⊂ M does not deﬁne a
homology class in Z, but it deﬁnes one inZ2, that is [S]∈ H2(M,∂M ; Z2).
As opposite to orientable surfaces, this class[S] is always non-trivial.
Proposition 9.1.7. Let M be orientable. Every non-orientable surfaceS
determines a non-trivial class[S]∈H2(M,∂M ; Z2). The manifoldM cannot
contain more thandimH2(M,∂M ; Z2) disjoint non-orientable surfaces.
Proof. A tubular neighbourhoodS×∼ I ofS contains a simple closed loop
α intersectingS transversely in one point. The class[S]∈H2(M,∂M ; Z2) =
H1(M; Z2) sends α to 1∈ Z2 and is hence non-trivial. IfS =S1⊔... ⊔Sk
are all non-orientable, each Si has its own αi and therefore the elements
[S1],..., [Sk]∈H2(M,∂M ; Z2) are linearly independent. □
Corollary 9.1.8.A simply-connected three-manifold does not contain any
closed non-orientable surface.
