---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-005-15-group-actions
section_title: "Group actions"
section_number: 1.5
pages: 40-42
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Groups acting of spaces are so important in geometry, that they are some-
times used as a deﬁnition of “geometry” itself.
1.5.1. Deﬁnitions.The action of a groupG on a topological spaceX is
a homomorphism
G→ Homeo(X)
where Homeo(X) is the group of all self-homeomorphisms ofX. The quotient
setX/G is the set of all orbits inX and we give it the usual quotient topology.
We denote byg(x) the image ofx∈X along the homeomorphism determined
byg∈G. The action is:
• free ifg(x)⁄=x for all non-trivialg∈G and allx∈X;
• properly discontinuous if any two pointsx,y ∈ X have neighbour-
hoodsUx andUy such that the set
{
g∈G
⏐⏐g(Ux )∩Uy⁄= ∅
}
is ﬁnite.
The relevance of these deﬁnitions is due to the following.
Proposition 1.5.1. Let G act on a Hausdorﬀ connected spaceX. The
following are equivalent:
(1) G acts freely and properly discontinuously;
(2) the quotientX/G is Hausdorﬀ and the mapX→X/G is a covering.
1.5. GROUP ACTIONS 33
A covering of typeX→X/G is calledregular. A coveringX→Y is regular
if and only if the image ofπ1(X) in π1(Y ) is normal, and in that caseG is
the quotient of the two groups. In particular every universal cover is regular.
Summing up:
Corollary 1.5.2.Every path-connected locally contractible Hausdorﬀ topo-
logical spaceX is the quotient ˜X/G of its universal cover by the action of
some groupG acting freely and properly discontinuously.
The groupG is isomorphic toπ1(X).
Exercise 1.5.3. Let a discrete groupG act on a locally compact spaceX.
The following are equivalent:
• the action is properly discontinuous;
• for every compactK⊂X, the set
{
g|g(K)∩K⁄= ∅
}
is ﬁnite;
• the mapG×X→X×X that sends (g,x ) to (g(x),x ) is proper.
1.5.2. Isometry group.We now want to consider the case where a group
G acts by isometries on a Riemannian manifoldM. In this case we have a
homomorphism
G→ Isom(M)
withvaluesinthe isometrygroup Isom(M)ofM,i.e.thegroupofallisometries
f :M→M. The groupIsom(M) is much smaller thanHomeo(M).
Theorem 1.5.4 (Myers – Steenrod).The group Isom(M) has a natural
Lie group structure compatible with the compact-open topology. The map
F : Isom(M)×M→M×M that sends (ϕ,p ) to (ϕ(p),p ) is proper.
Corollary 1.5.5.IfM is compact thenIsom(M) is compact.
Proposition 1.5.6. The stabilizer of any pointx ∈ M is a compact Lie
subgroup of Isom(M).
Proof. Thestabilizerof x isclosedandhenceisaLiesubgroupof Isom(M).
The isometries that ﬁxx are determined by their orthogonal action onTxM
and therefore form a compact Lie subgroup ofO(n). □
The hard part of the Myers – Steenrod Theorem is to endowIsom(M)with
a Lie group structure. In fact, in all the concrete cases that we will encounter,
the Lie group structure ofIsom(M) will be evident from the context, so we
will not need the full strength of Theorem 1.5.4. The rest of the theorem is
not diﬃcult to prove and we can leave it as an exercise.
Exercise 1.5.7. Prove thatF is proper.
We denote byIsom+(M) the subgroup of Isom(M) consisting of all the
orientation-preserving isometries. It has index one or two inIsom(M).
34 1. PRELIMINARIES
1.5.3. Discrete groups. Let M be a Riemannian manifold. The group
Isom(M) is a Lie group, so it makes sense to consider discrete subgroups.
Proposition 1.5.8.A groupΓ< Isom(M) acts properly discontinuously on
M if and only if it is discrete.
Proof. If Γ is discrete, Theorem 1.5.4 and Exercise 1.5.3 imply that it acts
properly discontinuously. Conversely, if Γ acts properly discontinuously then
e∈ Γ is easily seen to be isolated, and we apply Exercise 1.4.18. □
If Γ< Isom(M) is discrete and acts freely, the quotient mapM→M/Γ is
a covering. Moreover, the Riemannian structure projects fromM toM/Γ.
Proposition 1.5.9. Let Γ < Isom(M) act freely and properly discontinu-
ously onM. There is a unique Riemannian structure on the manifoldM/Γ
such that the coveringπ :M→M/Γ is a local isometry.
Proof. LetU⊂M/Γ be a well-covered set: we haveπ−1(U) =⊔i∈IUi and
π|Ui :Ui→U is a homeomorphism. Pick ani∈I and assign toU the smooth
and Riemannian structure ofUi transported alongπ. The resulting structure
onU does not depend oni since the open setsUi are related by isometries in
Γ. We get a Riemannian structure onM/Γ, determined by the fact thatπ is
a local isometry. □
1.5.4. Measures. The case where a groupG acts by preserving some
measure instead of a Riemannian metric is also very interesting, although
quite diﬀerent. This situation will occur only in Chapter 8.
Letagroup G actonamanifold M. ABorelmeasure µonM isG-invariant
ifµ(S) =µ(g(S)) for every Borel setS⊂M.
If G acts onM freely and properly discontinuously, thenM→ M/G is a
covering and everyG-invariant measureµ onM descends to a natural measure
on the quotient M/G which we still indicate byµ. The measure on M/G
is deﬁned as follows: for every well-covered open setU ⊂ M/G we have
π−1(U) =⊔i∈IUi and we assign toU the measure ofUi for anyi∈ I. This
assignment extends to a unique Borel measure onM/G by Proposition 1.3.4.
Note that the measure onM/G is not the push-forward ofµ, namely it is
not true thatµ(U) =µ(π−1(U)).
