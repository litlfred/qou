---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-087-57-jacobian-varieties-125
section_title: "Jacobian varieties 125"
section_number: 5.7
pages: 133-135
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
For partitionsα = (α1,α2, . . .) such that 2g−2≥ α1≥ α2≥···≥ 0, one
can deﬁne the Brill-Noether sheaf
pδα∈ Perv(X,C)
as the simple perverse sheaf corresponding to the irreducible representation
of Sl2g−2(C) whose highest weight is given by the conjugate partitionαt
in the basis of the weights deﬁned by the diagonal entries of matrices. For
instance, the singleton partitionsα = (α1) correspond to the fundamental
representations, and for these it has been shown in loc. cit. that
pδi∼= δWi and pδ2g−2−i∼= δ−Wi for 0 ≤ i≤ g−1,
where the second equality is due to the Riemann-Roch theorem. Now the
Tannakian formalism provides a means to decompose arbitrary convolution
products between these perverse intersection cohomology sheaves via the
combinatorial Littlewood-Richardson rule for the decomposition of tensor
products of irreducible representations ofSl2g−2(C), see [46, sect. 9.3.5]
and [106, sect. 5.4]. In the special case of fundamental representations this
gives the formula
pδm∗ pδn ∼= τm,n⊕
n⨁
i=0
pδ(m+i,n−i) for m≥ n,
where τm,n∈ Dbc (X,C) is a negligible sheaf complex in the sense that all
its perverse cohomology sheaves have Euler characteristic zero. In fact it
has been shown in lemma 27 of loc. cit. thatτm,n (and more generally any
negligible direct summand of a convolution of Brill-Noether sheaves) is a
direct sum of degree shifts ofδX = CX[g]. As an application we have the
following result concerning the difference morphism.
LEMMA 5.25. Let X=JC be the Jacobian variety of a non-hyperelliptic
smooth projective curve of even genus g=2n. Then over some Zariski-open
dense subset U⊂ X there exists an irreducible local system LU of complex
vector spaces such that
dn∗(CCn×Cn)|U∼= CU⊕LU.
Proof. A Bertini-type argument like the one in lemma 5.3 shows that
over some Zariski-open dense subsetU⊂ X the morphismdn restricts to a
ﬁnite ´etale cover. Furthermore, ifS denotes the singular locus ofWn, then
for dimension reasons the closed subset(S×Wn)∪(Wn×S)⊂Wn×Wn is
mapped under the difference morphism
gn : Wn×Wn−→X
to a proper closed subset ofX, so we can assume thatg−1n (U) is contained
in (Wn\S)×(Wn\S). The Riemann-Kempf singularity theorem [48, p. 348]
126 Chapter 5 – A family of surfaces
says that the Abel-Jacobi morphismfn :Cn−→Wn restricts over the smooth
locus to an isomorphism
f−1
n (Wn\S)
∼=−→Wn\S.
Putting everything together and using the commutative diagram
Cn×Cn
(fn,fn) //
dn
..
Wn×Wn
gn

  (−in,in) // X×X
a
ppX
for the closed embeddingin :Wn ↪→X, we therefore obtain by the deﬁnition
of convolution an isomorphism
dn∗(CCn×Cn[g])|U ∼= (δWn∗δ−Wn)|U.
To control the convolution on the right hand side, we use the formalism of
Brill-Noether sheaves. Recall thatδWn = pδn andδ−Wn = pδ3n−2, where the
second equality is due to the Riemann-Roch theorem. Hence we get from
the Littlewood-Richardson rule that
δWn∗δ−Wn
∼= pδn∗ pδ3n−2∼= τ⊕
n⨁
i=0
pδ3n−2+i,n−i
whereτ is a direct sum of degree shifts ofδX. In factτ = δX as one may see
from the above isomorphismdn∗(CCn×Cn[g])|U∼= (δWn∗δ−Wn)|U and from
the fact thatdn is generically ﬁnite. Therefore our claim will follow for the
cohomology sheaf
LU = H−g(pδ3n−2,n)|U,
provided that for alli > 0 the perverse sheavespδ3n−2+i,n−i are supported
on a proper closed subset ofX. But this is indeed the case because by the
Littlewood-Richardson rule the perverse sheaf
n⨁
i=1
pδ3n−2+i,n−i∼= pδn−1∗ pδ2g−(n−1)∼= δWn−1∗δ−Wn−1
has the supportdn−1(Cn−1×Cn−1)⊂ X of dimension 2(n−1) < g. □
Proof of part (b) in proposition 5.24. For this we again use Brill-Noether
sheaves. The perverse sheafδΘ = δW3 = pδ3 corresponds by deﬁnition to
the third fundamental representation of the Tannaka groupSl6(C). One can
check that the alternating square of this representation decomposes into two
irreducible pieces of highest weightαt for α = (4,2) and α = (6). Hence
it follows that
δ−∼= pδ4,2⊕ pδ6⊕τ
