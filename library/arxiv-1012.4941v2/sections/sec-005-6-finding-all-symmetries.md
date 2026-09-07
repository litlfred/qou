---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-005-6-finding-all-symmetries
section_title: "Finding All Symmetries"
section_number: 6
pages: 13-16
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
For the algorithms presented it is never necessary to know the ent ire group of automorphisms
of LP(A,b,c ) or ILP( A,b,c ). Generally, any subgroup will do, the larger the better. Yet
here we would like to discuss the question of how to ﬁnd automorphism s of integer linear
programs. From the input data we will construct a labeled graph G( A,b,c ) whose group of
labeled automorphisms coincides with Sym(ILP( A,b,c )).
Expressing symmetry in optimization via graph automorphisms is not a new idea: the
linear automorphism group of a polytope and of a linear program can b e obtained by com-
puting the automorphism group of a certain graph as described by B remner, Dutour Sikiri´ c,
and Sch¨ urmann [4]. The combinatorial automorphisms of a polytope are the (labeled) graph
automorphisms of the bipartite graph encoded by the vertex-edg e-incidences. This directly
follows from the fact that the face lattice of a polytope is atomic and coatomic; see Kaibel
14 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
and Schwartz [9]. Liberti studies automorphisms of optimization pro blems which are more
general than integer linear programs [12]. His approach, however, deals with expression
trees obtained from a speciﬁc encoding of the optimization problem. None of these concepts
seems to be directly related to the kind of symmetry studied here. A n idea similar to ours,
however, has been applied by Berthold and Pfetsch [1] to ﬁnd symm etries of 0/1-ILPs.
The complexity status of the graph isomorphism problem is notorious ly open. While the
known algorithms for determining the automorphism group of a grap h require exponential
time, there exist software packages, for instance, nauty [16] or SymPol [21], that can solve
this problem very well in practice.
For a given matrix A∈ Rm×n, right hand side b∈ Rm, and objective function c∈ Rn we
will now associate two undirected simple graphs, the ILP graph G(A,b,c ), and the restricted
ILP graph G′(A,b,c ). For the sake of a simpliﬁed exposition we start out by describing th e
restricted ILP graph. Throughout we assume that the rows of th e extended matrix (A|b) are
normalized as described in Remark 5. We have one node αij for each position in the matrix
A, one node ρi for each row, and one node ζj for each column, that is, ( i,j )∈ [m]× [n],
where [n] = {1, 2,...,n }. Further, we have one node κu for each distinct coeﬃcient u in
the matrix A, one node λv for each distinct coeﬃcient v of b, and one node µw for each
distinct coeﬃcient w of c. This gives a total of mn +m +n +nA +nb +nc nodes, where
nA,nb, and nc denotes the respective number of diﬀerent entries in A,b, and c. The nodes
receive labels in the following way: all positions share the same label, th e rows receive a
second, and the columns a third label. Each node corresponding to o ne of the coeﬃcients
receives an individual label. This way we arrive at nA +nb +nc + 3 labels altogether. The
edges of G ′(A,b,c ) are deﬁned as follows: the node αij is adjacent to ρi and ζj as well as
to the coeﬃcient node which represents the coeﬃcient aij of the matrix A. Moreover, the
row node ρi is adjacent to the node λbi , and the node ζj is adjacent to the node µcj . This
totals to 3mn +m +n edges.
Example 36. The reduced ILP graph of the integer linear program
(10)
max x1 + x2 + x3
s.t. x1 + 2 x2 ≤ 3
x2 + 2 x3 ≤ 3
2x1 + x3 ≤ 3, x i∈ Z
is shown in Figure 1.
Letγ be an automorphism of G ′(A,b,c ) which respects all node labels. Since the common
label of the column nodes is preserved γ induces a column permutation ψγ∈ Sym(n). Now
ψγ acts on the standard basis {e1,e 2,...,e n}, and by linear extension we obtain a linear
transformation which we denote ψ∗
γ.
Lemma 37. The linear transformation ψ∗
γ is a symmetry of ILP(A,b,c ).
Proof. As above let γ be a labeled automorphism of G ′ = G ′(A,b,c ) with induced column
permutation ψ = ψγ and linear transformation ψ∗∈ Sym(n)≤ GLnR. As for the column
nodes the graph automorphism γ also induces a permutation φ∈ Sym(m) of the row nodes
of G ′. The position nodes αij form a label class of their own, and so they are permuted by
γ as well. Since each position node is adjacent to precisely one row and o ne column node
we infer that γ(αij) = αφ(i),ψ(j). Each position node is adjacent to precisely one matrix
coeﬃcient node, each of which forms a singleton label class. This implie s that the coeﬃcient
aij corresponding to the node αij is the same as the coeﬃcient aφ(i),ψ(j). Likewise we obtain
bi =bφ(i) and cj =cψ(j). This means that ψ∗
γ is a symmetry of ILP( A,b,c ). □
SYMMETRIC LINEAR AND INTEGER PROGRAMS 15
3 1
0 1 2
ρ1 ρ2 ρ3 ζ1 ζ2 ζ3
α11 α12 α13 α21 α22 α23 α31 α32 α33
Figure 1. The reduced ILP graph for (10).
Proposition 38. The map γ↦→ψ∗
γ is an isomorphism from the group of labeled automor-
phisms of the graph G′(A,b,c ) to the group Sym(ILP(A,b,c ))∩ Sym(n).
Proof. We describe the inverse map. To this end let σ be a symmetry of ILP( A,b,c ) which
acts on the standard basis of Rn. Hence σ induces a permutation φ of the rows of the
extended matrix (A|b) and a permutation ψ of the columns of A. It is obvious how φ and
ψ induce permutations of the row nodes and of the column nodes of G ′. By the same
reasoning as in the proof of Lemma 37 the pair ( φ,ψ ) uniquely extends to a labeled graph
automorphism γ(σ) of the reduced ILP graph.
We omit the straightforward proofs that the equations γ(ψ∗
γ) = γ and ψ∗
γ(σ) = σ both
hold. From these it follows that the map γ↦→ψ∗
γ is bijective. In both groups the multipli-
cations are given by concatenations of maps. A direct computation yields ψ∗
γ1γ2 =ψ∗
γ1ψ∗
γ2 ;
all maps are acting on the left. Hence the group structures are pr eserved. □
We now explain how the full ILP graph G( A,b,c ) diﬀers from the restricted ILP graph
G′(A,b,c ). The key to the construction of G ′(A,b,c ) is the map γ↦→ψ∗
γ yielding a linear
transformation which acts as a permutation of the standard basis of Rn. In order to allow for
signed permutations certain nodes have to be duplicated: each colu mn node ζj in G ′(A,b,c )
gets a twin node ˆζj in G(A,b,c ), each matrix coeﬃcient node αij corresponding to a non-
zero coeﬃcient gets a twin node ˆ αij. Moreover, we add further nodes representing negatives
of non-zero coeﬃcients in the matrix A and the objective function c unless nodes with
these labels already exist. This way ILP( A,b,c ) has less than twice as many nodes as
ILP′(A,b,c ); it is always strictly less as the nodes corresponding to the coeﬃcie nts in b are
never duplicated. We also add edges such that ﬁrst ˆ αij is adjacent to ρi and ˆζj for all i
and j, second ˆζj is adjacent to µ−cj , third ˆαij is adjacent to κ−aij , and, ﬁnally, the twins
are matched up: αij is adjacent to ˆαij and ˆζj is adjacent to ζj. The labeling is extended
in a way such that twins share the same label; the nodes newly introdu ced for negatives of
coeﬃcients receive new singleton labels.
Each labeled graph automorphism of G ′(A,b,c ) uniquely extends to a labeled graph
automorphism of G(A,b,c ), but the automorphism group of the non-reduced ILP graph is
larger, in general. We have the following result.
16 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
Theorem 39. The group of labeled graph automorphisms of G(A,b,c ) is isomorphic to the
group of symmetries of ILP(A,b,c ).
Proof. One can follow the strategy in the proof of Proposition 38. We know t hat a labeled
graph automorphism of G ′(A,b,c ) encodes a symmetry of ILP( A,b,c ) which permutes the
set{e1,e 2,...,e n}. Now a labeled graph automorphism of G( A,b,c ) may map a column
node ζj to some node ˆζk. But then it follows that ˆζj is mapped to ζk since ˆζj is the only
column node adjacent to ζj, and ζk is the only column node adjacent to ˆζk. This shows that
the permutation of the column nodes can be extended to a linear tra nsformation. As in the
proof of Proposition 38 one can show that this linear transformatio n is a symmetry of the
integer linear program. Conversely, each such symmetry acts like a signed permutation on
the signed standard basis and yields a labeled isomorphism of the grap h G(A,b,c ). □
Roughly speaking, a class C of graphs is graph isomorphism complete if the problem of
deciding isomorphy for any two graphs in C is as diﬃcult as for general graphs, up to a poly-
nomial time transformation. For a precise deﬁnition, for instance, see the monograph [10].
The next result is not only of theoretical interest. To the contrar y, for practical applica-
tions it can be read as: ﬁnding the symmetries of an integer linear pro gram via reducing to
automorphisms of suitable (labeled) graphs, is the right thing to do.
Theorem 40. The classes of ILP graphs and reduced ILP graphs are both grap h isomor-
phism complete.
Proof. We only prove that the class of reduced ILP graphs is graph isomorp hism complete.
It is known that the class of bipartite graphs is graph isomorphism co mplete. Hence it
suﬃces to encode an arbitrary bipartite graph as a reduced ILP gr aph, which is not too
large.
Let G = (V,E ) be an undirected bipartite graph with m +n nodes V = U∪W =
{u1,...,u m}∪{ w1,...,w n}. As our matrix AG = (aij)∈ Rm×n we take the bipartite
adjacency matrix of G, that is,
aij =
{
1 if {ui,wj}∈ E
0 otherwise .
For a second bipartite graph G′ it is easy to see that the reduced ILP graph of ILP( AG, /BD , /BD )
is isomorphic to the reduced ILP graph of ILP( AG′, /BD , /BD ) if and only if G is isomorphic to
G′. □
Remark 41. Rehn investigates arbitrary automorphisms of the integer lattice Zn in the
context of polyhedral geometry [20]. In particular, his modiﬁcatio n of a backtracking al-
gorithm of Plesken and Souvignier [18] allows to obtain matrix genera tors of the group of
symmetries. For practical applications this should be superior to ou r approach via graph
automorphisms if the number m of constraints is much larger than the dimension n.
