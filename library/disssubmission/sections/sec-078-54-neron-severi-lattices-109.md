---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-078-54-neron-severi-lattices-109
section_title: "N´eron-Severi lattices 109"
section_number: 5.4
pages: 117-119
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
and the top quotient deﬁnes a surjection
H2(Y+,Z) = E2
∞↠ E02
∞ = E02
2 = H2(Y,Z)+.
By construction of the spectral sequence this surjection coincides with the
mapq∗ induced by the quotient morphismq : Y−→Y+.
The spectral sequence also shows that the kernelK of this surjection is
an extension of(Z/2Z)8 by Z/2Z. In factK = (Z/2Z)9 becauseK must be
a 2-torsion group: If we denote by
q! : H2(Y,Z)−→H2(Y+,Z)
the Gysin map (i.e. the Poincar´e dual to the pushforward on homology),
then q!q∗ is multiplication by the degree deg(q) = 2, hence for anyα∈ K
it follows that 2α = q!q∗(α) =q!(0) =0 as claimed.
To conclude the proof, note thatF = H2(Y+,Z)/K is a subgroup of
the free abelian groupH2(Y,Z). As such the group F is torsion-free and
therefore equal to the free part ofH2(Y+,Z), whose rank ish2(Y+) = 34
by the computation of Hodge numbers in lemma 5.8. □
5.4. N´eron-Severi lattices
Recall that in the setting of the previous section we have embeddings of
free abelian groups
H2(X,Z)⊂ H2(Y,Z)+⊂ H2(Y,Z).
In what follows we equip these groups with the integral bilinear form that
is given by the intersection form onY. The goal of the present section is to
determine the structure of the obtained integral lattices with respect to this
bilinear form, for which we ﬁrst brieﬂy recall from [22] some basic notions
from lattice theory that will be used throughout.
By a lattice we mean a pair consisting of a ﬁnitely generated free abelian
group L and a non-degenerate symmetric bilinear formb : L×L−→Z,
though we will usually suppress the bilinear form in the notation. Such a
lattice is called even ifb(λ,λ)∈ 2Z for all λ∈ L. For integersn⁄= 0 we
denote byL(n) the lattice with the same underlying free abelian group asL
but with the bilinear formn·b in place ofb. As usual, by an embedding of
lattices we mean an embedding of free abelian groups which respects the
bilinear forms, and similarly for isomorphisms of lattices. For example, the
diagonal embedding
diag: L(2) ↪→ L2 = L⊕L
is given byλ↦→ (λ,λ). We also remark that any lattice can be deﬁned with
respect to a chosen basise1, . . . ,en of the underlying free abelian group by
the corresponding Gram matrix — the non-degenerate integral symmetric
110 Chapter 5 – A family of surfaces
matrix(b(ei,ek))i,k=1,...,n of sizen×n whose entries are the scalar products
between the basis vectors. The discriminant of a lattice is deﬁned as the
determinant of its Gram matrix with respect to any chosen basis, and the
lattice is called unimodular if its discriminant is±1. In what follows we
consider the lattice
Λ = Z4 with Gram matrix
(0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
)
and the standard hyperbolic latticeU = Z2 with Gram matrix(0 1
1 0
). Note
that bothΛ andU are even lattices and thatU is unimodular whereas a direct
calculation shows thatΛ has discriminant−3. This being said, consider the
even lattices
K = U12⊕Λ and L = U13⊕E8(−1).
In terms of these two lattices, the main result of the present section can be
formulated as follows.
PROPOSITION 5.12. There exists an isomorphism H2(Y,Z)∼= L2⊕U9
of lattices which gives a commutative diagram
H2(X,Z)   //
∼=

H2(Y,Z)+   //
∼=

H2(Y,Z)
∼=

K(2)   i(2) // L(2)   (diag,0) // L2⊕U9
for some lattice embedding i: K ↪→L with orthocomplement K⊥∼=E6(−1).
To complete the picture, we remark that with the above identiﬁcations
it follows that on the latticeL2⊕U9 the involutionσ : Y−→Y acts by the
formula
σ(λ1,λ2,u) = ( λ2,λ1,−u) for u∈U9 and λ1,λ2∈ L.
Indeed, looking at the eigenspace decomposition over the rational numbers
one sees that the involutionσ must act by−1 on the orthocomplement of
the σ-invariant partH2(Y,Z)+ insideH2(Y,Z).
The proof of proposition 5.12 will occupy the rest of this section and
will also involve a study of the intersection form onH2(Y+,Z). Note that
since this latter cohomology group contains torsion, it is not a lattice in the
above sense. So let us introduce the following notations. For any smooth
complex projective surfaceS let
LS = H2(S,Z)/Torsion
