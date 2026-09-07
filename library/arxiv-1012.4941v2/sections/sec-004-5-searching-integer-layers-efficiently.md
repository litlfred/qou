---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-004-5-searching-integer-layers-efficiently
section_title: "Searching Integer Layers Efficiently"
section_number: 5
pages: 11-13
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
The question remaining is how to test ILP-feasibility of a c-layer in an eﬃcient way. Our
key observation is that some optimal integral solution is close to the ﬁxed space if the group
of symmetries acts suﬃciently transitive.
Deﬁnition 29. Given a c-layer with center z, an integral point in the c-layer is a core point
if it minimizes the distance to z.
Example 30. For the objective function c = /BD and an integer k =qn +r with q∈ Z and
r∈{ 0, 1,...,n − 1}, the set of core points in the k-th layer consists of all integer points with
r coeﬃcients equal to q +1 and n−r coeﬃcients equal to q. In particular, the number of core
points in this case equals
(n
r
)
. These core points are the vertices of an ( r,n )-hypersimplex,
translated by the vector q /BD .
For the algorithms below the geometric structure of the set of cor e points is very relevant.
We therefore make a short digression: the ( r,n )-hypersimplex ∆( r,n ) is the 0 /1-polytope
with vertices
eS =
∑
i∈S
ei,
where S ranges over all r-element subsets of [ n]. The hypersimplices are highly regular
structures, and this yields the following.
Proposition 31. Let Γ≤ GLnR be a linear group which acts µ-transitively on the standard
basis. Then Γ acts transitively on the set of vertices of the (r,n )-hypersimplex for any
r∈{ 0, 1,...,µ }∪{ n−µ,n−µ + 1,...,n }.
Proof. By assumption Γ acts transitively on the r-element subsets of [ n] for r≤µ. Since Γ
is a linear group it thus acts transitively on the set of vertices of ∆( r,n ). The corresponding
claim for the remaining hypersimplices follows since ∆( r,n ) is aﬃnely isomorphic to ∆( n−
r,n ) via the map x↦→/BD −x. □
Below we will apply the previous results in the special case where µ≥⌊n/2⌋. Then the
groups acts transitively on the sets of vertices of all hypersimplices.
Lemma 32. Let x ∈ P (A,b ) be an LP-feasible point in the k-th c-layer, and let γ ∈
Sym(ILP(A,b,c )) with γx⁄=x. Then any point in the interior of the line segment [x,γx ] is
LP-feasible and closer to the center of the k-th c-layer than x.
Proof. Since γ is an orthogonal linear map it preserves distances. The center z of the k-th
c-layer is ﬁxed under γ, and this implies that ( x,z,γx ) is an isosceles triangle. We infer that
‖p−z‖<‖x−z‖ for all points p in the interior of [ x,γx ]. Since γ is an automorphism of
the linear relaxation LP( A,b,c ) the point γx is feasible, too. The feasible region is convex,
and hence p is feasible. □
Theorem 33. Suppose that Γ ≤ Sym(ILP(A,b, /BD )) acts (⌊n/2⌋ + 1) -transitively on the
standard basis of Rn, and n≥ 2. Then either each core point in the k-th /BD -layer is feasible
or H
/BD ,k does not contain any feasible point.
Proof. Let x be a feasible integer point in the k-th /BD -layer which is not a core point. We
will show that there is another feasible integer point which is closer to the center, and this
will prove the claim.
Due to the invariance of Zn under translation by integer vectors we may assume that
k ∈ {0, 1,...,n − 1}. Since x is not a core point, in particular, it is not the center of
12 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
the k-th layer. Hence x is not contained in the ﬁxed space R/BD , which means that not all
coordinates of x are the same. We split the set [ n] of coordinate directions into two subsets
by considering
{i|xi is even} and {i|xi is odd} .
Then one of the sets — denoted by I — contains at least ⌊(n + 1)/2⌋ elements, while
the other set J has at most ⌊n/2⌋ elements. We will employ the ⌊n/2⌋-transitivity of the
automorphism group to control J, and the additional degree of freedom to produce two
distinct feasible integer points. We distinguish two cases.
(i) Suppose that x has two diﬀerent coordinates, say xu and xv, which are in the
same congruence class modulo two. That is, the set {u,v} is contained in either
I or J. Observe that this condition is satisﬁed whenever x has at least three
pairwise distinct coordinates. Due to the ( ⌊n/2⌋ + 1)-transitivity of Γ there is an
automorphism γ∈ Γ which leaves J invariant and which maps u to v. Since J
is invariant, its complement I = [n]\J is invariant, too. Notice that we do not
require the set J to be non-empty (if {u,v}⊆ I).
Letting x′ = γx we observe that xi and x′
i are congruent modulo two for all
i∈ [n]. Since xu⁄=xv =xγ(u) =x′
u we have x⁄=x′, and hence
y = 1
2 (x +x′) = 1
2 (x +γx)
is an integer point in the interval [ x,γx ].
(ii) Otherwise the point x has exactly two diﬀerent coordinates xu andxv, one of them
being even, the other one odd. Without loss of generality, xi =xu for all i∈I and
xj =xv for all j∈J. Due to the transitivity of Γ there is an automorphism γ∈ Γ
with γeu =ev. Then x and γx are distinct points. Consider an interior point
(5) y = λx + (1−λ)γx for 0 <λ< 1
in the line segment [ x,γx ]. We want to ﬁnd a parameter λ such that y is integral.
As x has only two distinct coordinates the i-th coordinate of y can attain the
following values only:
yi = λxu + (1−λ)xu = xu or(6)
yi = λxv + (1−λ)xv = xv or(7)
yi = λxu + (1−λ)xv = λ(xu−xv) +xv or(8)
yi = λxv + (1−λ)xu = λ(xv−xu) +xu.(9)
Sincex is integral coordinates of types (6) and (7) are integers for arbit rary param-
etersλ∈ (0, 1). The coordinates of types (8) and (9) are integral if λ·|xu−xv|∈ Z.
We assumed that x is contained in the k-th /BD -layer for some k = 0, 1,...,n − 1
and that it is not a core point. In Example 30 it has been observed tha t the core
points in these layers are the vertices of a translated hypersimplex . We learned
that some coordinate diﬀerence |xi−xk| must exceed one. Since all coeﬃcients are
equal to either xu or xv it follows that |xu−xv|≥ 2. We can now set
λ = 1
|xu−xv|
in the formula (5).
SYMMETRIC LINEAR AND INTEGER PROGRAMS 13
Input: (A,b ) such that Sym(ILP( A,b, /BD )) acts (⌊n/2⌋ + 1)-transitively on standard
basis
Output: optimal solution of ILP( A,b, /BD ) or “infeasible”
1 let z =ζ /BD be a symmetric optimal solution of the LP relaxation LP( A,b, /BD )
2 d←⌊nζ⌋− n⌊ζ⌋
3 repeat
4 x← (⌊ζ⌋ + 1,..., ⌊ζ⌋ + 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
d
,⌊ζ⌋,..., ⌊ζ⌋/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
n−d
)
5 if x infeasible then
6 d←d− 1
7 until feasible x found or d< 0
8 return x or “infeasible”
Algorithm B: Core point algorithm
In both cases we obtain an integral point y in the interior of the interval [ x,γx ]. By
Lemma 32, such a point is always closer to the center than x. This shows that there exists
a feasible core point in the same layer as x. Applying Proposition 31 with µ =⌊n/2⌋ + 1
yields that then each core point must be feasible. □
Now Algorithm A can be modiﬁed in Step 5 to check a single core point per layer for
feasibility, provided that the group of automorphisms of the ILP ac ts at least (⌊n/2⌋ + 1)-
transitively. This is our Core Point Algorithm B.
Corollary 34. For given A and b such that Sym(ILP(A,b, /BD )) acts (⌊n/2⌋ + 1)-transitively
on the standard basis the Core Point Algorithm B solves the in teger linear program ILP(A,b, /BD )
in O(mn2) time.
Proof. The correctness follows from Theorems 27 and 33. The main loop of t he algorithm
is executed at most n times. In each step the costs are dominated by checking one point in
Rn for feasibility against m linear inequalities. □
Remark 35. The linear search in Algorithms A and B cannot be substituted by a dire ct
bisectional approach. The reason is that the set of all k in{0, 1,..., ⌊nζ⌋− n⌊ζ⌋} such that
the k-th /BD -layer contains a feasible point is not necessarily (the set of integer points of) an
interval.
