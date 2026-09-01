---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity"
section_id: sec-003-32-partition-scheme-via-minimum-spanning-tree
section_title: "Partition scheme via minimum spanning tree"
section_number: 3.2
pages: 8-13
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity — We establish new lower bounds for the convergence radius of the Ma yer series and the Virial series of a continuous"
---
The key point now is to ﬁnd a partition scheme M in such a way that is possible to ﬁnd a good
bound for the factor exp {−β ∑
{i,j }∈EM (τ )\E+
τ
V (xi − xj)} appearing in the r.h.s. of (3.2).
We will construct explicitly our partition scheme M : Tn → G n by ﬁrst deﬁning an auxiliary map
T : Gn → T n and then deriving M from T according to the following proposition.
Proposition 2 The following statements are equivalent.
1. There are two maps
Gn
T /d47/d47 TnM
/d111/d111
such that T −1(τ) = {g ∈ G n : τ ⊂ g ⊂ M (τ)} for every τ ∈ T n.
2. M is a partition scheme in Gn.
8
Proof. 1 ⇒ 2. Since g ∈ T −1(T (g)), we have T (g) ⊂ g for all g ∈ G n. In particular, for every
tree τ we have T (τ) ⊂ τ which implies T (τ) = τ because both are trees. I.e., T is surjective and
thus the intervals T −1(τ) are nonempty. This implies that Gn is the disjoint union of the intervals
Gn = ⋃
τ∈Tn T −1(τ) = ⋃
τ∈Tn[τ, M (τ)]. Hence in view of Deﬁnition 3 we conclude that M is a
partition scheme in Gn.
2 ⇒ 1. If M is a partition scheme then for any g ∈ G n there exists a unique tree τ ∈ T n such that
g ∈ [τ, M (τ)]. Therefore we can deﬁne the map T from Gn to Tn such that, for all g ∈ [τ, M (τ)],
T (g) = τ. □
We thus start by ﬁrst deﬁning the map T from Gn to Tn. In order to do that, assume we have
a function deﬁned on the edges of the complete graph, f : En → R∗. Then, for every connected
graph g ∈ G n there is at least a tree τ ⊂ g, among the trees τ′ ⊂ g, which minimizes the value
of ∑
e∈Eτ ′ f (e). This tree is called a minimum spanning tree of g w.r.t. f . If f is such that this
minimum spanning tree is unique for each graph g ∈ G n, then f induces a map, say Tf , from Gn to
Tn which associates to each g ∈ G n this unique minimum spanning tree.
Let now V be a stable and tempered pair potential in Rdn and let ( x1, . . . , x n) ∈ Rdn be given. We
would like to consider as the function f : En → R∗ the one that associates to each {i, j } ∈ En the
value V (xi − xj). The problem is that such f , depending on the potential V and the conﬁguration
(x1, . . . , x n) ∈ Rdn chosen, in general does not guarantee that each g ∈ G n contains a unique
minimum spanning tree w.r.t. to f . In order to avoid multiple minima, we will therefore modify
the codomain of the function f by adding n(n − 1)/ 2 auxiliary “coordinates” (which will take only
integers values), each of them one-to-one associated to an e dge of En. These coordinates will permit
to distinguish eventual multiple minimum trees.
To carry out this procedure, we need to widen our framework an d consider, instead of functions
from En to R∗, a suitable class of more general functions f : En → K with K being a totally ordered
Abelian monoid and having the key property that ∑
e∈Eτ f (e) is diﬀerent for diﬀerent trees τ ∈ T n.
We recall that a totally ordered Abelian monoid (shortly tomonid) is a structure ( K, +, 0, ≥) such
that ( K, +, 0) is an Abelian (i.e. commutative) monoid, ( K, ≥) is a totally ordered set and for
all x, y, z ∈ K we have that x ≥ y implies x + z ≥ y + z (i.e. the total order ≥ is translational
invariant).
Deﬁnition 4 Let f : En → K where K is a totally ordered Abelian monoid. We say that f is
admissible if for any τ, τ ′ ∈ T n such that τ ⁄= τ′ we have that ∑
e∈E(τ) f (e) ⁄= ∑
e∈E(τ ′) f (e).
Once an admissible function f : En → K has been given, we can deﬁne the maps Tf from Gn to Tn
Mf from Tn to Gn as follows.
Deﬁnition 5 Let K be a totally ordered Abelian monoid. Let f : En → K be an admissible function.
Then, for every g ∈ G n there is a unique spanning tree τ ⊂ g for which ∑
e∈E(τ) f (e) is minimum.
We deﬁne the map Tf : Gn → T n such that Tf (g) is this unique minimum spanning tree of g.
Deﬁnition 6 Let K be a totally ordered Abelian monoid and let f : En → K be an admissible
function. We deﬁne the map Mf : Tn → G n such that Mf (τ) is the graph on the vertices [n] whose
edges are the {i, j } such that f ({i, j }) ≥ f (e) for every edge e ∈ Eτ belonging to the path from i to
j through τ.
9
Thus we have constructed
Gn
Tf /d47/d47 Tn
Mf
/d111/d111
Observe that τ ⊂ Mf (τ) and Tf (g) ⊂ g. Moreover, these two maps Tf , Mf satisfy the hypothesis
of the Proposition 2. This is the content of the following lem ma.
Lemma 1 Let f : En → K be an admissible function and τ ∈ T n. Let Tf and Mf be the maps
given in Deﬁnitions 5 and 6 respectively. Then
T −1
f (τ) = {g ∈ G n : τ ⊂ g ⊂ Mf (τ)}
and therefore Mf is a partition scheme in Gn.
Proof. Let g ∈ T −1
f (τ). We have τ = Tf (g) ⊂ g. Now take {i, j } ∈ Eg, and let e ∈ Eτ be any
edge belonging to the path from i to j in τ. Consider τ′ the graph obtained from τ after replacing
the edge e by {i, j }. Clearly τ′ is connected and has n − 1 edges, so it is a tree. By minimality of
τ we must have f (d) ≤ f ({i, j }), whence {i, j } ∈ EMf (τ). Therefore g ⊂ Mf (τ).
Conversely, let τ ⊂ g ⊂ Mf (τ). We must show Tf (g) = τ. By cardinality, it suﬃces to show
Tf (g) ⊂ τ. Proceeding by contradiction, take {i, j } ∈ ETf (g) \ Eτ . Consider the path pτ ({i, j }) in
τ joining i with j. Since Tf (g) ⊂ Mf (τ), f ({i, j }) is greater or equal than the corresponding value
for any edge in the path pτ ({i, j }). If we remove {i, j } from Tf (g), the tree splits into two trees.
Necessarily, at least one of the edges in the path pτ ({i, j }) joins a vertex of one tree with a vertex
of the other. Thus, by adding this edge we obtain a connected g raph with n − 1 edges, a new tree,
which contradicts the minimality of Tf (g).
We now provide an explicit construction for the admissible f unction f of Deﬁnition 5.
We start by specifying the totally ordered Abelian monoid K. Assume to have chosen an order
in En (e.g. the lexicographic order: {i, j } < {i′, j ′} if either i < i ′ or i = i′ and j < j ′). Let
N0 = N ∪ {0} and consider the set
NEn
0 =
|En| times
/bracehtipdownleft /bracehtipupright/bracehtipupleft /bracehtipdownright
N0 × · · · × N0
such that the mth entry (with 1 ≤ m ≤ |En|) of an element x ∈ NEn
0 corresponds to the mth edge
w.r.t. the order chosen of En. Now we set
K .= R∗ × NEn
0 (3.6)
An element of K is thus an ordered ( |En| + 1)-tuple such that the ﬁrst entry is a real number while
the remaining |En| entries are natural numbers or zero.
The set K deﬁned in (3.6) has a canonical structure of Abelian monoid a nd can also be endowed
with a natural total order by considering the lexicographic al order on R∗ × Nm
0 , prioritizing the
entries from left to right. It is easy to show that such an orde r is translational invariant respect to
the standard sum in K which is thus a totally ordered Abelian monoid.
We are now ready to deﬁne the function f : En → K. Let 1{i,j } be the element of NEn
0 with all
entries zero except the one at the position corresponding to the edge {i, j } which is equal to one.
10
Deﬁnition 7 Given a pair potential V and given (x1, . . . , x n) ∈ Rdn, deﬁne the function
f : En → K : {i, j } ↦→V (xi − xj) × 1{i,j } (3.7)
Remark. The function f above is, for every pair potential V and for any ( x1, . . . , x n) ∈ Rdn,
admissible according to Deﬁnition 5 and thus, according to D eﬁnition 6 and Lemma 1, the map
Mf : Tn → G n is a partition scheme in Gn. This is our new partition scheme. The advantage
to consider this new partition Mf scheme instead of the one originally proposed by Penrose is
manifestly clear in the following key lemma which practical ly concludes the proof of Proposition 1.
Lemma 2 Let V : Rd → R∗ be a stable pair potential with stability constant B, and τ ∈ T n. Then,
for every (x1, ..., x n) ∈ Rdn,
∑
{i,j }∈EMf (τ )\E+
τ
V (xi − xj) ≥ −Bn (3.8)
where f is the function given in Deﬁnition 7, Mf (τ) is the graph given in Deﬁnition 6 and E+
τ is
the subset of Eτ deﬁned in (3.3).
Proof. In the following, Vij denotes V (xi − xj), and we will make implicit use of the following
trivial fact:
(x, σ ) ≥ (x′, σ ′) ⇒ x ≥ x′ for ( x, σ ), (x′, σ ′) ∈ R∗ × NEn
0
Now we proceed to show that the inequality (3.8) holds true. T he set of edges Eτ \ E+
τ forms the
forest {τ1, ..., τ k}. Let us denote Vτs the vertex set of the tree τs of the forest. Assume i ∈ V τa,
j ∈ V τb. If a ⁄= b, the path from i to j through τ involves an edge e in E+
τ . Thus, if in addition
{i.j } ∈ EMf (τ), we have Vij ≥ Ve ≥ 0. If a = b, the path from i to j through τ is contained in τa.
Thus, if in addition {i, j } /∈ EMf (τ), we must have Vij ≤ Ve ≤ 0 for some edge e in that path. This
allows to bound:
∑
{i,j }∈EMf (τ )\E+
τ
Vij ≥
k∑
s=1
∑
{i,j }⊂Vτs
Vij ≥
k∑
s=1
−|Vτs|B ≥ −nB □
3.3 Conclusion of the proof of Proposition 1
We now have all ingredients to conclude the proof of Proposit ion 1. Indeed, for any ﬁxed conﬁgu-
ration ( x1, . . . , x n) ∈ Rdn, by Corollary 1 and Lemma 1 we have
⏐⏐⏐
∑
g∈Gn
∏
{i,j }∈Eg
(e−βV (xi−xj) − 1)
⏐⏐⏐ ≤

 ∏
{i,j }∈Eτ
(1 − e−β |V (xi−xj)|)

 e
−β ∑
{i,j }∈EMf (τ )\E+τ
V (xi−xj)
≤
≤ eβBn ∑
τ∈Tn
∏
{i,j }∈τ
(1 − e−β |V (xi−xj)|)
where f is the admissible function given in (3.7), Mf is the partition scheme given in Deﬁnition 6
and where to get the inequality of the last line we have used Le mma 2.
11
4 Proof of Theorem 1
To deduce Theorem 1 from Proposition 1 we just need to show the following easy lemma.
Lemma 3 For any τ ∈ Tn it holds
∫
Λ
dx1 . . .
∫
Λ
dxn
∏
{i,j }∈Eτ
(
1 − e−β |V (xi−xj)|
)
≤ |Λ |
[
ˆC(β )
] n−1
Proof. Without loss of generality we can always assume (eventuall y through a renomination of the
indices in the integral of the l.h.s. of equation above) that Eτ = {2, j 2}, {3, j 3}, . . . {n, j n} with
jk < k for all k = 2, . . . , n , so that
∫
Λ
dx1 . . .
∫
Λ
dxn
∏
{i,j }∈Eτ
(
1 − e−β |V (xi−xj)|
)
=
∫
Λ
dx1 . . .
∫
Λ
dxn
n∏
k=2
(
1 − e−β |V (xk−xjk )|
)
Deﬁne the following change of variables ( x1, . . . , x n) → (y1, . . . , y n) in the integral
y1 = x1, y k = xk − xjk, ∀k = 2, . . . , n (4.1)
The Jacobian matrix of such transformation (4.1), being low er triangular with entries of the diagonal
all equal to one, has determinant equal to one. Therefore we h ave
∫
Λ
dx1 . . .
∫
Λ
dxn
n−1∏
k = 1
(
1 − e−β |V (xik −xjk )|
)
≤
≤
∫
Λ
dy1
∫
R3
dy2 . . .
∫
R3
dyn
n∏
j=2
(
1 − e−β |V (yj )|
)
=
= |Λ |
[ ∫
R3
(1 − e−β |V (x)|)dx
] n−1
= |Λ |
[
ˆC(β )
] n−1
□
Theorem 1 follows now straightforwardly. Indeed, from Prop osition 1 and Lemma 3 we get the
following bound for the absolute value of the Mayer coeﬃcien t Cn(β, Λ).
|Cn(β, Λ) | ≤ 1
|Λ |
1
n!
∫
Λ
dx1 . . .
∫
Λ
dxn
⏐⏐⏐⏐⏐⏐
∑
g∈Gn
∏
{i,j }∈Eg
[
e−βV (xi−xj)| − 1
]
⏐⏐⏐⏐⏐⏐
≤
≤ eβBn
|Λ |
1
n!
∫
Λ
dx1 . . .
∫
Λ
dxn
∑
τ∈Tn
∏
{i,j }∈Eτ
(1 − e−β |V (xi−xj)|) =
= eβBn
|Λ |
1
n!
∑
τ∈Tn
∫
Λ
dx1 . . .
∫
Λ
dxn
∏
{i,j }∈Eτ
(1 − e−β |V (xi−xj)|) ≤
≤ eβBn 1
n!
[
ˆC(β )
] n−1 ∑
τ∈Tn
1 = eβBn nn−2
n!
[
ˆC(β )
] n−1
where in the last line we have also used the Cayley formula ∑
τ∈Tn 1 = |Tn| = nn−2 (see [4]). This
concludes the proof of Theorem 1.
12
