---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-044-42-dependency-graphs
section_title: "Dependency graphs"
section_number: 4.2
pages: 31-35
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In this paragraph, we will see that the uniform bounds on cumulants are satisﬁed for sumsSn =∑n
i=1Ai,n of dependent random variables with speciﬁc dependency structure.
More precisely, if(Av)v∈V is a family of real valued random variables, we calldependency graph for
this family a graphG = (V,E ) with the following property: ifV1 and V2 are two disjoint subsets of
V with no edge e ∈ E joining a vertex v1 ∈ V1 to a vertex v2 ∈ V2, then (Av)v∈V1 and (Av)v∈V2
are independent random vectors. For instance, let(A1,...,A 7) be a family of random variables with
dependency graph drawn on Figure 6. Then the vectors(A1,A 2,A 3,A 4,A 5) and (A6,A 7) corresponding
to diﬀerent connected components must be independent. Moreover, note that(A1,A 2) and (A4,A 5) must
be independent as well: although they are in the same connected component of the graphG, they are not
directly connected by an edgee∈E.
1
2
3
4
5
6
7
Fig. 6 A dependency graph for7 real-valued random variables.
Theorem 34 (Féray–Méliot–Nikeghbali, see [FMN16]).Let (Av)v∈V be a family of random vari-
ables, with|Av|≤ A a.s., for allv∈V. We suppose thatG = (V,E ) is a dependency graph for the family
and denote
•N =
∑
v∈V E|Av|
A ≤ cardV;
•D the maximum degree of a vertex inG plus one.
If S =∑
v∈V Av, then for allr≥ 1,
|κ(r)(S)|≤ Nr r−2 (2D)r−1Ar.
32 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
Consider a sequence(Sn)n∈N, where eachSn writes as∑
v∈VnAv,n, with theAv,n uniformly bounded
byA (in a lot of examples, theAv,n are indicator variables, so that we can takeA = 1). Set
Nn =
∑
v∈Vn E|Av,n|
A
and assume that, for eachn, (Av,n)v∈Vn has a dependency graph of maximal degreeDn− 1. Then the
sequence (Sn)n∈N admits uniform bounds on cumulants with parameters(Dn,Nn,A ) and the result of the
previous section applies. Note that in this setting we have the bound~σn≤A, so the bound of Corollary
30 holds with the better constant 52.52.
Remark 35.The parameterD is equal to the maximal number of neighbors of a vertexv∈V, plus 1. In
the following, we shall simply callD the maximal degree, being understood that one always has to add
1. Another way to deal with this convention is to think of dependency graphs as having one loop at each
vertex.
Example 36.The following example, though quite artiﬁcial, shows that one can construct families of
random variables with arbitrary parametersN andD for their dependency graphs. Let(Uk)k∈Z/NZ be a
family of independent Bernoulli random variables withP[Uk = 1] = 1− P[Uk = 0] =q; and fori∈ Z/NZ,
Ai = 2
( i+D∏
k=i+1
Uk
)
− 1.
EachAi is a Bernoulli random variable withP[Ai = 1] = 1− P[Ai =−1] =qD, which we denotep (p is
considered independent ofN). We are interested in the ﬂuctuations ofS =∑N
i=1Ai. Note that the partial
sums∑k≤N
i=1 Ai correspond to random walks with correlated steps: asD increases, the consecutive steps
of the random walk have a higher probability to be in the same direction, and therefore, the variance
of the sumS =∑N
i=1Ai grows. We refer to Figure 7, where three such random walks are drawn, with
parameters p = 1
2, N = 1000 and D∈{ 5, 15, 30}.
D = 30
D = 15
D = 5
Fig. 7 Random walks with1000 steps and correlation lengthsD = 5, D = 15 and D = 30.
If d(i,j ) ≥ D in Z/NZ, then Ai and Aj do not involve any common variableUk, and they are
independent. It follows that ifG is the graph with vertex setZ/NZ and with an edgee betweeni and j
ifd(i,j )≤D, thenG is a dependency graph for theAi’s. This graph hasN vertices, and maximal degree
2D− 1. Moreover, one can compute exactly the expectation and the variance ofS =∑N
i=1Ai:
Mod-φ convergence, II: Estimates on the speed of convergence 33
E[S] =N(2p− 1);
Var(S) = 4
N∑
i,j=1
cov(Ui+1··· Ui+D,Uj+1··· Uj+N)
= 4
N∑
i,j=1
(
qD+min(D,d(i,j))−p2)
= 4Np
D−1∑
j=−(D−1)
(q|j|−p)
= 4Np
(
1 +p
1
D− 2p
1−p
1
D
− (2D− 1)p
)
.
If N and D go to inﬁnity withD =o(N), thenq =p
1
D = 1 + logp
D +O( 1
D2 ), and
E[S] =N(2p− 1);
Var(S) = 8N(D +O(1))p
( 1−p
− logp−p
)
.
So, one can apply Corollary 30 to the sumS, and one obtains:
dKol
(
S− E[S]√
Var(S)
,NR(0, 1)
)
≤ 6
(
p
(
1−p
− logp−p
))3/2
√
D
N.
Example 37.Fix p∈ (0, 1), and consider a randomErdös–Rényi graphG =Gn =G(n,p ), which means
that one keeps at random each edge of the complete graphKn with probabilityp, independently from
every other edge. Note that we only consider the case of ﬁxedp here; forp→ 0, we would get rather
weak bounds, see [FMN16, Section 10.3.3] for a discussion on bounds on cumulants in this framework.
Let H = (VH,EH) and G = (VG,EG) be two graphs. The number of copies ofH in G is the number
of injectionsi :VH→VG such that, if(h1,h 2)∈EH, then (i(h1),i (h2))∈EG. In random graph theory,
this is called thesubgraph countstatistics; we denote it byI(H,G ). We refer to Figure 8 for an example,
where H =K3 is the triangle andG is a random Erdös–Rényi graph of parametersn = 30 and p = 1
10.
Fig. 8 Count of triangles in a random Erdös–Rényi graph of parametersn = 30 and p = 0.1. Here, there are4× 3! = 24
ways to embed a triangle in the graph.
One can always writeI(H,G ) as a sum of dependent random variables. IdentifyVH with [ [1,k ] ]and
VG with [ [1,n ] ], and denote A(n,k ) the set of arrangements(a1,...,a k) of size k in [ [1,n ] ]. Given such
34 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
an arrangement, theinduced subgraphG[a1,...,a k] is the graph with vertex set[ [1,k ] ], and with an edge
betweeni and j if (ai,aj)∈EG. Then,
I(H,G ) =
∑
A∈A(n,k)
IA(H,G ),
where IA(H,G ) = 1 if H⊂G[A], and 0 otherwise.
A dependency graph for the random variablesIA(H,Gn) has vertex set A(n,k ) of cardinalityNn =
n↓k =n(n−1)(n−2)··· (n−k+1), and an edge between two arrangements(a1,...,a k) and (b1,...,b k) if
they share at least two points (otherwise, the random variablesIA(H,Gn) andIB(H,Gn) involve disjoint
sets of edges and are therefore independent). As a consequence, the maximal degree of the graph is smaller
than
Dn =
((k
2
)2
2(n− 2)(n− 3)··· (n−k + 1)
)
,
and of ordernk−2. Therefore, Dn
Nn
≤
2(
k
2)
2
n(n−1) =O( 1
n2 ), and on the other hand, ifh is the number of edges
of H, one can compute the asymptotics of the expectation and of the variance ofI(H,Gn):
E[I(H,Gn)] =n↓kph;
Var(I(H,Gn)) = 2h2p2h−1(1−p)n2k−2 +O(n2k−3),
see [FMN16, Section 10] for the details of these computations. In particular,
lim
n→∞
Var(Sn)
NnDn
=p2h−1(1−p)
(
h(k
2
)
)2
=~σ2 > 0.
Thus, using Corollary 30, we get
dKol
(
I(H,Gn)− E[I(H,Gn)]√
Var(I(H,Gn))
,NR(0, 1)
)
≤ 4.65 (k(k− 1))4
p3h ( 1
p− 1)3/2h3
1
n
for n large enough. For instance, ifTn =I(K3,Gn) is the number of triangles inGn, then
E[Tn] =n↓3p3
Var[Tn] = 18n↓4p5(1−p) + 6n↓3p3(1−p3)
and
dKol
(
Tn−n↓3p3
√
18n↓4p5(1−p) + 6n↓3p3(1−p3)
,NR(0, 1)
)
≤ 234
p9( 1
p− 1)
3
2
1
n (1 +O( 1
n)).
This result is not new, except maybe the explicit constant. We refer to [BKR89] for an approach of speed
of convergence for subgraph counts using Stein’s method. More recently, Krokowski, Reichenbachs and
Thäle [KRT15] applied Malliavin calculus to the same problem. Our result corresponds to the case where
p is constant of their Theorem 1. Similar bounds could be obtained by Stein’s method, see [Rin94].
To conclude our presentation of the convergence of sums of bounded random variables with sparse
dependency graphs, let us analyse precisely the case ofuncorrelated random variables.
Corollary 38.LetSn =∑Nn
i=1Ai,n be a sum of centered and bounded random variables, that are uncor-
related and withE[(Ai,n)2] = 1 for alli. We suppose that the random variables have a dependency graph
of parametersNn→ +∞ and Dn.
Mod-φ convergence, II: Estimates on the speed of convergence 35
