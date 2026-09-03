---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-008-33-the-pivotal-operators
section_title: "The pivotal operators"
section_number: 3.3
pages: 10-14
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Using the pairing convention, we can diagrammatically deﬁne involutions on the
fusion vector spaces.
Deﬁnition 3.7. Let{di} be a root choice on C. The pivotal operators
Ti
jk : Hom(Xi,Xj⊗Xk)→ Hom(Xi,Xj⊗Xk)
10
are deﬁned by
↦→
 . (18)
where the pairing convention has been used.
That is, to evaluate the right hand side of (18), make an arbitrary choice of
right duals ( X∗
i,ηi,ϵi), (X∗
j,ηj,ηj) and ( X∗
k,ηk,ϵk) for Xi, Xj and Xk, and
then choose the left dual structure maps using the pairing convention.
Note that changing the root choice by setting di ↦→ xidi for some signs
xi =±1 with xi = xi∗ will change the sign of the pivotal operators according
to Ti
jk↦→xixjxkTi
jk.
Lemma 3.8. In an arbitrary trivalent basis {eα : Xi→ Xj⊗Xk} with corre-
sponding dual basis{ˆeβ : Xj⊗Xk→Xi} in the sense of (5), the matrix elements
of Ti
jk compute as
⟨ˆeβTi
jk(eα)⟩ = 1
di
.
Proof. We can compute the scalar⟨ˆeβTi
jk(eα)⟩ by closing the loop, as in (16):
ˆeβTi
jkeα = 1
 = 1
di
.
Lemma 3.9. Suppose Xi,Xj are simple objects and f : Xi⊗Xj→ Xi⊗Xj.
Then the following equations hold in the pairing convention:
(a)
=
(b)
=
(c)
=
 .
11
Proof. To prove (a), write
= λ
for some scalar λ, as in equation (15), and extract the value of λ as in equation
(16). Inserting this back into the left hand side of (a) immediately gives the
right hand side. Equation (b) is the interchange law in a monoidal category.
The proof of (c) is similar to the proof of (a), but uses in addition di =di∗.
Theorem 3.10 (cf. [10, Thm 3]) . The operatorTi
jk is an involution — that is,
(Ti
jk)2 = id.
Proof. The operator T 2 sends
↦→
 .
Its matrix elements are thus:
=
12
=
 =
 =
 =diδβ
α
where we have used Lemma 3.9 twice in the third equation. In other words, we
have expanded T 2(eα) in the basis eα using the technique from eq. (17), and
we have shown that T 2(eα) =eα.
Remark 3.11. This calculation is essentially the Dirac belt trick proving that
π1SO(3) = Z/2Z, and provides a link between fusion categories and spin struc-
tures, as mentioned in Remark 2.2. See also [7] and Remark 3.27.
Remark 3.12. If C = RepH for a semisimple Hopf algebraH, then the identity
(Ti
jk)2 = id corresponds to the Larson-Radford formula S2 = id (see [9] and
references therein). The string diagram argument above can be regarded as
giving a graphical proof of Radford’s formula.
Remark 3.13. The proof in [10, Thm 3] proceeds by ﬁrst passing to a strictiﬁed
skeletal category equivalent to C. In our approach, the pairing convention,
together with our conventions on string diagrams from Section 2.1, allows us to
work directly in the category C.
SinceTi
jk is an involution, the vector space Hom(Xi,Xj⊗Xk) has a basis of
eigenvectorseα whose eigenvalues are±1. We call such a basis a pivotal basis
for the fusion category C.
Deﬁnition 3.14. The pivotal symbols ϵi
jk,α =±1 are the eigenvalues of the
pivotal operators, Ti
jkeα =ϵi
jk,peα.
Thus, in a fusion category, the vector spaces Hom(Xi, Xj⊗Xk) decompose
into the positive and negative eigenspaces of Ti
jk,
Hom(Xi, Xj⊗Xk) = Hom(Xi, Xj⊗Xk)+⊕ Hom(Xi, Xj⊗Xk)− (19)
Note that this decomposition is canonical since our convention will be to make
the unique root choice where the di are positive real numbers, as guaranteed by
Theorem 3.19 below.
Lemma 3.15. In a pivotal basis, the pivotal symbols can be computed as follows:
ϵi
jk,α = 1
di
.
Proof. Follows immediately from Lemma 3.8.
13
Lemma 3.16. The pivotal operators T 1
11 and T 1
ii∗ are the identity maps for all
i∈I.
Proof. Follows from an elementary string diagram argument.
