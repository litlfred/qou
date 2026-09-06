---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-033-42-the-standard-triangle-of-a-strict-morphism
section_title: "The Standard Triangle of a Strict Morphism"
section_number: 4.2
pages: 82-83
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
abelian category M and a DG ringA. Here is the cone construction inC(A, M), as
it looks using the operatort.
Deﬁnition 4.2.1.Letφ:M→N be a strict morphism inC(A, M). Thestandard
cone ofφis the objectCone(φ)∈C(A, M)deﬁned as follows. As a gradedA-module
in M we let
Cone(φ) :=N⊕T(M).
The diﬀerentialdCone is this: if we express the graded module as a column
Cone(φ) =
N
T(M)

,
then dCone is left multiplication by the matrix
dCone :=
dN φ◦t−1
M
0 d T(M)

of degree 1 morphisms of gradedA-modules in M.
In other words, the morphism di
Cone : Cone(φ)i →Cone(φ)i+1 is di
Cone =
di
N + di
T(M) +φi+1◦t−1
M , whereφi+1◦t−1
M is the composed morphismT(M)i t−1
M
−−→
Mi+1 φi+i
−−−→Ni+1.
In the situation of Deﬁnition 4.2.1, let us denote by
(4.2.2) eφ:N→N⊕T(M)
the embedding, and by
(4.2.3) pφ:N⊕T(M)→T(M)
the projection. Thus, as matrices we have
eφ=
idN
0

and pφ=
0 id T(M)

.
The standard cone ofφsits in the exact sequence
(4.2.4) 0→N
eφ
−→Cone(φ)
pφ
−→T(M)→0
in the abelian categoryCstr(A, M).
Deﬁnition 4.2.5.Let φ:M→N be a morphism inCstr(A, M). The diagram
M
φ
−→N
eφ
−−→Cone(φ)
pφ
−−→T(M)
in Cstr(A, M) is called thestandard triangleassociated toφ.
The cone construction is functorial, in the following sense.
Proposition 4.2.6. Let
M0
φ0 //
ψ

N0
χ

M1
φ1 //N1
be a commutative diagram inCstr(A, M). Then
(4.2.7)
(
χ,T(ψ)
{
: Cone(φ0)→Cone(φ1)
82
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is a morphism inCstr(A, M), and the diagram
M0
φ0 //
ψ

N0
eφ0 //
χ

Cone(φ0)
pφ0 //
(χ,T(ψ))

T(M0)
T(ψ)

M1
φ1 //N1
eφ1 // Cone(φ1)
pφ1 // T(M1)
in Cstr(A, M) is commutative.
Proof. This is a simple consequence of the deﬁnitions. □
