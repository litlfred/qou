---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-035-123-polar-decomposition
section_title: "Polar Decomposition"
section_number: 12.3
pages: 88-90
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Polar Decomposition
Theorem 12.3.1. Let A : H →K be a closed, densely deﬁned operator.
Then:
88
(i) A∗A and AA∗are positive self-adjoint operators (hence (A∗A)1/2 and
(AA∗)1/2 exist).
(ii) There exists a partial isometry with initial space Range(A∗A)1/2 and
ﬁnal space Range(A) and
A = v(A∗A)1/2.
(iii) If A = uB for some positive B and partial isometry v with initial space
Range(B) then u = v and B = (A∗A)1/2.
(iv) In addition A = (AA∗)1/2v.
Proof.
(i) Since Γ(A) is closed, it is a Hilbert space. Let P : Γ(A) →H be
projection onto the ﬁrst component. Since A is an operator Ker(P) =
{0} and hence Range(P ∗) is dense in Γ(A) (so PP ∗H is a core for A).
Let ξ ∈H, P ∗ξ = (η, Aη). Then, for all σ ∈D(A),
< ξ, σ >=< P ∗ξ, (σ, Aσ) >=< η, σ > + < Aη, Aσ >
⇒
< ξ −η, σ >=< Aη, Aσ >
⇒
Aη ∈D(A∗) and A∗Aη = ξ −η.
Thus D(A∗A) ⊃PP ∗H which is a core for A. In addition Range(A∗A+
1) = H.
It is easy to see that A∗A is symmetric, so A∗A + 1 ⊂(A∗A + 1)∗.
Let ξ ∈D((A∗A + 1)∗).
Since Range(A∗A + 1) = H there exists
˜ξ ∈D(A∗A + 1) with (A∗A + 1)∗ξ = (A∗A + 1)˜ξ(= (A∗A + 1)∗˜ξ).
Ker((A∗A + 1)∗) = {0} because Range(A∗A + 1) = H, and hence
ξ = ˜ξ ∈D(A∗A+1). Thus (A∗A+1)∗= A∗A+1 and so (A∗A)∗= A∗A.
Finally, for ξ ∈D(A∗A), < A∗Aξ, ξ >=< Aξ, Aξ >≥0 so A∗A is
positive, i.e. σ(A∗A) ⊂[0, ∞) (just use the Spectral Theorem).
(ii) As we noted above, D(A∗A) is a core for A. D(A∗A) is also a core for
|A| = (A∗A)1/2 (use spectral theory). Thus AD(A∗A) = RangeA and
|A|D(A∗A) = Range|A|. Note that for ξ ∈D(A∗A),
|||A|ξ||2 =< A∗Aξ, ξ >=< Aξ, Aξ >= ||Aξ||2,
so that the map v : |A|ξ 7→Aξ, ξ ∈D(A∗A), extends to a partial
isometry with initial space |A|D(A∗A) = Range|A| and ﬁnal space
AD(A∗A) = RangeA.
89
For ξ ∈D(|A|) take ξn ∈D(A∗A) with (ξn, |A|ξn) →(ξ, |A|ξ). Then
Aξn = v|A|ξn →v|A|ξ and, as A is closed, ξ ∈D(A) and Aξ = v|A|ξ.
For ξ ∈D(A) take ξn ∈D(A∗A) with (ξn, Aξn) →(ξ, Aξ). Then
|A|ξn = v∗v|A|ξn = v∗Aξn →v∗Aξ.
Since |A| is closed, ξ ∈D(|A|).
Hence D(A) = D(|A|) and A = v|A|.
(iii) If A = uB then A∗= B∗u∗= Bu∗. A∗A = Bu∗uB = B2 since u∗u is
projection onto Range(B). By uniqueness of the positive square root
of a positive operator (Exercise 12.3.3), (A∗A)1/2 = B. Thus the initial
space of u is Range(|A|) and u|A| = A = v|A| so u = v.
(iv) A = v(A∗A)1/2 so A∗= (A∗A)1/2v∗and hence AA∗= v(A∗A)1/2(A∗A)1/2v∗=
v(A∗A)v∗(Exercise 12.3.3). Thus v implements the unitary equivalence
of AA∗|Range(A) and A∗A|Range(A∗). Hence (AA∗)1/2 = v(A∗A)1/2v∗and
then A = v(A∗A)1/2 = (AA∗)1/2v.
Remark 12.3.2. Note that it was very important in (i) to establish that
D(A∗A) contained a core for A and hence was dense. It was not clear a
priori that D(A∗A) contained any elements other than 0.
Exercise 12.3.3.
(i) Let T be a positive operator. Show that T 1/2T 1/2 = T.
(ii) Show that a positive operator has a unique positive square-root.
12.4
