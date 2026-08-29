---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-051-52-uniform-weighted-dependency-graphs
section_title: "Uniform weighted dependency graphs"
section_number: 5.2
pages: 41-42
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
If A1,...,A r are real-valued random variables, there is a notion of joint cumulant that generalize the
cumulants of Section 4:
κ(A1,A 2,...,A r) = [z1z2··· zr]
(
log E[ez1A1+z2A2+···+zrAr]
)
.
The joint cumulants are multilinear and symmetric functionals ofA1,...,A r. On the other hand,
κ(r)(X) =κ(X,X,...,X )
with r occurrences of X in the right-hand side. In particular, ifS = ∑
v∈V Av is a sum of random
variables, then
κ(r)(S) =
∑
v1,...,vr∈V
κ(Av1,Av2,...,A vr).
Deﬁnition 43.Let (Av)v∈V be a family of random variables deﬁned on the same probability space.
A weighted graphG = (V,E,w G) is a C-uniform weighted dependency graph for(Av)v∈V if, for any
multisetB ={v1,...,v r} of elements ofV, one has
⏐⏐κ
(
Av, v∈B
)⏐⏐≤C|B| ∑
T∈ST(G[B])
w(T ).
Proposition 44.Let (Av)v∈V be a ﬁnite family of random variables with aC-uniform weighted depen-
dency graphG. Assume thatG has N =|V| vertices, and maximal weighted degreeD− 1, that is:
∀v∈V,
∑
v′:v′⁄=v
{v,v′}∈EG
wG({v,v′})≤D− 1.
Then, forr≥ 1, ⏐⏐⏐⏐⏐κ(r)
(∑
v∈V
Av
)⏐⏐⏐⏐⏐≤Nr r−2Dr−1Cr.
Consider a sequence(Sn)n∈N, where eachSn writes as∑
v∈VnAv,n. SetNn =|Vn| and assume that, for
eachn, (Av)v∈Vn has C-uniform weighted dependency graph of maximal degreeDn− 1 (by assumption,
C does not depend onn). Then the sequence(Sn) admits uniform bounds on cumulants with parameters
(Dn
2 ,Nn,C ) and the results of Section 4, in particular Corollary 30, apply.
Proof. By multilinearity and deﬁnition of a uniform weighted dependency graph, we have
⏐⏐⏐⏐⏐κr
(∑
v∈V
Av
)⏐⏐⏐⏐⏐≤Cr ∑
v1,...,vr
∑
T∈ST(G[v1,...,vr])
w(T ). (7)
By possibly adding edges of weight0, we may assume thatG[v1,...,v r] is always the complete graph
Kr so that ST(G[v1,...,v r])≃ ST(Kr) as sets. The weight of a treeT however depends onv1,··· ,vr,
namely
w(T ) =
∏
{i,j}∈T
wG({vi,vj}),
where wG({vi,vj}) is the weight of the edge{vi,vj} in G (or 1 if vi =vj).
With this viewpoint, we can exchange the order of summation in (7). We claim that the contribution
of a ﬁxed treeT∈ ST(Kr) can then be bounded as follows:
∑
v1,...,vr
w(T ) =
∑
v1,...,vr
∏
{i,j}∈T
wG({vi,vj})≤NDr−1. (8)
42 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
Let us prove this claim by induction onr. The caser = 1 is trivial. Up to renaming the vertices ofT,
we may assume thatr is a leaf ofT so thatT is obtained from a spanning tree~T of Kr−1 by adding an
edge{i0,r} for somei0 <r . Then
∑
v1,...,vr
∏
{i,j}∈T
wG({vi,vj})
=
∑
v1,...,vr−1

 ∏
{i,j}∈~T
wG({vi,vj})


[∑
vr∈V
wG({vi0,vr})
]
.
The expression in square brackets is by deﬁnition smaller thanD for all vi0 (the sum forvr⁄= vi0 is
smaller thanD− 1 and the term forvr =vi0 is 1). By induction hypothesis, the sum of the parenthesis is
smaller thanNDr−2. This concludes the proof of (8) by induction. The lemma now follows immediately,
since the number of spanning trees ofKr is well known to berr−2. ⊓ ⊔
Remark 45.A classical dependency graph with a uniform boundA on all variablesAv can be seen as a
C-uniform weighted dependency graph forC = 2A (all edges have weight 1); see [FMN16, Section 9.4].
In this case, Proposition 44 reduces to Theorem 34. The proof of Proposition 44 given here is a simple
adaptation of the second part of the proof of Theorem 34 (see [FMN16, Chapter 9]) to the weighted
context. The ﬁrst, and probably the hardest part of the proof of Theorem 34 consisted in showing that
a classical dependency graph is indeed aC-uniform weighted dependency graph.
Remark 46.In the case where the setV is a subset ofZd and the weight function only depends on the
distance, the notion of uniform weighted dependency graph coincides with the notion ofstrong cluster
properties, proposed by Duneau, Iagolnitzer and Souillard in [DIS73]. These authors also observed that
this implies uniform bounds on cumulants whenD is bounded, see [DIS73, Eq. (10)].
Remark 47.A weaker notion of weighted dependency graph, where the bound on cumulant is not uniform
onr, was recently introduced in [Fér16]. This weaker notion only enables to prove central limit theorem,
without normality zone or speed of convergence results. However, it seems to have a larger range of
applications.
