---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-056-2-θp-trt1
section_title: "(θP )tr−t1. ⊓ ⊔"
section_number: 2
pages: 46-48
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
Proposition 54.The family of random variables{Yt}t∈N admits aK
√
M-uniform weighted dependency
graph, where, for integerss<t , the weight betweenYt and Ys is 2(θP )t−s.
Proof. A lemma of Saulis and Statulevičius [SS91, Lemma 1.1] expresses usual cumulants in terms of
Boolean cumulants:
κ(r)(Yt1,...,Y tr) =
∑
π∈P([r])
(−1)|π|−1N(π)
∏
C∈π
B(|C|)(Ytj, j∈C). (10)
Here, the sum runs over set-partitionsπ of [r] :={1,...,r };|π|is the number of blocks of a set-partitionπ,
the product runs over blocksC inπ andB(|C|)(Ytj, j∈C) is the Boolean cumulant of the subfamily(Ytj)
indexed by integersj in the blockC, with the times ordered in increasing order (recall that the Boolean
are not symmetric functionals). FinallyN(π) is a combinatorial factor that can be computed as follows.
Mod-φ convergence, II: Estimates on the speed of convergence 47
For each blockC of π, denotemC and MC its smallest and biggest elements; then callnC the number
of blocksC′⁄=C such thatmC is in the interval[mC′;MC′]. We ﬁnally deﬁneN(π) =∏
C∈π;1/∈CnC. In
other terms,N(π) counts the functionsg mapping each blockC of π (except the one containing1) to a
block g(C)⁄=C such thatmC∈ [mg(C);Mg(C)].
Let us make an observation. Ifπ is a partition andk an integer such that each block ofπ either
contains only numbers smaller than or equal tok or only numbers bigger thank (π is then said to be
disconnected), then no functiong as above exists (there is no possible image for the blockC containing
k + 1) andN(π) = 0. On the other hand, forconnectedpartitions π, we always haveN(π)> 0, so that
the sum in (10) is in eﬀect a sum over connected partitions.
Eq. (10) and Proposition 52 imply the bound
⏐⏐⏐κ(r)(Yt1,...,Y tr)
⏐⏐⏐≤
(
K
√
M
)r ∑
π∈P([r])
N(π)
∏
C∈π
(θP )tMC−tmC.
We would like to prove
⏐⏐⏐κ(r)(Yt1,...,Y tr)
⏐⏐⏐≤ 2r−1
(
K
√
M
)r ∑
T∈ST(Kr)
w(T ),
where w(T ) = ∏
{j,j′}∈ET,j<j′(θP )tj′−tj. Therefore it is suﬃcient for us to ﬁnd an injective mappingη
from pairs (π,g ) as above to edge-bicolored spanning trees~T such that
w
(
η(π,g )
)
=
∏
C∈π
(θP )tMC−tmC ; (11)
here, by convention, the weightw(~T ) of a colored tree is the weightw(T ) of its uncolored version. In the
following, we describe such a mapping, concluding the proof of the proposition.
Let (π,g ) be a pair of objects as above:π is a set-partition of[r] andg is function mapping each block
C ofπ (except the one containing1) to a blockg(C)⁄=C such thatmC∈ [mg(C);Mg(C)]. For each block
C of π, we consider the set
S(C) =C∪{mC′, C′∈g−1(C)}.
Let us callPC the path with vertex-setS(C), where the vertices are in increasing order along the path.
We also color in blue (resp. in red) edges of this path whose extremity with smaller label is inC (resp.
in{mC′, C′∈g−1(C)}).
As an example, takeπ ={C1,··· ,C 6} withC1 ={1, 5, 10},C2 ={2, 11},C3 ={3, 9},C4 ={4, 6, 13},
C5 ={7, 12}, C6 ={8}. As functiong, we takeg(C2) = C1, g(C3) = C1, g(C4) = C2, g(C5) = C1 and
g(C6) = C4. In this case, we getS(C1) ={1, 2, 3, 5, 7, 10}, S(C2) ={2, 4, 11}, S(C4) ={4, 6, 8, 13} and
S(Ci) =Ci for i∈{ 3, 5, 6}. The associated bicolored paths are drawn in Fig. 11.
As in Fig. 11, we then take the union of the pathsPCi, identifying vertices with the same label (the
minimummC⁄= 1 of a blockC appears in the pathS(C) and in the pathS(g(C))). Doing that, we get
an edge-bicolored graph that we callη(π,g ). Let us ﬁrst check thatη(π,g ) is a tree. To this purpose, we
order the blocksC1,...,C |π| of π in increasing order of their minima (as done in the example). Observe
that this implies thatg(Ci) = Cj for some j < i. We will prove by induction that, for eachi≤| π|,
PC1∪···∪ PCi is a tree. The casei = 1 is trivial. Fori > 1, the graphPC1∪···∪ PCi is obtained
by gluing the pathPCi on the graphPC1∪···∪ PCi−1, identifyingmCi which appears in both. Since
PC1∪···∪ PCi−1 is a tree by induction hypothesis, the resulting graphPC1∪···∪ PCi is a tree as well,
concluding the induction. Thusη(π,g ) =PC1∪···∪ PC|π| is a tree.
The equality (11) is easy: since the edge set ofη(π,g ) is the union of the edge sets of thePCi, we have
48 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
1
2
3
5
7
10
2
4
11
3
9
4
6
8
13
7
12
8 1
2
3
5
7
10
6
8
13
411
9
12
Fig. 11 Illustration of the constructionη in the proof of Proposition 54: the pathPCi and their gluingη(π,g ). For readers
of a black-and-white printed version, red edges are thicker.
w
(
η(π,g )
)
=
|π|∏
i=1
w(PCi) =
|π|∏
i=1
(θP )tMCi
−tmCi.
We ﬁnally need to prove thatη is injective,i.e. that we can recover(π,g ) from η(π,g ). We start by the
following easy observation: inη(π,g ), vertices with a red incident edge going to a vertex with bigger label
are exactly the vertices with a label which is the minimummC⁄= 1 of a blockC of π. By construction,
such vertices have at most three incident edges, which are as follow:
(E1) as said above, a ﬁrst one is red and goes to a vertex to bigger label;
(E2) a second one is either blue or red and goes to a vertex of lower label.
(E3) possibly, a last one is blue and goes to a vertex to bigger label (there is such an edge whenmC is not
alone in its block);
Indeed, in the construction, edges (E1) and (E2) comes fromSg(C) while edge (E3) comes fromSC. We
split the vertexmC into two, keeping edges (E1) and (E2) in the same component. Doing that for the
|π|− 1 verticesmC⁄= 1, we inverse the gluing step of the construction ofη(π,g ). It is then straightforward
to recover(π,g ). ⊓ ⊔
Theorem 55.Let (Xt)t∈N be an ergodic Markov chain on a ﬁnite state spaceX of sizeM, andθP < 1
the constant associated by(9) with the transition matrixP. We consider a sumSn =∑n
t=1ft(Xt) with
‖ft‖∞≤K. Then, for anyr≥ 1,
⏐⏐⏐κ(r)(Sn)
⏐⏐⏐≤nrr−2
(
2 1 +θP
1−θP
)r−1(
K
√
M
)r
. (12)
As a consequence:
