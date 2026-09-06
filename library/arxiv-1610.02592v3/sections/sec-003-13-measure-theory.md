---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-003-13-measure-theory
section_title: "Measure theory"
section_number: 1.3
pages: 31-34
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We prove (1) by showing that the ballB = B(p, injpN) is well-covered
for all p ∈ N. Since M is complete, every geodesic inN can be lifted to
a geodesic inM (at any starting point). For every ˜p∈ f−1(p) the mapf
sends the geodesics exiting from ˜p to geodesics exiting fromp and hence
sends isometricallyB(˜p, injpN) ontoB. On the other hand, given a pointq∈
f−1(B), the geodesic inB connectingf (q) top lifts to a geodesic connecting
q to some point˜p∈f−1(p). Therefore
f−1(
B(p, injpN)
)
=
⨆
˜p∈f−1(p)
B(˜p, injpN)
andf is a covering. □
Proposition 1.2.20. Let f : M→ N be a local isometry and a degree-d
covering. We have
Vol(M) =d· Vol(N).
Sketch of the proof. We may ﬁnd a disjoint union of well-covered open
sets inN whose complement has zero measure. Every such open set lifts to
d copies of it inM, and the zero-measure set lifts to a zero-measure set.□
Theformulamakessensealsowhensomeofthequantities Vol(M), Vol(N),
andd are inﬁnite.
1.2.13. Totally geodesic submanifolds.A diﬀerentiable submanifoldM
in a Riemannian manifoldN is totally geodesicif every geodesic inM with the
induced metric is also a geodesic inN.
When dimM = 1 this notion is equivalent to that of an unparametrized
embedded geodesic; ifdimM> 2 then M is a quite peculiar object: generic
Riemannian manifolds do not contain totally geodesic surfaces at all. An
equivalent condition is that, for everyp∈M and everyv∈Tp(M), the unique
geodesic inN passing throughp with velocityv stays inM for some interval
(−ε,ε ).
1.2.14. Riemannianmanifoldswithboundary. Manygeometricnotions
in Riemannian geometry extend easily to manifoldsM with boundary. The
boundary∂M of a Riemannian manifoldM is naturally a Riemannian manifold
without boundary. A particularly nice (and exceptional) case is when∂M is
totally geodesic.
1.3. Measure theory
We will use some basic measure theory only in Chapter 8.
24 1. PRELIMINARIES
1.3.1. Borel measure.A Borel setin a topological spaceX is any subset
obtained from open sets through the operations of countable union, countable
intersection, and relative complement. LetF denote the set of all Borel sets.
A Borel measureonX is a functionµ: F→ [0, +∞] which is additive on any
countable collection of disjoint sets.
The measure islocally ﬁniteif every point has a neighbourhood of ﬁnite
measure and istrivial ifµ(S) = 0 for allS∈ F.
Exercise 1.3.1. Ifµ is a locally ﬁnite Borel measure thenµ(X)< +∞ for
any compact Borel setK⊂X.
Example 1.3.2. Let D ⊂ X be a discrete set. The Dirac measure δD
concentrated inD is the measure
δD(S) = #(S∩D).
SinceD is discrete, the measureδD is locally ﬁnite.
Thesupport of a measure is the set of all pointsx∈X such thatµ(U)> 0
for any open setU containing x. The support is a closed subset ofX. The
measure isfully supportedif its support isX. The support ofδD is of course
D. A pointx∈X is anatom forµ ifµ({x})> 0.
1.3.2. Construction by local data.A measure can be deﬁned using local
data in the following way.
Proposition 1.3.3.Let{Ui}i∈I be a countable, locally ﬁnite open covering
of X and for anyi ∈ I let µi be a locally ﬁnite Borel measure onUi. If
µi|Ui∩Uj =µj|Ui∩Uj for alli,j ∈I there is a unique locally ﬁnite Borel measure
µ onX whose restriction toUi isµi for alli.
Proof. For every ﬁnite subsetJ⊂I we deﬁne
XJ =
(
∩j∈JUj
)
\
(
∪i∈I\JUi
)
.
The setsXJ form a countable partition ofX into Borel sets and everyXJ is
equipped with a measureµJ =µj|Xj for anyj∈J. Deﬁneµ by setting
µ(S) =
∑
j∈J
µ(S∩Xj )
on any BorelS⊂X. □
WhenX is a reasonable space some hypothesis may be dropped.
Proposition 1.3.4. If X is paracompact and separable, Proposition 1.3.3
holds for any open covering{Ui}i∈I.
Proof. By paracompactness and separability the open covering{Ui} has
a reﬁnement that is locally ﬁnite and countable: apply Proposition 1.3.3 to
the reﬁnement to get a measureµ. To prove that indeedµ|Ui = µi apply
Proposition 1.3.3 again to the covering ofUi given by the reﬁnement. □
1.3. MEASURE THEORY 25
1.3.3. Topology on the measures space.In what follows we suppose
for simplicity that X is a ﬁnite-dimensional topological manifold, although
everything is valid in a much wider generality. We indicate by M (X) the
space of all locally ﬁnite Borel measures onX and byCc(X) the space of all
continuous functionsX→ R with compact support: the spaceCc(X) is not
a Banach space, but it is a topological vector space.
Recall that the topological dual of a topological vector spaceV is the
vector spaceV∗ formed by all continuous linear functionalsV → R. A measure
µ∈ M (X) acts like a continuous functional onCc(X) as follows
µ:f↦−→
∫
µ
f
and hence deﬁnes an element ofC∗
c (X). A functional inC∗
c (X) is positive if
it assumes non-negative values on non-negative functions.
Theorem 1.3.5 (Riesz representation).The spaceM (X)may be identiﬁed
in this way to the subset inCc(X)∗ of all positive functionals.
The space M (X) in Cc(X)∗ is closed with respect to sum and product
with a positive scalar. We now use the embedding ofM (X) into Cc(X)∗ to
deﬁne a natural topology onM (X).
Deﬁnition 1.3.6. LetV be a real topological vector space. Every vector
v∈V deﬁnes a functional inV∗ asf↦→f (v ). Theweak-* topologyonV∗ is
the weakest topology among those where these functionals are continuous.
We giveCc(X)∗, and henceM (X), the weak-* topology.
1.3.4. Sequences of measures. By deﬁnition, a sequence of measures
µi converges toµ if and only if
∫
µi
f→
∫
µf for anyf∈Cc(X). This type of
weak convergence is usually denoted with the symbolµi ⇀µ .
Exercise 1.3.7. Letxi be a sequence of points inX that tend tox∈X:
we getδxi ⇀δ x.
It is important to note thatµi ⇀ µdoes not imply µi (U)→ µ(U) for
any open (or closed) setU: consider for instance a sequenceµi = δxi with
xi exiting from (or entering into) the setU. We can get this convergence on
compact sets if we can control their topological boundary.
Proposition 1.3.8. LetK⊂X be a Borel compact subset. Ifµi ⇀µ and
µ(∂K ) = 0 thenµi (K)→µ(K).
On Banach spaces, the unitary ball is compact in the weak-* topology.
Here M (X) is not a Banach space, but we have an analogous compactness
theorem.
Theorem 1.3.9. A sequence of measuresµi such thatµi (K) is bounded
on every Borel compact setK⊂X converges on a subsequence.
26 1. PRELIMINARIES
