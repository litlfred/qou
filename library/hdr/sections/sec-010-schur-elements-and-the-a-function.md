---
doc_id: hdr
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-010-schur-elements-and-the-a-function
section_title: "Schur elements and the a-function"
section_number: null
pages: 28-29
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "HAL Id: tel-01411063 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: Algebras of"
---
The canonical symmetrising form τ onH(W ) (see Assumptions 3.4) can be extended to K(v)H(W ) by
extension of scalars, and can be used to deﬁne Schur elements ( sE)E∈Irr(W) forH(W ), as in the real
case. The Schur elements of H(W ) have been explicitly calculated for all complex reﬂection groups:
• for ﬁnite Coxeter groups see §2.2;
• for complex reﬂection groups of type G(l, 1,n ) by Geck–Iancu–Malle [GIM] and Mathas [Mat];
• for complex reﬂection groups of type G(l, 2, 2) by Malle [Mal2];
• for the non-Coxeter exceptional complex reﬂection groups by Malle [Mal2, Mal4].
With the use of Cliﬀord theory, we obtain the Schur elements for type G(l,p,n ) from those of type
G(l, 1,n ) when n> 2 or n = 2 and p is odd. The Schur elements for type G(l,p, 2) when p is even derive
from those of type G(l, 2, 2) (see [Mal1], [Ch4, A.7]).
Using a case-by-case analysis, we have been able to determine that the Schur elements ofH(W ) have
the following form [Ch4, Theorem 4.2.5].
Theorem 3.7 LetE∈ Irr(W ). The Schur element sE is an element of ZK[v, v−1] of the form
sE =ξENE
∏
i∈IE
ΨE,i(ME,i) (3.3)
where
(a) ξE is an element of ZK,
(b) NE =∏
C,jvbC,j
C,j is a monomial in ZK[v, v−1] with∑eC−1
j=0 bC,j = 0 for all C∈A /W ,
(c) IE is an index set,
(d) (ΨE,i)i∈IE is a family of K-cyclotomic polynomials in one variable,
(e) (ME,i)i∈IE is a family of monomials in ZK[v, v−1] such that if ME,i =∏
C,jvaC,j
C,j , then gcd(aC,j) = 1
and∑eC−1
j=0 aC,j = 0 for all C∈A /W .
Equation (3.3) gives the factorisation of sE into irreducible factors. The monomials ( ME,i)i∈IE are
unique up to inversion, and we will call them potentially essential for W .
Remark 3.8 Theorem 3.7 was independently obtained by Rouquier [Ro2, Theorem 3.5] using a general
argument on rational Cherednik algebras.
Example 3.9 Let us consider the example of S3, which is isomorphic to G(1, 1, 3). We have
sE(3) = Φ2(vt,0v−1
t,1)Φ3(vt,0v−1
t,1), sE(2,1) =v−1
t,0vt,1Φ3(vt,0v−1
t,1), sE(1,1,1) =v−3
t,0v3
t,1Φ2(vt,0v−1
t,1)Φ3(vt,0v−1
t,1),
where Φn denotes the n-th Q-cyclotomic polynomial.
Let ϕm : vC,j↦→ qmC,j be a cyclotomic specialisation. The canonical symmetrising form on H(W )
specialises via ϕm to become a canonical symmetrising form τϕm onHϕm(W ). The Schur elements of
Hϕm(W ) with respect to τϕm are (ϕm(sE))E∈Irr(W), hence they can be written in the form (2.2). We
can again deﬁne the a-function am : Irr(W )→ Z and the A-function Am : Irr(W )→ Z by setting
am
E :=−valq(ϕm(sE)) and Am
E :=−degq(ϕm(sE)).
25
