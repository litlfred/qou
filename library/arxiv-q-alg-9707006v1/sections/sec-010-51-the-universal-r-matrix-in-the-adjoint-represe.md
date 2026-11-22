---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-010-51-the-universal-r-matrix-in-the-adjoint-represe
section_title: "The universal R-matrix in the adjoint representation"
section_number: 5.1
pages: 9-9
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
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
