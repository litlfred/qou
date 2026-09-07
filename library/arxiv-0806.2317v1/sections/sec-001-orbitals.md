---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-001-orbitals
section_title: "Orbitals"
section_number: null
pages: 3-5
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
In this section we describe the orbits of pairs of elements of Gm,n under the
action of U (n).
First, we claim that Gm,n can be identiﬁed with a factor group of the unitary
group, U (n)/ (U (m) × U (n − m)). For, consider the ﬁrst m columns of a matrix
of U (n) as the basis for a subspace a of dimension m in Cn, letting the last
n − m columns be a basis for a⊥. Then a is invariant under the action of U (m)
on the ﬁrst m columns, while a⊥ is invariant under U (n − m).
As a result of this factor group, U (n) acts on Gm,n as follows: if U is in
U (n) and Pa is the projection matrix for a ∈ G m,n , then
U : Pa ↦→U PaU ∗.
3
This action is an isometry, in that it preserves the trace inn er product on Gm,n .
Unlike the complex unit sphere, however, U (n) is not 2 -homogeneous on Gm,n :
U (n) does not act transitively on pairs of subspaces with the sam e distance. In
other words, the fact that tr( PaPb) = tr( PcPd) does not imply that there is a
unitary matrix mapping a to c and b to d. In order to use zonal polynomials,
we need to understand the orbits of pairs in Gm,n under this isometry group,
which requires principal angles.
Given a and b in Gm,n , the principal angles θ1, . . . , θ m between a and b are
deﬁned as follows: ﬁrstly, θ1 is the largest angle that occurs between any two
unit vectors a1 ∈ a and b1 ∈ b:
θ1 := mina1∈a
b1∈b
arccos |a∗
1b1| .
Secondly, θ2 is the largest angle that occurs between any two unit vectors
a2 ∈ a ∩ a⊥
1 and b2 ∈ b ∩ b⊥
1 . Similarly deﬁne θ3, . . . , θ m. These principle angles
are closely related to the eigenvalues of PaPb: the ﬁrst m eigenvalues of PaPb are
{cos2 θ1, . . . , cos2 θm}. Because of this correspondence, for the remainder of this
paper we simply refer to the eigenvalues yi := cos 2 θi (rather than the values
θi) as the principal angles between a and b. Note that n − m of the eigenvalues
of PaPb are zero, so we need only consider the ﬁrst m eigenvalues. Conway,
Hardin, and Sloane [8] accredit the following lemma to Wong [ 24, Theorem 2].
Lemma 2.1. The principal angles characterize the orbits of pairs of sub spaces
under U (n).
Proof. Suppose U ∈ U (n) maps projection matrices Pa and Pb to Pc and Pd
respectively. Then by similarity, the eigenvalues of
PcPd = (U PaU ∗)(U PbU ∗) = U PaPbU ∗
are the same as the eigenvalues of PaPb.
Conversely, we show that if PaPb and PcPd have the same eigenvalues, then
some unitary matrix U maps a to c and b to d. We do this by unitarily mapping
a and b into a canonical form that depends only on the eigenvalues of PaPb.
Let Ma be an n × m matrix whose columns [ a1, . . . , a m] are an orthonor-
mal basis for a, so that MaM ∗
a = Pa and M ∗
a Ma = I. Similarly deﬁne
Mb = [ b1, . . . , b m] for b. Suppose M ∗
a Mb has singular value decomposition
U DV ∗, where U and V are m × m unitary and D is m × m diagonal. Then
(MaU )∗(MbV ) = D. Since the columns of MaU are another orthonormal basis
for a, without loss of generality we replace Ma by MaU and likewise replace
4
Mb with MbV . In other words, we may assume without loss of generality tha t
M ∗
a Mb = D, where D is a diagonal matrix of singular values.
Next, deﬁne the columns of Na = [ am+1, . . . , a n] to be any orthonormal
basis for a⊥, so that NaN ∗
a = I − Pa and N ∗
a Na = I. Further assume that
N ∗
a Mb = QR, where Q is ( n − m) × (n − m) unitary and R is ( n − m) × m
upper triangular (the QR-decomposition of N ∗
a Mb). Then Q∗N ∗
a Mb = R, and
the columns of NaQ form another orthonormal basis for a⊥. Replacing Na by
NaQ, we may assume without loss of generality that N ∗
a Mb is upper triangular.
Finally, let Ua :=
(
M ∗
a
N ∗
a
)
; this is an n × n unitary matrix. Then
UaMa =
(Im
0
)
; UaMb =
(D
R
)
.
If PaPb has eigenvalues cos 2 θi, then M ∗
a Mb = D has singular values cos θi.
Moreover, since UaMb has orthonormal columns, it follows that R also has
orthogonal columns. We may therefore assume that R is not just the upper
triangular but diagonal, with diagonal entries sin θi. Thus Ua is a unitary
matrix which maps Ma and Mb into the form
Ma ↦→
(Im
0
)
, M b ↦→


cos θ1
. . .
cos θm
sin θ1
. . .
sin θm
0


.
Since any pair ( Ma, M b) with principal angles cos 2 θi can be mapped to this
canonical form, it follows that the eigenvalues of PaPb characterize the orbits
of pairs ( a, b ) under the unitary group.
