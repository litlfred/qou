---
doc_id: 18
doc_title: "Combinatorial scalar curvature and rigidity of ball packings"
section_id: sec-001-1-conformal-simplices
section_title: "Conformal simplices"
section_number: 1
pages: 1-4
source_pdf: 18.pdf
source_sha256: 0b7bf055085cb04b
toc_source: inferred
doc_brief: "Combinatorial scalar curvature and rigidity of ball packings — 11 sections: Front matter; Introduction; Conformal simplices"
---
results. In section 3 we extend these techniques to conformal simplices in
H3. In section 4 we study the deformation space of conformal simplices. In
section 5 we prove the results on scalar curvature alluded to above, and in
section 6 we discuss the ball-packing results.
1. Conformal simplices
Let T be a simplex in E3. Denote the vertices of T by v1, . . . , v4, and
denote the edge joining vi and vj by eij. The length of eij shall be denoted
by lij, while the dihedral angle of eij shall be denoted by αij. The solid
angle at the vertex vi of T shall be denoted by Si. From the Gauss-Bonnet
formula we know that Si = 
j̸=i αij −π.
We say that T is conformal if there are r1, . . . , r4 > 0 such that l(eij) =
ri+rj. Denote the space of all conformal simplices by CT – this is a topolog-
ical space, if we require that the map of C to R4, where we map a conformal
sequence to the radii r1, . . . , r4 deﬁning it, be a homeomorphism. The col-
lection of vectors (r1, . . . , r4) ∈R4 which correspond to geometric simplices
Received October 26, 1995.
51
52
DARYL COOPER AND IGOR RIVIN
is an open set. Denote this set by Cr
T . Since the set of all three-dimensional
Euclidean simplices is an open set in R6 (as parametrized by edge-lengths,
for example), it is clear that the property of conformality is rather special.
In the sequel the simplex T and all of its geometric parameters will be
viewed as functions of r = (r1, r2, r3, r4) ∈Cr
T . Let
S(r) =
4

i=1
Siri.
The next two results form the foundation of what follows.
Lemma 1.1.
dS =
4

i=1
Sidri.
Proof. Let us rewrite the formula for S using the relations lij = ri +rj and
Si = 
j̸=i αij −π. A short computation shows that
S =

i̸=j
lijαij −π
4

i=1
ri,
and thus
dS =

i̸=j
αijdlij +

i̸=j
lijdαij −π
4

i=1
dri.
However, by the Euclidean case of the Schl¨aﬂi diﬀerential formula, the
second sum above vanishes, and since lij = ri + rj, the claim of the lemma
follows.
□
Note. The Schl¨aﬂi diﬀerential formula (for a good exposition and proof,
see [1][Chapter 7, section 2.2.2]) states that as a simplex T (and thus any
polyhedron) varies smoothly in one of the spaces of constant curvature Hn,
Sn or En, its volume also varies smoothly, and furthermore
(1.1)
Kd volT =
1
n −1

dim F =n−2
volF dαF ,
where K is the curvature of the space, and αF is the dihedral angle at the
(n−2)-dimensional face F. Note that when K = 0, the formula simply says
that the right-hand side vanishes.
COMBINATORIAL SCALAR CURVATURE
53
Lemma 1.2. The Hessian H of S is negative semi-deﬁnite – its null-space
is spanned by the vector r.
Proof. It is clear that r is in the null-space of the Hessian, since it corre-
sponds to a rescaling of the simplex. To show that all other eigenvalues
of H are negative it is enough to show that the diagonal entries of H
are negative, while the oﬀ-diagonal elements are positive. To see this, let
(v1, . . . , v4) be an eigenvector of H corresponding to a non-negative eigen-
value λ, and let wi = vi/ri. We want to show that wi = wj, for all i, j.
If not, assume without loss of generality that 0 < w1 = max{wi}. Then,
(λ −H11)v1 = 
i>1 H1ivi, so
λr1w1 −H11r1w1 =

i>1
H1iriwi ≤

i>1
H1iriw1,
and so λ ≤0, with equality if and only if all of the wi are equal.
Note now that Hij = ∂Si/∂rj. If r1, r2, r3 are kept ﬁxed and r4 is in-
creased, v4 is moving along a trajectory h such that the angles between the
tangent vector to h and the edges e4i are equal (an easy consequence of the
law of cosines). Thus, the simplex T(r1, r2, r3, r4 +ϵ) (where ϵ > 0) strictly
contains T(r1, r2, r3, r4), while sharing its base. The desired inequalities
are then clear.
□
As a preview of the argument to come in the next section, we prove the
following results.
Theorem 1.3. Fix the scale of the simplices under consideration, by set-
ting
(1.2)
r1 + r2 + r3 + r4 = 1.
Then the regular simplex, for which ri = 1/4, is a critical point of the
function S, and furthermore, the regular simplex cannot be conformally
deformed while keeping the solid angles ﬁxed.
Proof. By Lemma 1.2, the function S is strictly concave on the slice of Cr
T
determined by the equation 1.2. By the principle of Lagrange multipliers
and Lemma 1.1, S has a critical point subject to equation 1.2, precisely
when all of the solid angles are equal. By concavity, such a critical point
is isolated, proving the rigidity statement.
□
A similar argument shows the following:
54
DARYL COOPER AND IGOR RIVIN
Theorem 1.4. A conformal simplex cannot be deformed while keeping the
solid angles ﬁxed; that is, the set CS1,S2,S3,S4 ⊂C1 is discrete.
Proof. We have seen above that this is true for the regular simplex. To
show the theorem, we modify the function S as follows: Let Sa1,a2,a3,a4 =
S + airi. Now Sa1,a2,a3,a4 is still strictly concave subject to the condition
1.2, but its gradient is (S1 + a1, . . . , S4 + a4). Hence the critical points of
Sa1,...,a4 occurs when Si + ai = Sj + aj, for all i, j ≤4. This shows the
assertion of the theorem.
□
