---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-012-16-chapter-1-vanishing-theorems-on-abelian-varie
section_title: "Chapter 1 – Vanishing theorems on abelian varieties"
section_number: 16
pages: 24-25
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
Proof.Via the Riemann-Hilbert correspondence [57] we can considerP
as a D-module. For Z⊆ X closed and irreducible, letΛZ⊆ T∗X be the
closure inT∗X of the conormal bundle inX to the smooth locus ofZ. As in
loc. cit. we write the characteristic cycle ofP as a ﬁnite formal sum
CC(P) = ∑
Z⊆X
nZ· ΛZ with nZ∈ N0,
whereZ runs through all closed irreducible subsets ofX. From CC(P) the
support ofP can be recovered via SuppP =⋃
nZ⁄=0Z. Furthermore, by the
microlocal index formula [44, th. 9.1] we have
χ(P) = ∑
Z⊆X
nZ·dZ with dZ = [ΛX]· [ΛZ]∈ Z.
The intersection numbersdZ are well-deﬁned even thoughΛZ is not proper
forZ⁄=X, see loc. cit. for details. Now ifX is a simple abelian variety, then
lemma 1.8 below implies(a), and if we additionally assume dim(X) > 1,
also (b) follows in view of lemma 1.9 below. The non-simple case can be
reduced to the simple case, see [107]. □
The reduction to the case of simple abelian varieties in loc. cit. works for
ground ﬁeldsk of characteristicp > 0 as well, but we do not know how to
deal with simple abelian varieties in that case. Fork = C, Christian Schnell
has given in [94, cor. 3.11] a different proof of proposition 1.6(a) via the
Fourier-Mukai transform forD-modules.
COROLLARY 1.7. A simple perverse sheaf P∈ Perv(X,C) has Euler
characteristic zero iff H•(X,Pχ) =0 for most charactersχ.
Proof.“⇐” holds by corollary 2.2. For “⇒” take a positive-dimensional
abelian subvarietyA ↪→X with quotientq : X↠B =X/A and a characterϕ
such that P∼= Lϕ⊗q∗(Q)[dim(A)] for some perverse sheafQ on B as in
proposition 1.6(a). We can assume that the Euler characteristic ofQ is not
zero. Then we claim that
H•(X,Pχ) =H•(B,Rq∗(Pχ)) =H•(B,Rq∗(Lϕ χ)⊗Q[dim(A)])
vanishes iff the restriction of the local systemLϕ χ to A = ker(q)⊆ X is
not trivial. Indeed, if this restriction is non-trivial, then by base change one
checks thatRq∗(Lϕ χ) =0 and hence a fortioriH•(X,Pχ) =0. On the other
hand, if this restriction is trivial, thenLϕ χ = q∗(Lψ) for some characterψ
and thenH•(X,Pχ) =H•(A,C)⊗H•(B,Qψ)[dim(A)] is non-zero since the
Euler characteristic ofQψ is not zero. □
For completeness we include the following two elementary lemmas
about characteristic cycles that have been used, in the case of simple abelian
varieties, in the proof of proposition 1.6.
