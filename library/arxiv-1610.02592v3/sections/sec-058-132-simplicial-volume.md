---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-058-132-simplicial-volume
section_title: "Simplicial volume"
section_number: 13.2
pages: 418-424
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Gromov has introduced a topological invariant on closed manifolds of any
dimension called thesimplicial volume. This nice invariant can be used, among
other things, to prove Mostow’s rigidity theorem.
13.2.1. Deﬁnition.Gromov has introduced a measure of “volume” of a
closed manifoldM which makes use only of the homology ofM. Quite sur-
prisingly, this notion of volume coincides (up to a factor) with the Riemannian
one whenM is hyperbolic.
Consider a topological spaceX and its homology with ringR. We deﬁne
the norm of a cycleα =λ1α1 +... +λhαh as follows:
|α| =|λ1| +... +|λh|.
Deﬁnition 13.2.1. Thenorm of a classa∈Hk(X, R) is the inﬁmum of the
norms of its elements:
|a| = inf
{
|α|
⏐⏐α∈Zk(X, R), [α] =a
}
.
Recall that aseminorm on a real vector spaceV is a map|·| :V → R>0
such that
•| λv| =|λ||v| for any scalarλ∈ R and vectorv∈V,
•| v +w|⩽|v| +|w| for any pair of vectorsv,w ∈V.
Anormisaseminormwhere |v| = 0 impliesv = 0. Thefollowingisimmediate.
Proposition 13.2.2. The norm|·| induces a seminorm onHk(X, R).
Although it is only a seminorm, the function|·| is called a norm for
simplicity. Let now M be an oriented closed connected manifold: we know
thatHn(M, Z)∼= Z and the orientation ofM determines afundamental class
[M]∈Hn(M, Z) that generates the group. MoreoverHn(M, R)∼= R and there
is a natural inclusion
Z∼=Hn(M, Z)↪→Hn(M, R)∼= R
hence the fundamental class[M] is also an element ofHn(M, R) and has a
norm.
Deﬁnition 13.2.3. Thesimplicial volume‖M‖∈ R>0 of a closed oriented
connectedM is the norm of its fundamental class:
‖M‖ =|[M]|
Since|[M]| =|− [M]| the simplicial volume actually does not depend on
the orientation. WhenM is non-orientable we set‖M‖ =
‖‖ ˜M
‖‖/2 where ˜M is
the orientable double cover ofM. The deﬁnition of‖M‖ is relatively simple
but has various non-obvious consequences.
13.2. SIMPLICIAL VOLUME 411
13.2.2. Properties. A continuous mapf : M → N between closed ori-
ented n-manifolds induces a homomorphismf∗ : Hn(M, Z)→ Hn(N, Z), and
recall that thedegree off is the integerdegf such that
f∗([M]) = degf· [N].
Proposition 13.2.4. Let f :M→N be a continuous map between closed
oriented manifolds. The following inequality holds:
‖M‖>| degf|·‖ N‖.
Proof. Every description of[M] as a cycleλ1α1 +... +λhαh induces a
description off∗([M]) = deg f [N] as a cycleλ1f◦α1 +... +λhf◦αh with
the same norm (or less, if there is some cancelation). □
Corollary13.2.5. IfM andN areclosedorientableandhomotopicallyequiv-
alentn-manifolds then‖M‖ =‖N‖.
Proof. A homotopic equivalence consists of two mapsf : M → N and
g :N→M whose compositions are both homotopic to the identity. In partic-
ular bothf andg have degree±1. □
Corollary 13.2.6.IfM admits a continuous self-mapf :M→M of degree
at least two then‖M‖ = 0.
Corollary 13.2.7.Every sphereSn has norm zero. More generally we have
‖M×Sn‖ = 0 for every closedM and anyn> 1.
Proof. A sphereSn admits self-maps of degree> 2, and hence also the
productM×Sn does. □
Among the genus-g surfacesSg, we deduce that the sphere and the torus
have simplicial volume zero. We will see soon that every surface of genus
g> 2 has positive simplicial volume. When the continuous map is a covering
the inequality from Proposition 13.2.4 is promoted to an equality.
Proposition 13.2.8. Iff :M→N is a degree-d covering we have
‖M‖ =d·‖N‖.
Proof. Thereasonforthisequalityisthatcyclescanbeliftedandprojected
through the covering. More precisely, we already know that‖M‖>d·‖N‖.
Conversely, let α = λ1α1 +... +λhαh represent [N]; each αi is a map
∆n→ N. Since ∆n is simply connected, the mapαi lfts tod distinct maps
α1
i,...,α d
i : ∆n→N. Thechain ˜α =∑
ij λiαj
i isacyclein M andf∗( ˜α) =dα.
Hence‖M‖⩽d·‖N‖. □
We also note the following fact.
Proposition 13.2.9. IfM is triangulated withk simplices, then‖M‖⩽k.
412 13. MOSTOW RIGIDITY THEOREM
Proof. Up to taking a double cover we may suppose thatM is oriented.
The closedn-manifoldM is triangulated into some simplices∆1,..., ∆k, and
weﬁxanorientation-preservingparametrisation si : ∆→ ∆i ofeach. Wewould
like to say thats1 +... +sk is a fundamental cycle, however this singular chain
is not necessarily a cycle because the restriction to adjacent faces coincide
only up to the symmetriesSn+1 of ∆.
We can ﬁx this problem easily by averaging eachsi on all its permutations,
that is we substitute eachsi with 1
(n+1)!
∑
σ∈Sn+1(−1)sgn(σ)si◦σ. Now s =
s1 +... +sk is a fundamental cycle and|s| =k. □
13.2.3. Seifert manifolds. We can now calculate the simplicial volume
of Seifert manifolds.
Proposition 13.2.10. IfM is a closed Seifert 3-manifold then‖M‖ = 0.
Proof. Every Seifert manifold is ﬁnitely covered by a productS×S1 (if
e = 0) or by a bundle
(
S, (1, 1)
)
with Euler number 1 (ife⁄= 0). In the ﬁrst
case we are done since‖S×S1‖ = 0.
In the second, if S = S2 then
(
S2, (1, 1)
)
= S3 and ‖S3‖ = 0 , so
we suppose χ(S) ⩽ 0. There is a universal K > 0 such that
(
S, (1, 1)
)
triangulates with at mostK|χ(S)| +K tetrahedra (exercise) and therefore‖‖(
S, (1, 1)
)‖‖⩽ K|χ(S)| +K. Exercise 10.3.27 shows that for everye > 0
there is a degree-e covering ˜S→S and two degree-e coverings
( ˜S, (1, 1)
)
−→
( ˜S, (1,e )
)
−→
(
S, (1, 1)
)
which compose to a degree-e2 covering
( ˜S, (1, 1)
)
→
(
S, (1, 1)
)
. Therefore
‖‖(
S, (1, 1)
)‖‖ =
‖‖( ˜S, (1, 1)
)‖‖
e2 ⩽ K|χ( ˜S)| +K
e2 ⩽ Ke|χ(S)| +K
e2 → 0
ase→∞ . □
13.2.4. Simplicial and hyperbolic volume. In the next pages we will
prove the following theorem. Letv3 be the volume of the regular ideal tetra-
hedron in H3.
Theorem 13.2.11.LetM be a closed hyperbolic3-manifold. We have
Vol(M) =v3‖M‖.
The theorem furnishes in particular some examples of manifolds with pos-
itive simplicial volume and shows thatVol(M) is a topological invariant ofM,
thus generalising the Gauss-Bonnet theorem to dimensionn = 3. Mostow
rigidity will then strengthen this result in dimensionn = 3, showing that the
hyperbolic metric itself (not only its volume) is a topological invariant.
Both quantities Vol(M) and‖M‖ are multiplied byd if we substituteM
withadegree- d covering. In particular, uptosubstitutingM withitsorientable
double cover we can suppose thatM is orientable.
13.2. SIMPLICIAL VOLUME 413
13.2.5. Cycle straightening. The straight singulark-simplex with ver-
ticesv0,...,v k∈ Hn is the map
α: ∆ k−→ Hn
(t0,...,t k)↦−→t0v0 +... +tkvk
deﬁned using convex combinations, see Section 2.4.3. If thek + 1vertices are
not contained in a(k− 1)-plane the singulark-simplex isnon-degenerate and
its image is a hyperbolick-simplex.
The straightening αst of a singular simplexα: ∆k → Hn is the straight
singular simplex with the same vertices ofα. The straightening αst of a
singular simplexα: ∆k → M in a hyperbolic manifoldM = Hn/Γ is deﬁned
by lifting the singular simplex inHn, straightening it, and projecting it back
toM by composition with the covering map. Diﬀerent lifts produce the same
straightening inM because they are related by isometries ofHn.
The straightening extends by linearity to a homomorphism
st :Ck(M,R )→Ck(M,R )
which commutes with∂ and hence induces a homomorphism in homology
st∗ :Hk(M,R )→Hk(M,R ).
Proposition 13.2.12. The map st∗ is the identity.
Proof. We may deﬁne a homotopy between a singular simplexσ and its
straighteningσst using the convex combination
σt(x) =tσ(x) + (1−t)σst(x).
This deﬁnes a chain homotopy betweenst∗ and id via the same technique used
to prove that homotopic maps induce the same maps in homology. □
The abstract volume of a straightened singularn-simplex α: ∆n→M is
the volume of its lift inHn and may also be calculated as
⏐⏐⏐⏐
∫
α
ω
⏐⏐⏐⏐
whereω is the volume form onM pulled back alongα. Ifα is non-degenerate,
we say that itssign is positive ifα is orientation-preserving andnegative oth-
erwise: equivalently, it is the sign of
∫
αω.
We now concentrate on the dimensionn = 3 where we know that a
tetrahedron has maximum volumev3 if and only if it is both regular and ideal:
a straight simplex is compact and hence its abstract volume is strictly smaller
thanv3. We can now easily prove one inequality.
Proposition 13.2.13. LetM be a closed hyperbolic3-manifold. We have
Vol(M)⩽v3‖M‖.
414 13. MOSTOW RIGIDITY THEOREM
Proof. As we said above, we can suppose thatM is orientable. Take a
cycle α = λ1α1 +... +λkαk that represents [M]. We can suppose it is
straightened, because the straightening preserves both the coeﬃcients and
the homology class. Letω be the volume form onM. We get
Vol(M) =
∫
M
ω =
∫
α
ω =λ1
∫
α1
ω +... +λk
∫
αk
ω.
The quantity
⏐⏐∫
αi
ω
⏐⏐ is the abstract volume ofαi. Hence
⏐⏐∫
αi
ω
⏐⏐<v 3 and
Vol(M)<
(
|λ1| +... +|λk|
)
v3.
This holds for allα, hence Vol(M)⩽v3‖M‖. □
The proof of the converse inequality is less immediate.
13.2.6. Eﬃcient cycles.Let M = H3/Γ be a closed oriented hyperbolic
3-manifold. Anε-eﬃcient cycleforM is a straightened cycle
α =λ1α1 +... +λkαk
representing [M] where the abstract volume ofαi if bigger thanv3−ε and
the sign ofαi is coherent with the sign ofλi, for alli.
We will construct anε-eﬃcient cycle for everyε> 0. This will conclude
the proof of Theorem 13.2.11 in virtue of the following:
Lemma 13.2.14. If for everyε >0 the manifoldM admits anε-eﬃcient
cycle, then we haveVol(M)>v3‖M‖.
Proof. Let α = λ1α1 +...λ kαk be an ε-eﬃcient cycle andω be the
volume form onM. Coherence of signs givesλi
∫
αi
ω> 0 for alli. We get
Vol(M) =
∫
M
ω =
∫
α
ω =λ1
∫
α1
ω +... +λk
∫
αk
ω
>
(
|λ1| +... +|λk|
)
· (v3−ε).
Therefore Vol(M)>‖M‖· (v3−ε) for allε> 0. □
It remains to constructε-eﬃcient cycles.
Exercise 13.2.15. If ∆i is a sequence of tetrahedra inH3 whose vertices
tend to the vertices of a regular ideal tetrahedron in∂H3, then
Vol(∆i )→v3.
For anyt > 0, let ∆(t) be a regular tetrahedron obtained as in Section
3.2.4asfollows. Pickapoint x∈ H3 andaregulartetrahedronintheEuclidean
tangent spaceTx H3, centred at the origin with vertices at distancet from it,
project the vertices inH3 via the exponential map, and pick their convex hull.
At-simplex is a tetrahedron isometric to∆(t) equipped with an ordering
of its vertices: the ordering allows us to consider it as a straightened singular
simplex. LetS(t) be the set of allt-simplices in H3.
13.2. SIMPLICIAL VOLUME 415
Exercise 13.2.16. The groupIsom(H3) acts onS(t) freely and transitively.
RecallfromCorollary2.4.8that Isom(H3)isunimodular: theHaarmeasure
on Isom(H3) induces an Isom(H3)-invariant measure onS(t).
Let M = H3/Γ be a closed hyperbolic 3-manifold andπ : H3→ M the
covering projection. Fix a base pointx0∈ H3 and consider its orbitO = Γx0.
Consider the set
Σ = Γ 4/Γ
of the 4-uples (g0,g 1,g 2,g 3) considered up to the diagonal action ofΓ:
g· (g0,g 1,g 2,g 3) = (gg0,gg 1,gg 2,gg 3).
An elementσ = (g0,g 1,g 2,g 3)∈ Σdetermines a singular simplex˜σ in H3 with
vertices g0(x0),g 1(x0),g 2(x0),g 3(x0)∈ O only up to translations byg∈ Γ,
hence it gives a well-deﬁned singular simplex inM, which we still denote byσ.
We now introduce the chain
α(t) =
∑
σ∈Σ
λσ(t)·σ
for some appropriate real coeﬃcientsλσ(t) that we now deﬁne. The base
point x0 determines the Dirichlet tessellation ofH3 into domainsD(g(x0)),
g∈ Γ. Forσ = (g0,g 1,g 2,g 3) we letS+
σ (t)⊂S(t) be the set of all positive
t-simplices whosei-th vertex lies inD(gi (x0)) for alli. The numberλ+
σ (t) is
the measure ofS+
σ (t). We deﬁne analogouslyλ−
σ (t) and set
λσ(t) =λ+
σ (t)−λ−
σ (t).
Lemma 13.2.17.The chainα(t) has ﬁnitely many addenda and is a cycle.
If t is suﬃciently big the cycleα(t) represents a positive multiple of[M] in
the groupH3(M, R).
Proof. We prove that the sum is ﬁnite. Letd,T be the diameters ofD(x0)
and of at-simplex. We write σ = (id,g 1,g 2,g 3) for allσ∈ Σ: that is, all
simplices have their ﬁrst vertex atx0. Ifλσ(t)⁄= 0 thend(gix0,x 0)< 2d +T
for alli: thereforeα(t) has ﬁnitely many addenda (becauseO is discrete).
We prove thatα(t) is a cycle. The boundary∂α(t) is a linear combination
of straight2-simplices with vertices in(g0x0,g 1x0,g 2x0) asg0,g 1, andg2 vary.
The coeﬃcient of one such2-simplex is
∑
g∈Γ
(
−λ(g,g0,g1,g2)(t) +λ(g0,g,g1,g2)(t)−λ(g0,g1,g,g2)(t) +λ(g0,g1,g2,g)(t)
)
.
We prove that each addendum summed alongg∈ Γ is zero; for simplicity we
consider the last addendum and get
∑
g∈Γ
λ(g0,g1,g2,g)(t) =
∑
g∈Γ
λ(g0,g1,g2,g)(t)+−
∑
g∈Γ
λ(g0,g1,g2,g)(t)−.
