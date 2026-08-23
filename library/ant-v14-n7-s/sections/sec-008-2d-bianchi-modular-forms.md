---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-008-2d-bianchi-modular-forms
section_title: "2D. Bianchi modular forms"
section_number: null
pages: 10-11
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
details following our exact conventions, see [Williams 2017, §1; Ghate 1999] for a more general treatment.
As above, let F be an imaginary quadratic ﬁeld, and U an open compact subgroup of GL2(A f
F). Then,
for any k> 0, there is a ﬁnite-dimensional C-vector space Sk,k(U) of Bianchi cusp forms of weight(k, k)
and level U, which are functions
9: GL2(F)\GL2(AF)/U→ V(r)
2k+2(C)
transforming appropriately under right-translation by the group C×· SU2(C), and satisfying suitable
harmonicity and growth conditions.
These forms can be described by an appropriate analogue of q-expansions; see [Williams 2017, §1.2].
Let eF: AF/F→ C× denote the unique continuous character whose restriction to F⊗ R∼= C is
x∞↦−→e2πiTrF/Q(x∞),
and let W∞: C×→ V2k+2(C) be the real-analytic function deﬁned in [op. cit., 1.2.1(v)] (involving the
Bessel functions Kn).
Theorem 2.9. Let9 be a Bianchi modular form of weight(k, k) and level U. Then there is a Fourier–
Whittaker expansion
9
((y x
0 1
))
=| y|AF
∑
ζ∈F×
W f(ζ y f,9) W∞(ζ y∞)eF(ζ x),
where W f(−,9) , the “Kirillov function” of 9, is a locally constant function on (A f
F)×, with support
contained in a compact subset of A f
F.
If U= UF,1(n) for some n, then W f(−,9) is supported in D−1ˆOF. For m an ideal of OF, we deﬁne
a coefﬁcient c(m,9) as the value W f( y f,9) for any y f generating the fractional ideal D−1mˆOF; this is
independent of the choice of y f .
Exactly as for elliptic modular forms, the space Sk,k(UF,1(n)) has an action of (commuting) Hecke
operators(Tm)∗ for all ideals m; and if9 is an eigenvector for all these operators, normalised such that
p-adic Asai L-functions of Bianchi modular forms 1677
c(1,9)= 1, then the eigenvalue of the m-th Hecke operator on 9 is c(m,9) . Moreover, the space
Sk,k(UF,1(n)) is a direct sum of “new” and “old” parts, and the Hecke operators(Tm)∗ are simultaneously
diagonalisable on the new part.
