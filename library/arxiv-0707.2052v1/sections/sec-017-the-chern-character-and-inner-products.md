---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-017-the-chern-character-and-inner-products
section_title: "The Chern character and inner products."
section_number: null
pages: 24-25
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
One reading of the Hirzebruch-Riemann-Roch Theorem is that it says that
the usual Chern character map ch : K0→ H•(X) is a map of inner product
spaces when K0(X) is equipped with the Euler pairing (see below) and H•(X)
is equipped with the pairing ⟨x1, x2⟩ := ( x1 ∪ x2 ∪ tdX) ∩ [X]. It is shown
in [5] that the Hochschild homology Chern character compose d with the
Hochschild-Kostant-Rosenberg map IHKR gives the usual Chern character:
K0
ch−→ HH0(X)
IHKR
− − −→
⨁
p
Hp,p(X).
Here we show that the Hochschild homology Chern character is an inner-
product map when HH•(X) is equipped with the Mukai pairing.
First recall that the Euler pairing on K0(X) is deﬁned by
χ(E , F ) :=
∑
i
(− 1)i dim Exti
X(E , F ).
24
Theorem 14 (Semi-Hirzebruch-Riemann-Roch). The Chern character
ch : K0→ HH0(X)
is a map of inner-product spaces: in other words, for E , F ∈ D(X) we have
⟨ch(E ), ch(F )⟩M = χ(E , F ).
Proof. The ﬁrst thing to do is to get an interpretation of the Euler pa iring.
Considering the totality of Ext-groups Ext•(E , F ) as a graded vector space,
the Euler characteristic is just the graded dimension of Ext•(E , F ), which
is to say it is the trace of the identity map on Ext•(E , F ). Moreover, if
Rπ∗ : D(X)→ D(pt) is the derived functor coming from the map X→ pt,
then
Ext•(E , F ) ∼= H•(X, E ∨ ⊗ F ) ∼= Rπ∗(E ∨ ⊗ F )
and the latter is just the composition E ∨ ◦F , where E ∨ and F are considered
as kernels respectively X→ pt and pt→ X. Thus, using the invariance of
the Serre trace under the partial trace map,
χ(E , F ) = Tr(IdE ∨ ◦F ) = Tr

 F
X ptpt
E

 = Tr


F
ptpt
X
E


=
⟨
E , F
⟩
M
= ⟨ch(E ), ch(F )⟩M.
