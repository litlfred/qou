---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-001-2-automorphisms-of-linear-programs
section_title: "Automorphisms of Linear Programs"
section_number: 2
pages: 2-7
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
The purpose of this section is to introduce the notation and to collec t basic facts for future
reference. The results of this section up to and including Corollary 1 4 can be found in the
literature which is why we skip some of the proofs.
We consider linear programs LP( A,b,c ) of the form
(1) max ctx
s.t. Ax≤b, x∈ Rn
where A∈ Rm×n, b∈ Rm, and c∈ Rn\{ 0}. Throughout we will assume that the set
P (A,b ) := {x∈ Rn|Ax≤ b} of feasible points is not empty, and hence it is a convex
polyhedron, which may be bounded or unbounded. We will also assume that an optimal
solution exists. This is to say, our linear program LP( A,b,c ) is bounded even if the feasible
region may be unbounded. In this case the set of optimal solutions f orms a non-empty face
of P (A,b ). Our ﬁnal assumption c⁄= 0 is not essential for the algorithms below, but it
allows to simplify the exposition somewhat.
Each row of the matrix A corresponds to one linear inequality. Suppose that one of these
rows is the zero vector. Then the corresponding right hand side mu st be non-negative, since
otherwise the linear program would be infeasible, and this was explicitly excluded above.
But then this linear inequality is trivially satisﬁed. Therefore we will fur ther assume that the
matrixA does not contain any zero rows. In this case each row deﬁnes an aﬃ ne hyperplane.
This way LP(A,b,c ) gives rise to an arrangement H(A,b ) of m labeled aﬃne hyperplanes
in Rn.
Deﬁnition 1. An automorphism of the linear program LP(A,b,c ) is a linear transformation
in GLnR which induces a permutation of H(A,b ), which leaves P (A,b ) invariant, and which
does not change the objective value ctx for any feasible point x∈P (A,b ).
The objective function is linear, and hence it follows that an automor phism of LP(A,b,c )
does not change the objective value on the linear span lin( P (A,b )) of the feasible points.
One could also take more general aﬃne transformations into accou nt. In all what comes
below this would require a number of straightforward changes. We r efrain from doing so for
the sake of a clearer exposition. The following examples show that th e three properties to
be satisﬁed by a linear automorphism are mutually independent.
Example 2. For m = n = 1 let A = 1, b = 0, and c = 1. The feasible region is the
non-positive ray R≤0. Multiplication with any positive real number γ leaves the feasible
region and the hyperplane arrangement (consisting of the origin) in variant. If γ⁄= 1 the
objective function is not preserved.
SYMMETRIC LINEAR AND INTEGER PROGRAMS 3
Example 3. Form =n = 2 let
A =
(−1 0
0 −1
)
, b = 0 , c =
(−1
0
)
.
Then P (A,b ) is the non-negative quadrant in R2. Now γ =
(1 0
0 −1
)
leaves the coordinate
hyperplane arrangement H(A,b ) invariant, but it changes the feasible region. For each
x∈ R2 we have ctx =ctγx.
Example 4. Form = 3 and n = 2 let
A =


−1 0
0 −1
−1 −2

 , b = 0 , c =− /BD .
The feasible region is the non-negative quadrant in R2; the third inequality is redundant.
The linear transformation γ = ( 0 1
1 0 ) leaves the feasible region invariant, and it satisﬁes
ctx =ctγx for all x∈ R. The hyperplane arrangement H(A,b ) is changed.
For more examples see [3]. There it is also shown that each ﬁnite (perm utation) group
occurs as the group of automorphisms of a linear program.
Remark 5. It is always possible to scale the rows of the extended matrix ( A|b) such that
the leftmost non-zero coeﬃcient is ±1. This allows to remove duplicate inequalities from
the input by sorting. The complexity of sorting the rows by pair-wise comparison is of order
O(mn logm). This can be neglected in the asymptotic analysis of our algorithms b elow since
it is always dominated. This way we can always assume that the hyperp lanes in H(A,b ),
that is, the inequalities, and the rows of the extended matrix ( A|b) are in a one-to-one
correspondence. In the rational case it is more natural to scale t he inequalities to integer
coeﬃcients which are coprime. This is what we will usually do. For a more sophisticated
algorithm to sort out equivalent constraints, see Bixby and Wagner [2].
Since we view points in Rn as column vectors, a matrix γ representing a linear transfor-
mation acts by multiplication on the left. The adjoint action on the row space, and thus
on the set of linear inequalities, is by multiplication of the inverse trans pose γ−t on the
right. The set of linear transformations permuting the arrangeme nt H(A,b ) forms a closed
subgroup of GL nR, that is, a linear Lie group. Similarly, the set of linear transformation s
leaving the feasible region P (A,b ) invariant forms a linear Lie group. It follows that the set
Aut(LP(a,b,c )) of automorphisms of the linear program LP( A,b,c ) also forms a linear Lie
group. For basic facts about (linear) Lie groups, see Rossmann [22 ].
Remark 6. Clearly, the value and the set of optimal solutions of a linear program only
depend on the non-redundant constraints. At the expense of on e linear program per con-
straint one can get rid of the redundant ones. This obviously does n ot help to reduce the
complexity of solving the linear program given since the linear program for a redundancy
check is of the same size. However, for more costly algorithmic prob lems, like integer pro-
gramming as is discussed below, this reduction can be useful. In part icular, this will be
the case when the group of automorphisms becomes larger, see Ex ample 4. Notice that the
notion of “invariance” from [6, Deﬁnition 3.1], specialized to linear prog ramming, implies
that redundant constraints are going to be ignored.
The following result is a consequence of the combinatorial propertie s of a convex poly-
tope P : the faces of P are partially ordered by inclusion, and this partially ordered set
4 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
forms a lattice. The automorphisms of this lattice, the face lattice of P , are called combi-
natorial automorphisms . Each linear (or aﬃne or projective) automorphism of P induces
a combinatorial automorphism, but, in general, a polytope may have many combinatorial
automorphisms which are not linearly induced. See Ziegler [24] for the details.
Lemma 7. If the feasible region P (A,b ) is bounded and full-dimensional, then the automor-
phism group Aut(LP(A,b,c )) is ﬁnite. Moreover, the objective function c satisﬁes ctγx =ctx
for all x∈ Rn and γ∈ Aut(LP(A,b,c )).
Proof. Let v be a vertex of the polytope P = P (A,b ). Since dim P = n there are vertices
w1,w 2,...,w n each of which shares an edge with v and such that the diﬀerence vectors w1−
v,w 2−v,...,w n−v form a basis of Rn. This implies that each combinatorial automorphism
of P is induced by at most one linear automorphism. Hence the group Aut( LP(A,b,c ))
is contained in the group of combinatorial automorphisms of P , which is ﬁnite. While
Deﬁnition 1 asks that each feasible point is mapped to a (feasible) point with the same
objective value, the additional claim deals with all points, feasible or n ot. However, this
follows from lin(P (A,b )) = Rn as c is linear. □
If the polyhedron P (A,b ) is not full-dimensional, then the automorphism group is a direct
product of the group of automorphisms ﬁxing the linear span of P (A,b ) with a full general
linear group of the orthogonal complement. In the sequel we will th erefore restrict our
attention to the full-dimensional case.
Deﬁnition 8. Given a subset Y ⊆ Rn and a group Γ ≤ GLR acting on Y , the set of ﬁxed
points of Y with respect to an element γ∈ Γ is deﬁned by
Fixγ(Y ) := {y∈Y |γy =y} .
Therefore, the set of ﬁxed points of Y with respect to Γ is given by
FixΓ (Y ) := {y∈Y |γy =y for all γ∈ Γ} =
⋂
γ∈Γ
Fixγ(Y ).
The set of ﬁxed points Fix γ(Rn) is the (possibly zero-dimensional) eigenspace Eig( γ, 1)
of the linear transformation γ with respect to the eigenvalue 1. This implies that Fix Γ (Rn)
is a linear subspace for any group Γ of linear transformations. More generally, Fix Γ (Y ) is
the intersection of this subspace with the set Y .
Remark 9. If the linear group Γ ≤ GLnR is generated by the set G⊂ Γ, then
FixΓ (Rn) =
⋂
γ∈G
Fixγ(Rn) =
⋂
γ∈G
Eig(γ, 1).
In particular, if G is ﬁnite, that is, if the group Γ is ﬁnitely generated, this leads to an
algorithm to compute (a primal or dual basis of) the ﬁxed space by s olving one linear
system of equations per transformation in the generating set G.
Remark 10. Let Γ ≤ Aut(LP(A,b,c )) be a group of automorphisms of the linear program
LP(A,b,c ) such that P (A,b ) is bounded and full-dimensional. Then, by Lemma 7, the
set of ﬁxed points Fix Γ (Rn) contains the one-dimensional linear subspace spanned by the
objective vector c.
For any ﬁnite set S⊂ Rn let
β(S) := 1
|S|
∑
v∈S
v
SYMMETRIC LINEAR AND INTEGER PROGRAMS 5
be its barycenter. The two subsequent results are basic observations from repres entation
theory, not restricted to applications in (linear) optimization. For a brief proof, for instance,
see [23, Lemma 3.5].
Lemma 11. The map
Rn→ FixΓ (Rn), v↦→β(Γv)
which sends a point to the barycenter of its Γ -orbit is a linear projection onto the ﬁxed space.
LetS⊆ Rn be a ﬁnite set which is spanning, that is, we require lin( S) = Rn. Further let
Γ be a ﬁnite subgroup of GL nR acting on S. Phrased diﬀerently, we are considering a linear
representation of an abstract group Γ on the vector space Rn which induces a permutation
representation on the set S. In this case Γ splits S into disjoint orbits O1,O 2,...,O k. In
our applications below, S will usually be the set of vertices of some polytope which linearly
spans Rn.
Lemma 12. For the ﬁxed space of Γ we have
FixΓ (Rn) = lin {β(O1),β (O2),...,β (Ok)}.
In particular, dim FixΓ (Rn)≤k.
Proof. SinceS =O1∪O2∪···∪ Ok is spanning and since the union of the orbits gives S it
follows that
(2) Rn = lin( O1) + lin(O2) +··· + lin(Ok).
Fori∈{ 1, 2,...,k } the linear subspace lin( Oi) is Γ-invariant. If we apply the surjective
linear map v↦→β(Γv) from Lemma 11 to the set S, we obtain a generating set for Fix Γ (Rn).
Applying the same map to a single orbit Oi similarly yields a generating set for Fix Γ (lin(Oi)).
Now the claim follows from the equation Γ Oi =Oi. □
Notice that the sum decomposition (2) is not necessarily direct. We n ow apply the results
obtained so far to a ﬁnite group of automorphisms of a linear progra m.
Proposition 13. Let Γ≤ Aut(LP(A,b,c )) be ﬁnite. If x∈ Rn is an arbitrary point, the
barycenter of its Γ -orbit satisﬁes ctβ(Γx) = ctx. If, moreover, x∈P (A,b ) is feasible, then
β(Γx) is feasible, too.
Geometrically this means that the points of one orbit are in the same a ﬃne hyperplane
orthogonal to c.
Proof. As the objective function is constant on the orbit Γ x it follows that ctβ(Γx) = ctx.
If x is a feasible point, then γx is also feasible for all γ∈ Γ. So the barycenter β(Γx) is a
convex combination of feasible points. The claim follows as the feasible region is convex. □
Since we assumed that LP( A,b,c ) has an optimal solution, the following is an immediate
consequence of the preceding result.
Corollary 14. There exists an optimal solution of LP(A,b,c ) which is a ﬁxed point with
respect to the entire automorphism group Aut(LP(A,b,c )).
Up to minor technical details Theorem 3.3 of [6] generalizes Corollary 1 4 to semi-deﬁnite
programming.
Let LP(A,b,c ) be a linear program with P (A,b ) bounded and full-dimensional, and let
Γ = ⟨γ1,γ 2,...,γ t⟩ be a ﬁnite subgroup of Aut(LP( A,b,c )). Following Remark 9 we can
compute a matrix E such that the kernel {x|Ex = 0} is the ﬁxed space Fix Γ (Rn): for each
6 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
γi we determine a dual basis for the eigenspace {x| (γi− id)x = 0} by solving a square
system of linear equations. The total number of operations to do s o is of order O(tn3).
Throughout this paper we measure algorithmic complexity in the RAM m odel; that is, we
ignore the encoding lengths of real numbers, and all arithmetic ope rations are assumed to
take constant time. The group Γ acts on the rows of the extended matrix (A|b), and we
deﬁne a new extended matrix ( A′|b′) by summing the rows of the same Γ-orbit. We have
the following general result.
Theorem 15. The polyhedron
P ′ = {x∈ Rn |A′x≤b′, Ex= 0}
is the set FixΓ (P (A,b )) of feasible points which is ﬁxed under the action of Γ . In particular,
P ′ ={β(Γx)|x∈P (A,b )}. Each optimal solution of the linear program
(3)
max ctx
s.t.


A′
E
−E

x≤


b′
0
0

 , x∈ Rn
is an optimal solution of LP(A,b,c ), and the objective values are the same.
Proof. We constructed the matrix E to guarantee that each ﬁxed point in P = P (A,b )
satisﬁes the equation Ex = 0. Further, each inequality of the system A′x≤b′ is a positive
linear combination of valid inequalities. It follows that Fix Γ (P ) is contained in P ′.
To prove the reverse inclusion consider a point x which is ﬁxed by each transformation
in Γ but which is not contained in P . Then for some index i we have the strict inequality
ai,·x> bi. Without loss of generality we can assume that the ﬁrst k rowsa1,·,a 2,·,...,a k,·
of A form the Γ-orbit of the row ai,·. It follows that b1 = b2 =··· = bk = bi. Moreover,
since x is a ﬁxed point we have
a1,·x = a2,·x = ··· = a1,·x =ai,·x > bi.
This implies that ( ∑ k
j=1aj,·)x>kb i, and hence x is not contained in P ′. We conclude that
P ′ is the set of points in P ﬁxed by each transformation of Γ. Now Lemma 11 says that
P ′ is the image of P under the map x↦→β(Γx). The claim about the linear program (3)
follows from Corollary 14. □
Remark 16. It has been observed by Scharlau and Sch¨ urmann 1 that the vertices of the
polyhedron P ′ are barycenters of orbits of vertices of P . This is a consequence of the fact
that P ′ is the image of P under the linear map x↦→β(Γx).
Corollary 14 and Theorem 15 yield a direct algorithm for solving a symme tric linear
program: instead of solving LP( A,b,c ) one can solve the linear program (3). The beneﬁt is
the following: The larger the group Γ ≤ Aut(LP(A,b,c )) the smaller the dimension of the
ﬁxed space and the number of constraints.
Remark 17. Formally, the feasible points of the derived linear program live in the sa me
space Rn as the original linear program. However, an algorithm based on the S implex
Method directly beneﬁts if the solutions are contained in a proper su bspace: the rows of
the matrix E describing the ﬁxed space never have to be exchanged in a Simplex ta bleau.
Alternatively, one can project Fix Γ (Rn) onto a full-dimensional coordinate subspace, solve
the projected linear program and lift back.
1private communication
SYMMETRIC LINEAR AND INTEGER PROGRAMS 7
In the special case where the linear program admits a group of auto morphisms acting on
the standard basis of Rn (that is, the groups acts by permuting the columns) it is standard
optimization practice to identify variables in the same orbit, and to so lve the reduced linear
program. Theorem 15 generalizes this approach to arbitrary grou ps of automorphisms.
