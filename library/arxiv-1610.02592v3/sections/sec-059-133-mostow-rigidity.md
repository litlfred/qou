---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-059-133-mostow-rigidity
section_title: "Mostow rigidity"
section_number: 13.3
pages: 424-429
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
The ﬁrst addendum measures the positivet-simplices whose ﬁrst3 vertices
lie inD(g0(x0)),...,D (g2(x0)), the second measures the negativet-simplices
with the same requirement. These two subsets have the same volume inS(t)
because they are related by the involutionr : S(t) → S(t) that mirrors a
simplex with respect to its ﬁrst facet.
We show that for suﬃciently bigt the cycle is a positive multiple of[M].
Let t be suﬃciently big so that two vertices in at-simplex have distance
bigger than2d. This condition implies that if there is a positivet-simplex with
vertices inD(g0(x0)),...,D (g3(x0)), then any straight simplex with vertices
inD(g0(x0)),...,D (g3(x0)) is positive. Therefore in the expression
α(t) =
∑
σ∈Σ
λσ(t)·σ
the signs ofλσ(t) andσ are coherent and
∫
α(t)
ω =
∑
σ∈Σ
λσ(t)·
∫
σ
ω> 0.
Thereforeα(t) is a positive multiple of[M]. □
For suﬃciently bigt we haveα(t) =kt[M] in homology for somekt > 0.
The rescaled ¯α(t) = α(t)/kt hence represents [M]. We have found ourε-
eﬃcient cycles.
Lemma 13.2.18. For anyε > 0 there is at0 > 0 such that ¯α(t) is ε-
eﬃcient for allt >t0.
Proof. Letd be the diameter of the Dirichlet domainD(x0). Let aquasi
t-simplex be a simplex whose vertices are at distance< dfrom those of a
t-simplex. By construction ¯α(t) is a linear combination of quasit-simplices.
We now show that for anyε> 0 there is at0> 0 such that for allt >t0
every quasit-simplex has volume bigger thanv3−ε. By contradiction, let∆t
be a sequence of quasit-simplices of volume smaller thanv3−ε witht→∞ .
The vertices of∆t ared-closed to at-simplex ∆t
∗, and we move the pair∆t, ∆t
∗
isometrically so that thet-simplices ∆t
∗ have the same barycenter. Now both
the vertices of∆t and ∆t
∗ tend to the vertices of an ideal regular tetrahedron
and Exercise 13.2.15 gives a contradiction. □
The previous lemmas together prove the second half of Theorem 13.2.11.
Corollary 13.2.19.LetM be a closed hyperbolic3-manifold. We have
Vol(M)>v3‖M‖.
Theorem 13.2.11 has some non-trivial consequences.
Corollary13.2.20. LetM,N betwoclosedorientablehyperbolic 3-manifolds.
If there is a mapf :M→N of degreed then Vol(M)>|d|· Vol(N).
13.3. MOSTOW RIGIDITY 417
Corollary 13.2.21.Two homotopically equivalent and closed hyperbolic 3-
manifolds have the same volume.
Remark 13.2.22. If we are able to prove that the regular ideal simplex has
the maximum volumevn among hyperbolicn-simplices in Hn, then the whole
proof extends as is fromH3 to Hn and shows thatVol(M) = vn·|M| for any
closed hyperbolicn-manifold M. This is obviously true whenn = 2, and we
getv2 =π.
13.3. Mostow rigidity
13.3.1. Introduction. We want to prove the following.
Theorem 13.3.1 (Mostow rigidity).LetM andN be two closed connected
orientable hyperbolic 3-manifolds. Every isomorphismπ1(M) ∼→ π1(N) be-
tween fundamental groups is induced by a unique isometryM ∼→N.
This very powerful theorem says that an algebraic isomorphism between
fundamental groups alone is enough to produce and characterise an isometry.
Corollary 13.3.2. Two closed orientable hyperbolic 3-manifolds with iso-
morphic fundamental groups are isometric.
We prove Mostow’s rigidity in this section. All the ingredients are already
there, we only need to make a little last eﬀort.
We note that closed hyperbolic manifolds are aspherical because their
universal cover Hn is contractible. For such manifolds every isomorphism
π1(M)→π1(N) is induced by a homotopy equivalencef :M→N, unique up
to homotopy: see Corollary 1.7.7. To prove Mostow’s theorem we need to
promote this homotopy equivalence to an isometry in dimensionn = 3. We
already know thatVol(M) = Vol(N) by Corollary 13.2.21.
13.3.2. ProofofMostow’stheorem. Letf :M→N beasmoothhomo-
topy equivalence. Recall from Theorem 5.2.1 thatflifts to a map˜f : H3→ H3
whichextendscontinuouslytoahomeomorphism ˜f :∂H3→∂H3 ofthebound-
ary spheres. We start with a lemma.
Lemma 13.3.3. The extension ˜f :∂H3→∂H3 sends the vertices of every
regular ideal simplex to the vertices of some regular ideal simplex.
Proof. Letw0,...,w 3 be vertices of a regular ideal simplex and suppose
by contradiction that their images˜f (w0),..., ˜f (w3) span a non-regular ideal
simplex, which has volume smaller thanv3− 2δ for someδ >0. By Exercise
13.2.15 there are neighbourhoodsUi of wi in H3 for i = 0,..., 3 such that
the volume of the simplex with vertices˜f (u0),..., ˜f (u3) is smaller thanv3−δ
for any choice ofui∈Ui.
418 13. MOSTOW RIGIDITY THEOREM
In Section 13.2.6 we have deﬁned a cycle
α(t) =
∑
σ∈Σ
λσ(t)·σ
where t depends onε. We say that a singular simplexσ∈ Σ is bad if its
i-th vertex is contained inUi for alli. Let Σbad⊂ Σ be the subset of all bad
singular simplices and deﬁne
α(t)bad =
∑
σ∈Σbad
λσ(t)·σ.
We want to estimate|α(t)| and|α(t)bad|. We prove that
|α(t)| =
∑
σ∈Σ
|λσ(t)|
is a real number independent oft: letS0⊂S(t) be the set of allt-simplices
having the ﬁrst vertex in the Dirichlet domainD(x0) of the ﬁxed base point
x0∈ H3. It follows from the deﬁnitions that|α(t)| equals the measure ofS0
for suﬃciently bigt. Moreover the setS0 is in natural correspondence with
the set of all isometries that sendx0 to some point inD(x0): its volume does
not depend ont.
To estimate|α(t)bad| we ﬁxg0∈ Γ so thatD(g0x0)⊂ U0. Let Sbad⊂
S(t) be the set of all badt-simplices with ﬁrst vertex inD(g0x0). If t is
suﬃciently big, the volume ofSbad is bigger than a constant independent oft
(exercise).
We have proved that|α(t)bad|/|α(t)| > C >0 independently oft. We
may suppose thatα(t) represents [M] up to renormalising. The mapf :M→
N has degree±1 and it sendsα(t) to a class
f∗(α(t)) =
∑
σ∈Σ
λσ(t)· (f◦σ)st
representing±[N]. Since aC-portion ofα(t) is bad, aC-portion of simplices
inf∗(α(t)) has volume smaller thanv3−δ and hence
Vol(N) =
⏐⏐⏐⏐
∫
f∗(α(t))
ω
⏐⏐⏐⏐<|α(t)|((1−C)v3 +C(v3−δ)) =|α(t)|(v3−δC).
Since this holds for allt and|α(t)|→‖ M‖ we get
Vol(N)<‖M‖(v3−δC) = Vol(M)−δC·‖M‖.
Corollary 13.2.21 givesVol(M) = Vol(N), a contradiction. □
Proposition 13.3.4. Every ideal triangle inH3 is the face of precisely two
regular ideal tetrahedra.
Proof. Pick the linel orthogonal to the barycenter of the triangle: the
vertex of a regular ideal tetrahedron must be an endpoint ofl. To prove that
13.3. MOSTOW RIGIDITY 419
these vertices give regular ideal tetrahedra, note that all ideal triangles inH3
are isometric, so one concrete example suﬃces. □
We turn back to Mostow rigidity.
Proposition13.3.5. Letf :M→N beasmoothhomotopicequivalencebe-
tween closed hyperbolic orientable 3-manifolds. The restriction˜f|∂H3 :∂H3→
∂H3 is the trace of an isometryψ : H3→ H3.
Proof. Letv0,...,v 3∈∂Hn be vertices of a regular ideal tetrahedron∆.
By Lemma 13.3.3 the lift˜f sends them to the vertices of some regular ideal
tetrahedron, and letψ be the unique isometry ofH3 such thatψ(vi ) = ˜f (vi )
for alli.
ByProposition13.3.4thereisauniquepoint v4⁄=v3 suchthat v0,v 1,v 2,v 4
are the vertices of an ideal regular tetrahedron, andψ(v4) is the unique point
other thanψ(v3) such thatv0,v 1,v 2,ψ (v4) are the vertices of an ideal regular
tetrahedron. By Lemma 13.3.3 we also have˜f (v4) =ψ(v4).
If we mirror ∆ along its faces iteratively we get a tessellation ofH3 via
regular ideal tetrahedra, whose ideal vertices form a dense subset of∂H3. By
iterating this argument in all directions the functionsψ and ˜f coincide on this
dense subset and hence on the whole of∂H3. □
We can ﬁnally prove Mostow’s rigidity theorem.
Theorem 13.3.6 (Mostow Rigidity).Letf :M→N be a homotopic equiv-
alence between closed orientable hyperbolic 3-manifolds. The mapf is homo-
topically equivalent to an isometry.
Proof. SetM = H3/Γ andN = H3/Γ′, and pick a lift˜f. We have
(18) ˜f◦g =f∗(g)◦ ˜f ∀g∈ Γ
for an isomorphismf∗ : Γ → Γ′. We may supposef smooth. The boundary
extension of ˜f is the trace of an isometryψ : H3→ H3 and hence
(19) ψ◦g =f∗(g)◦ψ ∀g∈ Γ
holdsat ∂H3. Bothtermsin(19)areisometries, andisometriesaredetermined
by their boundary traces: hence (19) holds for all points inH3. Thereforeψ
descends to an isometry
ψ :M→N.
A homotopy betweenf andψ may be constructed from a convex combination
of ˜f andψ in Hn, which is alsoΓ-equivariant and hence descends. □
13.3.3. Consequences of Mostow rigidity.The most important con-
sequence is that the entire geometry of a closed hyperbolic3-manifold is a
topological invariant: numerical quantities like the volume of the manifold, its
geodesic spectrum, etc. depend only on the topology of the manifold. We
single out another application.
420 13. MOSTOW RIGIDITY THEOREM
Corollary 13.3.7.LetM be a closed orientable hyperbolic 3-manifold. The
natural map
Isom(M)→ Out(π1(M))
is an isomorphism.
Proof. We already know that it is injective by Proposition 4.3.6. We
prove that it is surjective: every automorphism ofπ1(M) is represented by a
homotopy equivalence sinceM is aspherical (see Corollary 1.7.7), which is in
turn homotopic to an isometry by Mostow’s rigidity. □
We note that this is false in dimensionn = 2, where Isom(S) is ﬁnite and
Out(π1(S)) is inﬁnite.
13.3.4. Orbifolds and cone manifolds.While by Mostow’s theorem an
orientable closed 3-manifoldM can have at most one hyperbolic structure, it
may have plenty of hyperbolic cone manifold or orbifold structures, typically
distinguished by their singular sets and their cone angles. For instanceM =S3
has plenty of such structures, as we will see.
For the moment we note that the volumes of these hyperbolic orbifold
structures may be arbitrarily big, but not arbitrarily small:
Proposition 13.3.8.Let a closed orientable 3-manifoldM be the underlying
space of a hyperbolic orbifoldO. We have
Vol(O)>v3‖M‖.
Proof. By Selberg’s Lemma there is a degree-d orbifold coveringN→O
which is a closed hyperbolic manifold. We haveVol(N) =dVol(O), and since
the covering is a degree-d map N→ M we can apply Corollary 13.2.20 and
get‖M‖⩽ ‖N‖
d = Vol(N)
dv 3
= Vol(O)
v3
. □
13.3.5. References. Most of the proofs presented in this chapter were
taken from Benedetti – Petronio [4], and are also contained in Thurson’s
notes [56]. The proof of Mostow’s rigidity presented here was proposed by
Gromov and applies to every dimensionn> 3, because ideal regular simplexes
have indeed the maximum volume by Haagerup and Munkholm [24].
CHAPTER 14
Hyperbolic three-manifolds
We have studied and classiﬁed the three-manifolds having seven of the
eight geometries, and we are now left with the most interesting ones: hyper-
bolic three-manifolds.
In dimension two every closed hyperbolic surface is constructed by gluing
some geodesic pair-of-pants. In dimension three, although closed hyperbolic
three-manifolds are everywhere, it is somehow harder to construct them ex-
plicitly: the most general procedure to determine a hyperbolic metric (if any)
on a given closed 3-manifold consists of solvingThurston’s equations.
Thurston’s equations arise naturally in the attempt of constructing a hy-
perbolic three-manifold by triangulating it into hyperbolic tetrahedra. The
most relevant and unexpected aspect of the theory is that it is much easier
to employ hyperbolicideal tetrahedra than compact ones. The combinatorial
framework in the ideal case is so convenient, that we use it also for closed
three-manifolds.
In this chapter we describe these equations and use them to determine
various ﬁnite-volume hyperbolic 3-manifolds. We start with the cusped case
and then turn to the slightly more complicate closed one.
