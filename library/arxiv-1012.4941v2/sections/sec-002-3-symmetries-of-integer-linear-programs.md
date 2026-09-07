---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-002-3-symmetries-of-integer-linear-programs
section_title: "Symmetries of Integer Linear Programs"
section_number: 3
pages: 7-9
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
We now turn to our main focus. Associated with LP( A,b,c ) is the integer linear program
(4) max ctx
s.t. Ax≤b, x∈ Zn,
which we denote as ILP( A,b,c ). Throughout we make the same assumptions as above: the
linear program LP( A,b,c ) is feasible, the matrix A does not have any zero rows, and the
inequalities bijectively correspond to the hyperplane arrangement H(A,b ); see Remark 5.
Deﬁnition 18. A symmetry of the integer linear program ILP( A,b,c ) is an automorphism
of LP(A,b,c ) which acts on the signed standard basis {±e1,±e2,..., ±en} of Rn as a signed
permutation.
The symmetries of the integer linear program (4) form a group Sym( ILP(A,b,c )) which
is a subgroup of the group O nZ, the group of all 0 /1/−1-matrices with exactly one non-zero
entry per row and column. We have O nZ = OnR∩ GLnZ, and O nZ is isomorphic to the
Coxeter group of type Bn, the group of automorphisms of the regular n-dimensional cube
and its polar, the regular n-dimensional cross polytope. As a consequence, the group of
symmetries of an integer linear program is ﬁnite, even if Aut(LP( A,b,c )) is inﬁnite.
The motivation for our deﬁnition is Lie-theoretical: let Γ be any ﬁnite s ubgroup of GLnZ.
Then Γ is a compact subgroup of GL nR, hence it is contained in (a conjugate copy of) the
maximal compact subgroup O nR. It follows that, up to conjugation in GL nR, the group Γ
is a subgroup of O nZ.
As an abstract group O nZ is isomorphic to the wreath product
Z2≀ Sym(n) = ( Z2)n ⋊ Sym(n),
where Z2 is the cyclic group of order two and Sym( n) is the symmetric group of degree n;
the group Sym(n) acts on the direct product ( Z2)n by permuting the factors. Each element
of OnZ can be written as a product of a sign vector and a permutation. Sinc e a permutation
is a product of disjoint cycles, each signed permutation is a product of signed cycles which
are disjoint. In terms of notation we write the signs between the ind ices within a cycle. This
is to say, (1+2−4+3−) denotes the signed permutation matrix


0 0 −1 0
1 0 0 0
0 0 0 1
0 −1 0 0


which is to be multiplied to column vectors from the left.
Remark 19. In the optimization literature the authors often restrict their att ention to
symmetries permuting the standard basis vectors; for instance, see Margot [13] and the
references listed there. However, our more general analysis belo w shows that taking signed
permutations into account does not cause any extra eﬀort. More over, if the polyhedron
P (A,b ) is full-dimensional and bounded the group of automorphisms of the linear relaxation
is already ﬁnite by Lemma 7. Then Aut(LP( A,b,c ))∩ GLnZ is already contained in O nZ by
8 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
the Lie-theoretical argument given above. Hence, at least in this c ase, considering groups
of signed permutations is a natural choice.
Before we will inspect groups of symmetries of integer linear progra ms we need to collect
a few basic results on the action of the group O nZ on the entire space Rn. Throughout let
Γ be a subgroup of O nZ. Then Γ acts on the standard basis
S = {±e1,±e2,..., ±en}.
In the sequel we will always consider this particular action of Γ. Ther e are two kinds of
orbits to distinguish: the bipolar orbits contain at least one pair ±ei, while the unipolar
orbits do not. Since Γ is a linear group, a signed permutation σ∈ Γ with σei = ǫej and
ǫ∈{± 1} maps−ei to−ǫej. Hence, a bipolar orbit only consists of pairs, that is, −O =O.
On the other hand, for each unipolar orbit O the set −O ={−ei|ei∈ O} forms another
orbit, and Γ acts equivalently on O and−O.
Proposition 20. For the ﬁxed space of Γ we have
FixΓ (Rn) = lin {β(O)|O orbit of Γ} = lin {β(O)|O unipolar orbit of Γ} .
Proof. The ﬁrst equality is a consequence of Lemma 12. The second equality holds as
β(O) = 0 for any bipolar orbit O. □
Remark 21. The points in S are the vertices of the regular n-dimensional cross polytope.
If O⊂ S is a unipolar Γ-orbit, then β(O) is the barycenter of the non-trivial face of the
cross polytope which is spanned by the vertices in O. In view of cone polarity the action of
Γ on S is dual to the induced action on the vertices of the regular cube [ −1, 1]. That is, the
two corresponding representations of Γ, on Rn and its dual space, form a contra-gradient
pair.
We call the action of Γ on the set of signed standard basis vectors semi-transitive if there
are precisely two opposite orbits of length n. Moreover, we call the action sub-transitive if
there is no proper coordinate subspace which is invariant under Γ. C learly, a semi-transitive
action is necessarily sub-transitive. The converse does not hold, b ut we have the following
characterization.
Proposition 22. Suppose that Γ acts sub-transitively. Then either Γ acts semi-transitively
with orbits O and−O such that the ﬁxed space
FixΓ (Rn) = lin( βO) = lin( β−O)
is one-dimensional, or FixΓ (Rn) = 0 .
Proof. If Γ has a bipolar orbit O, then O equals the entire set S of signed standard basis
vectors because Γ acts sub-transitively. In this case the ﬁxed sp ace reduces to the origin. If,
however, each orbit is unipolar, we have exactly one pair ( O,−O) of opposite orbits, again
due to sub-transitivity. Now the claim follows from Proposition 20. □
Corollary 23. If Γ acts semi-transitively, then Γ is conjugate to a subgroup of Sym(n) in
OnZ.
Proof. Let O and−O be the two orbits of Γ, both of which have length n. Pick a transfor-
mation ǫ∈ OnZ which maps O to the standard basis {e1,e 2,...,e n}. Now for each γ∈ Γ
the conjugate transformation ǫγǫ −1 leaves the sets{e1,e 2,...,e n} and{−e1,−e2,..., −en}
invariant. We conclude that ǫΓǫ−1 is a subgroup of Sym( n). □
SYMMETRIC LINEAR AND INTEGER PROGRAMS 9
We now interprete the results above for integer linear programming . Consider an integer
linear program ILP(A,b,c ) such that the set P (A,b ) of feasible points of the linear relaxation
is full-dimensional. Let Γ ≤ Sym(ILP(A,b,c )) be a group of automorphisms. We have
Γ≤ OnZ. The action of Γ on the set {±e1,±e2,..., ±en} can be decomposed into orbits.
In this way the most relevant case occurs when Γ acts sub-transit ively. From Lemma 7 we
know that c is contained in the ﬁxed space Fix Γ (Rn), and then Proposition 22 says c⁄= 0
enforces the action of Γ to be semi-transitive. Finally, by Corollary 2 3 we can conjugate Γ
into a subgroup of Sym(n) acting on the standard basis {e1,e 2,...,e n}. This is the situation
that we will be dealing with in our algorithms below.
