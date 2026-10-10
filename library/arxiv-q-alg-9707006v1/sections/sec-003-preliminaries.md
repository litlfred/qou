---
doc_id: arxiv-q-alg-9707006v1
doc_title: "arXiv:q-alg/9707006v1 4 Jul 1997"
section_id: sec-003-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 5-10
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
---
The method
Consider the matrix representation Cq ≡ρ⊗2
r (∆(Cq)) of the coproduct of the quantum casimir. Its eigenvectors
|i; q⟩, i = 1 . . . 9, form (for each value of q) a basis in the nine dimensional space on which the above matrix acts
(i can be thought of as a composite label, i = {αq, hq}, where αq is an eigenvalue of the casimir in ρ⊗2
r
and hq
diﬀerentiates between eigenvectors belonging to the same casimir eigenvalue - we will use the eigenvalues of H for
that purpose). Taking representations in both spaces of (13) (with C replacing x) one ﬁnds
Cq = Fqρ⊗2
r (∆c(Cq))F −1
q
(16)
where Fq ≡ρ⊗2
r (F). It follows that
|i; q⟩= Fq|i; 1⟩,
i = 1 . . . 9 .
(17)
Putting Mij ≡⟨j; 1|i; 1⟩we ﬁnd for Fq
Fq = M −1
ij |j; q⟩⟨i; 1| .
(18)
Notice that we have allowed for the possibility of the eigenvectors being nonorthogonal. Trying to produce an
orthonormal set by taking suitable linear combinations might (and will, typically) involve mixing eigenvectors of
diﬀerent (casimir) eigenvalues. Nevertheless, in the particular representation chosen (ρ⊗2
r ), the casimir will turn
out to be given by a symmetric matrix and, consequently, the matrix M above will be diagonal, resulting in
signiﬁcant simpliﬁcation of the computations.
Orthogonality
One of the advantages in switching from ρf to ρr is the fact that, as mentioned earlier, in this latter representation,
the transpose of X+ is equal to X−(this requirement dictated the rescaling of x−). A glance at the form of the
coproduct of Cq (equation (19) below) reveals that the above property (along with H being diagonal) results in
Cq being a symmetric matrix. Its eigenvectors therefore can be taken to form, for each value of q, an orthonormal
basis. Equation (17) then shows that Fq is an orthogonal matrix which rotates this basis from its classical (at
q = 1) to its quantum position (at general q).
Invariant subspaces
The coproduct of H being undeformed, Fq commutes with its representation and is therefore of a block-diagonal
form, with each block acting in a subspace of ﬁxed H-eigenvalue. We expect therefore two 1-dimensional blocks
(corresponding to the directions (++) and (−−) with H-eigenvalues 4 and -4 respectively), two 2-dimensional
blocks (corresponding to the planes (+0, 0+) and (0−, −0) with H-eigenvalues 2 and -2 respectively) and one
3-dimensional block (acting in the subspace (+−, 00, −+) of H-eigenvalue 0). Similar remarks hold for Cq. The
1-dimensional blocks of Fq are equal to 1 due to orthogonality while those of Cq are obviously equal to each other
(being the values of the casimir in the same multiplet). A glance at eqn. (19) below shows that the 2-dimensional
blocks of Cq are also equal to each other (since H has opposite eigenvalues in the corresponding planes). It
then follows, from (18), that the above property holds for Fq as well. We will present any matrix W, with the
structure described above, in the form {µW , DW , TW } where µW , DW , TW are 1, 2 and 3-dimensional matrices
respectively.
4.2
Explicit computation of Fq
We start by computing Cq. We ﬁrst ﬁnd
∆(Cq)
=
X−X+ ⊗qH + X−q−H/2 ⊗qH/2X+
+q−H/2X+ ⊗X−qH/2 + q−H ⊗X−X+
+λ−2(q · qH ⊗qH + q−1q−H ⊗q−H −2 · 1 ⊗1)
(19)
and substituting from (11) we obtain
Cq = {[5/2]2,
 
[1/2]2 + q−1[2]2
[2]
[2]
[1/2]2 + q[2]2
!
,



[1/2]2 + q−2[2]
−q−1[2]
0
−q−1[2]
[1/2]2 + 2[2]
−q[2]
0
−q[2]
[1/2]2 + q2[2]


} . (20)
The corresponding 2 and 3-dimensional eigenvectors are
(1, −q−2)
[3/2]2
(1, q2)
[5/2]2
(q2, q, 1)
[1/2]2
(1, −λ, −1)
[3/2]2
(1, −q −q3, q4)
[5/2]2 ,
(21)
where, in the second column, we give the corresponding eigenvalue (Cq has eigenvalues of the form [j + 1/2]2, j =
0, 1, 2, . . .). It is now easy to construct Fq using (18). We ﬁnd
µFq = 1,
DFq =
1
√
2a
 
q2 + 1
−(q2 −1)
q2 −1
q2 + 1
!
(22)
as well as
TFq =
1
√
6ab



√
2q2a +
√
3qb + 1
√
2q2a −2
√
2q2a −
√
3qb + 1
√
2qa −
√
3(q2 −1)b −q(1 + q2)
√
2qa + 2q(1 + q2)
√
2qa +
√
3(q2 −1)b −q(1 + q2)
√
2a −
√
3qb + q4
√
2a −2q4
√
2a +
√
3qb + q4


,
(23)
where a ≡
p
1 + q4, b ≡
p
1 + q2 + q4. Recalling the discussion in section 2.2, regarding the properties of ρr
under the substitution q 7→q−1, we see that, with ∆(Cq) as in (19), Cq satisﬁes (Cq−1)12 = (Cq)21. It follows then
from (18) that the same relation holds for Fq.
The 2-dimensional subspace
DFq is an SO(2) matrix, even in q, corresponding to an angle of rotation θ(2)
q
given by
tan(θ(2)
q ) = q2 −1
q2 + 1 ,
(24)
counterclockwise in the (+0, 0+) or (0−, −0) plane. As q ranges in the interval (0, ∞), θ(2)
q
goes from −π
4 to
π
4 . Notice that although at the endpoints of the above interval in q, neither the quantum su(2) algebra nor the
adjoint representation (11) make sense, DFq retains nevertheless a well deﬁned value. Under q 7→q−1, the two
axes get interchanged and the angle of rotation changes sign.
As pointed out in [6], a more natural reference point in describing the rotation eﬀected by Fq, and one which
simpliﬁes the results, is the crystal limit q →0 (notice that the eigenvectors of Cq in (21), when normalized, tend
to the basis vectors in this limit). The matrix that connects the general value of q to this limit is Fq0 ≡FqF −1
0
.
We ﬁnd
DFq0 = 1
a
 
1
−q2
q2
1
!
,
(25)
with corresponding angle of rotation θ(2)
q0 given by tan(θ(2)
q0 ) = q2.
0
20
40
60
80
100
120
-8
-6
-4
-2
00
20
40
60
80
100
120
Figure 1: The curve TFq in the SO(3) manifold (−1 ≤q ≤1)
The 3-dimensional subspace
TFq is an SO(3) matrix - we denote by ˆnq the unit vector along the axis of the rotation represented by TFq and
by θ(3)
q
the angle of rotation (clockwise) around ˆnq (θ(3)
q
ranges in the interval [0, π)). Working in a basis where
one of the basis vectors is along ˆnq, and using the invariance of the trace of TFq under rotations, we ﬁnd
1 + 2 cos(θ(3)
q ) = Tr(TFq) ,
(26)
where, using (23),
Tr(TFq) =
1
√
6ab(
√
2(q2 + q + 1)a + 2
√
3qb + q4 + 2q3 + 2q + 1) .
(27)
Let αi, i = 1, 2, 3 denote the angles that ˆnq makes with the axes - a little geometry shows that
cos2(αi) = TFq ii −cos(θ(3)
q )
1 −cos(θ(3)
q )
.
(28)
Notice that TFq ii (no summation over i) is the angle that the i-th basis vector makes with its image under the
rotation. The correct signs for cos(αi) are obtained by examining the derivatives dFq/dq|q=0 and d2Fq/dq2|q=0.
Under q 7→q−1, the axes (+−) and (−+) get interchanged. As q ranges over the reals, TFq traces out a curve
in the SO(3) manifold (a ball of radius π with antipodal points on the surface identiﬁed). We have plotted this
curve (for the range −1 ≤q ≤1) in ﬁgure 1. The left - right axis is in the (+−)-direction while the vertical is
along (−+) (the axes are marked in degrees). The points of the curve are projected down to the (+−, 00)-plane
and back to the (+−, −+)-plane (at equal intervals in q) for clarity of presentation. To ﬁnd the value qs at which
the curve meets the surface of the ball, we substitute (27) in (26), set θ(3)
q
equal to π and solve for qs - the result is
qs = −1. The corresponding rotation matrix has (1, −1, 1) along the second diagonal as its only nonzero entries.
The curve starts (for q = −1) at the right part of the ﬁgure (upper edge of the ribbon), touching at that point the
(+−, −+)-plane on the diagonal (notice the anisotropic scaling of the axes) as well as the surface of the SO(3)
ball. At q = 1, TFq is the unit matrix, which corresponds to the origin of the ball. Notice that the tangent to
the curve at the origin is along the diagonal in the (+−, −+)-plane (the same holds at q = −1). The property
(Fq−1)12 = (Fq)21 reﬂects itself in the following symmetry of the curve: the points corresponding to q and q−1
are mapped into each other by central reﬂection and subsequent interchange of the (+−), (−+) axes (this allows
one to picture the missing segments −∞< q < −1 and 1 < q < ∞, which are omitted from ﬁgure 1 for clarity).
-100
-50
0
50
100
-8
-6
-4
-2
0
2
4
6
8
-100
-50
0
50
100
Figure 2: The curve TFq0 in the SO(3) manifold (−3 ≤q ≤3)
Notice that the above two missing segments “touch” as q →±∞since, in this limit, TFq tends to the common
value
TF±∞=
1
√
6



√
2
√
2
√
2
−
√
3
0
√
3
1
−2
1


.
(29)
As in the 2-dimensional case, the results are simpliﬁed when the crystal limit is used as reference point. We
ﬁnd
TFq0 = 1
ab



1
qb
q2a
−q(1 + q2)
(1 −q2)b
qa
q4
−qb
a


.
(30)
The corresponding SO(3) curve (for q in the interval [−3, 3]) is plotted in ﬁgure 2. In this case, the lower left -
upper right axis is along the (+−) direction while the vertical is again along (−+). The origin corresponds to
q = 0 while the point of the curve on the surface of the ball (not shown) to q →±∞.
A remark on the omission of c from ρr is in order at this point. It is sometimes desirable to know Fq in the
entire 16-dimensional space spanned by the bilinears in c, x+, x0, x−. This, for example, could originate in the
fact that although the quantum adjoint action closes linearly in the set x+, x0, x−, the algebra of these three
generators involves c. Such cases are easily handled noting that Fq is simply a unit matrix in the 7-dimensional
space we have omitted in the above computation.
4.3
The representation of the coproduct of F
The method for computing Fq used above is easily adapted to the computation of Fq123 ≡ρ⊗3
r ((∆⊗id)F). The
matrix C123 = ρ⊗3
r (∆(2)C), where ∆(2)(C) ≡(∆⊗id) ◦∆(C), is again symmetric and its eigenvectors are rotated
by the orthogonal Fq123 from their classical to their deformed position. This allows the computation of Fq123
from a formula analogous to (18). Both C123 and Fq123 are of block-diagonal form, with each block acting in
a subspace of ﬁxed H-eigenvalue. Based on this observation, one easily sees that both matrices have 1, 3 and
6-dimensional blocks (two of each) and one 7-dimensional one. Blocks of equal dimension are equal to each other,
up to (easily identiﬁed) permutations of rows and columns. We have carried out, with the help of MAPLE,
the explicit computation of these matrices, with respect to the crystal limit (i.e. we have computed the matrix
Fq0123 ≡Fq123F0
−1
123). We present the (rather cumbersome) results in the appendix.
5
Applications
5.1
The universal R-matrix in the adjoint representation
The block diagonal form of the matrices involved simpliﬁes signiﬁcantly the computation of R ≡ρ⊗2
r (R). Applying
ρ⊗2
r
in (15) gives
R = F ′
q ρ⊗2
r (qt) F −1
q
.
(31)
For the representation of the classical R-matrix we compute
ρ⊗2
r (t) = {2,
 
0
2
2
0
!
,



−2
−2
0
−2
0
−2
0
−2
−2


}
(32)
which gives, upon exponentiation
µRc = q2,
DRc =
1
2q2
 
q4 + 1
q4 −1
q4 −1
q4 + 1
!
(33)
as well as
TRc =
1
6q4



q6 + 3q2 + 2
−2(q6 −1)
q6 −3q2 + 2
−2(q6 −1)
2(2q6 + 1)
−2(q6 −1)
q6 −3q2 + 2
−2(q6 −1)
q6 + 3q2 + 2


,
(34)
where Rc ≡ρ⊗2
r (Rc). We may now use (31) to ﬁnd
µR = q2,
DR =
 
1
q2 −q−2
0
1
!
,
TR =



q−2
−q + q−3
(q2 −q−2)(1 −q−2)2
0
1
−q + q−3
0
0
q−2


.
(35)
R is seen to be upper triangular while ˆR ≡PR is symmetric (P stands here for the permutation matrix,
Pij,kl = δilδkj - ˆR is obtained from R by interchange of the rows of DR and interchange of the ﬁrst and third row
of TR). One could also compute R starting from the known expression for R, apply ρ⊗2
f
to it and then conjugate
with the tensor square of A - the two results agree.
The characteristic equation for ˆR is easily computed now. Indeed, one ﬁnds that
(D ˆR −q2I)(D ˆR + q−2I) = 0,
(T ˆR −q2I)(T ˆR + q−2I)(T ˆR −q−4I) = 0 .
(36)
Notice that µ ˆR and D ˆR both satisfy the characteristic equation for T ˆR - this implies that ˆR does too, i.e. ˆR’s
minimal polynomial is cubic. The characteristic polynomial for ˆR is obtained from its minimal one by raising its
factors, in the order they appear above, to the powers 5, 3 and 1. Had we included c in ρr, obtaining in this way
a 16-dimensional matrix for ˆR, the minimal polynomial would turn out to be quintic, the extra two factors being
( ˆR −I)( ˆR + I), coming from the c-sector in which ˆR is a permutation matrix. The above two factors would be
raised to the power 3 and 4 respectively in the characteristic polynomial of ˆR.
5.2
Quantum symmetrization
We consider here the problem of quantum symmetrization of identical particle states. We supply, for reasons
of self-containment, a brief exposition of the relevant theory, along the lines of [7], which contains a thorough
discussion.
As a ﬁrst step towards the implementation of quantum group symmetries in quantum mechanics and quantum
ﬁeld theory, the question of the compatibility of Bose/Fermi statistics with quantum group actions ought to be
addressed. Consider, for concreteness, a two (identical) particle system in quantum mechanics. The Hilbert space
of the system is split into symmetric and antisymmetric subspaces, a division which is respected by the action
of classical Lie algebra generators. This latter fact is traced to the symmetry of the classical coproduct under
exchange of the two spaces, so that the classical permutation matrix P commutes with the representation of the
coproduct of the generators
[P, ρ⊗2(∆c(x))] = 0,
x ∈U(g),
(37)
where g is the Lie algebra under consideration and ρ the representation through which it acts on the one-particle
states. In the quantum case, the lack of cocommutativity implies that the quantum group action mixes the two
eigenspaces of P. The problem is rectiﬁed with the introduction of a quantum permutation operator P F , given
by conjugation by F of the classical one, i.e. P F = FPF −1. One easily shows that
[P F , ρ⊗2(∆(x))] = 0
x ∈Uq(g) ,
(38)
which guarrantees that quantum symmetric and antisymmetric states (deﬁned as eigenstates of P F ) remain such
after being acted upon by elements of Uq(g) (in the above equation, F is computed in ρ).
Specifying g, in the discussion above, to be su(2) and working in the representation ρr, we ﬁnd
SF = {1,
1
1 + q4
 
1
q2
q2
q4
!
,
1
1 + q4



q4 −q2 + 1
q3 −q
q2
q3 −q
q2
−q3 + q
q2
−q3 + q
q4 −q2 + 1


}
(39)
while
AF = {0,
1
1 + q4
 
q4
−q2
−q2
1
!
,
1
1 + q4



q2
−q3 + q
−q2
−q3 + q
(q2 −1)2
q3 −q
−q2
q3 −q
q2


}
(40)
where SF ≡F 1
2(1 + P)F −1 and AF ≡F 1
2(1 −P)F −1 are the quantum symmetrizer and antisymmetrizer
respectively. In the c-sector, SF and AF are equal to their classical counterparts. Clearly, SF 2 = SF (similarly
for AF ) and SF AF = 0.
For systems with more than two identical particles one proceeds along similar lines. The quantum permutation
matrix for adjacent spaces i, i + 1 is given by P F
i,i+1 = Fq12...nPi,i+1Fq
−1
12...n, where Pi,i+1 is the corresponding
classical permutation matrix and Fq12...n is the representation of (∆(n−1) ⊗id)F (diﬀerent choices for Fq12...n
are possible).
For example, for n = 3, Fq123 can be obtained from the crystal limit result of section 4 as
Fq123 = Fq0123F10
−1
123.
