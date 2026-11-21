---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-013-61-r-matrices-of-diagonal-type
section_title: "R-matrices of diagonal type"
section_number: 6.1
pages: 30-32
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
R-matrices of diagonal type
As a simple class of examples which exist in any dimension, we consider involutive
R-matrices of diagonal type. An R-matrix R ∈R0 is said to be diagonal if it is of the
form R = DF, with F the ﬂip, and for some orthonormal basis {ei}i of V , the matrix
D ∈End(V ⊗V ) is diagonal in the corresponding tensor basis, i.e.
D(ei ⊗ej) = λij ei ⊗ej ,
i, j = 1, . . . , d ,
(6.1)
where λij ∈C. It is easy to check that such R solve the Yang-Baxter equation. An
R-matrix is said to be of diagonal type if it is equivalent to a diagonal one.
The R-matrix R = DF, R(ei ⊗ej) = λji ej ⊗ei, is unitary and involutive if and
only if
|λij| = 1 ,
λji = λ−1
ij ,
i, j = 1, . . . , d.
(6.2)
30
In particular, we have λii = ±1 for each i ∈{1, . . . , d}, and we introduce the parameter
ℓ∈{0, . . . , d} as the number of λii’s that are equal to +1. This parameter is uniquely
ﬁxed by the rank r of R, which is deﬁned as the multiplicity of the eigenvalue +1 of
R. In fact, the trace of R is
2ℓ−d =
d
X
i=1
λii = Tr(R) = 2r −d2 .
(6.3)
As ℓranges over {0, . . . , d}, the rank r ranges over
1
2d(d −1) ≤r ≤1
2d(d + 1) .
(6.4)
Thus diagonal involutive R-matrices of dimension d and rank r exist if and only if
(6.4) is satisﬁed.
Proposition 6.1.
i) Let R ∈R0 be of diagonal type, with dimension d, rank r, and ℓ:= r−1
2d(d−1).
Then
R ∼
ℓ
⊞
i=1
11 ⊞
d−ℓ
⊞
j=1
(−11) ,
(6.5)
and the non-vanishing Thoma parameters of R are
α1 = α2 = . . . = αℓ= β1 = . . . = βd−ℓ= d−1.
(6.6)
ii) Any two involutive R-matrices of diagonal type with the same dimension and
rank are equivalent.
Proof. i) In the basis deﬁning D, one has
⟨ei, ptr(R) ej⟩=
X
k
⟨ei ⊗ek, D ek ⊗ej⟩= λii δij,
which shows ptr(R) = idCℓ⊕(−idCd−ℓ). The claim now follows from Thm. 3.4 ii) and
Thm. 4.8 ii).
ii) The character depends only on d and ℓ, and the rank r determines ℓuniquely.
In terms of diagrams, diagonal R-matrices have the form

,

,
(6.7)
with ℓboxes in the left and d−ℓboxes in the right column. Yang-Baxter characters of
diagonal R-matrices play a signiﬁcant role in the analysis of the statistics of superse-
lection sectors in quantum ﬁeld theory [46, Prop. 6.10]. They also feature prominently
in the context of tensor categories as the skew-invertible unitary R-matrices [18, 2].
31
