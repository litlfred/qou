---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-006-41-preliminaries
section_title: "Preliminaries"
section_number: 4.1
pages: 5-6
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
Preliminaries
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
