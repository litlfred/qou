---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-019-3-twisted-hochschild-homology
section_title: "Twisted Hochschild homology"
section_number: 3
pages: 10-11
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
3.1. Deﬁnition. Let A be an algebra and let σ be an algebra automorphism. A
σ-twisted version of the standard cochain complex used to deﬁne cy clic cohomology
is deﬁned in [KMT, Section 2], and used to deﬁne σ-twisted cyclic and Hochschild
(co)homology; the notation is HC σ
∗ (A) and HH σ
∗ (A) in the case of the homology
groups, and analogously for the cohomology groups. As shown in [HK 1, Proposition
2.1], when σ is diagonalisable, as will be the case in the most of the examples of
particular interest to us, one has
HH σ
n (A) ∼= Hn(A, σA),(3.1.1)
where the right hand side denotes Hochschild homology with coeﬃcien ts in σA.
Deﬁnition. The Hochschild dimension of A is deﬁned to be
Hdim A = max{i | HH i(A) = Hi(A, A) ⁄= 0}.
The twisted Hochschild dimension of A is deﬁned to be
tHdim A = max {i | Hi(A, σA) ⁄= 0 for some automorphism σ of A}.
Remark. Ideally the twisted Hochschild dimension should be deﬁned in terms of
twisted Hochschild homology HH σ
n (A). Unfortunately our computation in later
sections uses knowledge of Hn(A, σA); and we don’t know in general when σ will
be diagonalisable. Further, it’s not immediately obvious whether Hn(A, σA) ⁄= 0 is
equivalent to HH σ
n (A) ⁄= 0 when σ is not diagonalisable. The above deﬁnition is
therefore chosen so as to ﬁnesse this uncertainty.
In Section 6 we will comment on the diagonalisability of the relevant aut omor-
phisms for particular classes of examples.
Of course, in some cases diagonalisability is automatic. The following lem ma is
a standard result of linear algebra.
Lemma. If σ has ﬁnite order and the characteristic of k is zero, then σ is diago-
nalisable.
NOETHERIAN HOPF ALGEBRAS 11
3.2. Ischebeck’s spectral sequence. We need the following special case of Is-
chebeck’s spectral sequence [Is, 1.8]. Let A be an algebra, let M be a left A-module
and N a right A-module. Suppose that AM has a resolution by ﬁnitely generated
projectives and that NA has ﬁnite injective dimension. Then Ischebeck’s spectral
sequence is a convergent spectral sequence of vector spaces
Ep,q
2 := Ext p
Aop(Ext−q
A (M, A), N) = ⇒ TorA
−p−q(N, M ).(3.2.1)
If N is an A-bimodule, then this is a sequence of left A-modules. In particular, if
A has ﬁnite injective dimension, then we obtain the double Ext-spectr al sequence
of left A-modules
Ep,q
2 := Ext p
Aop(Ext−q
A (M, A), A) = ⇒ Hp+q(M )(3.2.2)
where Hn(M ) =
{
0 n ⁄= 0
M n = 0 .
As an immediate application we record here the fact that, when A is a noetherian
Hopf algebra the (AS2) condition of Deﬁnition (1.2)(b) can be replac ed by a weaker
form, as follows:
Lemma. Let A be a noetherian Hopf algebra of injective dimension d. If Exti
A(k, A)
and Exti
Aop(k, A) are ﬁnite dimensional over k for all i and if Extd
A(k, A) ⁄= 0, then
A is AS-Gorenstein.
Proof. Suppose that the stated hypotheses on the Ext-groups hold. Us ing the
double Ext-spectral sequence, or following the proof of [BG1, The orem 1.13], one
shows that Ext i
A(M, A) = 0 and Ext i
Aop(N, A) = 0 for all i ⁄= d and all ﬁnite
dimensional left A-modules M and ﬁnite dimensional right A-modules N . By the
proof of [WZ2, Lemma 4.8] dim Ext d
A(M, A) = dim M ·dim Extd
A(k, A) for any ﬁnite
dimension left A-module M . Thus
dim Extd
A(Extd
Aop(k, A), A) = dim Ext d
Aop(k, A) · dim Extd
A(k, A).
By the double-Ext spectral sequence (3.2.2), Ext d
A(Extd
Aop(k, A), A) ∼= k. Hence
dim Extd
Aop(k, A) = dim Ext d
A(k, A) = 1 .
Thus we have proved (AS2). □
